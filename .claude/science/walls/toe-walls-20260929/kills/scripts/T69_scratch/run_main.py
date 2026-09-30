import numpy as np, json, time
from sea_stiffness import a2_bz, qlat2
res = {}
def kappa(N, m, mu, dim, d):
    a2, c0 = a2_bz(N, m, mu, dim, d)
    a20 = c0 / 4
    return 4 * (a2 - a20) / qlat2(N, m, dim, d), c0, a2

# ---- G1: 1D free sea, N large
g1 = []
for N, m in [(4096, 1), (4096, 2), (4096, 4), (4096, 8), (4096, 16)]:
    k, c0, _ = kappa(N, m, 0.0, 1, 'x')
    g1.append(dict(N=N, m=m, q=2*np.pi*m/N, kappa=k, c0=c0))
# Richardson in q^2 using m=8,16
q1, q2 = g1[3]['q']**2, g1[4]['q']**2
k_ex = (g1[3]['kappa']*q2 - g1[4]['kappa']*q1)/(q2-q1)
res['G1'] = dict(rows=g1, kappa_extrap=k_ex, target=1/(3*np.pi), c0=g1[0]['c0'], c0_target=-2/np.pi,
                 rel_kappa=abs(k_ex-1/(3*np.pi))/(1/(3*np.pi)), rel_c0=abs(g1[0]['c0']+2/np.pi)/(2/np.pi))
print('G1', res['G1'], flush=True)

# ---- 3D main: same physical q for growing N
t0 = time.time()
rows = []
for d in ['x', 'd']:
    for (N, m) in [(64, 2), (128, 4), (192, 6), (64, 4), (128, 8), (64, 8), (128, 16)]:
        k, c0, a2 = kappa(N, m, 0.0, 3, d)
        rows.append(dict(dir=d, N=N, m=m, q=2*np.pi*m/N, kappa=k, c0=c0))
        print(rows[-1], round(time.time()-t0,1), flush=True)
res['main3D'] = rows
json.dump(res, open('T69_results_main.json', 'w'), indent=1)
