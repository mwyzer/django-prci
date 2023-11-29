from django.shortcuts import render
from django.http import HttpResponse
from .forms import PublisherForm

# Create your views here.


def index(request):
    return render(request, "prci/index.html")


def publisher_data(request):
    form = PublisherForm()
    return render(request, 'prci/publisher.html', {'form': form})
