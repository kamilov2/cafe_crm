from django.db import models
from django.utils.translation import gettext_lazy as _

# Model for menu items and dishes
class MenuItem(models.Model):
    name = models.CharField(_("Dish Name"), max_length=100)
    description = models.TextField(_("Description"), blank=True, null=True)
    price_per_kg = models.DecimalField(_("Price per 1 kg"), max_digits=10, decimal_places=2)
    price_per_half_kg = models.DecimalField(_("Price per 0.5 kg"), max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Model for reservations
class Reservation(models.Model):
    RESERVATION_CHOICES = [
        ('room', 'Room'),
        ('table', 'Table'),
        ('yurt', 'Yurt'),
        ('arena', 'Arena'),
        ('sauna', 'Sauna')
    ]

    reservation_type = models.CharField(_("Reservation Type"), max_length=10, choices=RESERVATION_CHOICES)
    date = models.DateTimeField(_("Date and Time"))
    duration = models.PositiveIntegerField(_("Duration (in hours)"))
    guests = models.PositiveIntegerField(_("Number of Guests"))

    def calculate_price(self):
        # Example calculation for the sauna
        if self.reservation_type == 'sauna':
            base_price = 250000  # price for up to 6 people
            extra_price_per_guest = 25000
            extra_guests = max(self.guests - 6, 0)
            return base_price + extra_price_per_guest * extra_guests
        return 0

    def __str__(self):
        return f"{self.get_reservation_type_display()} on {self.date}"

# Model for tracking income and expenses
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense')
    ]
    transaction_type = models.CharField(_("Transaction Type"), max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(_("Amount"), max_digits=10, decimal_places=2)
    description = models.TextField(_("Description"), blank=True, null=True)
    date = models.DateField(_("Date"))

    def __str__(self):
        return f"{self.get_transaction_type_display()} of {self.amount} on {self.date}"

# Model for employees
class Employee(models.Model):
    name = models.CharField(_("Employee Name"), max_length=100)
    salary = models.DecimalField(_("Salary"), max_digits=10, decimal_places=2)
    debt = models.DecimalField(_("Debt"), max_digits=10, decimal_places=2, default=0)
    credit = models.DecimalField(_("Credit"), max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

# Model for managing ingredients
class Ingredient(models.Model):
    name = models.CharField(_("Ingredient Name"), max_length=100)
    quantity = models.DecimalField(_("Quantity"), max_digits=10, decimal_places=2)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    supplier = models.CharField(_("Supplier"), max_length=100)

    def __str__(self):
        return self.name
