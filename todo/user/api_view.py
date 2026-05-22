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



from .models import Task
from .serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

class ReadCreateTask(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["title"]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        completed = self.request.GET.get("completed")
     #    title = self.request.GET.get("title")
        ordering = self.request.GET.get("ordering")

        if completed is not None: 
            is_completed = completed.lower() == "true"
            queryset = queryset.filter(completed = is_completed)

     #    if title is not None:  
     #        queryset = queryset.filter(title__icontains=title)
       
        if ordering is not None: 
            queryset = queryset.order_by(ordering)

        return queryset




class UpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

