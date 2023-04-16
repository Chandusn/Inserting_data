from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def display_topic(request):
   if request.method=='POST':
      tn=request.POST['tn']
      TO=Topic.objects.get_or_create(topic_name=tn)[0]
      TO.save()
      return HttpResponse("Topic name's are inserted successfully")
   return render(request,'display_topic.html')

def display_webpage(request):
   LTO=Topic.objects.all()
   d={'topics':LTO}

   if request.method=='POST':
      tn=request.POST['tn']
      n=request.POST['n']
      em=request.POST['em']
      u=request.POST['u']
      TO=Topic.objects.get(topic_name=tn)
      WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=em)[0]
      WO.save()
      return HttpResponse("Topic webpage's are inserted successfully")
   return render(request,'display_webpage.html',d)


def display_access(request):
   LTO=Webpage.objects.all()
   d={'webpage':LTO}

   if request.method=='POST':
      name=request.POST['name']
      author=request.POST['author']
      date=request.POST['date']
      WO=Webpage.objects.get(name=name)
      AO=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
      AO.save()
      return HttpResponse('inserted accessrecods')
   return render(request,'display_access.html',d)


def retrieve_data(request):
   LTO=Topic.objects.all()
   d={'topics':LTO}
   if request.method=='POST':
      td=request.POST.getlist('topic')
      print(td)
      webquery=Webpage.objects.none()
      for i in td:
         webquery=webquery|Webpage.objects.filter(topic_name=i)
      d1={'webpage':webquery}
      return render(request,'webpage.html',d1)
   return render(request,'retrieve_data.html',d)

def checkbox(request):
   LTO=Topic.objects.all()
   d={'topics':LTO}
   return render(request,'checkbox.html',d)

def radio(request):
   LTO=Topic.objects.all()
   d={'topics':LTO}
   return render(request,'radio.html',d)