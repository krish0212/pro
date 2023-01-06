#from django.contrib import admin  
from django.urls import path  
from akva1 import views
#from akva1.views import index
#from akva1.views import student_csv

urlpatterns = [  
    #path('admin/', admin.site.urls),
    path('index/', views.index),
    path('student_csv/', views.student_csv),
]
