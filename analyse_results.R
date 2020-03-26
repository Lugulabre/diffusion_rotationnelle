setwd("/Users/MAEL/Documents/M1_BI/Dynamique_moleculaire/projet/diffusion_rotationnelle")
data_prot = read.table("protein_result.txt")
data_h2o = read.table("h2o_result.txt")


plot(data_prot$V1, data_prot$V2, type = "l", col = "red",
     xlim = c(0,200), ylim = c(-0.2, 1.0),
     xlab = "temps")

lines(data_h2o$V2~data_h2o$V1, type = "l", col = "blue")
lines(exp(-data_prot$V1/18.70749066))
lines(exp(-data_prot$V1/0.0103079))
model = fit()
