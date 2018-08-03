from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {})
        pass
    elif request.method == 'GET':
        return render(request, 'login.html', {})
