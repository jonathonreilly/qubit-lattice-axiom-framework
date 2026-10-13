"""R18-10 run_ptb: EXACT-canonical PT = run_ptc with each replica running the N-biased GC chain (mcpair.sweeps_bias, lam = 0.3);
measurements only when that replica has N_ab = V/2 (all six). The bias is the same function of N in every replica, so the swap
ratio is exp((b_i-b_j)(E_i-E_j)) exactly. Original run_ptc docstring follows.
R18-10 canonical parallel tempering (dipole-conserving chain, mode 0, every replica in the SAME start state's
communicating class, which is bU-independent because the filter is bU-independent and every filtered move has
positive probability at finite bU). Swaps between neighbouring bU accept with min(1, exp((b_i-b_j)(E_i-E_j))),
E = sum gamma^2; this preserves the product of the restricted Boltzmann measures (detailed balance).
Usage: python3 run_ptc.py L bmax nrep nsweep_eq nsweep_meas start(hot|cold) seed tag [resume.npz]
Measures (R18-1 observables) at the replicas whose bU is in TARGETS. Tracks round trips of the replica labels."""
import numpy as np, sys, time, pickle
from mc import *
from mc10 import sweeps_c, counts
from mcpair import sweeps_bias
LAM = 0.3
L, bmax, nrep, neq, nme = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
start, seed, tag = sys.argv[6], int(sys.argv[7]), sys.argv[8]
resume = sys.argv[9] if len(sys.argv) > 9 else None
V = L**3; S, GE, GN = move_tables(L); half = V//2
import os; betas = np.linspace(float(os.environ.get("BMIN", "0")), bmax, nrep)
TARGETS = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
tidx = [int(np.argmin(np.abs(betas - t))) for t in TARGETS if np.min(np.abs(betas - t)) < 1e-9]
t0 = time.time(); rng = np.random.default_rng(seed)
if resume:
    z = np.load(resume); ns = [z['n'][r].astype(np.int64) for r in range(nrep)]; lab = z['lab']; dirn = z['dirn']; trips = z['trips']
else:
    n = np.zeros((6, L, L, L), dtype=np.int64); g = charges(n, L)
    sweeps(n, g, L, 0.0, S, GE, GN, 50, seed + 7, 1)
    bprep = 0.0 if start == "hot" else 3.0
    sweeps(n, g, L, bprep, S, GE, GN, 300, seed + 11, 1)
    Nc = counts(n); fl = np.zeros_like(n); dsw = 0
    while np.abs(Nc - half).sum() > 0 and dsw < 3000:
        sweeps_c(n, g, Nc, L, bprep, S, GE, GN, 1, seed + 13 + dsw, dsw % 2, 1, half, fl); dsw += 1
    pass
    print("start=%s prepared at bU=%.1f, drive sweeps %d, E/edge %.4f" % (start, bprep, dsw, (g**2).sum()/4/(3*V)), flush=True)
    ns = [n.copy() for r in range(nrep)]; lab = np.arange(nrep); dirn = np.zeros(nrep, int); trips = np.zeros(nrep, int)
    dirn[0] = 1; dirn[-1] = -1
gs = [charges(x, L) for x in ns]; Ncs = [counts(x) for x in ns]; fls = [np.zeros_like(x) for x in ns]
kd = kgrid_dirs(L); klist = []
for name, lst in kd.items():
    for m, vecs in lst:
        for v in vecs: klist.append((name, m, v))
K = np.array([2*np.pi*v/L for _, _, v in klist]); idx = np.array([np.mod(v, L) for _, _, v in klist])
ph = np.exp(-1j*(K @ OFFS.T))
nb_ = 20; per_bin = max(nme//nb_, 1)
Mb = {r: np.zeros((nb_, len(klist), 6, 6), complex) for r in tidx}; Gb = {r: np.zeros((nb_, len(klist))) for r in tidx}
Eb = {r: np.zeros(nb_) for r in tidx}; cnt = {r: np.zeros(nb_) for r in tidx}; Etr = {r: [] for r in range(nrep)}; nsw = 0; swa = np.zeros(nrep - 1); swt = np.zeros(nrep - 1)
def pt_step(it):
    global nsw
    for r in range(nrep):
        sweeps_bias(ns[r], gs[r], Ncs[r], L, betas[r], LAM, half, S, GE, GN, 1, seed*100000 + nsw*nrep + r, (nsw + r) % 2)
    nsw += 1
    Es = np.array([(x**2).sum()/4 for x in gs])
    for r in range(it % 2, nrep - 1, 2):
        d = (betas[r] - betas[r + 1])*(Es[r] - Es[r + 1]); swt[r] += 1
        if d >= 0 or rng.random() < np.exp(d):
            swa[r] += 1
            ns[r], ns[r + 1] = ns[r + 1], ns[r]; gs[r], gs[r + 1] = gs[r + 1], gs[r]; Ncs[r], Ncs[r + 1] = Ncs[r + 1], Ncs[r]
            lab[r], lab[r + 1] = lab[r + 1], lab[r]; dirn[r], dirn[r + 1] = dirn[r + 1], dirn[r]
            Es[r], Es[r + 1] = Es[r + 1], Es[r]
    # round trips: label at bU=0 that last visited the top
    if dirn[0] == -1: trips[lab[0]] += 1
    dirn[0] = 1; dirn[-1] = -1
    return Es
for it in range(neq):
    Es = pt_step(it)
    if it % max(neq//20, 1) == 0:
        for r in range(nrep): Etr[r].append(Es[r]/(3*V))
for f in fls: f[:] = 0
for b in range(nb_):
    for it in range(per_bin):
        Es = pt_step(it)
        for r in tidx:
            if np.any(Ncs[r] != half): continue
            cnt[r][b] += 1
            n = ns[r]
            F = np.fft.fftn(n.astype(float), axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T * ph
            Mb[r][b] += np.einsum('ks,kt->kst', F.conj(), F)
            Fg = np.fft.fftn(gs[r].astype(float)/2, axes=(1, 2, 3))[:, idx[:, 0], idx[:, 1], idx[:, 2]].T
            Gb[r][b] += (np.abs(Fg)**2).sum(1); Eb[r][b] += Es[r]/(3*V)
    for r in tidx: c = max(cnt[r][b], 1); Mb[r][b] /= c*V; Gb[r][b] /= c*V; Eb[r][b] /= c
for r in range(nrep): assert np.array_equal(gs[r], charges(ns[r], L)) and np.array_equal(Ncs[r], counts(ns[r]))
np.savez("../data/ptb_%s_state.npz" % tag, n=np.array([x.astype(np.int8) for x in ns]), lab=lab, dirn=dirn, trips=trips)
for r in tidx:
    res = dict(L=L, bU=float(betas[r]), klist=klist, K=K, Mb=Mb[r], Gb=Gb[r], Eb=Eb[r], Etr=np.array(Etr[r]), acc=0.0,
               secs=time.time() - t0, neq=neq, nme=nme, every=1, init="ptc_" + tag)
    ok = cnt[r] > 0; res.update(Mb=Mb[r][ok], Gb=Gb[r][ok], Eb=Eb[r][ok], ncanon=int(cnt[r].sum())); pickle.dump(res, open("../data/ptb_%s_b%.2f.pkl" % (tag, betas[r]), "wb"))
print("tag=%s L=%d ladder 0..%.2f (%d) sweeps eq %d meas %d: round trips total %d; swap acc min %.3f mean %.3f; %.1fs"
      % (tag, L, bmax, nrep, neq, nme, trips.sum(), (swa/np.maximum(swt, 1)).min(), (swa/np.maximum(swt, 1)).mean(), time.time() - t0))
for r in tidx:
    ok = cnt[r] > 0; print("  bU=%.2f canonical samples %d ; E/edge %.5f +- %.5f ; equil trace %s" % (betas[r], cnt[r].sum(), Eb[r][ok].mean(), Eb[r][ok].std()/np.sqrt(ok.sum()), np.round(np.array(Etr[r])[[0, len(Etr[r])//2, -1]], 4)))
