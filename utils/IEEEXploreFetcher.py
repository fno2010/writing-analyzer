#!/usr/bin/env python
"""IEEEXploreFetcher Class

Fetch metadata and full text of papers from ieeexplore.ieee.org.
"""

from selenium import webdriver
from pyquery import PyQuery as pq

class IEEEXploreFetcher():
    """A web fetcher for papers in ieeexplore.ieee.org."""

    def __init__(self):
        # TODO: Initiate attributes
        pass

    def fetchFullText(self, arnumbers):
        """Fetch full text by the given article number."""
        if type(arnumbers) != list:
            arnumbers = [arnumbers]
        browser = webdriver.Chrome()
        articles = []
        for num in arnumbers:
            browser.get("http://ieeexplore.ieee.org/xpls/icp.jsp?arnumber=" + str(num))
            # TODO: Ensure the page load is ready
            page = pq(browser.page_source)
            articles.append(page('div#article'))
        browser.quit()
        return articles

    def convertToJson(self, article):
        """Convert the html format of the article to JSON."""
        json_obj = {}
        for sec in article.children('div.section'):
            sec('div.section')
            # TODO: Format each section
        return json_obj

    def report(self):
        # TODO: Generate the report
        pass
