import os 

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Vale muito a pena aprender Python, pois e uma das linguagens que mais cresce atualmente{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} A media salarial de um programador Python e em torno de R$150.000.00 por ano.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} pra se torna um cientista de dados voce precisa estudar alguns temas que sao muito relevantes para a profissão.\n E preciso se dedicar e estar sempre em busca de novos conhecimentos. \nUma forma de aprimorar  seus conhecimentos e aprender muita coisa legal e se inscrever no Canal NERD DOS DADOS, \nporque e um canal que traz conteudos atualizados toda semana. \nEntao se inscreve aqui no canal e ative as noticaçoes pra sempre ficar por dentro das novidades.{os.linesep} ')
    else:
        print('Digite apenas as opçoes 1, 2, ou 3')

    def start():
        #Apresentar o chatbot
        print('Ola, bem vindo ao Bot Nerd dos Dados')

        #Pedir o nome
        nome = input('Digite seu nome: ')

        while True:

            #Oferecer um menu de opçoes 
            resposta = input(
                f'O que gostaria de saber hoje? {os.linesep}[1] - Vale a pena aprender Python? {os.linesep}[2] -Qual a media salarial de um profissional que trabalha com Python? {os.linesep}[3] - E como eu faço pra me torna um cientista de dados? {os.linesep}')

            # Processar a resposta enviada
            processar_resposta(resposta, nome) 

    if __name__=='__main__': 
        start() 