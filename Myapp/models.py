from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table="member"

    def __str__(self):
        return self.firstname + ' ' + self.lastname


