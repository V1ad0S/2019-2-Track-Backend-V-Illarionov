# Generated by Django 2.2.5 on 2019-11-28 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20191127_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='topic',
            field=models.CharField(max_length=60, verbose_name='Название'),
        ),
    ]