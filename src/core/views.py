from django.shortcuts import render
# from django.views.generic.list import ListView
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def index_fun(request):
   qs = Post.objects.all().order_by('id')
   paginator = Paginator(qs, 3, orphans=1)
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context = {
      'posts':qs,
      'page_obj': page_obj,
   }
   return render(request, 'core/index.html', context)

