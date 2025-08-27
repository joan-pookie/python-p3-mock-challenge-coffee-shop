import pytest
from many_to_many import Coffee, Customer, Order

class TestOrders:
    def test_has_price(self):
        '''Order is initialized with a price'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')

        order_2 = Order(customer, coffee, 5.0)

        assert (order_2.price == 5.0)

    def test_price_type_and_range(self):
        """price is of type float and between 1.0 and 10.0"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)

        assert isinstance(order_1.price, float)
        assert 1.0 <= order_1.price <= 10.0

    def test_price_is_immutable(self):
        """price is immutable"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)

        # comment out the next two lines if using Exceptions
        # order_1.price = 3.0

    def test_has_customer(self):
        """order has a customer"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order = Order(customer, coffee, 2.0)
        assert order.customer == customer

    def test_customer_is_customer_instance(self):
        """customer is of type Customer"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order = Order(customer, coffee, 2.0)
        assert isinstance(order.customer, Customer)

    def test_has_coffee(self):
        """order has a coffee"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order = Order(customer, coffee, 2.0)
        assert order.coffee == coffee

    def test_coffee_is_coffee_instance(self):
        """coffee is of type Coffee"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order = Order(customer, coffee, 2.0)
        assert isinstance(order.coffee, Coffee)

    def test_order_class_has_all(self):
        """Order class all attribute"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order = Order(customer, coffee, 2.0)
        assert order in Order.all
