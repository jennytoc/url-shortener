from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.forms import ValidationError
from .models import *
import pyshorteners

def index(request):
    data = {}
    if request.method == "POST":
        try:
            l = Link()
            s = pyshorteners.Shortener()
            l.original_url = request.POST["url"]
            l.short_url = s.tinyurl.short(l.original_url)
            l.full_clean()
            l.save()
            return redirect(reverse("encode", args=(l.id,)))

        except ValidationError as v:
            data["error"] = v.message_dict
    return render(request, 'pages/index.html', data)

def encode(request, link_id):
    l = Link.objects.get(id=link_id)
    data = {
        "short_url" : l.short_url
    }
    return JsonResponse(data)

def decode(request, link_id):
    l = Link.objects.get(id=link_id)
    data = {
        "link_details": l.original_url
    }
    return JsonResponse(data)