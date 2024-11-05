# 第4週目

## 学習内容

[Pythonプログラミング入門](https://utokyo-ipp.github.io/index.html#)にアクセスし、以下の内容を学習してください。

- [クラス](https://utokyo-ipp.github.io/6/6-3.html)


## パーセプトロン

パーセプトロンは、教師あり学習の最も古いアルゴリズムの1つです。パーセプトロンは、1943年にWarren McCullochとWalter Pittsによって提案され、1957年にFrank Rosenblattによって実装されました。

パーセプトロンは、入力$\mathbf{x} \in \mathbb{R}^d$を出力値$f(\mathbf{x}) \in \{-1, 1\}$にマッピングするバイナリ線形分類器です。パーセプトロンは次のように表すことができます。

$$
f(\mathbf{x}) = h(\mathbf{w} \cdot \mathbf{x} + b)
$$

ここで、$\mathbf{w}$は重みベクトル、$\mathbf{w} \in \mathbb{R}^d$、$\mathbf{b}$はバイアス、$h(\cdot)$は次のように定義されます。

$$
h(z) =
\begin{cases}
1 & \text{if } z \geq 0 \\
-1 & \text{otherwise}
\end{cases}
$$

適切な重みベクトル$\mathbf{w}$とバイアス$b$の値を設定することで、パーセプトロンは入力データ$\mathbf{x}$を$-1$と$1$の出力値で表される2つのクラスに分類することを学習することができます。

### 損失関数

説明を簡略化するために、$\hat{y}^{(i)} = f(\mathbf{x}^{(i)})$を使用して、入力$\mathbf{x}^{(i)}$のパーセプトロンの予測を表します。入力$\mathbf{x}^{(i)}$の真のラベルを$y^{(i)}$とします。パーセプトロンは、$\hat{y}^{(i)} = y^{(i)}$の場合は正しい予測を行い、$\hat{y}^{(i)} \neq y^{(i)}$の場合は誤った予測を行います。

パーセプトロン学習アルゴリズムで使用される損失関数は、ヒンジ損失と呼ばれ、次のように定義されます。

$$
\mathcal{L}(\mathbf{w}, b) = \sum_{i=1}^{n} \max(0, -y^{(i)} \hat{y}^{(i)})
$$

単一のサンプル$(\mathbf{x}_i, y_i)$のヒンジ損失は次のようになります。

$$
\mathcal{L}_i(\mathbf{w}, b) = \max(0, -y^{(i)} \hat{y}^{(i)})
$$

$y^{(i)}$と$\hat{y}^{(i)}$はどちらも$-1$または$1$のいずれかです。したがって、

- $y^{(i)} = f(\mathbf{x}^{(i)})$の場合、予測は正しい（すなわち、$y^{(i)} \hat{y}^{(i)} = 1$）ため、ヒンジ損失はゼロです。
- $y^{(i)} \neq f(\mathbf{x}^{(i)})$の場合、予測は誤っています（すなわち、$y^{(i)} \hat{y}^{(i)} = -1$）ため、ヒンジ損失は$-y^{(i)} \hat{y}^{(i)} = 1$です。

「完璧な」分類器の場合、ヒンジ損失$\mathcal{L}(\mathbf{w}, b) = 0$です。 

### 最適化

パーセプトロン学習アルゴリズムの目標は、ヒンジ損失を最小化することで、重みベクトル$\mathbf{w}$とバイアス$b$を更新することです。これを達成するために、損失を減少させる方向にパラメータを更新するために最急降下法を使用します。重みベクトル$\mathbf{w}$とバイアス$b$の更新ルールは次のとおりです。

$$
\begin{align*}
\mathbf{w} &\leftarrow \mathbf{w} - \eta \nabla_{\mathbf{w}} \mathcal{L}_i(\mathbf{w}, b) \\
b &\leftarrow b - \eta \nabla_{b} \mathcal{L}_i(\mathbf{w}, b)
\end{align*}
$$

ここで、$\nabla_{\mathbf{w}} \mathcal{L}_i(\mathbf{w}, b)$と$\nabla_{b} \mathcal{L}_i(\mathbf{w}, b)$は、サンプル$(\mathbf{x}^{(i)}, y^{(i)})$に対するヒンジ損失の重みベクトル$\mathbf{w}$とバイアス$b$に関する勾配です。

$-y^{(i)} \hat{y}^{(i)} \leq 0$の場合、ヒンジ損失の勾配はゼロであり、重みベクトル$\mathbf{w}$とバイアス$b$は変更されません。

$-y^{(i)} \hat{y}^{(i)} > 0$の場合、サンプル$(\mathbf{x}_i, y_i)$に対するヒンジ損失の重みベクトル$\mathbf{w}$とバイアス$b$の勾配は次のようになります。

$$
\begin{align*}
\nabla_{\mathbf{w}} \mathcal{L}(\mathbf{w}, b) &= -y^{(i)} \mathbf{x}^{(i)} \\
\nabla_{b} \mathcal{L}(\mathbf{w}, b) &= -y^{(i)}
\end{align*}
$$

これらの勾配を更新ルールに代入すると、次のようになります。

$$
\begin{align*}
\mathbf{w} &\leftarrow \mathbf{w} + \eta y^{(i)} \mathbf{x}^{(i)} \\
b &\leftarrow b + \eta y^{(i)}
\end{align*}
$$

重みベクトル$\mathbf{w}$とバイアス$b$を更新する別の方法があります。

$$
\begin{align*}
\mathbf{w} &\leftarrow \mathbf{w} + \eta (y^{(i)} - \hat{y}^{(i)}) \mathbf{x}_i \\
b &\leftarrow b + \eta (y^{(i)} - \hat{y}^{(i)})
\end{align*}
$$

この更新ルールは、前のものと同等です。$y^{(i)} = \hat{y}^{(i)}$の場合、更新はゼロであり、重みベクトル$\mathbf{w}$とバイアス$b$は変更されません。$y_i \neq \hat{y}^{(i)}$の場合、更新は$y^{(i)} - \hat{y}^{(i)}$であり、これは$2 y^{(i)}$と等価です。学習率$\eta$を調整することで、これら2つの更新ルールを同等と見なすことができます。

### アルゴリズム

パーセプトロン学習アルゴリズムの実装では、$x_0 = 1$および$w_0 = b$を設定することで、以下のように表現することができます。

$$
\mathbf{w} = [b, w_1, w_2, \ldots, w_n]
$$

および

$$
\mathbf{x} = [1, x_1, x_2, \ldots, x_n]
$$

ここで、$\mathbf{w} \in \mathbb{R}^{n+1}$および$\mathbf{x} \in \mathbb{R}^{n+1}$です。パーセプトロンは次のように表現することができます。

$$
f(\mathbf{x}) = h(\mathbf{w} \cdot \mathbf{x})
$$

ここで、$\mathbf{w} \cdot \mathbf{x} = \sum_{j=0}^{n} w_j x_j$です。

$x^{(i)}_0 = 1$と設定したため、更新ルールは次のように簡略化されます。

$$
\mathbf{w} \leftarrow \mathbf{w} + \eta y^{(i)} \mathbf{x}^{(i)}
$$

パーセプトロン学習アルゴリズムは、以下の通りです。

```{prf:algorithm} Perceptron Learning Algorithm
:label: perceptron-learning-algorithm

**Input**: Training data $\mathcal{D} = \{(\mathbf{x}_1, y_1), (\mathbf{x}_2, y_2), \ldots, (\mathbf{x}_n, y_n)\}$, Learning rate $\eta$, Number of epochs $T$   
**Output**: Weight vector $\mathbf{w}$

1. Initialize $\mathbf{w} \leftarrow \mathbf{0}$ 
2. **For** $t = 1$ to $T$
    1. **For** $i = 1$ to $n$
        1. Compute the prediction $f(\mathbf{x}^{(i)}) = h(\mathbf{w} \cdot \mathbf{x}^{(i)})$
        2. **If** $y^{(i)} f(\mathbf{x}^{(i)}) \leq 0$
            1. Update the weight vector $\mathbf{w} \leftarrow \mathbf{w} + \eta y^{(i)} \mathbf{x}^{(i)}$
3. **Return** $\mathbf{w}$
```

パーセプトロン学習アルゴリズムでは、重みベクトル$\mathbf{w}$は、トレーニングデータ$\mathcal{D}$の各トレーニング例$(\mathbf{x}^{(i)}, y^{(i)})$に対して反復的に更新されます。学習率$\eta$は、更新のステップサイズを制御します。アルゴリズムは、固定されたエポック数$T$または収束まで続行されます。

## 課題

Colabで新しいノートブックを作成し、以下の課題をそれぞれ一つのセルに記述してください。ファイル名は`week-4.ipynb`としてください。実験の成果物を Moodle 経由で提出しもらいます。

今回の課題3と4は、論文やネット上の情報を参考にしても構いませんが、その場合は参考文献を明記してください。

### 課題1(40点)

`your code here`の部分にコードを追加して、パーセプトロンアルゴリズムを実装してください。

```python
import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, learning_rate=0.1, n_iter=100):
        self.learning_rate = learning_rate
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        Fit the model to the data

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            Training data
        y : array-like, shape = [n_samples]
            Target values

        Returns
        -------
        self : object
        """

        # Initialize weights and bias
        self.w = np.zeros(1 + X.shape[1])
        self.errors = []

        # Train
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                if self.predict(xi) != target:
                    # your code here, update weights and bias
                    # Note: be careful with the size of the array self.w and xi
                    # Hint: self.w[0] is the bias term
                    errors += int(update != 0.0)
            self.errors.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w[1:]) + self.w[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def plot_errors(self):
        plt.plot(range(1, len(self.errors) + 1), self.errors, marker="o")
        plt.xlabel("Epochs")
        plt.ylabel("Number of updates")
        plt.show()


# Load data (linearly separable), blobs

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# plot data
figure = plt.figure()
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], s=40, c="red", marker="o", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], s=40, c="blue", marker="x", label="1")
plt.legend()
plt.show()

# make labels -1 and 1
y = np.where(y == 0, -1, 1)

# Train model
ppn = Perceptron(learning_rate=0.1, n_iter=10)
ppn.fit(X, y)

# plot errors
ppn.plot_errors()

# plot decision boundary
w = ppn.w[1:]
b = ppn.w[0]

plt.scatter(X[y == -1][:, 0], X[y == -1][:, 1], s=40, c="red", marker="o", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], s=40, c="blue", marker="x", label="1")

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1

y_min = (-w[0] * x_min - b) / w[1]
y_max = (-w[0] * x_max - b) / w[1]

plt.plot([x_min, x_max], [y_min, y_max], "k-")
plt.legend()
plt.show()
```

### 課題2(20点)

scikit-learnの[Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html)クラスを使用して、パーセプトロンアルゴリズムを実装して、課題1の分類問題に適用してください。

`Perceptron`クラスから`ppn`オブジェクトを作成し、`fit`メソッドを使用してモデルをトレーニングし、下記のコードを使用して結果の精度を確認してください。出力が`1.0`に近いほど、モデルの性能が高いことを示します。

```python
from sklearn.linear_model import Perceptron

# your code here

print(f"Accuracy: {ppn.score(X, y)}")
```

### 課題3(20点)

現実社会では、バイナリ分類機が適用できる例を挙げてください。その例において、入力データ$\mathbf{x}$と出力値$f(\mathbf{x})$は何ですか？

### 課題4(20点)

パーセプトロンにおいて、最急降下法はどのような最適化問題に適用されるかを説明せよ。
例：最適化問題の目的関数、決定変数は何かを説明する。