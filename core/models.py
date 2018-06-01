"""
We put the models into the project root dir to use it for web and REST API apps.

Models:
- Member: The member (not a user). FOr users we are going to use Django auth.
- Plan: The membership depends of the plan. Only 1 plan by member.
- Payment: To track the member payments (in the history)
"""
from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=200)
    fee = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return '%s' % (self.name)

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    joined_on = models.DateField(auto_now=True)
    plan = models.ForeignKey(Plan, models.SET_NULL, blank=True, null=True,)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Payment(models.Model):
    amount = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    member = models.ForeignKey(Member, on_delete=models.CASCADE,)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return '%.2f %s' % (self.amount, self.created_at)


