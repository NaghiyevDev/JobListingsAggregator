# Job Listings Aggregator

The **Job Listings Aggregator** is a Python-based project that scrapes job listings from **Indeed** and **LinkedIn**. The project uses **Selenium** for web scraping and aggregates job data, including job titles, company names, locations, and salaries, which is then saved in a JSON file for further analysis.

## Project Structure

The project is organized as follows:

- `data/`: Directory where the scraped job listings data is saved.
  - `results.json`: Contains the aggregated job listings from both Indeed and LinkedIn.
  
- `src/`: Main source code of the project.
  - `scrapers/`: Contains scripts that scrape job data from different platforms.
    - `indeed_scraper.py`: Script to scrape job listings from Indeed.
    - `linkedin_scraper.py`: Script to scrape job listings from LinkedIn.
  - `utils/`: (Optional: Not specified in this setup, can be used for helper functions).
  - `main.py`: Main script to run the job aggregation process.
  
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `readme.md`: This file, describing the project, installation, and usage.

## Installation

To set up and run the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/JobListingsAggregator.git
   cd JobListingsAggregator

2. **Set up a virtual environment**:
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install required dependencies**:
   pip install -r requirements.txt

**Usage**

Running the Aggregator

1. Execute the main.py script:
   python src/main.py

2. Provide inputs when prompted:
  Job title/keyword: The position or keyword you are searching for (e.g., "Software Engineer").
  Job location: The city or region where you are looking for jobs (e.g., "New York").
  Number of pages to scrape: The number of pages of job listings to scrape from each platform.

Example input:
  Enter job title/keyword: Software Engineer
  Enter job location: San Francisco
  Enter number of pages to scrape: 2


**Scrapers**

**indeed_scraper.py**

This script scrapes job listings from Indeed using Selenium. It retrieves:
    Job title
    Company name
    Location
    Salary (if available)

It supports multiple pages of job listings by iterating through pagination links.


**linkedin_scraper.py**

This script scrapes job listings from LinkedIn using Selenium. It extracts:
    Job title
    Company name
    Location
    
The scraper also supports pagination, allowing you to scrape multiple pages of job listings.

**main.py**

The main.py script is the entry point of the project. It:
    Takes user inputs for the job title, location, and number of pages to scrape.
    Calls the scrape_indeed_jobs and scrape_linkedin_jobs functions to collect job listings.
    Saves the combined results in data/results.json.

**Requirements**

The following Python packages are required to run the project:  
    selenium: For automating the web browser and interacting with the websites.
    webdriver-manager: Automatically installs and manages the web driver needed by Selenium.
    json: For reading and writing data in JSON format.
    time: To control the speed of the scraper by adding delays between requests.

Install all dependencies by running:
    pip install -r requirements.txt


**Notes**

    Headless Browsing: The scrapers use headless browsing, meaning the browser runs in the background without a graphical interface, which helps speed up the scraping process.
    Rate Limiting: Be cautious of scraping too frequently. Websites like Indeed and LinkedIn may block requests if they detect too many hits from the same IP in a short time. Consider using a delay or rotating IPs in production.
    Web Scraping Ethics: Always respect the terms of service of the websites you are scraping. Use this tool responsibly to avoid overloading the servers of the scraped sites.


Created by ***Rashad Naghiyev***.
