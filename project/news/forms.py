from django import forms
from django.core.exceptions import ValidationError

from .models import Post

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class NewsForm(forms.ModelForm):
    name = forms.CharField(label='Название')
    text = forms.CharField(label='содержание',min_length=20, widget = forms.Textarea)

    class Meta:
        model = Post
        fields = ['name', 'text','post_category']
    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user