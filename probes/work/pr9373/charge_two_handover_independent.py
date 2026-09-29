#!/usr/bin/env python3
"""J:falsifier:PR9373 -- independent check of 'the flux-free comparator's merged touchings at the handover are exact charge-two points for every J in (0,2)'.

Own construction of the four-site Bloch matrix from the site/colour/flavour rules of the composite-site network (the runner's network definition is re-coded here, then validated by the note's own
J = 1 numbers c = 48 and Hessian 192); then, with own algebra:
  (1) symbolic in q (sympy, exact): det(H - lambda) = lambda^2 (lambda^2 - c) with c = 256 q^2 (8q^2+1)/(4q^2+1)^2 at f+ and f-; D = det H, its gradient vanish; its Hessian is 4 pi^2 h(q) (1,-1,0)(1,-1,0)^T with h(q) as stated;
  (2) 40-digit mpmath at six rational q: own Schrieffer-Wolff effective two-level Hamiltonian in an orthonormal kernel basis to weighted order two (u weight 2; v, t weight 1): no first-order part, no identity part, and the
      true Pauli vector n has |n|^2 = 2 pi^2 h / c (so c |n|^2 u^2 is D's u^2 term); the whole weighted-degree-4 part of D (from an eps-Taylor series of det M) equals c |d|^2 at random (u, v, t);
      the two quadratic forms transverse to n have a negative resultant, on a dense q grid as well;
  (3) own Fukui-link Chern numbers of the lowest two bands on spheres of radius .004 and .008 around f+ and f- at J = 2/5 (kappa = 1/4) and J = 8/5 (kappa = 1), and a scan of further q.
Prints SUMMARY:; HIT: only if a stated identity or sign fails.
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

# ---------------------------------------------------------------- (1) exact algebra in q
q = sp.symbols('q', positive=True); z1, z2, z3, lam = sp.symbols('z1 z2 z3 lam')
NQ = 1 + 4 * q ** 2; Jq = 8 * q ** 2 / NQ
Msym = M_sym(z1, z2, z3, 1, 1, Jq, q)
Dsym = sp.factor(sp.together(Msym.det()))
def z0sym(sg): return (2 * q + sg * sp.I) ** 2 / NQ
c_formula = 256 * q ** 2 * (8 * q ** 2 + 1) / NQ ** 2
h_formula = 512 * q ** 2 * (8 * q ** 2 + 1) * (128 * q ** 6 + 16 * q ** 4 + 16 * q ** 2 + 1) / NQ ** 4
# validation of my reconstruction of the network against the note's own J = 1 numbers
M12 = M_sym(z1, z2, z3, 1, 1, 1, sp.Rational(1, 2)); sub12 = {z1: sp.I, z2: -sp.I, z3: -1}
check("network reconstruction: at J = 1, kappa = 1/2 and f+ = (1/4, 3/4, 1/2) the characteristic polynomial is lambda^2 (lambda^2 - 48)", sp.expand((sp.I * M12.subs(sub12) - lam * sp.eye(4)).det()) == lam ** 4 - 48 * lam ** 2)
ok_cp = ok_grad = ok_hess = True
for sg in (1, -1):
    sub = {z1: z0sym(sg), z2: sp.conjugate(z0sym(sg)), z3: -1}
    H0 = sp.I * Msym.subs(sub)
    cp = sp.expand((H0 - lam * sp.eye(4)).det())
    ok_cp &= sp.simplify(cp - lam ** 2 * (lam ** 2 - c_formula)) == 0
    zs = [z1, z2, z3]
    ok_grad &= sp.simplify(Dsym.subs(sub)) == 0 and all(sp.simplify((2 * sp.pi * sp.I * zs[j] * sp.diff(Dsym, zs[j])).subs(sub)) == 0 for j in range(3))
    Hess = sp.zeros(3, 3)
    for j in range(3):
        dj = 2 * sp.pi * sp.I * zs[j] * sp.diff(Dsym, zs[j])
        for k in range(3): Hess[j, k] = sp.simplify((2 * sp.pi * sp.I * zs[k] * sp.diff(dj, zs[k])).subs(sub))
    ok_hess &= (Hess - 4 * sp.pi ** 2 * h_formula * sp.Matrix([[1, -1, 0], [-1, 1, 0], [0, 0, 0]])).applyfunc(sp.simplify) == sp.zeros(3, 3)
check("for every q > 0 (symbolic in q): det(H - lambda) = lambda^2 (lambda^2 - c) with c = 256 q^2 (8q^2+1)/(4q^2+1)^2 at both f+ and f-", ok_cp, f"{time.time()-T0:.0f}s")
check("for every q > 0: D = det H and its gradient vanish at f+ and f-", ok_grad)
check("for every q > 0: the Hessian of D at f+ and f- equals 4 pi^2 h(q) (1,-1,0)(1,-1,0)^T with h(q) = 512 q^2 (8q^2+1)(128q^6+16q^4+16q^2+1)/(4q^2+1)^4 (h(1/2) = 192)", ok_hess and h_formula.subs(q, sp.Rational(1, 2)) == 192, f"{time.time()-T0:.0f}s")

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
rng = np.random.default_rng(3)
qs = ["0.2", "0.3333333333333333", "0.5", "1", "2", "5"]
ok_first = ok_id = ok_norm = ok_d4 = ok_res = True; details = []
for qs_ in qs:
    for sg in (1, -1):
        r = analyse(qs_, sg); qq = r["qq"]
        h = 512 * qq ** 2 * (8 * qq ** 2 + 1) * (128 * qq ** 6 + 16 * qq ** 4 + 16 * qq ** 2 + 1) / (4 * qq ** 2 + 1) ** 4
        n2 = sum(x ** 2 for x in r["n"])
        ok_first &= r["first"] < mp.mpf(10) ** -30
        ok_id &= r["idu"] < mp.mpf(10) ** -30 and r["idq"] < mp.mpf(10) ** -30
        ok_norm &= abs(n2 - 2 * mp.pi ** 2 * h / r["c"]) < mp.mpf(10) ** -28
        u_, v_, t_ = [mp.mpf(str(x)) for x in rng.uniform(-1, 1, 3)]
        coeffs = D_eps_coeff4(qs_, sg, u_, v_, t_)
        d = r["dvec"](u_, v_, t_); lhs = mp.re(coeffs[4]); rhs = r["c"] * sum(x ** 2 for x in d)
        ok_d4 &= abs(lhs - rhs) < mp.mpf(10) ** -18 * max(1, abs(rhs))
        low = [abs(mp.re(coeffs[k])) + abs(mp.im(coeffs[k])) for k in range(4)]
        ok_d4 &= max(low) < mp.mpf(10) ** -18
        # transverse forms and their resultant
        n = r["n"]; nn = n / mp.sqrt(n2)
        e1 = mp.matrix([nn[1], -nn[0], 0]); e1 = e1 / mp.sqrt(sum(x ** 2 for x in e1)) if abs(nn[2]) < 1 - mp.mpf(10) ** -12 and (abs(nn[0]) + abs(nn[1])) > mp.mpf(10) ** -12 else mp.matrix([0, 1, 0])
        e2 = mp.matrix([nn[1] * e1[2] - nn[2] * e1[1], nn[2] * e1[0] - nn[0] * e1[2], nn[0] * e1[1] - nn[1] * e1[0]])
        qv_, qt_, qvt_ = r["qforms"]
        A = [sum(e1[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]; B = [sum(e2[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]
        a0, a1, a2 = A; b0, b1, b2 = B
        res = (a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)
        ok_res &= res < 0
        details.append((qs_, sg, mp.nstr(res, 6)))
check("effective Hamiltonian to weighted order two (own orthonormal kernel basis, Schrieffer-Wolff with H^-1 = H/c on the complement): no first-order (v, t) part and no identity part at six q, both f+ and f-", ok_first and ok_id, f"{time.time()-T0:.0f}s")
check("the true Pauli vector has |n|^2 = 2 pi^2 h(q)/c(q) exactly, so c|n|^2 u^2 is D's u^2 term (40 digits, six q, f+ and f-)", ok_norm)
check("D's expansion at d1 = (eps v + eps^2 u)/2, d2 = (eps v - eps^2 u)/2, d3 = eps t: orders eps^0..eps^3 vanish and the eps^4 coefficient equals c |d|^2 (d = n u + quadratic(v, t)) at random (u, v, t)", ok_d4)
check("the homogeneous resultant of the two quadratic forms transverse to n is negative at all twelve (q, f+-) cases", ok_res, str(details[:4]) + " ...")
# dense q scan of the resultant sign and of the zero-level identity
qgrid = [mp.mpf(x) for x in np.geomspace(0.02, 30, 24)]
ok_scan = True; mins = []
for qq in qgrid:
    r = analyse(str(qq), 1); n = r["n"]; n2 = sum(x ** 2 for x in n); nn = n / mp.sqrt(n2)
    if abs(nn[2]) > 1 - mp.mpf(10) ** -12: continue
    e1 = mp.matrix([nn[1], -nn[0], 0]); e1 = e1 / mp.sqrt(sum(x ** 2 for x in e1))
    e2 = mp.matrix([nn[1] * e1[2] - nn[2] * e1[1], nn[2] * e1[0] - nn[0] * e1[2], nn[0] * e1[1] - nn[1] * e1[0]])
    qv_, qt_, qvt_ = r["qforms"]
    A = [sum(e1[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]; B = [sum(e2[k] * w[k] for k in range(3)) for w in (qv_, qvt_, qt_)]
    a0, a1, a2 = A; b0, b1, b2 = B
    res = (a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)
    # normalise by the fourth power of the transverse-form scale so the sign test is not a tiny-number artefact
    scale = max(abs(x) for x in A + B) ** 4
    ok_scan &= res < 0; mins.append(float(res / scale))
check(f"resultant sign scan: negative at all {len(mins)} q in a geometric grid 0.02..30 (largest normalised value {max(mins):.3g})", ok_scan and len(mins) > 15)
print(f"   ({time.time()-T0:.0f}s)", flush=True)

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
flux = {}
for qq in (0.25, 1.0, 0.5, 3.0):
    J = 8 * qq ** 2 / (1 + 4 * qq ** 2); T = terms_of(1.0, 1.0, J, qq)
    x = (np.arctan2(4 * qq, 4 * qq ** 2 - 1) / (2 * np.pi)) % 1.0
    flux[qq] = {sg: [round(sphere_chern(T, (x, 1 - x, 0.5) if sg > 0 else (1 - x, x, 0.5), r_)[0], 3) for r_ in (0.004, 0.008)] for sg in (1, -1)}
    print(f"   q = {qq}: J = {J:.4f}; sphere fluxes (radii .004, .008) at f+: {flux[qq][1]}, at f-: {flux[qq][-1]}", flush=True)
check("sphere fluxes of the lowest two bands at J = 2/5 (kappa = 1/4) and J = 8/5 (kappa = 1): magnitude two at f+ and f- on both radii, opposite between f+ and f-", all(abs(abs(v_) - 2) < 0.01 for q_ in (0.25, 1.0) for sg in (1, -1) for v_ in flux[q_][sg]) and all(flux[q_][1][0] * flux[q_][-1][0] < 0 for q_ in (0.25, 1.0)), f"{flux[0.25]}, {flux[1.0]}")
check("the same holds at the further couplings q = 1/2 (J = 1, the case of open PR 9357) and q = 3 (J = 72/37)", all(abs(abs(v_) - 2) < 0.01 for q_ in (0.5, 3.0) for sg in (1, -1) for v_ in flux[q_][sg]), f"{flux[0.5]}, {flux[3.0]}")
print(f"   total {time.time()-T0:.0f}s")
if not HITS:
    print(f"SUMMARY: no falsifier fires: an independently built four-site Bloch matrix reproduces the note's identities exactly for every q (det(H - lambda) = lambda^2 (lambda^2 - c), D and its gradient vanish, Hessian 4 pi^2 h (1,-1,0)(1,-1,0)^T) and, in 40-digit arithmetic at six q, the absence of first-order and identity terms, |n|^2 = 2 pi^2 h/c, the weighted-degree-4 identity D_4 = c |d|^2 and the negative resultant (also on a 24-point q grid); the sphere fluxes are magnitude two, opposite at f+ and f-, at four couplings; {PASS} checks pass. Presentation only: the note's printed n is the derivative of a non-orthonormal-basis d (its |n|^2 differs from the true Pauli vector's).")
else:
    print("SUMMARY: failed: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)
