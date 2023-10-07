#Metodos e loop
#len - comprimento da variavel (conta os caracteres da variavel)
#lista ou array [1,2,3,4]
#type identifica o tipo de dado dentro da variavel

#len
# cidade = "Ottawa"
# print(len(cidade))
 
# #Type
# x = True
# print(type(x)) 
# x = 4.9
# print(type(x))

# #Transformar numero
# z = 45
# n = str(z)
# print (n,10)
# print(z+10)

#Transformar uma viariavel em lista []
# print()
# cidade = 'Gurulhos'
# print (cidade,'\n')
# frag = list(cidade)
# print(frag)

# #Tupla - É uma lista imultavel ()
# tr = tuple(frag)
# print(tr)

# #range ex. De 1 a 10. a cada 1
# num = range(1,10,1)
# print(num)
# for i in range(0,10,2):
#   print(i)

# for n in range(1,100,10):
#   print(n)

# #SUM
# lista =[1,3,5,8,11]
# soma = sum(lista)
# print('A soma é:', soma)

# #Minimo e maximo - Mostra o minimo e o maximo dentro de uma sequência.
# lista = [1,36,145]
# maxi = max(lista)
# print("Maior numero é:",maxi)

# lista = [1,36,145]
# mini = min(lista)
# print("Menor numero é:", mini)

# #sorted(): Retorna uma nova lista ordenada a partir dos elementos de uma sequência.
# lista = [1,8,5,2,4,3,6,9]
# lista2 = ['Z','B','A','E']
# organize = sorted(lista),sorted(lista2)
# print(lista,lista2)

                    ## EXERCÍCIOS:
## Exercício 1:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

# for pares in range(2,21,2):
#   print(pares)

## Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 em 5 a 50 e, em seguida, calcule e imprima a soma desses múltiplos.
# for mult in range(5,51,5):
#   print(mult)
# lista = [5,10,15,20,25,30,35,40,45,50]
# soma = sum(lista)
# print("A soma é:", soma)

# ## Exercício 3: Escreva um programa que use a função type() para verificar o tipo de uma variável.
# tpvar = "Gabriel"
# tipo = type(tpvar)
# print (tpvar,tipo)

## Exercício 4: Escreva um programa que use a função print() para imprimir uma mensagem de saudação personalizada, incluindo o nome do usuário.

# cumprimento = 'Seja Bem vindo!'
# nameuser = input("Digite seu usuário:")
# print(cumprimento," ",nameuser)

# ## Exercício 5: Escreva um programa que use a função range() para gerar os números ímpares de 1 a 10 e, em seguida, calcule e imprima a média desses números.

# for imp in range(1,10,2):
#   print(imp)
# lista = [1,3,5,7,9]
# imp = sum(lista)
# med = (imp /5)
# print("A soma é:", imp)
# print("A Média é:", med)

##############################

# palavra = "python"
# for program in palavra:
#   print(program)

# frutas = ['maça', "banana", "uva"]
# for i in frutas:
#    print (i)

#DICIONARIO
dados = {
'nome':'Gabriel',
'idade': '18',
'endereco': 'rua falcoes'
}
for i1,i2 in dados.items():
      print(f'{i1} : {i2}')

matriz =[[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1][0])
for i in matriz:
  for n in i:
    print(n)