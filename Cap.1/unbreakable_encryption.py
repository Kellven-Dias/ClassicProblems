"""
One-time Pad: forma de criptografar dados combinando-os com dados dummy aleatórios e nao significativos
-os dados originais so podem ser reconstituidos se tivermos os dados dummy e o produto da criptgrafia
-O resultado disso é um par de chaves: uma chave é o produto e a outra os dados dummy
-Somente com o par é possível descriptografar os dados originais

-Neste exemplo, criptografaremos uma str = sequencia de bytes Unicode UTF-8
-Podemos converter para esta sequencia de bytes Unicode UTF-8 utilizando o método encode()
-Similarmente, podemos converter a sequência em str usando o método decode() no tipo bytes

Critérios para os Dados Dummy: devem ter o mesmo tam dos dados originais, devem ser aletórios e totalmente secretos.

É possível gerar dados aleatórios? Para a maioria dos computadores: Não!
-Neste ex, usaremos a função geradora de dados pseudoaleatórios token_bytes() do módulo secrets

"""

from secrets import token_bytes
from typing import Tuple

def random_key(lenght: int)->int:
    #gera lenght bytes aleatórios
    tb: bytes = token_bytes(lenght)
    #converte esses bytes em uma cadeia de bits e a devolve como um int 
    return int.from_bytes(tb, "big")


#Esta funcao cria um int preenchido com "lenght" bytes aleatorios
#o metodo int.from_bytes é usado para converter de bytes para int.
#Por ex, o from_bytes receberá 7 bytes (7bytes * 8 bits = 56 bits) e os converterá para um inteiro de 56 bits
#Operacoes bit a bit podem ser executadas com melhor desempenho

#Para combinar os dados dummy com os dados originais usaremos um XOR
#XOR é True quando somente um dos operandos é verdadeiro
#0^1 = 1; 1^0= 1; 0^0=0 e 1^1=0
#Uma propriedade conveniente do XOR: A^B=C; C^B=A e C^A=B
#Portanto, para calcular o nosso produto, faremos um XOR de um int que representa os bytes da str original
#com um int gerado de forma aleatoria com o mesmo tamanho em bits

def encrypt(original: str)->Tuple[int, int]:

    original_bytes: bytes = original.encode() #converte a str para uma sequencia de bytes
    
    dummy: int = random_key(len(original_bytes))#dados dummy com mesmo tamanho da seq de bytes a ser criptografada

    original_key: int = int.from_bytes(original_bytes, "big")

    encrypted: int = original_key^dummy #XOR

    return dummy, encrypted

#NOTA: o metodo from_bytes() recebe dois parâmetros: o primeiro sao os bytes e o segundo é o endianness desses bytes("big")
#endianness se refere à ordem dos bytes: qual é o mais significativo e qual o menos significativo.
#neste caso, a ordem nao importa desde que usemos a mesma ordem para dummy e para a seq de bytes da str.

#Para a descriptografia, simplesmente recombinamos o par de chaves através do XOR
#inicialmente o int é convertido em bytes usando int.to_bytes()
#Esse metodo exige o num de bytes a ser convertido do int. Para isso, dividimos o tamanho em bits por oito
#Por fim, decode() de bytes nos devolve a str.

def decrypt(key1:int, key2:int)-> str:

    decrypted: int = key1^key2 #XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+7) // 8, "big")
#somamos 7 ao tam dos dados para a fim de garantir um arredondamento para cima, evitando erro de off-by-one(erro por um)
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("Kellven Dias")
    result: str = decrypt(key1, key2) #deve devolver a str
    print(key1, key2, result, sep="\n")
