def juego_del_ahorcado():
  palabra_elegida = input()
  letras_adivinadas = []
  intentos_restantes = 6
  muneco = ""

  while True:
    salida = ""
    for letra in palabra_elegida:
      if letra in letras_adivinadas:
        salida += letra
      else:
        salida += "_"

    if salida == palabra_elegida:
      print("Felicidades, has adivinado la palabra: " + palabra_elegida)
      break

    print("Intentos restantes: " + str(intentos_restantes))
    print("Adivina una letra:")
    print(salida +"\n\n")

    letra = input()
    if letra in palabra_elegida:
      letras_adivinadas.append(letra)
    else:
      intentos_restantes -= 1
    
    if intentos_restantes == 5:
        muneco += "O"
        print(muneco)
    if intentos_restantes == 4:
        muneco = "O-"
        print(muneco)
    if intentos_restantes == 3:
        muneco = "O-<"
        print(muneco)
    if intentos_restantes == 2:
        muneco = "O-<-"
        print(muneco)
    if intentos_restantes == 1:
        muneco = "O-<-<"
        print(muneco)
    

    if intentos_restantes == 0:
      print("Lo siento, has perdido. La palabra era: " + palabra_elegida)
      break

print("Bienvenido al juego del ahorcado")
juego_del_ahorcado()
