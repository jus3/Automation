🚀 QA Automation Project Setup Guide (Pytest + Playwright + Selenium + Allure)

1) Create Project
Create project in PyCharm / any IDE

2) Create Virtual Environment (venv) [Always Create New]
where python  (Check Python path)
py -m venv .venv  (Create virtual environment)
.\.venv\Scripts\Activate  (Activate venv)
Remove-Item -Recurse -Force .venv (To Remove Old Evn)

3) Install Pytest
pip install pytest
pytest --version  (Verify installation)

4) Install Playwright
pip install playwright
playwright install  (Install browsers)
python -m pip install pytest-playwright  (Pytest integration)
playwright codegen  (Quick verification + locator capture tool)

5) Install Selenium
pip install selenium
pip install webdriver-manager  (Optional – auto manages drivers)

6) Install Git
Download & install from official site
git --version  (Verify installation)
git init  (Initialize repository)

7) Install Allure Reporting
pip install allure-pytest  (Pytest plugin)
allure --version  (Verify CLI installation)

⚠️ Note:
(Allure has 2 parts → Python plugin + CLI tool. Both are required)

8) Create requirements.txt
pip freeze > requirements.tx3t  (Save all installed dependencies)
pip install -r requirements.txt  (Install from file)

9) Standard Run Command (Recommended)
pytest --alluredir=Reports/allure-results (To generate and open HTML report in browser)
python -m pytest (Also Works)
python -m pytest --alluredir=Reports/allure-results (Also Works)