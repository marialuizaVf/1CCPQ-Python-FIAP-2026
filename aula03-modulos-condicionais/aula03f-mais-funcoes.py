#FUNÇÃO COM PARAMETRO SEM RETORNO

def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem-vinda!")

nome_digitado = input("Digite o seu nome:")
boas_vindas(nome_digitado)


#FUNÇÃO COM PARAMETRO COM RETORNO

def soma(num_a, num_b):
    soma= num_a + num_b
    return soma

resultado_soma = soma(1, 2)
print(resultado_soma)
