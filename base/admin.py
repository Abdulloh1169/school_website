from django.contrib import admin
from .models import ( Team, Subscribe, News, School_info, MySchool, Quote, OnlineService)


admin.site.register(School_info)
admin.site.register(Team)
admin.site.register(MySchool)
admin.site.register(Quote)
admin.site.register(News)
admin.site.register(OnlineService)
admin.site.register(Subscribe)




