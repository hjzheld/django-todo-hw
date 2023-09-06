from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:todo_id>/', views.read),  
    path('create/', views.create),
    path('update/<int:todo_id>/', views.update),
    path('mytodo/', views.mytodo),
]