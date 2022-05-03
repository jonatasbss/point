from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from . import forms
from .forms import AlvoForm
from .models import Alvo


# Create your views here.
@csrf_protect
def new_alvo(request):
    if request.method == "POST":
        form = AlvoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = AlvoForm()
    return render(request, 'index.html', {'form': form})


def list_alvo(request):
    alvo = Alvo.objects.all()
    return render(request, "show.html", {'alvo': alvo})


def edit_alvo(request, id):
    alvo = Alvo.objects.get(id=id)
    return render(request, 'edit.html', {'alvo': alvo})

@csrf_protect
def update_alvo(request, id):
    alvo = Alvo.objects.get(id=id)
    form = AlvoForm(request.POST, instance=alvo)
    if form.is_valid():
        form.save()
        return redirect('/show')

    return render(request, 'edit.html', {'alvo': alvo})


def delete_alvo(request, id):
    alvo = Alvo.objects.get(id=id)
    alvo.delete()
    return redirect('/show')
