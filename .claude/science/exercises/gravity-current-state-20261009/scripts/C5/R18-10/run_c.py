"""R18-10 driver. Usage: python3 run_c.py L bU neq nme every bprep ensemble seed out
ensemble = 'C' (dipole-conserving, mode 0, sector N_ab = V/2) or 'GC' (R18-1 chain, no filter; reference).
Preparation: n = 0 -> 50 GC sweeps at bU = 0 -> 200 GC sweeps at bprep -> (C only) drive at bprep until
sum|N_ab - V/2| = 0 -> neq sweeps of the production chain at bU -> nme measurements every `every` sweeps
(sweep length alternates by one move). Measurement identical to R18-1 run_mc.py (same k list, same Mb/Gb)."""
import numpy as np, sys, time, pickle
from mc import *
from mc10 import sweeps_c, counts
from mcpair import sweeps_pair
L, bU, neq, nme, every = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
bprep, ens, seed, out = float(sys.argv[6]), sys.argv[7], int(sys.argv[8]), sys.argv[9]
V = L**3; S, GE, GN = move_tables(L); half = V//2
import os
if os.environ.get('EXT') == '1':
    from ext import move_tables_ext
    S2, GE2, GN2 = move_tables_ext(L)
else:
    S2, GE2, GN2 = S, GE, GN
n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
t0 = time.time()
INIT = sys.argv[10] if len(sys.argv) > 10 else None
if INIT:
    n = np.load(INIT).astype(np.int64); g = charges(n, L)
else:
    sweeps(n, g, L, 0.0, S, GE, GN, 50, seed + 7, 1)
    sweeps(n, g, L, bprep, S, GE, GN, 200, seed + 11, 1)
Nc = counts(n); fl = np.zeros_like(n); dsw = 0
if ens in ("C", "P"):
    while np.abs(Nc - half).sum() > 0 and dsw < 2000:
        sweeps_c(n, g, Nc, L, bprep, S, GE, GN, 1, seed + 13 + dsw, dsw % 2, 1, half, fl); dsw += 1
    assert np.array_equal(Nc, counts(n))
    if np.abs(Nc - half).sum() > 0: print("DRIVE FAILED", Nc - half); sys.exit(1)
def step(ns, sd, ex):
    if ens == "C":
        return sweeps_c(n, g, Nc, L, bU, S2, GE2, GN2, ns, sd, ex, 0, half, fl)
    if ens == "P":
        a = sweeps_pair(n, g, L, bU, S, GE, GN, ns, sd, ex); return (a, 1.0)
    a = sweeps(n, g, L, bU, S, GE, GN, ns, sd, ex); return (a, 1.0)
Etr = []; nblk = 50; per = max(neq//nblk, 1)
for b in range(nblk):
    step(per, seed*1000 + b, b % 2); Etr.append((g**2).sum()/4/(3*V))
fl[:] = 0
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*v/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T))
nb_ = 20; Mb = np.zeros((nb_, len(klist), 6, 6), complex); Gb = np.zeros((nb_, len(klist))); Eb = np.zeros(nb_); acc = []; fil = []
per_bin = max(nme//nb_, 1)
for b in range(nb_):
    for it in range(per_bin):
        a, f = step(every, seed*7919 + b*100003 + it, it % 2); acc.append(a); fil.append(f)
        F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph
        Mb[b] += np.einsum('ks,kt->kst', F.conj(), F)
        Fg = np.fft.fftn(g.astype(float)/2, axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T
        Gb[b] += (np.abs(Fg)**2).sum(1)
        Eb[b] += (g**2).sum()/4/(3*V)
    Mb[b] /= per_bin*V; Gb[b] /= per_bin*V; Eb[b] /= per_bin
assert np.array_equal(g, charges(n, L)) and (ens == "GC" or np.array_equal(counts(n), np.full(6, half)))
res = dict(L=L, bU=bU, klist=klist, K=K, Mb=Mb, Gb=Gb, Eb=Eb, Etr=np.array(Etr), acc=float(np.mean(acc)), filt=float(np.mean(fil)),
           secs=time.time() - t0, neq=neq, nme=nme, every=every, init="%s_prep%.2f" % (ens, bprep), N=counts(n), flipped=float(fl.mean()),
           drive_sweeps=dsw, ens=ens)
pickle.dump(res, open(out, "wb")); np.save(out.replace(".pkl", "_final.npy"), n.astype(np.int8))
print("%s L=%d bU=%.2f prep=%.2f drive=%d: E/edge trace %s ; meas %.5f +- %.5f ; acc %.4f filt-pass %.4f ; flipped %.4f ; N-V/2 %s ; %.1fs" %
      (ens, L, bU, bprep, dsw, np.round(np.array(Etr)[[0, nblk//4, nblk//2, -1]], 5), Eb.mean(), Eb.std()/np.sqrt(nb_), res['acc'], res['filt'],
       res['flipped'], res['N'] - half, res['secs']), flush=True)
