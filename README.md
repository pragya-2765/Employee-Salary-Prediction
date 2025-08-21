# 💼 Employee Salary Prediction

This is a machine learning project that predicts whether an employee earns **more than 50K** or **less than or equal to 50K** annually based on features like age, education, occupation, and hours worked per week. The project includes a web-based interface using Streamlit and is deployable directly from Google Colab.

---

## 🚀 Features
- Predict salary class: **<=50K** or **>50K**
- Supports both individual and batch predictions
- Interactive UI using **Streamlit**
- Model trained using algorithms like Logistic Regression, Random Forest, SVM, and Gradient Boosting

---

## 📁 Project Structure
├── salary.py # Streamlit app code
├── best_model.pkl # Trained ML model
├── requirements.txt # Required Python libraries
├── README.md # Project overview and instructions

---

## 🛠 How to Run the App

### Option 1: Run via Google Colab
1. Upload all files (`salary.py`, `best_model.pkl`, etc.) to Colab
2. Install dependencies:
   !pip install streamlit joblib pandas scikit-learn matplotlib
3. Run the app using:   
   !streamlit run salary.py
### Option 2: Run Locally
1. Clone the repository:
   git clone https://github.com/your-username/employee-salary-prediction.git
   cd employee-salary-prediction
2. Install dependencies:
   pip install -r requirements.txt
3. Run the Streamlit app:
   streamlit run salary.py
### Option 3: Deploy on Streamlit Community Cloud
1. Push this repo to GitHub
2. Go to Streamlit Community Cloud
3. Select this repo and set salary.py as the entry point
4. Your app will be live! 🚀

📦 Dependencies
1. pandas
2. matplotlib
3. scikit-learn
4. streamlit
5. joblib

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Developed by Pragya Srivastava


