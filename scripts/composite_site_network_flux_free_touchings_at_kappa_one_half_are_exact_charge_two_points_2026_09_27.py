#!/usr/bin/env python3
"""Composite-site network, flux-free comparator at the handover (J = 1, kappa = 1/2): the merged touchings are exact charge-two points.

Supplied u = +1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J = 1, four-site
Bloch matrix H(f) = i M(f). At kappa = 1/2 the landed rational-point polynomial vanishes at f+ = (1/4, 3/4, 1/2) and f- = (3/4, 1/4, 1/2).
Exact rational algebra (sympy; the phases there are powers of i): (1) det(H - lambda) = lambda^2 (lambda^2 - 48) at f+-, D = det H and
its gradient vanish and its Hessian has rank one; (2) with u = d1 - d2 (weight two) and v = d1 + d2, t = d3 (weight one) the lowest
weighted part of D is positive definite; (3) the effective two-level Hamiltonian to weighted order two, from the kernel projector
P = I - H^2/48, has Pauli vector d = 2 pi u (1, 1, 0) + (2 pi^2/3)(v^2 - tv - t^2, -v^2 + 3tv - t^2, t^2 - tv - v^2) at f+ (and the
corresponding vector at f-); (4) transverse to (1, 1, 0) the quadratic part has no common zero and its zero directions alternate, so
d/|d| has local degree of magnitude two: the touchings are charge-two points, linear along (1, -1, 0) and quadratic across it.
(5) Consistency (floating point): discrete sphere fluxes of the lowest two bands on spheres of radius 0.004 and 0.008 are -2 at f+ and
+2 at f-. Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import time

import numpy as np
import sympy as sp

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
    return np.angle(_link(V[:-1, :-1], V[1:, :-1]) * _link(V[1:, :-1], V[1:, 1:]) * _link(V[1:, 1:], V[:-1, 1:]) * _link(V[:-1, 1:], V[:-1, :-1]))


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


# ------------------------------------------------------------------------------------------------ exact expansions at f+-
KAP = sp.Rational(1, 2)
TERMS = terms((1.0, 1.0, 1.0), 0.3)
u, v, t = sp.symbols("u v t", real=True)


def expansion(f):
    """Exact H, dH/df_j and d2H/df_j df_k at f, where every phase is a power of i."""
    base = [sp.I ** int(round(4 * x)) for x in f]            # e^{2 pi i f_j} for f_j in quarters
    H0 = sp.zeros(4, 4); dH = [sp.zeros(4, 4) for _ in range(3)]; d2H = [[sp.zeros(4, 4) for _ in range(3)] for _ in range(3)]
    for (a, b, n, tt) in TERMS:
        amp = sp.Integer(2) if abs(tt - 2.0) < 1e-12 else 2 * KAP
        n = [int(x) for x in n]
        ph = sp.Integer(1)
        for j in range(3):
            ph *= base[j] ** n[j]
        for (r, c, sgn, m, e) in ((int(a), int(b), 1, n, ph), (int(b), int(a), -1, [-x for x in n], sp.conjugate(ph))):
            H0[r, c] += sp.I * sgn * amp * e
            for j in range(3):
                dH[j][r, c] += sp.I * sgn * amp * e * 2 * sp.pi * sp.I * m[j]
                for k in range(3):
                    d2H[j][k][r, c] += sp.I * sgn * amp * e * (2 * sp.pi * sp.I) ** 2 * m[j] * m[k]
    return H0, dH, d2H


from sympy.polys.matrices import DomainMatrix
z1, z2, w3 = sp.symbols("z1 z2 w3")
S = 2
Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
for (a, b, n, tt) in TERMS:
    amp = sp.Integer(2) if abs(tt - 2.0) < 1e-12 else 2 * KAP
    e = [int(x) for x in n]
    Ms[int(a)][int(b)] += amp * z1 ** (S + e[0]) * z2 ** (S + e[1]) * w3 ** (S + e[2])
    Ms[int(b)][int(a)] -= amp * z1 ** (S - e[0]) * z2 ** (S - e[1]) * w3 ** (S - e[2])
R = sp.QQ[z1, z2, w3]
D = sp.expand(R.to_sympy(DomainMatrix([[R.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), R).det()) / (z1 * z2 * w3) ** (4 * S))
lam = sp.symbols("lam")
out = {}
for name, f in (("f+", (sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(1, 2))), ("f-", (sp.Rational(3, 4), sp.Rational(1, 4), sp.Rational(1, 2)))):
    H0, dH, d2H = expansion(f)
    cp = sp.expand((H0 - lam * sp.eye(4)).det())
    pt = {z1: sp.I ** int(4 * f[0]), z2: sp.I ** int(4 * f[1]), w3: sp.I ** int(4 * f[2])}
    zs = (z1, z2, w3)
    grad = [sp.simplify((zz * sp.diff(D, zz)).subs(pt)) for zz in zs]                       # dD/df = 2 pi i z dD/dz
    Hq = sp.Matrix(3, 3, lambda j, k: sp.simplify(-4 * sp.pi ** 2 * (zs[j] * sp.diff(zs[k] * sp.diff(D, zs[k]), zs[j])).subs(pt)))
    out[name] = (H0, dH, d2H, cp, grad, Hq, sp.simplify(D.subs(pt)))
ok1 = all(sp.expand(out[n][3] - lam ** 2 * (lam ** 2 - 48)) == 0 and out[n][6] == 0 and all(g == 0 for g in out[n][4]) and out[n][5].rank() == 1
          for n in out)
check("at kappa = 1/2 the characteristic polynomial at f+ and f- is lambda^2 (lambda^2 - 48), D = det H and its gradient vanish, and "
      "the Hessian of D has rank one", ok1, f"Hessian at f+ = 4 pi^2 x {sp.simplify(out['f+'][5] / (4 * sp.pi ** 2)).tolist()}; at f- "
      f"{sp.simplify(out['f-'][5] / (4 * sp.pi ** 2)).tolist()}")

# weighted expansion of D at f+: d1 = (eps v + eps^2 u)/2, d2 = (eps v - eps^2 u)/2, d3 = eps t
eps = sp.symbols("eps")
E = lambda base, dd: base * sp.exp(2 * sp.pi * sp.I * dd)
Dser = sp.series(sp.expand(D.subs({z1: E(sp.I, (eps * v + eps ** 2 * u) / 2), z2: E(-sp.I, (eps * v - eps ** 2 * u) / 2), w3: E(-1, eps * t)})),
                 eps, 0, 5).removeO()
low = [sp.simplify(Dser.coeff(eps, k)) for k in range(4)]
q4 = sp.expand(sp.simplify(Dser.coeff(eps, 4)))
s = sp.symbols("s", real=True)
a2 = sp.Poly(q4, u).coeff_monomial(u ** 2); a1 = sp.Poly(q4, u).coeff_monomial(u); a0 = sp.Poly(q4, u).coeff_monomial(1)
resid = sp.expand(sp.simplify((a0 - a1 ** 2 / (4 * a2)).subs(v, s * t) / t ** 4))
rq = sp.Poly(sp.nsimplify(sp.expand(resid / sp.pi ** 4 * 3)), s)
roots = sp.real_roots(rq)
ok2 = all(x == 0 for x in low) and (a2 / sp.pi ** 2).is_positive and not roots and rq.LC() > 0
check("with u = d1 - d2 (weight two), v = d1 + d2, t = d3 (weight one), D vanishes to weighted order three at f+ and its weighted-"
      "degree-4 part is positive definite (after completing the square in u the quartic in s = v/t has no real root)", ok2,
      f"weighted-4 part {sp.factor(q4)}; residual quartic x 3/pi^4: {rq.as_expr()}; real roots {roots}")

# effective two-level Hamiltonian to weighted order two, Pauli vector and its degree
sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
dres = {}
for name in ("f+", "f-"):
    H0, dH, d2H = out[name][0], out[name][1], out[name][2]
    P = sp.eye(4) - H0 ** 2 / 48; Q = sp.eye(4) - P
    dfull = [(v + u) / 2, (v - u) / 2, t]; dvt = [v / 2, v / 2, t]
    lin = sum((dH[j] * dfull[j] for j in range(3)), sp.zeros(4, 4)); lvt = sum((dH[j] * dvt[j] for j in range(3)), sp.zeros(4, 4))
    quad = sum((d2H[j][k] * dvt[j] * dvt[k] for j in range(3) for k in range(3)), sp.zeros(4, 4)) / 2
    first_vt_zero = sp.simplify(P * lvt * P) == sp.zeros(4, 4)
    Heff = sp.expand(P * lin * P + P * quad * P - P * lvt * Q * (H0 / 48) * Q * lvt * P)
    ker = H0.nullspace()
    U = sp.Matrix.hstack(*sp.GramSchmidt([ker[0], ker[1]], True))
    h = sp.simplify(U.H * Heff * U)
    d = [sp.expand(sp.simplify((h * sg).trace() / 2)) for sg in (sx, sy, sz)]
    dres[name] = (first_vt_zero, sp.simplify(h.trace() / 2), d)
lin_dir = {n: sp.Matrix([sp.diff(c, u) for c in dres[n][2]]) for n in dres}
check("effective two-level Hamiltonian to weighted order two (kernel projector P = I - H^2/48): the first-order projection in v and t "
      "vanishes, the identity part vanishes, and the Pauli vector is linear in u plus quadratic in (v, t)",
      all(dres[n][0] and dres[n][1] == 0 and all(sp.Poly(c, u, v, t).total_degree() <= 2 for c in dres[n][2]) for n in dres),
      f"f+: d = {[sp.factor(c) for c in dres['f+'][2]]}; f-: d = {[sp.factor(c) for c in dres['f-'][2]]}")


def degree_two(d):
    """|local degree| = 2: the u-linear direction n is nonzero and, transverse to n, the quadratic part in (v, t) has no common real zero
    and zero directions that alternate around the circle."""
    n = sp.Matrix([sp.diff(c, u) for c in d]).subs({u: 0, v: 0, t: 0})
    qv = sp.Matrix([c.subs(u, 0) for c in d])
    basis = [x for x in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1]))]
    e1 = (basis[0] - n * (n.dot(basis[0]) / n.dot(n))); e1 = e1 if e1.norm() != 0 else basis[1] - n * (n.dot(basis[1]) / n.dot(n))
    e2 = n.cross(e1)
    A_, B_ = sp.expand(qv.dot(e1)), sp.expand(qv.dot(e2))
    ra = sp.Poly(sp.expand(A_.subs({v: s, t: 1}) / sp.pi ** 2), s).real_roots(); rb = sp.Poly(sp.expand(B_.subs({v: s, t: 1}) / sp.pi ** 2), s).real_roots()
    Adeg, Bdeg = sp.Poly(A_, v, t), sp.Poly(B_, v, t)
    # directions: roots in s = v/t, plus t = 0 (s = infinity) when the v^2 coefficient vanishes
    dirs = [(float(sp.atan2(1, r)), "a") for r in ra] + [(float(sp.atan2(1, r)), "b") for r in rb]
    if Adeg.coeff_monomial(v ** 2) == 0:
        dirs.append((0.0, "a"))
    if Bdeg.coeff_monomial(v ** 2) == 0:
        dirs.append((0.0, "b"))
    dirs.sort()
    common = any(abs(x[0] - y[0]) < 1e-12 for x in dirs for y in dirs if x[1] != y[1])
    alternate = len(dirs) == 4 and all(dirs[i][1] != dirs[i + 1][1] for i in range(3))
    return n.norm() != 0 and not common and alternate, n.T, dirs


deg = {n: degree_two(dres[n][2]) for n in dres}
check("transverse to the u direction the quadratic part of d has no common zero and its zero directions alternate, so d/|d| has local "
      "degree of magnitude two at f+ and f- (charge-two touchings: linear along (1, -1, 0), quadratic across it)", all(deg[n][0] for n in deg),
      "; ".join(f"{n}: u direction {list(deg[n][1])}, zero directions {[(round(x, 4), c) for x, c in deg[n][2]]}" for n in deg))

# ------------------------------------------------------------------------------------------------ floating-point consistency
B = Bloch((1.0, 1.0, 1.0), 0.5)
fl = {n: [round(float(sphere_chern(B, np.array([float(x) for x in f]), r, m=64)[0]), 3) for r in (0.004, 0.008)]
      for n, f in (("f+", (0.25, 0.75, 0.5)), ("f-", (0.75, 0.25, 0.5)))}
check("consistency (floating point): discrete sphere fluxes of the lowest two bands on spheres of radius 0.004 and 0.008 are -2 at f+ "
      "and +2 at f-", fl["f+"] == [-2.0, -2.0] and fl["f-"] == [2.0, 2.0], f"{fl}; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
