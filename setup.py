#!/usr/bin/env python
# -*-coding:utf-8-*-


from setuptools import setup, find_packages
import codecs

REQUIREMENTS = []


def long_description():
    with codecs.open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='dags',
    version='0.0.1',
    description='bihu system airflow works',
    long_description=long_description(),
    author='wanze',
    author_email='a358003542@gmail.com',
    platforms='Linux',
    keywords=['dags support', 'python'],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
)
