from django.db import models

class Actor(models.Model):
    pass

class Movie(models.Model):
    actors = models.ManyToManyField(Actor,through='Role',related_name='movies')
    
class Role(models.Model):
    actor= models.ForeignKey(Actor, on_delete=models.CASCADE,related_name='roles')
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='roles')