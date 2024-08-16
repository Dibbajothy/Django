from django.contrib import admin
# from basicapp.models import Data
from basicapp.models import UserProfileInfo
# Register your models here.


# class MyAdmin(admin.ModelAdmin):
#     list_display = ('data_name', 'data_email', 'data_phone_number')

# admin.site.register(Data, MyAdmin)


admin.site.register(UserProfileInfo)


