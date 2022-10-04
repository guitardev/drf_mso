
from django.contrib import admin
from django.urls import path ,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', views.TaskList.as_view()),
    path('api/tasks/<int:pk>', views.TaskDetail().as_view()),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
