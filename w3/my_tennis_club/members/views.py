from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Member
from .import models

# def members(request):
#   mymembers = Member.objects.all().values()
#   template = loader.get_template('members/all_members.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))

def members(request):
  mymembers=models.Member.objects.all() 
#   return render(request,'members/myfirst.html',context=None)
  return render(request,'members/all_members.html',{'mymembers':mymembers})
#   return render(request,'members/all_members.html',{'abc':mymembers})


# def details(request, id):
#   mymember = Member.objects.get(id=id)
#   template = loader.get_template('members/details.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))

def details(request,id):
    mymembers=models.Member.objects.get(id=id)
    return render(request,'members/details.html',{'mymembers':mymembers})

def main(request):
   return render(request,'members/main.html',context=None)

def testing(request):
   fruits=['Apple', 'Banana', 'Cherry']
   return render(request,'members/template.html',{'fruits':fruits})