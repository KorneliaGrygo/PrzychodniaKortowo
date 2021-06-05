from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(initial='name@example.com',
                             label='Email address', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def clean_password(self):

        if not 'password' in cleaned_data:
            raise forms.ValidationError('The password is empty!')

        data = self.cleaned_data.get('password')

        return self.cleaned_data
