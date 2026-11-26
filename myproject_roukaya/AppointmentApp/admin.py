from django.contrib import admin
from .models import Appointment
# Register your models here.
#admin.site.register(Appointment)
def confirm_appointment(model, req, queryset):
    queryset.update(status='CONFIRMED')
@admin.register(Appointment)
class AppointmentAdminPers(admin.ModelAdmin):
    actions = [confirm_appointment]
    list_display = ('id', 'reason', 'status', 'duration_minutes', 'created_at', 'updated_at', 'appointment_date', 'doctor', 'patient')
    list_filter = ('status', 'appointment_date')
    list_editable = ('status',)
    search_fields = ('reason','status')
    ordering = ('-appointment_date',)
    list_per_page = 2
    fieldsets = (
        ('description', {
            'fields': ('reason', 'prescription', 'status')
        }),
        ('date + duration', {
            'fields': ('appointment_date', 'duration_minutes')
        }),
        ('doctor + patient', {
            'fields': ('doctor', 'patient')
        }),
        ('planification', {
            'fields': ('created_at', 'updated_at')
        }),
       
    )
    readonly_fields = ('created_at', 'updated_at')