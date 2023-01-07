from django.shortcuts import render , redirect
#from django.http import HttpResponse
from akva.resources import UserResource
from django.core.files.storage import FileSystemStorage
from http.client import HTTPResponse
from tablib import Dataset
from .models import User
import csv
# Create your views here.
def index(request):   
    return render(request,"index.html")  
 
def Import(request):
    if request.method == 'POST' :
        print("post method")
        User = UserResource()
        print("User",User)
        dataset = Dataset(headers = ['name','age','city'])        
        print("dataset",dataset)
        newuser = request.FILES
        user1=newuser['newuser']
        print("user1",user1)
        #data_import = dataset.load(open("newuser.csv").read())
        data_import =  dataset.load(open('C:/Users/ELCOT/Downloads/newuser.csv').read(),format='csv')
        print("data_import",data_import)
        result = User.import_data(dataset,dry_run=True)
        print("result",result)
        if not result.has_errors():
            User.import_data(dataset,dry_run=False)        
    return render(request, 'Import.html')


 
