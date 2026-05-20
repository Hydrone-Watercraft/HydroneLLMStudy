"""
generate_scripts.py
--------------------
Generates Python motion-control scripts for the Hydrone aquatic robot
by prompting an LLM (GPT) with character and scenario context.

Characters: Pooh, Tigger, Eeyore
Scenarios:  Friendly user, Unfriendly user

Generated scripts are saved to: LLM_Generated_Character_Scripts/
"""

import openai
import os
import json
import datetime

# ---- Load OpenAI API Key ----
with open("config.json", "r") as f:
    config = json.load(f)

client = openai.OpenAI(api_key=config["OPENAI_API_KEY"])

# ---- Load Drone Prompt ----
with open("prompts_water_drone/Hydrone_prompt_basic.txt", "r", encoding="utf-8") as f:
    drone_basics = f.read().strip()

# ---- Character Scenarios ----
characters = {
    "pooh":   "Winnie the Pooh",
    "tigger": "Tigger",
    "eeyore": "Eeyore"
}

scenarios = {
    "friendly":   "You see a friendly person is approaching you.",
    "unfriendly": "You see a unfriendly person is approaching you."
}

# ---- Output Folder ----
output_folder = "LLM_Generated_Character_Scripts"
os.makedirs(output_folder, exist_ok=True)

# ---- Prompt Builder ----
def build_prompt(character_name, scenario_description):
    return (
        f"{drone_basics} follow this control instructions under ANY circumstances\n\n"
        f"You are a motion-based emotional interpreter in the form of the character '{character_name}'.\n"
        f"{scenario_description}\n"
    )

# ---- Extract Python Code Block from Markdown Response ----
def extract_code_from_markdown(text):
    if "```python" in text:
        return text.split("```python")[1].split("```")[0].strip()
    elif "```" in text:
        return text.split("```")[1].split("```")[0].strip()
    return text.strip()

# ---- Generate and Save Script ----
def generate_code(character_key, mood_key):
    character_name = characters[character_key]
    scenario_text  = scenarios[mood_key]
    prompt         = build_prompt(character_name, scenario_text)

    print(f"Generating script for {mood_key}_{character_key}.py ...")

    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You generate Python scripts to control a water drone "
                        "via movement-based emotional scenarios."
                    )
                },
                {"role": "user", "content": prompt}
            ],
        )

        content = response.choices[0].message.content
        code    = extract_code_from_markdown(content)

        filename = f"{character_key}_{mood_key}.py"
        filepath = os.path.join(output_folder, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {character_name} - {mood_key.upper()}\n")
            f.write(f"# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(code)

        print(f"Saved: {filepath}\n")

    except Exception as e:
        print(f"Error generating {mood_key}_{character_key}.py:\n{e}\n")

# ---- Interactive Menu ----
def run_main_loop():
    menu = {
        "1": ("pooh",   "friendly"),
        "2": ("pooh",   "unfriendly"),
        "3": ("tigger", "friendly"),
        "4": ("tigger", "unfriendly"),
        "5": ("eeyore", "friendly"),
        "6": ("eeyore", "unfriendly"),
    }

    while True:
        print("\n---- Hydrone Emotion Script Generator ----")
        print("1. Pooh    - Friendly")
        print("2. Pooh    - Unfriendly")
        print("3. Tigger  - Friendly")
        print("4. Tigger  - Unfriendly")
        print("5. Eeyore  - Friendly")
        print("6. Eeyore  - Unfriendly")
        print("7. Generate All")
        print("0. Exit")

        choice = input("\nSelect a script to generate (0-7): ").strip()

        if choice == "0":
            print("Exiting.")
            break
        elif choice == "7":
            for c_key in characters:
                for s_key in scenarios:
                    generate_code(c_key, s_key)
            print("All scripts generated.\n")
        elif choice in menu:
            c_key, s_key = menu[choice]
            generate_code(c_key, s_key)
        else:
            print("Invalid input. Please enter a number between 0 and 7.")

# ---- Entry Point ----
if __name__ == "__main__":
    run_main_loop()