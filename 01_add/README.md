# Problem Statement

Hey!

I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

```
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
```

Try to solve this exercise without using any third-party libraries (without using pandas for example).

Before attempting any bonuses, I'd like you to put some effort into figuring out the clearest and most idiomatic way to solve this problem. If you're using indexes to loop, take a look at the first hint.

There are two bonuses this week.

Bonus 1

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️

```
>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
```

Bonus 2

For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️

```
>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.
```

# My solution

My solution is almost exactly as described in the given solution. We use variable positional arguments to allow the
user to pass as many list of lists as required to the function. We then unpack and zip these lists of lists using
```zip(*lists)``` twice so we can iterate through the elements of each list in each list of lists,
sum the elements, and return the sums in a list using list comprehension.

For the second bonus, namely raising an exception if the dimensions don't match, my solution was similar but not
optimal. I first check and compare the dimensions of the lists, and then the dimensions of the lists in the lists.
The easier method is to pack the dimensions of each list of lists into a tuple and check that all tuples are the same
(namely by checking the set of the tuples is size 1).