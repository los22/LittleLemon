from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(ID=10,Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item.Title, "IceCream")
        self.assertEqual(item.Price, 80)
        