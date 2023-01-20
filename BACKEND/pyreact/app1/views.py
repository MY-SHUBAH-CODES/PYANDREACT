from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializes import Studentserializer


@api_view(['GET', 'POST','PUT','DELETE'])
def Studentv1(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = Studentserializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'PUT':
        id=request.data['id']
        Students=Student.objects.get(id=id)#hard quoted cjange accordingly 
        serializer = Studentserializer(Students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id=request.data['id']
        Students=Student.objects.get(id=id)#hard quoted cjange accordingly 
        Students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)