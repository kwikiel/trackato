from django.db import models

# Create your models here.

from django.db import models

class Treasure(models.Model):

		name = models.CharField(max_length=100)
		value = models.DecimalField(max_digits=10, decimal_places=2)

		def __str__(self):
				return self.name
