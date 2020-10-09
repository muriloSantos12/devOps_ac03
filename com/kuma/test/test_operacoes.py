def func(x):
	return (1001 * x) + x

def test_answer_positive():
	assert func(2) == 2002

def test_answer_negative():
	assert func(-2) == -2002

def test_answer_zero():
	assert func(0) == 0

