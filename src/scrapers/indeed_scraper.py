# indeed_scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_indeed_jobs(query, location, pages=1):
    """Scrapes job listings from Indeed using Selenium."""
    results = []
    # Set up Chrome options for headless browsing
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headlessly (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    for page in range(pages):
        url = f"https://www.indeed.com/jobs?q={query}&l={location}&start={page*10}"
        driver.get(url)
        time.sleep(3)  # Wait for the page to load fully
        
        # Get the job elements
        job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
        print(f"Found {len(job_cards)} job listings on page {page + 1}")

        for job_card in job_cards:
            try:
                # Correct usage of By.CLASS_NAME
                title = job_card.find_element(By.CLASS_NAME, "jobTitle").text.strip()
                print('Job title:', title)

                company = job_card.find_element(By.CLASS_NAME, "companyName").text.strip()
                location = job_card.find_element(By.CLASS_NAME, "companyLocation").text.strip()

                # Salary is not always present
                try:
                    salary = job_card.find_element(By.CLASS_NAME, "salary-snippet").text.strip()
                except:
                    salary = "N/A"

                results.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "salary": salary,
                })
            except Exception as e:
                print(f"Error extracting job details: {e}")

    driver.quit()
    return results
