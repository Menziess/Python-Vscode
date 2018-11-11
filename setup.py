from setuptools import setup

setup(
    name='python-vscode',
    entry_points={
        'console_scripts': {
            'fib = src.cli.command_line_fib:main',
        }
    },
    install_requires=[
        'flask>=1.0',
        'redis',
    ])
