from django.shortcuts import render
import pyshorteners

def encode(request):
    data = {}
    if request.method == "POST":
        url = request.POST["url"]
        try:
            s = pyshorteners.Shortener()
            s.tinyurl.short(url)
    return render(request, 'pages/encode.html', {})