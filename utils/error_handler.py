# utils/error_handler.py

import time
import openai
from openai.error import RateLimitError, Timeout, APIError, AuthenticationError, InvalidRequestError
from utils.logger import log_error

def call_openai_with_retry(prompt, model, temperature, max_tokens, timeout, retries=3, backoff_factor=2):
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout=timeout,
                messages=[
                    {"role": "system", "content": "You are a thoughtful, philosophical AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message["content"].strip()
        except (RateLimitError, Timeout, APIError) as e:
            log_error(f"[TRANSIENT ERROR] {type(e).__name__} — retrying ({attempt+1}/{retries})")
            time.sleep(backoff_factor ** attempt)
        except (AuthenticationError, InvalidRequestError) as e:
            log_error(f"[FATAL ERROR] {type(e).__name__}: {e}")
            break
        except Exception as e:
            log_error(f"[UNKNOWN ERROR] {e}")
            break
    return "[ERROR] Failed after retries."
