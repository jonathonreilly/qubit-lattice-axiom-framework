"""R18-10 planar stress test driver. Usage: L bU neq nme seed out. Prepares a state with every conserved planar count
at L^2/2 (drive_all_planar at bU = 0), then runs sweeps_planar; measurement identical to run_c.py."""
import numpy as np, sys, time, pickle
from mc import *
from mc10 import counts
from mcplanar import sweeps_planar, drive_all_planar
L, bU, neq, nme, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
V = L**3; S, GE, GN = move_tables(L); t0 = time.time()
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); sweeps(n, g, L, 0.0, S, GE, GN, 50, seed, 1)
obj = -1; it = 0
while obj != 0 and it < 2000:
    obj = drive_all_planar(n, g, L, 0.0, S, GE, GN, 2, seed + 10 + it, it % 2); it += 1
if obj != 0: print("PLANAR DRIVE FAILED, objective", obj); sys.exit(1)
Etr = []
for b in range(50):
    sweeps_planar(n, g, L, bU, S, GE, GN, max(neq//50, 1), seed*1000 + b, b % 2); Etr.append((g**2).sum()/4/(3*V))
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*v/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T))
nb_ = 20; Mb = np.zeros((nb_, len(klist), 6, 6), complex); Gb = np.zeros((nb_, len(klist))); Eb = np.zeros(nb_); acc = []
per_bin = max(nme//nb_, 1)
for b in range(nb_):
    for it2 in range(per_bin):
        a, f = sweeps_planar(n, g, L, bU, S, GE, GN, 1, seed*7919 + b*100003 + it2, it2 % 2); acc.append((a, f))
        F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph
        Mb[b] += np.einsum('ks,kt->kst', F.conj(), F)
        Fg = np.fft.fftn(g.astype(float)/2, axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T
        Gb[b] += (np.abs(Fg)**2).sum(1); Eb[b] += (g**2).sum()/4/(3*V)
    Mb[b] /= per_bin*V; Gb[b] /= per_bin*V; Eb[b] /= per_bin
assert np.array_equal(g, charges(n, L)) and np.array_equal(counts(n), np.full(6, V//2))
acc = np.array(acc)
res = dict(L=L, bU=bU, klist=klist, K=K, Mb=Mb, Gb=Gb, Eb=Eb, Etr=np.array(Etr), acc=float(acc[:, 0].mean()), secs=time.time() - t0, init="planar")
pickle.dump(res, open(out, "wb"))
print("planar L=%d bU=%.2f: drive blocks %d; E/edge trace %s ; meas %.5f +- %.5f ; acc %.4f ; planar-filter pass %.4f ; %.1fs" %
      (L, bU, it, np.round(np.array(Etr)[[0, 25, -1]], 4), Eb.mean(), Eb.std()/np.sqrt(nb_), acc[:, 0].mean(), acc[:, 1].mean(), res['secs']), flush=True)
