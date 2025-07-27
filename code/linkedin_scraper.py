import pandas as pd
import requests
from bs4 import BeautifulSoup

#TODO: Parse the job listing with Python count and also the number of applicants
#TODO: Implement pagination to scrape multiple pages of job listings
#TODO: Add temporal filtering to only see a timeframe's job listings
#TODO: Figure out a constant day to fetch the results every month

def scrape_linkedin_jobs(keywords: str, location: str, past: str = None) -> pd.DataFrame:
    """
    Create a LinkedIn job search URL based on keywords and location.

    :param keywords: The job keywords to search for.
    :param location: The location to search in.
    :param past: Optional; a string to filter jobs by time (e.g., "day", "week", "month").
    :return: A dataframe containing job listings
    """
    search_url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}"

    # Map user-friendly arguments to LinkedIn's URL parameters.
    # These values were found by observing the "f_TPR" (Filter-Time Posted Range)
    # parameter in the URL when using the "Date Posted" filter on LinkedIn.
    # The number represents the duration in seconds.
    # 'day': 24 hours * 60 minutes * 60 seconds = 86,400
    # 'week': 7 days * 86,400 seconds/day = 604,800
    # 'month': 30 days * 86,400 seconds/day = 2,592,000
    time_filters = {'day': "r86400",
                    'week': "r604800",
                    'month': "r2592000"}

    # If a past filter is provided, append it to the search URL.
    if past and past.lower() in time_filters:
        search_url += f"&f_TPR={time_filters[past.lower()]}"
    print(search_url)