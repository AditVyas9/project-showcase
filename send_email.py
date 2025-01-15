import smtplib, ssl, os


def send_email( message):
    my_host = "smtp.gmail.com"
    my_port = 465
    username = "vyasadit879@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "vyasadit879@gmail.com"
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=my_host, port=my_port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

