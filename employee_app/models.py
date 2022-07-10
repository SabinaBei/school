from django.db import models
from courses_app.models import Course


class Position(models.Model):
    name = models.CharField(max_length=155)
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=255)
    permission = models.CharField(max_length=155)
    id_department = models.CharField(max_length=155)


    class Meta:
        ordering = ['name']
        unique_together = (
            'name',
            'duration',
            'description',
            'permission'
        )

    def __str__(self):
        return self.name


class Employee(models.Model):
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
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course = models.ManyToManyField(Course)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    school = models.CharField(max_length=155, null=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)

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
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name


class Department(models.Model):
    name = models.CharField(max_length=155)
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=255)


    class Meta:
        ordering = ['name']
        unique_together = (
            'name',
            'duration',
            'description'
        )

    def __str__(self):
        return self.name
