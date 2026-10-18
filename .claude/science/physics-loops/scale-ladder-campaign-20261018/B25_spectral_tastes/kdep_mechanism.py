#!/usr/bin/env python3
"""B25 part 1d: the k-dependent taste of the ALIGN2 words, made explicit.
W = S^a P S^a G S^a P' S^a G with P' = PL(-phi) (so P' is proportional to P^T = Y P Y) and t_Y = (pi/2a)(1,1,1) (Delta_a(t_Y) = Y).
Claim (derived by the slotwise gauge chain, checked here): W(k + t_Y) = c V W_rot(k) V^-1 with a k-INDEPENDENT diagonal V and
W_rot = S^a P' S^a G S^a P S^a G (P <-> P'), while W_rot(k) = X(k)^-1 W(k) X(k) with X = S^a P S^a G.  So t_Y is a spectral taste
whose intertwiner X(k)^-1 V^-1 is k-dependent, and no k-independent U or T intertwiner exists.  Prints PASS/FAIL, TOTAL."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
ALL.update(PLANE6)
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(31); KS = rng.uniform(-np.pi, np.pi, (3, 3))
def inter(A_of_k, B_of_k):
    rows = []
    for k in KS:
        A, B = A_of_k(k), B_of_k(k); rows.append(np.kron(A, np.eye(12)) - np.kron(np.eye(12), B.T))
    s = np.linalg.svd(np.vstack(rows), compute_uv=False); return int(np.sum(s < 1e-8 * s[0]))
res = []
for a, pw in ((1, 'S'), (2, 'S2'), (4, 'S4')):
    for m in (1, 2, 4, 5):
        for g in ('H13', 'L112', 'L230'):
            P, Pp = f"P{m}", f"P{12 - m}"
            w = [pw, ALL[P], pw, PC[g], pw, ALL[Pp], pw, PC[g]]; wr = [pw, ALL[Pp], pw, PC[g], pw, ALL[P], pw, PC[g]]
            tY = np.pi / (2 * a) * np.ones(3)
            Wf = lambda k: Wb(w, k[None])[0]; Wt = lambda k: Wb(w, (k + tY)[None])[0]; Wr = lambda k: Wb(wr, k[None])[0]
            Xk = lambda k: Wb([pw, ALL[P], pw, PC[g]], k[None])[0]
            d_rot = inter(Wt, Wr)                                       # k-independent V with W(k+tY) V = V W_rot(k)
            ok_conj = all(np.allclose(np.linalg.inv(Xk(k)) @ Wf(k) @ Xk(k), Wr(k)) for k in KS)
            dU = inter(Wt, Wf); dT = inter(Wt, lambda k: Wf(k).T)
            res.append((a, m, g, d_rot, ok_conj, dU, dT))
check("W(k + t_Y) has a k-independent intertwiner to the rotated word W_rot(k) (all 36 cases)", all(r[3] > 0 for r in res), f"{[r[3] for r in res][:6]}")
check("W_rot(k) = X(k)^-1 W(k) X(k) with X = S^a P S^a G (exact; k-dependent)", all(r[4] for r in res))
check("no k-independent U or T intertwiner between W(k + t_Y) and W(k) (so t_Y is a k-dependent taste)", all(r[5] == 0 and r[6] == 0 for r in res),
      f"{[(r[5], r[6]) for r in res][:6]}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
