"""Console script for aws_cognito_cli."""
import argparse
import sys
from aws_cognito_cli import aws_cognito_cli


def main():
    """Console script for aws_cognito_cli."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help="Username", required=True)
    parser.add_argument('-p', '--password', help="Password", required=True)
    parser.add_argument('--pool-id', help="Pool ID", required=True)
    parser.add_argument('--client-id', help="Client ID", required=True)
    args = parser.parse_args()
    print(aws_cognito_cli.get_access_token(
        username=args.username,
        password=args.password,
        pool_id=args.pool_id,
        client_id=args.client_id
    ), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
