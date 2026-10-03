"""A38 t4: (1) NN plaquette phases over H8 for RANDOM covariant star-local laws (calm or not): fixed?
(2) margin of the rank-1 NN block over the calm family; (3) the one-flip spectra over the calm family:
zero-cost modes, touchings at Gamma and at the zone corner, slopes; (4) records next to H8:
which contents keep it calm (pair law and the whole calm star family)."""
import os, sys, signal, itertools, time
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib38 import *
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
per = []
for t in basis:
    per.append(onefl_terms(H8, t))
def terms_of(c):
    out = []
    for ci, tl in zip(c, per):
        if abs(ci) > 1e-14:
            out += [(a, b, d, ci * amp, Si, Sj) for a, b, d, amp, Si, Sj in tl]
    return out
rng = np.random.default_rng(11)
# (1) random covariant laws, calm or not
phs = set()
for trial in range(5):
    c = rng.normal(size=len(basis))
    f = plaquette_fluxes(realspace_hop(terms_of(c)))
    phs |= set(round(p, 6) for x, fc, aw, p in f)
    # corner-parity pattern
    patt = all(abs(p - (2 / 3) * (-1) ** sum(x)) < 1e-9 for x, fc, aw, p in f)
print(f"(1) random covariant star-local laws (not calm in general): NN face phases/pi seen {sorted(phs)}; "
      f"pattern +2/3 at even corners, -2/3 at odd corners: {patt}")
# (2) NN block singular values over the calm family
keys = sorted(set((a, b, tuple(int(v) for v in d)) for tl in per for a, b, d, amp, Si, Sj in tl))
kidx = {k: i for i, k in enumerate(keys)}
A = np.zeros((len(keys), len(basis)), complex)
for j, tl in enumerate(per):
    for a, b, d, amp, Si, Sj in tl:
        A[kidx[(a, b, tuple(int(v) for v in d))], j] += amp
cls = np.array([sum(v * v for v in k[2]) for k in keys])
for c_ in (0, 1, 2, 4):
    sub = A[cls == c_] @ N
    sv = np.linalg.svd(np.vstack([sub.real, sub.imag]), compute_uv=False)
    print(f"(2) |d|^2={c_}: singular values over the calm family {np.round(sv[:4], 8).tolist()}")
fullsv = np.linalg.svd(np.vstack([(A @ N).real, (A @ N).imag]), compute_uv=False)
print(f"    rank of the whole one-flip map on the calm family: {int(np.sum(fullsv > 1e-9 * fullsv[0]))}")
# (3) spectra over the calm family
g = np.linspace(-np.pi / 2, np.pi / 2, 13)
kG = np.zeros(3); kR = np.array([np.pi / 2] * 3)
def report(c, name):
    tl = terms_of(c)
    ev = lambda k: np.linalg.eigvalsh(bloch(tl, np.asarray(k)))
    mins = min(np.min(np.abs(ev(k))) for k in itertools.product(g, repeat=3))
    sym = max(np.max(np.abs(np.sort(ev(k)) + np.sort(ev(k))[::-1])) for k in itertools.product(g[::4], repeat=3))
    eg, er = ev(kG), ev(kR)
    out = f"    {name}: smallest |cost| on 13^3 grid {mins:.2e}; spectrum symmetric about 0: {sym < 1e-9}; "
    out += f"cost levels at Gamma {np.round(eg, 3).tolist()}; at corner {np.round(er, 3).tolist()}"
    print(out)
    # slopes at Gamma of the levels nearest zero, along 4 directions
    for kp, nm in ((kG, "Gamma"), (kR, "corner")):
        e0 = ev(kp); i0 = np.argsort(np.abs(e0))[:2]
        sl = []
        for d in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, -1, 0)]:
            dv = np.array(d, float) / np.linalg.norm(d)
            e1, e2 = ev(kp + 1e-3 * dv), ev(kp + 2e-3 * dv)
            sl.append(round(float(np.min(np.abs(e1))) / 1e-3, 3))
        print(f"       near {nm}: |cost| of the lowest mode / dk along (100),(110),(111),(1-10): {sl}")
report(N.T @ np.linalg.lstsq(N, np.r_[1, 1, 0, np.zeros(len(basis) - 3)], rcond=None)[0] @ np.eye(N.shape[1]) if False else np.r_[1, 1, 0, np.zeros(len(basis) - 3)], "pair law J=K=1")
for trial in range(3):
    w = rng.normal(size=N.shape[1])
    report(N @ w, f"random calm member {trial}")
# (4) records next to H8: content c at the origin; compressed law; flips not touching the origin
def record_amps(c_law, content):
    ov = {(0, 0, 0): content}
    amps = {}
    for x in itertools.product(range(-3, 4), repeat=3):
        for key, C in c_law.items():
            S = [tuple(np.array(x) + np.array(s)) for s in key]
            if all(max(abs(v) for v in y) > 2 for y in S):
                continue
            Bs = [site_B(ov[y] if y in ov else tex_m(H8, y)) for y in S]
            k = len(S)
            for f in itertools.product((0, 1), repeat=k):
                if sum(f) == 0:
                    continue
                if any(f[i] and S[i] == (0, 0, 0) for i in range(k)):
                    continue                   # killed by the record's compression
                T = C
                for i in range(k):
                    T = np.tensordot(Bs[i][:, f[i], 0], T, axes=([0], [0]))
                fl = tuple(sorted(S[i] for i in range(k) if f[i]))
                if all(max(abs(v) for v in y) <= 1 for y in fl):   # patterns near the record only (all complete)
                    amps[fl] = amps.get(fl, 0) + complex(T)
    return amps
m0 = H8[(0, 0, 0)]
pl = pair_law(1, 1, 0)
for nm, cont in [("+m (background)", m0), ("-m", -m0), ("+z axis", np.array([0, 0, 1.])), ("(1,1,-1)/sqrt3", np.array([1, 1, -1.]) / np.sqrt(3))]:
    a = record_amps(pl, cont)
    print(f"(4) pair law, record content {nm:16s}: largest surviving flip amplitude near it {max(abs(v) for v in a.values()):.3e}")
# whole calm family with a -m record: is any member calm next to it?
cols = []
allk = set()
recs = []
for j in range(len(basis)):
    recs.append(record_amps(basis[j], -m0))
    allk |= set(recs[-1])
allk = sorted(allk)
R = np.array([[r.get(k, 0) for r in recs] for k in allk])
RN = R @ N
sv = np.linalg.svd(np.vstack([RN.real, RN.imag]), compute_uv=False)
print(f"(4) calm star family next to a -m record: smallest singular value {sv[-1]:.3e} (largest {sv[0]:.3f}); "
      f"members calm next to it: {int(np.sum(sv < 1e-9 * sv[0]))} dims of {N.shape[1]}")
print(f"time {time.time() - t0:.1f} s")
