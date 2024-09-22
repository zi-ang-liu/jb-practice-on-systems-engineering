# 第1週目

## 学習内容

[Pythonプログラミング入門](https://utokyo-ipp.github.io/index.html#)にアクセスし、以下の内容を学習してください。

- Google Colabの使い方
- 数値演算
- 変数と関数の基礎
- 論理・比較演算と条件分岐の基礎

## 課題

Colabで新しいノートブックを作成し、以下の課題をそれぞれ一つのセルに記述してください。ファイル名は`week-1.ipynb`としてください。

### 課題1
黄金比を求めてください。黄金比とは、5 の平方根に 1 を加えて 2 で割ったものです。約 1.618 になるはずです。

```python
# your code here
print(golden_ratio)
```

### 課題2

単価，数量を入力し，金額と消費税込みの金額を表示する．消費税率は 10% とする．

```python
price = int(input("単価を入力してください: "))
quantity = int(input("数量を入力してください: "))
# your code here
# hint: 金額は整数として扱う
print("金額: ", total)
print("消費税込みの金額: ", total_price)
```

### 課題3

秒数で表される時間を入力し，時間・分・秒に変換し表示するプログラムを作れ．

```python
seconds = int(input("秒数を入力してください: "))
# your code here
print("時間: ", hours)
print("分: ", minutes)
print("秒: ", seconds)
```

### 課題4
$f(x) = x^2 + 2x + 1$の関数を定義し、$f(3)$を計算してください。

```python
def f(x):
    # your code here

print(f(3))
```

### 課題5
成績を入力して、成績に応じて以下のように表示するプログラムを作成してください。

- 90点以上: A
- 80点以上: B
- 70点以上: C
- 60点以上: D
- 60点未満: F

```python
def grade(score):
    # your code here

score = int(input("点数を入力してください: "))
print(grade(score))
```