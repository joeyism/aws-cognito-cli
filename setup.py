#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = open("requirements.txt").read().splitlines()

test_requirements = open("requirements_dev.txt").read().splitlines()

setup(
    author="joeyism",
    author_email='joeyism101@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A simple CLI tool to get the AWS Cognito Access Token",
    entry_points={
        'console_scripts': [
            'aws-cognito-cli=aws_cognito_cli.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    package_data={
        "aws-cognito-cli": ["aws_cognito_cli/VERSION"],
    },
    keywords='aws-cognito-cli',
    name='aws-cognito-cli',
    packages=find_packages(include=['aws_cognito_cli', 'aws_cognito_cli.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/joeyism/aws_cognito_cli',
    version=open("aws_cognito_cli/VERSION").read().strip(),
    zip_safe=False,
)
