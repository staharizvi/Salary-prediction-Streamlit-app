import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

st.title("Salary Prediction")
st.write('## Welcome to Salary predictor')
st.write('**Note:** This salary predictor is trained on a specific dataset and requires you to provide input in order to predict your salary.')

# Load the encoder and model
encoder_path = 'encoder.pkl'
model_path = 'model.pkl'

with open(encoder_path, 'rb') as f:
    encoder = pickle.load(f)
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Define a sample data path for demonstration purposes
path = 'Salary Prediction of Data Professions.csv'
df = pd.read_csv(path)
df['DOJ'] = pd.to_datetime(df['DOJ'])
df['CURRENT DATE'] = pd.to_datetime(df['CURRENT DATE'])
st.dataframe(df.head())

st.write('### Predict your expected salary at our company')
st.write('Enter the required info below & get your prediction')
col1, col2, col3 = st.columns(3)
with col1:
    sex = st.selectbox('Gender', ['M', 'F'])
    designation = st.selectbox('Designation', ['Analyst', 'Senior Analyst', 'Senior Manager', 'Director', 'Associate', 'Manager'])
    rating = st.number_input('Rating', min_value=0, max_value=5, step=1)

with col2:
    age = st.number_input('Age', min_value=18, max_value=120, step=1)
    unit = st.selectbox('Unit', ['Marketing', 'Management', 'IT', 'Operations', 'Web', 'Finance'])
    leaveUsed = st.number_input('Leaves Used', min_value=0, max_value=30, step=1)

with col3:
    pastexp = st.number_input('Past Exp', min_value=0, max_value=30, step=1)
    service = st.number_input('Service (DAYS)', min_value=0, max_value=2500, step=1)

leaveRemain = 30 - leaveUsed

# Create a DataFrame for input data
input_data = pd.DataFrame({
    'SEX': [sex],
    'DESIGNATION': [designation],
    'UNIT': [unit],
    'AGE': [age],
    'LEAVES USED': [leaveUsed],
    'LEAVES REMAINING': [leaveRemain],
    'RATINGS': [rating],
    'PAST EXP': [pastexp],
    'SERVICE': [service]
})

# Encode categorical data
categorical_cols = ['SEX', 'DESIGNATION', 'UNIT']
input_encoded = encoder.transform(input_data[categorical_cols])
input_encoded_df = pd.DataFrame(input_encoded, columns=encoder.get_feature_names_out(categorical_cols))

# Concatenate encoded columns with the rest of the input data
input_final = pd.concat([input_data.drop(columns=categorical_cols), input_encoded_df], axis=1)

# Ensure the input data columns match the training data
input_final = input_final.reindex(columns=encoder.get_feature_names_out(categorical_cols).tolist() + ['AGE', 'LEAVES USED', 'LEAVES REMAINING', 'RATINGS', 'PAST EXP', 'SERVICE'], fill_value=0)

if st.button('Predict'):
    try:
        prediction = model.predict(input_final)
        st.success(f'**Predicted Salary: {prediction[0]}**')
    except Exception as e:
        st.error(f"An error occurred: {e}")
