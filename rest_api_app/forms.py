from django import forms
from rest_api_app.models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author', 'publication_date', 'publisher', 'summary', 'price', 'linkToBuy', 'image')