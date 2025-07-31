# 💼 Employee Salary Prediction

This is a machine learning project that predicts whether an employee earns **more than 50K** or **less than or equal to 50K** annually based on features like age, education, occupation, and hours worked per week. The project includes a web-based interface using Streamlit and is deployable directly from Google Colab.

---

## 🚀 Features
- Predict salary class: **<=50K** or **>50K**
- Supports both individual and batch predictions
- Interactive UI using **Streamlit**
- Model trained using algorithms like Logistic Regression, Random Forest, SVM, and Gradient Boosting
- Hosted using **ngrok** from Google Colab for public access

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
   !pip install streamlit pyngrok joblib pandas scikit-learn matplotlib
3.Run the app using:
   !streamlit run salary.py & npx localtunnel --port 8501

### Option 2: Run Locally
1.Clone the repository:
git clone https://github.com/your-username/employee-salary-prediction.git
cd employee-salary-prediction
2.Install dependencies:
pip install -r requirements.txt
3.Run the Streamlit app:
streamlit run salary.py

📦 Dependencies
pandas

1.matplotlib
2.scikit-learn
3.streamlit
4.pyngrok
5.joblib

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Developed by Pragya Srivastava

