---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 数学とPythonプログラミング

## Equality

- **Equality.** A relation between two mathmatical expressions that have the same mathematical object. For example, $1 + 1 = 2$.
- **Assignment.** If $E$ is an expression, and $x$ is a variable, then $x \coloneqq E$ is an assignment statement that assigns the value of $E$ to the variable $x$.
- **Inequality.** A relation between two mathmatical expressions that do not have the same mathematical object. For example, $1 + 1 \neq 3$.
- **Approximation.** A relation between two mathmatical expressions that are approximately equal. For example, $\pi \approx 3.14159$.

In Python:

```{code-cell}
## Equality
1 + 1 == 2
```

```{code-cell}
## Assignment
x = 1 + 1
print(x)
```

```{code-cell}
## Inequality
1 + 1 != 3
```

```{code-cell}
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

```{code-cell}
set_1 = {1, 2, 3}
print(set_1)
```
