from django.test import TestCase
from .models import User, Shop, Product, Review

class AssociationTestCase(TestCase):
  
  def setUp(self):
    self.shop_owner = User.objects.create()
    self.shop       = Shop.objects.create(owner=self.shop_owner)
    self.product    = Product.objects.create(shop=self.shop)
    self.user       = User.objects.create()
    self.review     = Review.objects.create(product=self.product, reviewer=self.user)
    
  def test_owner_of_shop(self):
    """returns the owner of the shop"""
    self.assertEqual(self.shop.owner, self.shop_owner)

  def test_shop_products(self):
    """returns the products for sale in the shop"""
    self.assertEqual(list(self.shop.products.all()), [self.product])

  def test_product_shop(self):
    """returns the shop the product belongs to"""
    self.assertEqual(self.product.shop, self.shop)

  def test_product_reviews(self):
    """returns the product's reviews"""
    self.assertEqual(list(self.product.reviews.all()), [self.review])

  def test_review_reviewer(self):
    """returns the review's author"""
    self.assertEqual(self.review.reviewer, self.user)


