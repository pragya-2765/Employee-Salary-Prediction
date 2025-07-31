import streamlit as st
import pandas as pd
import joblib

# Inject CSS
st.markdown("""
    <style>
        header[data-testid="stHeader"] {
         background-color: transparent;
        }
        .stApp {
            background-color: #FFEDD7;
            color: #333;
            font-family: 'Arial', sans-serif;
        }

        h1, h2, h3 {
            color: #003366;
        }

        .stButton>button {
            background-color: #4caf58;
            color: white;
            font-weight: bold;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }

        .stSidebar {
            background-color: #aee4e8;
        }
    </style>
""", unsafe_allow_html=True)

#Load the trained model
model = joblib.load('best_model.pkl')

# Define education to education-num mapping
education_map = {
    'Preschool': 1, '1st-4th': 2, '5th-6th': 3, '7th-8th': 4, '9th': 5, '10th': 6,
    '11th': 7, '12th': 8, 'HS-grad': 9, 'Some-college': 10, 'Assoc-acdm': 11, 'Assoc-voc': 12,
    'Bachelors': 13, 'Masters': 14, 'Doctorate': 15, 'Prof-school': 16
}

# Label maps (used for encoding)
workclass_map = {
    'Private': 3, 'Self-emp-not-inc': 5, 'Self-emp-inc': 4,
    'Federal-gov': 1, 'Local-gov': 2, 'State-gov': 6,
    'Without-pay': 0, 'Never-worked': 7, 'NotListed': 8
}
occupation_map = {
    'Machine-op-inspct': 6, 'Protective-serv': 10, 'Farming-fishing': 2,
    'Other-service': 8, 'Craft-repair': 1, 'Adm-clerical': 0,
    'Exec-managerial': 4, 'Prof-specialty': 9, 'Priv-house-serv': 7,
    'Handlers-cleaners': 3, 'Sales': 11, 'Transport-moving': 12,
    'Tech-support': 13, 'Armed-Forces': 14, 'Others': 5
}


st.set_page_config(page_title="Employee Salary Classification", page_icon="💼", layout="centered")

st.title("💼 Employee Salary Classification App")
st.markdown("Predict whether an employeee earn > 50K or <=50K based on input features.")

#Sidebar inputs
st.sidebar.header("Input Employee Details")
workclass = st.sidebar.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])
age = st.sidebar.slider("Age", 18, 65, 30)
education = st.sidebar.selectbox("Education Level", ["Bachelors", "Masters", "PhD", "HS-grad", "Assoc", "Some-college"])
educational_num = education_map.get(education, 13)  # Defaulting to Bachelors if not found
occupation = st.sidebar.selectbox("Job Role", ["Machine-op-inspct", "Protective-serv", "Farming-fishing", "Other-service", "Craft-repair", "Adm-clerical", "Exec-managerial", "Prof-specialty", "Priv-house-serv", "Handlers-cleaners", "Sales", "Transport-moving", "Tech-support", "Armed-Forces"])

hours_per_week = st.sidebar.slider("Hours Worked per Week", 1, 80, 40)
experience = st.sidebar.slider("Years of Experience", 0, 40, 5)

# Encode string values into the same format used in training
workclass_encoded = workclass_map.get(workclass, 8)
occupation_encoded = occupation_map.get(occupation, 5)
#Build input DataFrames
input_df = pd.DataFrame({
    'workclass': [workclass_encoded],
    'age': [age],
    'educational-num': [educational_num],
    'occupation': [occupation_encoded],
    'hours-per-week': [hours_per_week],
    'experience': [experience]
})

st.write("### Input Data")  #Display the data that we have given as input
st.write(input_df)

#Predict button
if st.button("Predict Salary Class"):
  prediction = model.predict(input_df)
  st.success(f"Prediction: {prediction[0]}")

#Batch prediction
st.markdown("---")
st.markdown("#### Batch Prediction")
uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type=["csv"])

if uploaded_file is not None:
  batch_df = pd.read_csv(uploaded_file)
  batch_df['educational-num'] = batch_df['education'].map(education_map)
  batch_df['experience'] = batch_df['age'] - 18
  batch_df['experience'] = batch_df['experience'].apply(lambda x: max(x, 0))
  batch_df['workclass'] = batch_df['workclass'].map(workclass_map)
  batch_df['occupation'] = batch_df['occupation'].map(occupation_map)
  input_batch = batch_df[['workclass', 'age', 'educational-num', 'occupation', 'hours-per-week', 'experience']]
  input_batch.fillna(-1, inplace=True)
  st.write("Processed batch data preview:", input_batch.head())
  batch_preds = model.predict(input_batch)
  batch_df['PredictedClass'] = batch_preds

  st.write("Predictions:")
  st.write(batch_df[['PredictedClass']].head())
  csv = batch_df.to_csv(index=False).encode('utf-8')
  st.download_button("Download Prediction CSV", csv, file_name='predicted_classes.csv', mime='text/csv')

