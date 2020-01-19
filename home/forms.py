from django import forms
from .models import Category
from .models import Country
from .models import News
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('article', 'content', 'country', 'category')