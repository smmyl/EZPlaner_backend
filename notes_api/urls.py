from django.urls import path
from . import views

urlpatterns = [
   path('api/notes', views.NotesList.as_view(), name='notes_list'),
   path('api/notes/<int:pk>', views.NotesDetail.as_view(), name='notes_detail'),
   path('api/profile', views.ProfileList.as_view(), name='profile_list'),
   path('api/profile/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
]
