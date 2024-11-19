from vigenere import Vigenere
#bibliotecas para facilitar a retirada de acentos e pontuação da frase
import string
import unicodedata

class criptofoda: 
    def __init__(self):
        self.cifra = Vigenere() #para conseguir ter acesso as informações da class Vegenere
    
    def run(self):
        #para que o codigo se repita até que o usuario não queira mais
        while True: 
            #escolha do que o programa vai ter que fazer
            escolha = input('Digite [c] para cifrar um mesagem, [d] para descifrar ou [s] para sair: ')

            #se caso a decisão for 's' para sair e encerrar o loop 
            if escolha == 's':
                print('...Saindo')
                break

            #controle de erro caso não seja digitado algo válido
            if escolha not in ['c', 'd']:
                print('ERRO: digite um termo válido. Tente novamente')
                continue
            
            #inputs para colocar as informações necessárias para o programa rodar
            text = input(f'texto a ser {"cifrado" if escolha == "c" else "descifrado"}: ')
            chave = input('senha: ')

            #pegando a variavel text e tirando os '.' , ',' e acentos 
            text = self.prepara_text(text)

            #se caso quiser cripitografar
            if escolha == 'c':
                self.cripitografar(text, chave)
            #se caso quiser descriptografar
            else:
                self.descriptografar(text, chave)
    
    #função para tirar o que não é letra da frase
    def prepara_text(self, text):
        text_sem_pontuacao = text.translate(str.maketrans('', '', string.punctuation))
        text_limpo = ''.join(c for c in unicodedata.normalize('NFD', text_sem_pontuacao) if unicodedata.category(c) != 'Mn')
        return text_limpo
    
    #função para cripitografar
    def cripitografar(self, text, chave):
        cifrado = self.cifra.cifra(text, chave)
        print(f'Mensagem criptografada: {cifrado}')
    
    #função para descriptografar
    def descriptografar(self, text, chave):
        descifrado = self.cifra.decifra(text, chave)
        print(f'Mensagem descriptografada: {descifrado}')


#para rodar o programa
app = criptofoda()
app.run()
            


     

   
    



