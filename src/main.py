# main.py

import json
from scrapers.indeed_scraper import scrape_indeed_jobs
from scrapers.linkedin_scraper import scrape_linkedin_jobs

def save_to_file(data, filename="data/results.json"):
    """Saves scraped data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    """Main function to scrape job listings."""
    print("Starting Job Listings Aggregator...")
    
    query = input("Enter job title/keyword: ")
    location = input("Enter job location: ")
    pages = int(input("Enter number of pages to scrape: "))
    
    print("Scraping from Indeed...")
    indeed_jobs = scrape_indeed_jobs(query, location, pages)
    
    print("Scraping from LinkedIn...")
    linkedin_jobs = scrape_linkedin_jobs(query, location, pages)
    
    all_jobs = {"indeed": indeed_jobs, "linkedin": linkedin_jobs}
    save_to_file(all_jobs)
    print(f"Scraping completed. Data saved to data/results.json")

if __name__ == "__main__":
    main()
