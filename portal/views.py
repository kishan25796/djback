from django.shortcuts import render
from .models import Homework
from rest_framework.response import Response
from .serializers import HomeworkSerializers
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET",])
def homew(request):
    homework = Homework.objects.all()
    serializer = HomeworkSerializers(homework, many =True)
    return Response(serializer.data)
@api_view(["GET",])
def gethw(request,pk):
    homework = Homework.objects.get(id=pk)
    serializer= HomeworkSerializers(homework, many=False)
    return Response(serializer.data)


