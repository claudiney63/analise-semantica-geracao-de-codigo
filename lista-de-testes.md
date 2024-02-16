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
    if(a<b){
        while(x<10 and y > 2){
            Print(a);
            y=y+1;
            x = 10 % z;
        }
    }
}
~~~

Código intermediário (Python)
~~~
// código
~~~

# Teste 2
Código fonte (SimpAlg)
~~~
var {
    int a, b;
    float Z, X, Y;
}
program {
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
// código
~~~

Código intermediário (Python)
~~~
// código
~~~
