from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    id = models.CharField(max_length=10, primary_key=True)  # JE1, VS1
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}, {self.name}"

class Module(models.Model):
    code = models.CharField(max_length=10, primary_key=True)  # CD1, PG1
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} {self.name}"

class ModuleInstance(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()
    professors = models.ManyToManyField(Professor)

    def __str__(self):
        return f"{self.module.code} {self.year} Semester {self.semester}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module_instance = models.ForeignKey(ModuleInstance, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"Rating {self.rating} for {self.professor.id} by {self.user.username}"
