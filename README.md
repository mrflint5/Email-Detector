# 📧 EMAIL DETECTOR – Fake Mail Classification App 🛡️

Welcome to **EMAIL DETECTOR** – a sleek and intelligent Python-powered application that detects **fake/spam emails** using cutting-edge **Machine Learning**. This project demonstrates how NLP and classification algorithms can be applied in real-world scenarios to enhance digital safety.

![📸 Working Screenshot](https://drive.google.com/uc?id=1TwmvZFbBPSBePjLfJ-i-A8tfjO8rGo5i)

---

## 🚀 Features

🔹 Detects whether an email is **SPAM** or **HAM (genuine)**  
🔹 Uses **TF-IDF Vectorization** for intelligent text representation  
🔹 Built with **Naive Bayes** for efficient classification  
🔹 Trained on a dataset of 1000 labeled emails  
🔹 Instant predictions via terminal input  
🔹 Auto-saves trained model for future use

---

## 🛠️ Tech Stack

- 🐍 Python 3
- 📊 pandas
- 🤖 scikit-learn
- 💾 joblib

---

## 🔍 How It Works

1. Loads or trains a classifier on email content
2. Applies **TF-IDF vectorization**
3. Uses **Naive Bayes** to classify the email
4. Outputs prediction in the terminal interface

---

## 🖥️ Run Locally

### 📥 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Email-Detector.git
cd Email-Detector
```

### 📦 Step 2: Install Dependencies

```bash
pip install pandas scikit-learn joblib
```

### 🚀 Step 3: Launch the App

```bash
python fake_mail_detector.py
```

You'll be prompted to enter email content:

```
📨 Enter email content (or type 'exit' to quit):
> Win a FREE iPhone now!
🔎 This email is likely: SPAM
```

---

## 📂 Project Structure

```
Email-Detector/
├── emails.csv              # Dataset containing 1000 email samples
├── fake_mail_detector.py   # Main script
└── README.md               # Project documentation
```

---

## 🤝 Connect with Me

I'm always open to collaboration, feedback, or a friendly chat!

- 📧 Email: [sameermalik1419@gmail.com](mailto:sameermalik1419@gmail.com)
- 🔗 LinkedIn: [Sameer Malik](https://www.linkedin.com/in/sameer-malik-b5b8772b9) – *Feel free to connect!*

---

## 🙌 Credits

Built with 💻 + ❤️ to demonstrate real-world machine learning applications in the fight against email spam.
