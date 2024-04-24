"""
2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
"""

def main() -> str:
      def pergunta() -> int:
        resposta = int(input('x -> '))
        return resposta

      def multipl(x):
        resultado = []
        for i in range(1, 10 + 1):
          multiplicacao = x * i
          resultado.append(multiplicacao)
        return resultado
      
      y = pergunta()
      resultado = multipl(y) 
      
      print(f'Tabuada do {y}')
      for r in resultado:
        print(f'{y} x {resultado.index(r) + 1} = {r}')
  
main()
