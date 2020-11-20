import pandas as pd

df_known = pd.read_csv("datas/name.basics.tsv.10k.tsv", sep='\t')

#----
df_crew = pd.read_csv("datas/title_crew10k.tsv", sep='\t')
df_crew2 = pd.read_csv("rendu/tcrew.tsv", sep='\t')
#----

def sep_KnownForTitle(data, namefile):
    
    data[["val1","val2","val3","val4"]] = data["knownForTitles"].str.split(",", expand=True ,n=3)
    data.to_csv("rendu/"+namefile + ".tsv",sep='\t', index=False)

# sep_KnownForTitle(df_known,"known2")
#________

df_crew[["w1","w2","w3","w4","w5"]] = df_crew["writers"].str.split(",", expand=True ,n=4)
df_crew2[["d1","d2","d3"]] = df_crew2["writers"].str.split(",", expand=True ,n=2)
#________

df_crew.to_csv("rendu/tcrew.tsv",sep='\t', index=False)
df_crew2.to_csv("rendu/tcrew2.tsv",sep='\t', index=False)
