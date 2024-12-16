#De acordo com a formula de Leibniz para o calculo de pi, temos:
#pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - ...
#Podemos realizar a conversão mecânica da formula para um funcao em python a fim de calcular o valor de pi

def calculate_pi(n_terms: int)-> float:

    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for _ in range(n_terms):
        pi += (numerator/denominator) * operation
        denominator += 2
        operation *= -1
    
    return pi

if __name__=="__main__":
    print(calculate_pi(1000)) #Quanto maior o n_terms, maior a precisão