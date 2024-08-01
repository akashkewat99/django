from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Book,Author

from . api.serializers import AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
# def test(request):
#     return HttpResponse("Sucess")


def main(request):
    return render(request,"bookApp/main.html",context=None)

# def books(request):
#     getAllBooks= Book.objects.all()
#     return render(request,'bookApp/index.html',{'getAllBooks':getAllBooks})

#from here applying django-rest Framework
#from here applying django-rest Framework
def books(request):
    getAllBooks= Book.objects.all().values()
    dataHere={
        'data':list(getAllBooks)
    } 
    return JsonResponse(dataHere)

# def author(request):
#     getAllAuthors= Author.objects.all()
#     print("Akash",getAllAuthors)
#     return render(request,'bookApp/authors.html',{'getAllAuthors':getAllAuthors})



@api_view(['GET','POST'])
def author(request):
    if request.method == 'GET':
        getAllAuthors= Author.objects.all()
        serializer = AuthorSerializer(getAllAuthors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# def authorDetail(request,id):
#     print(id)
#     getAuthorDetail=Author.objects.get(pk=id)
#     print(getAuthorDetail)
#     print("Akash")
#     getAuthorBooks=Book.objects.filter(author=id)
#     print(getAuthorBooks)
#     return render(request,"bookApp/authorDetail.html",{'author_name':getAuthorDetail.name,'authorBook':getAuthorBooks})

@api_view(['GET','PUT','DELETE'])
def getSingleauthorDetail(request,id):
    if request.method == 'GET':
            getAuthorDetail=Author.objects.get(pk=id)
            serializer=AuthorSerializer(getAuthorDetail)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        author = Author.objects.get(pk=id)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    

     


def bookDetails(request,id):
    getBookDetail=Book.objects.get(pk=id)
    return render(request,"bookApp/bookDetails.html",{"Book":getBookDetail})

