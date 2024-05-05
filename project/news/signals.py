from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


@receiver(post_save, sender=Post)
def notify_subscribers (sender, instance, created, **kwargs):
    recipient = []
    for i in instance.post_category.all():
        for b in i.subscribers.all():
            recipient.append(b.email)
    html_content = render_to_string(
        'email_send.html',
        {
            'post': instance
        })
    msg = EmailMultiAlternatives(
        subject=f'{instance.name}',
        body=f"{instance.text}",
        from_email='unton.edgar.2001@yandex.ru',
        to=recipient,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()