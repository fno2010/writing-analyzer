#!/usr/bin/env python
"""BibtexFetcher Class

Fetch bibtex from the given data source by the given pattern.
"""

import urllib2
import os
import nltk
from pyquery import PyQuery as pq

DEFAULT_BIB_URL_TEMPLATE = 'http://dblp.uni-trier.de/rec/bib1/%s.bib'
DEFAULT_BIB_URL_SELECTOR = """
#main ul.publ-list>li.entry.inproceedings,
#main ul.publ-list>li.entry.article
"""

DEFAULT_TITLE_SELECTOR = """
#main ul.publ-list>li.entry.inproceedings>div.data>span.title,
#main ul.publ-list>li.entry.article>div.data>span.title
"""

DEFAULT_BIB_CACHE_DIR = 'bib'

class BibtexFetcher:

    def __init__(self,
                 bib_url_template=DEFAULT_BIB_URL_TEMPLATE,
                 bib_url_selector=DEFAULT_BIB_URL_SELECTOR,
                 title_selector=DEFAULT_TITLE_SELECTOR,
                 bib_cache_dir=DEFAULT_BIB_CACHE_DIR):
        self.bib_url_template = bib_url_template
        self.bib_url_selector = bib_url_selector
        self.title_selector = title_selector
        self.bib_cache_dir = bib_cache_dir

    def fetchBibtex(self, url):
        """Fetch bibtex entries into the file

        url: the url of a dblp conference/journal homepage.
        """
        ext = '.bib'
        name = url.split('/')[-1].split('.')[0] + ext
        print 'Downloading %s -> file %s' % (url, name)

        page = pq(url=url,
                opener=lambda url, **kw: urllib2.urlopen(url).read())
        bibs = page(self.bib_url_selector)
        bib_urls = bibs.map(lambda i, e: self.bib_url_template % pq(e).attr('id'))

        with open(os.path.join(self.bib_cache_dir, name), 'w') as f:
            for bib_url in bib_urls:
                f.write(urllib2.urlopen(bib_url).read())
            f.close()

        print len(bib_urls), 'bib entries are written into the file.'

    def fetchBibtexs(self, urls):
        """Fetch bibtex entries from a list of urls"""
        if not os.path.exists(self.bib_cache_dir):
            os.mkdir(self.bib_cache_dir)
        print 'Downloading bibtex from:'
        for url in urls:
            self.fetchBibtex(url)

    def getTitles(self, url):
        """Extract title from url"""
        page = pq(url=url,
                opener=lambda url, **kw: urllib2.urlopen(url).read())
        titles = page(self.title_selector)
        return [pq(span).html() for span in titles]

    def getBatchTitles(self, urls):
        """Extract titles from a list of urls"""
        titles = []
        for url in urls:
            titles += self.getTitles(url)
        return titles

    def report(self, urls):
        titles = self.getBatchTitles(urls)
        try:
            nltk.word_tokenize('')
        except LookupError:
            nltk.download('punkt')

        length_hist = {}

        for title in titles:
            title_tokens = nltk.word_tokenize(title)
            length = len([token for token in title_tokens
                          if token not in ['.', ',', ':']])
            length_hist[length] = length_hist.get(length, 0) + 1

        return length_hist, len(titles)

    def plotLengthHist(self, urls):
        report = self.report(urls)
        length_hist = report[0]
        title_number = report[1]
        length_range = length_hist.keys()
        length_min = min(length_range)
        length_max = max(length_range)
        print '+--------+-------+------------+'
        print '| Length | Count | Percentage |'
        print '+--------+-------+------------+'
        total = 0
        for l in range(length_min, length_max + 1):
            count = length_hist.get(l, 0)
            total += count
            print '| %6d | %5d | %9.2f%% |' % (l, count,
                                               total * 100. / title_number)
            print '+--------+-------+------------+'

if __name__ == '__main__':
    sigcomm_url_pattern = 'http://dblp.uni-trier.de/db/conf/sigcomm/sigcomm%d.html'
    sigcomm_urls = [sigcomm_url_pattern % year for year in range(2012, 2017)]
    nsdi_url_pattern = 'http://dblp.uni-trier.de/db/conf/nsdi/nsdi%d.html'
    nsdi_urls = [nsdi_url_pattern % year for year in range(2012, 2018)]
    icnp_url_pattern = 'http://dblp.uni-trier.de/db/conf/icnp/icnp%d.html'
    icnp_urls = [icnp_url_pattern % year for year in range(2012, 2017)]
    urls = sigcomm_urls + nsdi_urls + icnp_urls
    for url in urls:
        print url
    fetcher = BibtexFetcher()
    fetcher.fetchBibtexs(urls)
