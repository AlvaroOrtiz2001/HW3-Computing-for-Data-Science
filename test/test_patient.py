import pytest
from hw4 import Patient 


def test_add_test():
    patient = Patient("Pere", ["fever"])
    patient.add_test("covid", True)
    assert "covid" in patient.tests
    assert patient.tests["covid"] == True

def test_has_covid_test():
    patient = Patient("Marc", ["fever", "cough"])
    patient.add_test("covid", True)
    probability = patient.has_covid()
    assert probability == 0.99

def test_has_covid_notest():
    patient = Patient("Maria", ["fever", "cough"])
    probability = patient.has_covid()
    assert probability == 0.25
