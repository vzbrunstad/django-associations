from django.test import TestCase
from .models import User, Post, Comment


class AssociationTestCase(TestCase):

  def setUp(self):
    self.user          = User()
    self.post          = Post()
    self.commenter_one = User()
    self.commenter_two = User()
    self.comment_one   = Comment(post=self.post, user=self.commenter_one)
    self.comment_two   = Comment(post=self.post, user=self.commenter_two)

  def test_author_of_post(self):
    """returns the author of the post"""
    self.assertEqual(self.post.author, self.author)

  def test_posts_comments(self):
    """returns the post's comments"""
    self.assertEqual(list(self.post.comments.all()), [self.comment_one, self.comment_two])

  def test_comments_author(self):
    """returns the comment's author(user)"""
    self.assertEqual(self.comment_one.author, self.commenter_one)

  def test_comments_post(self):
    """returns the comment's post"""
    self.assertEqual(self.comment_two.post, self.post)

  def test_users_posts(self):
    """returns the posts written by this user"""
    self.assertEqual(list(self.user.posts.all()), [self.post])

  def test_users_comments(self):
    """returns the comments created by the user"""
    self.assertEqual(list(self.commenter_two.comments.all()), [self.comment_two])
