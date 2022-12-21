#!/usr/bin/python3
import argparse
import subprocess

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="This script starts the website by invoking a flask command")

    parser.add_argument('--debug', action='store_true',
                        default=False, help='Enables debug mode for the flask')
    parser.add_argument('-p', '--port', default=80, type=int,
                        help='Specify the port for the webserver')
    parser.add_argument('--test', action='store_true', default=False,
                        help='Sets debug mode to true and the port to 5000')

    parser.add_argument('--app-name', default="website", type=str,
                        help='Sets the name for the python script that will be started. This is "website" by default')

    args = parser.parse_args()

    if args.test == True:
        args.debug = True
        args.port = 5000

    subprocess.run(['export', f'FLASK_RUN_PORT={args.port}'],shell=True)
    subprocess.run(['export', f'FLASK_APP={args.app_name}'],shell=True)
    if args.debug == True:
        subprocess.run(['export', f'FLASK_RUN_HOST=""'],shell=True)
        subprocess.run(['export', f'FLASK_ENV="debug"'],shell=True)
    else:
        subprocess.run(['export', f'FLASK_RUN_HOST="0.0.0.0"'],shell=True)
        subprocess.run(['export', f'FLASK_ENV="development"'],shell=True)

    subprocess.run([f'sudo','flask','run'], shell=True)
