import urlparse

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import fitbit
from app.models import Users
from app.models import Group
from app.models import Challenge
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.models import User
import webbrowser

# Create your views here.
'''
FITAPP_CONSUMER_KEY = '8cf83d9cc0be9d5ee42072ce55edf7a8'
FITAPP_CONSUMER_SECRET = 'b2293933b2b0e43cc4d04224e9cf53cd'
'''

FITAPP_CONSUMER_KEY = 'd781e18d924584fd4862904d11ad85e4'
FITAPP_CONSUMER_SECRET = '40723ad0a7c5e42142fabcab7c447711'

'''
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

    auth = fitbit.Fitbit(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET, resource_owner_key = owner_key, resource_owner_secret = owner_secret)
    profile = auth.user_profile_get(userid)

    username = profile.get('user').get('displayName')


    newUser = Users(user_id = userid, user_name = username, user_strength = 0,
                        user_agility = 0, user_willpower = 0, user_constitution = 0,
                        user_achievement = bin(0), token = owner_key,
                        token_secret = owner_secret, group = "None")
    newUser.save()


    now = datetime.datetime.now().strftime('%y%m%d')
    activity_stats = auth._COLLECTION_RESOURCE('activities', now, userid)
    time = activity_stats.get('goals').get('activeMinutes')

    return render_to_response('test.html', {"home" : userid,
                                                "token" : result,
                                                "client" : profile,
                                                "activity": activity_stats,
                                                "time" : time})
'''

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
    return render_to_response('register.html', args)
'''



def register_user(request):
    #url = request.build_absolute_uri(None)
    #form = UserCreationForm(request.POST)

    #parsed = urlparse.parse_qs(urlparse.urlparse(url).query)
    if request.method == "POST":
        print("IS THE FORM VALID")
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            print("YES IT IS")
            data = form.cleaned_data
            userid = data['username']
            print('USERID is ', userid)
            form.save()
            #print(userid)
            if userid != None:
                print("userid not None!!")

                owner_key = request.session.get('owner_key')
                owner_secret = request.session.get('owner_secret')
                newUser = Users(user_id = userid, user_name = "None", user_strength = 0,
                            user_agility = 0, user_willpower = 0, user_constitution = 0,
                            user_achievement = bin(0), token = owner_key,
                            token_secret=owner_secret, group = "None")

                newUser.save()

            return HttpResponseRedirect('/register_success')

    url = request.build_absolute_uri(None)
    parsed = urlparse.parse_qs(urlparse.urlparse(url).query)
    if(len(parsed)<1):
        client = fitbit.FitbitOauthClient(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
        token = client.fetch_request_token()
        request.session['token_no'] = token
        webbrowser.open(client.authorize_token_url())
        return render_to_response('register.html')

    else:
        client = fitbit.FitbitOauthClient(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET)
        token = request.session.get('token_no')
        listverifier = parsed['oauth_verifier']
        verifier = listverifier[0]
        result = client.fetch_access_token(verifier,token)
        userid = result.get('encoded_user_id')
        owner_key = result.get('oauth_token')
        owner_secret = result.get('oauth_token_secret')


        auth = fitbit.Fitbit(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET, resource_owner_key = owner_key, resource_owner_secret = owner_secret)
        profile = auth.user_profile_get(userid)
        request.session['owner_key'] = owner_key
        request.session['owner_secret'] = owner_secret


        #username = profile.get('user').get('displayName')

        '''
        newUser = Users(user_id = userid, user_name = username, user_strength = 0,
                            user_agility = 0, user_willpower = 0, user_constitution = 0,
                            user_achievement = bin(0), token = owner_key,
                            token_secret = owner_secret, group = "None")
        newUser.save()
        return HttpResponseRedirect
        '''




    return render(request,'register.html', {"userid": userid,
                                                "form" : UserCreationForm()})
def register_fitbit(request):
    return render_to_response('register_fitbit.html')

def register_success(request):
    return render_to_response('register_success.html')

def home(request):
    return render_to_response('home.html', {"home" : "Home Page"})


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
        return HttpResponseRedirect('/user')
    else:
        return HttpResponseRedirect('/invalid')

def invalid_login(request):
    return render_to_response('invalid.html')

def logout_view(request):
    logout(request)
    return render_to_response('logout.html')

def createGroup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        creator = request.user
        if name != "" and description != "":
            newGroup = Group(group_name = name, group_description=description,creator=creator,
                             member_2="None", member_3="None")
            newGroup.save()
            return HttpResponseRedirect('/createGroup_success')
        else:
            return HttpResponseRedirect('/createGroup_invalid')
    return render(request, 'CreateGroup.html', {})

def createGroup_success(request):
    return render_to_response('createGroup_success.html')

def createGroup_invalid(request):
    return render_to_response('createGroup_invalid.html')

def createChallenge(request):
    if request.method == "POST":
        gee = request.POST.get('gee', '')
        ger = request.user.username
        if User.objects.filter(username=gee).exists():
            newChallenge = Challenge(challenger = ger, challengee=gee, gerExp=0,
                                     geeExp=0,remain=7)
            newChallenge.save()
            return HttpResponseRedirect('/createChallenge_success')
        else:
            return HttpResponseRedirect('/createChallenge_invalid')
    return render(request, 'CreateChallenge.html', {})

def createChallenge_success(request):
    return render_to_response('createChallenge_success.html')

def createChallenge_invalid(request):
    return render_to_response('createChallenge_invalid.html')

def joinGroup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        try:
            exist = Group.objects.get(group_name=name) != "None"
        except Group.DoesNotExist:
            exist = False

        if exist:
            if Group.objects.get(group_name= name).member_2 == "None":
                print(Group.objects.get(group_name= name).member_2 == "None")
                group = Group.objects.get(group_name= name)
                group.member_2 = request.user.username
                group.save()
                user = Users.objects.get(user_id = request.user.username)
                user.group = name
                user.save()
                return HttpResponseRedirect('/join_success')
            elif Group.objects.get(group_name= name).member_3 == "None":
                group = Group.objects.get(group_name= name)
                group.member_3 = request.user.username
                group.save()
                user = Users.objects.get(user_id = request.user.username)
                user.group = name
                user.save()
                return HttpResponseRedirect('/join_success')
            else:
                return HttpResponseRedirect('/joinInvalid')
        return HttpResponseRedirect('/joinInvalid')
    return render(request, 'JoinGroup.html', {})

def join_invalid(request):
    return render_to_response('joinInvalid.html')

def join_success(request):
    return render_to_response('join_success.html')

def group_pg(request):
    group = Group.objects.all()
    return render_to_response('group_pg.html', {"group" : group})

def challenge_pg(request):
    name = request.user.username
    try:
        exist = Challenge.objects.get(challenger=name) != "None"
    except Group.DoesNotExist:
        exist = False

    if exist:
        challenge = Challenge.objects.get(challenger = name)
        gee = challenge.challengee
        gerExp = challenge.gerExp
        geeExp = challenge.geeExp
        remain = challenge.remain
        return render_to_response('challenge_pg.html', {"name" : name,
                                                     "challengee" : gee,
                                                     "gerExp" : gerExp,
                                                     "geeExp" : geeExp,
                                                     "remain" : remain})
    else:
        return  render_to_response('no_challenge.html')

def user_pg(request):
    name = request.user.username
    user = Users.objects.get(user_id = name)
    owner_key = user.token
    owner_secret = user.token_secret
    auth = fitbit.Fitbit(FITAPP_CONSUMER_KEY, FITAPP_CONSUMER_SECRET, resource_owner_key = owner_key, resource_owner_secret = owner_secret)
    profile = auth.user_profile_get(name)
    groupname = user.group

    agilevel = user.user_agility
    strlevel = user.user_strength
    willlevel = user.user_willpower
    constitution = user.user_constitution
    avatar = profile.get('user').get('avatar')
    try:
        exist = Group.objects.get(group_name=name) != "None"
    except Group.DoesNotExist:
        exist = False
    if exist:
        gee = Challenge.objects.get(challenger=name)
        challenge = gee.challengee
        return render_to_response('userpage.html', {"name" : name,
                                                 "avatar" : avatar,
                                                 "groupname" : groupname,
                                                 "challenge" : challenge,
                                                 "agilevel" : agilevel,
                                                 "strlevel" : strlevel,
                                                 "willlevel" : willlevel,
                                                 "constitution" : constitution})
    else:

        return render_to_response('userpage.html', {"name" : name,
                                                 "avatar" : avatar,
                                                 "groupname" : groupname,
                                                "challenge" : "You are currently not challenging anyone.",
                                                 "agilevel" : agilevel,
                                                 "strlevel" : strlevel,
                                                 "willlevel" : willlevel,
                                                 "constitution" : constitution})
