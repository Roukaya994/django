from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
class AppointmentStacked(admin.StackedInline):
    model = Appointment
    extra = 1
    class DoctorPerClass(admin.ModelAdmin):
        inlines = [AppointmentStacked,]
        admin.site.register(Doctor,DoctorPerClass)



admin.site.register(Patient)
admin.site.register(Speciality)
