from cipher import Cipher

class Vigenere(Cipher):
    """ Cifra de Vigenere """
    def repetir_senha(self, senha, texto):
        '''
        Repete a senha ate o tamanho de texto
        '''
        if len(senha) < len(texto): #se tamanho da senha for menor que o do texto
            novo_passe = senha * (len(texto)//len(senha)) #repete a senha inteira até ficar do mesmo tamanho que o texto
            if len(novo_passe):
                novo_passe += senha[:len(novo_passe)] 
                #Se ainda houver caracteres restantes, adiciona-se a parte da senha que falta para completar o comprimento do texto.
            return novo_passe.upper()#retorna a senha final em letra maiuscula
        return senha.upper() #em caso a senha já for maior ou do mesmo tamanho

    def cifra(self, puroTexto, senha, decrypt=False):
        '''
        Cifra puroTexto com a cifra de Vigenere
        Decifra se decrypt for verdadeiro/true
        '''
        senha = self.repetir_senha(senha, puroTexto)#ajustando a senha
        puroTexto = self.format_str(puroTexto) #ajusta o texto sem espaço e letra miuscula
        textoout = ''#para armazenar o resultado

        for idx, char in enumerate(puroTexto.upper()):#Para cada caractere do texto, é encontrado o índice da letra correspondente na senha
            # indice da letra da cifra
            idx_chave = Cipher.puro_alfabeto.find(senha[idx])
            # gera alfabeto cifrado, é gerado, deslocando o alfabeto padrão pelo índice da chave.
            c_alfabeto = self.shift_alfabeto(Cipher.puro_alfabeto, idx_chave)

            if decrypt:
                #o código busca o índice do caractere no alfabeto cifrado e o substitui pelo caractere correspondente no alfabeto padrão.
                idx_p = c_alfabeto.find(char)
                textoout += Cipher.puro_alfabeto[idx_p]
            else:
                #busca o índice no alfabeto padrão e o substitui pelo caractere no alfabeto cifrado.
                idx_p = Cipher.puro_alfabeto.find(char)
                textoout += c_alfabeto[idx_p]
        return textoout

    def decifra(self, ciphertexto, senha):
        '''
        Decifra ciphertexto
        '''
        return self.cifra(ciphertexto, senha, True)
    
