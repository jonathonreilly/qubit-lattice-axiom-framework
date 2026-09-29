#!/usr/bin/env python3
"""Composite-site network, flux-free comparator: the handover touchings are exact charge-two points for every J in (0, 2).

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings
J_x = J_y = 1, J_z = J, odd term kappa, four-site Bloch matrix H(f) = i M(f). Open PR 9350 found the touchings of the plane family
f1 + f2 = 1 hand over to the plane family f1 + f2 = 2 f3 at kappa_h^2 = J/[4(2 - J)]. Parametrise by q > 0: kappa = q,
J = 8 q^2/(1 + 4 q^2), which runs once over (0, 2) and gives kappa = kappa_h. The merged touchings are f+- = (x, 1 - x, 1/2) with
e^{2 pi i x} = (2q +- i)^2/(1 + 4q^2), a rational point of the circle, so every quantity below is a rational function of q (sympy).
Checks: (1) at kappa = kappa_h both families of open PR 9350 give f+-; (2) D = det H vanishes with its gradient at f+-, its Hessian is
a positive multiple of (1, -1, 0)(1, -1, 0)^T, and with u = d1 - d2 (weight two), v = d1 + d2, t = d3 (weight one) D vanishes to
weighted order three; (3) det(H - lambda) = lambda^2 (lambda^2 - c) with c = 256 q^2 (8q^2 + 1)/(4q^2 + 1)^2; (4) the effective
two-level Hamiltonian to weighted order two (kernel projector, H^-1 = H/c on its complement) has no first-order (v, t) part and no
identity part, and its Pauli vector is n u + quadratic(v, t) with n != 0; (5) D's weighted-degree-4 part equals c |d|^2 exactly, so it is
positive definite once d has an isolated zero; (6) the homogeneous resultant of the two components of the quadratic part transverse to
n is negative for every q > 0, so their zero directions interlace and d/|d| has local degree of magnitude two; (7) consistency
(floating point): sphere fluxes of the lowest two bands around f+ and f- at J = 2/5 and 8/5 are -2 and +2.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import time

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

AUDIT_TIMEOUT_SEC = 300

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""), flush=True)


AX = {"x": 0, "y": 1, "z": 2}


def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


A_VEC = np.array([[2, 0, 0], [0, 2, 0], [1, 1, 2]])       # rows: primitive translations of the site and colour rules
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]


def reduce(p):
    """p = rep + n1 a1 + n2 a2 + n3 a3 with rep in the 2x2x2 box; returns (rep index, n)."""
    n3 = p[2] // 2
    x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2
    rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)


def terms(J, kappa):
    """Real hopping terms (a, b, n, t): M(f)[a, b] += t e^{2 pi i f.n}, M(f)[b, a] -= t e^{-2 pi i f.n}, gauge u = +1."""
    out = []
    for p in REPS:
        a, n0 = reduce(p)
        assert n0 == (0, 0, 0) and is_site(p)
        if sum(p) % 2 == 0:
            for q in neighbours(p):
                b, n = reduce(q)
                out.append((a, b, n, 2.0 * J[AX[flavour(p, q)]]))
        if kappa:
            nb = {flavour(p, q): q for q in neighbours(p)}
            assert len(nb) == 3
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
                out.append((r1, r2, tuple(np.subtract(n2, n1)), 2.0 * kappa))
    return out


class Bloch:
    def __init__(self, J, kappa):
        self.T = terms(J, kappa)
        self.a = np.array([x[0] for x in self.T]); self.b = np.array([x[1] for x in self.T])
        self.n = np.array([x[2] for x in self.T], dtype=float); self.t = np.array([x[3] for x in self.T])
        # Lipschitz constant of every level in the sup-norm of the fractional momentum (Weyl's inequality, term by term)
        fac = np.where(self.a == self.b, 2.0, 1.0)
        self.lip = float(np.sum(fac * np.abs(self.t) * 2 * np.pi * np.abs(self.n).sum(axis=1)))

    def H(self, F):
        F = np.atleast_2d(F)
        ph = np.exp(2j * np.pi * F @ self.n.T)
        Mk = np.zeros((len(F), 4, 4), dtype=complex)
        for j in range(len(self.T)):
            Mk[:, self.a[j], self.b[j]] += self.t[j] * ph[:, j]
            Mk[:, self.b[j], self.a[j]] -= self.t[j] * np.conj(ph[:, j])
        return 1j * Mk

    def levels(self, F, vecs=False):
        return np.linalg.eigh(self.H(F)) if vecs else np.linalg.eigvalsh(self.H(F))


def _link(A_, B_):
    return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))


def _plaquettes(V):
    links = (_link(V[:-1, :-1], V[1:, :-1]), _link(V[1:, :-1], V[1:, 1:]),
             _link(V[1:, 1:], V[:-1, 1:]), _link(V[:-1, 1:], V[:-1, :-1]))
    assert all(np.isfinite(z).all() and np.min(np.abs(z)) > 1e-12 for z in links), 'singular occupied-band overlap'
    return np.angle(links[0] * links[1] * links[2] * links[3])


def sphere_chern(B, c, s, m=48, nocc=2):
    """Chern number of the lowest nocc bands on the sphere |f - c| = s (fractional coordinates, outward orientation), Fukui
    link method on a latitude-longitude grid with shared poles and a periodic seam. Also returns the smallest middle gap met."""
    th = np.linspace(0, np.pi, m + 1)
    ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    P = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :],
                  np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + c
    ev, V = B.levels(P.reshape(-1, 3), vecs=True)
    V = V[:, :, :nocc].reshape(m + 1, 2 * m + 1, 4, nocc).copy()
    V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    return _plaquettes(V).sum() / (2 * np.pi), float((ev[:, 2] - ev[:, 1]).min())



# ------------------------------------------------------------------------------------------------ exact algebra in q
q = sp.symbols("q", positive=True)
u, v, t, s, lam = sp.symbols("u v t s lam", real=True)
z1, z2, w3 = sp.symbols("z1 z2 w3")
NQ = 1 + 4 * q ** 2
JQ = 8 * q ** 2 / NQ
TERMS = terms((1.0, 1.0, 7.0), 0.3)                      # amplitude tags: 2 (J_x, J_y), 14 (J_z), 0.6 (kappa)


def amp_of(tt, A):
    return next(val for key, val in A.items() if abs(tt - key) < 1e-9)


def cjg(e):
    """Complex conjugate of an expression in I and real symbols."""
    return e.subs(sp.I, -sp.I)


def zpow(sign, a):
    """z0^a with z0 = (2q + sign i)^2/(1 + 4q^2), |z0| = 1."""
    return ((2 * q + sign * sp.I) ** (2 * a) if a >= 0 else (2 * q - sign * sp.I) ** (-2 * a)) / NQ ** abs(a)


def sign_for_positive_q(e):
    """+1 or -1 when every non-constant factor of e is a polynomial in q with positive coefficients (so e has that sign for all q > 0)."""
    num, den = sp.fraction(sp.cancel(sp.together(e)))
    for part in (num, den):
        c_, fs_ = sp.factor_list(part)
        for f_, _ in fs_:
            if not all(x > 0 for x in sp.Poly(f_, q).coeffs()):
                return None
    return int(sp.sign(sp.factor_list(num)[0] * sp.factor_list(den)[0]))


# D = det H as a Laurent polynomial, scaled by (1 + 4q^2)^4 so that its coefficients lie in QQ[q]
S0 = 2
AS = {2.0: 2 * NQ, 14.0: 16 * q ** 2, 0.6: 2 * q * NQ}
Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
for (a, b, n, tt) in TERMS:
    e = [int(x) for x in n]; amp = amp_of(tt, AS)
    Ms[int(a)][int(b)] += amp * z1 ** (S0 + e[0]) * z2 ** (S0 + e[1]) * w3 ** (S0 + e[2])
    Ms[int(b)][int(a)] -= amp * z1 ** (S0 - e[0]) * z2 ** (S0 - e[1]) * w3 ** (S0 - e[2])
RD = sp.QQ[q, z1, z2, w3]
DP = sp.Poly(RD.to_sympy(DomainMatrix([[RD.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), RD).det()), z1, z2, w3)
DT = [((m[0] - 4 * S0, m[1] - 4 * S0, m[2] - 4 * S0), c) for m, c in DP.terms()]
EMAX = max(abs(e[0]) + abs(e[1]) for e, _ in DT)
SCALE = NQ ** (EMAX + 4)                                  # moments below are the true ones times SCALE

# (1) the handover point of open PR 9350's families at kappa = q, J = 8q^2/(1 + 4q^2)
z0p = sp.expand((2 * q + sp.I) ** 2 / NQ)
cx = sp.cancel(sp.re(sp.expand_complex(z0p)))
kh2 = sp.cancel(JQ / (4 * (2 - JQ)))
fam2_x = sp.cancel(1 - JQ / (4 * q ** 2)); fam2_f3 = sp.cancel((JQ + 2) / (4 * q ** 2) - (4 + JQ - JQ ** 2) / JQ)
root = sp.cancel(5 * JQ ** 2 + 8 * JQ + JQ * (JQ + 2) / q ** 2)
fam3_f3 = sp.cancel((JQ + 2 - (JQ + 4)) / 2); fam3_g = sp.cancel(-JQ - fam3_f3)
ok1 = (sp.cancel(kh2 - q ** 2) == 0 and sp.cancel(root - (JQ + 4) ** 2) == 0 and sp.cancel(fam2_x - cx) == 0 and fam2_f3 == -1
       and fam3_f3 == -1 and sp.cancel(-fam3_g - cx) == 0 and sp.cancel(cx - (JQ - 1)) == 0 and sp.cancel(sp.im(sp.expand_complex(z0p)) - 4 * q / NQ) == 0
       and sign_for_positive_q(sp.diff(JQ, q)) == 1 and sp.limit(JQ, q, sp.oo) == 2)
check("at kappa = q, J = 8q^2/(1 + 4q^2) (q > 0 runs once over J in (0, 2)): kappa^2 = J/[4(2 - J)] = kappa_h^2, and both families of open "
      "PR 9350 reach f+- = (x, 1 - x, 1/2) with cos 2 pi x = J - 1 = (4q^2 - 1)/(4q^2 + 1), sin 2 pi x = +-4q/(4q^2 + 1)", ok1,
      f"family (ii): cos 2 pi x = {sp.factor(fam2_x)}, cos 2 pi f3 = {fam2_f3}; family (iii): sqrt(...) = J + 4, cos 2 pi f3 = {fam3_f3}, "
      f"cos 2 pi (1/2 + g) = {sp.factor(-fam3_g)}")


def moments(sign):
    ws = []
    for e, c in DT:
        ws.append((e, sp.expand(c * zpow(sign, e[0]) * NQ ** abs(e[0]) * zpow(-sign, e[1]) * NQ ** abs(e[1]) * (-1) ** (e[2] % 2)
                                * NQ ** (EMAX - abs(e[0]) - abs(e[1])))))
    return {(i, j, k): sp.expand(sum(w * e[0] ** i * e[1] ** j * e[2] ** k for e, w in ws))
            for i in range(5) for j in range(5 - i) for k in range(5 - i - j)}


def weighted_series(Sm):
    """Coefficients eps^0..eps^4 of D at d1 = (eps v + eps^2 u)/2, d2 = (eps v - eps^2 u)/2, d3 = eps t (times SCALE)."""
    a, b, c = sp.symbols("a b c")
    L = (a + b) / 2 * v + c * t; Q = (a - b) / 2 * u
    x = 2 * sp.pi * sp.I
    es = [sp.Integer(1), x * L, x * Q + x ** 2 * L ** 2 / 2, x ** 2 * L * Q + x ** 3 * L ** 3 / 6,
          x ** 2 * Q ** 2 / 2 + x ** 3 * L ** 2 * Q / 2 + x ** 4 * L ** 4 / 24]
    return [sp.expand(sum(coef * Sm[mon] for mon, coef in sp.Poly(sp.expand(em), a, b, c).terms())) for em in es]


def point_matrices(sign):
    """Exact H, dH/df_j and d2H/df_j df_k at f+ (sign = +1) or f- (sign = -1)."""
    A = {2.0: sp.Integer(1), 14.0: JQ, 0.6: q}                 # halves of the amplitudes 2 J_x, 2 J_y, 2 J_z, 2 kappa
    H0 = sp.zeros(4, 4); dH = [sp.zeros(4, 4) for _ in range(3)]; d2H = [[sp.zeros(4, 4) for _ in range(3)] for _ in range(3)]
    for (a, b, n, tt) in TERMS:
        amp = 2 * amp_of(tt, A); n = [int(x) for x in n]
        ph = zpow(sign, n[0]) * zpow(-sign, n[1]) * (-1) ** (n[2] % 2)
        for (r, c, sg, m, e) in ((int(a), int(b), 1, n, ph), (int(b), int(a), -1, [-x for x in n], zpow(-sign, n[0]) * zpow(sign, n[1]) * (-1) ** (n[2] % 2))):
            H0[r, c] += sp.I * sg * amp * e
            for j in range(3):
                dH[j][r, c] += sp.I * sg * amp * e * 2 * sp.pi * sp.I * m[j]
                for k in range(3):
                    d2H[j][k][r, c] += sp.I * sg * amp * e * (2 * sp.pi * sp.I) ** 2 * m[j] * m[k]
    return H0.applyfunc(sp.cancel), dH, d2H


def dot(a_, b_):
    return sp.cancel(sp.expand(sum(cjg(a_[i]) * b_[i] for i in range(4))))


RES = {}
for sign, name in ((1, "f+"), (-1, "f-")):
    Sm = moments(sign)
    Hq = sp.Matrix(3, 3, lambda j, k: Sm[tuple(int(x == j) + int(x == k) for x in range(3))])     # D_jk = -4 pi^2 Hq / SCALE
    ell = sp.Matrix([1, -1, 0])
    ser = weighted_series(Sm)
    H0, dH, d2H = point_matrices(sign)
    co = [sp.cancel(x) for x in H0.charpoly(lam).all_coeffs()]
    cc = -co[2]
    k0, k1 = H0.nullspace(simplify=sp.cancel, iszerofunc=lambda x_: sp.expand(sp.cancel(sp.expand(x_))) == 0)
    w1 = k0.applyfunc(sp.cancel); w2 = (k1 - w1 * sp.cancel(dot(w1, k1) / dot(w1, w1))).applyfunc(sp.cancel)
    n1, n2 = dot(w1, w1), dot(w2, w2)
    W = (w1, w2)
    dfull = [(v + u) / 2, (v - u) / 2, t]; dvt = [v / 2, v / 2, t]
    lin = [sum((dH[j] * dfull[j] for j in range(3)), sp.zeros(4, 4)) * wv for wv in W]
    lvt = [sum((dH[j] * dvt[j] for j in range(3)), sp.zeros(4, 4)) * wv for wv in W]
    quad = [sum((d2H[j][k] * dvt[j] * dvt[k] for j in range(3) for k in range(3)), sp.zeros(4, 4)) * wv / 2 for wv in W]
    first = [[dot(W[i], lvt[j]) for j in range(2)] for i in range(2)]
    ht = [[sp.cancel(sp.expand(dot(W[i], lin[j]) + dot(W[i], quad[j]) - dot(lvt[i], H0 * lvt[j]) / cc)) for j in range(2)] for i in range(2)]
    assert sp.cancel(n1 - 2) == 0 and sp.cancel(n2 - 2) == 0
    # Normalize the off-diagonal element as well as the diagonal elements.
    h11, h22, h12 = sp.cancel(ht[0][0] / n1), sp.cancel(ht[1][1] / n2), sp.cancel(ht[0][1] / 2)
    d = [sp.cancel((h12 + cjg(h12)) / 2), sp.cancel((h12 - cjg(h12)) / (2 * sp.I)), sp.cancel((h11 - h22) / 2)]
    nvec = sp.Matrix([sp.cancel(sp.diff(x, u)) for x in d])
    qv = sp.Matrix([sp.expand(x.subs(u, 0)) for x in d])
    nn = (nvec / sp.pi).applyfunc(sp.cancel)
    e1 = sp.Matrix([nn[1], -nn[0], 0]); e2 = nn.cross(e1)
    Af = sp.Poly(sp.cancel(qv.dot(e1) / sp.pi ** 2), v, t); Bf = sp.Poly(sp.cancel(qv.dot(e2) / sp.pi ** 2), v, t)
    a0, a1, a2 = (Af.coeff_monomial(m) for m in (v ** 2, v * t, t ** 2)); b0, b1, b2 = (Bf.coeff_monomial(m) for m in (v ** 2, v * t, t ** 2))
    res = sp.factor(sp.cancel((a0 * b2 - a2 * b0) ** 2 - (a0 * b1 - a1 * b0) * (a1 * b2 - a2 * b1)))
    ident = sp.cancel(ser[4] / SCALE - cc * (d[2] ** 2 + (d[0] ** 2 + d[1] ** 2)))
    RES[name] = dict(S000=Sm[(0, 0, 0)], grad=[Sm[(1, 0, 0)], Sm[(0, 1, 0)], Sm[(0, 0, 1)]], hess_off=(Hq - Hq[0, 0] * ell * ell.T).applyfunc(sp.expand),
                     hess=sp.factor(-Hq[0, 0] / SCALE), low=ser[:4], cp=[co[0] - 1, co[1], co[3], co[4]], c=sp.factor(cc),
                     first=first, idpart=sp.cancel((h11 + h22) / 2), d=d, n=nvec, deg2=all(sp.Poly(x, u, v, t).total_degree() <= 2 for x in d),
                     A=sp.factor(Af.as_expr()), B=sp.factor(Bf.as_expr()), res=res, ident=ident)

ok2 = all(R_["S000"] == 0 and all(g == 0 for g in R_["grad"]) and R_["hess_off"] == sp.zeros(3, 3) and sign_for_positive_q(R_["hess"]) == 1
          and all(x == 0 for x in R_["low"]) for R_ in RES.values())
check("for every q > 0: D = det H and its gradient vanish at f+-, the Hessian of D is 4 pi^2 h(q) (1, -1, 0)(1, -1, 0)^T with h(q) > 0, and D "
      "vanishes to weighted order three", ok2, f"h(q) = {RES['f+']['hess']} at f+ and {RES['f-']['hess']} at f-")
ok3 = all(all(x == 0 for x in R_["cp"]) and sign_for_positive_q(R_["c"]) == 1 for R_ in RES.values()) and RES["f+"]["c"] == RES["f-"]["c"]
check("for every q > 0: det(H - lambda) = lambda^2 (lambda^2 - c) at f+- with c > 0 (J = 1: c = 48)", ok3,
      f"c = {RES['f+']['c']}; at q = 1/2: {RES['f+']['c'].subs(q, sp.Rational(1, 2))}")
ok4 = all(all(x == 0 for row in R_["first"] for x in row) and R_["idpart"] == 0 and R_["deg2"] and R_["n"][0] != 0 for R_ in RES.values())
check("effective two-level Hamiltonian to weighted order two (kernel projector, H^-1 = H/c on the complement): no first-order (v, t) part, "
      "no identity part, Pauli vector n u + quadratic(v, t) with n != 0", ok4,
      f"n at f+ = {[sp.factor(x) for x in RES['f+']['n']]}, at f- = {[sp.factor(x) for x in RES['f-']['n']]}")
ok5 = all(R_["ident"] == 0 for R_ in RES.values())
check("D's weighted-degree-4 part equals c |d|^2 exactly (two independent computations agree), so it is positive definite wherever d has "
      "an isolated zero", ok5)
ok6 = all(sign_for_positive_q(R_["res"]) == -1 for R_ in RES.values())
check("for every q > 0 the homogeneous resultant of the two quadratic forms transverse to n is negative: their zero lines in the (v, t) "
      "plane are real and interlace, so d has an isolated zero and d/|d| has local degree of magnitude two at f+ and f- (charge two)", ok6,
      f"f+: A = {RES['f+']['A']}, B = {RES['f+']['B']}, resultant {RES['f+']['res']}; f-: resultant {RES['f-']['res']}")

# ------------------------------------------------------------------------------------------------ floating-point consistency
fl = {}
for qq in (sp.Rational(1, 4), sp.Integer(1)):
    J = float(JQ.subs(q, qq)); B = Bloch((1.0, 1.0, J), float(qq))
    x = float(sp.atan2(4 * qq, 4 * qq ** 2 - 1) / (2 * sp.pi)) % 1.0
    fl[str(sp.nsimplify(J))] = [[round(float(sphere_chern(B, np.array(f), r, m=64)[0]), 3) for r in (0.004, 0.008)]
                                for f in ((x, 1 - x, 0.5), (1 - x, x, 0.5))]
check("consistency (floating point): discrete sphere fluxes of the lowest two bands on spheres of radius 0.004 and 0.008 around f+ and "
      "f- at J = 2/5 and J = 8/5 are -2 and +2", all(v_ == [[-2.0, -2.0], [2.0, 2.0]] for v_ in fl.values()), f"{fl}; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
