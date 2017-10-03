#from playground.basic_math import Number
from playground.compute_basic_math import compute

class TestComputeBasicMath(object):

	def test_compute_is_accurate(self):
		expected=15
		computed_val=compute(10)
		assert expected == computed_val
