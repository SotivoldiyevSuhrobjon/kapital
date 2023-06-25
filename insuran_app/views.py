from django.shortcuts import render
from datetime import date, timedelta
from insuran_app.models import *
from django.http import JsonResponse
from django.shortcuts import render


# from .models import MyForm

# Create your views here.
def home_page(request):
    sugurta = Sugurta.objects.all()
    context = {
        'sugurta': sugurta
    }
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     description = request.POST.get('description')
    #     sup = Support.objects.create(
    #         name=name,
    #         phone=phone,
    #         description=description,
    #     )
    #     sup.save()
    return render(request, 'home.html', context)


def osago_page(request):
    sugurta = Sugurta.objects.all()
    context = {
        'sugurta': sugurta
    }
    return render(request, 'osago.html', context)


def sport_page(request):
    sport = Sport.objects.all()
    sport_type = RelatedSport.objects.all()
    today = date.today()
    one_month_later = today + timedelta(days=30)
    sugurta = Sugurta.objects.all()
    region = Region.objects.all()
    city = City.objects.all()
    context = {
        'sport': sport,
        'sport_type': sport_type,
        'region': region,
        'city': city,
        'sugurta': sugurta,
        'today': today,
        'one_month_later': one_month_later
    }
    return render(request, 'sport.html', context)


def personal_page(request):
    region = Region.objects.all()
    city = City.objects.all()
    today = date.today()
    one_month_later = today + timedelta(days=30)
    sugurta = Sugurta.objects.all()
    context = {
        'region': region,
        'city': city,
        'sugurta': sugurta,
        'today': today,
        'one_month_later': one_month_later
    }
    return render(request, 'personal.html', context)


def accident_page(request):
    region = Region.objects.all()
    city = City.objects.all()
    today = date.today()
    one_month_later = today + timedelta(days=30)
    sugurta = Sugurta.objects.all()
    context = {
        'region': region,
        'city': city,
        'sugurta': sugurta,
        'today': today,
        'one_month_later': one_month_later
    }
    return render(request, 'accident.html', context)


def travel_page(request):
    region = Region.objects.all()
    city = City.objects.all()
    today = date.today()
    one_month_later = today + timedelta(days=30)
    sugurta = Sugurta.objects.all()
    context = {
        'region': region,
        'city': city,
        'sugurta': sugurta,
        'today': today,
        'one_month_later': one_month_later
    }
    return render(request, 'travel.html', context)


def get_cities(request, region_id):
    cities = City.objects.filter(region_id=region_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)


def get_related_sports(request, sport_id):
    related_sports = RelatedSport.objects.filter(sport_id=sport_id).values('id', 'name')
    return JsonResponse({'related_sports': list(related_sports)})
