from flask import Flask, render_template, request, jsonify
import pandas as pd
from datetime import datetime
from db_connection import log_cleaned_file
import os

app = Flask(__name__)

# Ensure cleaned_files directory exists
CLEANED_FILES_DIR = "./cleaned_files"
os.makedirs(CLEANED_FILES_DIR, exist_ok=True)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(file)

        # Perform cleaning: Replace null or empty values in numeric columns with their mean
        numeric_columns = df.select_dtypes(include=['number']).columns
        for column in numeric_columns:
            if df[column].isnull().any() or (df[column] == '').any():  # Check for nulls or empty strings
                mean_value = df[column].mean()
                df[column] = df[column].fillna(mean_value)
                df[column] = df[column].replace('', mean_value)

        # Save cleaned data to a new CSV file
        cleaned_file_name = f"cleaned_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        cleaned_file_path = os.path.join(CLEANED_FILES_DIR, cleaned_file_name)
        df.to_csv(cleaned_file_path, index=False)

        # Log the cleaned file details in the database
        log_cleaned_file(cleaned_file_name)

        return jsonify({"message": "File cleaned and saved", "cleaned_file": cleaned_file_name}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
