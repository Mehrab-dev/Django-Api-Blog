from locust import HttpUser,task

class QuickstartUser(HttpUser) :

    def on_start(self) :
        response = self.client.post("/account/api/v1/create/jwt/",data={
            "email": "programmer.py.mail@gmail.com",
            "password": "Mm20399990"
        }).json()
        self.client.headers = {"Authorization" : f"Bearer {response.get('access',None )}"}
    
    @task
    def post_list(self) :
        self.client.get("/blog/api/v1/posts/")

    @task
    def category_list(self) :
        self.client.get("/blog/api/v1/categories/")