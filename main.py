#!/usr/bin/env python3

# main.py
# please see README.md
# Mike Zhang
# 14-01-2019

import os
import argparse
import pandas as pd
from segid import get_ids, seg
from scores import score
from wilcoxon import changes
from relatedness import related
from langsim import langsim

# file paths
files_seg = ['newstest2016-humaneval/analysis/', 'newstest2017-humaneval/analysis/', 'newstest2018-humaneval/analysis/']
files_id = ['test-wmt16/', 'test-wmt17/', 'test-wmt18/']


def main():
    # loop through test data and human evaluation (DA) data.
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
                        # splits the segments into original and translationese of both source and reference.
                        # after this is done use the concat.py script.
                        if args.language_pair and args.segments:
                            if filename_lang == testset_split[1] and (testset_split[-1].startswith('src')):
                                seg(path_id + testset, filename_split[-2], 'src', path_id[5:10], filename_lang)
                            if filename_lang == testset_split[1] and (testset_split[-1].startswith('ref')):
                                seg(path_id + testset, filename_split[-2], 'ref', path_id[5:10], filename_lang)
                            else:
                                pass

                        # recomputes the wilcoxon rank sum test when data is split.
                        elif args.language_pair and args.wilcoxon:
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

                        # calculates the relatedness of language pairs, sends the data to a CSV for R usage.
                        elif args.language_pair and args.related:
                            df = {'PAIR': [], 'RAW_SRC': [], 'ABS_D': [], 'REL_D': []}
                            f = open('related.csv', 'w')
                            if filename_lang == testset_split[1] and testset_split[-1].startswith('src'):
                                src_ids, ref_ids = get_ids(path_id + testset, filename_split[-2])
                                result = score(path_seg + filename, src_ids, ref_ids, filename_lang, False)
                                related(result, path_id[5:10], filename_lang, df)
                                pd.set_option('display.expand_frame_repr', False)
                                sim_dic = langsim()
                                dif_df = pd.DataFrame.from_dict(df)
                                dif_df['SIM'] = dif_df['PAIR'].map(sim_dic)
                                dif_df = dif_df.sort_values(by=['REL_D'], ascending=False).reset_index(drop=True)
                                f.write(dif_df.to_csv(index=False))
                                f.close()

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
    parser.add_argument('-w', '--wilcoxon', action='store_true', help='Does the Wilcoxon Rank Sum test for '
                                                                        'significance')
    parser.add_argument('-r', '--related', action='store_true', help='Answers Research Question 4 '
                                                                        'about how much two languages are related')
    parser.add_argument('-s', '--segments', action='store_true', help='Aligns the data of source with reference.')
    args = parser.parse_args()

    main()