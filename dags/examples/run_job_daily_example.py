#!/usr/bin/env python
# -*-coding:utf-8-*-


from datetime import datetime, timedelta
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


START_DT = datetime(2018,5,8,10)

default_args = {
    'owner': 'cdwanze',
    'depends_on_past': False,
    'start_date': START_DT,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('run_job_daily_example', default_args=default_args, schedule_interval='@daily')


def main(ds, **kwargs):
    logging.info('start view content ...')

    execution_date = kwargs['execution_date']
    logging.info('execution_date is {0}'.format(execution_date))

    start_dt = execution_date

    return 'view execution_date is {0} finished'.format(execution_date)


task_view = PythonOperator(
    task_id = 'run_job_daily_example',
    python_callable = main,
    provide_context=True,
    dag = dag
)

