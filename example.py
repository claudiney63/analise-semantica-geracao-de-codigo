
from goto import with_goto
@with_goto
def main():
	x = 20
	y = 21
	label .l4
	_t1 = x > y
	if _t1 : goto .l5
	goto .l6
	label .l5
	_t2 = x + 1
	x = _t2
	_t3 = z > r
	if _t3 : goto .l1
	_t4 = z < d
	_t5 = d < f
	_t6 = y > d
	_t7 = _t5 and _t6
	_t8 = _t4 or _t7
	_t9 = not _t8
	if _t9 : goto .l2
	label .l2
	r = 20
	print(r)
	goto .l3
	label .l1
	print(x)
	label .l3
	goto .l4
	label .l6
main()