# Initial Setup

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv load_env
    source load_env/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

# Application Under Test

The application is a simple mobile stock API server written in NodeJS.

- **URL:** [http://localhost:5050](http://localhost:5050)

# Running a Linear Load Test Until Breaking Point

Run the load test using the following command:
```bash
locust -f mobile_get_linear_load.py --web-host localhost --web-port 8089 --host http://localhost:5050