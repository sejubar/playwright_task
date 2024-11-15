# playwright_task

1. create python virtual enviroment:  `python -m venv venv` or `python3 -m venv venv` depending on your machine. 

2. activate virtual enviroment: `source venv/bin/activate`
install pip: `sudo apt install python3-pip`

3. install dependencies: `pip install -r requirements.txt`


## using vscode devcontainers
See how to install here: https://code.visualstudio.com/docs/devcontainers/containers

once you are in your devcontainers you can follow steps above.

## running the test
`pytest tests/test_example.py --headed --slowmo 2000`
