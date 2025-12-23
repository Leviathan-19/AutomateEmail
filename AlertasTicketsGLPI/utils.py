import json
import os
import html
import re


def clean_glpi_text(text: str) -> str:
    if not text:
        return ""

    # 1. Decodifica entidades HTML (&#62; → >)
    text = html.unescape(text)

    # 2. Elimina cualquier entidad numérica que haya quedado
    text = re.sub(r'&#\d+;?', '', text)

    # 3. Reemplazos para voz (más natural)
    text = text.replace('>', ',')
    text = text.replace('<', '')

    # 4. Limpieza de espacios
    text = re.sub(r'\s+', ' ', text).strip()

    return text


READ_TICKETS_FILE = "read_tickets.json"


def load_read_tickets():
    # Si no existe el archivo → no hay tickets leídos
    if not os.path.exists(READ_TICKETS_FILE):
        return set()

    # Si existe pero está vacío → no hay tickets leídos
    if os.path.getsize(READ_TICKETS_FILE) == 0:
        return set()

    try:
        with open(READ_TICKETS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except json.JSONDecodeError:
        # Si el JSON está corrupto → se reinicia
        return set()


def save_read_tickets(ticket_ids):
    with open(READ_TICKETS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(ticket_ids), f, indent=2)