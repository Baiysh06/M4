from django.shortcuts import HttpResponse
import datetime
def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello ! its my project')

def time(request):
    if request.method == 'GET':
        times = datetime.datetime.time()
        return HttpResponse(times)

def goodby(request):
    if request.method == "GET":
        return HttpResponse("goodby user")
