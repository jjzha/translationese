WMT18 Human evaluation data
------------------------------

The data contained in this package is provided for research purposes only and comes with no guarantee.

If using the following data, please cite the WMT'18 findings paper:
@InProceedings{bojar-EtAl:2018:WMT1,
  author    = {Bojar, Ondrej  and  Federmann, Christian  and  Fishel, Mark  and  Graham, Yvette  and  Haddow, Barry  and  Huck, Matthias  and  Koehn, Philipp  and  Monz, Christof},
  title     = {Findings of the 2018 Conference on Machine Translation (WMT18)},
  booktitle = {Proceedings of the Third Conference on Machine Translation, Volume 2: Shared Task Papers},
  month     = {October},
  year      = {2018},
  address   = {Belgium, Brussels},
  publisher = {Association for Computational Linguistics},
  pages     = {272--307},
  url       = {http://www.aclweb.org/anthology/W18-6401}
}

A main purpose of providing this data is to allow participants in the news shared task to verify results
for themselves and to provide data for developing better ways of ranking systems in future evaluations. 

The data included in this package was collected in one of the following ways:

(a) Crowd-sourced via Mechanical Turk using the standard Direct Assessment quality control mechanism -
A HIT consisted of 100 translations: 70 original system output translations, 10 repeats of those,
10 bad reference translations (each paired with one of the original 70), 10 human-produced reference
translations again (each paired with one of the original 70).

(b) Provided by researchers vi Appraise using the standard Direct Assessment quality control mechanism -
HIT structure the same as (a)

(c) Provided by researchers vi Appraise using an alternate Direct Assessment quality control mechanism - 
HIT structure consisted of 100 translations: 88 original system output translations and 12 bad reference 
(each paired with one of the original 88).

The main data files to look at are:

analysis/ad-latest.csv -- Contains all unfiltered data ~650k human judgments

analysis/ad-<source language><target language>-good-stnd-redup.csv 
-- eg analysis/ad-csen-good-stnd-redup.csv for czech to english
This file contains judgements from human judges who passed quality control, where scores are standardised
by that judge's mean and standard deviation score (computed over all the judgments they provided). This
is the basis of overall scores for systems. Overall scores for systems are calculate by computing
 a micro average over segments (eg analysis/ad-seg-scores-cs-en.csv) before an overall average per system 
(eg analysis/ad-sys-ranking-cs-en-z.csv).
Significance test results are in eg: analysis/ad-DA-diff-wilcoxon-rs-csen.csv

Questions please email graham.yvette@gmail.com or wmt-organisers@inf.ed.ac.uk 







