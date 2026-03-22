from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from home.serializers import PersonSerializer
from home.serializers import UserRegister
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST','PUT'])
def index(request): 
    if request.method=='GET':
       people_details= {
            'name':'anju p',
            'age':23,
            'place':'alappuzha'
    }
       return Response(people_details)

    elif request.method=='POST':
       return Response({"message":"POST method is working"})

    elif request.method=='PUT':
       return Response({"message":"PUT is working"})
    
    

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
   if request.method=='GET':
      objperson=Person.objects.all()
      serializers=PersonSerializer(objperson,many=True)
      return Response(serializers.data)
   elif request.method=='POST':
      data=request.data
      serializers=PersonSerializer(data=data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data)
      return Response(serializers.errors)
   elif request.method=='PUT':
      data=request.data
      obj=Person.objects.get(id=data['id'])
      serializers=PersonSerializer(obj,data=data,partial=False)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data)
      return Response(serializers.errors)
   elif request.method=='PATCH':
      data=request.data
      obj=Person.objects.get(id=data['id'])
      serializers=PersonSerializer(obj,data=data,partial=True)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data)
      return Response(serializers.errors)
   else:
      data=request.data
      obj=Person.objects.get(id=data['id'])
      obj.delete()
      return Response({"message": 'person delete'})
   
class Register(APIView):
   def post(self,request,formate=None):
      serializer = UserRegister(data=request.data)
      data={}
      if serializer.is_valid():
         account = serializer.save()
         data['respone']='registered'
         data['username']=account.username
         data['email']=account.email
         token,created=Token.objects.get_or_create(user=account)
         data['token']=token.key
      else:
         data=serializer.errors
         return Response(data)
      
class Welcome(APIView):
   permission_classes=(IsAuthenticated,)
   def get(self,request):
      content = {"user":str(request.user),'userid':str(request.user.id)}
      return Response(content)