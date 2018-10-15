from django.test import TestCase

from django.test import TestCase
from .models import Actor, Role, Movie


class AssociationTestCase(TestCase):

  def setUp(self):
    self.actor = Actor()
    self.movie = Movie()
    self.role  = Role(movie=self.movie, actor=self.actor)

  def test_roles_movie(self):
    """returns the role's movie"""
    self.assertEqual(self.role.movie, self.movie)

  def test_roles_actor(self):
    """returns the role's actor"""
    self.assertEqual(self.role.actor, self.actor)
  
  def test_movies_roles(self):
    """returns the movie's roles"""
    self.assertEqual(list(self.movie.roles), [self.role])

  def test_movies_actors(self):
    """returns the movie's actors"""
    self.assertEqual(list(self.movie.actors), [self.actor])
  
  def test_actors_roles(self):
    """returns the actor's roles"""
    self.assertEqual(list(self.actor.roles), [self.role] )

  
