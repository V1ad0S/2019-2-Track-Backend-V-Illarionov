from django import forms
from django.core.exceptions import ValidationError
from chats.models import *
from users.models import *

class CreatePersonalChatForm(forms.Form):
    first_user_id = forms.IntegerField()
    second_user_id = forms.IntegerField()

    def clean_first_username(self):
        first = self.cleaned_data['first_user_id']
        try:
            User.objects.get(id=first)
        except User.DoesNotExist:
            self.add_error('first_user_id', 'User does not exist')
            # raise ValidationError('User does not exist', code='invalid')
        return first

    def clean_second_username(self):
        second = self.cleaned_data['second_user_id']
        try:
            User.objects.get(id=second)
        except User.DoesNotExist:
            self.add_error('second_user_id', 'User does not exist')
            # raise ValidationError('User does not exist', code='invalid')
        return second

    def clean(self):
        if not len(self.errors):
            first = self.cleaned_data['first_user_id']
            second = self.cleaned_data['second_user_id']
            topic = sorted([first, second])

            try:
                Chat.objects.get(topic='id{}&id{}'.format(topic[0], topic[1]))
                self.add_error(None, 'Chat already exist')
            except Chat.DoesNotExist:
                pass

    def save(self):
        first = self.cleaned_data['first_user_id']
        second = self.cleaned_data['second_user_id']
        topic = sorted([first, second])

        first_user = User.objects.get(id=first)
        second_user = User.objects.get(id=second)

        new_chat = Chat.objects.create(
            topic='id{}&id{}'.format(topic[0], topic[1]),
            is_group_chat=False
        )

        Member.objects.create(
            user=first_user,
            chat=new_chat,
            new_messages=0,
        )
        Member.objects.create(
            user=second_user,
            chat=new_chat,
            new_messages=0,
        )
        return new_chat.id


class SendMessageForm(forms.ModelForm):
    def clean(self):
        try:
            member = Member.objects.get(
                user=self.cleaned_data.get('user'),
                chat=self.cleaned_data.get('chat'),
            )
        except Member.DoesNotExist:
            self.add_error('user', 'Forbidden. Member does not exist')

    def save(self):
        message = Message.objects.create(
            chat = self.cleaned_data.get('chat'),
            user = self.cleaned_data.get('user'),
            content = self.cleaned_data.get('content'),
        )
        return message.id

    class Meta:
        model = Message
        fields = ['chat', 'user', 'content']


class ReadMessageForm(forms.Form):
    chat_id = forms.IntegerField()
    user_id = forms.IntegerField()
    message_id = forms.IntegerField()

    def clean_chat_id(self):
        chat_id = self.cleaned_data['chat_id']
        try:
            Chat.objects.get(id=chat_id)
        except Chat.DoesNotExist:
            self.add_error('chat_id', 'Chat does not exist')
            # raise ValidationError('Chat does not exist', code='invalid')
        return chat_id

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            self.add_error('user_id', 'Chat does not exist')
            # raise ValidationError('User does not exist', code='invalid')
        return user_id

    def clean_message_id(self):
        message_id = self.cleaned_data['message_id']
        try:
            Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            self.add_error('message_id', 'Message does not exist')
            # raise ValidationError('Message does not exist', code='invalid')
        return message_id

    def clean(self):
        if not len(self.errors):
            chat = Chat.objects.get(id=self.cleaned_data.get('chat_id'))
            user = User.objects.get(id=self.cleaned_data.get('user_id'))
            try:
                Member.objects.get(chat=chat, user=user)
            except Member.DoesNotExist:
                self.add_error('user_id', 'Forbidden. Member does not exist')

    def save(self):
        chat = Chat.objects.get(id=self.cleaned_data['chat_id'])
        user = User.objects.get(id=self.cleaned_data['user_id'])
        message = Message.objects.get(id=self.cleaned_data['message_id'])
        member = Member.objects.get(chat=chat, user=user)
        member.last_read_message = message
        member.save()
