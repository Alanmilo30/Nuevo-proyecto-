from datetime import datetime
import random

nombre = input("¿Cómo te llamas? ")
momento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
numero_suerte = random.randint(1, 100)  # Número aleatorio entre 1 y 100

print(f"\nHola, {nombre}! Bienvenido al mundo de Python.")
print(f"Fecha y hora actuales: {momento}")
print(f"Tu nombre tiene {len(nombre)} caracteres.")
print(f"Tu número de la suerte para hoy es: {numero_suerte}")
print("¡Que tengas un excelente día, inge!")




