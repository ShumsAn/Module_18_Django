from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sign_up_by_django(request):
    users = ['Vasya','Petya','Sanya']
    info = {}
    context = {'info': info,
               'users':users}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password :
            print(f' username = {type(username)},password = {password} ,age = {age} ')
            return HttpResponse (f"Приветствуем! {username}")


    return render(request, 'fifth_task/registration_page.html',context)
