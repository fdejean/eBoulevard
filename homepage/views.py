from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')


def switch_language(request, lang):
    request.session['lang'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))
