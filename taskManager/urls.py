from django.urls import path
from . import views

app_name = 'taskManager'

urlpatterns = [  
       
    path('registerTask/', views.RegisterTaskView.get, name='registerTask'),
    path('postRegisterTask/', views.RegisterTaskView.post, name='postRegisterTask'),     
    path('listTask/', views.ListTaskView.get, name='listTasks'),
    path('deleteTask/<int:taskID>', views.DeleteTaskView.post, name='deleteTask'), 

    path('', views.GenericView.index, name='index'), 
    path('login/', views.GenericView.login, name='login'),  
 
]