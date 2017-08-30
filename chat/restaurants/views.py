
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView
from .models import RestaurantLocation

# Create your views here.
def restaurants_listview(request):
    template_name='restaurants/restaurants_list.html'
    queryset=RestaurantLocation.objects.all()
    context={
          "object_list":queryset
    }
    return render(request,template_name,context)


class IndianView(ListView):
      queryset=RestaurantLocation.objects.filter(category__exact='Indain')
      template_name='restaurants/restaurants_list.html'

      
class AmericanView(ListView):
      queryset=RestaurantLocation.objects.filter(category__exact='American')
      template_name='restaurants/restaurants_list.html'
