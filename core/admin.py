from django.contrib import admin

from core.models import Movie
from core.models import Role
from core.models import Person

# Register your models here.


admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
