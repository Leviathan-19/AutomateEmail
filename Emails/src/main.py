from csv_reader import leer_csv
from mailer import enviar_correo


# from mailer import enviar_correo

# enviar_correo(
#     destinatario="pasante.it@ituran.com.ec",
#     asunto="Prueba SMTP Gmail",
#     cuerpo="Correo enviado desde Python usando Gmail"
# )

RUTA_CSV = "../data/destinatarios.csv"
RUTA_TEMPLATE = "../templates/correo_base.txt"

def cargar_template():
    with open(RUTA_TEMPLATE, "r", encoding="utf-8") as f:
        return f.read()

def main():
    datos = leer_csv(RUTA_CSV)
    print(datos.columns)
    template = cargar_template()
    
    for _, fila in datos.iterrows():
        cuerpo = template.format(
            area=fila["area"],
            equipo=fila["equipo"],
            serial=fila["serial"]
        )

        enviar_correo(
            destinatario=fila["correo"],
            asunto="Notificación de equipo asignado",
            cuerpo=cuerpo
        )

if __name__ == "__main__":
    main()
