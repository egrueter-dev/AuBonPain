# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.translation import ugettext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson
from models import Invitation, InviteRequest
from invite_registration.forms import InvitationForm
from invite_registration.invite_registration_settings import REDIRECT_URL
from invite_registration.forms import InvitationForm, RegistrationFormInvitation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def home_beta(request, form_class=InvitationForm):
    import json
    invitationForm = InvitationForm(data=None)
    registrationForm = RegistrationFormInvitation(data=request.POST or None)
    loginForm = AuthenticationForm(data=request.POST or None)
    """
    Allow a user to request an invite at a later date by entering their email address.
    """
    if request.method == 'POST':
        print request.POST
        form = form_class(request.POST)
        if form.is_valid():
            email = request.POST['email']
            request, created = InviteRequest.objects.get_or_create(email=request.POST['email'])
            if created:
                response = ({'created' : 'success', 'not_created': 'no'})
            if not created:
                response = ({'created' : 'false', 'not_created' : 'yes'})

            data = json.dumps(response)
            return HttpResponse(data, content_type="application/json")
        else:
            if not request.is_ajax():
                return HttpResponseRedirect(REDIRECT_URL)
            response = ({'success':False})
            json = json.dumps(response, ensure_ascii=False)
            return Http404

    return render_to_response('home_beta.html', locals(), context_instance=RequestContext(request))


def request_invite(request, form_class=InvitationForm):
    """
    Allow a user to request an invite at a later date by entering their email address.
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            InviteRequest.objects.get_or_create(email=form.cleaned_data['email'])            
            if not request.is_ajax():  
                return HttpResponseRedirect(REDIRECT_URL)
            response = ({'success':True})
            json = simplejson.dumps(response, ensure_ascii=False)
            return HttpResponse(json, mimetype="application/json") 
        else:
            if not request.is_ajax():  
                return HttpResponseRedirect(REDIRECT_URL)
            response = ({'success':False})
            json = simplejson.dumps(response, ensure_ascii=False)
            return HttpResponse(json, mimetype="application/json")

@login_required
def invite(request, success_url=None, form_class=InvitationForm,
               template_name='invite_registration/invitation_form.html',
               extra_context=None):
    """
    Create an invitation and send invitation email.
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            #create a new invitation object
            #if already exists, then it just resend an email to the appropriate email
            invitation = Invitation.objects.get_or_create(
                                     request.user, form.cleaned_data["email"])            
            invitation.send_email(request=request)
            return HttpResponseRedirect(success_url or reverse('invitation_invite'))
    else:
        form = form_class()
    context = {'form': form}
    if extra_context is not None:
        context.update(extra_context)    
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
