# ML DevOps Pipeline Demo

This project demonstrates a simple workflow for automating the training, testing, and deployment of a machine learning model using Jenkins—designed specifically to boost your DevOps and MLOps resume!

## Features

- 🧑‍💻 Simple Python script that trains a RandomForestClassifier on the famous Iris dataset.
- 🛠️ Automated tests using `pytest`.
- ⚙️ Jenkinsfile for Continuous Integration: installs dependencies, runs tests, trains and saves the model automatically.
- 🏷️ Reproducible and extendable structure following real MLOps practices.

## Files

- `src/train.py` — Training script
- `tests/test_train.py` — Basic test for training script
- `requirements.txt` — Python dependencies
- `Jenkinsfile` — Defines the Jenkins pipeline
- `models/iris_model.pkl` — Saved trained model (auto-generated)

## How to Run Locally

1. **Clone the repository**
2. **Install dependencies:**  
   `pip install -r requirements.txt`
3. **Run tests:**  
   `pytest`
4. **Train the model:**  
   `python src/train.py`

## How to Run with Jenkins

- Point Jenkins to your repository.
- Jenkins will automatically execute the pipeline in the `Jenkinsfile`:
  1. Installs Python packages
  2. Runs all tests
  3. Trains and saves the ML model

## Why This Is Great for Your Resume 🚀

- Combines DevOps (CI/CD pipelines with Jenkins) and AI/ML in a single, real-world project.
- Demonstrates automation, testing, model training, and reproducibility.
- Can be expanded with Docker, MLflow, Github Actions, etc.

---

Feel free to use or adapt this project for job applications and interviews!
