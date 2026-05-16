from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.views import APIView

class ReadTask(APIView):
    def get(self,request):
        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)

class CreateTask(APIView):
    def post(self,request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
                serializer.save()
                return Response({
                     "message" : " Task Created "
                })
        return Response(serializer.errors)

class PatchTask(APIView):
     def patch(self,request,id):
        try: 
               course = Task.objects.get(id=id)
        except Task.DoesNotExist:
             return Response({
                 "error" : "Task doesnot exist "
             })
        serializer = TaskSerializer(instance=course, data = request.data, partial = True)
        if serializer.is_valid():
             serializer.save()
             return Response({
                  "message": "Course updated"
             })
        return Response(serializer.errors)

class DeleteTask(APIView):
     def delete(self,request,id): 
          try: 
               task = Task.objects.get(id=id)
          except: 
               return Response({
                "message" : "Course doesnot exists "
               })
          task.delete()
          return Response({
               "message" : "Course deleted successfully"
          })
          