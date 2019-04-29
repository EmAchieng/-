#from django.views import ListView
from django.views.generic import ListView
from django.shortcuts import render
from products.models import Product

# Create your views here.

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "product_list.html"

#function based-view

def product_list_view(request):
	context = {
		'object_list' : queryset
	}
	return render(request, "product/list.html", context)

