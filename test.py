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