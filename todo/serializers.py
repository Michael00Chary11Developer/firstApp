from rest_framework import serializers
from .models import Todo


# class TodoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['id', 'title', 'content']


# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['id', 'title', 'content']
