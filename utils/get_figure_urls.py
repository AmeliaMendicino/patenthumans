"""
A script to grab all of the figure image URLs for patents from Google Patents
when a newline delimited list of patent IDs is piped in.
"""

import sys
import time
import requests
from lxml import html

WAIT_TIME = 0.5
GOOGLE_PATENTS_URL = 'https://patents.google.com/patent/'
FIGURE_XPATH = '//meta[@itemprop="full"]/@content'

for patentNumber in sys.stdin:
    # Wait a little bit so we don't get blocked for scraping
    time.sleep(WAIT_TIME)

    patentPage = GOOGLE_PATENTS_URL + patentNumber.strip()
    page = requests.get(patentPage)
    tree = html.fromstring(page.content)

    # Grab the full sized images from the page
    figures = tree.xpath(FIGURE_XPATH)
    for url in figures:
        print (url)
