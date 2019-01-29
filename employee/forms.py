from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password']
        labels = {
            'password':'Password'
        }


    def clean_email(self):

        if self.cleaned_data['email'].endswith('@gmail.com'):
             return self.cleaned_data['email']
        else:
            raise ValidationError("email is not correct")

    def save(self):
         password = self.cleaned_data.pop('password')
         role = self.cleaned_data.pop('role')
         print("============================= Password", password)
         u = super().save()
         u.set_password(password)
         u.groups.set([role])
         u.save()
         return u

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):

            initial = kwargs.setdefault('initial', {})

            if kwargs['instance'].groups.all():
                initial['role'] =  kwargs['instance'].groups.all()[0]
            else:
                initial['role']= None

        forms.ModelForm.__init__(self, *args, **kwargs)


