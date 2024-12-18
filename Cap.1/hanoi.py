"""
Neste exemplo, faremos a implementação do problema das torres de Hanoi
-Utilizaremos uma pilha para modelar as torres
-Uma pilha em python pode ser implementada com lista
"""

from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self):
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self)->T:
        return self._container.pop()
    
    def __repr__(self)->str:
        return repr(self._container)
    

num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs+1):
    tower_a.push(i)

"""
Uma solução é usarmos um caso base: quando movemos apenas um disco e um caso recursivo: quando movemos dois discos.
Podemos montar os discos da seguinte forma:
1- Disco menor move-se para torre C(temporária) e o disco médio para a torre B
2- Em seguida, movemos o disco menor para a torre B e, assim, fizemos o caso recursivo
3- Move-se o disco maior para a torre C
4-Usa-se a mesma ideia aplicada nos passos 1 e 2: Move-se o disco menor para uma torre temporária, neste caso, a torre A e
move-se o disco médio para a torre que queremos, torre C, e por fim movemos o disco menor para a torre que queremos(torre C)
Generalizando, temos:

1- Mover os n-1 discos de cima da torre A para a torre B(temp), usando C como intermediária
2- Mover o único disco que está mais embaixo, de A para C.
3- Mover os n-1 discos da torre B para a torre C usando A como intermediária
"""

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int)-> None:

    if n == 1:#caso base
        end.push(begin.pop())

    else:
        hanoi(begin, temp, end, n-1)#1
        hanoi(begin, end, temp, 1)#2
        hanoi(temp, end, begin, n-1)#3

if __name__=="__main__":

    print(tower_a, tower_b, tower_c, sep='\n')
    print()
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a, tower_b, tower_c, sep='\n')

    