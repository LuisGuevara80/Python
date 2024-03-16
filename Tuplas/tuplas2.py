#            0         1         2       3        4
cursos = ("python", "Flask", "Django", "Rails", "MongoDB")


primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

sub_tupla = cursos[:3]
print(sub_tupla)


"""
primer_curso, segundo_curso, *_, ultimo_curso = cursos

print(primer_curso)
print(segundo_curso)
print(ultimo_curso)

"""
#Esta es mejor forma de hacerlo
