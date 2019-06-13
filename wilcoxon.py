#!/usr/bin/env python3

# wilcoxon.py
# Mike Zhang
# 02-03-2019

import pandas as pd
import re

def changes(both, src , tra, lang, year):

    print('LANGUAGE: ', lang)
    both = both.sort_values(by=['Z.BOTH'], ascending=False)
    src = src.sort_values(by=['Z.SOURCE'], ascending=False)
    trans = tra.sort_values(by=['Z.TRANS'], ascending=False)
    both_copy = pd.DataFrame(data=None, index=both['SYS'], columns=both['SYS'])
    src_copy = pd.DataFrame(data=None, index=src['SYS'], columns=src['SYS'])
    tra_copy = pd.DataFrame(data=None, index=trans['SYS'], columns=trans['SYS'])

    print()
    print('WMT INPUT')
    with open('original_input.txt') as f:
        for line in re.findall(year+'_'+lang+'.csv(.*?)wilcoxon',f.read(), re.S):
            line = line.replace('[1]','').replace('"', '').strip().split('\n')
            it = iter(line)
            for systems in it:
                sys = systems.split()[1:]
                value = next(it).split()[-1]
                if '*' not in value:
                    value = float(value)
                both_copy.at[sys[0],sys[1]] = value
                both_copy = both_copy.fillna('-')
            if 'HUMAN' in both_copy:
                both_copy = both_copy.drop(index='HUMAN', columns='HUMAN')

        print(both_copy.round(5))

    f.close()

    print()
    print('ONLY ORIGINAL INPUT')
    with open('source_input.txt') as f:
        for line in re.findall(year+'_'+lang+'.csv(.*?)wilcoxon',f.read(), re.S):
            line = line.replace('[1]','').replace('"', '').strip().split('\n')
            it = iter(line)
            for systems in it:
                sys = systems.split()[1:]
                value = next(it).split()[-1]
                if '*' not in value:
                    value = float(value)
                src_copy.at[sys[0],sys[1]] = value
                src_copy = src_copy.fillna('-')
            if 'HUMAN' in src_copy:
                src_copy = src_copy.drop(index='HUMAN', columns='HUMAN')

        print(src_copy.round(5))

    f.close()

    print()
    print('ONLY TRANSLATIONESE INPUT')
    with open('trans_input.txt') as f:
        for line in re.findall(year+'_'+lang+'.csv(.*?)wilcoxon',f.read(), re.S):
            line = line.replace('[1]','').replace('"', '').strip().split('\n')
            it = iter(line)
            for systems in it:
                sys = systems.split()[1:]
                value = next(it).split()[-1]
                if '*' not in value:
                    value = float(value)
                tra_copy.at[sys[0],sys[1]] = value
                tra_copy = tra_copy.fillna('-')
            if 'HUMAN' in tra_copy:
                tra_copy = tra_copy.drop(index='HUMAN', columns='HUMAN')

        print(tra_copy.round(5))

    f.close()
