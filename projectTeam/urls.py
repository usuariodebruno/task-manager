from django.contrib import admin
from django.urls import path, include
import taskManager.urls

urlpatterns = [    
    path('', include(taskManager.urls)),
    path('admin/', admin.site.urls),
]
