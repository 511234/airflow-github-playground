from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.decorators import task
from utils.constants import default_args

dag_id = "example_4"
ALL_RUNS = [1, 2, 3, 4, 5]

tasks = []

with DAG(dag_id=dag_id, default_args=default_args, schedule_interval=None) as dag:

    for run_name in ALL_RUNS:

        op_task_run = EmptyOperator(task_id=f"task_{run_name}")

        tasks.append(op_task_run)
    tasks[0] >> tasks[1] >> tasks[2] >> tasks[3] >> tasks[4]
