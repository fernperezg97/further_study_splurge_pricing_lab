"""Classes for melon orders."""

from random import randint
import datetime

class AbstractMelonOrder:
    """Abstract base class that other melons inherit from"""
    order_type = None

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        
    def get_base_price(self):
        weekday = datetime.datetime.isoweekday()

        current_time = str(datetime.datetime.now().time())
        hour = current_time[0:2]
        print(hour)

        #  Judging whether the current time is within the range
        if n_time > d_time and n_time < d_time1 and 0 < weekday < 5:
            return randint(5,9) + 4
        else:
            return randint(5,9)

        
        
        # current_time = datetime.datetime.hour()

        # if week < 5 and 8 < current_time < 11:
        #     return randint(5,9) + 4
        # else:
        #     return randint(5,9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = get_base_price()

        if self.species == "Christmas Melon":
            base_price = base_price* 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if order_type == "international" and self.qty < 10:
            total = total + 3

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        super().__init__(species, qty)
        """Initialize melon order attributes."""




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""

        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernementMelonOrder(AbstractMelonOrder):
    """Ubermelon deal with Government"""
    tax = 0

    def __init__(self, species, qty, shipped):
        super().__init__(species, qty, shipped)
        self.passed_inspection = False
        
    
    def mark_inspection(self, passed):
        """Record the fact than an order has been shipped."""
        
        self.passed_inspection = passed