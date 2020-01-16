from django.shortcuts import render
from django.http import HttpResponse
import csv,io

from .models import Deepak

# Create your views here.
def index(request):
    

    if request.method== "GET":
        return render(request, 'temp/index.html')
    

    csv_file - request.FILES['files']
    if not csv_file.name.endswith('csv'):
        return render(request, 'temp/index.html')
        
    
    data_set = csv_file.read().decode('UTF-8')
    io_string =io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',',  quotchar="|"):
        _,created = Deepak.objects.update_or_create(
            phone=column[0],
            email=column[1],
            firstname=column[2],
            lastname=column[3],
            role=column[4],
            username=column[5],
            isActive=column[6],
            _created_at=column[7],
            _uploaded_at=column[8]

        )
def processed(request):
    #if request.method=='POST':
        #text=request.POST['text']
       # processed=text.upper()
    return render(request,'temp/column.html')


def process1(request):
    return render(request, 'temp/data.html')

