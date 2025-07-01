# ai_alchemy.py

import time
from datetime import datetime
from typing import Dict

import openai

from utils.config_loader import load_config
from utils.error_handler import call_openai_with_retry
from utils.input_validator import validate_prompt
from utils.logger import print_section, log_error
from utils.prompt_builder import (
    load_principles,
    build_initial_prompt,
    build_critique_prompt,
    build_revise_prompt,
    build_reflection_prompt
)

# ----------------------------------------
# 🔧 Load configuration
# ----------------------------------------
config = load_config()

# Set OpenAI key + config
openai.api_key = config["openai"]["api_key"]
MODEL = config["openai"]["model"]
TEMP = config["openai"]["temperature"]
MAX_TOKENS = config["openai"]["max_tokens"]
TIMEOUT = config["openai"].get("timeout", 20)

# ----------------------------------------
# 🧠 Core Pipeline Functions
# ----------------------------------------

def generate_initial_response(user_prompt: str) -> str:
    prompt = build_initial_prompt(user_prompt)
    return call_openai_with_retry(prompt, MODEL, TEMP, MAX_TOKENS, TIMEOUT)

def critique_response(initial_response: str, principles: list[str]) -> str:
    prompt = build_critique_prompt(initial_response, principles)
    return call_openai_with_retry(prompt, MODEL, TEMP, MAX_TOKENS, TIMEOUT)

def revise_response(original: str, critique: str) -> str:
    prompt = build_revise_prompt(original, critique)
    return call_openai_with_retry(prompt, MODEL, TEMP, MAX_TOKENS, TIMEOUT)

def reflect_on_transformation(original: str, revised: str) -> str:
    prompt = build_reflection_prompt(original, revised)
    return call_openai_with_retry(prompt, MODEL, TEMP, MAX_TOKENS, TIMEOUT)

# ----------------------------------------
# 🔁 Full Chain Runner
# ----------------------------------------

def run_full_chain(user_prompt: str) -> Dict[str, str]:
    try:
        validate_prompt(user_prompt, config["run"]["max_prompt_length"])
    except ValueError as e:
        log_error(f"[INPUT ERROR] {e}")
        return {}

    print_section("🧠 Original Prompt")
    print(user_prompt)

    principles = load_principles(config["principles"]["path"])

    print_section("🔹 Step 1: Generating Initial Response")
    start = time.time()
    initial = generate_initial_response(user_prompt)
    print(initial)
    print(f"⏱️ Time: {round(time.time() - start, 2)}s")

    print_section("🔍 Step 2: Critiquing with Outsider Principles")
    start = time.time()
    critique = critique_response(initial, principles)
    print(critique)
    print(f"⏱️ Time: {round(time.time() - start, 2)}s")

    print_section("🔧 Step 3: Revising Based on Critique")
    start = time.time()
    revised = revise_response(initial, critique)
    print(revised)
    print(f"⏱️ Time: {round(time.time() - start, 2)}s")

    print_section("🪞 Step 4: Reflecting on the Transformation")
    start = time.time()
    reflection = reflect_on_transformation(initial, revised)
    print(reflection)
    print(f"⏱️ Time: {round(time.time() - start, 2)}s")

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "initial": initial,
        "critique": critique,
        "revised": revised,
        "reflection": reflection
    }
