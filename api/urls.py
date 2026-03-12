from django.urls import path
from home.views import index
from home.views import person

urlpatterns=[
    path('index/',index,name='index'),
    path('person/',person,name='person')
]