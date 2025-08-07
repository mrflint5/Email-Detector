# 📧 EMAIL DETECTOR – Fake Mail Classification App 🛡️

Welcome to **EMAIL DETECTOR**, a sleek Python-powered application that detects **fake/spam emails** using **Machine Learning**. This project leverages **Natural Language Processing (NLP)** and a **Naive Bayes classifier** to enhance digital safety by identifying malicious or unwanted emails.

---

## 🚀 Features

- 🔍 Classifies emails as **SPAM** or **HAM (genuine)** with high accuracy
- 🧠 Uses **TF-IDF Vectorization** for smart text feature extraction
- ⚡ Powered by **Naive Bayes** for fast and reliable predictions
- 📚 Trained on a dataset of **1000 labeled email samples**
- 💬 User-friendly terminal-based interface for real-time predictions
- 💾 Saves the trained model using **joblib** for future use
- 📈 Displays prediction confidence scores

---

## 🛠️ Tech Stack

| Tool            | Purpose                              |
|-----------------|--------------------------------------|
| 🐍 **Python 3**  | Core programming language            |
| 📊 **pandas**    | Data manipulation and preprocessing  |
| 🤖 **scikit-learn** | Machine learning and NLP tools     |
| 💾 **joblib**    | Model persistence (saving/loading)   |

---

## 🔍 How It Works

1. Loads a pre-trained **Naive Bayes classifier** or trains a new one if none exists
2. Processes email text using **TF-IDF Vectorization** to extract features
3. Predicts whether the email is **SPAM** or **HAM** using the trained model
4. Outputs the prediction and confidence score in the terminal
5. Saves the model for reuse

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

```pgsql
📨 Enter email content (or type 'exit' to quit):
> Win a FREE iPhone now! Click here!
🔎 Prediction: SPAM (Confidence: 92%)
```

### 📂 Project Structure

```bash
Email-Detector/
├── data/
│   └── emails.csv              # Dataset with 1000 labeled emails
├── models/
│   └── nb_model.joblib         # Saved Naive Bayes model
├── fake_mail_detector.py       # Main script for training & prediction
└── README.md                   # Project documentation
```

### 📸 Screenshots

View the app in action: [Screenshot](https://drive.google.com/file/d/1TwmvZFbBPSBePjLfJ-i-A8tfjO8rGo5i/view?usp=drive_link)

---

## 🤝 Connect with Me

I'm open to feedback, collaboration, or a quick chat!

📧 **Email**: [sameermalik1419@gmail.com](mailto:sameermalik1419@gmail.com)  
🔗 **LinkedIn**: [Sameer Malik](https://linkedin.com/in/sameer-malik)

---

## 🙌 Credits

Built with 💻 + ❤️ to fight email spam using machine learning. Thanks to **scikit-learn** for powering the NLP and classification.

⭐ **If you like this project, please star the repo and share it!**
