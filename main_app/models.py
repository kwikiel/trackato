from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):

		name = models.CharField(max_length=14)
		balance =  models.DecimalField(max_digits=5, decimal_places=2)

		def __str__(self):
				return self.name
		def __repr__(self):
				return '<User {}, {} BTC>'.format(self.name, self.balance)

class Transaction(models.Model):

		amount = models.DecimalField(max_digits=5, decimal_places=2)
		sender = models.ForeignKey('User', related_name = 'sender')
		reciever = models.ForeignKey('User', related_name = 'reciever')

		def __str__(self):
				return 'Amount: {}, Sender: {} Reciever {}'.format(self.amount, self.sender, self.reciever)

