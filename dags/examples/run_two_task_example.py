#!/usr/bin/env python
# -*-coding:utf-8-*-



from datetime import datetime, timedelta
import logging
import os

import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


START_DT = datetime(2018,5,9)

default_args = {
    'owner': 'cdwanze',
    'depends_on_past': False,
    'start_date': START_DT,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('run_two_task_example', default_args=default_args, schedule_interval='@hourly')



def task_one_main():
    logging.info('task_one is running...')


def task_two_main():
    logging.info('task_two is running...')


task_one = PythonOperator(
    task_id = 'task_one',
    python_callable = task_one_main,
    dag = dag
)

task_two = PythonOperator(
    task_id = 'task_two',
    python_callable = task_two_main,
    dag = dag
)

task_two.set_upstream(task_one)