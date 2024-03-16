### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermedio/my_file.txt", "w+") # r+ leer y escribir # w+ Escribir, leer y sobreescribir si ya existe

txt_file.write(
    "Mi nombre es Luis\nMi apellido es Guevara\n18 años\nY mi lenguaje preferido es Python")

txt_file.write("\nAunque también me gusta Kotlin")

txt_file.close()

with open("Intermedio/my_file.txt", "a") as my_other_file1:  # El with asegura que una vez hecho esto se cierre el archivo. Y el as es para llamarlo de otra forma. el "a" permite que pueda escribir adentro del fichero.
    my_other_file1.write(" Y Swift\n")

with open("Intermedio/my_file.txt", "r+") as my_other_file1:  # El with asegura que una vez hecho esto se cierre el archivo. Y el as es para llamarlo de otra forma. el "r+" permite que lo pueda leer
    for line in my_other_file1.readlines():
        print(line)

# os.remove("Intermedio/my_file.txt")

# .json file


json_file = open("Intermedio/my_file.json", "w+")

json_test = {
    "name": "Luis",
    "surname": "Guevara",
    "age": 18,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://luis.dev"}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermedio/my_file.json", "r+") as my_other_file: # El with asegura que una vez hecho esto se cierre el archivo. Y el as es para llamarlo de otra forma. el "r+" permite que lo pueda leer
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermedio/my_file.json")) # Pase el diccionario del doc json a la variable json_dict.
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("Intermedio/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Luis", "Guevara", 18, "Python", "https://luis.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermedio/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)