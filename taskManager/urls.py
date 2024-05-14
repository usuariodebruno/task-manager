from django.urls import path
from . import views

app_name = 'taskManager'

urlpatterns = [  
       
    path('registerTask/', views.RegisterTaskView.get, name='registerTask'),
    path('postRegisterTask/', views.RegisterTaskView.post, name='postRegisterTask'), 

    path('', views.GenericView.index, name='index'), 
    path('login/', views.GenericView.login, name='login'),
    path('listTask/', views.ListTaskView.get, name='listTasks'),   
 
]