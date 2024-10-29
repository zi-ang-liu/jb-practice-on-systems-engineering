# 第3週目

## 学習内容

[Pythonプログラミング入門](https://utokyo-ipp.github.io/index.html#)にアクセスし、以下の内容を学習してください。

- モジュールの使い方
- NumPyライブラリ

## 最急降下法

$\mathbf{x} \in \mathbb{R}^n$の関数$f(\mathbf{x})$を最小化する問題を考える。ここで、$f$は微分可能であるとする。

最急降下法は、以下の式で与えられる更新式を繰り返すことで、$f$の極小値を求めるアルゴリズムである。

$$
\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - \alpha \nabla f(\mathbf{x}^{(k)})
$$

ここで、$\nabla f(\mathbf{x})$は$f$の勾配を表し、$\alpha$はステップサイズを表す。$\mathbf{x}^{(0)}$は初期値である。

勾配$\nabla f(\mathbf{x})$は、以下のように定義される。

$$
\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n} \right]
$$

$\alpha$は、ステップサイズを表すハイパーパラメータであり、適切な値を選択することでアルゴリズムの収束性能を向上させることができる。

最急降下法は、勾配の逆方向に進むことで、関数$f$の極小値を探索するアルゴリズムである。

最急降下法の停止条件として、よく使われるのは以下の式である。

$\|\nabla f(\mathbf{x})\| < \text{tol}$

$\|\cdot\|$ はベクトルのノルムを表し、$\text{tol}$はあらかじめ与えられた許容誤差である。

最急降下法のアルゴリズムは以下の通りである。

```{prf:algorithm} Gradient descent
:label: gradient-descent-algorithm

**Inputs:** function $f$, gradient $\nabla f$, initial guess $\mathbf{x}^{(0)}$, step size $\alpha$, tolerance $\text{tol}$   
**Output:** estimate of the minimum $\mathbf{x}$

1. Initialize $\mathbf{x} \leftarrow \mathbf{x}^{(0)}$
2. While $\|\nabla f(\mathbf{x})\| > \text{tol}$:
    1. $\mathbf{x} \leftarrow \mathbf{x} - \alpha \nabla f(\mathbf{x})$
3. Return $\mathbf{x}$
```

## Random Search

Random search (RS)は最適化問題を解くためにランダムな探索を行うアルゴリズムです。

RSは、探索空間内のランダムな点を評価することで、最適解を探索します。RSは、勾配情報を必要とせず、関数$f$が微分可能である必要もありません。そのため、非常にシンプルで汎用性のある最適化手法となります。

$\mathbf{x} \in \mathbb{R}^n$を探索空間とし、目的関数$f: \mathbb{R}^n \to \mathbb{R}$を最小化する問題を考えます。$x_i$は$i$番目の次元の値を表します。$\mathcal{X}$を探索空間とします。

RSのアルゴリズムは以下の通りです。

```{prf:algorithm} Random Search
:label: random-search-algorithm

**Inputs:** function $f$, number of iterations $N$, search space $\mathcal{X}$     
**Output:** estimate of the minimum $\mathbf{x}$

1. Initialize $\mathbf{x}$ with a point in the search space $\mathcal{X}$
2. For $i = 1, 2, \ldots, N$:
    1. Generate a random point $\mathbf{x}'$ in the search space $\mathcal{X}$
    2. If $f(\mathbf{x}') < f(\mathbf{x})$, then $\mathbf{x} \leftarrow \mathbf{x}'$
3. Return $\mathbf{x}$
```

RSは、まず探索空間内の一つの実行可能解$\mathbf{x}\in\mathcal{X}$をランダムに選択します。その後、指定された回数だけ探索を繰り返し、新しい解がより良い場合には解を更新します。

## 課題

Colabで新しいノートブックを作成し、以下の課題をそれぞれ一つのセルに記述してください。ファイル名は`week-3.ipynb`としてください。実験の成果物を Moodle 経由で提出しもらいます。

### 課題1 (10点)

#### 課題1-1
`numpy.array()`関数を使って、list型のデータをnumpyの配列に変換してください。

```python
import numpy as np

data = [1, 2, 3, 4, 5]
# your code here
```

#### 課題1-2
課題1-1で作成したNumPyの配列の各要素を2乗してください。

#### 課題1-3
`numpy.sum()`関数を使って、課題1-2で作成したNumPyの配列の要素の合計を計算してください。

#### 課題1-4
`np.random.uniform()`関数は、指定された範囲内の一様分布からランダムな数値を生成します。`np.random.uniform()`関数は、`low`と`high`と`size`の3つの引数を取ります。`low`は一様分布の下限、`high`は上限、`size`は生成する乱数の数を指定します。以下の例では、0から1の範囲でランダムな数値を10個生成しています。

```python
import numpy as np

np.random.uniform(low=0.0, high=1.0, size=10)
```

`np.random.uniform()`関数を使って、-1から1の範囲でランダムな数値を5個生成してください。

### 課題2 (50点)

関数$f(\mathbf{x}) = x_1^2 + x_2^2$を最小化する問題を考えます。最急降下法を用いて、この関数の最小値を求めるPythonプログラムを作成してください。初期値は$\mathbf{x}^{(0)} = [1, 1]$とし、ステップサイズ$\alpha$は`1e-3`、停止条件$\text{tol}$は`1e-6`としてください。

`# your code here`の部分にコードを記述してください。

```python
import numpy as np

def gradient_descent(f, grad, x0, alpha=1e-3, tol=1e-6):
    """
    Gradient descent (optimization algorithm)

    Parameters
    ----------
    f : function
        The function to minimize
    grad : function
        The gradient of the function
    x0 : np.ndarray
        Initial guess
    alpha : float
        Step size
    tol : float
        Tolerance

    Returns
    -------
    x : np.ndarray
        The estimate of the minimum
    """
    
    # your code here

    while np.linalg.norm(grad(x)) > tol:
        # your code here
    return x


def f(x):
    return x[0]**2 + x[1]**2

def grad(x):
    return np.array([2*x[0], 2*x[1]])

x0 = np.array([1.0, 1.0])
x = gradient_descent(f, grad, x0)
print(x)
```

### 課題3 (20点)

Sphere関数を最小化する問題を考えます。Sphere関数は以下のように定義されます。

$$
f(\mathbf{x}) = \sum_{i=1}^{n} x_i^2
$$

$n$次元のSphere関数の最小値は$\mathbf{x} = \mathbf{0}$であり、その値は$f(\mathbf{0}) = 0$です。探索空間は$\mathcal{X} = [-5.12, 5.12]^n$です。

`# your code here`の部分にコードを記述してください。

```python
import numpy as np


def sphere(x):
    """
    Sphere function

    Parameters
    ----------
    x : np.ndarray
        The input vector

    Returns
    -------
    float
        The value of the Sphere function
    """
    return np.sum(x**2)


def random_search(f, num_iter, search_space, num_dim):
    """
    Random Search

    Parameters
    ----------
    f : function
        The objective function
    num_iter : int
        Number of iterations
    search_space : tuple
        The search space
    num_dim : int
        Number of dimensions

    Returns
    -------
    x : np.ndarray
        The estimate of the solution
    """

    x = np.random.uniform(search_space[0], search_space[1], num_dim)

    for _ in range(num_iter):
        # your code here
        if f(x_new) < f(x):
            # your code here

    return x


# number of dimensions
n = 2
# search space
search_space = (-5.12, 5.12)
# number of iterations
num_iter = 1000000

x = random_search(sphere, num_iter, search_space, n)
print("Estimated solution:", x)
```

### 課題4 (20点)

ナップサック問題は、最適化問題の一つで、与えられた重さと価値を持つアイテムの集合から、重さの合計が制限内で価値の合計を最大化するアイテムの集合を見つける問題です。

ナップサック問題の設定は以下の通りです。

- $n$: アイテムの数
- $\mathcal{I}$: アイテムの集合, $\mathcal{I} = \{1, 2, \ldots, n\}$
- $w_i$: アイテム$i$の重さ
- $v_i$: アイテム$i$の価値
- $W$: ナップサックの重さの制限
- $x_i$: アイテム$i$をナップサックに入れるかどうかを表すバイナリ変数, $x_i \in \{0, 1\}$

この問題の目的は、アイテムの集合$\mathcal{I}$から選んだアイテムの重さの合計が$W$以下となるようにして、価値の合計を最大化するアイテムの集合を見つけることです。

最適化問題は以下のように定式化されます。

$$
\begin{align*}
\text{maximize} \quad & \sum_{i \in \mathcal{I}} v_i x_i \\
\text{subject to} \quad & \sum_{i \in \mathcal{I}} w_i x_i \leq W \\
& x_i \in \{0, 1\}, \quad \forall i \in \mathcal{I}
\end{align*}
$$

Random Searchを用いて、ナップサック問題を解くPythonプログラムは以下の通りです。

`np.where()`関数は、条件を満たす要素のインデックスを返します。

```python
import numpy as np


def knapsack_value(x):
    """
    Calculate the total value of selected items

    Parameters
    ----------
    x : np.ndarray
        The vector with binary values, 1 if the item is selected, 0 otherwise

    Returns
    -------
    float
        The total value
    """
    return np.sum(v * x)


def knapsack_weight(x):
    """
    Calculate the total weight of selected items

    Parameters
    ----------
    x : np.ndarray
        The vector with binary values, 1 if the item is selected, 0 otherwise

    Returns
    -------
    float
        The total weight
    """
    return np.sum(w * x)


def random_search(num_item, num_iter):
    """
    Random Search for Knapsack Problem

    Parameters
    ----------
    num_item : int
        Number of items
    num_iter : int
        Number of iterations

    Returns
    -------
    x : np.ndarray
        The estimate of the solution
    """

    x = np.zeros(num_item)
    
    for _ in range(num_iter):
        x_new = np.random.randint(0, 2, num_item)
        if knapsack_weight(x_new) <= W and knapsack_value(x_new) > knapsack_value(x):
            x = x_new

    return x


# weight of items
w = np.array([7, 5, 3, 2, 8])
# value of items
v = np.array([5, 10, 8, 4, 7])
# knapsack capacity
W = 15
# number of items
num_item = len(w)
# number of iterations
num_iter = 500

x = random_search(num_item, num_iter)
print("Selected items:", np.where(x == 1)[0])
print("Total value:", knapsack_value(x))
print("Total weight:", knapsack_weight(x))
```

#### 課題 4-1 (5点)

ソースコードでは、`x = np.zeros(num_item)`で初期解を設定しています。なぜこのような初期解が設定されているのか、説明してください。ランダムに初期解を設定すると、どのような問題が発生する可能性があるか、考察してください。

#### 課題 4-2 (5点)

ソースコードでは、`knapsack_weight(x_new) <= W and knapsack_value(x_new) > knapsack_value(x)`という条件で解を更新しています。この条件について、なぜこのような条件が設定されているのか、説明してください。

#### 課題 4-3 (10点)

他の効率的に初期解を設定する方法を考えてください。新しい初期解の設定方法を実装し、その効果を調査してください。

アルゴリズムの比較について、以下の表を作成してください。ランダムサーチには、ランダム性があるため、複数回（10回程度）実行して平均値を求めてください。

解を$\mathbf{x}$としたとき、その評価値を$\sum_{i \in \mathcal{I}} v_i x_{i}$とします。

Table: 解の評価値の比較

| 指標 | ランダムサーチ | 提案手法 |
| --- | --- | --- |
| `n_iter = 10` |  |  |
| `n_iter = 100` |  |  |
| `n_iter = 1000` |  |  |

##### ヒント

```{note}
例えば、$v_1 / w_1, v_2 / w_2, \ldots, v_n / w_n$の値がアイテムの価値を重さで割った値であり、これを基準にアイテムを選択する方法が考えられます。
```

`np.argsort()`関数は、配列の要素を昇順に並べ替えたインデックスを返します。

```python
import numpy as np

a = np.array([3, 1, 2])
idx = np.argsort(a)
print(idx)
```






