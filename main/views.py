from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse

from json import dumps

from .models import Task
from . import serializers

from rest_framework.decorators import api_view

# Create your views here.


'''
2 Вида views

1. Function based view
2. Class based view (APIView, generics, ViewSet)
'''

# function based-view


@api_view(['GET'])
def tasks_list(request):
    querySet = Task.objects.all()
    serializer = serializers.TaskListSerializer(querySet, many=True,)
    print(dumps(serializer.data))
    return Response(serializer.data, status=200,)


@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = serializers.TaskDetailSerializer(instance=task)
        return Response(serializer.data, status=200)
    except Task.DoesNotExist:
        return Response(f'This task with {pk} does not exist!', status=404)


@api_view(['POST'])
def task_create(request):
    print(f'\n{request.data}\n!!!!!!!!!!!!!')
    serializer = serializers.TaskDetailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print(f'\n\n{serializer}\n\n')
    return Response(serializer.data, status=201)


@api_view(['PUT', 'PATCH'])
def task_update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = serializers.TaskDetailSerializer(instance=task, data=request.data)
        else:
            serializer = serializers.TaskDetailSerializer(instance=task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    except Task.DoesNotExist:
        return Response(f"This task with {pk} does not exist!', status=404")


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({'msg':'Successfully deleted!'}, status=204)
    except Task.DoesNotExist:
        return Response(f"This task with {pk} does not exist!", status=404)
