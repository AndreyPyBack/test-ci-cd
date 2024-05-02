from django.contrib import admin
from .models import Profile,Car,Product,Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Car)
admin.site.register(Product)
admin.site.register(Comment)