# GUIDE only: tau on S_1 (one message + free field) and decimated linear proxy at other beta.
import numpy as np, sys
exec(open('star2.py').read().split("z4 = np.zeros(4)")[0].replace("beta = float(sys.argv[1])", "beta = float(sys.argv[1])"))
from scipy.optimize import minimize
z4 = np.zeros(4); rng = np.random.default_rng(11)
def search(fun, n, trials, fev, f0=True):
    best = 0
    for _ in range(trials):
        p0 = rng.normal(size=4*n+4)*rng.uniform(0.1, 1.5)*beta
        def unpack(p):
            Gs = []
            for i in range(n):
                v = p[4*i:4*i+4]; r = np.linalg.norm(v); Gs.append(v if r <= 5*beta else v*5*beta/r)
            F0 = p[4*n:] if f0 else z4; r = np.linalg.norm(F0); F0 = F0 if r <= 6*beta else F0*6*beta/r
            return F0, Gs
        res = minimize(lambda p: -fun(*unpack(p)), p0, method='Powell', options={'maxfev': fev, 'xtol': 1e-3, 'ftol': 1e-8})
        best = max(best, -res.fun)
    return best
t = afun(np.array([beta]))[0]*beta
print(f"beta={beta}: t/4={t/4:.5f}  max tau on S_1 (field free) = {search(tau, 1, 6, 400):.5f}", flush=True)
mL = search(Lval, 6, 3, 400, f0=False)
print(f"beta={beta}: max L (n=6, F0=0) = {mL:.5f}  ratio to t/4 = {mL/(t/4):.4f}  30*beta*maxL = {30*beta*mL:.4f}", flush=True)
