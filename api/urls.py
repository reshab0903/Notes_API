from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes),
    path('notes/',views.getNotes),
    path('notes/<int:pk>/',views.getNote),
     path('notes/create/',views.createNote),
     path('notes/update/<int:pk>/',views.updateNote),
     path('notes/delete/<int:pk>/',views.deleteNote),
]