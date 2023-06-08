from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from myapp.views import *


# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

    def get(self, request, *args, **kwargs):
       result = []
       if not result:
           print('error')
       context = {}
       return render(request, 'index.html', context=context)
