from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)


    class Meta:
        ordering = ['name']
        unique_together = (
            'name',
            'location',
            'phone_number'
        )

    def __str__(self):  # menyaet nazvanie ob'ekta
        return self.name

