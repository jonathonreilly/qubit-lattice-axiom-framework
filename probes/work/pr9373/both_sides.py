#!/usr/bin/env python3
"""J:attack-b:PR9373 -- SAME TEST, BOTH SIDES: the note states its results 'at both f+ and f-' and says the resultant is 'the same at f-'; the charge-two statement separates the merged touching from an isolated Weyl point (charge one) and from a generic point (no touching).

Applies the identical tests to both objects in every representation the note uses, with own network and own algebra (40-digit effective Hamiltonian in an orthonormal kernel basis, exact where possible):
  (1) f+ against f-: the spectrum, c, the u^2 coefficient of D (Hessian), |n|, the transverse forms' resultant, and the discrete sphere fluxes (radii 0.004, 0.008) at six values of q; expected: everything equal except the sign of the flux (-2 against +2);
  (2) the same flux test on a comparison object the note's claim separates the touching from: a generic point (gap open: flux 0), and a nearby simple Weyl point (charge one) of the same network at the coupling J = 1, kappa = 0.45 (below the handover, node (0.3680, 0.6320, 0) of open PR 9350's line family): the flux test must return
      +-1 there, not +-2, so that '2' separates and does not merely count the two touching bands;
  (3) the same test at q = 1/2 with radii from 0.02 to 0.3 around f+, to show that the value does not depend on the radius in that range.
Prints SUMMARY:; HIT only if a same-test comparison fails.
"""
import sys, time, itertools
import numpy as np
import sympy as sp
import mpmath as mp
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
T0 = time.time()
# ---------------------------------------------------------------- own network construction (site, flavour and Bloch-cell rules)
def is_site(p):
    i, j, z = p; m = z % 4
    if m == 0: return j % 2 == 0
    if m == 1: return i % 2 == 1
    if m == 2: return j % 2 == 1
    return i % 2 == 0
def nbrs(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q): out.append(q)
    return out
def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0: return "z"
    lo = p if sum(d) > 0 else q; m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]
def reduce(p):
    n3 = p[2] // 2; x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2; rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)
def terms_of(Jx, Jy, Jz, kappa):
    J = {"x": Jx, "y": Jy, "z": Jz}; out = []
    for p in REPS:
        a, _ = reduce(p)
        if sum(p) % 2 == 0:
            for q in nbrs(p):
                b, n = reduce(q); out.append((a, b, n, 2 * J[flavour(p, q)]))
        nb = {flavour(p, q): q for q in nbrs(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(x) for x in np.subtract(n2, n1)), 2 * kappa))
    return out
def M_sym(z1, z2, z3, Jx, Jy, Jz, kappa):
    M = sp.zeros(4, 4)
    for (a, b, n, amp) in terms_of(Jx, Jy, Jz, kappa):
        e = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += amp * e; M[b, a] -= amp / e
    return M

# ---------------------------------------------------------------- (2) effective Hamiltonian, weighted degree four, resultant (mpmath, 40 digits)
mp.mp.dps = 40
def setup(qv, sg):
    qq = mp.mpf(qv); NQn = 1 + 4 * qq ** 2; J = 8 * qq ** 2 / NQn
    T = terms_of(1, 1, J, qq)
    z0 = (2 * qq + sg * 1j * mp.mpf(1)) ** 2 / NQn
    x = mp.arg(z0) / (2 * mp.pi)
    f0 = [x, 1 - x, mp.mpf(1) / 2]
    return qq, J, T, f0
def Hnum(T, f):
    M = mp.zeros(4, 4)
    for (a, b, n, amp) in T:
        ph = mp.expjpi(2 * sum(n[j] * f[j] for j in range(3)))
        M[a, b] += amp * ph; M[b, a] -= amp * mp.conj(ph)
    return 1j * M
def derivs(T, f0):
    H0 = Hnum(T, f0); Hj = [mp.zeros(4, 4) for _ in range(3)]; Hjk = {}
    for j in range(3):
        for k in range(j, 3): Hjk[(j, k)] = mp.zeros(4, 4)
    for (a, b, n, amp) in T:
        ph = mp.expjpi(2 * sum(n[j] * f0[j] for j in range(3)))
        for j in range(3):
            Hj[j][a, b] += 1j * amp * ph * (2j * mp.pi * n[j]); Hj[j][b, a] += 1j * amp * mp.conj(ph) * (2j * mp.pi * n[j])   # d/d delta of -amp*conj(ph) is -amp*(-2 pi i n) conj(ph)
            for k in range(j, 3):
                Hjk[(j, k)][a, b] += 1j * amp * ph * (2j * mp.pi) ** 2 * n[j] * n[k]
                Hjk[(j, k)][b, a] -= 1j * amp * mp.conj(ph) * (-2j * mp.pi) ** 2 * n[j] * n[k]
    return H0, Hj, Hjk
def analyse(qv, sg):
    qq, J, T, f0 = setup(qv, sg)
    H0, Hj, Hjk = derivs(T, f0)
    c = 256 * qq ** 2 * (8 * qq ** 2 + 1) / (4 * qq ** 2 + 1) ** 2
    E, Ev = mp.eigh(H0)
    ker = [i for i in range(4) if abs(E[i]) < mp.mpf(10) ** -25]
    assert len(ker) == 2 and abs(sorted([E[i] for i in range(4)])[3] ** 2 - c) < mp.mpf(10) ** -30
    K = mp.matrix(4, 2)
    for a_, i in enumerate(ker):
        for r in range(4): K[r, a_] = Ev[r, i]
    Qm = mp.eye(4) - K * K.H
    def pieces(u, v, t):
        d = [(v + u) / 2, (v - u) / 2, t]
        V1 = sum((Hj[j] * d[j] for j in range(3)), mp.zeros(4, 4)) if False else None
    def heff(u, v, t):
        dv = [v / 2, v / 2, t]; du = [u / 2, -u / 2, 0]
        V1 = sum((Hj[j] * dv[j] for j in range(3)), mp.zeros(4, 4))
        W2 = sum((Hj[j] * du[j] for j in range(3)), mp.zeros(4, 4))
        for (j, k), X in Hjk.items(): W2 += X * dv[j] * dv[k] * (mp.mpf(1) / 2 if j == k else 1)
        first = K.H * V1 * K
        second = K.H * W2 * K - K.H * V1 * Qm * (H0 / c) * Qm * V1 * K
        return first, second
    def pauli(h): return mp.re((h[0, 0] + h[1, 1]) / 2), mp.matrix([mp.re(h[0, 1]), -mp.im(h[0, 1]), mp.re((h[0, 0] - h[1, 1]) / 2)])
    first_max = max(abs(x) for M_ in (heff(0, 1, 0)[0], heff(0, 0, 1)[0], heff(0, 1, 1)[0]) for x in M_)
    n = pauli(heff(1, 0, 0)[1])[1]; idu = abs(pauli(heff(1, 0, 0)[1])[0])
    Q2 = {}
    for name, (a_, b_) in (("v", (1, 0)), ("t", (0, 1)), ("vt", (1, 1))):
        Q2[name] = pauli(heff(0, a_, b_)[1])
    idq = max(abs(Q2[k][0]) for k in Q2)
    qv_ = Q2["v"][1]; qt_ = Q2["t"][1]; qvt_ = Q2["vt"][1] - qv_ - qt_
    def dvec(u, v, t): return n * u + qv_ * v ** 2 + qt_ * t ** 2 + qvt_ * v * t
    return dict(qq=qq, c=c, J=J, T=T, f0=f0, n=n, first=first_max, idu=idu, idq=idq, dvec=dvec, qforms=(qv_, qt_, qvt_))
def D_eps_coeff4(qv, sg, u, v, t):
    qq, J, T, f0 = setup(qv, sg)
    def Deps(eps):
        d = [(eps * v + eps ** 2 * u) / 2, (eps * v - eps ** 2 * u) / 2, eps * t]
        return mp.det(Hnum(T, [f0[j] + d[j] for j in range(3)]))
    return mp.taylor(Deps, 0, 4)
def resultant(qforms):
    qv_, qt_, qvt_ = qforms
    return qv_, qt_, qvt_
# ---------------------------------------------------------------- (3) sphere fluxes (Fukui links), own implementation
def Hfloat(F, T):
    F = np.atleast_2d(F); Mk = np.zeros((len(F), 4, 4), dtype=complex)
    for (a, b, n, amp) in T:
        ph = np.exp(2j * np.pi * (F @ np.array(n, dtype=float)))
        Mk[:, a, b] += float(amp) * ph; Mk[:, b, a] -= float(amp) * np.conj(ph)
    return 1j * Mk
def link(A_, B_): return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))
def sphere_chern(T, c, s, m=64, nocc=2):
    th = np.linspace(0, np.pi, m + 1); ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    P = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :], np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + np.array(c)
    ev, V = np.linalg.eigh(Hfloat(P.reshape(-1, 3), T))
    V = V[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy(); V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    pl = np.angle(link(V[:-1, :-1], V[1:, :-1]) * link(V[1:, :-1], V[1:, 1:]) * link(V[1:, 1:], V[:-1, 1:]) * link(V[:-1, 1:], V[:-1, :-1]))
    return float(pl.sum() / (2 * np.pi)), float((ev[:, 2] - ev[:, 1]).min())

mp.mp.dps = 40
def res_true(r):
    n = r["n"]; n2 = sum(x ** 2 for x in n); nn = n / mp.sqrt(n2)
    e1 = mp.matrix([nn[1], -nn[0], 0]); e1 = e1 / mp.sqrt(sum(x ** 2 for x in e1)); e2 = mp.matrix([nn[1] * e1[2] - nn[2] * e1[1], nn[2] * e1[0] - nn[0] * e1[2], nn[0] * e1[1] - nn[1] * e1[0]])
    qv_, qt_, qvt_ = r["qforms"]
    A = [sum(e1[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]; B = [sum(e2[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]
    a0, a1, a2 = A; b0, b1, b2 = B
    return (a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)
ok_eq = True; rows = []
for qs_ in ["0.2", "0.3333333333333333", "0.5", "1", "2", "5"]:
    rp = analyse(qs_, 1); rm = analyse(qs_, -1)
    qq = rp["qq"]
    D2 = lambda r: r["c"] * sum(x ** 2 for x in r["n"])
    same = abs(rp["c"] - rm["c"]) < mp.mpf(10) ** -30 and abs(D2(rp) - D2(rm)) < mp.mpf(10) ** -28 * D2(rp) and abs(sum(x ** 2 for x in rp["n"]) - sum(x ** 2 for x in rm["n"])) < mp.mpf(10) ** -28 * sum(x ** 2 for x in rp["n"])
    Rp, Rm = res_true(rp), res_true(rm)
    same &= abs(Rp - Rm) < mp.mpf(10) ** -25 * abs(Rp) and Rp < 0 and Rm < 0
    T = terms_of(1.0, 1.0, float(8 * qq ** 2 / (1 + 4 * qq ** 2)), float(qq))
    x = float(np.arctan2(4 * float(qq), 4 * float(qq) ** 2 - 1) / (2 * np.pi)) % 1.0
    fp = [round(sphere_chern(T, (x, 1 - x, 0.5), r_, m=48)[0], 3) for r_ in (0.004, 0.008)]
    fm = [round(sphere_chern(T, (1 - x, x, 0.5), r_, m=48)[0], 3) for r_ in (0.004, 0.008)]
    same &= fp == [-2.0, -2.0] and fm == [2.0, 2.0]
    ok_eq &= same; rows.append((qs_, fp, fm))
check("at six q, f+ and f- give equal c, equal u^2 coefficient of D, equal |n| and equal negative transverse resultant, and fluxes -2 (f+) and +2 (f-) at both radii: the note's 'the same at f-' holds under the identical test", ok_eq, "; ".join(f"q = {r[0]}: fluxes {r[1]} / {r[2]}" for r in rows))
# comparison objects
Tc = terms_of(1.0, 1.0, 1.0, 0.45)
g = np.load if False else None
def gap(f):
    ev = np.linalg.eigvalsh(Hfloat(np.asarray(f), Tc))[0]; return ev[2] - ev[1]
from scipy.optimize import minimize
r0 = minimize(gap, np.array([0.368, 0.632, 0.0]), method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-15, maxiter=4000))
w = np.mod(r0.x, 1.0)
fw = [round(sphere_chern(Tc, w, r_, m=48)[0], 3) for r_ in (0.004, 0.008)]
generic = [round(sphere_chern(Tc, (0.13, 0.41, 0.27), r_, m=48)[0], 3) for r_ in (0.004, 0.008)]
check("the same flux test on a simple Weyl point of the same network (J = 1, kappa = 0.45, the line node near (0.368, 0.632, 0), gap %.1e at the located point) returns magnitude 1, and on a generic gapped point returns 0: the value 2 separates the merged touchings from both" % r0.fun,
      r0.fun < 1e-9 and all(abs(abs(v) - 1) < 1e-9 for v in fw) and all(abs(v) < 1e-9 for v in generic), f"line node {np.round(w, 6)}: fluxes {fw}; generic point: {generic}")
big = [round(sphere_chern(terms_of(1.0, 1.0, 1.0, 0.5), (0.25, 0.75, 0.5), r_, m=48)[0], 3) for r_ in (0.02, 0.05, 0.1, 0.2, 0.3)]
print(f"   flux around f+ at q = 1/2 for radii 0.02, 0.05, 0.1, 0.2, 0.3: {big}")
check("the identical test at q = 1/2 gives -2 at every radius from 0.02 to 0.3 around f+ (the ball contains no other node), so the value does not depend on the radius within that range", all(v == -2.0 for v in big))
print(f"   total {time.time() - T0:.0f}s")
if not HITS:
    print("SUMMARY: no purchase: the identical tests give identical results at f+ and f- except the sign of the flux, and the flux test separates the merged touching (magnitude two) from a simple Weyl point (one) and a generic point (zero) of the same network")
else:
    print("SUMMARY: a same-test comparison fails: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)
