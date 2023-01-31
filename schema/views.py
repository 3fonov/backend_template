from django.shortcuts import render
from django.http.response import HttpResponsePermanentRedirect
from django.conf import settings


def csrf(request) -> HttpResponsePermanentRedirect:
    return render(request, "csrf.html", {"url": settings.FRONT_URL})
