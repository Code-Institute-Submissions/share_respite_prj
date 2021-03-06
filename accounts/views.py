# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate

from testimonials.models import *
from forum.models import *

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You successfully created an account!')
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='/login/')
def profile(request):
    testimonialposts = TestimonialPost.objects.all()
    threadposts = Thread.objects.all()
    forum_subjects = Subject.objects.all()

    return render(request, 'registration/profile.html', {'testimonialposts': testimonialposts,
                                                         'threadposts': threadposts,
                                                         'forum_subjects': forum_subjects})
