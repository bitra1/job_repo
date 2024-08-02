from django.contrib import admin
from testapp.models import HydJobs,VijJobs,BangJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)


class VijJobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','address','email','phonenumber']
admin.site.register(VijJobs,VijJobsAdmin)


class BangJobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','address','email','phonenumber']
admin.site.register(BangJobs,BangJobsAdmin)
