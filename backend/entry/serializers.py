from rest_framework import serializers
from .models import Entry, Comment, Reply

class EntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'