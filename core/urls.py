from django.urls import path

from core.views import MovieList
from core.views import MovieDetail
from core.views import PersonDetail

app_name='core'
urlpatterns = [
    path('movies/', MovieList.as_view(), name='MovieList'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='MovieDetail' ),
    path('persons/<int:pk>/', PersonDetail.as_view(), name='PersonDetail' ),
]