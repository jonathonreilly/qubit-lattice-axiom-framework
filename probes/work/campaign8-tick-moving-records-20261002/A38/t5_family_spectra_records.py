"""A38 t5: (A) records next to H8, exact difference method (only terms containing the record site change);
(B) one-flip spectra over the calm star family: is the zone-corner level 8-fold for every member; members
with that level at zero cost; slopes in 60 directions around the corner and around Gamma; zero-cost
modes elsewhere (21^3 grid)."""
import os, sys, signal, itertools, time, functools
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib38 import *
print = functools.partial(print, flush=True)
t0 = time.time()
H8 = {r: np.array([(-1) ** r[0], (-1) ** r[1], (-1) ** r[2]], float) / np.sqrt(3) for r in CELL}
shapes = [[(0, 0, 0), (1, 0, 0)], [(1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (1, 0, 0)],
          [(0, 0, 0), (1, 0, 0), (0, 1, 0)], [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
          [(1, 0, 0), (0, 1, 0), (0, 0, 1)], [(-1, 0, 0), (0, 1, 0), (1, 0, 0)]]
basis = []
for sh in shapes:
    basis += covariant_basis(sh)
basis[0:3] = [pair_law(1, 0, 0), pair_law(0, 1, 0), pair_law(0, 0, 1)]
M, _ = calm_matrix(H8, basis)
N, S = null_space(M, tol=1e-9)
# ---------- (A) records
def rec_amps(tpl, content, site=(0, 0, 0)):
    amps = {}
    for key, C in tpl.items():
        for s in key:
            x = tuple(np.array(site) - np.array(s))
            Sx = [tuple(np.array(x) + np.array(q)) for q in key]
            k = len(Sx)
            for which, sign in ((content, 1.0), (tex_m(H8, site), -1.0)):
                Bs = [site_B(which if y == site else tex_m(H8, y)) for y in Sx]
                for f in itertools.product((0, 1), repeat=k):
                    if sum(f) == 0 or any(f[i] and Sx[i] == site for i in range(k)):
                        continue
                    T = C
                    for i in range(k):
                        T = np.tensordot(Bs[i][:, f[i], 0], T, axes=([0], [0]))
                    fl = tuple(sorted(Sx[i] for i in range(k) if f[i]))
                    amps[fl] = amps.get(fl, 0) + sign * complex(T)
    return amps
m0 = H8[(0, 0, 0)]
pl = pair_law(1, 1, 0)
for nm, cont in [("+m (background)", m0), ("-m", -m0), ("+z", np.array([0, 0, 1.])), ("(1,1,-1)/sqrt3", np.array([1, 1, -1.]) / np.sqrt(3))]:
    a = rec_amps(pl, cont)
    print(f"(A) pair law, record content {nm:16s}: largest flip amplitude it causes {max([abs(v) for v in a.values()] + [0]):.3e}")
# sphere scan of contents for the pair law
best = min((max(abs(v) for v in rec_amps(pl, np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th)])).values()), th, ph)
           for th in np.linspace(0, np.pi, 31) for ph in np.linspace(-np.pi, np.pi, 61))
print(f"    pair law, contents on a 31x61 sphere grid: smallest largest-amplitude {best[0]:.3e} at theta={best[1]:.3f}, phi={best[2]:.3f}"
      f" (background direction theta={np.arccos(m0[2]):.3f}, phi={np.arctan2(m0[1], m0[0]):.3f})")
recs = [rec_amps(t, -m0) for t in basis]
ks = sorted(set(k for r in recs for k in r))
R = np.array([[r.get(k, 0) for r in recs] for k in ks]) @ N
NR, sv = null_space(np.vstack([R.real, R.imag]), tol=1e-9)
print(f"(A) calm star family next to a -m record: calm subspace dimension {NR.shape[1]} of {N.shape[1]}")
per = [onefl_terms(H8, t) for t in basis]
def terms_of(c):
    out = []
    for ci, tl in zip(c, per):
        if abs(ci) > 1e-14:
            out += [(a, b, d, ci * amp, Si, Sj) for a, b, d, amp, Si, Sj in tl]
    return out
if NR.shape[1]:
    for j in range(NR.shape[1]):
        c = N @ NR[:, j]
        tl = terms_of(c)
        mx = max([abs(x[3]) for x in tl] + [0])
        print(f"    record-calm direction {j}: largest one-flip matrix element {mx:.3e}; pair part {np.round(c[:3], 6).tolist()}")
print(f"    time {time.time() - t0:.1f} s")
# ---------- (B) spectra
kR = np.array([np.pi / 2] * 3)
HR = [bloch_batch(terms_of(N[:, j]), kR[None, :])[0] for j in range(N.shape[1])]
offd = max(np.max(np.abs(h - np.trace(h) / 8 * np.eye(8))) for h in HR)
print(f"(B) zone corner: H(R) - (tr/8) I over all 24 calm directions: max {offd:.2e} (8-fold level for every member)")
trR = np.array([np.trace(h).real / 8 for h in HR])
P0 = null_space(trR[None, :], tol=1e-12)[0]          # members with the corner level at zero cost
rng = np.random.default_rng(5)
dirs = rng.normal(size=(60, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
g = np.linspace(-np.pi / 2, np.pi / 2, 21)
grid = np.array(list(itertools.product(g, repeat=3)))
for trial in range(4):
    w = (P0 @ rng.normal(size=P0.shape[1])) if trial else None
    c = np.r_[1, 1, 0, np.zeros(len(basis) - 3)] if trial == 0 else N @ w
    tl = terms_of(c)
    nm = "pair law" if trial == 0 else f"calm member {trial} (corner level at 0)"
    hs = [1e-3, 2e-3]
    sl = []
    for d in dirs:
        e1 = np.linalg.eigvalsh(bloch_batch(tl, (kR + hs[0] * d)[None, :])[0])
        e2 = np.linalg.eigvalsh(bloch_batch(tl, (kR + hs[1] * d)[None, :])[0])
        v1, v2 = e1 / hs[0], e2 / hs[1]
        sl.append(np.sort(np.abs(v1)))
        lin = np.max(np.abs(v1 - v2))
    sl = np.array(sl)
    E = np.linalg.eigvalsh(bloch_batch(tl, grid))
    nzero = int(np.sum(np.min(np.abs(E), axis=1) < 1e-8))
    print(f"(B) {nm}: corner-level cost {np.trace(bloch_batch(tl, kR[None,:])[0]).real/8:+.2e}; slopes |dE/dk| of the 8 modes at the corner over 60 directions:"
          f" smallest mode min {sl[:,0].min():.3f} max {sl[:,0].max():.3f}; largest mode min {sl[:,7].min():.3f} max {sl[:,7].max():.3f};"
          f" linearity check {lin:.1e}; zero-cost grid points (21^3) {nzero}")
    # Gamma
    eG = np.linalg.eigvalsh(bloch_batch(tl, np.zeros((1, 3)))[0])
    z = np.argsort(np.abs(eG))[:2]
    q = [np.sort(np.abs(np.linalg.eigvalsh(bloch_batch(tl, (h * dirs[:10]))))) [:, :2] for h in (1e-2, 2e-2)]
    ratio = np.median(q[1][:, 1] / np.maximum(q[0][:, 1], 1e-30))
    print(f"    Gamma levels {np.round(eG, 3).tolist()}; growth ratio of the zero modes for doubling dk: {ratio:.2f} (2 = linear, 4 = quadratic)")
print(f"time {time.time() - t0:.1f} s")
