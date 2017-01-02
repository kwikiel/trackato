from django.contrib import admin
from .models import Treasure, Transaction, User
# Register your models here.
admin.site.register(Treasure)
admin.site.register(Transaction)
admin.site.register(User)
