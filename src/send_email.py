import smtplib
from email.message import EmailMessage
import os

# Envía un correo electrónico con los reportes generados como adjuntos
def send_email():
    # Configuración del remitente (usar credenciales seguras en producción)
    sender = "@outlook.com"
    password = ""  # Contraseña de aplicación generada en Outlook
    receiver = ""  # Correo destino

    # Construcción del mensaje
    msg = EmailMessage()
    msg["Subject"] = "Reporte Automatizado de Ventas"
    msg["From"] = sender
    msg["To"] = receiver

    # Cuerpo del correo (mensaje profesional)
    msg.set_content(
        "Buen día,\n\n"
        "Se remiten los reportes generados automáticamente a partir del procesamiento de datos de e-commerce. "
        "El flujo implementado garantiza la limpieza, transformación y consolidación de la información para su análisis.\n\n"
        "Saludos cordiales."
    )

    # Lista de archivos a adjuntar
    files = [
        "data/clean/dataset_limpio.xlsx",
        "data/clean/resumen.xlsx"
    ]

    # Adjuntar archivos al correo
    for file in files:
        with open(file, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(file)

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )

    # Conexión al servidor SMTP de Outlook y envío del correo
    with smtplib.SMTP("smtp.office365.com", 587) as smtp:
        smtp.starttls()  # Inicia conexión segura
        print("Conectando...")
        smtp.login(sender, password)
        print("Logueado...")
        smtp.send_message(msg)
        print("Correo enviado correctamente")