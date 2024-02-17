
from goto import with_goto
@with_goto
def main():
	_t1 = a < 3
	if _t1 : goto .l9
	goto .l10
	label .l9
	label .l6
	_t2 = x < 5
	_t3 = y > 0
	_t4 = _t2 and _t3
	if _t4 : goto .l7
	goto .l8
	label .l7
	print(a)
	_t5 = y + 1
	y = _t5
	_t6 = 15 % z
	x = _t6
	_t7 = x < 10
	if _t7 : goto .l4
	goto .l5
	label .l4
	i = 0
	label .l1
	_t8 = i <= 10
	if _t8 : goto .l2
	goto .l3
	label .l2
	print(x)
	goto .l1
	label .l3
	label .l5
	goto .l6
	label .l8
	label .l10
main()