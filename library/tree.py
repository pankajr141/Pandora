'''
Created on Feb 5, 2018

@author: 703188429
'''
import math
import numpy as np
import pandas as pd

def calculate_entropy(labels):
    entropy = 0 
    nclasses = len(labels.unique())
    if nclasses == 1:
        return 0
    for cls in labels.value_counts():
        pi = float(cls)/len(labels)
        entropycls = - pi * math.log(pi, nclasses)
        entropy = entropy + entropycls
    return entropy

def buildFeatures(data, labels):
    entropy_parent = calculate_entropy(labels)
    print("Parent Entropy:", entropy_parent)

    questions = []
    for column in data.columns:
        datapoints = np.unique(data[column].tolist())
        for datapoint in datapoints:
            questions.append([column, '=', datapoint])
            questions.append([column, '>=', datapoint])
            questions.append([column, '<=', datapoint])            
    
    information_gains = []
    for question in questions:
        column, operator, datapoint = question
        if operator == '=':    
            child1_indexes = data[data[column] == datapoint].index.tolist()
        elif operator == '>=':    
            child1_indexes = data[data[column] >= datapoint].index.tolist()
        elif operator == '<=':    
            child1_indexes = data[data[column] <= datapoint].index.tolist()
        child2_indexes = list(set(data.index) - set(child1_indexes))
        child1_labels = labels[child1_indexes]
        child2_labels = labels[child2_indexes]
        if not child1_indexes or not child2_indexes:
            continue
        child1_entropy = calculate_entropy(child1_labels)
        child2_entropy = calculate_entropy(child2_labels)
        #print(child1_entropy, child2_entropy)
        information_gain = entropy_parent - (child1_entropy + child2_entropy)
        information_gains.append([question, information_gain])
        #print(labels[child1_indexes])
    df = pd.DataFrame(data=information_gains, columns=['questions', 'information_gain'])
    df = df.sort(['information_gain'], ascending=False)
    print(df)
    #print(information_gains)