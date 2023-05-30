from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Remember


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    remembers = Remember.objects.all()
    data = {'remembers': remembers}
    return render(request, 'home.html', context=data)


class AddRemember(View):
    def post(self, request, pk):
        user = User.objects.get(id=pk)
        remember = Remember()
        remember.user = user
        remember.name = request.POST["name"]
        remember.comment = request.POST["comment"]
        remember.lng = request.POST["lng"]
        remember.lat = request.POST["lat"]
        remember.save()
        print(request.POST)

        return redirect('/')

