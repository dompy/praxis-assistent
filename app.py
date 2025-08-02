import streamlit as st
import json
import requests
from jinja2 import Template

# Streamlit-Seitenkonfiguration
st.set_page_config(page_title="Zuweisungsgenerator", layout="centered")

st.title("🩺 Automatische Zuweisung")
st.markdown("Lade eine Patientenakte im JSON-Format hoch, wähle einen Prompt und erhalte automatisch ein Zuweisungsschreiben.")

# JSON-Datei hochladen
uploaded_file = st.file_uploader("🔍 Patientendatei (JSON) hochladen", type=["json"])

if uploaded_file:
    data = json.load(uploaded_file)
    st.success("Patientendaten geladen.")

    # Prompt-Vorlage laden
    with open("prompts/zuweisung.txt", "r") as file:
        prompt_template = Template(file.read())

    # Prompt ausfüllen
    filled_prompt = prompt_template.render(
        verlauf=data.get("verlauf", ""),
        diagnosen="\n".join(data.get("diagnosen", [])),
        labor="\n".join(f"{k}: {v}" for k, v in data.get("labor", {}).items()),
        ziel=data.get("ziel", "")
    )

    st.subheader("📨 Generierter Prompt")
    st.code(filled_prompt, language="markdown")

    if st.button("🧠 Anfrage an lokales LLM (mistral) senden"):
        try:
            response = requests.post(
                "http://127.0.0.1:11434/api/generate",  # ✅ funktioniert auf RunPod zuverlässig
                json={"model": "mistral", "prompt": filled_prompt, "stream": True},
                stream=True
            )

            result = ""
            for line in response.iter_lines():
                if line:
                    part = json.loads(line.decode("utf-8"))
                    result += part.get("response", "")

            st.subheader("✉️ Zuweisungsvorschlag")
            st.text_area("Antwort vom Modell", value=result, height=300)

        except Exception as e:
            st.error(f"Fehler bei der Anfrage an das lokale Modell: {e}")