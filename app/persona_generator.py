import os

def save_persona(username, persona):
    os.makedirs("output", exist_ok=True)
    file_path = f"output/output_{username}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"[✓] Persona saved to {file_path}")
