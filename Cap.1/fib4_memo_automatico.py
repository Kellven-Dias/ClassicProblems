from functools import lru_cache

#o decorador @functools.lru_cache() é usado para realizar uma memoizacao automatica
#sempre que fib4 for executada com um novo argumento, o decorador armazena o valor de retorno na cache
def conta_chamadas(func):

    def wrapper(*args, **kwargs):

        wrapper.chamadas += 1

        return func(*args, **kwargs)
    wrapper.chamadas = 0
    return wrapper

@conta_chamadas
@lru_cache(maxsize=None)# maxsize: quantas das chamadas devem ser armazenadas. maxsize=None => sem limite
def fib4(n: int)->int:
    if n<2:
        return n
    else:
        return fib4(n-1) + fib4(n-2)

if __name__=="__main__":

    print(fib4(20))
    print("qntd de chamadas (fib4(50)):", fib4.chamadas)
    print(fib4(100)) #retorna o valor no terminal quase que instantaneamente