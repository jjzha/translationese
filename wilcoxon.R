#!/usr/bin/env Rscript
# This script is to computate the WMT18 way of clustering.
# Mike Zhang


# Data
files = list.files(path="wilcoxon/", pattern=".+csv", full.names=TRUE)
for (f in files) {
  mydf <- read.csv(f, sep="\t")
  cou = gsub(".+([a-z]{2})[a-z]{2}\\.csv", "\\1", f)
  trs = gsub(".+[a-z]{2}([a-z]{2})\\.csv", "\\1", f)
  df <- mydf[mydf$LANG==cou,]
  dftrs <- mydf[mydf$LANG==trs,]
  
  #averages
  
  s_avg <- aggregate( mydf$RAW.SCR ~ mydf$SYS + mydf$SID, FUN = mean )
  names(s_avg) <- c("SYS", "SID", "RAW.SCR")
  zs_avg <- aggregate( mydf$Z.SCR ~ mydf$SYS + mydf$SID, FUN = mean )
  names(zs_avg) <- c("SYS", "SID", "Z.SCR")

  s_avg_cou <- aggregate( df$RAW.SCR ~ df$SYS + df$SID, FUN = mean)
  names(s_avg_cou) <- c("SYS", "SID", "RAW.SCR")
  zs_avg_cou <- aggregate( df$Z.SCR ~ df$SYS + df$SID, FUN = mean)
  names(zs_avg_cou) <- c("SYS", "SID", "Z.SCR")

  s_avg_trs <- aggregate( dftrs$RAW.SCR ~ dftrs$SYS + dftrs$SID, FUN = mean)
  names(s_avg_trs) <- c("SYS", "SID", "RAW.SCR")
  zs_avg_trs <- aggregate( dftrs$Z.SCR ~ dftrs$SYS + dftrs$SID, FUN = mean)
  names(zs_avg_trs) <- c("SYS", "SID", "Z.SCR")

## Original Scores

s_sys <- aggregate(s_avg$RAW.SCR ~ s_avg$SYS, FUN = mean )
names(s_sys) <- c("SYS", "RAW.SCR")

s_sys_cou <- aggregate(s_avg_cou$RAW.SCR ~ s_avg_cou$SYS, FUN = mean )
names(s_sys_cou) <- c("SYS", "RAW.SCR")

s_sys_trs<- aggregate(s_avg_trs$RAW.SCR ~ s_avg_trs$SYS, FUN = mean )
names(s_sys_trs) <- c("SYS", "RAW.SCR")

# print(f)

for (sys1 in unique(zs_avg$SYS)) {
  for (sys2 in unique(zs_avg$SYS)) {
    if (identical(sys1, sys2)) {
      next
    }

# Wilcoxon rank-sum
print(paste("Comparing: ", sys1, sys2, sep=" "))
res = wilcox.test(zs_avg_trs$Z.SCR[zs_avg_trs$SYS==sys1], zs_avg_trs$Z.SCR[zs_avg_trs$SYS==sys2], conf.int=TRUE, alternative = "greater")

# 2018 metrics
if (identical("wmt18", gsub(".+(wmt[0-9]{2}).+", "\\1", f))) {
    score = abs(mean(zs_avg_trs$Z.SCR[zs_avg_trs$SYS==sys2]) - mean(zs_avg_trs$Z.SCR[zs_avg_trs$SYS=="HUMAN"])) - abs(mean(zs_avg_trs$Z.SCR[zs_avg_trs$SYS==sys1]) - mean(zs_avg_trs$Z.SCR[zs_avg_trs$SYS=="HUMAN"]))
    if (res$p.value < 0.001) {
      print(paste(round(score,2),'***',sep=""))
    } else if (res$p.value < 0.01) {
      print(paste(round(score,2),'**',sep=""))
    } else if (res$p.value < 0.05) {
      print(paste(round(score,2),'*',sep=""))
    } else {
      print(round(score,2))
    }
  } else {
  print(paste("p:", res$p.value, sep=" "))
}
    }
  }
}
print('wilcoxon')
