from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class ticketChatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ticketChatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_id = 'id-exampleForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('отправить', 'Отправить'))

    post = forms.CharField(widget=forms.HiddenInput(), )
    name = forms.CharField(widget=forms.HiddenInput())
    body = forms.CharField(label='Сообщения')
    file = forms.FileField(label='Файл', max_length=100, required=False)

    def setF(self, post, name):
        self.fields['post'].initial = str(post)
        self.fields['name'].initial = str(name)
        return True
