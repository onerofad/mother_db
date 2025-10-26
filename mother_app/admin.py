from django.contrib import admin
from .models import Register, MakeRequest

# Register your models here.
admin.site.register({Register, MakeRequest})
