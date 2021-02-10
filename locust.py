import time
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def LoginPage(self):
        self.client.get(url= "/login")
        
    @task
    def LoginPage(self):
        self.client.get(url= "/CreateUsers")