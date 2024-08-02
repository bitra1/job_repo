from django.shortcuts import render
from testapp.models import HydJobs,VijJobs,BangJobs
# Create your views here.
def jobs_info(request):
    return render(request,'testapp/index.html')

def Hyd_info(request):
    hyd = HydJobs.objects.all()
    my_dict = {'hyd':hyd}
    return render(request,'testapp/hydjobs.html',my_dict)


def Vij_info(request):
    vij = VijJobs.objects.all()
    my_dict = {'vij':vij}
    return render(request,'testapp/vijjob.html',my_dict)

def bang_info(request):
    bang = BangJobs.objects.all()
    my_dict = {'bang':bang}
    return render(request,'testapp/bang.html',my_dict)
