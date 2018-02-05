'''
Created on 30-Jan-2018

@author: amuse
'''
from sklearn import datasets
import pandas as pd
from library import tree

def buildFeatures(data, labels, library=None, search=None):
    tree.buildFeatures(data, labels)

if __name__ == "__main__":
    dataset = datasets.load_iris()
    data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    labels = pd.Series(dataset.target)
    buildFeatures(data, labels)