from django.shortcuts import render
from django.http import HttpResponse
from akva1.models import User
import csv

# Create your views here.
def index(request):   
    return render(request,"index.html")  

def student_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student.csv"'
    #print("before calling writer")
    
    users = User.objects.all()  
    writer = csv.writer(response)
    writer.writerow(['name', 'age', 'city'])
    #print("after the writer")
    
    for user in users:
        writer.writerow([user.name,user.age,user.city])
    return response