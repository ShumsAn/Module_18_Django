from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
#Create your views here.



def main_page(request):
    return render(request, 'third_task/platform.html')

def button_a(request):
    return HttpResponse("Нажал на кнопку")


def game_page(request):
    context = {
        "atomic": "Атомик Вар 100500",
        "ciberPunk": "Кибер пунк 3000",
        "payday": "ПЭЙ ДЭЙ 333"
    }
    return render(request, 'third_task/games.html',context)

def cart_page(request):
    return render(request, 'third_task/cart.html')