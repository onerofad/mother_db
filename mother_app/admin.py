from django.contrib import admin
from .models import Register, MakeRequest, Support

# Register your models here.
admin.site.register({Register, MakeRequest, Support})
