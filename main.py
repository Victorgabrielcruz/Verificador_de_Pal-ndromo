def menu():
    while True:
        op = input("Deseja continuar :\n [1]Sim\n [2]Não\n")
        if op == "1":
            return True
        elif op == "2":
            return False

def entrada():
    print("------------------------\n")
    frase = input("Insira a frase que deseja verificar: ")
    return frase
def comparador(frase):
    frase_1 = ""
    for caractere in frase[::-1]:
        frase_1 += caractere
    if frase_1 == frase:
        print(frase_1)
        return True
    else:
        print(frase_1)
        return False
op = True
while op:
    frase = entrada()
    resultado = comparador(frase)
    if resultado:
        print("Esta frase é um Palíndromo")
    else:
        print("Esta frase não é um Palíndromo")
    op = menu()