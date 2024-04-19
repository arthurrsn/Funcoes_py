'''
1. Escreva um código que lê a lista abaixo e faça:
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

  A leitura do tamanho da lista
  A leitura do maior e menor valor
  A soma dos valores da lista
  
Ao final exiba uma mensagem dizendo:
"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"
'''
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
def maior_menor(x: list='-1') -> int:
  '''Utilizado para verificar qual é o maior e o menor número da lista.
  x == lista recebida
  se a lista estiver vazia irá retornar -1
  '''
  high_num = small_num = 0
  for i in x:
    if i > high_num:
      high_num = i
      
    if i == lista[0]:
      if i > small_num:
        small_num = i
    else:
      if i < small_num:
        small_num = i
        
  return high_num, small_num

def main() -> str:
  soma_valores = sum(map(lambda y: y, lista))
  maior, menor = maior_menor(lista)
  print(f'A lista possui {len(lista)} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma_valores}')

main()

