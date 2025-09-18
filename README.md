
# AAVAIL ML Project

## Run API locally
1. Install dependencies:
   pip install -r requirements.txt
2. Run Flask app:
   python app.py
3. POST JSON to /predict with "target_date" and "country"

## Run tests
bash run_tests.sh

## Docker
docker build -t aavail-app .
docker run -p 5000:5000 aavail-app
