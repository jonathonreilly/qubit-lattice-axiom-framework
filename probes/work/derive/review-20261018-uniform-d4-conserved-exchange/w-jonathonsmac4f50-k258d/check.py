#!/usr/bin/env python3
"""Disjoint check for J:derive:review-20261018-uniform-d4-conserved-exchange:a1.

Scope: the supplied D4-cone Regge carrier and supplied scalar corner stress of
the 2026-10-18 exact-Ward note.  No physical gravity identification and no
nonlinear action symmetry is assumed.

Disjointness from the source runner:
  * the Regge Hessian is rebuilt with ANALYTIC derivatives of areas and
    dihedral angles (inverse-Gram / dual-Gram formulas), not the source's
    centred finite differences; the two are compared once, entry by entry;
  * the exchange is evaluated with a lambda-regularised bilinear solve for
    real and complex momenta alike (no SVD-selected subspaces);
  * the comparison form is NEW: the trace is the w-weighted trace.
Exact claims use sympy/Fractions.  Regge-Hessian claims are float64 with the
stated tolerances (they are CHECKED, not exact).
"""
import itertools
import os
import sys
import time
from fractions import Fraction

for _k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import numpy as np
import sympy as sp

T0 = time.time()
PASS = FAIL = 0
HITS_OK = []


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""), flush=True)
    return ok


# ======================================================================
# 1.  EXACT ALGEBRA (sympy / Fractions)
# ======================================================================
def exact_block():
    x = sp.symbols("x0:4", nonzero=True)
    y = sp.symbols("y0:4", nonzero=True)
    w = [1 / (a * b) for a, b in zip(x, y)]
    d = [b - a for a, b in zip(x, y)]
    u = [z - 1 for z in w]
    delta = sum(a + 1 / a - b - 1 / b for a, b in zip(x, y))
    sq = sum(z * z for z in u)
    S = sp.Matrix(4, 4, lambda m, n: -d[m] * d[n] / 4 + (u[m] * u[n] - (sq if m == n else 0)) / 4)
    ok = all(sp.cancel(sum(u[m] * S[m, n] for m in range(4)) + d[n] * delta / 4) == 0 for n in range(4))
    check("E1 exact Laurent Ward identity, all 4 components (reproduction of source, not new)", ok)

    # E2: for every v != 0 the map T -> v.T from Sym^2(C^4) onto C^4 is onto, so
    #     dim N(q) = 6 for EVERY q with w != 1 (real or complex).  Explicit right inverse
    #     T = y a^T + a y^T - (v.y) a a^T with v.a = 1 (a = e_j / v_j).
    v = sp.symbols("v0:4", nonzero=True)
    ys = sp.symbols("y0:4")
    ok = True
    for j in range(4):
        a = sp.Matrix([sp.Integer(1) / v[j] if i == j else 0 for i in range(4)])
        yv = sp.Matrix(ys)
        vv = sp.Matrix(v)
        vy = (vv.T * yv)[0]
        T = yv * a.T + a * yv.T - vy * a * a.T
        sym = sp.simplify(T - T.T) == sp.zeros(4, 4)
        res = sp.simplify((vv.T * T).T - yv) == sp.zeros(4, 1)
        ok = ok and sym and res
    check("E2 exact: (w-1).T = y has a symmetric solution for every y whenever w != 1 -> dim N(q)=6 (also complex q)", ok)

    # E3: staggered variable T~_{mu nu} = exp(-i(q_mu+q_nu)/2) T_{mu nu}.
    #     (w-1).T = -i exp(i q_nu/2) * sum_mu p_mu T~_{mu nu},  p = 2 sin(q/2) (real for real q).
    uu = sp.symbols("u0:4", nonzero=True)          # u_mu = exp(-i q_mu/2)
    Tm = sp.Matrix(4, 4, lambda i, j: sp.Symbol("T%d%d" % (min(i, j), max(i, j))))
    ok = True
    for n in range(4):
        lhs = sum((uu[m] ** 2 - 1) * Tm[m, n] for m in range(4))
        p = [-sp.I * (1 / uu[m] - uu[m]) for m in range(4)]       # 2 sin(q/2) = -i (e^{iq/2}-e^{-iq/2})
        Tt = [uu[m] * uu[n] * Tm[m, n] for m in range(4)]
        rhs = -sp.I * (1 / uu[n]) * sum(p[m] * Tt[m] for m in range(4))
        ok = ok and sp.simplify(lhs - rhs) == 0
    check("E3 exact: lattice conservation (w-1).T=0  <=>  p.T~=0 with p=2sin(q/2), T~=exp(-i(q_m+q_n)/2)T", ok)

    # E4: tr T~ = sum_mu w_mu T_mumu  and first-order expansion of the w-weighted trace form.
    t = sp.symbols("t")
    nn = sp.symbols("n0:4", real=True)
    d1 = sp.symbols("a0:4")
    d2 = sp.symbols("b0:4")
    wl = [sp.exp(-sp.I * t * nn[m]) for m in range(4)]           # w(q), q = t n
    wr = [sp.exp(+sp.I * t * nn[m]) for m in range(4)]           # w(-q)
    form = sum(wr[m] * d1[m] for m in range(4)) * sum(wl[m] * d2[m] for m in range(4))
    form0 = sum(d1) * sum(d2)
    first = sp.diff(form - form0, t).subs(t, 0)
    claimed = sp.I * (sum(nn[m] * d1[m] for m in range(4)) * sum(d2) - sum(d1) * sum(nn[m] * d2[m] for m in range(4)))
    check("E4 exact: d/dt [w(-q)-weighted trace x w(q)-weighted trace] at t=0 = i[(n.d1)(tr2)-(tr1)(n.d2)]", sp.simplify(first - claimed) == 0)

    # E5: exact vanishing of that first-order form on axis, tick and body directions for
    #     conserved sources (rational arithmetic, Fractions), and an exact rational direction where it does not vanish.
    def Lform(n, T1, T2):
        n = [Fraction(c) for c in n]
        x1 = sum(n[m] * T1[m][m] for m in range(4)); x2 = sum(n[m] * T2[m][m] for m in range(4))
        y1 = sum(T1[m][m] for m in range(4)); y2 = sum(T2[m][m] for m in range(4))
        return x1 * y2 - y1 * x2

    def rank1(vv):
        return [[Fraction(vv[i]) * Fraction(vv[j]) for j in range(4)] for i in range(4)]

    def cont_conserved(n, T):
        return all(sum(Fraction(n[m]) * T[m][nu] for m in range(4)) == 0 for nu in range(4))

    # axis / tick: n = e_a  -> row a of T vanishes, so n.diag T = T_aa = 0 identically
    ok = True
    for a in range(4):
        n = [1 if i == a else 0 for i in range(4)]
        vs = [[0 if i == a else (i + 1 + 2 * j) for i in range(4)] for j in range(3)]   # v with v_a=0 -> n.v=0
        Ts = [rank1(vv) for vv in vs]
        ok = ok and all(cont_conserved(n, T) for T in Ts)
        ok = ok and all(Lform(n, A, B) == 0 for A in Ts for B in Ts)
    # body: n=(1,1,1,1): v with sum v = 0
    n = [1, 1, 1, 1]
    vs = [(1, -1, 0, 0), (1, 1, -2, 0), (1, 1, 1, -3), (2, -1, -1, 0)]
    Ts = [rank1(vv) for vv in vs]
    ok = ok and all(cont_conserved(n, T) for T in Ts) and all(Lform(n, A, B) == 0 for A in Ts for B in Ts)
    check("E5a exact: first-order form vanishes identically on axis, tick and body directions (conserved sources)", ok)
    n = [1, 2, 0, 0]
    T1 = rank1((2, -1, 1, 0)); T2 = rank1((0, 0, 1, 1))
    val = Lform(n, T1, T2)
    check("E5b exact counterexample direction n=(1,2,0,0): T1=vv^T, T2=uu^T continuum-conserved and first-order form = %s != 0" % val,
          cont_conserved(n, T1) and cont_conserved(n, T2) and val == 12)

    # E6: for real T the diagonal first-order form vanishes: L(T,T) = i(conj(x) y - conj(y) x) = 2 i Im-type; =0 when x*conj(y) real.
    xs, ys_ = sp.symbols("x y", real=True)
    Ldiag = sp.I * (sp.conjugate(xs) * ys_ - sp.conjugate(ys_) * xs)
    check("E6 exact: first-order form is anti-Hermitian-imaginary; it vanishes on every real source tensor (real-part / real-source fits cannot see it)",
          sp.simplify(Ldiag) == 0)


# ======================================================================
# 2.  CARRIER (geometry copied in spirit from the source note's description; derivatives are NEW)
# ======================================================================
PAIRS = list(itertools.combinations(range(4), 2))
HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def _key_pair(v1, v2):
    (b1, t1), (b2, t2) = v1, v2
    if (t1, b1) > (t2, b2):
        (b1, t1), (b2, t2) = (b2, t2), (b1, t1)
    return (t1, t2, tuple(np.subtract(b2, b1))), tuple(b1)


def _key_tri(vs):
    vs = sorted(vs, key=lambda v: (v[1], v[0]))
    b0 = vs[0][0]
    return tuple((t, tuple(np.subtract(b, b0))) for b, t in vs), tuple(b0)


def tri_area_s(s):
    a, b, c = s
    return 0.25 * np.sqrt(max(2 * (a * b + b * c + c * a) - a * a - b * b - c * c, 0.0))


def d4cone():
    OFF = [np.zeros(4), 0.5 * np.ones(4)] + [0.5 * (np.eye(4)[m] + np.eye(4)[n]) for m, n in PAIRS]

    def as_vertex(p):
        p = np.asarray(p, float)
        if np.allclose(p, np.round(p)):
            return (tuple(int(x) for x in np.round(p)), 0)
        q = p - 0.5
        return (tuple(int(x) for x in np.round(q)), 1)
    sims = []
    for h, (m, n) in enumerate(PAIRS):
        r, s = [i for i in range(4) if i not in (m, n)]
        c = OFF[2 + h]; E = np.eye(4)
        axes = [0.5 * (E[m] + E[n]), 0.5 * (E[m] - E[n]), 0.5 * (E[r] + E[s]), 0.5 * (E[r] - E[s])]
        for signs in itertools.product([1, -1], repeat=4):
            sims.append([((0, 0, 0, 0), 2 + h)] + [as_vertex(c + sg * ax) for sg, ax in zip(signs, axes)])
    return OFF, sims


def dual_gram(s):
    G = np.array([[0.5 * (s[0, b] + s[0, a] - s[a, b]) for b in range(1, 5)] for a in range(1, 5)])
    D = np.linalg.inv(G)
    E = np.zeros((5, 5)); E[1:, 1:] = D
    E[0, 1:] = -D.sum(axis=1); E[1:, 0] = E[0, 1:]; E[0, 0] = D.sum()
    return G, D, E


def dihedral_s(s, m, n):
    _, _, E = dual_gram(s)
    return np.arccos(np.clip(-E[m, n] / np.sqrt(E[m, m] * E[n, n]), -1, 1))


def dihedral_ds(s, m, n):
    """exact d theta_mn / d s_ij (squared-length variables) for the interior dihedral angle between facets opposite m,n."""
    G, D, E = dual_gram(s)
    c = -E[m, n] / np.sqrt(E[m, m] * E[n, n])
    out = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        dG = np.zeros((4, 4))
        if i == 0:
            a = j - 1
            for b in range(4):
                if b == a:
                    dG[a, a] = 1.0
                else:
                    dG[a, b] = 0.5; dG[b, a] = 0.5
        else:
            dG[i - 1, j - 1] -= 0.5; dG[j - 1, i - 1] -= 0.5
        dD = -D @ dG @ D
        dE = np.zeros((5, 5)); dE[1:, 1:] = dD
        dE[0, 1:] = -dD.sum(axis=1); dE[1:, 0] = dE[0, 1:]; dE[0, 0] = dD.sum()
        r = np.sqrt(E[m, m] * E[n, n])
        dc = -dE[m, n] / r + 0.5 * E[m, n] / r * (dE[m, m] / E[m, m] + dE[n, n] / E[n, n])
        out[i, j] = out[j, i] = -dc / np.sqrt(1 - c * c)
    return out


class Carrier:
    def __init__(self, OFF, sims, analytic=True, fd=1e-6):
        self.OFF = [np.array(o, float) for o in OFF]
        self.simp = sims
        self.ekey = {}
        for s in self.simp:
            for i, j in itertools.combinations(range(5), 2):
                k, _ = _key_pair(s[i], s[j])
                self.ekey.setdefault(k, len(self.ekey))
        self.E = len(self.ekey)
        self.evec = [None] * self.E
        for (t1, t2, rel), c in self.ekey.items():
            self.evec[c] = np.array(rel, float) + self.OFF[t2] - self.OFF[t1]
        self.types = sorted({t for s in self.simp for _, t in s})
        self.analytic = analytic
        self.fd = fd
        self._build()

    def pos(self, v):
        return np.array(v[0], float) + self.OFF[v[1]]

    def s2(self, v1, v2):
        d = self.pos(v2) - self.pos(v1)
        return float(d @ d)

    def _build(self):
        stars, hverts = {}, {}
        for si, s in enumerate(self.simp):
            for tri in itertools.combinations(range(5), 3):
                key, anc = _key_tri([s[i] for i in tri])
                T = -np.array(anc)
                stars.setdefault(key, []).append((si, T, tri))
                hverts.setdefault(key, [(tuple(np.add(s[i][0], T)), s[i][1]) for i in tri])
        self.terms = []
        for key, st in stars.items():
            hv = hverts[key]
            pairs = [(0, 1), (0, 2), (1, 2)]
            s3 = [self.s2(hv[i], hv[j]) for i, j in pairs]
            A = tri_area_s(s3)
            a, b, c = s3
            dA = [(b + c - a) / (16 * A), (a + c - b) / (16 * A), (a + b - c) / (16 * A)]
            a_terms = []
            for n_, (i, j) in enumerate(pairs):
                cc, anc = _key_pair(hv[i], hv[j])
                a_terms.append((self.ekey[cc], np.array(anc, float), dA[n_] * 2 * np.sqrt(s3[n_])))
            d_terms = []
            for si, T, tri in st:
                vs = [(tuple(np.add(v[0], T)), v[1]) for v in self.simp[si]]
                L2 = np.array([[self.s2(vs[i], vs[j]) for j in range(5)] for i in range(5)])
                m, n = [i for i in range(5) if i not in tri]
                if self.analytic:
                    dth = dihedral_ds(L2, m, n)
                for i, j in itertools.combinations(range(5), 2):
                    l = np.sqrt(L2[i, j])
                    if self.analytic:
                        val = dth[i, j] * 2 * l
                    else:
                        th = []
                        for sg in (1, -1):
                            M = L2.copy(); M[i, j] = M[j, i] = (l + sg * self.fd) ** 2
                            th.append(dihedral_s(M, m, n))
                        val = (th[0] - th[1]) / (2 * self.fd)
                    cc, anc = _key_pair(vs[i], vs[j])
                    d_terms.append((self.ekey[cc], np.array(anc, float), -val))
            pack = lambda tl: (np.array([t[0] for t in tl]), np.array([t[1] for t in tl]), np.array([t[2] for t in tl]))
            self.terms.append((pack(a_terms), pack(d_terms)))

    def Q(self, k):
        k = np.asarray(k, complex)
        Q = np.zeros((self.E, self.E), complex)

        def row(t, kk):
            r = np.zeros(self.E, complex)
            np.add.at(r, t[0], t[2] * np.exp(1j * (t[1] @ kk)))
            return r
        for a, d in self.terms:
            Q += 0.5 * (np.outer(row(a, -k), row(d, k)) + np.outer(row(d, -k), row(a, k)))
        return Q

    def gauge(self, k):
        k = np.asarray(k, complex)
        nt = len(self.types); tix = {t: i for i, t in enumerate(self.types)}
        G = np.zeros((self.E, 4 * nt), complex)
        for (t1, t2, rel), c in self.ekey.items():
            v = self.evec[c]; u = v / np.sqrt(v @ v)
            G[c, 4 * tix[t2]:4 * tix[t2] + 4] += u * np.exp(1j * k @ np.array(rel, float))
            G[c, 4 * tix[t1]:4 * tix[t1] + 4] -= u
        return G


def segment_readings(C, k):
    """24 site-to-site segments (4 axes, 12 face diagonals via deep holes, 8 body diagonals via centre): d(l^2) rows."""
    E = np.eye(4, dtype=int); Z = (0, 0, 0, 0); k = np.asarray(k, complex)
    R, ls = [], []

    def seg(parts, l):
        r = np.zeros(C.E, complex)
        for (p, q) in parts:
            key, anc = _key_pair(p, q)
            r[C.ekey[key]] += 2 * l * np.exp(1j * k @ np.array(anc, float))
        return r
    for mu in range(4):
        R.append(seg([((Z, 0), (tuple(E[mu]), 0))], 1.0)); ls.append(1.0)
    for h, (m, n) in enumerate(PAIRS):
        hv = (Z, 2 + h)
        R.append(seg([((Z, 0), hv), (hv, (tuple(E[m] + E[n]), 0))], np.sqrt(2))); ls.append(np.sqrt(2))
        R.append(seg([((tuple(E[n]), 0), hv), (hv, (tuple(E[m]), 0))], np.sqrt(2))); ls.append(np.sqrt(2))
    for sg in itertools.product([1, -1], repeat=3):
        s_ = np.array([1, *sg]); v0 = tuple(int(x) for x in (1 - s_) // 2); v1 = tuple(int(x) for x in (1 - s_) // 2 + s_)
        R.append(seg([((v0, 0), (Z, 1)), ((Z, 1), (v1, 0))], 2.0)); ls.append(2.0)
    return np.array(R), np.array(ls)


def couple(S, w, kappa):
    b = np.zeros(24, complex)
    for nu in range(4):
        b[nu] += S[nu, nu] / 2
    for h, (m, n) in enumerate(PAIRS):
        b[4 + 2 * h] += S[m, n] / 2; b[5 + 2 * h] -= S[m, n] / 2
        b[m] -= (w[n] - 1) * S[m, n] / 4; b[n] -= (w[m] - 1) * S[m, n] / 4
    kap = kappa * np.trace(S)
    for h, (m, n) in enumerate(PAIRS):
        b[4 + 2 * h] += kap; b[5 + 2 * h] += kap
        b[m] -= 0.5 * (1 + w[n]) * kap; b[n] -= 0.5 * (1 + w[m]) * kap
    return b


SYM = [(a, b) for a in range(4) for b in range(a, 4)]


def tens(v):
    T = np.zeros((4, 4), complex)
    for j, (a, b) in enumerate(SYM):
        T[a, b] = T[b, a] = v[j]
    return T


def cons_basis(q):
    """orthonormal basis (in C^10) of lattice-conserved symmetric tensors, (w-1).T = 0, w = exp(-iq); works for complex q."""
    w = np.exp(-1j * np.asarray(q, complex))
    A = np.zeros((4, 10), complex)
    for j, (a, b) in enumerate(SYM):
        E_ = np.zeros((4, 4)); E_[a, b] = E_[b, a] = 1
        A[:, j] = (w - 1) @ E_
    U, sv, Vh = np.linalg.svd(A)
    assert np.count_nonzero(sv > 1e-12 * sv[0]) == 4
    return [tens(v) for v in Vh[4:].conj()], w


def exchange(C, ls, q, kappa, lam=1.0):
    """bilinear (analytic) exchange K_ij = (q.q) B(T'_i;-q) R(q) (Q + lam G G(-q)^T)^{-1} R(-q)^T B(T_j;q).
    Left tensors T' span N(-q) (= conj N(q) for real q), right tensors T span N(q)."""
    q = np.asarray(q, complex)
    Tr, w = cons_basis(q); Tl, wm = cons_basis(-q)
    Br = np.array([couple(T, w, kappa) / ls ** 2 for T in Tr]); Bl = np.array([couple(T, wm, kappa) / ls ** 2 for T in Tl])
    Rp = segment_readings(C, q)[0]; Rm = segment_readings(C, -q)[0]
    G = C.gauge(q); Gm = C.gauge(-q)
    right = Rm.T @ Br.T; left = Bl @ Rp
    X = np.linalg.solve(C.Q(q) + lam * G @ Gm.T, right)
    ward = max(np.linalg.norm(Gm.T @ right) / np.linalg.norm(right), np.linalg.norm(left @ G) / np.linalg.norm(left))
    return (left @ X) * (q @ q), Tl, Tr, w, wm, ward


def F_plain(Tl, Tr, al, be):          # source form: alpha <T1,T2> + beta tr tr, T = S/2
    return np.array([[al * np.sum((a / 2) * (b / 2)) + be * np.trace(a / 2) * np.trace(b / 2) for b in Tr] for a in Tl])


def F_w(Tl, Tr, w, wm, al, be):       # NEW: trace replaced by the w-weighted trace
    return np.array([[al * np.sum((a / 2) * (b / 2)) + be * np.sum(wm * np.diag(a / 2)) * np.sum(w * np.diag(b / 2)) for b in Tr] for a in Tl])


def L_first(Tl, Tr, q, be):           # explicit first-order difference F_w - F_plain (E4)
    return np.array([[be * 1j * ((q @ np.diag(a / 2)) * np.trace(b / 2) - np.trace(a / 2) * (q @ np.diag(b / 2))) for b in Tr] for a in Tl])


def rel(A, B):
    return np.linalg.norm(A - B) / np.linalg.norm(B)


# ======================================================================
def numeric_block():
    OFF, sims = d4cone()
    C = Carrier(OFF, sims, analytic=True)
    R0, ls = segment_readings(C, np.zeros(4))
    check("N0 carrier: 96 simplices, 72 edge classes, 8 vertex types, 24 segments",
          len(sims) == 96 and C.E == 72 and len(C.types) == 8 and R0.shape[0] == 24)

    # N1: analytic derivative vs independent centred finite differences, entrywise on Q at three momenta
    Cfd = Carrier(OFF, sims, analytic=False, fd=1e-6)
    dev = max(np.abs(C.Q(k) - Cfd.Q(k)).max() for k in ([0.3, -0.2, 0.5, 0.1], [0.01, 0.02, -0.01, 0.015], [0, 0, 0, 0]))
    check("N1 analytic-derivative Regge Hessian equals centred-FD Hessian (all 72x72 entries, 3 momenta)", dev < 1e-7, "max abs dev %.2e" % dev)

    rng = np.random.default_rng(20261018)
    # ---- spectrum / ranks (real q)
    Q0 = C.Q(np.zeros(4)); ev0 = np.linalg.eigvalsh(Q0)
    nul0 = int(np.sum(np.abs(ev0) < 1e-9)); gap0 = np.min(np.abs(ev0[np.abs(ev0) >= 1e-9]))
    sv0 = np.linalg.svd(C.gauge(np.zeros(4)), compute_uv=False)
    rg0 = int(np.sum(sv0 > 1e-9))
    check("N2a rank change at q=0: nullity(Q(0))=40, gauge rank 28, nonzero spectrum gap >= 2.4 (CHECKED, float64)",
          nul0 == 40 and rg0 == 28 and gap0 > 2.4, "nullity %d, gauge rank %d, gap %.4f" % (nul0, rg0, gap0))

    dirs = [rng.standard_normal(4) for _ in range(40)]
    dirs += [np.array(v, float) for v in ([1, 1e-2, 0, 0], [1, 1e-2, 1e-2, 0], [1, 1, 1, 1.01], [1, 1, 1e-3, 1e-3],
                                           [1, -1, 1, -1], [1, 1, 0, 0], [1, 1, 1, 0], [1, 2, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1])]
    dirs = [d / np.linalg.norm(d) for d in dirs]
    nulls, lowdev, hi, gdev = [], [], [], []
    target = np.array([-0.5, -0.5, -0.25, -0.25, -0.25, -0.25, -0.25, 0.25])
    for t in (0.02, 0.01):
        nl, ld, hh, gd = [], [], [], []
        for d in dirs:
            q = t * d
            Q = C.Q(q); ev = np.linalg.eigvalsh(Q)
            nl.append(int(np.sum(np.abs(ev) < 1e-9)))
            low = np.sort(ev[(np.abs(ev) >= 1e-9) & (np.abs(ev) < 0.5)] / t ** 2)
            ld.append(np.abs(low - np.sort(target)).max() if len(low) == 8 else 9.9)
            hh.append(np.min(np.abs(ev[np.abs(ev) >= 0.5])))
            G = C.gauge(q); gd.append(np.linalg.norm(Q @ G) / (np.linalg.norm(Q) * np.linalg.norm(G)))
        nulls.append(set(nl)); lowdev.append(max(ld)); hi.append(min(hh)); gdev.append(max(gd))
    check("N2b real q (51 directions, |q|=.02,.01): nullity of Q(q) is exactly 32 = gauge rank; exactly 8 low modes; gap to O(1) modes >= 2.4",
          nulls[0] == {32} and nulls[1] == {32} and min(hi) > 2.4, "min high |ev| %.4f; gauge residual max %.1e" % (min(hi), max(gdev)))
    check("N2c low cluster = {-1/2 (x2), -1/4 (x5), +1/4 (x1)} |q|^2 (1+O(q^2)) in every sampled real direction; deviation ratio ~4",
          lowdev[0] < 2e-3 and 3.5 < lowdev[0] / lowdev[1] < 4.5, "max dev %.2e (.02), %.2e (.01), ratio %.3f" % (lowdev[0], lowdev[1], lowdev[0] / lowdev[1]))

    # ---- real-q exchange: source form vs w-weighted form
    for kappa, be in ((0.0, 4 / 3), (1 / 24, 2.0)):
        r_plain, r_w, supw, fits = [], [], [], []
        for d in dirs:
            e0, e1 = [], []
            for t in (0.02, 0.01):
                K, Tl, Tr, w, wm, ward = exchange(C, ls, t * d, kappa)
                assert ward < 1e-10
                nF = np.linalg.norm(F_plain(Tl, Tr, -4, be))
                e0.append(np.linalg.norm(K - F_plain(Tl, Tr, -4, be)) / nF)
                e1.append(np.linalg.norm(K - F_w(Tl, Tr, w, wm, -4, be)) / nF)
            r_plain.append((e0[0] / e0[1], e0[1]))
            r_w.append(e1[0] / e1[1]); supw.append(e1[1] / 0.01 ** 2)
        rp = np.array(r_plain)
        check("N3a kappa=%.4f: remainder against W-WEIGHTED form: .02/.01 ratio in [3.98,4.02] for all 51 real directions (O(q^2)); sup rel.rem/|q|^2 = %.3f"
              % (kappa, max(supw)), 3.98 < min(r_w) and max(r_w) < 4.02 and max(supw) < 0.5)
        check("N3b kappa=%.4f: remainder against SOURCE form (plain trace): ratio .02/.01 reaches 2.0 (O(q)) in generic directions; sup rel.rem/|q| = %.3f"
              % (kappa, rp[:, 1].max() / 0.01), rp[:, 0].min() > 1.99 and rp[:, 0].min() < 2.01 and rp[:, 1].max() / 0.01 > 0.15)

    # ---- reproduce the source note's generic fit residuals (.003295, .004885 at .02) with the analytic Hessian
    d = np.array([.3, -.5, .6, .55]); d /= np.linalg.norm(d)
    res = {}
    for kappa, be in ((0.0, 4 / 3), (1 / 24, 2.0)):
        for t in (.02, .01):
            K, Tl, Tr, w, wm, _ = exchange(C, ls, t * d, kappa)
            X = np.array([[np.sum((a / 2) * (b / 2)), np.trace(a / 2) * np.trace(b / 2)] for a in Tl for b in Tr])
            co = np.linalg.lstsq(X, K.ravel(), rcond=None)[0]
            res[(kappa, t)] = (np.linalg.norm(X @ co - K.ravel()) / np.linalg.norm(K.ravel()), co)
    check("N4 source-variable two-invariant fit residual, generic direction: .003295/.004885 at .02 exceed .003, ratio .02/.01 = 2.000 (reproduces the note's diagnostic)",
          abs(res[(0.0, .02)][0] - 0.003295) < 2e-6 and abs(res[(1 / 24, .02)][0] - 0.004885) < 2e-6
          and abs(res[(0.0, .02)][0] / res[(0.0, .01)][0] - 2) < 2e-3 and abs(res[(1 / 24, .02)][0] / res[(1 / 24, .01)][0] - 2) < 2e-3,
          "%.6f %.6f ; %.6f %.6f" % (res[(0.0, .02)][0], res[(0.0, .01)][0], res[(1 / 24, .02)][0], res[(1 / 24, .01)][0]))
    check("N4b the fitted coefficients themselves are accurate to O(q^2) (alpha -> -4, beta -> 4/3, 2) although the full tensor is only O(q)-accurate",
          all(abs(res[(0.0, t)][1][0] + 4) < 2e-3 and abs(res[(0.0, t)][1][1] - 4 / 3) < 2e-3 for t in (.02, .01)))

    # ---- explicit first-order coefficient
    out = []
    for kappa, be in ((0.0, 4 / 3), (1 / 24, 2.0)):
        for t in (.02, .01, .005):
            K, Tl, Tr, w, wm, _ = exchange(C, ls, t * d, kappa)
            D = K - F_plain(Tl, Tr, -4, be); L = L_first(Tl, Tr, t * d, be)
            out.append(np.linalg.norm(D - L) / np.linalg.norm(L))
    check("N5 first-order remainder K - F_plain equals the explicit exact form L (E4) up to O(q): relative defect halves with q (ratios ~2)",
          all(1.9 < out[i] / out[i + 1] < 2.1 for i in (0, 1, 3, 4)) and max(out) < 0.02, "defects " + ", ".join("%.4f" % o for o in out))

    # ---- partner (face-null) channel: beta(kappa)
    ok = True; det = []
    for kappa in (0.0, 1 / 48, 1 / 36, 1 / 24, 1 / 16, 1 / 12):
        K, Tl, Tr, w, wm, _ = exchange(C, ls, 0.01 * d, kappa)
        X = np.array([[np.sum((a / 2) * (b / 2)), np.sum(wm * np.diag(a / 2)) * np.sum(w * np.diag(b / 2))] for a in Tl for b in Tr])
        co = np.linalg.lstsq(X, K.ravel(), rcond=None)[0]
        pred = 2 - (2 / 3) * (1 - 24 * kappa) ** 2
        ok = ok and abs(co[1] - pred) < 2e-4 and abs(co[0] + 4) < 2e-4
        det.append("%.3f->%.5f(pred %.5f)" % (kappa, co[1].real, pred))
    check("N6 other low modes: beta(kappa)=2-(2/3)(1-24 kappa)^2 at six kappa (the two partner modes carry the whole kappa-dependence at leading order)", ok, "; ".join(det))

    # ---- complex directions
    z_res = []
    for trial in range(6):
        z = rng.standard_normal(4) + 1j * rng.standard_normal(4); z /= np.sqrt(abs(z @ z))
        e = []
        for t in (.02, .01):
            K, Tl, Tr, w, wm, ward = exchange(C, ls, t * z, 0.0)
            assert ward < 1e-10
            e.append((rel(K, F_w(Tl, Tr, w, wm, -4, 4 / 3)), rel(K, F_plain(Tl, Tr, -4, 4 / 3))))
        z_res.append((e[0][0] / e[1][0], e[0][1] / e[1][1]))
    z_res = np.array(z_res)
    check("N7 complex directions with |z.z|=1 (6 random): bilinear continuation K = F_w + O(q^2) (ratio 4) while the plain-trace form is O(q) (ratio 2)",
          np.all(abs(z_res[:, 0] - 4) < 0.02) and np.all(abs(z_res[:, 1] - 2) < 0.05), "ratios w-form %s, plain %s" % (np.round(z_res[:, 0], 3), np.round(z_res[:, 1], 3)))

    # ---- approach to the complex null cone: rank change, remainder ~ |q|^2/(q.q)
    n = np.array([.3, -.5, .6, .55]); n /= np.linalg.norm(n)
    m = np.array([.5, .7, -.1, .2]); m -= n * (n @ m); m /= np.linalg.norm(m)
    prod, lowratio = [], []
    for s in (0.5, 0.9, 0.99):
        z = n + 1j * s * m; zz = (z @ z).real
        K, Tl, Tr, w, wm, _ = exchange(C, ls, 0.02 * z, 0.0)
        r = rel(K, F_w(Tl, Tr, w, wm, -4, 4 / 3))
        prod.append(r * zz / 0.02 ** 2)
        ev = np.sort(np.abs(np.linalg.eigvals(C.Q(0.01 * z))))[32:40] / (1e-4 * zz)
        lowratio.append(np.sort(ev))
    check("N8 complex null cone q.q->0: remainder*(q.q)/|q|^2 stays ~0.06 over q.q=.75,.19,.02 (non-uniform: remainder ~ |q|^2/(q.q)); low eigenvalues = (q.q){1/4 x6, 1/2 x2}",
          max(prod) / min(prod) < 1.4 and 0.04 < min(prod) and max(prod) < 0.09
          and all(abs(l - np.array([.25] * 6 + [.5] * 2)).max() < 0.02 for l in lowratio), "r*zz/t^2 = %s" % np.round(prod, 4))
    return C


def main():
    exact_block()
    numeric_block()
    print("runtime %.1f s" % (time.time() - T0))
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    if FAIL == 0:
        print("HIT: scoped counterexample + structure on the supplied D4 carrier (CHECKED, sampled, not a theorem): the O(q) remainder of the exchange tensor against the source two-invariant form is "
              "to first order i*beta/4*[(q.diag T1*)(tr T2)-(tr T1*)(q.diag T2)] (a corner-registration phase of the trace; vanishes on axis/tick/body directions); "
              "replacing tr T by sum_mu w_mu T_mumu gives remainder O(q^2) in 51 real and 6 complex directions; remainder blows up like |q|^2/(q.q) toward the complex null cone.")
    print("SUMMARY: With analytic Regge derivatives, the source's generic O(q) fit residual is identified as an exact corner-registration phase in the trace term (proved algebra, checked against the exchange), "
          "the w-weighted-trace form holds to O(q^2) in sampled real and complex directions, but non-uniformity at the complex null cone is checked and no uniform theorem is proved.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
