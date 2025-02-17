import pandas as pd
import numpy as np

data = pd.read_csv(".\data.csv")
print(data)
label_copy = data.copy()
data = np.array(data)[:,:-1]
print(data)
label = np.array(label_copy)[:,-1:]
label = [x[0] for x in label]
print(label)

def s_algo(data,label):
    hypothesis = data[0].copy()

    for i in range(1,len(data)):
        if label[i]=='yes':
            for j in range(len(hypothesis)):
                if hypothesis[j] != data[i][j]:
                    hypothesis[j] = '?'
    return hypothesis

result = s_algo(data,label)
print("The Hypothesis is: ",result) 
