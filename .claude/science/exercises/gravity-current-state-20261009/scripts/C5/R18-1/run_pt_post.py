"""R18-1 PT with post-selection: also accumulates S(k) over every replica state with sum gamma^2 = 0 exactly
(at any ladder point; the conditional law given gamma = 0 is uniform on the gamma = 0 states of the coset = the bU = infinity
ensemble, provided the finite-bU chain is equilibrated). Based on the parallel-tempering driver (replica exchange in bU) for the slow large-bU regime.
Usage: python3 run_pt.py L bmin bmax dlow dhigh nequil nmeas every seed out
Ladder: arange(bmin, 3, dlow) + arange(3, bmax+eps, dhigh). Swaps between neighbours (alternating parity) each PT sweep.
Measures at ladder points nearest to the targets {1,1.5,2,2.5,3,3.5,4,4.5,5,6}. Hot start (bU=0 equilibrium)."""
import numpy as np, sys, time, pickle
from mc import *
L, bmin, bmax, dlo, dhi = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
neq, nme, every, seed, out = int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9]), sys.argv[10]
V = L**3; S, GE, GN = move_tables(L); rng = np.random.default_rng(seed)
betas = np.concatenate([np.arange(bmin, 3.0 - 1e-9, dlo), np.arange(3.0, bmax + 1e-9, dhi)]); R = len(betas)
targets = [b for b in [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6] if bmin - 1e-9 <= b <= bmax + 1e-9]
tidx = sorted(set(int(np.argmin(np.abs(betas - b))) for b in targets))
ns = []; gs = []
for r in range(R):
    n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
    sweeps(n, g, L, 0.0, S, GE, GN, 30, seed*100 + r, 1); ns.append(n); gs.append(g)
perm = np.arange(R)          # perm[slot] = replica index sitting at betas[slot]
rep_dir = np.zeros(R, int); trips = 0; rep_last = -np.ones(R, int)
swap_try = np.zeros(R - 1); swap_acc = np.zeros(R - 1)
def E(r): return (gs[r]**2).sum()/4.0
def pt_sweep(it, k):
    global trips
    for s in range(R):
        r = perm[s]; sweeps(ns[r], gs[r], L, betas[s], S, GE, GN, k, seed*1000003 + it*R + s, (it + s) % 2)
    for s in range(it % 2, R - 1, 2):
        r1, r2 = perm[s], perm[s + 1]; d = (betas[s + 1] - betas[s])*(E(r2) - E(r1))
        swap_try[s] += 1
        if d >= 0 or rng.random() < np.exp(d):
            perm[s], perm[s + 1] = r2, r1; swap_acc[s] += 1
    # round trips: replica reaching top after bottom
    for s_end, lab in [(0, 1), (R - 1, 2)]:
        r = perm[s_end]
        if rep_last[r] != lab:
            if rep_last[r] == 1 and lab == 2: trips += 1
            rep_last[r] = lab
t0 = time.time()
for it in range(neq): pt_sweep(it, 1)
teq = time.time() - t0
kd = kgrid_dirs(L); klist = [(name, m, v) for name, lst in kd.items() for m, vecs in lst for v in vecs]
K = np.array([2*np.pi*v/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T)); nb_ = 20; per_bin = max(nme//nb_, 1)
Mb = {s: np.zeros((nb_, len(klist), 6, 6), complex) for s in tidx}; Gb = {s: np.zeros((nb_, len(klist))) for s in tidx}
Eb = np.zeros((nb_, R)); trips0 = trips
PM = np.zeros((len(klist), 6, 6), complex); PG = np.zeros(len(klist)); npost = 0; seen = set()
for b in range(nb_):
    for it in range(per_bin):
        pt_sweep(neq + b*per_bin + it, every)
        for s in range(R): Eb[b, s] += E(perm[s])/(3*V)
        for r in range(R):
            if E(r) == 0:
                F = np.fft.fftn(ns[r].astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T*ph
                PM += np.einsum('ks,kt->kst', F.conj(), F)/V; npost += 1; seen.add(hash(ns[r].tobytes()))
        for s in tidx:
            r = perm[s]
            F = np.fft.fftn(ns[r].astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T*ph
            Mb[s][b] += np.einsum('ks,kt->kst', F.conj(), F)
            Fg = np.fft.fftn(gs[r].astype(float)/2, axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T
            Gb[s][b] += (np.abs(Fg)**2).sum(1)
    for s in tidx: Mb[s][b] /= per_bin*V; Gb[s][b] /= per_bin*V
    Eb[b] /= per_bin
for r in range(R): assert np.array_equal(gs[r], charges(ns[r], L))
for s in tidx:
    res = dict(L=L, bU=float(betas[s]), klist=klist, K=K, Mb=Mb[s], Gb=Gb[s], Eb=Eb[:, s], Etr=Eb[:, s], acc=float('nan'),
               secs=time.time() - t0, neq=neq, nme=nme, every=every, init="PT")
    pickle.dump(res, open(out + "_b%.2f.pkl" % betas[s], "wb"))
pickle.dump(dict(L=L, bU=np.inf, klist=klist, K=K, Mb=(PM/max(npost, 1))[None], Gb=np.zeros((1, len(klist))), Eb=np.zeros(1), Etr=np.zeros(3), acc=float("nan"), secs=0, neq=neq, nme=nme, every=every, init="post", npost=npost, ndistinct=len(seen)), open(out + "_post.pkl", "wb"))
print("post-selected gamma=0 samples: %d (distinct configurations %d)" % (npost, len(seen)))
np.save(out + "_ladder.npy", np.vstack([betas, Eb.mean(0), Eb.std(0)/np.sqrt(nb_)]))
print("L=%d PT: R=%d replicas, betas %.2f..%.2f, equil %d + meas %d PT sweeps (every %d), %.0fs (equil %.0fs)" %
      (L, R, betas[0], betas[-1], neq, nme, every, time.time() - t0, teq))
print("  swap acceptance min %.3f mean %.3f ; round trips total %d (during measurement %d)" %
      ((swap_acc/np.maximum(swap_try, 1)).min(), (swap_acc/np.maximum(swap_try, 1)).mean(), trips, trips - trips0))
for s in range(R):
    print("  bU=%.3f E/edge=%.5f +- %.5f%s" % (betas[s], Eb[:, s].mean(), Eb[:, s].std()/np.sqrt(nb_), "  *measured" if s in tidx else ""))
