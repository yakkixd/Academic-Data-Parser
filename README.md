# 📘 Academic Result Parser (CBSE Simulator)

A lightweight **Flask** web application that simulates the official **CBSE Results Portal**.  
Users can search for student results using a **Roll Number**, and the system fetches data from a simple **JSON database**.

> ⚠️ This project is for **educational purposes only** and is not affiliated with CBSE or NIC.

---

## 🚀 Features

- 🎨 **Authentic UI** – Replicates the look of the official CBSE results website  
- 🗂️ **JSON Database** – No SQL or external DB required  
- 🔍 **Roll Number Search** – Validates input & handles errors  
- 📱 **Responsive Design** – Clean HTML/CSS table layout  
- ☁️ **Cloud Ready** – Includes `vercel.json` for deployment  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Python (Flask) |
| Frontend | HTML, CSS |
| Data Storage | JSON |
| Deployment | Vercel |

---

## 📂 Project Structure

```
result_spoof_/
├── main.py            # Main application entry point (Local)
├── results.json       # Database containing student marks
├── vercel.json        # Configuration for Vercel deployment
├── api/               # Serverless function entry point
│   └── main1.py
└── templates/         # HTML Templates
    ├── index.html     # Search/Home page
    └── result.html    # Result display page
```

---

## ⚙️ Setup & Installation

### 🔹 Prerequisites
- Python 3.x  
- pip (Python Package Manager)

### 🔹 Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/result-spoof.git
   cd result_spoof_
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 📖 Usage

1. Open the **Examination Results 2025** page  
2. Enter a valid **Roll Number**  
3. Click **Submit**  
4. View the student's marksheet  

---

## 🧪 Sample Data

Use this Roll Number from the default `results.json`:

```
Roll Number: 11111111
```

---

## 📝 Customizing Results

You can add or modify students directly in `results.json`.

### Example Format:

```json
"ROLL_NUMBER": {
  "name": "STUDENT NAME",
  "mother_name": "MOTHER NAME",
  "father_name": "FATHER NAME",
  "school_name": "SCHOOL NAME",
  "result": "PASS",
  "subjects": [
    {
      "code": "301",
      "name": "ENGLISH CORE",
      "theory": "070",
      "practical": "020",
      "total": "090",
      "grade": "A1"
    }
  ]
}
```

---

## ⚠️ Disclaimer

This project is strictly for **educational and demonstration purposes**.  
It is **not** affiliated with:

- Central Board of Secondary Education (CBSE)  
- National Informatics Centre (NIC)  
