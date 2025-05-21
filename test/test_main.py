import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(current_path)
sys.path.insert(0, project_path)
from src.main import sum_func, mult_func


def test_sum_func():
    assert sum_func(2, 3) == 5


def test_mult_func():
    assert mult_func(2, 3) == 6
