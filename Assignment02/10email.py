class EmailSender:
    def send_mail(self, to, subject, body):
        print(f"Email sent to: {to}\nSubject: {subject}\nBody: {body}")


if __name__ == '__main__':
    es = EmailSender()
    es.send_mail("xyz@gmail.com", "Hello", "This is a test email")