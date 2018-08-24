from setuptools import setup, find_packages


APP_NAME = 'countq'
VERSION = '0.1.0'
AUTHOR = 'James Hibbard'
AUTHOR_EMAIL = ''

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="Python tool for counting variants",
    license="MIT",
    install_requires=[
        'click==6.7',
        'pandas==0.23.4',
        'openpyxl==2.5.5',
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        countq=countq.runner:cli
    ''',
)
