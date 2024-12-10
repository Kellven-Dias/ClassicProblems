#Sequencia de fibonacci = 0, 1, 1, 2, 3, 5, 8, ...
#fib(n) = fib(n-1) + fib(n-2)
#casos base = 0 e 1

"""
def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)

if __name__=="__main__":
    print(fib1(5))
"""
#esta primeira tentiva retorna o erro "maximum recursion depth exceeded"
#pois a fib1() executa indefinidamente.
#em funcoes recursivas, um caso de base serve como condicao de parada
#imagine os ramos da arvore sendo formados ao executar fib1
#se n houver nós folhas(casos de base) a funcao executa indefinidamente

