import numpy as np, pickle
from walks import *
dat = pickle.load(open("nn_eqs_class0.pkl", "rb")); names, Bo = dat["names"], dat["B"].astype(float)
act = {"o00": 1, "o0i": 1j, "oi0": -1j, "oii": -1, "000": 1, "0ii": 1}
A = sum(v * Bo[names.index(k)] for k, v in act.items()) / 4
rng = np.random.default_rng(2)
for k in list(rng.uniform(-np.pi, np.pi, (4, 3))) + [np.array([0.3,0,0]), np.array([0.3,0.3,0.3])]:
    p = -np.angle(np.linalg.eigvals(symbol(A, k)))
    # candidate closed form: cos(omega) of dispersive bands vs products of cos(k_i/2)
    c = np.cos(k/2)
    print(np.round(k,3), "omega:", np.round(np.sort(p),5), " prod cos(k/2):", round(np.prod(c),5), " |c|:", np.round(c,4))
