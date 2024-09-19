from setuptools import setup

setup(
    name='django-q-monitor',
    packages=['django_q_monitor'],
    description='monitor django-q tasks',
    version='1.0.0',
    url='http://github.com/simukka/django-q-monitor',
    author='Kyle Simukka',
    author_email='kylesimukka@gmail.com',
    keywords=['django-q'],
    install_requires=[
        'django',
        'django-q'
    ],
)