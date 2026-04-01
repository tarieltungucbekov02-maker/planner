from rest_framework import viewsets
from rest_framework import serializers
from .models import Task

# Сериализатор для модели Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'due_date']

# ViewSet для API
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer