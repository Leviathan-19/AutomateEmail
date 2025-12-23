import time
from glpi_client import init_session, get_today_tickets
from utils import load_read_tickets, save_read_tickets
from voice import speak
from utils import clean_glpi_text
from utils import reset_if_new_day

CHECK_INTERVAL = 180  #segundos  (3 minutos)


def build_ticket_speech(ticket):
    id_ticket = ticket.get("id", "Desconocido")
    solicitante = ticket.get("users_id_recipient", "Usuario no identificado")
    asunto = ticket.get("name", "Sin asunto")

    categoria = clean_glpi_text(ticket.get("itilcategories_id", ""))
    ubicacion = clean_glpi_text(ticket.get("locations_id", ""))
    fecha = clean_glpi_text(ticket.get("date", ""))
    return (
        f"Ticket nuevo entrante. "
        f"Numero de ticket: {id_ticket}. "
        f"Asunto: {asunto}. "
        f"Usuario solicitante: {solicitante}. "
        f"Categoría: {categoria}. "
        f"Ubicación: {ubicacion}."
        f"Fecha: {fecha}."
    )


def main():
    session_token = init_session()
    if reset_if_new_day():
        save_read_tickets(set())
        print("Nuevo día detectado, tickets reiniciados")
    read_tickets = load_read_tickets()

    print("Notificador de GLPI iniciado 🔊")

    while True:
        tickets = get_today_tickets(session_token)

        for ticket in tickets:
            ticket_id = ticket["id"]

            if ticket_id in read_tickets:
                continue  # ya fue leído

            texto = build_ticket_speech(ticket)
            print(texto)
            speak(texto)

            read_tickets.add(ticket_id)
            save_read_tickets(read_tickets)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
