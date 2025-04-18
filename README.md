# 📘 VTU SGPA Calculator

This is a simple command-line Python project that calculates **SGPA (Semester Grade Point Average)** for students following the **VTU (Visvesvaraya Technological University)** examination pattern.

---

## 📋 Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Limitations](#limitations)
- [License](#license)

---

## 🔍 Overview
The SGPA Calculator takes subject marks and credit points as input and calculates the SGPA using the formula:

```
SGPA = (sum of (marks × credit)) / (sum of credits)
```

It includes basic input validation and handles scaling for SGPA values if the result is higher than typical bounds.

---

## ⚙️ How It Works
- Prompts user for name and number of subjects.
- Accepts marks and credits for each subject.
- Validates if marks entered are within the 0–100 range.
- Computes the total weighted result and total credit points.
- Calculates SGPA and adjusts scale based on output value.

---

## ▶️ Usage
Run the script in any Python environment:

```bash
python sgpa_calculator.py
```

### 👇 Input Required:
- Student name
- Number of subjects
- Marks (for each subject)
- Credit points (for each subject)

---

## 💡 Sample Output
```
Enter the name : Swapnil
Enter the number of subject you have: 3
Enter the mark of sub 1 marks: 80
Enter the mark of sub 2 marks: 70
Enter the mark of sub 3 marks: 90
Enter the credits point of sub 1 marks: 4
Enter the credits point of sub 2 marks: 3
Enter the credits point of sub 3 marks: 3
[320, 210, 270]
10
800
8.0
```

---

## ⚠️ Limitations
- Only supports numerical entry; no exception handling for string inputs.
- No GUI or web version.
- Only works for up to 100 marks per subject.

---

## 📝 License
This project is licensed under the **MIT License**.



