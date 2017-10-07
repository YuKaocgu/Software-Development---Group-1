from django.contrib import admin

# Register your models here.
from Camper.models import Camper, Dorm, Band

admin.site.register(Camper)
admin.site.register(Dorm)
admin.site.register(Band)