import random

i = 1

class PersonajeA():
    nombreA = "Charizard"
    defensaA = random.uniform(100, 200)
    ataqueA = random.uniform(10, 20)
    pass

class PersonajeB():
    nombreB = "Kyogre"
    defensaB = random.uniform(100, 200)
    ataqueB = random.uniform(10, 20)
    pass

print("La defensa de ",PersonajeA.nombreA, "es",PersonajeA.defensaA, ",y su ataque",PersonajeA.ataqueA,"\n")
print("La defensa de ",PersonajeB.nombreB, "es",PersonajeB.defensaB, ",y su ataque",PersonajeB.ataqueB,"\n")
x = input("Pulsa enter para continuar")

turno = random.randint(1, 2)

while (PersonajeA.defensaA >= 0 and PersonajeB.defensaB > 0):
    print ("Turno",i,)
    
    if (turno == 1):
        print("Ataca",PersonajeA.nombreA,)
        PersonajeB.defensaB = PersonajeB.defensaB - PersonajeA.ataqueA
        print("La defensa de",PersonajeB.nombreB, "es", PersonajeB.defensaB)

    elif (turno == 2):
        print("Ataca",PersonajeB.nombreB,)
        PersonajeA.defensaA = PersonajeA.defensaA - PersonajeB.ataqueB
        print("La defensa de",PersonajeA.nombreA, "es", PersonajeA.defensaA)

    if (turno == 1):
        turno = 2
    elif (turno == 2):
        turno = 1

    x = input("Pulsa enter para continuar")
    i = i + 1
if (PersonajeA.defensaA > 0):
    print ("Ganador:",PersonajeA.nombreA,)

elif (PersonajeB.defensaB > 0):
    print ("Ganador:",PersonajeB.nombreB,)
