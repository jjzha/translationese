#!/usr/bin/env python3

# segid.py
# This script is to split the original data from the translated data.
# Mike Zhang
# 12-01-2019

from bs4 import BeautifulSoup


def get_ids(file_test, lang):
    """this function splits the source language file sentence id from translationese id."""

    with open(str(file_test)) as f:
        soup = BeautifulSoup(f, 'lxml')
        for i, element in enumerate(soup.find_all('seg')):
            element['id']=str(i+1)

        only_src = []
        only_ref = []
        for element in soup.find_all('doc'):
            if element['origlang'] == lang:
                only_src.append(element.contents)
            else:
                only_ref.append(element.contents)

        only_src_ids = []
        only_ref_ids = []
        for item in only_src:
            p = item[1]
            for element in p.find_all('seg'):
                only_src_ids.append(element['id'])

        for item in only_ref:
            p = item[1]
            for element in p.find_all('seg'):
                only_ref_ids.append(element['id'])

        f.close()
        return only_src_ids, only_ref_ids
