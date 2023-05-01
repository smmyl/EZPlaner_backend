from rest_framework import serializers
from .models import Notes
from .models import Profile

class NotesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Notes
       fields = ('id', 'notes',)

class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
       model = Profile
       fields = ('id', 'name', 'zipcode')