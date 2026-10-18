#!/usr/bin/env python3
"""COROLLARY check, part 3: is the eight-node step W = S R_L U_H U_L gapless in quasi-energy?

Model: B18_check/chk_model.py (a copy of the runner's construction code; NOT independent of the runner).

Certificate (rigorous up to floating-point eigenvalues): on each grid edge [k1, k2] along x (h = 2 pi / N), choose a phase beta
whose chord distance to spec W(k1) and spec W(k2) exceeds Lx * h / 2, with Lx >= sup_k ||d_x W(k)|| from the hopping blocks.
By Bauer-Fike (W normal) beta is attained nowhere on the edge, so the count of eigenphases in the ccw arc (beta, theta) can change
along the edge only where theta is attained. With sorted relative phases x_(j) (at k1) and y_(j) (at k2), the counts differ
exactly for theta in the arcs [min(x_(j), y_(j)), max(...)] (shifted by beta); every such theta is attained on the edge.
If the union over edges (plus the grid eigenphases) is the whole circle, W has no quasi-energy gap.
"""
import itertools, sys, os
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B18_check')
from chk_model import blS, blL, UH, UL, Ws, kst, CUBE, wrap

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

def Hk_many(bl, ks):
    out = np.zeros((len(ks), 12, 12), complex)
    for sh, M in bl.items(): out += np.exp(1j * ks @ np.array(sh, float))[:, None, None] * M[None]
    return out
C0 = UH @ UL
def W_many(ks): return Hk_many(blS, ks) @ Hk_many(blL, ks) @ C0[None]
k_test = np.random.default_rng(1).uniform(-np.pi, np.pi, size=(5, 3))
check("vectorised step matches chk_model Ws and is unitary",
      all(np.allclose(W_many(k_test)[i], Ws(k_test[i])) for i in range(5)) and np.allclose(W_many(k_test) @ W_many(k_test).conj().transpose(0, 2, 1), np.eye(12)))
def dx_norm_bound(bl):
    """sup_k ||d_x X(k)||: if the x-derivative's blocks together form a partial-permutation pattern (<= 1 nonzero per row and
    column over all shifts), the derivative is a monomial matrix at every k and its norm is the largest |sh_x * entry|;
    otherwise fall back to the triangle inequality."""
    pat = sum((np.abs(M) > 1e-12).astype(int) * (sh[0] != 0) for sh, M in bl.items())
    if pat.max() <= 1 and pat.sum(0).max() <= 1 and pat.sum(1).max() <= 1:
        return max(abs(sh[0]) * np.abs(M).max() for sh, M in bl.items() if sh[0] != 0)
    return sum(abs(sh[0]) * np.linalg.norm(M, 2) for sh, M in bl.items())
Lx = dx_norm_bound(blS) + dx_norm_bound(blL)   # ||d_x (S R C)|| <= ||d_x S|| + ||d_x R|| (S, R unitary, C constant unitary)
e0 = np.angle(np.linalg.eigvals(Ws(kst))); E = [x for x in e0 if np.sum(np.abs(wrap(e0 - x)) < 1e-7) == 2][0]
print(f"node quasi-energy E = {E:.6f}; Lipschitz bound along x: Lx = {Lx:.4f}")

def certify(N, Wfun=None, Lip=None):
    Wfun = Wfun or W_many; Lip = Lx if Lip is None else Lip
    h = 2 * np.pi / N
    ax = -np.pi + h * np.arange(N)
    intervals = []; dropped = 0; tot = 0
    allph = []
    for ky, kz in itertools.product(ax, ax):
        ks = np.stack([ax, np.full(N, ky), np.full(N, kz)], 1)
        ph = np.mod(np.angle(np.linalg.eigvals(Wfun(ks))), 2 * np.pi)       # (N, 12)
        allph.append(ph.ravel())
        for i in range(N):
            a, b = ph[i], ph[(i + 1) % N]; tot += 1
            both = np.sort(np.concatenate([a, b])); gaps = np.diff(np.concatenate([both, [both[0] + 2 * np.pi]]))
            j = int(np.argmax(gaps)); beta = both[j] + gaps[j] / 2
            if 2 * np.sin(gaps[j] / 4) <= Lip * h / 2: dropped += 1; continue
            x = np.sort(np.mod(a - beta, 2 * np.pi)); y = np.sort(np.mod(b - beta, 2 * np.pi))
            lo = np.minimum(x, y) + beta; hi = np.maximum(x, y) + beta
            intervals.append(np.stack([lo, hi], 1))
    if not intervals: return dict(N=N, edges=tot, dropped=dropped, holes=[(0, 2*np.pi)], maxhole=2*np.pi)
    iv = np.concatenate(intervals)
    iv = np.mod(iv[:, 0:1], 2 * np.pi) + np.concatenate([np.zeros((len(iv), 1)), iv[:, 1:2] - iv[:, 0:1]], 1)
    iv = np.concatenate([iv, iv - 2 * np.pi]); iv = iv[np.argsort(iv[:, 0])]
    iv = np.concatenate([iv, iv + 2 * np.pi]); iv = iv[np.argsort(iv[:, 0])]
    merged = []
    for s_, e_ in iv:
        if merged and s_ <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e_)
        else: merged.append([s_, e_])
    holes = []; pos = 0.0
    for s_, e_ in merged:
        if e_ <= pos: continue
        if s_ >= 2 * np.pi: break
        if s_ > pos: holes.append((pos, min(s_, 2 * np.pi)))
        pos = max(pos, e_)
    if pos < 2 * np.pi: holes.append((pos, 2 * np.pi))
    grid_ph = np.concatenate(allph)
    return dict(N=N, edges=tot, dropped=dropped, holes=holes, maxhole=max([b - a for a, b in holes], default=0.0))

for N in (24, 48, 64):
    r = certify(N)
    hl = [(round(wrap(a), 4), round(wrap(b), 4)) for a, b in r['holes'][:6]]
    print(f"N={N}: edges {r['edges']}, edges without a certified beta {r['dropped']}, uncovered arcs {len(r['holes'])}, "
          f"largest {r['maxhole']:.2e} rad; first holes (wrapped) {hl}")
check("eight-node step: every quasi-energy is attained (edge certificate on the N = 64 x-line grid covers the whole circle)",
      r['maxhole'] == 0.0 and len(r['holes']) == 0, f"largest uncovered arc {r['maxhole']:.2e}")
# negative control: a gapped step must leave holes. W_c = exp(i a R_L) U_H U_L with a = 0.2 (R_L^2 = 1, so exp(i a R) = cos a + i sin a R)
a_ = 0.2
def Wc_many(ks):
    R = Hk_many(blL, ks); return (np.cos(a_) * np.eye(12)[None] + 1j * np.sin(a_) * R) @ C0[None]
rc = certify(24, Wc_many, np.sin(a_) * dx_norm_bound(blL))
onsite = np.sort(np.angle(np.linalg.eigvals(C0)))
check("negative control: the certificate leaves the true gaps (each of width about pi - 0.4) uncovered for a gapped step (exp(0.2 i R_L) U_H U_L)",
      rc["maxhole"] > 2.5, f"{len(rc['holes'])} uncovered arcs, largest {rc['maxhole']:.3f} rad; on-site phases {np.round(onsite, 3).tolist()}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
