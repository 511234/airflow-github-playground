from time import sleep
from airflow.decorators import dag, task
from utils.constants import default_args

dag_id = "example_1"

class SomeClass:
    def __init__(self, some_name="some_first_name"):
        self.some_name = some_name
        self.operator_size = 5

    def dag_wrapper(self):
        @dag(dag_id=dag_id, default_args=default_args, schedule_interval=None)
        def some_dag():
            @task
            def dummy_start_task():
                print("start")

            tasks = []
            for i in range(self.operator_size):

                @task(task_id=f"test_{str(i)}")
                def get_name():
                    print("now start sleeping")
                    sleep(600)
                    return self.some_name

                tasks.append(get_name())

            @task
            def dummy_collector_task(tasks):
                print(tasks)

            dummy_start_task_ = dummy_start_task()
            dummy_start_task_ >> tasks
            dummy_collector_task(tasks)

        return some_dag()


some_class_instance = SomeClass()
greet_dag = some_class_instance.dag_wrapper()
