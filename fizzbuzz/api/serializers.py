from rest_framework import serializers
from ..models import Fizzbuzz

class FizzbuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fizzbuzz 
        fields = ['fizzbuzz_id', 'creation_date', 'useragent', 'message']
