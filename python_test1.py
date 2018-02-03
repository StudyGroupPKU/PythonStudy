import numpy as np

def sample_data(n_samples=1000, maxval=1, n=1):
        vectors = []
        for i in range(n_samples):
                #subvector = []
                #for j in range(0,n):
                val = np.random.random(n) *  maxval;
                #       subvector.append(val)
                #print (val)
                vectors.append(val)
        return np.array(vectors)

data_train = sample_data(10,1,2)
print(data_train)
