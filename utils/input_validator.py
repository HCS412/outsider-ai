# utils/input_validator.py

def validate_prompt(prompt: str, max_length: int = 1000):
    if not prompt or not prompt.strip():
        raise ValueError("Prompt is empty.")
    if len(prompt) > max_length:
        raise ValueError(f"Prompt exceeds maximum length of {max_length} characters.")
