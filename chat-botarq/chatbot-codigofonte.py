import os

def processar_resposta(pergunta, nome):
    if "salário" in pergunta or "salarial" in pergunta:
        print(f'{os.linesep}{nome}, a média salarial de um programador Python é em torno de R$150.000,00 por ano.{os.linesep}')
    elif "cientista de dados" in pergunta:
        print(f'{os.linesep}{nome}, para se tornar um cientista de dados, você precisa estudar alguns temas que são muito relevantes para a profissão.\nÉ preciso se dedicar e estar sempre em busca de novos conhecimentos.\nUma forma de aprimorar seus conhecimentos é aprender muita coisa legal e se inscrever no Canal NERD DOS DADOS,\nporque é um canal que traz conteúdos atualizados toda semana.\nEntão se inscreva aqui no canal e ative as notificações para sempre ficar por dentro das novidades.{os.linesep}')
    elif "aprender" in pergunta:
        print(f'{os.linesep}{nome}, vale muito a pena aprender Python, pois é uma das linguagens que mais cresce')
    elif "IA" in pergunta or "inteligencia artificial" in pergunta:
        print(f'{os.linesep}{nome}, IA, ou Inteligência Artificial, refere-se à capacidade de um sistema computacional imitar e executar tarefas que \nnormalmente exigiriam inteligência humana. Isso inclui aprendizado, raciocínio, resolução de problemas, \ncompreensão de linguagem natural, reconhecimento de padrões e tomada de decisões. \nAs IA podem ser categorizadas em várias formas, incluindo IA fraca (específica para uma tarefa ou domínio) e IA forte \n(capaz de realizar uma ampla gama de tarefas com autonomia.{os.linesep}')
    else:
        print(f'{os.linesep}{nome}, desculpe, não entendi sua pergunta.')

def start():
    # Apresentar o chatbot
    print('Olá, bem vindo ao Bot Nerd dos Dados ')

    # Pedir o nome
    nome = input('Digite seu nome: ')

    while True:
        # Pedir a pergunta
        pergunta = input('Faça sua pergunta: ')

        # Processar a pergunta e fornecer a resposta
        processar_resposta(pergunta.lower(), nome)

if __name__ == '__main__':
    start()
