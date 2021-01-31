from django.contrib import admin
from farms.models import Trainer, Babysitter, GymMember

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Babysitter)
admin.site.register(GymMember)