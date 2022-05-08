from django.shortcuts import render, redirect, reverse
from django.forms import ValidationError
from .models import *
import pyshorteners

def encode(request):
    data = {}
    if request.method == "POST":
        try:
            l = Link()
            s = pyshorteners.Shortener()
            l.original_url = request.POST["url"]
            l.short_url = s.tinyurl.short(l.original_url)
            l.full_clean()
            l.save()
            return redirect(reverse("new_url", args=(l.id,)))

        except ValidationError as v:
            data["error"] = v.message_dict
    return render(request, 'pages/encode.html', data)

def new_url(request, link_id):
    data = {
        "link_details": Link.objects.get(id=link_id)
    }
    return render(request, 'pages/new_url.html', data)

def decode(request, link_id):
    data = {
        "link_details": Link.objects.get(id=link_id)
    }
    return render(request)