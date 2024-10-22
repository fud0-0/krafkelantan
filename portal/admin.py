from django.contrib import admin
from .models import Performance, Stall, Activity, StarredItem, Client, Feedback

admin.site.register(Client)
admin.site.register(Performance)
admin.site.register(Stall)
admin.site.register(Activity)
admin.site.register(StarredItem)
admin.site.register(Feedback)

