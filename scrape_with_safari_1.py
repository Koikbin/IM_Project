from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver for Safari
driver = webdriver.Safari()

def login_to_threads(username, password):
    try:
        driver.get("https://www.threads.net/accounts/login/")
        print("Here 0000")
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username, phone or email']")))

        # Locate username input using placeholder attribute
        driver.find_element(By.XPATH, "//input[@placeholder='Username, phone or email']").send_keys(username)
        print("Here 1111")
        # Locate password input similarly (use appropriate placeholder or other attribute)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        print("Here 2222")
        # Submit the form
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(Keys.RETURN)
        print("Here 3333")

        # Wait to ensure login success
        time.sleep(5)

        if "accounts" not in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed. Check credentials.")

    except Exception as e:
        print(f"Error during login: {e}")
        # print(User)
        # print(Pass)

def scrape_with_safari():
    username = "account"
    password = "passwords"

    # Login to Threads
    login_to_threads(username, password)

    # Scrape example URL
    driver.get("https://www.threads.net/t/C8CTu0iswgv")
    time.sleep(5)

    # Get page source
    page_source = driver.page_source
    print(page_source)

    driver.quit()

if __name__ == "__main__":
    scrape_with_safari()
