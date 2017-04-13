#!/usr/bin/env python

# from optparse import OptionParser
from BibtexFetcher import BibtexFetcher

DATA_SOURCE = {
    # 'SIGCOMM': {
    #     'type': 'conf',
    #     'abbr': 'sigcomm',
    #     'range': range(2012, 2017)
    # },
    # 'NSDI': {
    #     'type': 'conf',
    #     'abbr': 'nsdi',
    #     'range': range(2012, 2018)
    # },
    # 'ICNP': {
    #     'type': 'conf',
    #     'abbr': 'icnp',
    #     'range': range(2012, 2017)
    # },
    'Trans on Knowledge and Data Engineering': {
        'type': 'journals',
        'abbr': 'tkde',
        'range': range(24, 30)
    },
    'Trans on Information Forensics and Security': {
        'type': 'journals',
        'abbr': 'tifs',
        'range': range(7, 13)
    },
    'Trans on Software Engineering': {
        'type': 'journals',
        'abbr': 'tse',
        'range': range(38, 44)
    },
    'Trans on Embedded Computing Systems': {
        'type': 'journals',
        'abbr': 'tecs',
        'range': range(11, 17)
    },
}

def main():
    """Main function"""
    # TODO: add parser options
    # parser = OptionParser()

    # TODO: get options
    fetcher = BibtexFetcher()

    # TODO: fetch the bibtex
    # sigcomm_url_pattern = 'http://dblp.uni-trier.de/db/conf/sigcomm/sigcomm%d.html'
    # sigcomm_urls = [sigcomm_url_pattern % year for year in range(2012, 2017)]
    # nsdi_url_pattern = 'http://dblp.uni-trier.de/db/conf/nsdi/nsdi%d.html'
    # nsdi_urls = [nsdi_url_pattern % year for year in range(2012, 2018)]
    # icnp_url_pattern = 'http://dblp.uni-trier.de/db/conf/icnp/icnp%d.html'
    # icnp_urls = [icnp_url_pattern % year for year in range(2012, 2017)]
    # urls = sigcomm_urls + nsdi_urls + icnp_urls

    # print 'SIGCOMM:'
    # fetcher.plotLengthHist(sigcomm_urls)
    # print 'NSDI:'
    # fetcher.plotLengthHist(nsdi_urls)
    # print 'ICNP:'
    # fetcher.plotLengthHist(icnp_urls)
    # print 'ALL:'
    # fetcher.plotLengthHist(urls)
    all_urls = []
    for data_source, desp in DATA_SOURCE.items():
        print data_source + ':'
        urls = ['http://dblp.uni-trier.de/db/%s/%s/%s%d.html' % (desp['type'],
                                                                 desp['abbr'],
                                                                 desp['abbr'],
                                                                 index)
                for index in desp['range']]
        fetcher.plotLengthHist(urls)
        all_urls += urls
    print 'ALL:'
    fetcher.plotLengthHist(all_urls)

if __name__ == '__main__':
    main()
