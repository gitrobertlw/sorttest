# 📦 Package Sorting System

This module classifies packages into different handling stacks based on their **size** and **weight**.

## 🚦 Sorting Rules

A package is evaluated using the following criteria:

### 📏 Bulky Package

A package is considered **bulky** if:

- Its **volume ≥ 1,000,000 cm³**, OR
- Any dimension (**width, height, length ≥ 150 cm**)

### ⚖️ Heavy Package

A package is considered **heavy** if:

- Its **mass ≥ 20 kg**

---

## 📚 Dispatch Categories

| Category | Condition               |
| -------- | ----------------------- |
| STANDARD | Not bulky AND not heavy |
| SPECIAL  | Bulky OR heavy          |
| REJECTED | Both bulky AND heavy    |

---

## 🧠 Implementation

```python
def sort(width, height, length, mass):
    volume = width * height * length

    bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
```
