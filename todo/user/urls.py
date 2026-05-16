from django.urls import path
from .api_view import ReadTask,CreateTask,PatchTask,DeleteTask

urlpatterns = [
    path("course-get/", ReadTask.as_view()),
    path("course-post/", CreateTask.as_view()),
    path("course-patch/", PatchTask.as_view()),
    path("course-delete/", DeleteTask.as_view())
    
]