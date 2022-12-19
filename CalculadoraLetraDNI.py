def letra_dni(DNI):
    number = DNI % 23
    cadena = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra = cadena[number]
    return(letra)
