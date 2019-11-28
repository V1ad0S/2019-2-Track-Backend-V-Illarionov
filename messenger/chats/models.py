from django.db import models
from django.utils import timezone
from users.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField(verbose_name='Групповой ли чат')
    topic = models.CharField(
        max_length=60,
        verbose_name='Название',
    )
    last_message = models.TextField(
        max_length=100,
        verbose_name='Последнее сообщение',
        null=True,
    )

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.CASCADE,
        verbose_name='Чат',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    content = models.TextField(verbose_name='Содержание')
    added_at = models.DateTimeField(
        null=True,
        auto_now_add=True,
        verbose_name='Дата отправки',
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-added_at']


class Attachment(models.Model):
    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.CASCADE,
        verbose_name='Чат',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    message = models.ForeignKey(
        to=Message,
        on_delete=models.CASCADE,
        verbose_name='Сообщение',
    )
    attach_type = models.TextField(
        max_length=60,
        verbose_name='Тип вложения',
    )
    url = models.CharField(
        max_length=100,
        verbose_name='Ссылка',
    )

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'


class Member(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    chat = models.ForeignKey(
        to=Chat,
        on_delete=models.CASCADE,
        verbose_name='Чат',
    )
    new_messages = models.IntegerField(verbose_name='Кол-во новых сообщений')
    last_read_message = models.ForeignKey(
        to=Message,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Последнее прочитанное',
    )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
