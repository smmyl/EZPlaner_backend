from django.shortcuts import render
from rest_framework import generics
from .serializers import NotesSerializer
from .serializers import ProfileSerializer
from .models import Notes
from .models import Profile

# Create your views here.
class ProfileList(generics.ListCreateAPIView):
   queryset = Profile.objects.all().order_by('id')
   serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Profile.objects.all().order_by('id')
   serializer_class = ProfileSerializer

class NotesList(generics.ListCreateAPIView):
   queryset = Notes.objects.all().order_by('id')
   serializer_class = NotesSerializer

class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Notes.objects.all().order_by('id')
   serializer_class = NotesSerializer