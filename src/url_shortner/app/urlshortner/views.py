from django.http import HttpResponse
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random, string
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request) -> HttpResponse:
    return HttpResponse("Welcome to home page")

@api_view(['POST'])
def createShortURL(request) -> HttpResponse:
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
                    
            d = datetime.now()
            s = ShortURL(original_url=original_website, short_url=random_chars, time_date_created=d)
            s.save()
            return HttpResponse(f'url created : {random_chars}')

@api_view(['GET'])
def redirect(request, url) -> HttpResponse:
    current_obj = ShortURL.objects.filter(short_url=url)
    if len(current_obj) == 0:
        return HttpResponse("page not found")
    return HttpResponse(f"redirect to {current_obj[0]}")
