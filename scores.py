#!/usr/bin/env python3

# scores.py
# This file creates the pandas dataframes for comparing scores.
# Mike Zhang
# 12-01-2019

import pandas as pd


def score(file_seg, src_ids, ref_ids, lang, wilcoxon):
    """imports data from CSV files, and puts it in a pandas dataframe, calculates score for different input"""

    with open(file_seg) as file_seg:
        df = pd.read_csv(file_seg, sep=' ', usecols=['SYS','SID','RAW.SCR','Z.SCR','N'])
        dic_both = {'SYS':[], 'RAW.BOTH':[], 'Z.BOTH':[]}
        dic_src = {'SYS':[], 'RAW.SOURCE':[], 'Z.SOURCE':[]}
        dic_ref = {'SYS':[], 'RAW.TRANS':[], 'Z.TRANS':[]}
        systems = df.SYS.unique()

        for system in systems:
            dic_both['SYS'].append(system)
            raw_both_score = df.loc[df['SYS'] == system, 'RAW.SCR'].mean() # raw score
            dic_both['RAW.BOTH'].append(raw_both_score)
            z_both_score = df.loc[df['SYS'] == system, 'Z.SCR'].mean() # z score
            dic_both['Z.BOTH'].append(z_both_score)

        df_src = df.loc[df['SID'].isin(src_ids)] # get only scores with id in src
        for system in systems:
            dic_src['SYS'].append(system)
            raw_src_score = df_src.loc[df_src['SYS'] == system, 'RAW.SCR'].mean() # raw score
            dic_src['RAW.SOURCE'].append(raw_src_score)
            z_src_score = df_src.loc[df_src['SYS'] == system, 'Z.SCR'].mean() # z score
            dic_src['Z.SOURCE'].append(z_src_score)

        df_ref = df.loc[df['SID'].isin(ref_ids)] # get only scores with id in ref
        for system in systems:
            dic_ref['SYS'].append(system)
            raw_ref_score = df_ref.loc[df_ref['SYS'] == system, 'RAW.SCR'].mean() # raw score
            dic_ref['RAW.TRANS'].append(raw_ref_score)
            z_ref_score = df_ref.loc[df_ref['SYS'] == system, 'Z.SCR'].mean() # z score
            dic_ref['Z.TRANS'].append(z_ref_score)

        df_final_both = pd.DataFrame.from_dict(dic_both)
        df_final_src = pd.DataFrame.from_dict(dic_src)
        df_final_ref = pd.DataFrame.from_dict(dic_ref)

        if wilcoxon:
            pd.options.mode.chained_assignment = None
            result_final = pd.merge(df_final_both, df_final_src, on='SYS')
            df_src['LANG'] = lang[0:2]
            df_ref['LANG'] = lang[2:]
            result_sid = pd.concat([df_src,df_ref])
            return df_final_both, df_final_src, df_final_ref , result_final, result_sid

        else:
            # print('LANGUAGE: ', lang)
            both = df_final_both.sort_values(by=['Z.BOTH'], ascending=False).reset_index(drop=True)
            source = df_final_src.sort_values(by=['Z.SOURCE'], ascending=False).reset_index(drop=True)
            ref = df_final_ref.sort_values(by=['Z.TRANS'], ascending=False).reset_index(drop=True)

            joined = pd.concat([both, source, ref], axis = 1, join='inner')
            decimals = pd.Series([1, 3, 1, 3, 1, 3], index=['RAW.BOTH', 'Z.BOTH', 'RAW.SOURCE', 'Z.SOURCE',
                                                            'RAW.TRANS', 'Z.TRANS'])
            result = joined.round(decimals)

        return result
