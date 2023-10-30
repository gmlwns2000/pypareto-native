import os
import random, time
random.seed(42)

import pypareto

n_dim = 3
n_data = 5000
data = [tuple([random.random() for j in range(n_dim)]) for i in range(n_data)]

chain = pypareto.Comparison(pypareto.by_value, pypareto.MaxMinList(pypareto.MaxMin.MIN, pypareto.MaxMin.MIN, pypareto.MaxMin.MIN)).as_chain()
print('pareto start')
t = time.time()
result = chain.split_by_pareto(data)
print(result[-1])
print('pareto end', (time.time() - t) * 1000)

print('done')