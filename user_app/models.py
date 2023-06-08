from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField()

    def age(self):
        from datetime import date
        current_year = date.today().year
        return current_year - self.birth_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
