# !/usr/bin/env Rscript
# Created by: Mike Zhang
# Created on: 17/04/2019

library("ggpubr")

mydf <- read.csv("related.csv", sep=",")
print(mydf)

p <- ggscatter(mydf, x = "RAW_SRC", y = "REL_D",
    add = "reg.line",
    conf.int = TRUE,
    add.params = list(color = "blue", fill = "lightgray"),
    label = "PAIR",
    size = 1,
    title = "Best system vs. relative difference",
    xlab = "Score of the best system with original input",
    ylab = "Relative difference between WMT input and original input")

p2 <- p + grids(linetype = "dashed")
p2 + stat_cor(method = "pearson", label.x = 75, label.y = 12)

##############################

p <- ggscatter(mydf, x = "RAW_SRC", y = "ABS_D",
    add = "reg.line", conf.int = TRUE,
    add.params = list(color = "blue", fill = "lightgray"),
    label = "PAIR",
    size = 1,
    title = "Best system vs. absolute difference",
    xlab = "Score of the best system with original input",
    ylab = "Absolute difference between WMT input and original input")

p2 <- p + grids(linetype = "dashed")
p2 + stat_cor(method = "pearson", label.x = 75, label.y = 8)

##############################

p <- ggscatter(mydf, x = "SIM", y = "REL_D",
    add = "reg.line", conf.int = TRUE,
    add.params = list(color = "blue", fill = "lightgray"),
    label = "PAIR",
    size = 1,
    title = "LS vs. relative difference",
    xlab = "Similarity of the language pair using URIEL and lang2vec",
    ylab = "Relative difference between original input and source input")

p2 <- p + grids(linetype = "dashed")
p2 + stat_cor(method = "pearson", label.x = 0.6, label.y = 12)

###############################

p <- ggscatter(mydf, x = "SIM", y = "ABS_D",
    add = "reg.line", conf.int = TRUE,
    add.params = list(color = "blue", fill = "lightgray"),
    label = "PAIR",
    size = 1,
    title = "LS vs. absolute difference",
    xlab = "Similarity of the language pair using URIEL and lang2vec",
    ylab = "Absolute difference between original input and source input")

p2 <- p + grids(linetype = "dashed")
p2 + stat_cor(method = "pearson", label.x = 0.6, label.y = 8)