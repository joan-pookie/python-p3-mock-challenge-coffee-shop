# classes/many_to_many.py

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 2:
            raise ValueError("Coffee name must be a string longer than 2 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        """Coffee name is immutable"""
        return self._name

    def orders(self):
        """Return all orders for this coffee"""
        return [order for order in self._orders if order.coffee == self]

    def customers(self):
        """Return unique customers who ordered this coffee"""
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        """Number of times this coffee has been ordered"""
        return len(self.orders())

    def average_price(self):
        """Average price of orders for this coffee"""
        if not self.orders():
            return 0
        total = sum(order.price for order in self.orders())
        return total / len(self.orders())


class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name  # use setter for validation
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    def orders(self):
        """Return all orders for this customer"""
        return [order for order in self._orders if order.customer == self]

    def coffees(self):
        """Return unique coffees this customer has ordered"""
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        """Customer creates a new order"""
        return Order(self, coffee, price)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        # register order
        customer._orders.append(self)
        coffee._orders.append(self)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        """Order price is immutable"""
        return self._price
