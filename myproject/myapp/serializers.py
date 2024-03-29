# myapp/serializers.py

from rest_framework import serializers

class FIXTUREdataserializer(serializers.Serializer):
    Round_number=serializers.IntegerField()
    Team_1 = serializers.CharField()
    Team_2=serializers.CharField()
    Date=serializers.DateField()
    Location=serializers.CharField()
    Group=serializers.CharField()
