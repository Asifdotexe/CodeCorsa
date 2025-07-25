import requests
from bs4 import BeautifulSoup

#TODO: Parse the job listing with Python count and also the number of applicants
#TODO: Implement pagination to scrape multiple pages of job listings
#TODO: Add temporal filtering to only see a timeframe's job listings

def create_linkedin_search_url(keywords: str, location: str) -> str:
    """
    Create a LinkedIn job search URL based on keywords and location.

    :param keywords: The job keywords to search for.
    :param location: The location to search in.
    :return: A formatted LinkedIn job search URL.
    """
    url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}"
    return url

search_keywords = "Python"
search_location = "India"

URL = create_linkedin_search_url(search_keywords, search_location)
print(f"Scraping URL: {URL}")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
else:
    print("Successfully fetched the page!")
    soup = BeautifulSoup(response.content, "html.parser")

    # --- NEW PARSING LOGIC STARTS HERE ---

    # Find all job card containers
    job_cards = soup.find_all('div', class_='base-card')

    print(f"Found {len(job_cards)} job cards.")

    # Loop through each job card and extract information
    for card in job_cards:
        # Extract Job Title
        title_tag = card.find('h3', class_='base-search-card__title')
        job_title = title_tag.text.strip() if title_tag else "N/A"

        # Extract Company Name
        company_tag = card.find('h4', class_='base-search-card__subtitle')
        company_name = company_tag.text.strip() if company_tag else "N/A"

        # Extract Location
        location_tag = card.find('span', class_='job-search-card__location')
        location = location_tag.text.strip() if location_tag else "N/A"

        # Extract Job Link
        link_tag = card.find('a', class_='base-card__full-link')
        job_link = link_tag['href'] if link_tag else "N/A"

        #TODO: Extract the number of applicants

        print("-" * 50)
        print(f"Title: {job_title}")
        print(f"Company: {company_name}")
        print(f"Location: {location}")
        print(f"Link: {job_link}")