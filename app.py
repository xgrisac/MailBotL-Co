from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText # Import format mail
from email.mime.image import MIMEImage # Import image
import pandas as pd
import smtplib # LIP que me conecta ao SMPT

# LE O ARQUIVO EXCEL
fornecedores = pd.read_excel("./planilhateste.xlsx") 

# Agrupa as placas e modelos por e-mail e fornecedor
agrupamento = fornecedores.groupby(['email',]).agg({
    'placa' : lambda placas: list(placas),
    'modelo' : lambda modelos: list(modelos),
}).reset_index()

# Conexão com servidor SMTP(Mail)
servidorMail = smtplib.SMTP('smtp.gmail.com', port=587)
servidorMail.starttls()
servidorMail.login('INSIRA SEU LOGIN', 'INSIRA SUA SENHA') # NECESSÁRIO LOGIN DE ACESSO AO E-MAIL

# Loop que percorre cada 'fornecedor'
for index, row in agrupamento.iterrows():
    try:
        email = row['email']
        placas = row['placa']
        modelos = row['modelo']

        msg = MIMEMultipart('related')
        msg['Subject'] = 'Confirmação de veículos'
        msg['From'] = 'xgrisac@gmail.com'
        msg['To'] = email

        # Lista HTML de veículos
        listaDeVeiculos = "".join(
            [f"<li><strong>{placa} - {modelo}</strong></li>" for placa, modelo in zip(placas, modelos)]
        )

        conteudo_html = f"""
        <html>
        <body>
            <p>Prezados, bom dia!</p>

            <p>Por gentileza, podem nos confirmar se os veículos abaixo se encontram com vocês e estão disponíveis para coleta?</p>

            <br>
            <ul>
                {listaDeVeiculos}
            </ul>
            <br>

            <p>No aguardo do seu retorno!</p>

            <p><strong>Atenciosamente...</strong></p>

            <table>
                <tr>
                    <td><img src="cid:assinatura_logo" width="150"/></td>
                    <td style="padding-left:10px">
                        <p><strong style="color:#000">Seu nome</strong><br>
                        <span style="color:#00704A">Seu setor<br>
                        +55 (31) 3247-4248</span><br><br>
                        🌐 <a href="URL" style="text-decoration:none; color:#00704A;">Site</a> &nbsp;&nbsp;
                        📷 <a href="URL" style="text-decoration:none; color:#00704A;">Instagram</a> &nbsp;&nbsp;
                        💼 <a href="URL" style="text-decoration:none; color:#00704A;">LinkedIn</a>
                        </p>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """

        msg.attach(MIMEText(conteudo_html, 'html'))

        # Anexa imagem
        with open("./logodaempresa", 'rb') as img:
            imagem = MIMEImage(img.read())
            imagem.add_header('Content-ID', '<assinatura_logo>')
            msg.attach(imagem)

        # Envia e-mail
        servidorMail.sendmail(msg['From'], msg['To'], msg.as_string())
        print(f"E-mail enviado para {email}")

    except Exception as e: # Retorno em caso de erro / 'e' exibe o erro retornado
        print(f"Erro ao enviar para {email}: {e}")

# Encerra a conexão com o servidor
servidorMail.quit()
