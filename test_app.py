import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Salary Prediction API is Running!" in response.data

def test_predict_endpoint(client):
    response = client.post('/predict', json={'YearsExperience': 5.0})
    assert response.status_code == 200
    assert 'predicted_salary' in response.json