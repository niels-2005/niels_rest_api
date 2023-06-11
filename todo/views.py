from django.shortcuts import render
from .models import Todo
from rest_framework import viewsets, serializers
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(
            title=self.request.POST.get("title", ""),
            description=self.request.POST.get("description", ""),
            user=self.request.user,
        )
        serialized_obj = serializers.serialize("json", [todo])
        return HttpResponse(serialized_obj, content_type="application/json")
