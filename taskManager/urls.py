from django.urls import path
from . import views

app_name = 'taskManager'

urlpatterns = [  
    path('registerTask/', views.RegisterTaskView.post, name='post'),
    path('', views.GenericView.index, name='index'),  
]