
from goto import with_goto
@with_goto
def main():
	x = [float(x) if "." in x else int(x) for x in input("input: ").split()]
	y = [float(x) if "." in x else int(x) for x in input("input: ").split()]
	a = [float(x) if "." in x else int(x) for x in input("input: ").split()]
	_t1 = a < 4
	if _t1 : goto .l4
	goto .l5
	label .l4
	label .l1
	_t2 = x < 15
	_t3 = y < 50
	_t4 = _t2 and _t3
	if _t4 : goto .l2
	goto .l3
	label .l2
	print(a)
	_t5 = y * 2
	y = _t5
	_t6 = 20 / x
	x = _t6
	goto .l1
	label .l3
	label .l5
main()