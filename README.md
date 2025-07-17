# Praxis-Assistent

Ein lokal laufendes KI-Tool zur Unterstützung hausärztlicher Tätigkeiten – entwickelt für Schweizer Hausarztpraxen.

## Funktionen

- Automatische Erstellung von Zuweisungsschreiben (via LLM), zahlreiche Use Cases geplant
- Verarbeitung von Patientendaten im JSON-Format
- Promptgenerierung mit Jinja2
- Antwort über lokales LLM (Mistral, LLaMA2 etc.)

## Projektstruktur

| Datei             | Beschreibung                            |
|------------------|-----------------------------------------|
| `app.py`         | Streamlit-App zur Promptgenerierung     |
| `patient_001.json` | Beispiel-Patientendaten                |
| `zuweisung.txt`  | Prompt-Template                         |
| `requirements.txt` | Python-Abhängigkeiten                 |

## Starten der Anwendung

```bash
# 1. Virtuelle Umgebung aktivieren
source .venv/bin/activate

# 2. Abhängigkeiten installieren
pip install -r requirements.txt

# 3. Lokales Modell starten
ollama run mistral  # oder llama2:7b-chat

# 4. App starten
streamlit run app.py
