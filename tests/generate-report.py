import pytest
import sys
import os
# print(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
from backendCode import produce_ivd_result_event

@pytest.mark.smoke
def test_gid_322133_report_generation():
    print(produce_ivd_result_event())
    print('py test execute: Passed')