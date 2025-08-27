# lib/many_to_many.py

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Coffee name must be a non-empty string")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set([order.customer for order in self._orders]))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if len(self._orders) == 0:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise Exception("Customer name must be a string between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

class Order:
    # class variable to store all orders
    all = []

    def __init__(self, customer, coffee, price):
        from numbers import Number
        if not isinstance(customer, Customer):
            raise Exception("Order must have a valid Customer")
        if not isinstance(coffee, Coffee):
            raise Exception("Order must have a valid Coffee")
        if not isinstance(price, Number) or not (1.0 <= price <= 10.0):
            raise Exception("Price must be a number between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        # register the order with coffee and customer
        coffee.orders().append(self)
        customer.orders().append(self)

        # add to global list
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

