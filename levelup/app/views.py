from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import fitbit
from django.template import RequestContext

import fitapp
import fitbitapi
from fitapp import views
from app.models import Users
from app.models import Group
from app.models import Challenge
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.models import User

# Create your views here.

FITAPP_CONSUMER_KEY = '8cf83d9cc0be9d5ee42072ce55edf7a8'
FITAPP_CONSUMER_SECRET = 'b2293933b2b0e43cc4d04224e9cf53cd'

callback_url = 'http://localhost/callback'

client_id = '22B3QN'


import urlparse

import os
import pprint
import sys
import webbrowser

import urllib2
import requests

userid = ""
username = ""
owner_key = ""
owner_secret = ""

def auth(request):


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


    #auth = fitbit.Fitbit(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
    auth = fitbit.Fitbit(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET, resource_owner_key = owner_key, resource_owner_secret = owner_secret)
    profile = auth.user_profile_get(userid)

    username = profile.get('user').get('displayName')

    #if not(Users.objects.filter(user_id = "user_id").exists()):

    '''
    newUser = Users(user_id = userid, user_name = username, user_strength = 0,
                        user_agility = 0, user_willpower = 0, user_constitution = 0,
                        user_achievement = bin(0), token = owner_key,
                        token_secret = owner_secret, group = "None")
    newUser.save()
    '''

    now = datetime.datetime.now().strftime('%y%m%d')
    activity_stats = auth._COLLECTION_RESOURCE('activities', now, userid)
    time = activity_stats.get('goals').get('activeMinutes')

    return render_to_response('test.html', {"home" : userid,
                                                "token" : result,
                                                "client" : profile,
                                                "activity": activity_stats,
                                                "time" : time})

    '''
    return render_to_response('home.html', {"home" : token,
                                            "token" : client.authorize_token_url(),
                                            "client" : username})
    '''

'''
def createUser(request):
    if request.method == "GET":
        form = CreateUserForm
        return render(request, 'create.html', {'form': form})
    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        form.save()
        return HttpResponseRedirect('/home')
'''
'''
def createUser(request):
    if request.method == "GET":
        form = CreateUserForm
        return render(request, 'create.html', {'form': form})
    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        form.save()
        return HttpResponseRedirect('/login')
'''

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    print args
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def home(request):
    return render_to_response('home.html', {"home" : "Home Page"})

'''
def login_view(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        print("user: ", username)
        print("pass: ", password)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #this should be user home page
                return HttpResponseRedirect('/home')
                #state = "You're successfully logged in!"
            else:
                #return HttpResponse("The password is valid, but the account has been disabled!")
                state = "The password is valid, but the account has been disabled!"
        else:
            #return HttpResponse("The username and password were incorrect.")
            state = "Your username and/or password were incorrect."
    return render_to_response('auth.html',{'state':state, 'username': username}, context_instance=RequestContext(request))
'''

def user_login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/invalid')

def invalid_login(request):
    return render_to_response('invalid.html')

def logout_view(request):
    logout(request)
    '''this should be login page'''
    return HttpResponseRedirect('/home')



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


def test(request):

    unauth_client = fitbit.Fitbit('0b59e1fc7fb88458a9d5c68cbbbc3857',
                                  '7650c86938d928872c6e7367621afbc6',
                                  'http://127.0.0.1:8000/')
    return render_to_response('test.html', {"Testing" : unauth_client.food_units()})


    client = fitbit.FitbitOauthClient(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
    token = client.fetch_request_token()
    verifier = client.authorize_token_url()
    #verifier = '65e089e405cb0cfa2170dadd3350a20f'
    #response = client.fetch_access_token(verifier, token)
    return render_to_response('test.html', {"response" : verifier})
'''

def createGroup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        creator = userid
        if name != "" and description != "":
            newGroup = Group(group_name = name, group_description=description,creator=creator,
                             member_2="None", member_3="None")
            newGroup.save()
            return HttpResponseRedirect('/home')
    return render(request, 'CreateGroup.html', {})

def createChallenge(request):
    if request.method == "POST":
        gee = request.POST.get('gee', '')
        ger = userid
        if User.objects.filter(username=gee).exists():
            #print("AAAAAAAAAAAAAAAA")
            newChallenge = Challenge(challenger = ger, challengee=gee, gerExp=0,
                                     geeExp=0,remain=7)
            newChallenge.save()
            return HttpResponseRedirect('/home')
        #print("here")
    return render(request, 'CreateChallenge.html', {})

def joinGroup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        if Group.objects.get(group_name=name).creator != "None":
            #description = Group.objects.filter(group_name=name).group_description
            #creator = Group.objects.filter(group_name=name).creator
            #newMember = Group(group_name = name, group_description= description, creator =

            if Group.objects.get(group_name= name).member_2 == "None":
                print(Group.objects.get(group_name= name).member_2 == "None")
                group = Group.objects.get(group_name= name)
                group.member_2 = userid
                group.save()
                user = Users.objects.get(user_id = userid)
                user.group = name
                user.save()
                print ("Join success")
            elif Group.objects.get(group_name= name).member_3 == "None":
                group = Group.objects.get(group_name= name)
                group.member_3 = userid
                group.save()
                user = Users.objects.get(user_id = userid)
                user.group = name
                user.save()
                print ("Join success")
            else:
                print ("Cannot join group. group full")

    return render(request, 'JoinGroup.html', {})