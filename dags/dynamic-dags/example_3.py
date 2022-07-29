from airflow import DAG
from airflow.decorators import task
from utils.constants import default_args

# A combination of example 1 and example 2

dag_id = "example_3"

with DAG(dag_id=dag_id, default_args=default_args, schedule_interval=None) as dag:

    list_one_to_twenty = list(range(1, 21))

    @task
    def dummy_start_task():
        print("start")

    tasks = []
    for i in range(10):

        @task(task_id=f"test_{str(i)}")
        def each_value(x: int):
            return x

        tasks.append(each_value.expand(x=list_one_to_twenty))

    @task
    def dummy_collector_task(tasks):
        print(tasks)

    dummy_start_task_ = dummy_start_task()
    dummy_start_task_ >> tasks
    dummy_collector_task(tasks)
