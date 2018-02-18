import sys, os
import numpy as np
from ch04_3_TwoLayerNet import TwoLayerNet

Net = TwoLayerNet(784,100,10)
#print(Net.params['W1'].shape)

x = np.random.randn(10,784)
t = np.random.randn(10,10)
#print(x.shape)
print('t shape',t.shape)
y = Net.predict(x)
print('y shape',y.shape)

grads = Net.numerical_gradient2(x,t)
print('W1',grads['W1'].shape)
print('b1',grads['b1'].shape)
print('W2',grads['W2'].shape)
print('b2',grads['b2'].shape)


