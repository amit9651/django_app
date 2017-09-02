from django.db.models import Q
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


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
            Q(category_iexact = slug) |
            Q(category_icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
            return queryset
