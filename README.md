College Predictor
This project is a College Prediction Model designed to help students find the best-matching colleges based on their entrance exam rank and other criteria. It provides a web interface where users can input their details and receive personalized college recommendations.

Project Overview
The College Predictor leverages a dataset of college opening and closing ranks along with details such as category, state, quota, and gender requirements. By applying custom filters, the model returns the best possible college options for a given student's criteria.

Features
Data Collection & Cleaning:
Initial dataset was collected from various sources and cleaned to ensure accuracy.
Data was merged and filtered, focusing on non-IIT colleges for this model.
Custom Prediction Model:
Filters colleges based on rank, category, state, gender, and home state.
Returns a list of college options that meet the criteria specified by the user.
Web Interface:
Built using Flask and HTML, allowing users to enter their information through a form and receive results in real time.
Simple, intuitive UI for ease of use.
Tech Stack
Backend: Python, Flask
Frontend: HTML
Data Processing: Pandas
