"""TOR-1 (b2, c) bulk locality on the torus: response R[l', l] = d kbb_{l'} / d theta_l (central differences) vs torus taxicab
distance of link midpoints; exponential fit; far plateau.  Also the plaquette-derivative profile |g(x, p)| vs distance.
usage: python3 tor1_locality.py Lx Lt model nfield seed [Ns]"""
import sys, time
import numpy as np
from tor1_lib import *
Lx, Lt, model, nf, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
Ns = int(sys.argv[6]) if len(sys.argv) > 6 else 4
t0 = time.time(); S = Torus(Lx, Lt); M = TorusMeasure.__new__(TorusMeasure)
M.S, M.model = S, MODELS[model]; M.charges = sorted(set(e for (e, _, _) in M.model))
M.coef = {e: sum(m * e * (1 if c == 'L' else -1) for (ee, c, m) in M.model if ee == e) for e in M.charges}
rng = np.random.default_rng(seed); eps = 1e-4
mid = np.array([(l[4] + 0.5, l[5]) if l[2] == 'x' else (l[4], l[5] + 0.5) for l in S.L])
def tdist(a, b):
    dx = np.abs(a[:, None, 0] - b[None, :, 0]); dt = np.abs(a[:, None, 1] - b[None, :, 1])
    return np.minimum(dx, Lx - dx) + np.minimum(dt, Lt - dt)
DL = tdist(mid, mid)
psite = np.array([(x + 0.5, t + 0.5) for (x, t) in S.plaq]); ssite = np.array([(s % Lx, s // Lx) for s in range(S.ns)])
DG = tdist(psite, ssite)                        # (np, ns)
print(f"# TOR-1 locality Lx={Lx} Lt={Lt} model={model} nfield={nf} seed={seed} Ns={Ns} eps={eps}", flush=True)
allchi = []
for f in range(nf):
    while True:
        th = rng.normal(0, 0.12, S.nl) + rng.uniform(0, 2*np.pi) * S.Ux + rng.uniform(0, 2*np.pi) * S.Ut
        Fr = (th @ S.Pm.T + np.pi) % (2*np.pi) - np.pi
        if np.abs(Fr).max() < 0.55 and abs(round(Fr.sum()/(2*np.pi))) == 0: break
    Rm = np.zeros((S.nl, S.nl)); CH = 16 if S.N <= 64 else 4
    pts = np.concatenate([th[None] + eps * np.eye(S.nl), th[None] - eps * np.eye(S.nl)], 0)
    out = []
    for c in range(0, len(pts), CH):
        k, g = kbb_only(M, pts[c:c+CH], Ns); out.append(k)
    out = np.concatenate(out); Rm = ((out[:S.nl] - out[S.nl:]) / (2 * eps)).T      # Rm[l', l]
    _, g0 = kbb_only(M, th[None], Ns); g0 = np.abs(g0[0])                             # (np, ns) at mid-ray
    ds = np.unique(DL); chi = np.array([np.abs(Rm[DL == d]).max() for d in ds]); allchi.append(chi)
    gd = np.unique(DG); gprof = np.array([g0[DG == d].max() for d in gd])
    far = DL >= DL.max() - 0.5
    print(f"field {f}: chi(d) " + " ".join(f"{d:.1f}:{c:.2e}" for d, c in zip(ds, chi)) + f"  | far-plateau median {np.median(np.abs(Rm[far])):.2e} [{time.time()-t0:.0f}s]", flush=True)
    print(f"   |g(x,p)| vs dist " + " ".join(f"{d:.1f}:{c:.2e}" for d, c in zip(gd, gprof)), flush=True)
chi = np.array(allchi); ds = np.unique(DL)
sel = (ds >= 1) & (ds <= ds.max())
X = ds[sel]; Y = np.log(chi[:, sel].max(0))
A = np.vstack([X, np.ones_like(X)]).T; coef, res, *_ = np.linalg.lstsq(A, Y, rcond=None)
r = Y - A @ coef; s2 = (r @ r) / max(len(X) - 2, 1); cov = s2 * np.linalg.inv(A.T @ A)
nu, se = -coef[0], np.sqrt(cov[0, 0])
print(f"FIT log chi_max(d) over d in [1, {ds.max():.1f}]: nu = {nu:.3f} +- {se:.3f} ({nu/se if se>0 else np.inf:.1f} sigma); chi(dmax)/chi(1) = {chi[:, sel].max(0)[-1]/chi[:, sel].max(0)[0]:.2e}")
np.save(f"loc_Lx{Lx}_Lt{Lt}_{model}_s{seed}.npy", np.vstack([ds, chi]))
