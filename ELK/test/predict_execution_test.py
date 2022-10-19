# Unit test for predict_execution func

import numpy as np

from execution_time.prediction_execution import predict_exe


def test_empty_array():
    assert predict_exe([]) == 'empty array'


def test_one_sample():
    assert predict_exe([1]) == 1


def test_input_str():
    assert predict_exe(['gdh']) == 'string cant consider as the execution time'


def test_mixture_gaussian():
    assert predict_exe([1, 200.1, 34, 67.5]) == 75


def test_two_sample():
    assert predict_exe([1, 200]) == 200


def test_big_array():
    assert predict_exe(np.arange(0, 1000, 0.00001)) == 999
