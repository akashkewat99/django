from django.shortcuts import render
from django.http import HttpResponse
from . models import Book,Author

# Create your views here.
# def test(request):
#     return HttpResponse("Sucess")


def main(request):
    return render(request,"bookApp/main.html",context=None)

def books(request):
    getAllBooks= Book.objects.all()
    return render(request,'bookApp/index.html',{'getAllBooks':getAllBooks})

def author(request):
    getAllAuthors= Author.objects.all()
    print("Akash",getAllAuthors)
    return render(request,'bookApp/authors.html',{'getAllAuthors':getAllAuthors})


def authorDetail(request,id):
    print(id)
    getAuthorDetail=Author.objects.get(pk=id)
    print(getAuthorDetail)
    print("Akash")
    getAuthorBooks=Book.objects.filter(author=id)
    print(getAuthorBooks)
    return render(request,"bookApp/authorDetail.html",{'author_name':getAuthorDetail.name,'authorBook':getAuthorBooks})


def bookDetails(request,id):
    getBookDetail=Book.objects.get(pk=id)
    return render(request,"bookApp/bookDetails.html",{"Book":getBookDetail})

