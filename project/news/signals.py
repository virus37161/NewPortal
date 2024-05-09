from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .tasks import send_post

@receiver(post_save, sender=Post)
def notify_subscribers (sender, instance, created, **kwargs):
    recipient = []
    name = instance.name
    text = instance.text
    for i in instance.post_category.all():
        for b in i.subscribers.all():
            recipient.append(b.email)
    send_post.apply_async(args=[recipient, name, text])
