from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from home.serializer import PersonSerializer


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
      serializer=PersonSerializer(objperson,many=True)
      return Response(serializer.data)
   elif request.method=='POST':
      datas=request.data
      serializer=PersonSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   elif request.method=='PUT':
      datas=request.data
      obj=Person.objects.get(id=data['id'])
      serializer=PersonSerializer(obj,data=data,partial=False)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   elif request.method=='PATCH':
      data=request.data
      obj=Person.objects.get(id=data['id'])
      serializer=PersonSerializer(obj,data=data,partial=True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors)
   else:
      data=request.data
      obj=Person.objects.get(id=data['id'])
      obj.delete()
      return Response({"message": 'person delete'})