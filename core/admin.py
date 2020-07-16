from django.contrib import admin
from .models import Profile, Journal, Comment, Foll

# Register your models here.
admin.site.register(Profile)
admin.site.register(Journal)
admin.site.register(Comment)
admin.site.register(Foll)
