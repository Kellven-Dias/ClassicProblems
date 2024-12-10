#podemos utilizar uma abordagem iterativa tradicional para atacar o problema:

def fib5(n: int)-> int:

    if n == 0: return n
    count=0
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        count+=1
    return next, count

if __name__=="__main__":
    
    result, chamadas = fib5(20)
    print(result, chamadas, sep=";")

#Concluimos que a quantidade de passos para calcular fib(20) utilizando fib5 é igual a 19
#Superando, assim, todos os outros algoritmos
#Imensamente mais otimizado que utilizando recursao

    