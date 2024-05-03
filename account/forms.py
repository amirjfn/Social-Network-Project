from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'your Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'your Email'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'your Password'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your Password'}))


    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل از قبل مورد استفاده قرار گرفته شده است')
        return email


    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user :
            raise ValidationError('این نام از قبل مورد استفاده قرار گرفته شده است')
        return username


    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError(' رمزها مشابه نیستند')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':'your Password'}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ('age', 'bio')