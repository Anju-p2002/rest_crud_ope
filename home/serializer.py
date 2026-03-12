from rest_framework import serializers
from home.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
         model=Person
         fields='__all__'
    def validate(self,data):
        spl_chars="!@#$%^&*()_+<>/"
        if any(c in spl_chars for c in data['name']):
            raise self.serializer.validationError("name should not have special char")
        if data['age']<18:
            raise serializer.validationError('Age should not be less 18')
            
        return data