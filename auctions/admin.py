from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(listings)
admin.site.register(bids)
admin.site.register(comments)