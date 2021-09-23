
# Importações necessarias para realizar o codigo
# , biblioteca beatifulSoup e Requests
import requests  # Envia requisições
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # Servidor
from bs4 import BeautifulSoup  # scrapping
agora = datetime.datetime.now()  # PEga a hora


# Função
def extratorNoticias(URL):
    print('Extraindo as noticias...')
    cont = ''
    cont += ('<b>G1 Noticias!: </b>\n'+'<br>'+'-'*50+'<br>')
    resposta = requests.get(URL)  # Pega a resposta da URL inserida
    conteudo = resposta.content  # Pega todo o conteúdo da página do G1
    sopa = BeautifulSoup(conteudo, 'html.parser')
    for i, tag in enumerate(sopa.find_all('a',
                                          attrs={'class':
                                                 'feed-post-link', 'valign': ''})):  # Procura na pagina elementos <a> com a classe = feed-post-link
        cont += ((str(i+1)+'::'+tag.text+'\n'+'<br>'))
    return cont


def email(Conteudo):
    conteudo = Conteudo
    SERVER = 'smtp.gmail.com'  # Servidor
    PORT = 587  # porta
    # Aqui você insere o email que você usa para mandar
    FROM = ''
    PASS = ''  # A senha do email de envio
    listaEmail = []

    for i in range(len(listaEmail)):
        TO = listaEmail[i]  # Aqui você insere um ou mais emails para enviar
        # Corpo do email
        mensagem = MIMEMultipart()
        mensagem['Subject'] = 'G1 Top Noticias'+'----'+str(agora)
        mensagem['From'] = FROM
        mensagem['To'] = TO
        mensagem.attach(MIMEText(conteudo, 'html'))

        # Iniciando servidor
        server = smtplib.SMTP(SERVER, PORT)
        server.set_debuglevel(1)
        server.ehlo()
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, TO, mensagem.as_string())

        server.quit()


def main():
    # Função onde o código é rodado
    conteudo = ''
    site = str(input('Insira a URL do G1: '))
    cnt = extratorNoticias(site)
    conteudo += cnt
    conteudo += ('<br>-----------<br>')
    conteudo += ('<br><br>Fim da mensagem')
    print('Criando email...')
    email(conteudo)
    print('Email enviado ')


main()
