# MailBotLocaliza&Co 💚

Automatiza o envio de e-mails de confirmação de veículos para fornecedores, consolidando múltiplas placas em um único e-mail por destinatário — solução desenvolvida para uma demanda real de trabalho na Localiza.

## Funcionalidades

- Leitura dos dados de veículos e fornecedores a partir de planilha Excel.
- Agrupamento de placas e modelos por e-mail para envio único.
- E-mails HTML personalizados com lista de veículos.
- Inclusão de assinatura e logo da Localiza no corpo do e-mail.
- Envio seguro via SMTP Gmail.

## Tecnologias

- Python 3
- Pandas (Biblioteca para manipulação de dados)
- smtplib (Biblioteca a parte, oriunda da biblioteca padrão do Python usada para envio de e-mails via protocolo SMTP.
- email.mime (MIMEMultipart, MIMEText e MIMEImage, para inclusão de imagem, texto do tipo Html e divisão em partes do corpo do e-mail)

## Como usar

1. Configure o arquivo Excel com as colunas: `fornecedor`, `email`, `placa` e `modelo`.
2. Atualize o login SMTP com seu e-mail e senha (recomenda-se usar senha de app do Gmail).
4. Configure o smtplib.SMTP para o domínio de e-mail utilizado como remente.
5. Execute o script Python.
6. O bot envia e-mails agrupando veículos para cada destinatário.

## Observações

- Para funcionar corretamente, a conta Gmail deve ter a senha de app ativada e o acesso via SMTP liberado.

> ⚠️ **Nota Importante:**
>
> Para utilização em ambiente corporativo ou em demandas reais do dia a dia, é necessário:
>
> - Alterar a configuração do `smtplib` para utilizar o servidor SMTP oficial da empresa.
> - Substituir o campo `msg['From']` por um endereço de e-mail corporativo autorizado e autenticado.
>
> Essas alterações garantem a formalização adequada das comunicações e o alinhamento com as diretrizes de segurança e conformidade da organização.
>
> ![image](https://github.com/user-attachments/assets/81aab36f-bdd1-4e5c-8d04-97ede65e14ad)
