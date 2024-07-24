# Salary Prediction App

This repository contains a Streamlit application for predicting salaries based on various features. The model is built using a RandomForestRegressor from scikit-learn.

## Table of Contents

- Installation
- Usage
- Model Training
- File Descriptions
- Contributing
- License

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/taharizvi-ai/Salary-prediction-Streamlit-app.git
    cd salary-prediction-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Upload your CSV file containing the data.

3. The app will display the predicted salaries based on the input data.

## Model Training

The model is trained using the following steps:

1. **Data Reading and Cleaning**:
    - Read the CSV file and drop unnecessary columns.
    - Handle missing values.

2. **Feature Engineering**:
    - Convert date columns to datetime.
    - Calculate the service duration.

3. **Encoding**:
    - One-hot encode categorical features.

4. **Model Training**:
    - Train a RandomForestRegressor model.

5. **Saving the Model**:
    - Save the trained model and encoder using `pickle`.

## File Descriptions

- `app.py`: The main Streamlit app file.
- `model.py`: Contains functions for data processing and model training.
- `requirements.txt`: List of required packages.
- `Salary Prediction of Data Professions.csv`: Sample dataset (if applicable).
- `model.pkl`: Trained model file.
- `encoder.pkl`: Trained encoder file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


![Alt text](https://github.com/taharizvi-ai/Salary-predition-Streamlit-app/blob/main/spapp.PNG)
