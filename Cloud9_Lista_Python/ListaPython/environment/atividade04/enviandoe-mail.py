import yagmail,configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read("conf")
sender = yagmail.SMTP(config['Mail']['username'],config['Mail']['password'])
anexo = 'Python - Sending Email using SMTP - Tutorialspoint.pdf'

destinatario = ['atividadepythonsmtp@gmail.com','ricardoqvidal@gmail.com']
nome ='Python SMTP','Ricardo'
assunto = 'Notificação Tutorial'

conteudo =f"""
    <html>
        <body>
            <p> Olá {{name}}!</p>
            <p> Aprenda mais sobre Python em  <a href="https://www.tutorialspoint.com/python/index.htm">TutorialPythons</a></p>
        </body>
    </html>
"""

for dest in range(0,2):
    nome[dest]
    conteudo.format(name=nome[dest])
    print (nome[dest], destinatario[dest], conteudo.format(name=nome[dest]))
    sender.send(to=destinatario[dest], subject=assunto, contents=conteudo.format(name=nome[dest]), attachments=anexo)

print ("Mensagem enviada com sucesso...")