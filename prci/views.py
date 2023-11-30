from django.shortcuts import render
from django.http import HttpResponse
from .forms import PublisherForm
from .models import Publisher

# Create your views here.


def index(request):
    return render(request, "prci/index.html")


def publisher_data(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['pub_name']
            address = form.cleaned_data['pub_address']
            is_publisher = form.cleaned_data['is_publisher']
            pub_founding_date = form.cleaned_data['publisher_founding_date']
            # publisher_founding_date = form.cleaned_data['publisher_founding_date']


            pub = Publisher.objects.create(
                pub_name=name, 
                pub_address=address,
                is_publisher = is_publisher,
                publisher_founding_date = pub_founding_date
                # pub_founding_date = publisher_founding_date, 
            )

            pub.save()
            return HttpResponse("The data is saved in database")

    form = PublisherForm()

    return render(request, 'prci/publisher.html', {'form': form})
