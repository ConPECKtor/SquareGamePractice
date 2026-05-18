
import pytest
import fact

def test_fact_with_zero():
  assert fact.factorial(0) == 1

def test_fact_with_one():
  assert fact.factorial(1) == 1

def test_fact_with_ten():
  assert fact.factorial(10) == 3628800

import math

def test_fact_with_onehundred():
  assert fact.factorial(100) == math.factorial(100)

  
