import json
import logging
import os

import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    #Add timestamp to report file name
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    #Create logs folder if not exists
    os.makedirs("logs",exist_ok=True)
    log_file = datetime.now().strftime("logs/test_run_%Y-%m-%d_%H-%M-%S.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [$(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


    logging.info("\nSetting up resources....")
    yield
    logging.info("\nTearing down resources....")

#Load test data to use one by one
def get_test_data(key):
    with open("data/test_data.json") as td:
        test_data = json.load(td)
    return test_data[key]

#Load config data
def get_config_data(key):
    with open("data/config.json") as f:
        data = json.load(f)
    return data[key]
