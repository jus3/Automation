import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://practicesoftwaretesting.com/"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()

#Code related to allure report generation
def pytest_sessionfinish(session, exitstatus):
    """Auto-generate Allure report after execution (clean structure)."""

    import datetime
    from pathlib import Path
    import subprocess
    import shutil
    import webbrowser

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    project_root = Path(__file__).resolve().parents[1]

    reports_dir = project_root / "Reports"
    results_dir = reports_dir / "allure-results"
    output_dir = reports_dir / f"allure-report-{timestamp}"

    # ✅ Ensure Reports folder exists
    reports_dir.mkdir(exist_ok=True)

    # 🔴 Move results if generated in root
    root_results = project_root / "allure-results"
    if root_results.exists():
        if results_dir.exists():
            shutil.rmtree(results_dir)
        shutil.move(str(root_results), str(results_dir))

    # 🔴 Check results exist
    if not results_dir.exists() or not any(results_dir.iterdir()):
        print("\n❌ No allure results found. Did you run with --alluredir?\n")
        return

    # 🔴 Allure path
    allure_path = r"C:\Users\USER\scoop\apps\allure\current\bin\allure.bat"

    # ✅ Generate report
    subprocess.run(
        f'"{allure_path}" generate "{results_dir}" -o "{output_dir}" --clean',
        shell=True,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print(f"\n✅ Allure report generated at: {output_dir}\n")

    # ✅ Open report (clean way)
    # webbrowser.open((output_dir / "index.html").as_uri())