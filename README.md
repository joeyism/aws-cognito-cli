# AWS Cognito CLI
A simple CLI tool to get the AWS Cognito Access Token, because it's currently far more complicated than it needs to be

## Installation
```bash
pip install aws-cognito-cli
```

## Usage
```
usage: aws-cognito-cli [-h] -u USERNAME -p PASSWORD --pool-id POOL_ID --client-id CLIENT_ID
```

### Example Usage
```bash
aws-cognito-cli -u joeyism -p somePassword --pool-id us-east-1_abc123 --client-id ABCDEFGHIJKLMN1234567890
```

## Future Features
* Cache pool id and client id
* Read info from env
* Add CI/CD


## Documentation
* Free software: Apache Software License 2.0
* Documentation: https://aws-cognito-cli.readthedocs.io.


## Credits
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
