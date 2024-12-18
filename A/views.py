from django.shortcuts import render
from django.core.mail import EmailMessage



def send(requests):
    email = EmailMessage(
        subject='test',
        body='hi rohyyy',
        from_email='alitezanaghipour@gmail.com',
        to=['rohollahnaghipour41@gmail.com']
    )
    email.send()


