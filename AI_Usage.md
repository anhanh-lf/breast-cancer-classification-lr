# AI Usage Documentation

## Tools Used

- **Claude AI** (by Anthropic):
  - **Technical Aspects:**
    - Code framework generation and structure recommendations
    - Algorithmic and mathematical explanation
    - Gradient descent and loss function guidance
    - Debugging and code review
  
  - **Language & Documentation:**
    - Vietnamese to English translation
    - Grammar and phrasing correction
    - Documentation refinement for README.md and AI_Usage.md

- **GitHub Copilot Student:** Terminology explanation and code suggestions

## Main Purposes

- **Algorithm & Mathematics:** Explain the underlying principles, mathematical foundations of Logistic Regression, loss functions, fit mechanisms, and related formulas
- **Framework & Structure:** Provide guidance on class structure, function signatures, and performance analysis diagrams for comparing custom vs sklearn implementations
- **Result Interpretation:** Guide analysis of model outputs, metrics, and visualization
- **Code Review:** Review implementations, identify bugs, and suggest improvements

## How AI Was Used

- **Algorithm Implementation:** Claude provided guidance on implementing LogisticRegressionScratch class with sigmoid, binary cross-entropy loss, and fit functions
- **Result Analysis:** Used Claude to interpret classification metrics, confusion matrices, and performance comparisons
- **Framework Design:** AI suggested project structure and file organization
- **Mathematical Guidance:** Explained gradient descent formulas and regularization concepts

## Student Contribution

- **Algorithm Understanding:** Self-studied and comprehended how Logistic Regression makes predictions through gradient descent and sigmoid transformation
  
- **Code Implementation:** 
  - Independently implemented data loading and preprocessing
  - Wrote sigmoid, loss, fit, predict, and predict_proba functions from scratch
  - Performed hyperparameter tuning with GridSearchCV
  - Tested and validated both implementations

- **Testing & Analysis:** 
  - Ran both implementations on the same dataset
  - Generated confusion matrices and classification reports
  - Compared results between sklearn and custom version
  - Analyzed performance differences

- **Documentation:** 
  - Wrote README.md with problem statements and results
  - Created this AI_Usage.md to document AI assistance
  - Wrote comparison analysis in notebooks

## Code Components with AI Assistance

| Component | AI Role | Student Role |
|---|---|---|
| Sigmoid function | Explained formula and purpose | Implemented with eps handling for numerical stability |
| BCE loss | Explained binary cross-entropy formula | Implemented with eps to avoid log(0) |
| Gradient descent | Guided mathematical derivation | Full implementation in fit function |
| Fit function | Explained algorithm steps | Wrote complete training loop with weight updates |
| GridSearchCV | Explained how it works | Applied to sklearn model for tuning |
| Result interpretation | Guided what metrics mean | Analyzed and compared outputs |

## Learning Outcomes

1. **Algorithm Mastery:** Understand how Logistic Regression works mathematically—from sigmoid activation to gradient descent to convergence
2. **Practical Implementation:** Recognize the difference between understanding an algorithm and implementing it correctly
3. **Model Evaluation:** Interpret Precision, Recall, F1-score, and Confusion Matrix in the context of medical diagnosis
4. **Comparison Skills:** Analyze trade-offs between custom implementations (flexibility, clarity) vs library implementations (optimization, robustness)
5. **AI as a Tool:** Use AI effectively for learning and problem-solving while maintaining critical thinking

---

**Note:** This project demonstrates the use of AI as a **learning accelerator**, not a replacement for understanding. All code has been carefully reviewed, tested, and manually validated to ensure genuine comprehension of the underlying concepts.