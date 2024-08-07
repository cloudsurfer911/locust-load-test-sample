# Initial Setup

1. Create and activate a virtual environment:
   python3 -m venv load_env
   source load_env/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

# Application Under Test

The application is a simple mobile stock API server written in NodeJS.

- URL: http://localhost:5050

# Running a Linear Load Test Until Breaking Point

**Command:**
   locust -f mobile_get_linear_load.py --web-host localhost --web-port 8089 --host http://localhost:5050

# Run the performance test for varying production-like load:
   locust -f mobile_stock_real_world_load.py

Launch http://0.0.0.0:8089/ and provide the host as http://localhost:5050/

The load, spawn rate, and duration are determined by the stages[] list in the locust file, so there's no need to provide any other details.