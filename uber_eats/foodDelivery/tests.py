from django.test import TestCase
from .models import Driver, MenuItem, OrderItem, Order, User

class AssociationTestCase(TestCase):

  def setUp(self):
    self.driver = Driver()
    self.customer = User()
    self.salad = MenuItem()
    self.burrito = MenuItem()
    self.burrito_order_item = OrderItem(menu_item=self.burrito)
    self.salad_order_item = OrderItem(menu_item=self.salad)
    self.order = Order(driver=self.driver, customer=self.customer, order_items=[self.burrito_order_item, self.salad_order_item])

  def test_drivers_orders(self):
    """returns the driver's orders""" 
    self.assertEqual(list(self.driver.orders.all()), [self.order])

  def test_drivers_customers(self):
    """returns the driver's customers""" 
    self.assertEqual(list(self.driver.customers.all()), [self.customer])

  def test_order_item_menu_item(self):
    """returns the menu item""" 
    self.assertEqual(self.burrito_order_item.menu_item,  self.burrito)

  def test_order_item_order(self):
    """returns the order""" 
    self.assertEqual(self.burrito_order_item.order, self.order)
  
  def test_menu_item_order_items(self):
    """returns the order items for the menu item""" 
    self.assertEqual(list(self.burrito.order_items.all()),  [self.burrito_order_item])
  
  def test_users_orders(self):
    """returns the user's orders""" 
    self.assertEqual(list(self.customer.orders), [self.order])

