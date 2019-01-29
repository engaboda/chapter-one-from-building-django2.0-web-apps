from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator

from core.models import Movie
from core.models import Person


class MovieList(ListView):
    model = Movie
    paginate_by = 10

class MovieDetail(DetailView):
    queryset = (Movie.objects.all_with_related_persons())

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetched_movies()