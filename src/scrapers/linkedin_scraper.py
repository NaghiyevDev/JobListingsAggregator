# linkedin_scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_linkedin_jobs(query, location, pages=1):
    """Scrapes job listings from LinkedIn using Selenium."""
    results = []
    
    # Set up Chrome options for headless browsing
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headlessly (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for page in range(pages):
        url = f"https://www.linkedin.com/jobs/search?keywords={query}&location={location}&start={page*25}"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load fully
        
        # Get the job elements
        job_cards = driver.find_elements(By.CLASS_NAME, "result-card")
        print(f"Found {len(job_cards)} job listings on page {page + 1}")

        for job_card in job_cards:
            title = job_card.find_element(By.CLASS_NAME, "result-card__title").text.strip()
            company = job_card.find_element(By.CLASS_NAME, "result-card__subtitle").text.strip()
            location = job_card.find_element(By.CLASS_NAME, "job-result-card__location").text.strip()
            
            results.append({
                "title": title,
                "company": company,
                "location": location
            })

    driver.quit()
    return results
