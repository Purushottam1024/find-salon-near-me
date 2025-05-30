import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def search_salons(driver, query, scrolls):
    driver.get("https://www.google.com/maps")
    time.sleep(3)

    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)

    for _ in range(scrolls):
        driver.execute_script(
            "document.querySelectorAll('div[role=\"feed\"]')[0].scrollBy(0, 1000);"
        )
        time.sleep(2)

    salon_elements = driver.find_elements(By.CSS_SELECTOR, "a.hfpxzc")
    return [elem.get_attribute("href") for elem in salon_elements]
