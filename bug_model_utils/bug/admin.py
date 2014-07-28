from django.contrib import admin
from .models import Foo

# Register your models here.

class FooAdmin(admin.ModelAdmin):
    pass

admin.site.register(Foo, FooAdmin)
