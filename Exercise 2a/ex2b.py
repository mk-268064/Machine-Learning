import pandas as pd
import numpy as np
data=pd.DataFrame(data=pd.read_csv('data.csv'))
concepts=np.array(data.iloc[:,:-1])
print("concepts=",concepts)
target=np.array(data.iloc[:,-1])
print("target:",target)
def learn(concepts,target):
    spec_h=concepts[0].copy()
    print("initialization of specific and general_h")
    print("specific_h=",spec_h)
    general_h=[["?" for i in range(len(spec_h))]for i in range(len(spec_h))]
    print("general_h",general_h)
    for i,h in enumerate(concepts):
        if target[i]=="yes":
            for x in range(len(spec_h)):
                if h[x]!= spec_h[x]:
                     spec_h='?'
                     general_h[x][x]='?'
        if target[i]=="no":
             for x in range(len(spec_h)):
                if h[x]!= spec_h[x]:
                     general_h[x][x]=spec_h
                else:
                    general_h[x][x]='?'
        indices=[i for i,val in  enumerate(general_h) if val==['?','?','?','?','?']]
        for i in indices:
            general_h.remove(['?','?','?','?','?'])
        return spec_h,general_h
s_final,g_final=learn(concepts,target)
print("final specfic_h",s_final,sep="\n")
print("final general_h",g_final,sep="\n")