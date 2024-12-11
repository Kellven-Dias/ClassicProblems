"""
-Compactar dados é um metodo para reduzir o espaco ocupado por esses dados
-Compactar: tomar os dados e codificá-los de modo que ocupem menos espaço
-Descompactar: processo inverso da compactacao

-Ha uma relacao de custo-beneficio entre tempo e espaco:
-compactar e descompactar leva tempo
-por isso o metodo fara sentido quando um tam menor tem mais prioridade que tempo de execucao

-um int sem sinal que esteja armazenado em 64bits esta ineficiente, pois um int nunca ultrapassaria 65.535
-ele poderia ser armazenado como um inteiro de 16 bits, reduzindo em 75% o espaço ocupado

-Em Python, o desenvolvedor eh protegido de pensar em bits
-so ha um tipo: int
-a funcao sys.getsizeof() pode ajudar a descobrir qnts bytes de memoria os objetos estao ocupando

EXEMPLO:
Considere os 4 nucleotideos que compoem o DNA: A, C, G ou T
Em uma cadeia de nucleotideos (ACGTAGCG...), se armazenarmos cada letra como uma str, ocuparemos 8 bits para cada caractere.
-Em binario, apenas 2bits sao necessarios para representar 4 valores diferentes: 00, 01, 10, 11
Se fizermos: 00=A, 01=C, 10=G e 11=T, reduziremos o armazenamento de 8bits para 2, uma reducao de 75%

-o codigo a seguir converte uma str composta de As, Cs, Gs e Ts em uma cadeia de bits

"""

class CompressedGene:

#este metodo inicializa a cadeia de bits com os dados apropriados
#compress faz a compressoa transformando as str em cadeias de bits
    def __init__(self, gene: str)-> None:
        self._compress(gene)

#compress com underscore na frente sinaliza que atores externos à classe nao deverao depender da implementacao
#de um metodo, isto e, o metodo deve ser tratado como privado.
#para, realmente, enfaizar que e privado podemos usar dois underscores na frente

    def _compress(self, gene:str)-> None:
        self.bit_string: int = 1 #comeca com uma sentinela

        for nucleotide in gene.upper():
            self.bit_string <<=2 #descola dois bits para esquerda
            if nucleotide == "A":
                self.bit_string |= 0b00 #muda os dois ultimos bits para 00
            elif nucleotide == "C":
                self.bit_string |= 0b01 #muda os dois ultimos bits para 01
            elif nucleotide == "G":
                self.bit_string |= 0b10 #muda os dois ultimos bits para 10
            elif nucleotide == "T":
                self.bit_string |= 0b11 #muda os dois ultimos bits para 11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
            
    def decompress(self)->str:
        gene: str=""

        for i in range(0, self.bit_string.bit_length() - 1, 2): #-1 para excluir a sentinela

            bits: int = self.bit_string >> i & 0b11 #obtem apenas 2 bits relevantes

            if bits == 0b00:
                gene+="A"
            elif bits == 0b01:
                gene+="C"
            elif bits == 0b10:
                gene+="G"
            elif bits == 0b11:
                gene+="T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
            
        return gene[::-1] #inverte a str
    
    def _str__(self) -> str:
        return self.decompress()
    

if __name__=="__main__":
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("original is {} bytes\n".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original) #compacta
    print("compressed is {} bytes\n".format(getsizeof(compressed.bit_string)))
    #print(compressed.decompress())
    print("\noriginal and decompressed are the same: {}".format(original == compressed.decompress()))

#ao rodarmos o algoritmo, podemos ver que o original ocupava 8641 bytes enquanto o compactado ocupa somente 2320 bytes.
