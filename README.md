# 🎓 Student Score Prediction using Machine Learning

A Machine Learning project that predicts a student's exam score based on study habits, academic background, and lifestyle factors.

This project demonstrates the complete ML workflow:
- Data preprocessing
- Model training
- Model evaluation
- Model saving
- GitHub project structuring

---

## 🚀 Project Overview

This system predicts the **Exam Score** of a student using multiple real-world factors such as:

- Study hours
- Attendance
- Sleep duration
- Previous academic performance
- Motivation level
- Internet access
- Family income
- Teacher quality
- And more...

The model learns patterns from historical student data and estimates expected performance.

---

## 🧠 Machine Learning Details

- **Model Used:** Random Forest Regressor  
- **Problem Type:** Regression  
- **Dataset Size:** 6607 rows × 20 columns  
- **Model Accuracy (R² Score):** ~0.76  

---

## 📁 Project Structure

```
Student-Score-Prediction/
│
├── data/
│   └── StudentPerformanceFactors.csv
│
├── model/
│   └── student_score_model.pkl
│
├── student_score.ipynb
├── README.md
```

---

## 📊 Dataset Information

The dataset contains multiple features that influence student performance:

### Input Features:
- Hours_Studied  
- Attendance  
- Parental_Involvement  
- Access_to_Resources  
- Extracurricular_Activities  
- Sleep_Hours  
- Previous_Scores  
- Motivation_Level  
- Internet_Access  
- Tutoring_Sessions  
- Family_Income  
- Teacher_Quality  
- School_Type  
- Peer_Influence  
- Physical_Activity  
- Learning_Disabilities  
- Parental_Education_Level  
- Distance_from_Home  
- Gender  

### Target Variable:
`Exam_Score`

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Jupyter Notebook  

---

## 📈 Model Performance

The trained model was evaluated on test data and achieved:

**R² Score: ~0.76**

This indicates the model can reasonably predict student exam scores based on multiple influencing factors.

---

## 💾 Model Saving

The trained model is saved as:

```
model/student_score_model.pkl
```

This allows reuse without retraining.

---

## ▶️ How to Run This Project

### 1️⃣ Install required libraries
```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

### 2️⃣ Open Jupyter Notebook
```bash
jupyter notebook
```

### 3️⃣ Run:
```
student_score.ipynb
```

---

## 🔮 Future Improvements

- Add Streamlit web interface
- Deploy model online
- Create real-time prediction system
- Improve model accuracy with feature engineering

---

## 👨‍💻 Author

**Mr-Yantrik**

