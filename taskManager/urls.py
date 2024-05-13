from django.urls import path
from . import views

app_name = 'taskManager'

urlpatterns = [  
    path('registerTask/', views.RegisterTaskView.post, name='post'),
    path('', views.GenericView.index, name='index'), 
    path('login/', views.GenericView.login, name='login'),
    path('listTask/', views.ListTaskView.get, name='listTasks'),    
 
]