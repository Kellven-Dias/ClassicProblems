#memoização é a técnica de armazenar os valores já calculados
#dessa forma os valores calculados podem ser consultados e nao precisam ser calculados todas as vezes

#usaremos um dicionario para realizar esta tecnica
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1} #casos de base


def conta_chamadas(func):

    def wrapper(*args, **kwargs):

        wrapper.chamadas += 1

        return func(*args, **kwargs)
    wrapper.chamadas = 0
    return wrapper

@conta_chamadas
def fib3(n: int)->int:
    if n not in memo: #se n for um caso de base
        memo[n] = fib3(n-1) + fib3(n-2) #calcula e guarda o valor no dict
    return memo[n]


if __name__ == "__main__":
    fib3(20)
    print("qntd de chamadas fib3(20):", fib3.chamadas)
    fib3.chamadas = 0
    print(fib3(50))
    print("qntd de chamadas (fib3(50)):", fib3.chamadas)

    #Comparando fib2 com fib3 para o caso em que n=20 temos que
    #fib2 realizou mais de 20mil chamadas, enquanto fib3 utilizou apenas 39