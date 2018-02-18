import sys, os
import numpy as np
sys.path.append(os.pardir)
from common.functions import softmax, cross_entropy_error
#from self.ch04_1_gradient import numerical_gradient
from common.gradient import numerical_gradient

class SimpleNet:
    def __init__(self, tmp=1):
        self.W = np.random.randn(2,3)
        print(tmp)

    def predict(self, x):
        return np.dot(x,self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

#net = SimpleNet(2)
net = SimpleNet()
print("weight value is : ")
print(net.W)
#print(net.W.shape)
#print(net.W.shape[0])
#print(net.W.shape[1])

x = np.array([0.6, 0.9])
p = net.predict(x)
#print(x[0])
print("input value is",x)
print("predicted value is", p)

t = np.array([0,0,1])
print("Answer label is ", t)
loss = net.loss(x, t)
print("CEE =",loss)

def f(w):
    return net.loss(x,t)
print(f(1))
print(f(10.0001))

dW = numerical_gradient(f,net.W)
print(dW)



