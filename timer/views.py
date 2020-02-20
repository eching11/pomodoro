from django.shortcuts import render

# Create your views here.
from timer.models import Category, Pomodoro

def index(request):
    """ View function for home page of site."""
    
    # Generate counts of some of the main objects
    num_categorys = Category.objects.all().count()
    num_pomodoros = Pomodoro.objects.all().count()
    
    # Pomodoro's for today (Tuesday)
    num_pomodoros_today = Pomodoro.objects.filter(day_of_week='Tuesday').count()
    
    context = {
        'num_categorys': num_categorys,
        'num_pomodoros': num_pomodoros,
        'num_pomodoros_today': num_pomodoros_today,
    }
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# Django Tutorial part 6
from django.views import generic

class CategoryListView(generic.ListView):
    model = Category
    #context_object_name = 'category_list' # template variable
    #queryset = Category.objects.filter(name__icontains='Coding')[:5] # Get 5 categories containing name coding
    #template_name = 'category/category_list.html' # specifying template name/location

from django.shortcuts import get_object_or_404
class CategoryDetailView(generic.DetailView):
    model = Category

def category_detail_view(request, primary_key):
    category = get_object_or_404(Category, pk=primary_key)
    return #render(request, 'timer/category_detail.html', context={'category': category})

class PomodoroListView(generic.ListView):
    model = Pomodoro
    context_object_name = 'pomodoro_list'
    template_name = 'pomodoro/pomodoro_list.html'
    
class PomodoroDetailView(generic.DetailView):
    model = Pomodoro
    
def pomodoro_detail_view(request, primary_key):
    pomodoro = get_object_or_404(Pomodoro, pk=primary_key)
    return render(request, 'timer/pomodoro_detail.html', context={'pomodoro': pomodoro})
