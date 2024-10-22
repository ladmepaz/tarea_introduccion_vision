import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_add():
    from student_code import add  # assuming student_code.py is where students write their code
    assert add(1, 2) == 3
