Automated Data Cleaning Tool
This project is a Flask-based web application that allows users to upload CSV files and automatically cleans the data by replacing missing or empty values in numeric columns with their respective mean values. The cleaned data is then saved as a new CSV file, and the filename along with the cleaning timestamp is stored in a database.

Features:
✅ Upload CSV files via a simple web interface
✅ Automatically replace missing or empty numeric values with their mean
✅ Save the cleaned file in a dedicated directory
✅ Store the filename and timestamp in a database for tracking
✅ Lightweight and easy to use

Tech Stack:
Backend: Flask (Python)
Frontend: HTML, CSS
Database: SQLite/MySQL (for storing cleaned file logs)
Libraries Used: Pandas, Flask, SQLAlchemy
How It Works:
Upload a CSV file from the web interface.
The application cleans the data (fills missing numeric values with mean).
The cleaned file is saved in the cleaned_files directory.
The filename and timestamp are stored in the database for reference.
A response is returned with the cleaned file details.
Setup & Installation:
Clone this repository:
sh
Copy
Edit
git clone https://github.com/yourusername/automated-data-cleaning-tool.git  
cd automated-data-cleaning-tool
Install dependencies:
sh
Copy
Edit
pip install -r requirements.txt
Run the Flask app:
sh
Copy
Edit
python app.py
Open http://127.0.0.1:5000/ in your browser and start cleaning your data!
Credits
This project was developed using ChatGPT for guidance, optimization, and debugging. Special thanks to AI for making development smoother and faster! 🚀
