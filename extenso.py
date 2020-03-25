from math import ceil, floor

class Palavra:

    def __init__(self, singular, plural):
        self.singular = singular
        self.plural = plural

class Extenso:

    def __init__(self):

        self._numero_maximo = 999999999999999999999999999999999999999999999

        # Dicionários para armazenar os números por extenso
        self.unidades = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10 : 'dez', 
                         11 : 'onze', 12 : 'doze', 13 : 'treze', 14 : 'quatorze', 15 : 'quinze', 16 : 'dezesseis', 17 : 'dezessete', 18 : 'dezoito', 19 : 'dezenove'}

        self.dezenas = {2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta', 6: 'sessenta', 7: 'setenta', 8: 'oitenta', 9: 'noventa'}

        self.centenas = {1: Palavra('cem', 'cento'), 2: 'duzentos', 3: 'trezentos', 4: 'quatrocentos', 5: 'quinhentos', 6: 'seiscentos', 7: 'setecentos', 8: 'oitocentos', 9: 'novecentos'}

        # Tupla armazenando os milhares
        self.milhares = (Palavra('',''), Palavra('mil','mil'), Palavra('milhão','milhões'), \
                        Palavra('bilhão','bilhões'), Palavra('trilhão','trilhões'), Palavra('quatrilhão','quatrilhões'), \
                        Palavra('quintilhão','quintilhões'), Palavra('sextilhão','sextilhões'), Palavra('septilhão','septilhões'), \
                        Palavra('octilhão','octilhões'),Palavra('nonilhão','nonilhões'), Palavra('decilhão','decilhões'), \
                        Palavra('undecilhão','undecilhões'), Palavra('duodecilhão','duodecilhões'),Palavra('tredecilhão','tredecilhões'))


    def escrever(self, numero):
        if (numero > self._numero_maximo):
            raise Exception('Número informado maior que o número máximo suportado')
        if (numero == 0):
            return 'zero'
        extenso = ''

        # Conversão do número recebido para string
        numero_string = str(numero)
        # Busca o tamanho do número informado
        tamanho = len(numero_string)

        # Arredonda para cima para saber quantos grupos de três há
        ternarios = ceil(tamanho / 3)

        # Preenche a string do número com zeros até o tamanho divisível por 3
        numero_string = numero_string.zfill(ternarios * 3)
        
        # percorre os grupos de três números
        for n in range(1, ternarios + 1):
            # Busca a parte do número referente ao grupo atual
            parte_numero = int(numero_string[(n - 1) * 3 : n * 3])

            # Caso o grupo seja zero, não precisa de tratamento
            if parte_numero == 0:
                continue

            # Cálculo para retornar a centena
            centena = floor(parte_numero / 100)

            # Cálculo para retornar a dezena
            dezena = floor((parte_numero - (centena*100)) / 10)

            # Cálculo para retornar a unidade
            unidade = parte_numero - (centena*100) - (dezena*10)

            # Caso a centena esteja preenchida, faz o tratamento
            if (centena > 0):
                if (dezena == 0 and unidade == 0 and extenso != ''):
                    extenso += ' e '
                elif extenso != '':
                    extenso += ', '
                if (centena == 1): # Se for CEM deve busca do singular, caso a unidade ou dezena esteja preenchida, busca do plural
                    if(dezena > 0 or unidade > 0):
                        extenso += self.centenas[centena].plural
                    else:
                        extenso += self.centenas[centena].singular
                else:
                    extenso += self.centenas[centena] # Caso a centena for maior que 1, busca a string correspondente no dicionário
            
            # Caso a dezena esteja preenchida, faz o tratamento
            if (dezena > 0):
                if (extenso != ''): # Se o número por extenso já veio preenchido, adiciona "E"
                    extenso += ' e '

                if (dezena == 1): # Se a dezena for um, busca das unidades
                    dezena = 10 + unidade
                    unidade = 0 # para não executar o extenso das unidades
                    extenso += self.unidades[dezena] # Busca o extenso correspondente nas unidades
                else:
                    extenso += self.dezenas[dezena] # Se a dezena for maior que um, busca da sua posição correspondente nas dezenas

            # Caso a unidade esteja preenchida, faz o tratamento
            if (unidade > 0):
                if (extenso != ''): # Se a centena ou dezena estão preenchidas, adiciona "E"
                    extenso += ' e '
                extenso += self.unidades[unidade] # Busca o extenso correspondente nas unidades

            # Tratamento para milhares
            if n < tamanho: # Se não for o último, concatena o milhar correspondente
                if (parte_numero > 1):
                    extenso += f' {self.milhares[ternarios - n].plural}' # Maior que 1, busca o plural
                else:
                    extenso += f' {self.milhares[ternarios - n].singular}' # Se for 1, busca o singular
        return extenso


if (__name__ == "__main__"):
    numero = int(input('Digite um número: '))
    print(Extenso().escrever(numero))
