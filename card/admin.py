from django.contrib import admin

from card.models import Card, WhyStop, WhyEat, WhyLook, MyHistory, ZoneRelax, Proiz, Question

# Register your models here.
admin.site.register(WhyStop)
admin.site.register(WhyEat)
admin.site.register(WhyLook)
admin.site.register(MyHistory)
admin.site.register(ZoneRelax)
admin.site.register(Proiz)
admin.site.register(Question)
