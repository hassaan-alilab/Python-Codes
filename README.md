# Python-Codes
# Python Shape Printer

A collection of Python functions designed to print geometric shapes using asterisks (`*`) in the terminal. This project demonstrates basic loops, string manipulation, and time complexity optimizations—moving from nested loops \(O(n^2)\) to optimized single-loop \(O(n)\) solutions.

## 🚀 Features

* **Triangles:** Right-angled, left-angled, and inverted variations.
* **Squares:** Standard block patterns.
* **Pyramids:** Optimized math-driven pyramids handling both odd and even dimensions.
* **Code Optimizations:** Alternative methods showcasing how to replace inner loops with Python's string multiplication to drastically reduce execution steps.

---

## 🛠️ Functions Overview

### 1. Right-Angled Triangles
* **`rtriangle(length)`**: Prints a right-angled triangle using nested loops.
* **`altrnoftriangle(le)`**: An alternative approach that uses string multiplication (`*` * `i`) for cleaner code.

### 2. Squares
* **`square(len)`**: Prints a solid square block of size `len` x `len`.

### 3. Inverted Triangles
* **`invtriangle(leng)`**: Prints an upside-down right-angled triangle using a reverse loop step (`-1`).

### 4. Left-Angled Triangles
* **`ltriangle(len)`**: Traditional nested loop implementation to handle leading spaces and stars.
* **`altltriangle(len)`**: **Optimized \(O(n)\) version** that calculates spacing and stars mathematically on a single line.

### 5. Pyramids
* **`pyramid(length)`**: Prints a standard centered pyramid (optimized for odd numbers).
* **`gpyramid(len)`**: A generic, robust version that handles **both odd and even** lengths perfectly using dynamic spacing adjustments in \(O(n)\) time complexity.

---

## 📦 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the directory:
   ```bash
   cd YOUR_REPO_NAME
   ```
3. Run the script:
   ```bash
   python shapes.py
   ```

---

## 📈 Optimization Spotlight

Instead of using nested loops which result in \(O(n^2)\) time complexity, the alternative methods in this repository utilize Python's native string replication:

```python
# Traditional O(n^2) nested loop approach
for i in range(1, len + 1):
    for k in range(len - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Optimized O(n) string math approach
for i in range(1, len + 1):
    space = " " * (len - i)
    stars = "*" * i
    print(space + stars)
```
