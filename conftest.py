import pytest
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

#Files and data manipulation
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_DATA_FILE=BASE_DIR / "AQA_SimplePractice_task/data.json"

@pytest.fixture(scope="session")
#Fixture to load data used in test in JSON file
def task_data():
    try:
        with open(TASK_DATA_FILE,'r') as f:
            data=json.load(f)
            return data
    except FileNotFoundError:
        pytest.fail(f"File not found in: {TASK_DATA_FILE}")

    except json.JSONDecodeError:
        pytest.fail(f"JSON decode error in: {TASK_DATA_FILE}")

#Playwright instance for test session
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

#Launching Chromium browser
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

#Creating browser context
@pytest.fixture(scope="function")
def page(browser, task_data):
    context = browser.new_context()
    page = context.new_page()
    page.goto(task_data["login"]["base_url"])
    yield page
    context.close()