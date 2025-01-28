from django.shortcuts import render
from django.views.generic import TemplateView

from app.models import Banner, MainInfo, AboutImages, Prospecs, Apartments


def index_view(request):
    return render(request, 'app/index.html', context={"banners":Banner.objects.all(), "main_info":MainInfo.objects.first(), "about_images":AboutImages.objects.all(), "prospecs": Prospecs.objects.all(), "apartments": Apartments.objects.all()})
