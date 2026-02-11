##mesclando todos los conceptos aprendidos
!pip install fpdf
proyecto = input("escriba el nombre del proyecto: ")
horas_estimadas = input("escriba las horas que va a dedicar al proyecto: ")
valor_hora = input("cual es el valor de la hora trabajada?: ")
plazo_estimado = input("cual es el plazo estimado para el proyecto: ")

print(proyecto)
print(horas_estimadas)
print(valor_hora)
print(plazo_estimado)

valor_total = int(horas_estimadas) * int(valor_hora)