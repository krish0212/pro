from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin


# Register your models here.
 
#admin.site.register(User)
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    #list_display = ("name","age","city")
    pass