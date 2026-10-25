# Breast Cancer Classification with Logistic Regression

**Date:** October 24, 2026

## Introduction

This is an **educational project** designed to deepen my understanding of machine learning fundamentals.

**Note:** The code may not be fully optimized or may contain verbose sections. This is intentional, as the focus is on clarity and learning rather than production efficiency.

### Why This Project?

I learned that Logistic Regression is the simplest form of a Neural Network. Motivated by this insight, I decided to implement Logistic Regression from scratch using NumPy to:

1. **Understand the fundamentals:** Explore the mathematical mechanics and algorithms behind Logistic Regression
2. **Build a foundation:** Prepare myself before diving into deeper Neural Network architectures
3. **Compare implementations:** Answer the question—*Does my custom implementation produce the same results as scikit-learn?* Are the accuracy and performance metrics identical?

### Project Approach

I built two implementations:
- **From Scratch (NumPy):** A custom implementation using only NumPy, understanding every step from gradient descent to loss computation
- **Using Sklearn:** The industry-standard implementation for benchmarking and comparison

This side-by-side comparison reveals how different optimization strategies and hyperparameter choices affect model performance.


## Project Overview

This project implements Logistic Regression from scratch to understand the mathematical foundations of machine learning before diving into Neural Networks. It compares a custom NumPy implementation with scikit-learn's production-ready version.

---

## Problem Statements

1. **How does Logistic Regression work mathematically?**
   - Understand gradient descent, loss functions, and optimization
   
2. **Can a from-scratch implementation match sklearn's performance?**
   - Compare accuracy, precision, recall, confusion matrix
   
3. **What are the trade-offs between custom and library implementations?**
   - Code clarity vs optimization
   - Flexibility vs robustness

---

## Main Features

- **Custom Implementation (NumPy)**
  - Sigmoid activation function
  - Binary cross-entropy loss
  - Gradient descent optimization
  - Custom predict & predict_proba methods

- **Sklearn Implementation**
  - Built-in regularization (L2)
  - Advanced solvers (liblinear, lbfgs)
  - GridSearchCV for hyperparameter tuning

- **Comprehensive Comparison**
  - Side-by-side accuracy comparison
  - Confusion matrices & classification reports
  - Loss curve visualization
  - Performance analysis

---

## System Architecture
```
breast-cancer-classification-lr/
│
├── models/
│ ├── from_sklearn.ipynb
│ └── from_scratch.ipynb 
│
├── notebooks/
│ └── comparison.ipynb 
│
├── result/ 
│
├── README.md 
├── AI_Usage.md 
├── requirements.txt 
└── .gitignore 

```
## Dataset

**Breast Cancer Wisconsin (Diagnostic) Dataset**

### Overview
- **Samples:** 569
- **Features:** 30
- **Task:** Binary Classification

### Target Classes
- **0: Malignant** - cancer
- **1: Benign** - non-cancerous

### Key Features

The 30 features represent measurements of cell nuclei characteristics:

- **Radius:** Distance from center to points on the perimeter
- **Texture:** Standard deviation of gray-scale values
- **Perimeter:** Perimeter of the cell nucleus
- **Area:** Area of the cell nucleus
- **Smoothness:** Local variation in radius lengths
- **Compactness:** (Perimeter² / Area) - 1.0
- **Concavity:** Severity of concave portions of contour
- **Concave Points:** Number of concave portions of contour
- **Symmetry:** Symmetry of the cell nucleus
- **Fractal Dimension:** "Coastline approximation" - 1

Each characteristic is measured 3 times (mean, standard error, worst), resulting in 30 total features.

### Class Distribution
- Malignant: 212 samples (37%)
- Benign: 357 samples (63%)
---

## Results

| Implementation | Accuracy | Recall (Malignant) | Precision (Malignant) | Recall (Benign) | Precision (Benign) |
|:---|:---|:---|:---|:---|:---
| Sklearn | 98.25% | 0.98 | 0.98 | 0.99 | 0.99 |
| From Scratch | 97.37% | 0.98 | 0.95 | 0.97 | 0.99 |
For detailed analysis, see [comparison.ipynb](notebooks/comparison.ipynb)
---

## Author
Nguyen Thi Van Anh

## License
MIT
