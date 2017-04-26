#!/usr/bin/env python

import yaml
import PaperAnalysis

DIR = '../samples/'

def main():
    papers = ['paper1-analysis.yml',
              'paper2-analysis.yml',
              'paper3-analysis.yml',
              'paper4-analysis.yml']
    for paper in papers:
        name = paper.split('.')[0]
        save_name = name + '-report.yml'
        print 'Loading data from', paper
        meta, body = PaperAnalysis.extract_content(DIR + paper)
        print ''
        print '---'
        print yaml.dump({'meta': meta})
        print '---'
        body_stat = PaperAnalysis.paper_statistics(body)
        PaperAnalysis.report_statistics(body_stat)
        print ''
        print 'Saving report to', save_name
        print ''
        with open(DIR + save_name, 'w') as f:
            yaml.dump({'meta': meta, 'body': body_stat}, f)

if __name__ == '__main__':
    main()
