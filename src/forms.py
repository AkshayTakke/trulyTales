from django import forms
from .models import *
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField

from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10 or len(phone) > 25:
            raise ValidationError("Phone number must be between 10 and 25 characters.")
        return phone

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'phone', 'password1', 'password2']


# forms.py


class UserProfileForm(forms.ModelForm):
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10 or len(phone) > 25:
            raise ValidationError("Phone number must be between 10 and 25 characters.")
        return phone

    class Meta:
        model = user_profile
        fields = ['name', 'phone', 'email', 'image']


class AddBlog(forms.ModelForm):
    # date = forms.DateField(label="Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
    class Meta:
        model = blog
        exclude = ('user', 'is_verified',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-5'}),
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30, 'class': 'mb-5'}),
            'category': forms.Select(attrs={'class': 'form-control'})

        }


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})

        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('blog_id', 'parent', 'content')

        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'ml-3 mb-3 form-control border-0 comment-add rounded-0', 'rows': '1',
                       'placeholder': 'Add a public comment'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)
