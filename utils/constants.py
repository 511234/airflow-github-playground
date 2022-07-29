from airflow.utils.dates import days_ago
from datetime import timedelta


default_args = {
    "owner": "owner",
    "depends_on_past": False,
    "email": ["someone@somehost.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 4,
    "retry_delay": timedelta(seconds=15),
    "start_date": days_ago(1),
}