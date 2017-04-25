#!/usr/bin/env python

# from optparse import OptionParser
from BibtexFetcher import BibtexFetcher

DATA_SOURCE = {
    # 'SIGCOMM': {
    #     'type': 'conf',
    #     'abbr': 'sigcomm',
    #     'range': range(2013, 2017)
    # },
    'NSDI': {
        'type': 'conf',
        'abbr': 'nsdi',
        'range': range(2014, 2015)
    },
    # 'ICNP': {
    #     'type': 'conf',
    #     'abbr': 'icnp',
    #     'range': range(2012, 2017)
    # },
    # 'Trans on Knowledge and Data Engineering': {
    #     'type': 'journals',
    #     'abbr': 'tkde',
    #     'range': range(24, 30)
    # },
    # 'Trans on Information Forensics and Security': {
    #     'type': 'journals',
    #     'abbr': 'tifs',
    #     'range': range(7, 13)
    # },
    # 'Trans on Software Engineering': {
    #     'type': 'journals',
    #     'abbr': 'tse',
    #     'range': range(38, 44)
    # },
    # 'Trans on Embedded Computing Systems': {
    #     'type': 'journals',
    #     'abbr': 'tecs',
    #     'range': range(11, 17)
    # },
}

def main():
    """Main function"""
    # TODO: add parser options
    # parser = OptionParser()

    # TODO: get options
    fetcher = BibtexFetcher()

    # all_urls = []
    for data_source, desp in DATA_SOURCE.items():
        print data_source + ':'
        urls = ['http://dblp.uni-trier.de/db/%s/%s/%s%d.html' % (desp['type'],
                                                                 desp['abbr'],
                                                                 desp['abbr'],
                                                                 index)
                for index in desp['range']]
        # fetcher.plotLengthHist(urls)
        fetcher.fetchBibtexs(urls)
        # all_urls += urls
    # print 'ALL:'
    # fetcher.plotLengthHist(all_urls)

if __name__ == '__main__':
    main()
