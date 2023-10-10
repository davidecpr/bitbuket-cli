from setuptools import setup, find_packages

setup(
    name="bitbucket-cli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'click',
        'requests',
        'prompt_toolkit'
    ],
    entry_points={
        'console_scripts': [
            'bitbucket-cli=bitbucket_cli.main:cli',
        ],
    },
)
