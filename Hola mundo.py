from datetime import datetime

nombre = input("¿Cómo te llamas? ")
momento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print(f"Hola, {nombre}! Bienvenido al mundo de Python.")
print(f"Fecha y hora actuales: {momento}")


