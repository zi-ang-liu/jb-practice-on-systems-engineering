# Logic in Python
In Python, the logical operators are `and`, `or`, and `not`. 

| Operator | Description                                   | Example             |
| -------- | --------------------------------------------- | ------------------- |
| `and`    | Returns True if both statements are true      | `x < 5 and  y < 10` |
| `or`     | Returns True if one of the statements is true | `x > 10 or x < 5`   |
| `not`    | Returns False if the result is true           | `not(x < 5)`        |

The following example demonstrates the use of logical operators in Python:
```python
x = 5
y = 10
print(x < 10 and y > 5)  # Output: True
print(x < 10 or y < 5)    # Output: True
print(not(x > 5))         # Output: False
```

# Quantifiers

The two most common quantifiers are the *universal quantifier* and the *existential quantifier*.

- **Universal Quantifier.** The universal quantifier, denoted by the symbol $\forall$, is used to express that a statement is true for all elements in a set. For example, $\forall x \in \mathbb{N}, x > 0$ means that for all natural numbers $x$, $x$ is greater than zero.
- **Existential Quantifier.** The existential quantifier, denoted by the symbol $\exists$, is used to express that a statement is true for at least one element in a set. For example, $\exists x \in \mathbb{N}, x^2 = 4$ means that there exists a natural number $x$ such that $x^2 = 4$. 


To improve readability of existential quantifiers, the word "such that" (s.t.) is often used in place of the comma. For example, $\exists x \in \mathbb{N} \text{ s.t. } x^2 = 4$.

In addition, the expression $\exists! x \in \mathbb{R}, x^2 = 0$ denotes that there exists exactly one real number $x$ such that $x^2 = 0$.

In Python, `for` loops can be used to iterate over a set of elements. 
```python
set_1 = {1, 2, 3, 4, 5}
for x in set_1:
    print(x)
```

If we want to check if $\forall x \in \{1, 2, 3, 4, 5\}, x > 0$, we can use the following code:
```python
set_1 = {1, 2, 3, 4, 5}
result = []
for x in set_1:
    result.append(x > 0)
print(all(result))  # Output: True
```
where `all()` returns `True` if all elements in the iterable are true.

The code above can be simplified using a list comprehension:
```python
set_1 = {1, 2, 3, 4, 5}
print(all([x > 0 for x in set_1]))  # Output: True
```

Similarly, if we want to check if $\exists x \in \{1, 2, 3, 4, 5\} \text{ s.t. } x^2 = 4$, we can use the following code:
```python
set_1 = {1, 2, 3, 4, 5}
print(any([x**2 == 4 for x in set_1]))  # Output: True
```
where `any()` returns `True` if any element in the iterable is true.