#!/usr/bin/env python
# -*-coding:utf-8-*-



from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta



START_DT = datetime(2018,5,23,0)

default_args = {
    'owner': 'cdwanze',
    'depends_on_past': False,
    'start_date': START_DT,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG('run_bash_script_example', default_args=default_args, schedule_interval='@weekly')



task_backup = BashOperator(
    task_id = 'run_bash_script_example',
    bash_command = 'test.sh',
    dag = dag
)

