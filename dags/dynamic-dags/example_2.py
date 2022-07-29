from airflow import DAG
from airflow.decorators import task
from utils.constants import default_args

# Dynamic Task Mapping
# https://airflow.apache.org/docs/apache-airflow/2.3.0/concepts/dynamic-task-mapping.html

dag_id = "example_2"

with DAG(dag_id=dag_id, default_args=default_args, schedule_interval=None) as dag:

    list_one_to_ten = list(range(1, 11))

    @task
    def each_value(x: int):
        return x

    each_value_in_list = each_value.expand(x=list_one_to_ten)
