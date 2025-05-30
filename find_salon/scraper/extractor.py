import time

from selenium.webdriver.common.by import By


def extract_salon_data(driver, url):
    driver.get(url)
    time.sleep(5)

    def safe_find(by, value, attr=None):
        try:
            elem = driver.find_element(by, value)
            return elem.get_attribute(attr) if attr else elem.text
        except:
            return ""

    name = safe_find(By.XPATH, "//h1")
    address = safe_find(By.XPATH, "//button[@data-item-id='address']")
    phone = safe_find(By.XPATH, "//button[@data-tooltip='Copy phone number']")
    website = safe_find(By.XPATH, "//a[@data-item-id='authority']", attr="href")
    rating = safe_find(By.XPATH, "//span[@class='MW4etd']")
    reviews = safe_find(By.XPATH, "//span[contains(@aria-label, 'reviews')]")

    try:
        hours_button = driver.find_element(By.XPATH, "//span[text()='Hours']")
        hours_button.click()
        time.sleep(1)
        hours = "\n".join(
            [
                elem.text
                for elem in driver.find_elements(
                    By.XPATH, "//table[contains(@class, 'WgFkxc')]//tr"
                )
            ]
        )
    except:
        hours = ""

    return [name, address, phone, website, rating, reviews, hours, url]
