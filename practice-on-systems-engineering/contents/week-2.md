# 第2週目

## 学習内容

[Pythonプログラミング入門](https://utokyo-ipp.github.io/index.html#)にアクセスし、以下の内容を学習してください。

- リスト (list)
- 条件分岐
- 繰り返し
- 関数

## 二分法(数値解析)

以下のリンク先の内容を読んで、pythonで実装してみてください。
[二分法](https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%B3%95)

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
    tuple
        A tuple of the form (a, b)
        where f(a) and f(b) have opposite signs
    """

    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    if f(a) == 0:
        return a, a
    if f(b) == 0:
        return b, b

    # Your code here

    return a, b


def f(x):
    return x**2 - 4


a, b = bisection(f, 0, 3)
print(f"a={a}, b={b}")
```

## ニュートン法(数値解析)


## 課題

Colabで新しいノートブックを作成し、以下の課題をそれぞれ一つのセルに記述してください。ファイル名は`week-2.ipynb`としてください。実験の成果物を Moodle 経由で提出しもらいます。

### 課題1

