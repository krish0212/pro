#from django.contrib import admin  
from django.urls import path  
from akva import views
#from Import import settings
#from django.conf.urls.static import static

urlpatterns = [  
    #path('admin/', admin.site.urls),
    path('index/', views.index),
    #path('export/', views.export, name='export'),
    path('Import',views.Import,name="Import"),

] 
