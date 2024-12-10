#Vamos alterar a funcao fib1 colocando os casos de base:
#0, 1, 1, 2, 3, 5, 8, 13


def conta_chamadas(func):

    def wrapper(*args, **kwargs):
        wrapper.chamadas +=1
        return func(*args, **kwargs)
    wrapper.chamadas = 0
    return wrapper

@conta_chamadas
def fib2(n: int) -> int:
    if n<2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)
    
if __name__=="__main__":
    
    print(fib2(20))
    print("qntd de chamadas [fib(20)]:", fib2.chamadas)

    #print(fib2(50))
    #esta instrucao nunca acaba, pois usando recursao a arvore cresce exponencialmente
    #para fib2(20) temos mais de 20 mil chamadas recursivas.
    #como melhorar isto?