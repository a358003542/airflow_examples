#!/usr/bin/env python
# -*-coding:utf-8-*-


from datetime import datetime, timedelta
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


START_DT = datetime(2018,6,29,0)

default_args = {
    'owner': 'cdwanze',
    'depends_on_past': True,
    'start_date': START_DT,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('run_job_minutely_for_test', default_args=default_args, schedule_interval='* * * * *')


def main(ds, **kwargs):
    logging.info('start view content ...')

    execution_date = kwargs['execution_date']
    logging.info('execution_date is {0}'.format(execution_date))

    task_instance = kwargs['task_instance']
    run_id = kwargs['run_id']

    airflow_unique_id = '{0}_{1}_{2}'.format(task_instance.dag_id, task_instance.task_id, run_id)
    logging.info(airflow_unique_id)
    return 'view execution_date is {0} finished'.format(execution_date)


task_view = PythonOperator(
    task_id = 'run_job_minutely_for_test',
    python_callable = main,
    provide_context=True,
    dag = dag
)

