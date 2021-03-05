from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS

# Table for following system
class Follow(models.Model):
    # This means following(Person A) follows follower(Person B)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return str(self.following.username) + " follows " + str(self.follower.username)

    class Meta:
        unique_together = (('following', 'follower'), )


class Movie(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    production_year = models.IntegerField()
    overview = models.CharField(max_length=300, default="Movie description")
    rating = models.IntegerField()

    def __str__(self):
        return str(self.movie_name) + " has id: " + str(self.movie_id)


class MovieWatched(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')


class WatchList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    rating = models.IntegerField()
