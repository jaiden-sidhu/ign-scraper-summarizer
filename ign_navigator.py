from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from web_scraper import *

def perform_search(url, search_term):
    print("Opening IGN...")
    driver_path = 'chromedriver-win64\chromedriver.exe'
    service = Service(driver_path)
    
    # Initialize the Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Does not open window on PC, uncomment when complete
    options.add_argument('--disable-gpu')  # Disable GPU acceleration
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-dev-shm-usage')  # Bypasses any "low resource" errors
    options.add_argument('--disable-extensions')  # Disable extensions
    options.add_argument('--disable-infobars')  # Disable infobars
    options.add_argument('--log-level=3')  # Making Python shut up
    options.add_argument('--silent')  # Making ChromeDriver shut up

    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Opening the given URL
        driver.get(url)

        # Wait for the search button to be clickable and click it
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Search"]'))).click()

        # Wait for the input field to be visible
        print("Searching for game...")
        search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'term')))
        search_input.clear()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

        # 1 second is usually best for waiting for the search results to load
        time.sleep(1)

        # Putting the search results div into a variable
        search_results_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.jsx-337130575.jsx-4243969252.search-results'))
        )

        # Check if it contains text saying "No results."
        if "No results." in search_results_div.text:
            print("Error: No results found.")
        else:
            # Find the first link in the search results and clicking on it
            print("Navigating to game page...")
            first_result_link = search_results_div.find_element(By.TAG_NAME, 'a')
            first_result_link.click()

            print("Navigating to game review...")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.stack.jsx-2736506000.analytic-with-text-box.ign-rating'))).click()
            time.sleep(3)

            print("Extracting game verdict...")
            return extract_verdict_text(driver.current_url)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # finally:
        driver.quit()

# Testing
# url = "https://ign.com" 
# search_term = "sndiabdiobasodbsaiodbioa"
# perform_search(url, search_term)