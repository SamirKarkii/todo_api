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

#checks credentials, authenticates user, generates acces token/refresh token , and returns response 
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework_simplejwt.views import TokenRefreshView #to generate new accesss token using refresh token 

urlpatterns = [
    path("tasks/", ReadCreateTask.as_view()),
    path("tasks/<int:pk>/", UpdateDelete.as_view()),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view())
]
