# from .models import Task
# from rest_framework.response import Response
# from .serializers import TaskSerializer
# from rest_framework.views import APIView

# class ReadTask(APIView):
#     def get(self,request):
#         completed = request.GET.get("completed")
#         tasks = Task.objects.all()

#         if completed is not None:
#              is_completed = completed.lower() == "true"

#              tasks = Task.objects.filter(completed = is_completed)
#         serializer = TaskSerializer(tasks,many=True)
#         return Response(serializer.data)
    
# class ReadTask(APIView):
#     def get(self, request):
#         title_query = request.GET.get("title")
#         title = Task.objects.all()

#         if title_query is not None:
#              title = Task.objects.filter(title__icontains=title_query)
#         serializer = TaskSerializer(title,many=True)
#         return Response(serializer.data)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Task
# from .serializers import TaskSerializer
# from rest_framework import status

# class ReadTask(APIView):
#     def get(self, request):
  
#         completed = request.GET.get("completed")
#         title_query = request.GET.get("title")
        
#         tasks = Task.objects.all()

#         if completed is not None:
#             is_completed = completed.lower() == "true"
#             tasks = tasks.filter(completed=is_completed)  

#         if title_query is not None:
#             tasks = tasks.filter(title__icontains=title_query)  

    
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)



     

# class CreateTask(APIView):
#     def post(self,request):
#         serializer = TaskSerializer(data=request.data)

#         if serializer.is_valid():
#                 serializer.save()
#                 return Response(
#                      serializer.data, status=201
#                 )
#         return Response(serializer.errors, status=400)
    


# class PatchTask(APIView):
#      def patch(self,request,id):
#         try: 
#                course = Task.objects.get(id=id)
#         except Task.DoesNotExist:
#              return Response({
#                  "error" : "Task doesnot exist "
#              })
#         serializer = TaskSerializer(instance=course, data = request.data, partial = True)
#         if serializer.is_valid():
#              serializer.save()
#              return Response({
#                   "message": "Course updated"
#              })
#         return Response(serializer.errors)



# class DeleteTask(APIView):
#      def delete(self,request,id): 
#           try: 
#                task = Task.objects.get(id=id)
#           except: 
#                return Response({
#                 "message" : "Course doesnot exists "
#                })
#           task.delete()
#           return Response({
#                "message" : "Course deleted successfully"

     
#           })



from .models import Task,User
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class ReadCreateTask(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["title"]

    def perform_create(self, serializer): #else it will take what user sent
        serializer.save(owner=self.request.user) 

    def get_queryset(self):
        queryset = Task.objects.all()
        queryset = queryset.filter(owner=self.request.user)
        completed = self.request.GET.get("completed")
        ordering = self.request.GET.get("ordering")

        if completed is not None: 
            is_completed = completed.lower() == "true"
            queryset = queryset.filter(completed = is_completed)

       
        if ordering is not None: 
            queryset = queryset.order_by(ordering)

        return queryset






class UpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsOwner] #Because our serializer update() method does NOT update owner., # Usually we make fields like owner:read_only=True
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.select_related("owner") #the opeimization doesn't make a diff cause in serializer owner_id is stored not task.onwer.username
        queryset = queryset.filter(owner=self.request.user)
        return queryset 






# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin

# #maual how mixin works 
# class MixinExample(ListModelMixin,CreateModelMixin,GenericAPIView): 
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     def get(self,request): 
#         return self.list(request)
#     def post(self,request): 
#         return self.create(request)