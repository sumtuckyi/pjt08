from locust import HttpUser, task, between

# HttpUser : Http 요청을 만드는 가상 유저
class SampleUser(HttpUser):
    # 작업 간 대기시간
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def normal_sort(self):
        self.client.get("test/normal_sort/")

    # @task(N) : 가중치(실행확률) , N만큼 높은 확률로 작업을 수행
    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")


