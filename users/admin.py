from django.contrib import admin
from users.models import Notification, CustomUser


admin.site.register(Notification)
admin.site.register(CustomUser)
