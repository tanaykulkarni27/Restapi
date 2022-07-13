from django.shortcuts import render
from rest_framework import generics,mixins
from .models import BlogPost
from .serializer import PostSerializer

class RudAPIView(mixins.CreateModelMixin,generics.ListAPIView): #Retrieve update destroy 
    lookup_fielf = 'pk'
    serializer_class = PostSerializer
    # queryset = BlogPost.objects.all()
    def get_queryset(self):
        return BlogPost.objects.all()
    def perform_create(self,serializer):
        serializer.save(user = self.request.user)
    def post(self,req,*args,**kwargs):
        return self.create(req,*args,**kwargs)
class RudView(generics.RetrieveUpdateDestroyAPIView): #Retrieve update destroy 
    lookup_field = 'id'
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    def get_queryset(self):
        return self.queryset