import math
from math import log
from sklearn.metrics import log_loss

def log_p(w):
    e_w = math.exp(w)
    f = 1 / (1 + e_w)
    print('f=', f)


def kl_distance(w):
    f = 1 / (1 + math.exp(w))
    loss = f * (log(math.e, f)) + (1 - f) * log(math.e, (1 - f))
    print('loss=', loss)

kl_distance(0)

log_loss()