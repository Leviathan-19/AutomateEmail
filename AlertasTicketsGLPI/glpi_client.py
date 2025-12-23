import requests
from datetime import datetime

from config import GLPI_BASE_URL, USER_TOKEN, HEADERS_BASE

# InitSession Endpoint
def init_session():
    url = f"{GLPI_BASE_URL}/initSession"
    params = {
        "user_token": USER_TOKEN
    }

    response = requests.get(
        url,
        headers=HEADERS_BASE,
        params=params,
        timeout=10
    )

    response.raise_for_status()
    data = response.json()

    return data["session_token"]
#Tickets Endpoint

def get_today_tickets(session_token):
    url = f"{GLPI_BASE_URL}/Ticket"

    today = datetime.now().strftime("%Y-%m-%d")

    headers = {
        **HEADERS_BASE,
        "Session-Token": session_token
    }

    params = {
    "searchText[entities_id]": 4,
    "searchText[date_creation]": today,
    "expand_dropdowns": "true"
    }


    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()
    return response.json()
