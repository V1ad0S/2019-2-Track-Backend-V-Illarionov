# Generated by Django 2.2.5 on 2019-11-07 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group_chat', models.BooleanField()),
                ('topic', models.TextField(max_length=50)),
                ('last_message', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('added_at', models.DateTimeField(null=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['-added_at'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_messages', models.IntegerField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat')),
                ('last_read_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach_type', models.TextField(max_length=60)),
                ('url', models.CharField(max_length=100)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вложение',
                'verbose_name_plural': 'Вложения',
            },
        ),
    ]
