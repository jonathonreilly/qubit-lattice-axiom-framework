"""R18-10 exact canonical statics via the N-biased GC chain, measuring ONLY at N_ab = V/2 (all six).
Usage: python3 run_bias.py L bU lam neq nme every seed out. Same measurement as run_c.py / R18-1 run_mc.py."""
import numpy as np, sys, time, pickle
from mc import *
from mc10 import counts
from mcpair import sweeps_bias
L, bU, lam, neq, nme, every, seed, out = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8]
V = L**3; S, GE, GN = move_tables(L); half = V//2
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L); t0 = time.time()
sweeps(n, g, L, 0.0, S, GE, GN, 50, seed + 7, 1)
Nc = counts(n); Etr = []
for b in range(50):
    sweeps_bias(n, g, Nc, L, bU, lam, half, S, GE, GN, max(neq//50, 1), seed*1000 + b, b % 2); Etr.append((g**2).sum()/4/(3*V))
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*v/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T))
nb_ = 20; Mb = np.zeros((nb_, len(klist), 6, 6), complex); Gb = np.zeros((nb_, len(klist))); Eb = np.zeros(nb_); cnt = np.zeros(nb_); EbGC = np.zeros(nb_)
per_bin = max(nme//nb_, 1); acc = []
for b in range(nb_):
    for it in range(per_bin):
        acc.append(sweeps_bias(n, g, Nc, L, bU, lam, half, S, GE, GN, every, seed*7919 + b*100003 + it, it % 2))
        EbGC[b] += (g**2).sum()/4/(3*V)
        if np.any(Nc != half): continue
        cnt[b] += 1
        F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph
        Mb[b] += np.einsum('ks,kt->kst', F.conj(), F)
        Fg = np.fft.fftn(g.astype(float)/2, axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T
        Gb[b] += (np.abs(Fg)**2).sum(1); Eb[b] += (g**2).sum()/4/(3*V)
    Mb[b] /= max(cnt[b], 1)*V; Gb[b] /= max(cnt[b], 1)*V; Eb[b] /= max(cnt[b], 1); EbGC[b] /= per_bin
assert np.array_equal(g, charges(n, L)) and np.array_equal(Nc, counts(n))
ok = cnt > 0
res = dict(L=L, bU=bU, lam=lam, klist=klist, K=K, Mb=Mb[ok], Gb=Gb[ok], Eb=Eb[ok], Etr=np.array(Etr), acc=float(np.mean(acc)),
           secs=time.time() - t0, neq=neq, nme=nme, every=every, init="bias%.2f" % lam, ncanon=int(cnt.sum()))
pickle.dump(res, open(out, "wb"))
print("bias L=%d bU=%.2f lam=%.2f: canonical samples %d of %d (bins used %d); E/edge canonical %.5f +- %.5f ; biased-all %.5f ; acc %.4f ; trace %s ; %.1fs" %
      (L, bU, lam, cnt.sum(), nb_*per_bin, ok.sum(), Eb[ok].mean(), Eb[ok].std()/np.sqrt(ok.sum()), EbGC.mean(), res['acc'],
       np.round(np.array(Etr)[[0, 25, -1]], 4), res['secs']), flush=True)
