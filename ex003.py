"""
Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
"""

def main() -> None:
    lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
    def filtro(x: list=['-1']) -> list:
      mult_3 = []
      for i in x:
         if (i % 3) == 0:
             mult_3.append(i)
      return mult_3
    
    print(filtro(lista))
    
      
if __name__ == '__main__':
    main()
