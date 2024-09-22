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



# Tuple

In mathematics, a tuple is a collection of elements in which repetition is allowed and order matters (remember that in sets, repetition is not allowed and order does not matter).

A tuple is usually denoted by round brackets. For example, $(1, 2, 2, 3)$ and $(1, 3, 2, 2)$ are lists, and since order matters, they are different lists.  

A tuple can be represented by a letter, e.g., $a = (1, 2, 3)$, where $a_1 = 1$, $a_2 = 2$, and $a_3 = 3$.

An $n$-tuple is a tuple with $n$ elements. For example, $(1, 2, 3)$ is a 3-tuple. A 1-tuple is called a *singleton*, and a 2-tuple is called an *ordered pair*.

In Python, a tuple is a collection of elements that is ordered and immutable. Tuples are defined by enclosing the elements in parentheses `()`. For example:

```python
tuple_1 = (1, 2, 3)
tuple_2 = ('a', 'b', 'c')
print(tuple_1)  # Output: (1, 2, 3)
print(tuple_2)  # Output: ('a', 'b', 'c')
```

A list is a collection of elements that is ordered and mutable. Lists are defined by enclosing the elements in square brackets `[]`. For example:

```python
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
print(list_1)  # Output: [1, 2, 3]
print(list_2)  # Output: ['a', 'b', 'c']
```

The main difference between a tuple and a list is that a tuple is immutable, while a list is mutable. This means that the elements of a tuple cannot be changed, while the elements of a list can be changed.

```python
tuple_1 = (1, 2, 3)

# Attempting to change the first element of tuple_1 will raise an error
tuple_1[0] = 4  
```

```python
list_1 = [1, 2, 3]

# Changing the first element of list_1
list_1[0] = 4
print(list_1)  # Output: [4, 2, 3]
```

# Big Sum

In mathematics, the big sum is used to represent the sum a collection of elements. The big sum notation is denoted by the symbol $\sum$. A basic usage of the big sum notation is as follows:

$$
\sum_{i=\text{start}}^{\text{end}} \text{expression}
$$

For example, the sum of the first $n$ natural numbers can be represented as:

$$
\sum_{i=1}^{n} x_i^2 = x_1^2 + x_2^2 + \ldots + x_n^2
$$

In addition, we can use the big sum notation to traverse a list of elements. Let's consider a set $A = \{5, 10, 15, 20\}$. The sum of the elements in set $A$ can be represented as:

$$
\sum_{x \in A} x = 5 + 10 + 15 + 20
$$

In Python, the `sum()` function can be used to calculate the sum of a collection of elements. 

Let's consider a set $A = \{5, 10, 15, 20\}$. Then, $\sum_{x \in A} (x^2 + 1)$ can be calculated as follows:

```python
set_1 = {5, 10, 15, 20}
result = sum([x**2 + 1 for x in set_1])
print(result)
```

# Function

In mathematics, a function is a mapping from a set of inputs to a set of outputs. In general, given a set $A$ and a set $B$, the notation $f: A \rightarrow B$ denotes that the function $f$ takes an input from set $A$ and returns an output in set $B$. 

Note that it is not necessary that every element in set $B$ be an output of the function $f$. For example, $\sin: \mathbb{R} \rightarrow \mathbb{R}$ denotes that the sine function takes a real number as input and returns a real number as output. Although the output of the sine function is within the range $[-1, 1]$.


Given a function $f: A \rightarrow B$ and an element $x \in A$, the value of the function $f$ at $x$ is denoted by $f(x)$. 

For example, if $f(x) = x^2$, then $f(2) = 2^2 = 4$.

Another way to represent the value of a function is by using the notation 

$$
f(x) \rvert_{x=a}.
$$

In addition, $y = f(x)$ can be written as $x \xmapsto{f} y$ or $x \mapsto y$. 

In Python, functions can be defined using the `def` keyword. For example, the function $f(x) = x^2$ can be defined as follows:

```python
def f(x):
    return x**2
```

When we want to know the value of the function $f$ at $x = 2$, we can call the function `f` with the argument `2`:

```python
result = f(2)
print(result)  # Output: 4
```