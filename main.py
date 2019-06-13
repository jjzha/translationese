#!/usr/bin/env python3

# main.py
# please see README.md
# Mike Zhang
# 14-01-2019

import os
import argparse
import pandas as pd
from segid import get_ids
from scores import score
from wilcoxon import changes
from relatedness import related

# file paths
files_seg = ['newstest2016-humaneval/analysis/', 'newstest2017-humaneval/analysis/', 'newstest2018-humaneval/analysis/']
files_id = ['test-wmt16/', 'test-wmt17/', 'test-wmt18/']


def main():

    # calculates the relatedness of language pairs, sends the data to a CSV for R usage.
    if args.related:
        # obtained from using lang2vec
        sim_dic = {'zhen': 0.47474157544924134, 'enzh': 0.47474157544924134,
                   'csen': 0.46244754746607586, 'encs': 0.46244754746607586,
                   'eten': 0.53552677878953870, 'enet': 0.53552677878953870,
                   'fien': 0.43609034102562430, 'enfi': 0.43609034102562430,
                   'deen': 0.75274736442567450, 'ende': 0.75274736442567450,
                   'ruen': 0.61155187271550440, 'enru': 0.61155187271550440,
                   'tren': 0.19756942534896915, 'entr': 0.19756942534896915
                   }
        df = {'PAIR': [], 'RAW_SRC': [], 'ABS_D': [], 'REL_D': []}
        f = open('related.csv', 'w')
        for path_seg, path_id in zip(files_seg, files_id):
            for filename in os.listdir(path_seg):
                filename_split = filename.split('-')
                if len(filename_split) > 2 and filename_split[-1].endswith('.csv') and filename_split[1] == 'seg':
                    filename_lang = ''.join(filename_split[3:5])
                    filename_lang = filename_lang[:4]
                    for testset in os.listdir(path_id):
                        testset_split = testset.split('-')
                        if filename_lang == testset_split[1] and testset_split[-1].startswith('src'):
                            src_ids, ref_ids = get_ids(path_id + testset, filename_split[-2])
                            result = score(path_seg + filename, src_ids, ref_ids, filename_lang, False)
                            related(result, path_id[5:10], filename_lang, df)
                        else:
                            pass
            else:
                pass

        dif_df = pd.DataFrame.from_dict(df)
        dif_df['SIM'] = dif_df['PAIR'].map(sim_dic)
        dif_df = dif_df.sort_values(by=['REL_D'], ascending=False).reset_index(drop=True)
        f.write(dif_df.to_csv(index=False))
        print('Written to file!')
        f.close()

    # loop through test data and human evaluation (DA) data.
    else:
        for path_seg, path_id in zip(files_seg, files_id):
            print('YEAR: ', path_id[5:10])
            for filename in os.listdir(path_seg):
                filename_split = filename.split('-')

                # align the language input with file names.
                if len(filename_split) > 2 and filename_split[-1].endswith('.csv') and filename_split[1] == 'seg':
                    filename_lang = ''.join(filename_split[3:5])
                    filename_lang = filename_lang[:4]
                    if filename_lang == args.language_pair:
                        for testset in os.listdir(path_id):
                            testset_split = testset.split('-')

                            # argparse options

                            # recomputes the wilcoxon rank sum test when data is split.
                            if args.language_pair and args.wilcoxon:
                                if filename_lang == testset_split[1] and testset_split[-1].startswith('src'):
                                    src_ids, ref_ids = get_ids(path_id+testset, filename_split[-2])
                                    df_final_both, df_final_src, df_final_ref, result_final, result_sid = \
                                        score(path_seg + filename, src_ids, ref_ids, filename_lang, args.wilcoxon)
                                    # result_sid.to_csv('wilcoxon_' + path_id[5:10] + '_' + args.language_pair + '.csv',
                                    #               sep='\t', encoding='utf-8', index=False)
                                    # print('Written to CSV file!')
                                    # print()
                                    changes(df_final_both, df_final_src, df_final_ref, filename_lang, path_id[5:10])
                                    print()
                                else:
                                    pass

                            # re-computes the DA scores with ORG and TRS subsets.
                            elif args.language_pair:
                                if filename_lang == testset_split[1] and testset_split[-1].startswith('src'):
                                    src_ids, ref_ids = get_ids(path_id+testset, filename_split[-2])
                                    result = score(path_seg + filename, src_ids, ref_ids, filename_lang, args.wilcoxon)
                                    print(result.to_latex(index=False))
                                    print()
                                else:
                                    pass
                            else:
                                pass
                    else:
                        pass
                else:
                    pass



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Translationese in the WMT')
    parser.add_argument('language_pair', nargs='?', default='', metavar='[preferred language pair]', type=str,
                        help='Abbreviation of language pair e.g. csen (Czech-English), will do all language'
                             ' pairs if no language pair is given.')
    parser.add_argument('-w', '--wilcoxon', action='store_true', help='Does the Wilcoxon Ranksum test for '
                                                                        'significance')
    parser.add_argument('-r', '--related', action='store_true', help='Answers Research Question 4 '
                        'about how much two languages are related. Used without the language pair argument.')
    args = parser.parse_args()

    main()
