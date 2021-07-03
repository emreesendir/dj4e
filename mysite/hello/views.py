from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic


def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits >= 5 : del(request.session['num_visits'])
    resp = HttpResponse('547a5a56<br>view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', '547a5a56', max_age=1000)
    return resp