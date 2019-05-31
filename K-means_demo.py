# coding:utf-8

import numpy as np
import tensorflow as tf
import math

def data_set(filename):
    dataMat =[]
    fp = open(filename)
    for line in fp.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def EuclidDistrance(vecA, vecB):
    return math.sqrt(sum(pow(vecA-vecB,2)))

def randCent(dataSet, k):
    n = tf.shape(dataSet)[1]
    centroid = np.mat(tf.zeros(k, n))
    for j in range(n):
        minJ = min(dataSet[:,j]- minJ)
        rangeJ = float(max(dataSet[:, j]-minJ))
        centroid[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroid

