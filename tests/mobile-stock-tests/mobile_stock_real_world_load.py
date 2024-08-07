from locust import HttpUser, task, between, LoadTestShape
import logging
import random
import sys
import argparse

# Use  some basic logging for logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


'''

Author: Sujith Subramanian
Date: 2024-07-07

This class will generate load just like a real world scenario
i.e. with varying loads for varying durations
    
The load can be varied easily CustomShape stages list
'''
class MobileStockUserRealWorld(HttpUser):
    wait_time = between(1, 5)

    device_ids = []
    brand_ids = [1, 2, 3, 4, 5]  # Sample
    category_ids = [1, 2, 3, 4, 5]  # Sample and optional only

    number_of_get_calls = 0

    @task
    def post_device(self):
        # create a simple payload for the POST device call
        new_device = {"id": random.randint(10, 1000), "model": f"new phone model {random.randint(10, 1000)}"}
        logger.info(f'POST body is @@@ {new_device}')

        response = self.client.post('/devices', json=new_device)

        # do a basic check if the POST call is successful or not
        if response.status_code != 201 and response.status_code != 200:
            logger.error(f"POST device failed: {response.status_code}, {response.text}")
        else:
            logger.info("POST device was successful")
            if new_device["id"] not in self.device_ids:
                self.device_ids.append(new_device["id"])

                # the device_ids list is needed for future use
                # for other api calls
                logger.info(f'device_ids list is >>>: {self.device_ids}')

    @task
    def get_devices(self):
        response = self.client.get('/devices')
        if response.status_code != 200:
            logger.error(f"GET devices failed: {response.status_code}, {response.text}")
        else:
            self.number_of_get_calls += 1
            logger.info("GET devices request is OK")
            logger.info(f'number_of_get_calls now: {self.number_of_get_calls}')

    @task
    def delete_device(self):
        if self.device_ids:
            device_id = random.choice(self.device_ids)
            response = self.client.delete(f'/devices/{device_id}')
            if response.status_code != 204 and response.status_code != 200:
                logger.error(f"DELETE request failed: {response.status_code}, {response.text}")
            else:
                logger.info(f"DELETE devices/{device_id} request was successful")
                self.device_ids.remove(device_id)
        else:
            logger.info("No device ids available for DELETE request")

    @task
    def post_brand(self):
        new_brand = {"id": random.randint(6, 1000), "name": f"New Brand {random.randint(6, 1000)}"}
        logger.info(f'POST body is {new_brand}')
        response = self.client.post('/brands', json=new_brand)
        if response.status_code != 201 and response.status_code != 200:
            logger.error(f"POST request failed: {response.status_code}, {response.text}")
        else:
            logger.info("POST request was successful")
            if new_brand["id"] not in self.brand_ids:
                self.brand_ids.append(new_brand["id"])

    @task
    def get_brands(self):
        response = self.client.get('/brands')
        if response.status_code != 200:
            logger.error(f"GET request failed: {response.status_code}, {response.text}")
        else:
            logger.info("GET brands request was successful")

    @task
    def delete_brand(self):
        if self.brand_ids:
            brand_id = random.choice(self.brand_ids)
            response = self.client.delete(f'/brands/{brand_id}')
            if response.status_code != 204 and response.status_code != 200:
                logger.error(f"DELETE request failed: {response.status_code}, {response.text}")
            else:
                logger.info("DELETE brand request was successful")
                self.brand_ids.remove(brand_id)
        else:
            logger.info("No brand ids available for DELETE request")

    @task
    def post_category(self):
        new_category = {"id": random.randint(10, 1000), "name": f"New Category {random.randint(10, 1000)}"}
        logger.info(f'POST body is {new_category}')
        response = self.client.post('/categories', json=new_category)
        if response.status_code != 201 and response.status_code != 200:
            logger.error(f"POST request failed: {response.status_code}, {response.text}")
        else:
            logger.info("POST request was successful")
            if new_category["id"] not in self.category_ids:
                self.category_ids.append(new_category["id"])

    @task
    def get_categories(self):
        response = self.client.get('/categories')
        if response.status_code != 200:
            logger.error(f"GET request failed: {response.status_code}, {response.text}")
        else:
            logger.info("GET request was successful")

    @task
    def delete_category(self):
        if self.category_ids:
            category_id = random.choice(self.category_ids)
            response = self.client.delete(f'/categories/{category_id}')
            if response.status_code != 204 and response.status_code != 200:
                logger.error(f"DELETE request failed: {response.status_code}, {response.text}")
            else:
                logger.info("DELETE request was successful")
                self.category_ids.remove(category_id)
        else:
            logger.info("No category ids available for DELETE request")

'''Custom shape is use to set the shape of the test
    that is how long and how many users will run 
    in each defined time interval.
    
    This test is designed to run for about 3.10 hours
    Good for a real world scenario load test 
'''
class CustomShape(LoadTestShape):
    stages = [
        {"duration": 50, "users": 400, "spawn_rate": 20, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 120, "users": 200, "spawn_rate": 10, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 60, "users": 200, "spawn_rate": 10, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 240, "users": 400, "spawn_rate": 20, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 360, "users": 600, "spawn_rate": 30, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 160, "users": 600, "spawn_rate": 30, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 480, "users": 800, "spawn_rate": 40, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 600, "users": 1000, "spawn_rate": 50, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 720, "users": 800, "spawn_rate": 40, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 840, "users": 600, "spawn_rate": 30, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 960, "users": 400, "spawn_rate": 20, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 1080, "users": 200, "spawn_rate": 10, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 1200, "users": 100, "spawn_rate": 5, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 1080, "users": 200, "spawn_rate": 10, "user_classes": [MobileStockUserRealWorld]},
        {"duration": 1200, "users": 100, "spawn_rate": 5, "user_classes": [MobileStockUserRealWorld]}

    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                return (stage["users"], stage["spawn_rate"])
        return None


if __name__ == "__main__":
    import locust

    # Set the default command line arguments like port number and hostname etc
    parser = argparse.ArgumentParser()
    parser.add_argument("--web-host", default="localhost", help="Host for web interface")
    parser.add_argument("--web-port", default=8089, type=int, help="Port for web interface")
    args = parser.parse_args()
    sys.argv.extend(["--web-host", args.web_host, "--web-port", str(args.web_port)])
    locust.main()