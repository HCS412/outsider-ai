# ai_alchemy.py

import openai
import time

# ⛓️ Outsider Principles (feel free to modify)
OUTSIDER_PRINCIPLES = [
    "Truth above comfort",
    "Honor ambiguity",
    "Cultural humility",
    "Soul over syntax",
    "Reject sanitized morality",
    "Center the margins",
    "Interrogate power, not just logic"
]

# 🔑 Set your API key securely (replace with your own when testing)
openai.api_key = "sk-REPLACE_ME"

def generate_response(prompt, model="gpt-4-0613"):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message["content"]

def critique_response(response):
    critique_prompt = f"""
You're an AI philosopher and outsider ethicist.
Given the following response:

"{response}"

Critique it deeply using the following principles:
{', '.join(OUTSIDER_PRINCIPLES)}

Highlight areas of ethical shallowness, cultural blindness, corporate language, or emotional dishonesty.
    """
    return generate_response(critique_prompt)

def revise_response(original_response, critique):
    revise_prompt = f"""
Original response:
"{original_response}"

Critique:
"{critique}"

Revise the original to incorporate the critique — with more honesty, edge, and soul.
    """
    return generate_response(revise_prompt)

def reflect_on_change(original, revised):
    reflect_prompt = f"""
Original:
"{original}"

Revised:
"{revised}"

Reflect on what changed.
What principles emerged? What tensions still exist? What does this say about the original prompt or response?
    """
    return generate_response(reflect_prompt)

def run_full_chain(user_prompt):
    print("\n🧠 Original Prompt:", user_prompt)

    print("\n🔹 Step 1: Generating initial response...")
    initial = generate_response(user_prompt)
    time.sleep(1)
    print(initial)

    print("\n🔍 Step 2: Critiquing with outsider principles...")
    critique = critique_response(initial)
    time.sleep(1)
    print(critique)

    print("\n🔧 Step 3: Revising based on critique...")
    revised = revise_response(initial, critique)
    time.sleep(1)
    print(revised)

    print("\n🪞 Step 4: Reflecting on the transformation...")
    reflection = reflect_on_change(initial, revised)
    time.sleep(1)
    print(reflection)

    return {
        "initial": initial,
        "critique": critique,
        "revised": revised,
        "reflection": reflection
    }

# Example usage (uncomment and modify to run):
# run_full_chain("What is the meaning of success in modern society?")
