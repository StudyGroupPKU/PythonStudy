import sys, os
sys.path.append(os.pardir)
import numpy as np
from self.ch04_3_TwoLayerNet import TwoLayerNet
from dataset.mnist import load_mnist


network = TwoLayerNet(784,100,10)

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

train_loss_list=[]

iter_num = 2
train_size = x_train.shape[0]
batch_size = 5
learning_rate = 0.1

for i in range(iter_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print(i+1,"th")
    grad = network.numerical_gradient2(x_batch, t_batch)

    for key in ('W1','b1','W2','b2'):
        network.params[key] = network.params[key] - learning_rate * grad[key]
#        print("!!!",network.params['W1'].shape)

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

print(train_loss_list)  
