# Testes
##### Lista de testes
[Teste 1](#teste-1)  
[Teste 2](#teste-2)  
[Teste 3](#teste-3)  
[Teste 4](#teste-4)  
[Teste 5](#teste-5)  
[Teste 6](#teste-6)  
[Teste 7](#teste-7)  
[Teste 8](#teste-8)  
[Teste 9](#teste-9)  
[Teste 10](#teste-10)  
[Teste 11](#teste-11)  
[Teste 12](#teste-12) 

# Testes básicos
## Teste 1 - Teste de unicidade
Código fonte (SimpAlg)
~~~
var {
    int x, x;
}
program {}
~~~

~~~
var {
    int x;
    float x;
}
program {}
~~~

~~~
var {
    int x;
    float y, y;
}
program {}
~~~

~~~
var {
    int x;
    float y;
    float y;
}
program {}
~~~

## Teste 2 - Variáveis não declaradas
Código fonte (SimpAlg)
~~~
var {
    int x;
}
program {
    a = 2;
}
~~~

~~~
var {
    int x;
}
program {
    x = a;
}
~~~

~~~
var {
    int x;
}
program {
    x = a + b;
}
~~~

~~~
var {
    int x;
}
program {
    x = a % b;
}
~~~

~~~
var {
    int x;
}
program {
    x = a * b;
}
~~~

~~~
var {
    int x;
}
program {
    print(a);
}
~~~

~~~
var {
    int x;
}
program {
    scan(a);
}
~~~

~~~
var {
    int x;
}
program {
    if(x > a){}
}
~~~

~~~
var {
    int x;
}
program {
    if(x > a){}
}
~~~

~~~
var {
    int x;
}
program {
    if(x > x and x > a){}
}
~~~

~~~
var {
    int x;
}
program {
    if(x > x or x > a){}
}
~~~


# Teste 3 - Checagem de tipos
Código fonte (SimpAlg)
~~~
var {
    int x;
}
program {
    x = 2.0;
}
~~~

~~~
var {
    int x;
}
program {
    x = (2.0 + 2);
}
~~~

~~~
var {
    int x;
}
program {
    x = (2.0 * 2);
}
~~~

~~~
var {
    int x;
    float y;
}
program {
    x = y;
}
~~~

~~~
var {
    int x;
    float y;
}
program {
    x = (2 + y);
}
~~~


# Teste 4 - Módulo
Código fonte (SimpAlg)
~~~
var {
    int x;
    float y;
}
program {
    x = 2.0 % 2;
}
~~~

~~~
var {
    int x;
    float y;
}
program {
    x = 2 % 2.0;
}
~~~

~~~
var {
    int x;
    float y;
}
program {
    x = 2.0 % 2.0;
}
~~~

~~~
var {
    int x;
    float y;
}
program {
    y = 2.0 % 2.0;
}
~~~

~~~
var {
    int x;
    float y;
}
program {
    x = 2.0 + 2 % 2;
}
~~~


# Teste 1
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
    float x2, y2;
}
program {
    scan(x,y,a, x2, y2);
    if(a<x){
        while(x<10 and y > 2){
            print(a);
            y=y+1;
            x = 10 % y;
        }
    }
}
~~~

Código intermediário (Python)
~~~

from goto import with_goto
@with_goto
def main():
	x, y, a, x2, y2 = [float(x) if "." in x else int(x) for x in input("input: ").split()]
	_t1 = a < x
	if _t1 : goto .l4
	goto .l5
	label .l4
	label .l1
	_t2 = x < 10
	_t3 = y > 2
	_t4 = _t2 and _t3
	if _t4 : goto .l2
	goto .l3
	label .l2
	print(a)
	_t5 = y + 1
	y = _t5
	_t6 = 10 % y
	x = _t6
	goto .l1
	label .l3
	label .l5
main()
~~~

# Teste 2
Código fonte (SimpAlg)
~~~
var {
    int a, b;
    float Z, X, Y;
}
program {
    scan(Z, X, Y);
    Z = 10 % 2.0;
    X = a + b;
    Y = x +1;
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 3
Código fonte (SimpAlg)
~~~
var {
    int a, b;
    float Z, X, Y;
}
program {
    Z = 2 + 2.0;
    if( !(a<b or c> x)){
        print(x);
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 4
Código fonte (SimpAlg)
~~~
var {
    int x, y, a, z, i;
}
program {
    if(a < 3) {
        while(x < 5 and y > 0) {
            print(a);
            y = y + 1;
            x = 15 % z;
            if(x < 10) {
                i = 0;
                while(i <= 10) {
                    print(x);
                }
            }
        }
    }
}
~~~

Código intermediário (Python)
~~~
from goto import with_goto
@with_goto
def main():
        _t1 = a < 3
        if _t1 : goto .l8
        label .l8
        label .l5
        _t2 = x < 5
        _t3 = y > 0
        _t4 = _t2 and _t3
        if _t4 : goto .l6
        goto .l7
        label .l6
        print(a)
        _t5 = y + 1
        y = _t5
        _t6 = 15 % z
        x = _t6
        _t7 = x < 10
        if _t7 : goto .l4
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
        goto .l5
        label .l7
main()
~~~

# Teste 5
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
    float z;
}
program {
    scan(x);
    scan(y);
    scan(a);
    z = x / 2.0;

    if(a < 4) {
        while(x < 15 and y > 1) {
            print(a);
            y = y * 2;
            x = 20 / x;
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 6
Código fonte (SimpAlg)
~~~
var {
    int x, y, a, b;
}
program {
    scan(x);
    scan(y);
    scan(a);
    scan(b);

    if ((a >= 5 and b <= 15) or (x < y and a == b)) {
        while (x > 0 and y < 50) {
            if ((x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0)) {
                print("Valor de b = ", b);
            }
            y = y + 5;
            x = x - 2;
            print("Valor de y = ", y);
            print("Valor de x = ", x);
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 7
Código fonte (SimpAlg)
~~~
var {
    int x, y, a, b;
}

program {
    scan(x);
    scan(y);
    scan(a);
    scan(b);

    if (a > b or (x * y) > (a + b)) {
        while (x < 50 and y < 100) {
            if ((x + y) % 3 == 0 and (x * y) % 7 == 0) {
                print(x + y);
            }
            y = y + 7;
            x = x + 3;
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 8
Código fonte (SimpAlg)
~~~
var {
    float x, y, a;
}

program {
    scan(x);
    scan(y);
    scan(a);

    if (x >= 0.0 and y < 10.0) {
        while (x < 100.0 and y > 0.0) {
            if (x % 2.0 == 0.0) {
                print(a);
            }
            y = y - 2.5;
            x = x + 5.0;
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 9
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
}

program {
    scan(x);
    scan(y);
    scan(a);

    if (-x < 0) {
        while (x > -10 and y < 100) {
            print(a);
            y = y + 10;
            x = -x;
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 10
Código fonte (SimpAlg)
~~~
var {
    int x, y, a, z, i;
}
program {
    if(a < 3) {
        while(x < 5 and y > 0) {
            print(a);
            y = y + 1;
            x = 15 % z;
            if(x < 10) {
                i = 0;
                while(i <= 10) {
                    print(x);
                }
            }
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 11
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
    float x2, y2;
}
program {
    if(a<y){
        y = y + 1;
    }
}
~~~

Código intermediário (Python)
~~~
from goto import with_goto
@with_goto
def main():
        _t1 = a < y
        if _t1 : goto .l1
        label .l1
        _t2 = y + 1
        y = _t2
main()
~~~

# Teste 12
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
    float x2, y2;
}
program {
    while(a<y){
        y = y + 1;
        x = 10 % a;
    }
}
~~~

Código intermediário (Python)
~~~
from goto import with_goto
@with_goto
def main():
        label .l1
        _t1 = a < y
        if _t1 : goto .l2
        goto .l3
        label .l2
        _t2 = y + 1
        y = _t2
        _t3 = 10 % a
        x = _t3
        goto .l1
        label .l3
main()
~~~

# Teste 13
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
    float x2, y2;
}
program {
    while(a<y){
        y = y + 1;
        x = 10 % y2;
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~


# Teste 14
Código fonte (SimpAlg)
~~~
var {
    int x, y, a;
    float x2, y2;
}
program {
    if(a<y){
        while(x<10 and y > 2){
            print(a);
            y = y + 1;
            x = 10 % x;
        }
    }
}
~~~

Código intermediário (Python)
~~~
from goto import with_goto
@with_goto
def main():
        _t1 = a < y
        if _t1 : goto .l4
        label .l4
        label .l1
        _t2 = x < 10
        _t3 = y > 2
        _t4 = _t2 and _t3
        if _t4 : goto .l2
        goto .l3
        label .l2
        print(a)
        _t5 = y + 1
        y = _t5
        _t6 = 10 % x
        x = _t6
        goto .l1
        label .l3
main()
~~~

# Teste 15
Código fonte (SimpAlg)
~~~
var {
    int a, b;
    float Z, X, Y;
}
program {
    if(a<b or c>b and X>Y){
        X = 1;
        Y = 2.0
    }
    print(X, Y);
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 16
Código fonte (SimpAlg)
~~~
var {
    int a, b;
    float Z, X, Y;
}
program {
    if(a<b or X>b and X>Y){
        X = 1;
        Y = 2.0;
    }
    print(X, Y);
}
~~~

Código intermediário (Python)
~~~
from goto import with_goto
@with_goto
def main():
        _t1 = a < b
        _t2 = X > b
        _t3 = X > Y
        _t4 = _t2 and _t3
        _t5 = _t1 or _t4
        label .l1
        X = 1
        Y = 2.0
        print(X, Y)
main()
~~~

# Teste 17
Código fonte (SimpAlg)
~~~
var {
    int a, b, c;
    float Z, X, Y;
}
program {
    scan(X);
    if(!(a<b or X>b)){
        X = 1;
    }
    print(X, Y);
    while(X>Y){
        Y = Y + 1;
        X = a+b + (a-c);
    }
    print(X);
}
~~~

from goto import with_goto
@with_goto
def main():
        X = input("input: ").split()
        _t1 = a < b
        _t2 = X > b
        _t3 = _t1 or _t2
        _t4 = not _t3
        if _t4 : goto .l1
        label .l1
        X = 1
        print(X, Y)
        label .l2
        _t5 = X > Y
        if _t5 : goto .l3
        goto .l4
        label .l3
        _t6 = Y + 1
        Y = _t6
        _t7 = a + b
        _t8 = a - c
        _t9 = _t7 + _t8
        X = _t9
        goto .l2
        label .l4
        print(X)
main()

~~~
// código
~~~
# Teste 18
Código fonte (SimpAlg)
~~~
var {
    int a, b, c;
    float Z, X, Y;
}
program {
    scan(X, Y);
    if(X<=0 or Y <=0){
        print(a);
    }else{
        Z = X / (Y*Y);
    }
}

~~~

Código intermediário (Python)
~~~

from goto import with_goto
@with_goto
def main():
	X, Y = input("input: ").split()
	_t1 = X <= 0
	_t2 = Y <= 0
	_t3 = _t1 or _t2
	if _t3 : goto .l1
	_t4 = Y * Y
	_t5 = X / _t4
	Z = _t5
	goto .l2
	label .l1
	print(a)
	label .l2
main()
~~~
# Teste 19
Código fonte (SimpAlg)
~~~
var {
    int a, b, c;
    float Z, X, Y;
}
program {
    scan(X, Y);
    if(X<=0 or Y <=0){
        print(a);
    }else{
        Z = X / (Y*Y);
        while(a<b){
            if(c==2){
                X = 2 * 1 + a;
                print(X);
            }else{
                X = 2 * (1 + a);
            }
        }
    }
}

~~~

Código intermediário (Python)
~~~

from goto import with_goto
@with_goto
def main():
	X, Y = input("input: ").split()
	_t1 = X <= 0
	_t2 = Y <= 0
	_t3 = _t1 or _t2
	if _t3 : goto .l1
	_t4 = Y * Y
	_t5 = X / _t4
	Z = _t5
	label .l4
	_t6 = a < b
	if _t6 : goto .l5
	goto .l6
	label .l5
	_t7 = c == 2
	if _t7 : goto .l2
	_t10 = 1 + a
	_t11 = 2 * _t10
	X = _t11
	goto .l3
	label .l2
	_t8 = 2 * 1
	_t9 = _t8 + a
	X = _t9
	print(X)
	label .l3
	goto .l4
	label .l6
	goto .l7
	label .l1
	print(a)
	label .l7
main()
~~~
# Teste 20
Código fonte (SimpAlg)
~~~
var {
    int a, b, c;
    float Z, X, Y;
}
program {
    X = 1.0;
    if(Y<0){
        print(a);
    }
    while(Y>=0){
        if(a > b and !(b>c)){
            c = 8 % 2;
            a = c % 2;
        }else{
            X = (X * X) * 2;
        }
    }
    if(Y!=0){
        print(Y);
    }
    
}

~~~

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

# Teste 21
Código fonte (SimpAlg)
~~~
var {
    int a, b;
    float Z, X, Y;
}
program {
    scan(a, b, Z, X, Y);
    Z = 10 % 2;
    X = a + b;
    Y = X +1;
    print(Z, X, Y);
}
~~~
Código intermediário (Python)
~~~

from goto import with_goto
@with_goto
def main():
	a, b, Z, X, Y = [float(x) if "." in x else int(x) for x in input("input: ").split()]
	_t1 = 10 % 2
	Z = _t1
	_t2 = a + b
	X = _t2
	_t3 = X + 1
	Y = _t3
	print(Z, X, Y)
main()
~~~
# Teste 22
Código fonte (SimpAlg)
~~~

~~~
Código intermediário (Python)
~~~
// código
~~~