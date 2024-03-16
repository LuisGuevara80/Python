# and, or y not
# and todas verdades para que sea verdadera, con una falsa será falsa
# or  una verdadera para que el resultado final sea verdadero.
# not convierte false a true y viceversa

resultado_final = True and True and 100 > 20
print(resultado_final)

resultado_final2 = True or True or 100 < 20
print(resultado_final2)

resultado_final3 = True and ( False or 50 > 10) 
print(resultado_final3)

resultado_final4 = not False
print(resultado_final4)