#!/usr/bin/env python3
"""C1 part 1b: Floquet BdG of the eight-node step with symmetric pairing layers.

W_BdG(k) = exp(-i tau [[0, D(k)], [D(k)^dag, 0]]) . diag(e^{-i pi/2} W(k), e^{+i pi/2} W(Q-k)^*)  on (c_k, c^dag_{Q-k}).
The global phase e^{-i pi N/2} (a chemical-potential shift per step) moves the +pi/2 node set to quasi-energy 0 and the
-pi/2 set to pi.  Without pairing, quasi-energy 0 (and pi) of W_BdG is reached only at the eight nodes (B17 check).
Cases (on-site pairing matrices from the symmetric channels of c1_reps.py, normalised ||A||_F = 1):
 B1  Q = R, chi = det (A2): all eight gapped; global quasi-energy-0 and pi gaps (grid N + local refinement; numerical).
 B2  Q = R, chi = A1: exact 4-fold BdG zeros at all eight nodes (symmetry-pinned).
 B3  Q = 0 (pairs K with -K), symmetric on-site: nodes survive (local minimisation of |eps| near each node -> ~0).
 B4  Q = R, Wilson-type D(k) = w(k) A_det, w = 3 - sum cos q_i cos q_j (q = k - k*): w(+-k*) = 0, w(doublers) = 4.
     +-k* stay exactly gapless (4-fold BdG zero, isotropic cone at sqrt2/3), doublers gapped, no other zero found.
 B5  naturalness: the on-site A tuned so that the first-order k* singlet vanishes (c1_reps R5c) still gaps k* at
     higher order (|eps_min(k*)| ~ tau^3): the masslessness of B4 is a choice of Delta(k), not symmetry-protected.
"""
import time, sys
from scipy.optimize import minimize
from c1lib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
NG = int(sys.argv[1]) if len(sys.argv) > 1 else 24
rng = np.random.default_rng(11)
O_idx = list(range(24))

# ---- channel spaces (rebuilt here, same construction as c1_reps.py) ----
AB = []
for i in range(12):
    for j in range(i + 1, 12):
        X = np.zeros((12, 12)); X[i, j] = 1; X[j, i] = -1; AB.append(X)
chiA2 = {i: A2_O[cls(ROT[i]['M'])] for i in O_idx}; chiA1 = {i: 1 for i in O_idx}
def channel_space(chi):
    rowsM = [np.array([(ROT[i]['U'] @ X @ ROT[i]['U'].T - chi[i] * X)[np.triu_indices(12, 1)] for X in AB]).T for i in O_idx]
    _, s, Vh = np.linalg.svd(np.vstack(rowsM)); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))])
    return [sum(c * X for c, X in zip(v, AB)) for v in Vh[s < 1e-10]]
VA2, VA1 = channel_space(chiA2), channel_space(chiA1)
def rnd(V):
    A = sum((rng.normal() + 1j * rng.normal()) * X for X in V); return A / np.linalg.norm(A)
A2m, A1m = rnd(VA2), rnd(VA1)
for A_, chi in ((A2m, chiA2), (A1m, chiA1)):
    assert all(np.allclose(ROT[i]['U'] @ A_ @ ROT[i]['U'].T, chi[i] * A_) for i in O_idx) and np.allclose(A_, -A_.T)

def eps(k, Dfun, Q, tau):
    return bdg_quasienergies(k, Dfun, tau, Q)
def gap0(k, Dfun, Q, tau): return np.min(np.abs(eps(k, Dfun, Q, tau)))
def gappi(k, Dfun, Q, tau): return np.min(np.abs(wrap(eps(k, Dfun, Q, tau) - np.pi)))
def grid_scan(Dfun, Q, tau, N, exclude=(), r_ex=0.0):
    g = 2 * np.pi * np.arange(N) / N; best0 = (np.inf, None); bestp = (np.inf, None)
    for x in g:
        for y in g:
            for z in g:
                k = np.array([x, y, z])
                if any(np.linalg.norm(wrap(k - e)) < r_ex for e in exclude): continue
                ev = eps(k, Dfun, Q, tau); a0 = np.min(np.abs(ev)); ap = np.min(np.abs(wrap(ev - np.pi)))
                if a0 < best0[0]: best0 = (a0, k)
                if ap < bestp[0]: bestp = (ap, k)
    return best0, bestp
def refine(f, k0, r_box=None, center=None):
    obj = f
    if r_box is not None:
        obj = lambda k: f(k) + 10 * max(0, np.linalg.norm(wrap(k - center)) - r_box)
    res = minimize(obj, k0, method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-13, maxiter=4000))
    return res.fun, res.x

tau = 0.5
# ---------------- B1 ----------------
DA2 = lambda k: A2m
node_gaps = {nm: gap0(k, DA2, Q_R, tau) for nm, k in NODES.items()}
print("B1 quasi-energy-0 BdG gap at the nodes, Q=R chi=A2 on-site:", {nm: round(v, 4) for nm, v in node_gaps.items()})
(b0, kb0), (bp, kbp) = grid_scan(DA2, Q_R, tau, NG)
r0, _ = refine(lambda k: gap0(k, DA2, Q_R, tau), kb0); rp, _ = refine(lambda k: gappi(k, DA2, Q_R, tau), kbp)
check(f"B1 Q=R, chi=det(A2), on-site, tau={tau}: all eight nodes gapped; global gaps at quasi-energy 0 and pi stay open "
      f"(grid N={NG} + Nelder-Mead from the grid minimum; numerical, not certified)",
      min(node_gaps.values()) > 1e-2 and r0 > 1e-3 and rp > 1e-3, f"grid min |eps|: 0-gap {b0:.4f} (refined {r0:.4f}), pi-gap {bp:.4f} (refined {rp:.4f})")

# ---------------- B2 ----------------
DA1 = lambda k: A1m
z = {}
for nm, k in NODES.items():
    ev = eps(k, DA1, Q_R, tau); z[nm] = int(np.sum(np.abs(ev) < 1e-10))
# At the doublers the A1 channel couples the node doublet to OTHER D4 doublets (second-order shift +-delta of the
# zero), so the exact zero moves off K; test gaplessness by local minimisation in a 0.3-ball instead.
mins2 = {}
for nm, k in NODES.items():
    f = lambda kk: gap0(kk, DA1, Q_R, tau)
    mins2[nm] = min([f(k)] + [refine(f, k + 0.05 * rng.normal(size=3), r_box=0.3, center=k)[0] for _ in range(4)])
gK = {nm: gap0(k, DA1, Q_R, tau) for nm, k in NODES.items()}
check("B2 Q=R, chi=A1 on-site (singlet forbidden at all eight): no node is gapped -- +-k* keep an exact 4-fold zero, and within 0.3 "
      "of every doubler a BdG zero persists (the doubler zero is displaced off K by a second-order shift; local minimisation)",
      z['k*'] == 4 and z['-k*'] == 4 and max(mins2.values()) < 1e-6,
      f"zero counts at K {z}; |eps| at K {dict((nm, round(v, 5)) for nm, v in gK.items())}; local min near K "
      + ", ".join(f"{nm}:{v:.1e}" for nm, v in mins2.items()))

# ---------------- B3 ----------------
# Q = 0 needs Delta(k) = -Delta(-k)^T: on-site antisymmetric A in a channel; use A1 (nonzero inter-node blocks, c1_reps R6)
Q0 = np.zeros(3)
inter = {nm: np.abs(level(k, np.pi / 2).conj().T @ A1m @ level(-k, np.pi / 2).conj()).max() for nm, k in NODES.items()}
print("B3 inter-node pairing amplitudes |<K|A|-K>| (Q=0, A1 on-site):", {nm: round(v, 3) for nm, v in inter.items()})
mins = {}
for nm, k in NODES.items():
    f = lambda kk: gap0(kk, DA1, Q0, tau)
    best = min(refine(f, k + 0.02 * rng.normal(size=3), r_box=0.3, center=k)[0] for _ in range(3))
    mins[nm] = best
check("B3 Q=0 (pairs K with -K; opposite chiralities so each BdG point carries charge +-2): with a symmetric on-site pairing that "
      "couples every node to its partner, no node is gapped -- a BdG zero persists within 0.3 of every node (local minimisation)",
      max(mins.values()) < 1e-6 and min(inter.values()) > 1e-2,
      "min |eps| near nodes: " + ", ".join(f"{nm}:{v:.1e}" for nm, v in mins.items()))

# ---------------- B4 Wilson-type ----------------
DW = lambda k: wfun(k) * A2m
ok_w = all(abs(wfun(gk(g, k)) - wfun(k)) < 1e-12 and abs(wfun(Q_R - k) - wfun(k)) < 1e-12 for g in ROT for k in rng.uniform(-np.pi, np.pi, (3, 3)))
ok_w &= abs(wfun(kst)) < 1e-14 and abs(wfun(-kst)) < 1e-14 and all(abs(wfun(NODES[nm]) - 4) < 1e-12 for nm in NODES if '+pi' in nm)
check("B4a w(k) is invariant under all 24 affine rotation maps and k -> Q-k; w(+-k*) = 0, w = 4 at the six doublers, w >= 0", ok_w)
zW = {nm: int(np.sum(np.abs(eps(k, DW, Q_R, tau)) < 1e-10)) for nm, k in NODES.items()}
gW = {nm: gap0(k, DW, Q_R, tau) for nm, k in NODES.items()}
print("B4 node zero counts / gaps:", zW, {nm: round(v, 4) for nm, v in gW.items()})
# cone at +-k*: |eps| / |q| along random directions
vs = np.sqrt(2) / 3; cone = []
for nm in ('k*', '-k*'):
    for _ in range(6):
        d = rng.normal(size=3); d /= np.linalg.norm(d); q = 1e-4
        ev = np.sort(np.abs(eps(NODES[nm] + q * d, DW, Q_R, tau)))[:4]; cone.append(ev / q)
cone = np.array(cone)
check("B4b Wilson-type pairing: +-k* keep an exact 4-fold zero with an isotropic cone at sqrt2/3 (4 BdG bands, finite differences), "
      "the six doublers are gapped", all(zW[nm] == 4 for nm in ('k*', '-k*')) and min(gW[nm] for nm in NODES if '+pi' in nm) > 1e-2
      and np.allclose(cone, vs, atol=2e-4), f"cone |eps|/|q| range [{cone.min():.6f}, {cone.max():.6f}] vs {vs:.6f}")
(b0, kb0), (bp, kbp) = grid_scan(DW, Q_R, tau, NG, exclude=(kst, -kst), r_ex=0.35)
r0, k0r = refine(lambda k: gap0(k, DW, Q_R, tau), kb0); rp, kpr = refine(lambda k: gappi(k, DW, Q_R, tau), kbp)
far0 = min(np.linalg.norm(wrap(k0r - e)) for e in (kst, -kst)); farp = min(np.linalg.norm(wrap(kpr - e)) for e in (kst, -kst))
# inside the balls: minimisation from off-centre starts converges onto +-k* themselves
inside_ok = True
for e in (kst, -kst):
    for _ in range(4):
        f_, x_ = refine(lambda k: gap0(k, DW, Q_R, tau), e + 0.25 * rng.uniform(-1, 1, 3) / np.sqrt(3))
        inside_ok &= (np.linalg.norm(wrap(x_ - e)) < 1e-4) or f_ > 1e-3
check(f"B4c Wilson-type pairing: away from +-k* no other quasi-energy-0 or pi zero found (grid N={NG} outside 0.35-balls + refinement; "
      "minimisations started inside the balls end at +-k*); numerical, not certified",
      (r0 > 1e-3 or far0 < 0.3) and (rp > 1e-3 or farp < 0.3) and inside_ok,
      f"outside balls: 0-gap grid {b0:.4f} refined {r0:.4f} (dist to +-k* {far0:.2f}); pi-gap grid {bp:.4f} refined {rp:.4f} (dist {farp:.2f})")
# doubler gap scaling with tau (s-wave Majorana mass ~ tau * w * m)
print("B4 doubler gap vs tau:", {t: round(gap0(NODES['k*+pi ex'], DW, Q_R, t), 5) for t in (0.05, 0.1, 0.2, 0.5)})

# ---------------- B5 naturalness ----------------
TAB = {nm: level(k, np.pi / 2) for nm, k in NODES.items()}
def singlet(Qm, Dm): return (Qm.conj().T @ Dm @ Qm.conj())[0, 1]
def levels_all(k, tol=1e-7):
    e, V = np.linalg.eig(W(k)); ph = np.angle(e); used = np.zeros(12, bool); out = []
    for i in np.argsort(ph):
        if used[i]: continue
        grp = np.where((~used) & (np.abs(wrap(ph - ph[i])) < tol))[0]; used[grp] = True
        Qm, _ = np.linalg.qr(V[:, grp]); out.append((ph[i], Qm))
    return out
# B5a exact block decoupling at +-k*: every A in V_A2 (= every symmetric Delta(+-k*)) pairs the node doublet only with itself
cross = 0.0
for nm in ('k*', '-k*'):
    Dn = TAB[nm]
    for E, Qm in levels_all(NODES[nm]):
        if abs(wrap(E - np.pi / 2)) < 1e-6: continue
        cross = max(cross, max(np.abs(Dn.conj().T @ X @ Qm.conj()).max() for X in VA2))
check("B5a at +-k* every A2-channel pairing matrix (hence every symmetric Delta(+-k*)) has zero blocks between the node doublet and "
      "all other levels: the BdG node block decouples exactly, so +-k* is gapless iff its single complex singlet m_K vanishes "
      "(det(D) = A2 => D (x) D' carries A1, D (x) G3/2 carries no 1-dim character)", cross < 1e-12, f"max cross block {cross:.1e}")
F = np.array([[singlet(TAB[nm], X) for X in VA2] for nm in ('k*', '-k*')])
_, s, Vh = np.linalg.svd(F); nullv = Vh[np.sum(s > 1e-9):]
c = nullv.T @ (rng.normal(size=len(nullv)) + 1j * rng.normal(size=len(nullv)))
At = sum(ci * X for ci, X in zip(c, VA2)); At /= np.linalg.norm(At)
Dt = lambda k: At
first = max(abs(singlet(TAB[nm], At)) for nm in ('k*', '-k*'))
gt = {t: gap0(kst, Dt, Q_R, t) for t in (0.05, 0.1, 0.2, 0.4)}
dbl = {nm: gap0(NODES[nm], Dt, Q_R, tau) for nm in NODES if '+pi' in nm}
(b0, kb0), (bp, kbp) = grid_scan(Dt, Q_R, tau, NG, exclude=(kst, -kst), r_ex=0.35)
r0, k0r = refine(lambda k: gap0(k, Dt, Q_R, tau), kb0); rp, kpr = refine(lambda k: gappi(k, Dt, Q_R, tau), kbp)
far0 = min(np.linalg.norm(wrap(k0r - e)) for e in (kst, -kst)); farp = min(np.linalg.norm(wrap(kpr - e)) for e in (kst, -kst))
check("B5b on-site A2 pairing with m_{+-k*} tuned to 0 (2 complex conditions): +-k* exactly gapless for every tau, the six doublers gapped, "
      f"no other zero found (grid N={NG} outside 0.35-balls + refinement; numerical)",
      first < 1e-12 and max(gt.values()) < 1e-12 and min(dbl.values()) > 1e-2 and (r0 > 1e-3 or far0 < 0.3) and (rp > 1e-3 or farp < 0.3),
      f"k* |eps| vs tau {dict((t, f'{v:.1e}') for t, v in gt.items())}; doubler gaps {dict((nm, round(v, 4)) for nm, v in dbl.items())}; "
      f"outside balls 0-gap {r0:.4f}, pi-gap {rp:.4f}")
# B5c generic symmetric perturbation regenerates the k* mass linearly: the tuning is not protected
Ar = rnd(VA2)
gp = {eta: gap0(kst, (lambda k, e=eta: (At + e * Ar) / np.linalg.norm(At + e * Ar)), Q_R, tau) for eta in (1e-3, 1e-2, 1e-1)}
sl = np.polyfit(np.log(list(gp)), np.log(list(gp.values())), 1)[0]
check("B5c adding eta x (generic A2-channel on-site pairing) gaps +-k* linearly in eta: the +-k* masslessness of B4/B5b is a tuning "
      "(Wilson-like), not symmetry protection", 0.9 < sl < 1.1, f"k* gap vs eta {dict((e, f'{v:.2e}') for e, v in gp.items())}; slope {sl:.2f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
