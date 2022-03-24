from django.shortcuts import render
from django.http import HttpResponse
import json
from datetime import datetime


def index(request):
    data = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "hostname": request.get_host() ,
    "engine": "django",
    "visitor ip": get_client_ip(request)
    }

    # serialize data obj as a JSON stream 
    data = json.dumps(data)
    print(data)
    response = HttpResponse(data, content_type='application/json charset=utf-8')

    # add filename to response
    #response['Content-Disposition'] = 'attachment; filename="filename.json"'
    return response

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip