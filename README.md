# 🩺 MediFuture AI

### Predict Today, Prevent Tomorrow

MediFuture AI is an AI-powered healthcare project designed to predict multiple diseases using Machine Learning and eventually analyze a patient's current health information to estimate potential future health risks.

The project combines multiple disease prediction models with a planned risk prediction engine, health score system, and AI assistant.

> ⚠️ **Disclaimer:** MediFuture AI is an educational and experimental project. Its predictions are not medical diagnoses and should not replace professional medical advice.

---

## 🎯 Project Goal

Most disease prediction systems focus on predicting a single disease.

MediFuture AI aims to go further by building a system that can:

- Predict multiple diseases
- Analyze health risk factors
- Estimate potential future disease risks
- Generate an overall health score
- Provide AI-assisted health information
- Present results through a unified application

---

## 🧠 Disease Prediction Modules

The project currently contains Machine Learning models for:

| Disease | Status |
|---|---|
| Diabetes | ✅ Completed |
| Heart Disease | ✅ Completed |
| Chronic Kidney Disease | ✅ Completed |
| Liver Disease | ✅ Completed |
| Stroke | ✅ Completed |
| Hypertension | ✅ Completed |

Each module includes:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Train/test splitting
- Model training
- Model evaluation
- Best-model selection
- Model serialization
- User prediction

---

## 🤖 Machine Learning Models

Multiple classification algorithms are trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

Models are evaluated using metrics such as:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

For imbalanced datasets such as Stroke Prediction, metrics such as recall and F1-score are particularly important.

---

## 🔄 ML Pipeline

Newer disease modules use Scikit-learn pipelines to combine preprocessing and prediction.

```text
Raw Patient Data
        ↓
Missing Value Handling
        ↓
Numerical Scaling
        ↓
Categorical Encoding
        ↓
Machine Learning Model
        ↓
Disease Prediction
```

This ensures that the same preprocessing learned during training is automatically applied during prediction.

---

## 📂 Project Structure

```text
MediFuture-AI/
│
├── Datasets/
│   ├── Diabetes/
│   ├── Heart-Disease/
│   ├── Kidney-Disease/
│   ├── Liver-Disease/
│   ├── Stroke/
│   └── Hypertension/
│
├── Machine-Learning/
│   ├── Diabetes/
│   ├── Heart-Disease/
│   ├── Kidney-Disease/
│   ├── Liver-Disease/
│   ├── Stroke/
│   └── Hypertension/
│
├── Models/
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   ├── kidney_model.pkl
│   ├── liver_model.pkl
│   ├── stroke_model.pkl
│   └── hypertension_model.pkl
│
├── README.md
└── requirements.txt
```

The exact structure may evolve as backend, frontend, and AI components are integrated.

---

## ⚙️ Typical Disease Module Structure

```text
Disease/
│
├── EDA.py
├── preprocessing.py
├── train.py
├── evaluate.py
├── save_model.py
└── predict.py
```

### `EDA.py`

Explores the dataset, including:

- Dataset dimensions
- Features
- Data types
- Missing values
- Target distribution
- Statistical information

### `preprocessing.py`

Handles operations such as:

- Data cleaning
- Missing-value imputation
- Feature scaling
- Categorical encoding
- Target preparation
- Train/test splitting

### `train.py`

Trains multiple Machine Learning classifiers.

### `evaluate.py`

Evaluates the models and selects a suitable model based on performance metrics.

### `save_model.py`

Serializes the selected trained model/pipeline using Joblib.

### `predict.py`

Loads the saved model and performs prediction on new patient input.

---

## 🏗️ Planned Architecture

```text
                    MediFuture AI
                          │
                Patient Health Data
                          │
                          ▼
                Disease Prediction
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
     Diabetes          Heart            Kidney
        │              Disease           Disease
        │                 │                 │
        ├─────────────────┼─────────────────┤
        ▼                 ▼                 ▼
      Liver            Stroke         Hypertension
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                 Risk Prediction Engine
                          │
                          ▼
                     Health Score
                          │
                          ▼
                    AI Assistant
                          │
                          ▼
             Personalized Health Insights
```

---

## 🚧 Upcoming Features

The project is actively under development.

Planned work includes:

- Risk Prediction Engine
- Health Score System
- Disease probability/risk analysis
- AI-powered health assistant
- Backend API integration
- Frontend dashboard
- Unified patient input system
- Model optimization
- Cross-validation and hyperparameter tuning
- Improved model evaluation
- Prediction explanations
- Final system testing

---

## 🛠️ Technologies

### Programming

- Python

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

### ML Techniques

- Classification
- Feature preprocessing
- Standardization
- One-hot encoding
- Missing-value imputation
- ML pipelines
- Model evaluation

### Planned Application Stack

- FastAPI
- AI/LLM integration
- Web frontend
- REST APIs

---

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd MediFuture-AI
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate it

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run a prediction module

For example:

```bash
python3 Machine-Learning/Stroke/predict.py
```

---

## 📊 Current Progress

```text
Disease Prediction Models     ████████████████████  Completed
Risk Prediction Engine        ░░░░░░░░░░░░░░░░░░░░  Planned
Health Score                  ░░░░░░░░░░░░░░░░░░░░  Planned
Backend Integration           ░░░░░░░░░░░░░░░░░░░░  Planned
Frontend                      ░░░░░░░░░░░░░░░░░░░░  Planned
AI Assistant                  ░░░░░░░░░░░░░░░░░░░░  Planned
```

**Estimated overall project completion: ~60–65%**

---

## 🔮 Vision

The long-term goal of MediFuture AI is not simply:

> "Does this patient have a disease?"

Instead, the project aims to explore:

> "Based on available health information and model outputs, what health risks may require attention in the future?"

The final system is intended to combine disease prediction, risk analysis, health scoring, and AI-generated explanations into one platform.

---

## ⚠️ Medical Disclaimer

MediFuture AI is built for educational, research, and software-development purposes.

The datasets and Machine Learning models used in this project are not sufficient for clinical diagnosis. Predictions may be inaccurate and should not be used to make medical decisions.

Always consult qualified healthcare professionals for medical advice, diagnosis, and treatment.

---

## 👨‍💻 Author

**Arijeet Dhaka**

B.Tech Computer Science & Engineering  
Artificial Intelligence & Machine Learning

---

## ⭐ Support

If you find MediFuture AI interesting, consider giving the repository a ⭐ on GitHub.