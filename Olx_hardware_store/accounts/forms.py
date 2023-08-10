from django.contrib.auth import forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import HwStoreUser, PhoneNumbersUserModel


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = HwStoreUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
        )

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('')
        self.fields['username'].help_text = _('')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = HwStoreUser
        fields = ['first_name', 'last_name', 'profile_bio', ]


class PhoneNumbersUserForm(forms.ModelForm):
    class Meta:
        model = PhoneNumbersUserModel
        fields = ['phone', ]
