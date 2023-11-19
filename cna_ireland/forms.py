from django import forms
from django_recaptcha.fields import ReCaptchaField


class MyCustomSignupForm(forms.Form):

    captcha = ReCaptchaField()

    def signup(self, request, user):
        pass