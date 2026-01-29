from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_website():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://quotes.toscrape.com/tag/humor/"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".quote"))
        )
        quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
    except Exception as e:
        print("Error:", e)
        driver.quit()
        return []

    scraped_data = []

    for q in quotes:
        text = q.find_element(By.CSS_SELECTOR, ".text").text
        author = q.find_element(By.CSS_SELECTOR, ".author").text
        tags = [t.text for t in q.find_elements(By.CSS_SELECTOR, ".tag")]
        author_url = q.find_element(By.CSS_SELECTOR, "span a").get_attribute("href")

        scraped_data.append({
            "text": text,
            "author": author,
            "tags": tags,
            "author_url": author_url,
            "page_url": url,
        })

    driver.quit()
    return scraped_data
