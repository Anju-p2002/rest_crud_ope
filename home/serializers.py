from rest_framework import serializers
from home.models import Person
from django.contrib.auth import get_user_model

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
         model=Person
         fields='__all__'
    def validate(self,data):
        spl_chars="!@#$%^&*()_+<>/"
        if any(c in spl_chars for c in data['name']):
            raise self.serializer.validationError("name should not have special char")
        if data['age']<18:
            raise serializers.validationError('Age should not be less 18')
            
        return data
    
User = get_user_model
class UserRegister(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username']

        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.validationError({'password':'password does not match'})
        reg.set_password(password)
        reg.save()
        return reg