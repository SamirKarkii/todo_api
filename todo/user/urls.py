# from django.urls import path
# from .api_view import ReadTask,CreateTask,PatchTask,DeleteTask

# urlpatterns = [
#     path("tasks/", ReadTask.as_view()),
#     path("course-post/", CreateTask.as_view()),
#     path("course-patch/", PatchTask.as_view()),
#     path("course-delete/", DeleteTask.as_view())
    
# ]



from django.urls import path
from .api_view import ReadCreateTask,UpdateDelete

urlpatterns = [
    path("tasks/", ReadCreateTask.as_view()),
    path("tasks/<int:pk>/", UpdateDelete.as_view())
]
