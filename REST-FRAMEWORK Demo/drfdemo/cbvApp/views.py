
from django.http import HttpResponse
from rest_framework.views import APIView
from . models import StudentModel
from .api.serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status,mixins,generics
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
# Create your views here.

def temp(request):
    return HttpResponse("Done")




#####class based view
# class StudentList(APIView):
#     def get(self,request):
#         students = StudentModel.objects.all()
#         serializer = StudentSerializers(students,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#####PRIMARY key operation
# class StudentDetails(APIView):

#     def get_object(self,pk):
#         try:
#             return StudentModel.objects.get(pk=pk)
#         except StudentModel.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializers(student)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self, request,pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializers(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
                        
    

# #mixins

# #   Action Methods   #Mixin classes      #Handler Methods
# #   list()           ListModelMixin       get()
# #   create()         CreateModelMixin     post()
# #   retrieve()       RetrieveModelMixin   get()
# #   update()         UpdateModelMixin     put()
# #   destroy()        DestroyModelMixin    delete()


# class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializers

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    

# class StudentDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializers

#     def get(self,request,pk):
#         return self.retrieve(request)

#     def put(self,request,pk):
#         return self.update(request)
    
#     def delete(self,request,pk):
#         return self.destroy(request)




###########Generic
class customPagination(PageNumberPagination):
    page_size=2

class StudentList(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
    pagination_class = customPagination

class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
