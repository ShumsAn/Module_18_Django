from django.shortcuts import render

# Create your views here.
def main_page(request):
    page_name = "Главная страница"
    context = {'page_name': page_name}
    return render(request, 'fourth_task/platform.html',context)


def game_page(request):
    page_name = "Игры"
    context = {
        'games': ["Atomic Heart", "Cyberpunk 2077","Payday"],
        'page_name': page_name
    }
    return render(request, 'fourth_task/games.html',context)

def cart_page(request):
    page_name = "Корзина"
    content = "Ваша корзина пуста"
    context = {'page_name': page_name,
               'content': content}
    return render(request, 'fourth_task/cart.html', context)
