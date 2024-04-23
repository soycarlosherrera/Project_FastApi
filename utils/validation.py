
import re #Para manejo de expresiones regulares
from datetime import datetime


def validate_phone_number(phone_number: str) -> str:
    phone_pattern = r'\+573\d{9}'  # Patrón para validar el formato de número de teléfono
    if not re.fullmatch(phone_pattern, phone_number):
        raise ValueError("El número de teléfono no cumple con el formato +573XXXXXXXXX")
    return phone_number

def validate_email(email: str) -> str:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Patrón para validar direcciones de correo electrónico
    if not re.fullmatch(email_pattern, email):
        raise ValueError("La dirección de correo electrónico no es válida")
    return email

def validate_date(date_str: str) -> str:
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise ValueError("Formato de fecha inválido. Use el formato YYYY-MM-DD")