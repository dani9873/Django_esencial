"""Platzigram views."""
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    # now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('OH, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs') #now
        ))

def sorted_integers(request):
    """Return a JSON response with sorted integers."""
    # print(request)
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data ={
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    #import pdb; pdb.set_trace() #Debugger que se detendra has que apachemos la tecla c.
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type ='application/json'
        )
    
def say_hi(request,name, age):
    """Return a greeting"""
    if age <12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
