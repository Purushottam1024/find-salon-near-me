import os
import stat

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver_path = ChromeDriverManager().install()
    print("ChromeDriverManager().install() returned:", driver_path)

    chromedriver_exec = driver_path

    # If the returned path is not an actual chromedriver executable, fix it
    if not os.path.basename(driver_path) == "chromedriver":
        print(
            "Returned path is not 'chromedriver'; stepping back to find executable..."
        )
        base_dir = os.path.dirname(driver_path)
        chromedriver_exec = os.path.join(base_dir, "chromedriver")

    # Validate final path
    if not os.path.isfile(chromedriver_exec):
        raise FileNotFoundError(f"chromedriver not found at: {chromedriver_exec}")

    # Ensure it is executable
    if not os.access(chromedriver_exec, os.X_OK):
        print("Making chromedriver executable...")
        st = os.stat(chromedriver_exec)
        os.chmod(chromedriver_exec, st.st_mode | stat.S_IEXEC)

    print("Using chromedriver executable:", chromedriver_exec)

    service = Service(executable_path=chromedriver_exec)
    driver = webdriver.Chrome(service=service, options=options)
    return driver
