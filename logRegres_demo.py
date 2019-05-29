#coding = utf-8

import numpy as np
import tensorflow as tf
import os

def dataset():
    datamat = [] ; labelmat = []
    fr = open("dataSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split()
        datamat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelmat.append(int(lineArr[2]))
    return datamat,labelmat

def sigmoid(x):
    return 1/(1+exp(-x))

def tanh(x):
    return (exp(x)-exp(-x))/(exp(x)+exp(-x))

def relu(x):
    return 0 if x<0 else x

def GradientDescent(datamat,classlabels):
    dataMatrix = mat(datamat)   
    labelMatrix = mat(classlabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    steps = 500
    w = ones((n,1))
    for i in range(steps):
        h=sigmoid(dataMatrix*w)
        error = labelMatirx - h
        w = w - alpha*dataMatrix.transpose()*error
    return w

def GradientAScent(datamat,classlabels):
    dataMatrix = mat(datamat)
    labelMatirx = mat(classlabels).transpose()
    m,n = shape(dataMatrix)
    steps = 500
    beta = 0.001
    w = ones((n,1))
    for i in range(beta):
         h = sigmoid(dataMatrix*w)
         error = labelMatrix - h
         w = w - beta*dataMatrix.transpose()*error
    return w


