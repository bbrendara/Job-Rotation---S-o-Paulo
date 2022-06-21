SP=67836.43
RJ=36678.66
MG=29229.88
ES=27165.48
OUTROS=19849.53

valortotal=SP+RJ+MG+ES+OUTROS
print (" \n \nFaturamento mensal: R$",valortotal)

perSP=(SP*100)/valortotal
print("\nPercentual representação SP:",perSP,"%")

perRJ=(RJ*100)/valortotal
print("\nPercentual representação RJ:",perRJ,"%")

perMG=(MG*100)/valortotal
print("\nPercentual representação MG:",perMG,"%")

perES=(ES*100)/valortotal
print("\nPercentual representação ES:",perES,"%")

perOUTROS=(OUTROS*100)/valortotal
print("\nPercentual representação Outros estados:",perOUTROS,"% \n")

