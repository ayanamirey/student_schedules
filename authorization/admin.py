from django.contrib import admin
from authorization.models.users import MyUser

admin.site.register(MyUser)
