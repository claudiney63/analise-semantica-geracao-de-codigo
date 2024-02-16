
from goto import with_goto
@with_goto
def main():
	X = 1.0
	_t1 = Y < 0
	if _t1 : goto .l1
	label .l1
	print(a)
	label .l4
	_t2 = Y >= 0
	if _t2 : goto .l5
	goto .l6
	label .l5
	_t3 = a > b
	_t4 = b > c
	_t5 = not _t4
	_t6 = _t3 and _t5
	if _t6 : goto .l2
	_t9 = X * X
	_t10 = _t9 * 2
	X = _t10
	goto .l3
	label .l2
	_t7 = 8 % 2
	c = _t7
	_t8 = c % 2
	a = _t8
	label .l3
	goto .l4
	label .l6
	_t11 = Y != 0
	if _t11 : goto .l7
	label .l7
	print(Y)
main()