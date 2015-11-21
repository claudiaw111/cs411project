from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
import fitbit

import fitapp
from fitapp import views
from app.models import *
from django.shortcuts import render_to_response

# Create your views here.

# FITAPP_CONSUMER_KEY = '0b59e1fc7fb88458a9d5c68cbbbc3857'
# FITAPP_CONSUMER_SECRET = '7650c86938d928872c6e7367621afbc6'
# callback_url = 'http://127.0.0.1:8000/'

def test(request):
    unauth_client = fitbit.Fitbit('0b59e1fc7fb88458a9d5c68cbbbc3857',
                                  '7650c86938d928872c6e7367621afbc6',
                                  'http://127.0.0.1:8000/')
    return render_to_response('test.html', {"Testing" : unauth_client.food_units()})