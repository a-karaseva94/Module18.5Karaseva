from django.shortcuts import render


def platform(request):
    return render(request, 'platform.html')


def games_store(request):
    main_page = 'Настольные игры'
    name_game = ['Warhammer Quest: Cursed City', 'Древний Ужас: Разрушенные города', 'Эверделл']
    context = {
        'main_page': main_page,
        'name_game': name_game,
    }
    return render(request, 'games.html', context)


def cart_of_store(request):
    return render(request, 'cart.html')
