from django.db import models

# Create your models here.
class Medication(models.Model):
    gespharx_id = models.IntegerField()
    din = models.CharField(max_length=30)
    generic_name = models.CharField(max_length=30)

    def __str__(self):
        return self.generic_name + ' ' + str(self.din)
    
