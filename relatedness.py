#!/usr/bin/env python3

# relatedness.py
# Mike Zhang
# 09-04-2019

def related(result, year, filename_lang, df):

    for tup in result.itertuples():
        if tup[1] == 'HUMAN' or (year == 'wmt16' or year == 'wmt17'):
            continue
        absdif = round(float(tup[2]) - float(tup[5]), 1)
        reldif = round(((float(tup[2]) - float(tup[5])) / ((float(tup[2]) + float(tup[5]))/ 2))*100, 1)
        if filename_lang not in df['PAIR']:
            df['PAIR'].append(filename_lang)
        else:
            continue
        df['RAW_SRC'].append(tup[5])
        df['ABS_D'].append(absdif)
        df['REL_D'].append(reldif)

    return df
