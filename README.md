Salary Predictor
A machine learning project with a CI/CD pipeline to predict salaries based on years of experience.
Project Structure

app.py: Flask app for salary prediction.
train_model.py: Script to train and save the model.
test_app.py: Unit tests for the Flask app.
requirements.txt: Python dependencies.
Dockerfile: Docker configuration.
Jenkinsfile: Jenkins pipeline for deployment.
.github/workflows/: GitHub Actions workflows for linting and testing.

Setup Instructions

Repository Setup:
Create branches: dev, test, master.
Protect master to require PR reviews.


Model Training:
Run python train_model.py to generate salary_model.pkl.


Run Locally:
Install dependencies: pip install -r requirements.txt.
Run the app: python app.py.


CI/CD Pipeline:
GitHub Actions: Linting on PRs to dev, testing on PRs to test.
Jenkins: Builds and pushes Docker image to Docker Hub on merge to master.
Admin Notification: Email sent to admin@example.com on successful deployment.



Pipeline Flow

Push code to dev → Flake8 checks via GitHub Actions.
PR from dev to test → Unit tests via GitHub Actions.
PR from test to master → Jenkins builds Docker image, pushes to Docker Hub, and sends email notification.

