# 数学とPythonプログラミング

## Equality

- **Equality.** A relation between two mathmatical expressions that have the same mathematical object. For example, $1 + 1 = 2$.
- **Assignment.** If $E$ is an expression, and $x$ is a variable, then $x \coloneqq E$ is an assignment statement that assigns the value of $E$ to the variable $x$.
- **Inequality.** A relation between two mathmatical expressions that do not have the same mathematical object. For example, $1 + 1 \neq 3$.
- **Approximation.** A relation between two mathmatical expressions that are approximately equal. For example, $\pi \approx 3.14159$.

In Python:

```python
## Equality
1 + 1 == 2
```

```python
## Assignment
x = 1 + 1
print(x)
```

```python
## Inequality
1 + 1 != 3
```

```python
## Approximation
import math

math.isclose(1.5, 2)
```

For more information on the `math.isclose()` function in Python, see the [Python documentation](https://docs.python.org/3/library/math.html#math.isclose).

```{note}
The difference between $=$ and $\coloneqq$ is that the former is an equality relation, while the latter is an assignment statement. In Python, `a = b` is an assignment statement that assigns the value of `b` to the variable `a`. The equality relation is expressed as `a == b`, which returns a boolean value (`True` or `False`).
```

## Collections

### Sets

A *set* is a collection of distinct objects. For example, $\{1, 2, 3\}$ is a set.

```python
set_1 = {1, 2, 3}
print(set_1)
```
