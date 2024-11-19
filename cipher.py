from random import shuffle
#A função shuffle do módulo random é importada, permitindo que listas sejam embaralhadas aleatoriamente.

# Classe com metodos basicos para cifras classicas 
class Cipher(object):
   #Classe base para as cifras classicas 
    puro_alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    puro_alfanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def format_str(self, text):
        #Retorna text sem espacos e em maiusculas
        return text.replace(' ', '').upper()

    def shift_alfabeto(self, alfabeto, shift):
        #Retorna alfabeto com deslocamento de valor shift
        #Por exemplo, um deslocamento de 3 em "ABC" resultaria em "DEF".
        return alfabeto[shift:] + alfabeto[:shift]

    def create_square(self, alfabeto = [], chave = '', alfanum = False, replace = ['J', 'I'], sequence = False):
        #Retorna um alfabeto numa matriz de num x num
        #Por padrao, retorna uma matriz formada pelo alfabeto ABCDEFGHIKLMNOPQRSTUVWXYZ
        #chave: retorna um quadrado, com chave iniciando o quadrado
        #alphanum: quadrado com letras e numeros
        #replace: letras a serem trocadas, 'j' por 'I'
        ##sequence se True continua a preencher o quadrado a partir do ultimo caracter da chave
        quadrado = []

        #determinando qual alfabeto usar
        if alfabeto: 
            if alfanum:
                replace = ['', '']
            # num = 5
            alfabet1 = alfabeto
        elif alfanum:
            # num = 6
            alfabet1 = self.puro_alfanum
            replace = ['', '']
        else:
            # num = 5
            alfabet1 = self.puro_alfabeto

        alfabet1 = self.criar_alfabeto(chave.upper(), alfabeto, replace, sequence)#gera um alfabeto modificado de acorco com a chave
        num = 5 + len(alfabeto) % 5 #divide o alfabeto em grupos de 5 + o tamanho do alfabeto 

        for idx in range(0, len(alfabet1), num):
            quadrado.append(alfabet1[idx:idx + num]) #adiciona ao quadrado
        return quadrado

    def criar_alfabeto(self, chave = '', alfabeto = puro_alfabeto, replace = ['', ''], sequence = False):
        # Retorna um alfabeto modificado pela chave, colocando ela no começo do alfabeto

        #Se houver uma chave, ela é processada (por exemplo, caracteres repetidos são removidos).
        #O alfabeto é modificado conforme necessário e combinado com a chave, resultando em um novo alfabeto.
        if chave:
            chave = self.chave_repetido(chave) #removendo caracteres
            if replace[0] in chave:
                chave = chave.replace(replace[0], replace[1]) #removendo caracteres
            if sequence: #Se sequence for True, o alfabeto é deslocado antes de ser combinado com a chave
                idx = alfabeto.index(chave[-1])
                alfabeto = self.shift_alfabeto(alfabeto, idx)

        cipher = alfabeto.replace(replace[0], '')

        for ch_chave in chave:
            if ch_chave in cipher:
                cipher = cipher.replace(ch_chave, '')
        return chave + cipher #novo alfabeto combinado com a chave

    def random_alfabeto(self, alfanum=False):
        #Retorna um alfabeto aleatório com a função shuffle
        if alfanum: #Se alfanum for True, ele utiliza o alfabeto alfanumérico.
            alfabeto = list(self.criar_alfabeto(alfabeto=self.puro_alfanum))
        else:
            alfabeto = list(self.criar_alfabeto())

        shuffle(alfabeto)

        return ''.join(alfabeto)

    def chave_repetido(self, chave):
        #Remove caracteres repetidos da senha  
        temp = ''
        for ch in chave.upper():#Para cada caractere na chave, adiciona à string temp somente se ainda não estiver presente.
            if ch not in temp:
                temp += ch
        return temp