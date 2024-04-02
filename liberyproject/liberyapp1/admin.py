from django.contrib import admin

from liberyapp1.models import Book,CustomUser

#register table in admin
admin.site.register(Book)
admin.site.register(CustomUser)
