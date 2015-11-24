from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse
import fitbit

import fitapp
import fitbitapi
from fitapp import views
from app.models import *
from django.shortcuts import render_to_response

# Create your views here.

FITAPP_CONSUMER_KEY = '8cf83d9cc0be9d5ee42072ce55edf7a8'
FITAPP_CONSUMER_SECRET = 'b2293933b2b0e43cc4d04224e9cf53cd'
#FITAPP_CONSUMER_KEY = '0b59e1fc7fb88458a9d5c68cbbbc3857'
#FITAPP_CONSUMER_SECRET = '7650c86938d928872c6e7367621afbc6'

callback_url = 'http://localhost/callback'

client_id = '22B3QN'


import urlparse

import os
import pprint
import sys
import webbrowser

import urllib2
#from BeautifulSoup import BeautifulSoup
import requests

userid = ""
owner_key = ""
owner_secret = ""

def home(request):


    client = fitbit.FitbitOauthClient(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
    token = client.fetch_request_token()
    print ("Sign up for fitbit account if you do not have one")
    print ("Please copy the oauth_verifier from the URL")
    webbrowser.open(client.authorize_token_url())
    verifier = raw_input('Verifier: ')
    result = client.fetch_access_token(verifier)
    userid = result.get('encoded_user_id')
    owner_key = result.get('oauth_token')
    owner_secret = result.get('oauth_token_secret')

    return render_to_response('home.html', {"home" : "Hello",
                                            "token" : owner_key,
                                            "client" : result})

    '''
    client = fitbit.FitbitOauthClient(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
    token = client.fetch_request_token()
    url = client.authorize_token_url()
    '''

    '''
    response = urllib2.urlopen(url)
    newurl = response.geturl()
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    for anchor in soup.findAll('a', href=True):
        print anchor['href']
    '''
    #opener = urllib2.build_opener()
    #f = opener.open(request)
    '''
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(url)
    newurl = request.url
    '''

    #newurl = requests.get(url).response.url
    '''
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib2.install_opener(opener)
    newurl = opener.open(url).url

    #newurl = requests.head(url).url

    uri = urlparse.urlparse(newurl)
    verifier = urlparse.parse_qs(uri.query)
    #response = client.fetch_access_token(verifier)

    return render_to_response('home.html', {"home" : "Hello",
                                                "token" : newurl,
                                                "client" : verifier})
    '''

def test(request):
    '''
    unauth_client = fitbit.Fitbit('0b59e1fc7fb88458a9d5c68cbbbc3857',
                                  '7650c86938d928872c6e7367621afbc6',
                                  'http://127.0.0.1:8000/')
    return render_to_response('test.html', {"Testing" : unauth_client.food_units()})
    '''

    client = fitbit.FitbitOauthClient(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
    token = client.fetch_request_token()
    verifier = client.authorize_token_url()
    #verifier = '65e089e405cb0cfa2170dadd3350a20f'
    #response = client.fetch_access_token(verifier, token)
    return render_to_response('test.html', {"response" : verifier})


