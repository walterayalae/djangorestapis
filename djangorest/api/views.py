from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializeer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView):

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializeer

    def perform_create(self, serializer):

        serializer.save()

# Create your views here.
