from datetime import datetime

Tiempo = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(Tiempo)

"""
un timestamp es una marca temporal que registra la fecha y hora exacta de un evento en un sistema informático, 
lo cual aporta mayor precisión, orden y contexto a los registros de actividades.
"""

year_2024 = datetime(2024, 1, 1) # Esto es lo minimo para definir un año, año, mes y día

print_date(year_2024)



from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()   # Se puede colocar el today para tener la actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 10, 6)   # O se le puede dar valores.

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date =  date(current_date.year, current_date.month + 1, current_date.day) # Esta es una forma de modificar los datos
print(current_date.month)


#Para poder hacer estas operaciones de resta tienen que ser del mismo tipo.
diff = year_2024 - Tiempo
print(diff)
diff = year_2024.date() - current_date
print(diff)


from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)