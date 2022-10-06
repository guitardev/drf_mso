from django.contrib import admin
from .models import PersonGov60,PersonHouse


@admin.register(PersonHouse)
class PersonHouseAdmin(admin.ModelAdmin):
    list_display = ['house_code','house_addr']

@admin.register(PersonGov60)
class PersonGov60Admin(admin.ModelAdmin):
    list_display = ['nnid','house_code','title','f_name','l_name','sex','birth_date','body_code']
        
