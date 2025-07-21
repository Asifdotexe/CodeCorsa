import requests
from bs4 import BeautifulSoup


def create_linkedin_search_url(keywords: str, location: str) -> str:
    """
    Create a LinkedIn job search URL based on keywords and location.

    :param keywords: The job keywords to search for.
    :param location: The location to search in.
    :return: A formatted LinkedIn job search URL.
    """
    url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}"
    return url