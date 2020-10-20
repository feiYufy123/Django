from django.db import models

# Create your models here.


class UserInfor(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    location = models.CharField(max_length=64)
    wen = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = "info_ation"
