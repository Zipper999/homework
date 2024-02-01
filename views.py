from django.shortcuts import render

news = [
    {
        'title': 'Первая запись',
        'text': 'Много-много текста',
        'date': '10 Мая 2020',
        'author': 'Валерий'
    },
    {
        'title': 'Вторая запись',
        'text': 'Снова много-много текста',
        'date': '19 Мая 2020',
        'author': 'Егор'
    }
]


def home(request):
    data = {
        'news': news,
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html')