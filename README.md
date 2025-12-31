# AI-ML-from-day-0
# month 0
  Being comfortable with python and basic mathematics. Focusing only on what machine learning needs.
#day 0

## Variables in Python 

### What is a Variable?

A **variable** is a name that stores data in memory.
You can think of it as a **label on a box** that holds a value.

In Python, variables help us store and manipulate data like numbers, text, images, model parameters, etc.
They are the **foundation of AI, ML, and programming in general**.

---

### Creating a Variable in Python

Python is simple — you don’t need to declare the data type.

```python
x = 10
name = "Prabha"
pi = 3.14
is_learning_ai = True
```

Here:

* `x` stores an integer
* `name` stores text (string)
* `pi` stores a decimal value (float)
* `is_learning_ai` stores a boolean value

---

### Rules for Naming Variables

 Must start with a letter or `_`
 Can contain letters, numbers, and `_`
 Cannot start with a number
 Cannot use Python keywords

 Valid:

```python
age = 17
learning_AI = True
_model = "claude"
```

 Invalid:

```python
2age = 17
class = 10
my-name = "AI"
```

---

### Variable Types (Basic)

Python automatically decides the type.

| Type    | Example | Meaning         |
| ------- | ------- | --------------- |
| `int`   | `10`    | Integer numbers |
| `float` | `3.5`   | Decimal numbers |
| `str`   | `"AI"`  | Text            |
| `bool`  | `True`  | True / False    |

Check type using:

```python
x = 10
print(type(x))
```

---

### Updating a Variable

Variables can be changed anytime.

```python
x = 5
x = x + 3
print(x)  # Output: 8
```

---

### Multiple Assignment

Python allows assigning multiple variables at once.

```python
a, b, c = 1, 2, 3
```



### Why Variables Matter in AI 

In AI & ML, variables store:

* Training data
* Model weights
* Learning rates
* Predictions
* Loss values

Example:

```python
learning_rate = 0.01
epochs = 100
```

Without variables, **AI models cannot learn or store information**.

