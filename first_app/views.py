from django.shortcuts import render
# connecting views to database
from first_app.models import Topic, AccessRecord, Webpage
from django.http import HttpResponse


# Create your views here.

def index(request):
    # making the entries of AccessRecord arrange in ascending order
    webpages_List = AccessRecord.objects.order_by('date')
    webpage = Webpage.objects
    return render(request, 'first_app/index.html',{'ws': webpage,'access_records': webpages_List})
    # my_dict = {'insert_me': "Hello I am from views.py !"}
    # return render(request, 'first_app/index.html', context=my_dict)


def home(request):
    return render(request, 'personal/home.html')
