
#gerador de cores e numeros python3
import random

# Função para gerar uma cor aleatória em formato hexadecimal
def random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

# Função para gerar números de 1 a 9 de forma aleatória
def random_number():
    number = random.randint(1, 9)
    return number

# Loop para gerar 10 pares de cor aleatória e número aleatório
for _ in range(10):
    color = random_color()
    number = random_number()
    print(f"Cor: {color}, Número: {number}")
