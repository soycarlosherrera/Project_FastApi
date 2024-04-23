from datetime import datetime

def calcular_edad(fecha_nacimiento):
    # Obtener la fecha actual
    today = datetime.now().date()

    # Calcular la edad
    age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

    return age