from django.urls import path
from akvap2.views import *


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.insertData, name='insertData'),
    path('', views.updateData, name='updateData'),
    path('', views.deleteData, name='deleteData'),
    path('', views.selectData, name='selectData'),
]
