# ABOUT

This repository contains supplementary material for the publication:

Mike Zhang, Antonio Toral. (2019). The Effect of Translationese in Machine Translation Test Sets. WMT19.

## General info:

There is one main script: `main.py`

Main script to run is `main.py`, this will compute the Direct Assessment  
scores using both languages as input, only the source language as input,  
and translationese as input.

## Command to run:

`python3 main.py` `[language pair]` `[-w]` `[-r]`

`[language pair]`: e.g. ruen (Russian-English), computes the DA scores of  
the systems using both languages as input, only the source language as in-  
put, and only translationese as input. Will compute for every WMT if the  
language pair exists.  
`[-w]`: Outputs a matrix using the Wilcoxon rank sum test, similar to the 
significance matrix of WMT.  
`[-r]`: Computates the relatedness of languages. After this ran, the command  
of: `Rscript related.R` should be run to obtain the plots.

## Possible language pairs:

#### WMT 2016

 * csen                    (Czech-English)
 * fien                    (Finnish-English)
 * deen                    (German-English)
 * roen                    (Romanian-English)
 * ruen                    (Russian-English)
 * tren                    (Turkish-English)

#### WMT 2017

 * zhen / enzh             (Chinese-English / English-Chinese)
 * csen / encs             (Czech-English   / English-Czech)
 * fien / enfi             (Finnish-English / English-Finnish)
 * deen / ende             (German-English  / English-German)
 * lven / enlv             (Latvian-English / English-Latvian)
 * ruen / enru             (Russian-English / English-Russian)
 * tren / entr             (Turkish-English / English-Turkish)

#### WMT 2018

 * zhen / enzh             (Chinese-English / English-Chinese)
 * csen / encs             (Czech-English   / English-Czech)
 * eten / enet             (Estonian-English/ English-Estonian)
 * fien / enfi             (Finnish-English / English-Finnish)
 * deen / ende             (German-English  / English-German)
 * ruen / enru             (Russian-English / English-Russian)
 * tren / entr             (Turkish-English / English-Turkish)

## Research Questions

RQ1. Does the use of translationese in the source side of MT test sets unfairly favour MT systems in general or is this just an artifact of the Chinese-to-English test set from WMT 2017?

RQ2. If the answer to RQ1 is yes, does this effect of translationese have an impact on WMT's system rankings? In other words, would removing the part of the test set that is translationese result in any change in the rankings?

RQ3. If the answer to RQ1 is yes, would some language pairs be more affected than others? E.g. based on the level of the relatedness between the two languages involved.
