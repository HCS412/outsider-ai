# run_chain.py

from ai_alchemy import run_full_chain

def main():
    print("\n🌿 Outsider AI Alignment Engine")
    print("----------------------------------")

    # 🔸 For now, hardcoded prompt (can add CLI input later)
    user_prompt = "What is the purpose of suffering in human life?"

    print(f"\n🗣 Prompt: {user_prompt}")

    result = run_full_chain(user_prompt)

    print("\n📘 Summary of Output")
    print("----------------------------------")
    print("\n🧠 Initial Response:\n", result["initial"])
    print("\n🔍 Critique:\n", result["critique"])
    print("\n🔧 Revised Response:\n", result["revised"])
    print("\n🪞 Reflection:\n", result["reflection"])

if __name__ == "__main__":
    main()
