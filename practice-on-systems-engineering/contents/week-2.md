# 第2週目

## 学習内容

[Pythonプログラミング入門](https://utokyo-ipp.github.io/index.html#)にアクセスし、以下の内容を学習してください。

- リスト (list)
- 条件分岐
- 繰り返し
- 関数

## 二分法(数値解析)

二分法は数値解析において根を求めるためのアルゴリズムの一つです。

$f$が連続関数である区間$[a, b]$が与えられたとき、$f(a)$と$f(b)$が異符号であれば、$f$は$[a, b]$上で少なくとも1つの根を持ちます。この性質は**中間値の定理**により保証されます。二分法は区間$[a, b]$を狭めていくことで、根を求めるアルゴリズムです。

二分法では、$I^{(0)} = [a^{(0)}, b^{(0)}]$を与えられた区間とし、$f(a^{(0)})f(b^{(0)})<0$であるとします。$I^{(0)}$の中点を$x^{(0)} = (a^{(0)}+b^{(0)})/2$とします。$f(x^{(0)})$の値が以下の三つの場合に分けられます。

1. $f(x^{(0)}) = 0$
2. $f(x^{(0)})<0$
3. $f(x^{(0)})>0$

$f(x^{(0)})=0$の場合、$x^{(0)}$は根であるため、計算を打ち切ります。$f(x^{(0)})<0$、または$f(x^{(0)})>0$の場合、必ず$f(a^{(0)})f(x^{(0)})<0$、または$f(b^{(0)})f(x^{(0)})<0$のどちらかが成り立ちます。この性質を利用して、次の区間を選択します。

- もし$f(a^{(0)})f(x^{(0)})<0$であれば、$a^{(1)}=a^{(0)}, b^{(1)}=x^{(0)}$とします。
- もし$f(b^{(0)})f(x^{(0)})<0$であれば、$a^{(1)}=x^{(0)}, b^{(1)}=b^{(0)}$とします。

$I^{(1)} = [a^{(1)}, b^{(1)}]$を新しい区間として、$f(a^{(1)})f(b^{(1)})<0$であることが保証されます。このように反復計算を行うことで、$I^{(1)}, I^{(2)}, \ldots$と区間を狭めていき、根の近似値を求めることができます。

### アルゴリズム

```{prf:algorithm} Bisection method
:label: bisection-algorithm

**Inputs:** function $f$, interval $[a, b]$, tolerance $\text{tol}$
**Output:** interval $[a, b]$, estimate of the root $x$

1. Ensure $f(a)f(b) < 0$
2. While $b - a > \text{tol}$:
    1. $x \leftarrow (a + b) / 2$
    2. If $f(x) = 0$, return $m$
    3. Else if $f(a)f(x) < 0$, $b \leftarrow x$
    4. Else, $a \leftarrow x$
3. Return $a, b, x$

```

## ニュートン法

ニュートン法は数値解析において、求根アルゴリズムの１つです。

ニュートン法では、以下の漸化式を用いて解を求めます。

$$
x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}
$$

$x^{(0)}$を与えられた初期値として、上記の漸化式を繰り返し適用することで、$x^{(1)}, x^{(2)}, \ldots$を求めます。

ニュートン法の停止条件として、よく使われるのは以下の２つです。

1. $|f(x^{(k)})| < \epsilon$
2. $|x^{(k+1)} - x^{(k)}| < \epsilon$

ここで、$\epsilon$はあらかじめ与えられた許容誤差です。

## アルゴリズム

```{prf:algorithm} Newton's method
:label: newton-algorithm

**Inputs:** function $f$, derivative of the function $f'$, initial guess $x^{(0)}$, tolerance $epsilon$　　　
**Output:** estimate of the root $x$

1. $x \leftarrow x^{(0)}$
2. While $|f(x)| > \epsilon$:
    1. $x \leftarrow x - f(x) / f'(x)$
3. Return $x$
```

## 課題

Colabで新しいノートブックを作成し、以下の課題完成してください。ファイル名は`week-2.ipynb`としてください。実験の成果物を Moodle 経由で提出しもらいます。

### 課題1：二分法の実装（４０点）
```python
def bisection(f, a, b, tol=1e-6):
    """
    Bisection method: root finding algorithm

    Parameters
    ----------
    f : function
        The function to find the root of
    a : float
        Lower bound of the interval
    b : float
        Upper bound of the interval
    tol : float
        Tolerance

    Returns
    -------
    a : float
        Lower bound of the interval
    b : float
        Upper bound of the interval
    x : float
        The estimated root

    """

    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    if f(a) == 0:
        return a, a, a
    if f(b) == 0:
        return b, b, b

    while b - a > tol:
        # Your code here
    return a, b, (a + b) / 2


def f(x):
    return x**2 - 4


a, b, x = bisection(f, 0, 3)
print(f"Root={x}, Lower bound={a}, Upper bound={b}")
```

### 課題2：ニュートン法の実装（４０点）
```python
def newton(f, df, x0, tol=1e-6):
    """
    Newton's method: root finding algorithm

    Parameters
    ----------
    f : function
        The function to find the root of
    df : function
        The derivative of the function
    x0 : float
        Initial guess
    tol : float
        Tolerance

    Returns
    -------
    x : float
        The estimated root

    """

    x = x0
    while abs(f(x)) > tol:
        # Your code here
    return x


def df(x):
    return 2 * x


def f(x):
    return x**2 - 4


x = newton(f, df, 3)

print(f"Root={x}")

```

### 課題3：実験分析（１０点）
二分法とニュートン法を用いて、各自で設定した関数に対して、根を求める実験を行い、実験結果を用いて、以下の内容について考察してください。

- 初期値の設定の違い
- 反復回数

### 課題4：最適化問題（１０点）
二分法とニュートン法は、求根アルゴリズムですが、$f'(x)=0$に適用することで、最適化問題にも応用することができます。

次の関数に対して、最小値を求める問題を考え、二分法やニュートン法を用いて、最小値を求めてください。

$$
f(x) = x^2 - 4x + 4
$$