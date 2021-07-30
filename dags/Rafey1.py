"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

from print1Hour import print_1_Hour
from print2Hour import print_2_Hour
from overlapping import over_lapping

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 7, 28),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("Rafey1", default_args=default_args, schedule_interval=timedelta(hours = 1), catchup =False)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id='No1_check_file_exists', bash_command = 'shasum ~/store_files_airflow/No1.csv', retries = 2, retry_delay = timedelta(seconds=15),dag=dag)
t2 = BashOperator(task_id='No2_check_file_exists', bash_command = 'shasum ~/store_files_airflow/No2.csv', retries = 2, retry_delay = timedelta(seconds=15),dag=dag)

t3 = PythonOperator(task_id="print1Hour",python_callable=print_1_Hour,dag=dag, retries = 5)
t4 = PythonOperator(task_id="print2Hour",python_callable=print_2_Hour,dag=dag, retries = 5)

t5 = PythonOperator(task_id="overlapping",python_callable=over_lapping,dag=dag, retries = 5)
t1>>t2>>[t3,t4]>>t5