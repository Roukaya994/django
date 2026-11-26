from django.db import models
from AccountApp.models import Doctor,Patient
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class appointment (models.Model):
    reason=models.TextField()
    prescription =models.FileField(
        blank = True,
        upload_to='prescriptions/'

    )
    class Status( models.TextChoices):
       PENDING="PENDING","En attente"
       CONFIRMED="CONFIRMED","confirme"
       CANCELLED="CANCELLED","annule" 

    status = models.CharField(max_length=10, choices=Status.choices,default=Status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField()
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='appointments')
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointment')
    def clean(self):
        modified_date = self._state.adding or (
            Appointment.objects.filter(
            pk=self.pk,
            appointment_date = self.appointment_date,
        ).exists()
        )
        if self.appointment_date < timezone.now():
            raise ValidationError("la date du rendez-vous doit etre superieur a la date actuelle")
    class Meta:
        ordering = ['-appointment_date']
        constraints = [
            models.UniqueConstraint(
            fields=["doctor","appointment_date"],
            name="unicite patient doctor date",
            violation_error_message = "un patient ne peut pas avoir deux rendez-vous avec le meme docteur a la meme date"
            )
        ]
    def __str__(self):
        return f"le rdv et pour le raison {self.reason} "