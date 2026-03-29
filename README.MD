# Fitness Tracker

A comprehensive, full-stack fitness tracking web application built with Flask. This platform allows users to monitor their health metrics, predict fitness trends using machine learning, and interact with a local AI fitness assistant.

## Features

* **User Authentication:** Secure login and account creation system.
* **Personalized Dashboard:** Track and view your health and fitness details.
* **BMI Calculator:** Quick and easy Body Mass Index calculation.
* **Predictive Analytics:** Uses XGBoost and Pandas to provide data-driven fitness predictions.
* **AI Fitness Bot:** Integrated chatbot powered by Ollama to answer fitness-related queries.
* **Email Reminders:** Automated workout and fitness reminders.
* **Flexible Database:** Automatically switches between SQLite for production environments (Render/PythonAnywhere) and MySQL for local development.

## Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLAlchemy (MySQL via PyMySQL locally, SQLite in production)
* **Machine Learning & Data:** Pandas, XGBoost
* **AI Integration:** Ollama
* **Environment Management:** python-dotenv

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Naseer-fez/fitness_tracker.git
   cd fitness_tracker
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add the following variables:
   ```env
   SECRET_KEY=your_secret_key_here
   Mysql_DB=your_mysql_password
   ```

5. **Initialize the Database and Run the Application:**
   The database tables will be created automatically on the first run.
   ```bash
   python app.py
   ```

The application will be accessible at http://127.0.0.1:5000/.

## Project Structure

- `app.py`: Main application entry point and blueprint registration.
- `routes/`: Contains modular routing blueprints (Login, CreateAccount, Dashboard, BMI, Prediction, FitnessBot, etc.).
- `models/`: Database schema definitions using SQLAlchemy.
- `requirements.txt`: Project dependencies.
