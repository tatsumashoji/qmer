#if (!requireNamespace("BiocManager", quietly = TRUE))
#    install.packages("BiocManager")
#BiocManager::install("edgeR")

library(edgeR)

count <- read.csv("count_table.csv", header=T, row.names=1)
group <- factor(c(rep("A", 17), rep("B", 19)))

design <- model.matrix(~ group)

d <- DGEList(counts = count, group = group)
d <- calcNormFactors(d)
d <- estimateDisp(d, design)
fit <- glmFit(d, design)
lrt <- glmLRT(fit, coef = 2)

table <- as.data.frame(topTags(lrt, n=nrow(count)))
write.table(table, file = "dge_result.csv", col.names=T, row.names=T, sep=",")

# Volcano plot
pdf(file="dge_volcano_plot.pdf", height=as.integer(5), width=as.integer(7))

with(table, plot(logFC, -log10(PValue), pch=20, main="Volcano plot", cex=.5, xlim=c(-5,5), ylim=c(0,7), xaxt="n", yaxt="n", col="black"))

axis(side=1, at=c(-4,-2,0,2,4))
axis(side=2, at=c(0,2,4,6,8))

with(subset(table, FDR<.1 ), points(logFC, -log10(PValue), pch=20, cex=.25, col="green"))
with(subset(table, abs(logFC)>1), points(logFC, -log10(PValue), pch=20, cex=.25, col="orange"))
with(subset(table, FDR<.1 & abs(logFC)>1), points(logFC, -log10(PValue), pch=20, cex=.5, col="red"))

dev.off()
