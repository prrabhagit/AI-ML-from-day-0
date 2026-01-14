
#  Day 0 of AI / ML — Foundations Only

### Goal of Day 0

-Build **mental clarity + basic tools**, not intelligence
-No math, no models, no pressure

---

## 1>>> What AI / ML Actually Is (Conceptual)

You should clearly understand this sentence:

> **Machine Learning = teaching a computer to learn patterns from data instead of writing rules**

### Learn the difference:

* **AI** → Big umbrella (smart behavior)
* **ML** → Learning from data
* **DL** → Neural networks (later)

 Day 0 rule:
If you can explain this to a non-tech person → you’re ready.

---

## 2>>>> Python Basics (Only These)

You **DO NOT** learn full Python today.

Learn ONLY:

* Variables 
* Data types (`int, float, str, bool`)
* `print()`
* Comments (`#`)
* Simple input/output

Example:

```python
name = "AI from 0"
day = 0
print(name, day)
```

- If you understand this → enough for Day 0.

---

## 3>>>> How Code Thinks (VERY IMPORTANT)

Learn **how a computer thinks**:

* Top to bottom
* Line by line
* No emotions, no guessing
Example:

```python
x = 5
x = x + 2
print(x)
```

Output is `7` because computer follows steps **literally**.

This mindset matters more than syntax.

---

## 4️>>>> Basic Command Line Awareness (Light)

Just know:

* What a **terminal** is
* What `python file.py` means
* What an error message looks like

No Linux mastery. Just awareness.

---

## 5>>> Git & GitHub (Observer Level)

For Day 0, only understand:

* GitHub = place to store code
* Repo = project folder
* README = explanation file

You **do not** need commands yet.

---

## 6️>>> Math? -- NOT TODAY

No:

* Linear algebra
* Calculus
* Probability

 Day 0 is about **confidence**, not intelligence.

---

## 7️>>>> Mindset for AI (Most Important)

You must accept:

* AI is **slow learning**
* Confusion is normal
* Consistency beats talent
* You will re-learn the same thing multiple times

This is not a sprint.

---

## ---- Day 0 Checklist (If all true → you’re done)

✔ I know what AI / ML means
✔ I can write basic Python variables
✔ I understand code runs line by line
✔ I’m not scared of errors
✔ I’m excited, not overwhelmed

If yes → **Day 0 completed **

---

##  What Comes on Day 1 (Preview)

* Python data types (deep)
* Lists & loops
* First tiny “learning logic”
* Thinking like a machine

---










#  Day 1 of AI / ML (Python + Thinking)

###  Goal of Day 1

By the end of today, you should:

* Think **logically like a machine**
* Be comfortable with **core Python**
* Be ready to handle **data (very small data)**

No AI models yet. This is **foundation day**.

---

## Time Plan (2–3 hours total)

### 1️>> Data Types (40 min)

You already met them. Now understand them.

| Type    | Example | Use in AI      |
| ------- | ------- | -------------- |
| `int`   | `10`    | counts, epochs |
| `float` | `0.01`  | learning rate  |
| `str`   | `"cat"` | labels, text   |
| `bool`  | `True`  | conditions     |

```python
x = 10
y = 2.5
name = "AI"
is_ai_fun = True

print(type(x), type(y), type(name), type(is_ai_fun))
```

---

### 2️>> Input & Output (20 min)

Make programs interactive.

```python
name = input("Enter your name: ")
print("Welcome to AI,", name)
```

Understand:

* `input()` always gives **string**
* Convert when needed

```python
age = int(input("Enter age: "))
```

---

### 3>> Operators (30 min)

These are **thinking tools**.

#### Arithmetic

```python
+  -  *  /  //  %  **
```

#### Comparison (VERY IMPORTANT)

```python
>  <  >=  <=  ==  !=
```

Example:

```python
x = 10
print(x > 5)   # True
```

---

### 4>> Conditions (If–Else) (40 min)

This is where **decision-making** starts.

```python
marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

AI = lots of **conditions + data**.

---

### >> Lists (Core of ML Data) (40 min)

Lists store **multiple values**.

```python
marks = [60, 70, 80, 90]
print(marks[0])
```

Why lists matter:

* Datasets = lists
* Features = lists
* Outputs = lists

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

---

### >> Loops (Machine Repetition) (30 min)

Machines are good at repetition.

```python
for i in range(5):
    print(i)
```

Loop through data:

```python
marks = [60, 70, 80]

for m in marks:
    print(m)
```

AI training = loops + updates.

---

##  Mini Practice (MANDATORY)

Do these without copy-paste:

> Take 5 numbers from user, store in list
> Print all numbers
> Print numbers greater than 50

Example logic:

```python
numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

for n in numbers:
    if n > 50:
        print(n)
```

---



##  Mindset Check

* Confusion = progress
* Errors = learning
* Repetition = mastery

---

##  Day 2 Preview

* Functions
* Tuples & dictionaries
* Problem-solving like ML
* Tiny “learning logic” program





#  Day 2 — Functions, Data Structures & Thinking Like ML

###  Goal of Day 2

By the end of Day 2, a beginner should:

* Write **functions**
* Use **tuples & dictionaries**
* Start thinking in **inputs → processing → outputs**
* Understand how ML code is structured

Still **no models yet** — but now you’re coding *like* ML.

---

## 1️. Functions (Core of ML Code)

### What is a Function?

A function is a **reusable block of code** that performs a task.

```python
def greet():
    print("Welcome to AI")
```

Call it:

```python
greet()
```

---

### Function with Parameters

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Why functions matter in ML:

* training step
* prediction step
* evaluation step

All are functions.

---

## 2️. Return vs Print (IMPORTANT)

```python
def square(x):
    return x * x
```

 `return` gives value back
 `print` only displays

ML functions **always return values**.

---

## 3️. Tuples (Fixed Data)

Tuples are **immutable** (cannot be changed).

```python
point = (3, 5)
x, y = point
```

Used for:

* coordinates
* dataset rows
* fixed configs

---

## 4️. Dictionaries (KEY ML STRUCTURE)

### What is a Dictionary?

Stores data as **key : value pairs**.

```python
student = {
    "name": "Prabha",
    "age": 17,
    "field": "AI"
}
```

Access:

```python
print(student["name"])
```

Why dictionaries matter in ML:

* model parameters
* datasets
* configs
* metrics

Example:

```python
metrics = {
    "loss": 0.23,
    "accuracy": 92.5
}
```

---

## 5️. Looping Through Dictionaries

```python
for key, value in metrics.items():
    print(key, value)
```

This is **very common** in training logs.

---

## 6. Simple ML-Style Logic (IMPORTANT)

### Example: Mean (Average)

```python
def mean(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

data = [10, 20, 30, 40]
print(mean(data))
```

This is **literally how ML starts**.

---

## 7️. Input → Process → Output (ML Thinking)

```python
def classify(score):
    if score >= 50:
        return "Pass"
    return "Fail"
```

ML is just **complex versions of this**.

---

##  Practice (Mandatory)

> Write a function to find max in a list
> Store student info in dictionary
> Loop through dictionary and print neatly

Example:

```python
def find_max(nums):
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
    return m
```

---



##  Day 2 Mindset

* Functions = ML blocks
* Dictionaries = ML memory
* Loops = training
* Logic = intelligence

---

##  Day 3 Preview

* Lists (deep)
* Nested loops
* Data preprocessing mindset
* First tiny “learning” system




# Day 3 — Lists, Loops & Simple Data Handling

## Goal

* Work comfortably with lists
* Use loops to process data
* Think step-by-step

---

## Lists (Deep Basics)

```python
numbers = [10, 20, 30, 40]
```

Access:

```python
numbers[0]
numbers[-1]
```

Modify:

```python
numbers.append(50)
numbers.remove(20)
```

---

## Looping Through Lists

```python
for n in numbers:
    print(n)
```

With index:

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

---

## Nested Lists

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Loop:

```python
for row in matrix:
    for value in row:
        print(value)
```

---

## Simple Data Processing

Sum:

```python
total = 0
for n in numbers:
    total += n
```

Filter:

```python
for n in numbers:
    if n > 25:
        print(n)
```

---

## Practice

1. Take 5 numbers from user
2. Store in list
3. Print max and average

---




# Day 4 — Strings, Files & Basic Data Cleaning

## Goal

* Work with text (strings)
* Read/write files
* Clean simple data

---

## Strings

```python
text = "AI from zero"
```

Basic operations:

```python
text.lower()
text.upper()
text.strip()
text.replace("zero", "0")
```

Split & join:

```python
words = text.split()
joined = " ".join(words)
```

---

## Looping Through Strings

```python
for ch in text:
    print(ch)
```

---

## Files (Read)

```python
file = open("data.txt", "r")
content = file.read()
file.close()
```

Line by line:

```python
for line in open("data.txt"):
    print(line.strip())
```

---

## Files (Write)

```python
file = open("output.txt", "w")
file.write("Hello World")
file.close()
```

---

## Basic Data Cleaning

Remove spaces:

```python
name = "  Prabha  "
clean = name.strip()
```

Lowercase + split:

```python
sentence = "Python Is Fun"
words = sentence.lower().split()
```

Remove empty values:

```python
data = ["10", "", "20", " ", "30"]
cleaned = [x for x in data if x.strip() != ""]
```

---

## Practice

1. Read a file
2. Convert text to lowercase
3. Remove empty lines
4. Save cleaned text to new file

---



# Day 5 — Data Handling & Simple Learning Logic

## Goal

* Work with numerical data
* Process data step by step
* Understand what “learning” means

---

## Working with Data

```python
data = [10, 20, 30, 40, 50]
```

Basic operations:

```python
min(data)
max(data)
sum(data)
len(data)
```

---

## Simple Feature Processing

```python
scaled = []
for x in data:
    scaled.append(x / max(data))
```

---

## Simple Rule-Based Prediction

```python
def predict(x):
    if x > 0.5:
        return 1
    return 0
```

---

## Measuring Performance

```python
y_true = [1, 0, 1, 1]
y_pred = [1, 0, 0, 1]

correct = 0
for i in range(len(y_true)):
    if y_true[i] == y_pred[i]:
        correct += 1

accuracy = correct / len(y_true)
print(accuracy)
```

---

## Core Idea

Learning =
data → rules → evaluation → improvement

---

## Practice

1. Normalize a list of numbers
2. Write a simple prediction rule
3. Calculate accuracy manually

---


## Next

* **Day 6**: Introduction to NumPy & arrays



### **Day 6 – NumPy & Arrays **

This is **core AI/ML groundwork**. Don’t rush this day.

---

## 1️. Array Data Types

```python
arr = np.array([1, 2, 3], dtype=float)
```

Common types:

* `int`
* `float`
* `bool`

Why it matters: ML math **breaks** with wrong dtypes.

---

## 2️. Type Conversion

```python
arr = np.array([1, 2, 3])
arr = arr.astype(float)
```

---

## 3️. Reshaping Arrays (VERY IMPORTANT)

```python
arr = np.array([1, 2, 3, 4, 5, 6])

arr.reshape(2, 3)
```

Used in:

* datasets
* neural network inputs

---

## 4️. Flattening

```python
matrix = np.array([[1, 2], [3, 4]])

matrix.flatten()
```

---

## 5️. Array Copy vs View (Critical Concept)

```python
a = np.array([1, 2, 3])
b = a.copy()

b[0] = 100
```

`copy()` → independent
without copy → linked (danger in ML)

---

## 6️. Boolean Indexing

```python
arr = np.array([10, 20, 30, 40])

arr[arr > 20]
```

Used for:

* data filtering
* cleaning datasets

---

## 7️. Random Arrays

```python
np.random.rand(5)
np.random.randint(1, 10, size=5)
```

Used in:

* weight initialization
* simulations

---

## 8️. Basic Statistics

```python
arr = np.array([1, 2, 3, 4])

arr.mean()
arr.max()
arr.min()
arr.sum()
```

---

## 9️. Broadcasting (ML Magic)

```python
arr = np.array([1, 2, 3])

arr + np.array([10])
```

No loops. Fast. Clean.

---

## What You Should NOT Learn Yet 

* Pandas
* SciPy
* TensorFlow
* PyTorch

---


## to explore more features of numpy, go to my numpy.py file




### **Day 7 – Conditional Logic for AI/ML**


## What You Learn (Day 7)

### 1️. Conditional Statements (Core)

```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

Used for:

* decision making
* data filtering
* rule-based logic

---

### 2️. Conditions with NumPy Arrays

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
arr[arr > 25]
```

This is **real ML-style filtering**.

---

### 3️. Boolean Masks

```python
mask = arr % 2 == 0
arr[mask]
```

Used in:

* cleaning data
* removing outliers

---

### 4️. `np.where()` (Very Important)

```python
np.where(arr > 25, 1, 0)
```

Used in:

* labeling data
* feature engineering

---

---

### Why Day 7 Matters

* ML models learn from **conditions**
* Labels = conditional logic
* Data preprocessing starts here

---

### Next (Day 8)

 **Functions + NumPy (ML pipelines)**
