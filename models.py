from django.db import models
class Officer(models,Model):
    Name=models.CharField(max_length=10)
    Cadre=models.CharField(max_length=10)
    Allotmentyear=models.IntegerField()
    DOB=models.Charfield(max_length=10)

    def __str__(self):
        return self.Name
        return self.Cadre
        return self.Allotmentyear
        return self.DOB
