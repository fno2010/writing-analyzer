#!/usr/bin/env python

import yaml
import pypandoc
import PaperAnalysis

DIR = '../samples/'

def main():
    papers = ['paper1-analysis.yml',
              'paper2-analysis.yml',
              'paper3-analysis.yml',
              'paper4-analysis.yml']
    for paper in papers:
        name = paper.split('.')[0]
        save_name = name + '.docx'
        print 'Loading data from', paper
        meta, body = PaperAnalysis.extract_content(DIR + paper)
        print ''
        print '---'
        print yaml.dump({'meta': meta})
        print '---'
        md = PaperAnalysis.export_markdown({'meta': meta, 'body': body})
        pypandoc.convert_text(md, 'docx', format='md', outputfile=save_name)

if __name__ == '__main__':
    main()
