from ClinicModule.models import Patient
from django import forms
from ClinicModule import validators
from django.utils.translation import ugettext, ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    error_messages = {
        'invalid_login': _("Proszę wprowadzić prawidłowy login %(username)s oraz hasło. "
                           "Zwróć uwagę na wielkość podawanych znaków."),
        'inactive': _("To konto jest nieaktywne."),
        'required': _('pole jest obligatoryjne do wypełnienia.'),
        'max_length': _('przekroczono dopuszczalny limit znaków.')}

    email = forms.EmailField(initial='name@example.com',
                             label='Adres email', max_length=64, error_messages=error_messages)
    password = forms.CharField(
        widget=forms.PasswordInput(), error_messages=error_messages)

    def clean_password(self):

        if not 'password' in cleaned_data:
            raise forms.ValidationError(
                _('Hasło jest puste!'), code='invalid')

        data = self.cleaned_data.get('password')

        return self.cleaned_data


class CustomUserForm(forms.Form):

    email = forms.EmailField(initial='email@przyklad.pl',
                             label=_('Adres email'), max_length=32,
                             error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                                             'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    first_name = forms.CharField(label=_('Imię'), initial='Jan', max_length=32, validators=[RegexValidator(
        r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", message=_("pole zawiera nieprawidłowy ciąg znaków."))],
        error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                        'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    second_name = forms.CharField(label=_('Nazwisko'), initial='Kowalski', max_length=48, validators=[RegexValidator(
        r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", message=_("pole zawiera nieprawidłowy ciąg znaków."))],
        error_messages={'required': _(
            'pole jest obligatoryjne do wypełnienia.'),
            'max_length': _('przekroczono limit znaków, maksymalna długość to 48.')})

    phone_number = forms.CharField(label=_('Numer kontaktowy'), initial='+48', min_length=9, max_length=12, validators=[RegexValidator(
        r'^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$', message=_('Numer kontakowy jest nieprawidłowy.'))],
        error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                        'max_length': _('przekroczono limit znaków, maksymalna długość to 12.'),
                        'min_length': _('pole zawiera niewystarczającą ilość znaków (minimum: 9. znaków).')})

    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, error_messages={
        'min_length': _('Hasło powinno zawierać co najmniej 8. znaków.'),
        'required': _('pole jest obligatoryjne do wypełnienia.')}, label=_('Hasło'))


class PatientForm(forms.Form):

    PESEL = forms.CharField(label=_('PESEL'), initial='', max_length=11, validators=[validators.validate_patient_pesel],
                            error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                                            'max_length': _('przekroczono limit znaków, maksymalna długość to 11.')})

    address = forms.CharField(label=_('Adres'), initial='', max_length=32, validators=[RegexValidator(
        r"[A-Za-z0-9'\.\-\s\,]", message=_("pole zawiera nieprawidłowy ciąg znaków."))],
        error_messages={'required': _(
            'pole jest obligatoryjne do wypełnienia.'),
            'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    city = forms.CharField(label=_('Miasto'), initial='+48', max_length=32, validators=[RegexValidator(
        r'^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$', message=_('pole jest nieprawidłowe.'))],
        error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                        'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    zip_code = forms.CharField(label=_('Kod pocztowy'), initial='10117', validators=[validators.validate_zip_code], max_length=6,
                               error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                                               'max_length': _('przekroczono limit znaków, maksymalna długość to 6.')},)




class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(label=_('Imię'), max_length=32, validators=[RegexValidator(
        r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", message=_("pole zawiera nieprawidłowy ciąg znaków."))],
        error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                        'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    second_name = forms.CharField(label=_('Nazwisko'), max_length=48, validators=[RegexValidator(
        r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$", message=_("pole zawiera nieprawidłowy ciąg znaków."))],
        error_messages={'required': _(
            'pole jest obligatoryjne do wypełnienia.'),
            'max_length': _('przekroczono limit znaków, maksymalna długość to 48.')})

    phone_number = forms.CharField(label=_('Numer kontaktowy'), min_length=9, max_length=12, validators=[RegexValidator(
        r'^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$', message=_('Numer kontakowy jest nieprawidłowy.'))],
        error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                        'max_length': _('przekroczono limit znaków, maksymalna długość to 12.'),
                        'min_length': _('pole zawiera niewystarczającą ilość znaków (minimum: 9. znaków).')})
    address = forms.CharField(label=_('Adres'), max_length=32, validators=[RegexValidator(
        r"[A-Za-z0-9'\.\-\s\,]", message=_("pole zawiera nieprawidłowy ciąg znaków."))],
        error_messages={'required': _(
            'pole jest obligatoryjne do wypełnienia.'),
        'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    city = forms.CharField(label=_('Miasto'), max_length=32, validators=[RegexValidator(
        r'^[a-zA-Z]+(?:[\s-][a-zA-Z]+)*$', message=_('pole jest nieprawidłowe.'))],
        error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                        'max_length': _('przekroczono limit znaków, maksymalna długość to 32.')})

    zip_code = forms.CharField(label=_('Kod pocztowy'), validators=[validators.validate_zip_code], max_length=6,
                               error_messages={'required': _('pole jest obligatoryjne do wypełnienia.'),
                                               'max_length': _('przekroczono limit znaków, maksymalna długość to 6.')},)
