from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    template = loader.get_template('main/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
