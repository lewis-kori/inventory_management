from django.contrib import admin
from .models import Category,Item,Transaction,Client
# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Transaction)