from django.shortcuts import render

from .models import Member

# Create your views here.



def index(request):
    books = Member.objects.all()
    context = {
        "books": books
    }

    return render(request, 'index.html', context)