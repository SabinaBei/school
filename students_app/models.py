from django.db import models
from courses_app.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    FEMALE = 'F'
    MALE = 'M'
    GENDER_CHOICES = [(FEMALE, 'Female'),(MALE, 'Male'),]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['first_name']
        unique_together = (
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',
            'email',
        )

#imya i familiya s zaglavnoi bukvi
    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name