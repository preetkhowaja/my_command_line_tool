from setuptools import setup

setup(
    name="my_cli",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        my_cli=my_cli:cli
    ''',
)