"""R19-1 driver: R18-1 Metropolis (copied mc.py), then per measurement: S matrix (as R18-1 run_mc.py) and f-sum matrix.
Usage: python3 run_fs.py L bU nequil nmeas every seed out [ksel: all|min]"""
import numpy as np, sys, time, pickle
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from mc import *
from fsum import fsum_meas, phase_table
L, bU, neq, nme, every, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
V = L**3; S, GE, GN = move_tables(L)
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
sweeps(n, g, L, 0.0, S, GE, GN, 50, seed + 7, 1)     # hot start (bU = 0 equilibrium), as R18-1
t0 = time.time(); Etr = []; nblk = 50; per = max(neq//nblk, 1)
for b in range(nblk):
    sweeps(n, g, L, bU, S, GE, GN, per, seed*1000 + b, b % 2); Etr.append((g**2).sum()/4/(3*V))
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        if m > 2 and L > 2: continue          # keep the two smallest |k| per direction (small-k behaviour)
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*np.array(v)/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T)); PH = phase_table(K, L)
nb_ = 20; Mb = np.zeros((nb_, len(klist), 6, 6), complex); Fb = np.zeros((nb_, len(klist), 6, 6), complex); Eb = np.zeros(nb_)
per_bin = max(nme//nb_, 1)
for b in range(nb_):
    for it in range(per_bin):
        sweeps(n, g, L, bU, S, GE, GN, every, seed*7919 + b*100003 + it, it % 2)
        F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph
        Mb[b] += np.einsum('ks,kt->kst', F.conj(), F)
        Mf = np.zeros((len(klist), 6, 6), complex); fsum_meas(n, g, L, bU, S, GE, GN, PH, Mf); Fb[b] += Mf
        Eb[b] += (g**2).sum()/4/(3*V)
    Mb[b] /= per_bin*V; Fb[b] /= per_bin*2*V; Eb[b] /= per_bin
assert np.array_equal(g, charges(n, L))
res = dict(L=L, bU=bU, klist=klist, K=K, Mb=Mb, Fb=Fb, Eb=Eb, Etr=np.array(Etr), secs=time.time() - t0, neq=neq, nme=nme, every=every, seed=seed)
pickle.dump(res, open(out, "wb"))
print("L=%d bU=%.2f seed=%d: E/edge trace %s ; meas %.5f +- %.5f ; %.1fs" % (L, bU, seed, np.round(np.array(Etr)[[0, nblk//4, nblk//2, -1]], 5),
      Eb.mean(), Eb.std()/np.sqrt(nb_), res['secs']), flush=True)
