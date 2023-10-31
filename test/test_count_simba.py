import pytest
from hw3 import count_simba

def test_count_simba():
    test_strings = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]
    result = count_simba(test_strings)
    assert result == 3