#!/usr/bin/env python

import re
# import json
import yaml
import nltk
from nltk.parse.stanford import StanfordParser, StanfordDependencyParser

parser = StanfordParser()
dep_parser = StanfordDependencyParser()

convert = {
    "VB": "SP",
    "VBD": "SD",
    "VBN": "SD"
}

keywords = ["will", "would", "have", "has", "had", "am", "is", "are"]


def paper_statistics(body):
    for section in body.keys():
        for paragraph in body[section]:
            sents = [re.sub(" *\[[ ,\d]+\]", "", s['content'])
                     for s in paragraph['content']]
            clauses_counts = sentences_clauses(sents)
            sents_triples = sentences_triples(sents)
            tenses = sentences_tense(sents_triples)
            modals_info = sentences_pos_count(sents_triples, 'aux', 'MD')
            sents_length = sentences_length(sents)
            for i in range(len(sents)):
                paragraph['content'][i]['clauses'] = clauses_counts[i]
                paragraph['content'][i]['tense'] = tenses[i]
                paragraph['content'][i]['modal_count'] = modals_info[i][0]
                paragraph['content'][i]['modals'] = modals_info[i][1]
                paragraph['content'][i]['length'] = sents_length[i]
    return body

def report_statistics(body):
    for section in body.keys():
        print section
        print '------------------------------------------------------------------------------------------'
        print 'Para | Sent | Move-Step | Signal Word | Length | Clauses | Conj. | Tense | Passive | Modal'
        for paragraph in body[section]:
            print '------------------------------------------------------------------------------------------'
            print paragraph['paragraph_no']
            for sentence in paragraph['content']:
                print '%11d | %9s | %11s | %6d | %7d | %5s | %5s | %7s | %d (%s)' \
                        % (sentence['sentence_no'],
                        sentence['move'],
                        sentence.get('signal_word', '-'),
                        sentence.get('length', '-'),
                        sentence.get('clauses', '-'),
                        sentence.get('conj', '-'),
                        sentence.get('tense', '-'),
                        sentence.get('passive', '-'),
                        sentence.get('modal_count', 0),
                        ', '.join(sentence.get('modals', [])))
        print '------------------------------------------------------------------------------------------'

def sentences_length(sents):
    return [sentence_length(sent) for sent in sents]

def sentence_length(sent):
    sent_tokens = nltk.word_tokenize(sent)
    return len([token for token in sent_tokens
                if token not in ['.', ',', ':', '(', ')', ';', "'", '-', '--']])

def sentences_clauses(sents):
    trees = [r.next().pformat().split() for r in parser.raw_parse_sents(sents)]
    return [t.count("(SBAR") + t.count("(SBARQ") + 1 for t in trees]

def sentence_clauses(sent):
    return sentences_clauses([sent])[0]

def sentences_triples(sents):
    return [[tr for tr in trs.next().triples()] for trs in dep_parser.raw_parse_sents(sents)]

def sentences_tense(sents_triples):
    return [sentence_tense(st) for st in sents_triples]

def sentence_tense(sent_triples):
    # sent_triples = list(dep_parser.raw_parse(sent).next().triples())
    filt_pair = [(x[0][1], x[2][0] if x in keywords else x[2][1] ) for x in sent_triples if x[0][1][:1] == 'V' and (x[2][1][:1] == 'V' or x[2][0] in keywords)]
    filt_verb = [x[0][1] for x in sent_triples if x[0][1][:1] == 'V']
    if not filt_pair:
        if not filt_verb:
            return "SP"
        else:
            return convert.get(filt_verb[0], "SP")
    else:
        values = dict(filt_pair).values()
        if ("will" in values or "would" in values) and ("have" in values):
            return "PF"
        elif "had" in values:
            return "PD"
        elif "have" in values and "has" in values:
            return "PP"
        elif ("VBG", "will") in filt_pair:
            return "GF"
        elif ("VBG", "VBD") in filt_pair:
            return "GD"
        elif "will" in values:
            return "SF"
        elif ("VBG", "am") in filt_pair or ("VBG", "is") in filt_pair or ("VBG", "are") in filt_pair:
            return "GP"
        else:
            return "SP"

def sentences_pos_count(sents_triples, relation, pos):
    return [sentence_pos_count(sent_triples, relation, pos)
            for sent_triples in sents_triples]

def sentence_pos_count(sent_triples, relation, pos):
    filt_triples = [tr for tr in sent_triples
                       if tr[1] == relation and tr[2][1] == pos]
    return len(filt_triples), list(set([tr[2][0] for tr in filt_triples]))

def word_concordance(triples, word, part):
    re_triples = [tr for tr in triples]
    filt_begin = [x[2] for x in re_triples if x[0][0] == word]
    filt_end = [x[0] for x in re_triples if x[2][0] == word]
    filt_triples = filt_begin + filt_end
    filt_words = [x[0] for x in filt_triples]
    filt_parts = [x[1] for x in filt_triples]
    if part == "NN" or "NNP":
        return (
            filt_words.count("the") + filt_words.count("The"),
            filt_words.count("a") + filt_words.count("A") + filt_words.count("an") + filt_words.count("An"),
            len([x for x in filt_parts if x[:1] == "V"]),
            filt_parts.count("JJ")
        )
    elif part == "VI":
        return (
            len([x for x in filt_begin if x[1] == "IN"]),
            len([x for x in filt_begin if x[1] == "RB"])
        )
    elif part == "VT":
        return (
            len([x for x in filt_begin if x[1] == "NN"]),
            len([x for x in filt_begin if x[1] == "VBG"])
        )
    elif part == "JJ":
        return (
            len(filt_end),
            len(filt_begin)
        )
    elif part == "RB":
        return (
            len(filt_begin),
            len([x for x in filt_end if x[1][:1] == "V"]),
            len([x for x in filt_end if x[1][:2] == "JJ"])
        )
    elif part == "PRP":
        return len(filt_triples)
    elif part == "MD":
        return (
            len([x for x in filt_parts if x[:2] == "RB"]),
            len([x for x in filt_parts if x[:1] == "V"])
        )


def extract_content(filename):
    data = yaml.load(open(filename, 'rb'))
    meta = data['meta']
    body = data['body']
    return meta, body

# FIXME: Deprecated
def tense_statistics(papers):
    for stat in papers:
        for sec in stat.keys():
            for mark in stat[sec].keys():
                stat[sec][mark]["tense"] = {
                    "SP": 0,
                    "SD": 0,
                    "SF": 0,
                    "GP": 0,
                    "GD": 0,
                    "GF": 0,
                    "PP": 0,
                    "PD": 0,
                    "PF": 0
                }
                for sent in stat[sec][mark]["content"]:
                    stat[sec][mark]["tense"][sentence_tense(sent)] += 1

# FIXME: Deprecated
def clause_satistics(papers):
    for stat in papers:
        for sec in stat.keys():
            for mark in stat[sec].keys():
                stat[sec][mark]["clause"] = 0
                for sent in stat[sec][mark]["content"]:
                    stat[sec][mark]["clause"] = sentence_clauses(sent)

def display_content(paper, section):
    print '\n'.join([' '.join([s['content']+' ('+s['move']+')' for s in p]) for p in paper['body'][section]])

def export_markdown(paper):
    title = paper['meta']['title']
    authors = paper['meta']['author']
    authors_str = ', '.join(authors[:-1]) + ' and ' + authors[-1] if len(authors) > 1 else authors[-1]
    body = ''
    for sec in paper['body'].keys():
        body += sec.upper() + '\n\n'
        for para in paper['body'][sec]:
            body += '\\'
            body += ' '.join(['(%d) %s' % (s['sentence_no'], s['content']) for s in para['content']])
            body += '\n\n'
    return '%%%s\n%%%s\n\n%s' % (title, authors_str, body)
