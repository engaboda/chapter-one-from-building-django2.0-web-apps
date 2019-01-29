from django.db import models


class MovieManager(models.Manager):

    def all_with_related_persons(self):
        qs = self.get_queryset()
        qs = qs.select_related(
            'director'
        )
        qs = qs.prefetch_related(
            'writers',
            'actors',
        )
        return qs

class Movie(models.Model):
    director = models.ForeignKey(to='Person', related_name='directed', blank=True, null=True, on_delete=models.CASCADE)
    writers = models.ManyToManyField( to='Person', related_name='writing_credits',blank=True )
    actors = models.ManyToManyField(to='Person', through='Role', related_name='acting_credits', blank=True)
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated' ),
        (RATED_G, 'G - General Audiences' ),
        (RATED_PG, 'PG - Perental Guidances "Suggested" ' ),
        (RATED_R, 'R - Restricted' ),
    )
    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    objects = MovieManager()

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)
    
    class Meta:
        ordering = ('-year','title')

class PersonManager(models.Manager):
    def all_with_prefetched_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related(
            'directed',
            'writing_credits',
            'acting_credits',
            'role_set__movie',
        )
        


class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()
    died = models.DateField(blank=True, null=True)

    objects = PersonManager()

    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        if self.died:
            return "{}, {}, ({}-{})".format(
                self.last_name,
                self.first_name,
                self.born,
                self.died
            )
        return '{}, {}, ({})'.format(self.last_name,
        self.first_name,
        self.born)


class Role(models.Model):
    movie = models.ForeignKey(to='Movie', on_delete=models.DO_NOTHING)
    person = models.ForeignKey(to='Person', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    def __str__(self):
        return "{} {} {}".format(self.movie_id, self.person_id, self.name)

    class Meta:
        unique_together = ('movie', 'person', 'name')