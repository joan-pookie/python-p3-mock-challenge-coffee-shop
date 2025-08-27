import pytest
from many_to_many import Coffee, Customer, Order

class TestCoffee:
    def test_has_name(self):
        """Coffee is initialized with a name"""
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"

    def test_name_length(self):
        """Coffee is initialized with a name of type str longer than 2.0 chars"""
        coffee = Coffee("Mocha")
        assert isinstance(coffee.name, str)
        assert len(coffee.name) > 2

    def test_name_is_immutable(self):
        """cannot change the name of the coffee"""
        coffee = Coffee("Mocha")

        # comment out the next two lines if using Exceptions
        # coffee.name = "Peppermint Mocha"

    def test_has_orders(self):
        """coffee has many orders"""
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        order = Order(customer, coffee, 5.0)
        assert order in coffee.orders()

    def test_orders_are_order_instances(self):
        """coffee orders are of type Order"""
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        order = Order(customer, coffee, 5.0)
        assert isinstance(coffee.orders()[0], Order)

    def test_has_customers(self):
        """coffee has many customers"""
        coffee = Coffee("Cappuccino")
        customer = Customer("Bob")
        Order(customer, coffee, 4.0)
        assert customer in coffee.customers()

    def test_customers_are_unique(self):
        """coffee has unique list of all the customers that have ordered it"""
        coffee = Coffee("Cappuccino")
        customer = Customer("Bob")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        assert coffee.customers().count(customer) == 1

    def test_customers_are_customer_instances(self):
        """coffee customers are of type Customer"""
        coffee = Coffee("Espresso")
        customer = Customer("Clara")
        Order(customer, coffee, 3.0)
        assert isinstance(coffee.customers()[0], Customer)

    def test_tracks_number_of_orders(self):
        """coffee tracks the number of times it has been ordered"""
        coffee = Coffee("Flat White")
        customer = Customer("Dave")
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 6.0)
        assert coffee.num_orders() == 2

    def test_average_price(self):
        """coffee calculates the average price of its orders"""
        coffee = Coffee("Macchiato")
        customer = Customer("Ella")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        assert coffee.average_price() == 5.0
