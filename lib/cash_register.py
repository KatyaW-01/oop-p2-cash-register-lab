#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0,total=0,items=[],previous_transactions=[]):
    self.discount = discount
    self.total = total
    self.items = items
    self.previous_transactions = previous_transactions

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self,value):
    if 0<= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
