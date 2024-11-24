from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Politician
from django.urls import reverse
# Create your views here.
def hellofunc(request):
   return HttpResponse("やっほー")

def index(request):
   latest_politician_list = Politician.objects.order_by('-pub_date')[:5]
   print(latest_politician_list)
   context = {'latest_politician_list': latest_politician_list}
   return render(request, 'politicians/index.html', context)

def detail(request, politician_id):
#    latest_politician_list = Politician.objects.order_by('-pub_date')[:5]
#    politician = get_object_or_404(Politician, pk=politician_id)
#    context = {'latest_politician_list': latest_politician_list}
#    return render(request, 'politicians/detail.html', context)
#    return HttpResponse("you are looking at question %s" % politician_id)
    politician = get_object_or_404(Politician, pk=politician_id)
    return render(request, 'politicians/detail.html', {'politician': politician})
