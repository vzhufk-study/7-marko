# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 20.09.2017


import math
import numpy as np
from scipy import stats


class myRV(stats.rv_continuous):
    def _pdf(self, x, *args):
        return np.where(x < 0, [0.], [math.sqrt(2 / math.pi) * math.e ** (-x * x / 2)])

    def _stats(self):
        return 0., 0., 0., 0.

p = myRV()
print("Математичне сподівання: " + str(p.expect()))
print("Дисперсія: " + str(p.var()))
for i in range(0, 4):
    print("Момент " + str(i) + ": " + str(p.moment(i)))

print("Eнтропія: " + str(p.entropy()))
print("Стандартне відхилення: " + str(p.std()))

