import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/student_score_model.pkl")

# Example input (change values as you want)
data = {
    "Hours_Studied": [5],
    "Attendance": [80],
    "Parental_Involvement": ["Medium"],
    "Access_to_Resources": ["High"],
    "Extracurricular_Activities": ["Yes"],
    "Sleep_Hours": [7],
    "Previous_Scores": [70],
    "Motivation_Level": ["High"],
    "Internet_Access": ["Yes"],
    "Tutoring_Sessions": [2],
    "Family_Income": ["Medium"],
    "Teacher_Quality": ["High"],
    "School_Type": ["Public"],
    "Peer_Influence": ["Positive"],
    "Physical_Activity": [3],
    "Learning_Disabilities": ["No"],
    "Parental_Education_Level": ["Graduate"],
    "Distance_from_Home": ["Near"],
    "Gender": ["Male"]
}

df = pd.DataFrame(data)

# Same encoding as training
df = pd.get_dummies(df)

# Align columns with training
model_features = model.feature_names_in_
df = df.reindex(columns=model_features, fill_value=0)

# Prediction
prediction = model.predict(df)

print("Predicted Exam Score:", round(prediction[0], 2))
