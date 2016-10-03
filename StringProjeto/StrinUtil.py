import string

def output(texto):
    print(texto)
def tamanho(texto):
    return len(texto)
def maiusculo(texto):
    textoMaiusculo = texto.upper()
    return textoMaiusculo
def minusculo(texto):
    textoMinusculo = texto.lower()
    return textoMinusculo
def encontrarLetra(letra, texto):
    aux = 0
    for i in texto.lower():
        if letra.lower() == i:
            aux = aux + 1
    if aux > 0:
        print("A letra aparece no texto.")

    print("A letra aparece",aux,"vezes no texto.")


