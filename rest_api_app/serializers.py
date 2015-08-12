from django.forms import widgets
from rest_framework import serializers
from rest_api_app.models import Books

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id',
                  'title',
                  'author',
                  'publication_date',
                  'publisher',
                  'summary',
                  'price',
                  'linkToBuy',
                  'image')