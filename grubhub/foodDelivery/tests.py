from django.test import TestCase
from .models import *

class AssociationTestCase(TestCase):
  def setUp(self):
    self.driver = Driver.objects.create()
    self.customer = User.objects.create()
    self.salad = MenuItem.objects.create()
    self.burrito = MenuItem.objects.create()
    self.burrito_order_item = OrderItem.objects.create(menu_item=self.burrito)
    self.salad_order_item = OrderItem.objects.create(menu_item=self.salad)
    self.order = Order.objects.create(driver=self.driver, customer=self.customer, order_items=[self.burrito_order_item, self.salad_order_item])

  def test_01_drivers_orders(self):
    """returns the driver's orders""" 
    self.assertEqual(list(self.driver.orders.all()), [self.order])

  def test_02_drivers_customers(self):
    """returns the driver's customers""" 
    self.assertEqual(list(self.driver.customers.all()), [self.customer])

  def test_03_order_item_menu_item(self):
    """returns the menu item""" 
    self.assertEqual(self.burrito_order_item.menu_item,  self.burrito)

  def test_04_order_item_order(self):
    """returns the order""" 
    self.assertEqual(self.burrito_order_item.order, self.order)
  
  def test_05_menu_item_order_items(self):
    """returns the order items for the menu item""" 
    self.assertEqual(list(self.burrito.order_items.all()),  [self.burrito_order_item])
  
  def test_06_users_orders(self):
    """returns the user's orders""" 
    self.assertEqual(list(self.customer.orders), [self.order])

