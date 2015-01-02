from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from forms import LoginForm
from django.contrib.auth.decorators import login_required



#Views dealing with logging in and out users
def login(request):
    """Used to login users and direct them to their main profile page"""
    
    #Check to see if the user has tried to submit login information
    if request.method == "POST":
        form = LoginForm(request.POST)
            
        if form.is_valid():
            
            #Extract the username and password from the form data submitted.
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']

            #Check to see if the user is already authenticated.
            user = auth.authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    
                    #If all checks pass, direct them to their profile page.
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('sysadmin_home'))

                else:
                    return render_to_response('login.html',
                        {'form':form,
                        'errmessage':'Login or Password Invalid!'},
                        context_instance = RequestContext(request))
            
            #If there is either the username does not exist, or if either the
            #username or password are wrong, then return a blank login form
            form = LoginForm()
            return render_to_response('login.html',
                {'form':form,
                'errmessage':'Login or Password Invalid!'},
                context_instance = RequestContext(request))
                
    #If the request is not a post request, return a blank login form.
    else:
        form = LoginForm()
        
    return render_to_response('login.html', 
                {'form':form},
                context_instance = RequestContext(request))

def logout(request):
    """Registers that the user has logged out and returns them to the landing
    page."""
    
    auth.logout(request)
    return HttpResponseRedirect("/")