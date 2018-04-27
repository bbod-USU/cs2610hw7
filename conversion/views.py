from django.shortcuts import render
from django.http import HttpResponse
from conversion.models import Converter
import math
import json


# Create your views here.
def get(request):
    print(request)
    value = request.GET.get('value')
    frm = request.GET['from']
    to = request.GET['to']
    print(value, " ", to, " ", frm)
    tmp = Converter.objects.get(units=frm)
    print(tmp)
    total = tmp.value * float(value)
    print(str(total))

    data = {}
    data['units'] = to
    data['value'] = total
    json_data = json.dumps(data)
    print(json_data)
    return HttpResponse(json_data)

def init(request):
    Converter.objects.all().delete();
    this = Converter(units='lbs', value='14.5833')
    this.save()

    return HttpResponse('Data Base Initialized')
