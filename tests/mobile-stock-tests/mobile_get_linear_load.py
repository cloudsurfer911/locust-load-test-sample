from locust import HttpUser, task, between

import logging
import sys
import argparse

# Use some basic logging for logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

'''
Author: Sujith Subramanian
Date: 2024-07-07

Test the APIs that are expected to reviece 
heavy load in production

Increase load linearly till the APIs reach
breaking point

'''
class MobileStockUser(HttpUser):
    host = "http://localhost:5050"
    wait_time = between(1, 5)

    @task
    def get_devices(self):
        response = self.client.get('/devices')
        if response.status_code != 200:
            logger.error(f"GET devices failed: {response.status_code}, {response.text}")
        else:
            logger.info("GET devices request is OK")

    @task
    def get_brands(self):
        response = self.client.get('/brands')
        if response.status_code != 200:
            logger.error(f"GET brands failed: {response.status_code}, {response.text}")
        else:
            logger.info("GET brands request was successful")

    @task
    def get_categories(self):
        response = self.client.get('/categories')
        if response.status_code != 200:
            logger.error(f"GET categories failed: {response.status_code}, {response.text}")
        else:
            logger.info("GET categories request was successful")



''' Linear load test  can be started using a command like 
    locust -f mobile_get_linear_load.py --web-host localhost 
    --web-port 8089 --host http://localhost:5050
    
    The number of users, ramp up, needs to specificed at 
    http://localhost:8089

'''
if __name__ == "__main__":
    import locust
    locust.main()