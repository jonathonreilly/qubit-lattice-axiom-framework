"""R18-1 MC driver: equilibrate, measure the 6x6 slot structure-factor matrices M(k) and S_gamma(k) along the
axis/face/body directions (all cubic copies), binned. Usage: python3 run_mc.py L bU nequil nmeas every init seed out"""
import numpy as np, sys, time, pickle
from mc import *
L, bU, neq, nme, every = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
init, seed, out = sys.argv[6], int(sys.argv[7]), sys.argv[8]
V = L**3; S, GE, GN = move_tables(L)
rng = np.random.default_rng(seed)
if init == "cold":
    n = np.zeros((6, L, L, L), dtype=np.int64)
elif init == "hot":
    n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
    sweeps(n, g, L, 0.0, S, GE, GN, 50, seed + 7, 1)      # bU = 0 equilibrium start
else:
    n = np.load(init).astype(np.int64)
g = charges(n, L)
t0 = time.time(); Etr = []
nblk = 50; per = max(neq//nblk, 1)
for b in range(nblk):
    a = sweeps(n, g, L, bU, S, GE, GN, per, seed*1000 + b, b % 2); Etr.append((g**2).sum()/4/(3*V))
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*v/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T))           # (nk, 6) slot offset phases
nb_ = 20; Mb = np.zeros((nb_, len(klist), 6, 6), complex); Gb = np.zeros((nb_, len(klist))); Eb = np.zeros(nb_); acc = []
per_bin = max(nme//nb_, 1)
for b in range(nb_):
    for it in range(per_bin):
        acc.append(sweeps(n, g, L, bU, S, GE, GN, every, seed*7919 + b*100003 + it, it % 2))
        F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph   # (nk, 6)
        Mb[b] += np.einsum('ks,kt->kst', F.conj(), F).real*0 + np.einsum('ks,kt->kst', F.conj(), F)
        Fg = np.fft.fftn(g.astype(float)/2, axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T
        Gb[b] += (np.abs(Fg)**2).sum(1)
        Eb[b] += (g**2).sum()/4/(3*V)
    Mb[b] /= per_bin*V; Gb[b] /= per_bin*V; Eb[b] /= per_bin
assert np.array_equal(g, charges(n, L))
res = dict(L=L, bU=bU, klist=klist, K=K, Mb=Mb, Gb=Gb, Eb=Eb, Etr=np.array(Etr), acc=float(np.mean(acc)),
           secs=time.time() - t0, neq=neq, nme=nme, every=every, init=init)
pickle.dump(res, open(out, "wb")); np.save(out.replace(".pkl", "_final.npy"), n.astype(np.int8))
print("L=%d bU=%.2f init=%s: E/edge equil-trace %s ; meas %.5f +- %.5f ; acc %.4f ; %.1fs" %
      (L, bU, init, np.round(np.array(Etr)[[0, nblk//4, nblk//2, -1]], 5), Eb.mean(), Eb.std()/np.sqrt(nb_), res['acc'], res['secs']), flush=True)
