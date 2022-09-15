from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ipModel)
admin.site.register(Announcement)
admin.site.register(Notification)
admin.site.register(Eligility_Conditions)
admin.site.register(Eligility_Conditions_PF_SP)
admin.site.register(Results)

