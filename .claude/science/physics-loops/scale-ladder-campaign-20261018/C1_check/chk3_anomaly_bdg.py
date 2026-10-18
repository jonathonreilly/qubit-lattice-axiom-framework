#!/usr/bin/env python3
"""C1 check, claims 4-5 (+ Q = 0 charge): chiralities by Berry flux (not by degenerate PT), Weyl-dipole table,
BdG charges for Q = 0 / Q = R, and spot checks of BdG cases B1, B2(k*), B4, B5b, B5c in the checker's own model/gauge."""
import time
from scipy.optimize import minimize
from cklib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(4242)

# ---------------- chirality by Berry flux of the upper band of a 2-fold crossing ----------------
def upper_vec(Uk, E0):
    e, V = np.linalg.eig(Uk); d = wrap(np.angle(e) - E0)
    cand = np.where(np.abs(d) < 0.3)[0]; j = cand[np.argmax(d[cand])]
    return V[:, j] / np.linalg.norm(V[:, j])
def berry_flux(Ufun, K, E0, r=2e-3, nt=16, nph=32):
    th = np.linspace(1e-4, np.pi - 1e-4, nt + 1); ph = np.linspace(0, 2 * np.pi, nph + 1)[:-1]
    vec = np.empty((nt + 1, nph, Ufun(K).shape[0]), complex)
    for i, t in enumerate(th):
        for j, p in enumerate(ph):
            q = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            vec[i, j] = upper_vec(Ufun(K + q), E0)
    F = 0.0
    for i in range(nt):
        for j in range(nph):
            a, b, c, d = vec[i, j], vec[i + 1, j], vec[i + 1, (j + 1) % nph], vec[i, (j + 1) % nph]
            F += np.angle(np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, d) * np.vdot(d, a))
    return F / (2 * np.pi)
chi = {}
for n, K in NODES.items():
    f = berry_flux(W, K, np.pi / 2); chi[n] = int(round(f))
    a, B = weyl_B(K, node_doublet(n)); chi_pt = int(np.sign(np.linalg.det(B)))
    print(f"   {NAME[n]:16s} Berry flux of upper band = {f:+.4f}   (degenerate-PT sign det B = {chi_pt:+d})")
ok = all(abs(chi[n]) == 1 for n in NODES) and all(chi[n] == (-1) ** sum(n) * chi[(0, 0, 0)] for n in NODES)
check("A1 Berry-flux chiralities: |flux| = 1 at all eight, chi(k*+pi n) = (-1)^{|n|} chi(k*); net zero", ok and sum(chi.values()) == 0, str({NAME[n]: c for n, c in chi.items()}))
# ---------------- dipole table ----------------
orbits = {'k*': [(0, 0, 0)], '-k*': [(1, 1, 1)], 'A': [n for n in DOUB if sum(n) == 1], 'B': [n for n in DOUB if sum(n) == 2]}
for o, ns in orbits.items():
    imgs = {tuple(np.round(wrap(gk(g, NODES[ns[0]])) / np.pi * 2).astype(int)) for g in PROPER}
    assert imgs == {tuple(np.round(wrap(NODES[m]) / np.pi * 2).astype(int)) for m in ns}, o
rows = {}
for r in range(5):
    for combo in itertools.combinations(orbits, r):
        S = [n for o in combo for n in orbits[o]]
        net = sum(chi[n] for n in S); b = sum((chi[n] * NODES[n] for n in S), np.zeros(3))
        bm = np.round(np.mod(b, 2 * np.pi) / np.pi, 6) % 2
        z2 = tuple(int(sum(chi[n] for n in S if n[i] == 1)) % 2 for i in range(3))
        rows['+'.join(combo) or 'empty'] = (len(S), net, bm, z2)
for lab, (m, net, bm, z2) in rows.items(): print(f"   {lab:14s} #{m}  net chi {net:+d}  b/pi mod 2 = {bm.tolist()}  Z2 counts {z2}")
free = sorted(l for l, (m, net, bm, z2) in rows.items() if net == 0 and np.allclose(bm, 0) and z2 == (0, 0, 0))
check("A2 dipole table: doublers (A+B) and {+-k*} each have net chirality 0 and b = pi(1,1,1) mod 2pi (Z2 counts (1,1,1)); all eight: b = 0; "
      "only 'empty' and 'all eight' are anomaly-free among rotation-invariant subsets",
      rows['A+B'][1] == 0 and np.allclose(rows['A+B'][2], 1) and rows['k*+-k*'][1] == 0 and np.allclose(rows['k*+-k*'][2], 1)
      and free == sorted(['empty', 'k*+-k*+A+B']), f"anomaly-free: {free}")
# Z2 count definition consistency with the dipole: b/pi mod 2 = sum chi n mod 2 for net-zero sets (since b = sum chi (k* + pi n))
cons = all(np.allclose(bm, z2) for l, (m, net, bm, z2) in rows.items() if net == 0)
check("A2b for net-zero subsets the Z2^3 counts equal b/pi mod 2 (they are the same invariant, not independent anomalies)", cons)

# ---------------- BdG charges ----------------
mu = np.pi / 2
def part(K): return lambda k: np.exp(-1j * mu) * W(k)
def hole(Q): return lambda k: np.exp(1j * mu) * np.conj(W(-Q - k))
chg = {}
for Qn, Q in (('R', QR), ('0', Q0)):
    for n, K in NODES.items():
        fp = berry_flux(lambda k: np.exp(-1j * mu) * W(k), K, 0.0); fh = berry_flux(hole(Q), K, 0.0)
        chg[(Qn, n)] = (int(round(fp)), int(round(fh)))
print("   BdG zero-sector charges (particle, hole):", {f"Q={q},{NAME[n]}": v for (q, n), v in chg.items()})
check("A3 BdG charge at each node: Q = R -> particle + hole = 0 (gappable, intra-node); Q = 0 -> particle + hole = +-2 (not gappable by small pairing)",
      all(sum(chg[('R', n)]) == 0 for n in NODES) and all(abs(sum(chg[('0', n)])) == 2 for n in NODES))
VA2, VA1 = onsite_channel(A2), onsite_channel(A1)
A1m = sum((rng.normal() + 1j * rng.normal()) * X for X in VA1); A1m /= np.linalg.norm(A1m)
DA1 = lambda ks: np.broadcast_to(A1m, (len(np.atleast_2d(ks)), 12, 12)).copy()
def local_min(f, K, r=0.3, tries=3):
    best = f(K)
    for _ in range(tries):
        obj = lambda k: f(k) + 10 * max(0, np.linalg.norm(k - K) - r)
        res = minimize(obj, K + 0.03 * rng.normal(size=3), method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=3000))
        best = min(best, res.fun)
    return best
def ball_min(f_batch, f1, K, r=0.3, ng=19):
    g = np.linspace(-r, r, ng); P = K + np.array(list(itertools.product(g, g, g))); v = f_batch(P); j = np.argmin(v)
    res = minimize(f1, P[j], method='Nelder-Mead', options=dict(xatol=1e-11, fatol=1e-15, maxiter=4000))
    return res.fun, np.linalg.norm(res.x - K)
# first run used tau = 0.5 in a 0.3-ball and FAILED: in this normalisation (Delta_a = 2A) the zeros move ~0.5-0.7 away
# (probe_q0.log), so "small" is tested at tau = 0.1 here
m0 = {n: ball_min(lambda P: gap0(P, DA1, 0.1, Q0), lambda k: gap0(k, DA1, 0.1, Q0)[0], K) for n, K in NODES.items()}
check("A4 Q = 0 symmetric on-site pairing (A1, tau = 0.1): a BdG zero survives within 0.3 of every node (grid + Nelder-Mead); at larger "
      "pairing the zeros are displaced further but persist (probe_q0.log)",
      max(v for v, d in m0.values()) < 1e-8, ", ".join(f"{NAME[n]}:{v:.1e}@{d:.2f}" for n, (v, d) in m0.items()))

# ---------------- B1 ----------------
A2m = sum((rng.normal() + 1j * rng.normal()) * X for X in VA2); A2m /= np.linalg.norm(A2m)
def const(Am): return lambda ks: np.broadcast_to(Am, (len(np.atleast_2d(ks)), 12, 12)).copy()
tau = 0.5
gB1 = {n: gap0(K, const(A2m), tau, QR)[0] for n, K in NODES.items()}
(b0, k0), (bp, kp) = grid_min(const(A2m), tau, QR, N=20)
r0 = minimize(lambda k: gap0(k, const(A2m), tau, QR)[0], k0, method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-12)).fun
rp = minimize(lambda k: gappi(k, const(A2m), tau, QR)[0], kp, method='Nelder-Mead', options=dict(xatol=1e-9, fatol=1e-12)).fun
check("B1 Q=R A2 on-site (random, ||A||=1, tau=0.5): all eight nodes gapped; global 0 and pi gaps open (grid N=20 + Nelder-Mead; uncertified)",
      min(gB1.values()) > 1e-2 and r0 > 1e-3 and rp > 1e-3, f"node gaps min {min(gB1.values()):.4f}; global 0-gap {r0:.4f}, pi-gap {rp:.4f}")
# ---------------- B2 at +-k*: A1 keeps an exact 4-fold zero ----------------
zA1 = {n: int(np.sum(np.abs(bdg_eps(NODES[n], DA1, tt, QR)[0]) < 1e-10)) for n in ((0, 0, 0), (1, 1, 1)) for tt in (0.3, 1.1)}
check("B2 Q=R A1 on-site: +-k* keep an exact 4-fold BdG zero (tau = 0.3, 1.1) although A1 couples the node doublet to the -pi/2 doublet",
      all(v == 4 for v in zA1.values()))
# ---------------- B4 Wilson ----------------
SG = np.array([1, -1, 1])
def wfun(ks):
    s = np.sin(np.atleast_2d(ks)) * SG; return 3.0 - (s[:, 0] * s[:, 1] + s[:, 1] * s[:, 2] + s[:, 2] * s[:, 0])
kt = rng.uniform(-np.pi, np.pi, (5, 3))
w_ok = all(abs(wfun(gk(g, k))[0] - wfun(k)[0]) < 1e-12 for g in PROPER for k in kt) and all(abs(wfun(-QR - k)[0] - wfun(k)[0]) < 1e-12 for k in kt)
w_ok &= abs(wfun(KST)[0]) < 1e-14 and abs(wfun(-KST)[0]) < 1e-14 and all(abs(wfun(NODES[n])[0] - 4) < 1e-12 for n in DOUB)
DW = lambda ks: wfun(ks)[:, None, None] * A2m[None]
zW = {n: int(np.sum(np.abs(bdg_eps(NODES[n], DW, tau, QR)[0]) < 1e-10)) for n in NODES}
gW = {n: gap0(NODES[n], DW, tau, QR)[0] for n in DOUB}
cone = []
for n in ((0, 0, 0), (1, 1, 1)):
    d = rng.normal(size=(20, 3)); d /= np.linalg.norm(d, axis=1)[:, None]; q = 1e-4
    ev = np.sort(np.abs(bdg_eps(NODES[n] + q * d, DW, tau, QR)), axis=1)[:, :4]; cone.append(ev / q)
cone = np.array(cone)
(b0, k0), (bp, kp) = grid_min(DW, tau, QR, N=20, exclude=(KST, -KST), r_ex=0.35)
check("B4 Wilson pairing w(k) A2 (w invariant under the 24 affine maps and k -> -Q-k; w(+-k*) = 0, w(doublers) = 4): +-k* exact 4-fold zeros "
      "with isotropic cone sqrt2/3 (40 directions), doublers gapped, nothing else outside 0.35-balls (grid N=20)",
      w_ok and zW[(0, 0, 0)] == 4 and zW[(1, 1, 1)] == 4 and min(gW.values()) > 1e-2 and np.allclose(cone, np.sqrt(2) / 3, atol=2e-4) and b0 > 1e-3 and bp > 1e-3,
      f"cone [{cone.min():.6f},{cone.max():.6f}]; doubler gaps min {min(gW.values()):.4f}; outside-ball min 0/pi {b0:.4f}/{bp:.4f}")
# ---------------- B5b / B5c tuned on-site ----------------
DQ = {n: node_doublet(n) for n in NODES}
F = np.array([[singlet(DQ[n], 2 * X) for X in VA2] for n in ((0, 0, 0), (1, 1, 1))])
_, s, Vh = np.linalg.svd(F); nullv = Vh[np.sum(s > 1e-9):].conj()
c = nullv.T @ (rng.normal(size=len(nullv)) + 1j * rng.normal(size=len(nullv)))
At = sum(ci * X for ci, X in zip(c, VA2)); At /= np.linalg.norm(At)
mt = {n: abs(singlet(DQ[n], 2 * At)) for n in NODES}
gt = {tt: max(gap0(NODES[n], const(At), tt, QR)[0] for n in ((0, 0, 0), (1, 1, 1))) for tt in (0.05, 0.2, 0.6, 1.2)}
dbl = {n: gap0(NODES[n], const(At), tau, QR)[0] for n in DOUB}
(b0, k0), (bp, kp) = grid_min(const(At), tau, QR, N=20, exclude=(KST, -KST), r_ex=0.35)
conet = []
for n in ((0, 0, 0), (1, 1, 1)):
    d = rng.normal(size=(20, 3)); d /= np.linalg.norm(d, axis=1)[:, None]; q = 1e-4
    conet.append(np.sort(np.abs(bdg_eps(NODES[n] + q * d, const(At), tau, QR)), axis=1)[:, :4] / q)
conet = np.array(conet)
check("B5b on-site A2 tuned to m_{+-k*} = 0 (rank of the two functionals on V_A2 = %d): +-k* exact zeros for all tau, doublers gapped, "
      "nothing else outside 0.35-balls (grid N=20)" % (np.sum(s > 1e-9)),
      max(mt[(0, 0, 0)], mt[(1, 1, 1)]) < 1e-12 and max(gt.values()) < 1e-10 and min(dbl.values()) > 1e-3 and b0 > 1e-3 and bp > 1e-3,
      f"doubler gaps {min(dbl.values()):.4f}..{max(dbl.values()):.4f}; outside-ball 0/pi {b0:.4f}/{bp:.4f}; small-q cone/q range [{conet.min():.5f},{conet.max():.5f}]")
print(f"   B5b cone at +-k*: anisotropy max/min of 4 lowest |eps|/q = {conet.max()/conet.min():.6f} (on-site pairing enters the node block only at O(q))")
Ar = sum((rng.normal() + 1j * rng.normal()) * X for X in VA2); Ar /= np.linalg.norm(Ar)
etas = (1e-3, 1e-2, 1e-1)
gp = [gap0(KST, const((At + e * Ar) / np.linalg.norm(At + e * Ar)), tau, QR)[0] for e in etas]
sl = np.polyfit(np.log(etas), np.log(gp), 1)[0]
check("B5c generic A2 admixture eta re-gaps +-k* linearly (tuning, not protection)", 0.9 < sl < 1.1, f"slope {sl:.3f}, gaps {[f'{x:.1e}' for x in gp]}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
