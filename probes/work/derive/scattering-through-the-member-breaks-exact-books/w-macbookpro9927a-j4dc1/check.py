#!/usr/bin/env python3
"""Exact checks for J:derive:scattering-through-the-member-breaks-exact-books:a2
(worker w-macbookpro9927a-j4dc1).  Every finite fact used in ATTEMPT.md is
checked here with exact arithmetic: sympy symbols and algebraic numbers,
fractions and Gaussian rationals.  No floating point decides anything; floats
are printed only as labels next to exact values.

Sections
  A  symbol identities: block 140 T1 current, the shell momentum g, lemma L0
  B  the pull's two-record Born kernel, checked in position space on the 4^3
     torus against an exact solve of block 53's clock law
  C  the regrouped first-order current J1 (placement algebra) on open boxes
  D  the witness shell pair: kinematics
  E  the witness Born amplitudes (distinguishable, symmetric, antisymmetric)
     and the on-shell first-order books defect; a second, off-grid witness
"""
import itertools
import time
from fractions import Fraction as F

import sympy as sp
from sympy.polys.domains import QQ_I

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]),
       sp.Matrix([[1, 0], [0, -1]])]
I2 = sp.eye(2)


def hmat(k):
    return sum((sp.sin(k[a]) * SIG[a] for a in range(3)), sp.zeros(2))


# ---------------------------------------------------------------- A
k1, k2, k3, K1 = sp.symbols('k1 k2 k3 K1', real=True)
kk = [k1, k2, k3]
h = hmat(kk)
okA1 = all(sp.simplify((h * h.diff(kk[a]) + h.diff(kk[a]) * h) / 2
                       - sp.sin(kk[a]) * sp.cos(kk[a]) * I2) == sp.zeros(2)
           and sp.simplify(h.diff(kk[a]) - sp.cos(kk[a]) * SIG[a]) == sp.zeros(2)
           for a in range(3))
check("A1", okA1, "velocity cos(k_a) sigma_a and (1/2){h, dh/dk_a} = sin k_a cos k_a * 1 "
      "(block 140 T1 in symbols: the one-record current is a scalar on the coin)")
okA2 = sp.simplify(sp.expand_trig(sp.sin(k1) * sp.cos(k1) + sp.sin(K1 - k1) * sp.cos(K1 - k1)
                                  - sp.sin(K1) * sp.cos(2 * k1 - K1))) == 0
check("A2", okA2, "P(k) + P(K - k) = sin K cos(2k - K) componentwise (block 143 T1)")
hv = sp.symbols('h1:4', real=True)
fv = sp.symbols('f1:4', real=True)
Hs = sum((hv[a] * SIG[a] for a in range(3)), sp.zeros(2))
Fs = sum((fv[a] * SIG[a] for a in range(3)), sp.zeros(2))
hh = sum(x * x for x in hv)
hf = sum(hv[a] * fv[a] for a in range(3))
lhs = Hs * (Hs * Fs - Fs * Hs) - (Hs * Fs - Fs * Hs) * Hs
rhs = 4 * sum(((hh * fv[a] - hf * hv[a]) * SIG[a] for a in range(3)), sp.zeros(2))
check("A3", sp.expand(lhs - rhs) == sp.zeros(2),
      "[h.s,[h.s,f.s]] = 4(|h|^2 f - (h.f)h).s: a one-body placement keeps the free "
      "books only if [h, f] = 0 (lemma L0)")

# ---------------------------------------------------------------- B
Z, ONE, IM = QQ_I(0, 0), QQ_I(1, 0), QQ_I(0, 1)


def q(a, b=0):
    return QQ_I(F(a), F(b))


def conj(z):
    return QQ_I(z.x, -z.y)


L4 = 4
sites4 = list(itertools.product(range(L4), repeat=3))
ix4 = {s: i for i, s in enumerate(sites4)}
n4 = len(sites4)
# block 53: L = I - A, A the six-neighbour average; neutral torus inverse solves
# (L + J/n) G = delta_0 - 1/n  (J all-ones), an invertible rational system.
M = sp.zeros(n4, n4)
for s in sites4:
    i = ix4[s]
    M[i, i] += 1
    for a in range(3):
        for sg in (1, -1):
            t = list(s)
            t[a] = (t[a] + sg) % L4
            M[i, ix4[tuple(t)]] -= sp.Rational(1, 6)
Lop = M.copy()
M = M + sp.ones(n4, n4) / n4
rhs = sp.Matrix([(1 if s == (0, 0, 0) else 0) - sp.Rational(1, n4) for s in sites4])
Gsol = M.LUsolve(rhs)
okG = (Lop * Gsol == rhs) and sum(Gsol) == 0
G4 = {s: Gsol[ix4[s]] for s in sites4}

def phase(n, x):  # e^{i (pi/2) n.x} as a Gaussian integer
    e = sum(n[a] * x[a] for a in range(3)) % 4
    return [ONE, IM, q(-1), q(0, -1)][e]


def hsym(n):  # h(k) at k = (pi/2) n, entries in Z[i]
    sv = [[0, 1, 0, -1][t % 4] for t in n]
    return [[q(sv[2]), q(sv[0], -sv[1])], [q(sv[0], sv[1]), q(-sv[2])]]


def applyH(psi):  # torus walk: H = sum_a sigma_a (T_a - T_a^-1)/(2i)
    out = {}
    for s in sites4:
        acc = [Z, Z]
        for a in range(3):
            tp = list(s); tp[a] = (tp[a] + 1) % L4
            tm = list(s); tm[a] = (tm[a] - 1) % L4
            d = [psi[tuple(tp)][c] - psi[tuple(tm)][c] for c in range(2)]
            sgm = [[[Z, ONE], [ONE, Z]], [[Z, q(0, -1)], [IM, Z]], [[ONE, Z], [Z, q(-1)]]][a]
            for r in range(2):
                acc[r] += (sgm[r][0] * d[0] + sgm[r][1] * d[1]) * q(0, F(-1, 2))
        out[s] = acc
    return out


def pw(n, u):
    return {s: [phase(n, s) * u[0], phase(n, s) * u[1]] for s in sites4}


def dens(psi_f, psi_i):  # x -> <psi_f| e_x |psi_i>, e_x = (Pi_x H + H Pi_x)/2
    Hi, Hf = applyH(psi_i), applyH(psi_f)
    return {s: (conj(psi_f[s][0]) * Hi[s][0] + conj(psi_f[s][1]) * Hi[s][1]
                + conj(Hf[s][0]) * psi_i[s][0] + conj(Hf[s][1]) * psi_i[s][1]) * q(F(1, 2))
            for s in sites4}


def ghat(n):  # 1/Lhat at p = (pi/2) n, neutral at p = 0
    if all(t % 4 == 0 for t in n):
        return F(0)
    c = sum([1, 0, -1, 0][t % 4] for t in n)
    return 1 / (1 - F(c, 3))


def ff(nf, ni, uf, ui):  # (1/2) uf^dag (h(kf) + h(ki)) ui
    A = [[hsym(nf)[r][c] + hsym(ni)[r][c] for c in range(2)] for r in range(2)]
    return sum(conj(uf[r]) * A[r][c] * ui[c] for r in range(2) for c in range(2)) * q(F(1, 2))


cases = [((1, 0, 3), (2, 1, 0), (0, 3, 1), (3, 2, 2)), ((1, 1, 0), (0, 2, 3), (3, 0, 1), (2, 3, 2)),
         ((2, 1, 1), (1, 1, 3), (1, 3, 0), (2, 3, 0)), ((1, 0, 3), (2, 1, 0), (1, 0, 3), (2, 1, 0)),
         ((1, 0, 3), (2, 1, 0), (0, 3, 1), (3, 2, 3))]
coins = [[q(1, 2), q(-1, 1)], [q(2), q(1, -3)], [q(0, 1), q(3, 1)], [q(-2, 1), q(1)]]
okB, nz = okG, 0
for (a1, a2, b1, b2) in cases:
    di = dens(pw(b1, coins[2]), pw(a1, coins[0]))
    dj = dens(pw(b2, coins[3]), pw(a2, coins[1]))
    direct = Z
    for x in sites4:
        for y in sites4:
            r = tuple((x[c] - y[c]) % L4 for c in range(3))
            gx = G4[r]
            direct += q(F(int(gx.p), int(gx.q))) * di[x] * dj[y]
    cons = all((a1[c] + a2[c] - b1[c] - b2[c]) % 4 == 0 for c in range(3))
    p = tuple((b1[c] - a1[c]) % 4 for c in range(3))
    formula = (q(n4) * q(ghat(p)) * ff(b1, a1, coins[2], coins[0]) * ff(b2, a2, coins[3], coins[1])
               if cons else Z)
    okB = okB and direct == formula
    nz += direct != Z
check("B1", okB and nz >= 3,
      f"4^3 torus, clock law solved exactly in position space: sum_xy G(x-y)<f1|e_x|i1><f2|e_y|i2> = "
      f"L^3 Ghat(k1'-k1) (1/2)u'(h'+h)u (x) (1/2)w'(h'+h)w in {len(cases)} cases "
      f"(incl. forward and non-conserving), Ghat = 1/(1 - sum cos p/3)")

# ---------------------------------------------------------------- C


def s_add(A, B, c=ONE):
    C = {i: dict(r) for i, r in A.items()}
    for i, r in B.items():
        Ci = C.setdefault(i, {})
        for j, v in r.items():
            Ci[j] = Ci.get(j, Z) + c * v
    return s_prune(C)


def s_prune(A):
    return {i: {j: v for j, v in r.items() if v != Z} for i, r in A.items()
            if any(v != Z for v in r.values())}


def s_mul(A, B):
    C = {}
    for i, r in A.items():
        Ci = {}
        for kx, a in r.items():
            for j, b in B.get(kx, {}).items():
                Ci[j] = Ci.get(j, Z) + a * b
        if Ci:
            C[i] = Ci
    return s_prune(C)


def s_scal(A, c):
    return s_prune({i: {j: c * v for j, v in r.items()} for i, r in A.items()})


def s_kron(A, B, nB):
    C = {}
    for i, r in A.items():
        for j, a in r.items():
            for kx, rb in B.items():
                Ci = C.setdefault(i * nB + kx, {})
                for l, b in rb.items():
                    Ci[j * nB + l] = Ci.get(j * nB + l, Z) + a * b
    return s_prune(C)


def s_comm(A, B):
    return s_add(s_mul(A, B), s_mul(B, A), q(-1))


def regroup_ok(dims):
    d = len(dims)
    sites = list(itertools.product(*[range(n) for n in dims]))
    N = len(sites)
    idx = {s: i for i, s in enumerate(sites)}
    sg = [[[Z, ONE], [ONE, Z]], [[Z, q(0, -1)], [IM, Z]], [[ONE, Z], [Z, q(-1)]]][:d]
    d1 = 2 * N
    H = {}
    for s in sites:
        for a in range(d):
            t = list(s); t[a] += 1; t = tuple(t)
            if t not in idx:
                continue
            i0, j0 = idx[s], idx[t]
            for c in range(2):
                for e_ in range(2):
                    val = sg[a][c][e_] * q(0, F(-1, 2))
                    H.setdefault(2 * i0 + c, {})
                    H[2 * i0 + c][2 * j0 + e_] = H[2 * i0 + c].get(2 * j0 + e_, Z) + val
                    H.setdefault(2 * j0 + c, {})
                    H[2 * j0 + c][2 * i0 + e_] = H[2 * j0 + c].get(2 * i0 + e_, Z) - val
    H = s_prune(H)
    herm = all(H.get(j, {}).get(i, Z) == conj(v) for i, r in H.items() for j, v in r.items())
    e = {}
    for s in sites:
        i = idx[s]
        P = {2 * i: {2 * i: ONE}, 2 * i + 1: {2 * i + 1: ONE}}
        e[s] = s_scal(s_add(s_mul(P, H), s_mul(H, P)), q(F(1, 2)))
    S = {}
    for s in sites:
        S = s_add(S, e[s])
    I1 = {i: {i: ONE} for i in range(d1)}
    H2 = s_add(s_kron(H, I1, d1), s_kron(I1, H, d1))

    def G(r):  # generic even kernel (the identity holds for any)
        return q(F(3, 7 + sum((a + 2) * t * t for a, t in enumerate(r)) + r[0] * r[-1]))

    def omega(x, y):  # generic placement weights, sum 1, with weight off both records
        th = F(1, 3) + F(x[0] + 2 * y[-1], 11)
        w = {}
        for site, wt in ((x, th), (y, 1 - th), (sites[(idx[x] + idx[y]) % N], F(1, 5)),
                         (sites[(2 * idx[x] + 1) % N], F(-1, 5))):
            w[site] = w.get(site, 0) + wt
        return w

    Hc = {s: s_scal(s_comm(e[s], H), IM) for s in sites}
    ok = herm and S == H
    for comp in range(d):
        D2 = {}
        for s in sites:
            if s[comp]:
                D2 = s_add(D2, s_add(s_kron(e[s], I1, d1), s_kron(I1, e[s], d1)), q(s[comp]))
        j = {}
        for x in sites:
            jx = {}
            for zz in sites:
                if zz[comp] != x[comp]:
                    jx = s_add(jx, s_comm(e[x], e[zz]), q(0, zz[comp] - x[comp]))
            j[x] = jx
        V, FV, R = {}, {}, {}
        for x in sites:
            for y in sites:
                g = G(tuple(x[a] - y[a] for a in range(d)))
                P = s_kron(e[x], e[y], d1)
                V = s_add(V, P, g)
                c = sum(F(ws[comp]) * wt for ws, wt in omega(x, y).items())
                FV = s_add(FV, P, g * q(c))
                T = s_add(s_kron(j[x], e[y], d1), s_kron(e[x], j[y], d1))
                T = s_add(T, s_kron(Hc[x], e[y], d1), q(F(x[comp]) - c))
                T = s_add(T, s_kron(e[x], Hc[y], d1), q(F(y[comp]) - c))
                R = s_add(R, T, g)
        J1 = s_scal(s_add(s_comm(V, D2), s_comm(H2, FV)), IM)
        ok = ok and J1 == R and bool(J1)
    return ok


okC = all(regroup_ok(dm) for dm in ((5,), (2, 3), (2, 2, 2)))
check("C1", okC, "open chain 5, box 2x3, box 2x2x2, generic even G and generic placement "
      "weights (incl. weight off both records): i[V,D2] + i[H2,F_V] = sum G(r)[j_x e_y + e_x j_y "
      "+ (x-c) i[e_x,H] e_y + (y-c) e_x i[e_y,H]], j_x = sum_z (z-x) i[e_x,e_z]")

# ---------------------------------------------------------------- D
pi = sp.pi


def vsub(a, b):
    return [sp.nsimplify(a[i] - b[i]) for i in range(3)]


def eps2(k):
    return sp.nsimplify(sum(sp.sin(t) ** 2 for t in k))


def gvec(k, m):
    return [sp.nsimplify((sp.sin(2 * k[a]) + sp.sin(2 * m[a])) / 2) for a in range(3)]


def Ghat(p):
    return sp.nsimplify(1 / (1 - sp.Rational(1, 3) * sum(sp.cos(t) for t in p)))


def is_zero_mod2pi(p):
    return all(sp.simplify(t / (2 * pi)).is_integer for t in p)


Kw = [pi / 4, pi / 4, 3 * pi / 4]
kw = [sp.Integer(0), pi / 2, pi / 4]
mw = vsub(Kw, kw)
kpw = [kw[1], kw[0], kw[2]]
mpw = vsub(Kw, kpw)
gi, gf = gvec(kw, mw), gvec(kpw, mpw)
pd, pe = vsub(kpw, kw), vsub(kpw, mw)
Ei = {(s1, s2): s1 * sp.sqrt(eps2(kw)) + s2 * sp.sqrt(eps2(mw)) for s1 in (1, -1) for s2 in (1, -1)}
Ef = {(s1, s2): s1 * sp.sqrt(eps2(kpw)) + s2 * sp.sqrt(eps2(mpw)) for s1 in (1, -1) for s2 in (1, -1)}
okD = (eps2(kw) == eps2(kpw) == sp.Rational(3, 2) and eps2(mw) == eps2(mpw) == 2
       and all(sp.simplify(Ei[b] - Ef[b]) == 0 for b in Ei)
       and len(set(sp.nsimplify(v) for v in Ei.values())) == 4
       and gi == [sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 2)]
       and gf == [-sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 2)]
       and not any(is_zero_mod2pi(vsub(a, b)) for a in (kpw, mpw) for b in (kw, mw))
       and Ghat(pd) == sp.Rational(3, 2) and sp.simplify(Ghat(pe) - (2 + sp.sqrt(2))) == 0
       and all(sp.simplify(t * 8 / (2 * pi)).is_integer for t in kw + mw + kpw + mpw))
check("D1", okD, "K=(pi/4,pi/4,3pi/4): (k,K-k)=((0,pi/2,pi/4),(pi/4,-pi/4,pi/2)) -> "
      "(k',K-k')=((pi/2,0,pi/4),(-pi/4,pi/4,pi/2)); eps^2 = 3/2, 2 kept, all four band "
      "energies equal and distinct; g: (1/2,-1/2,1/2) -> (-1/2,1/2,1/2); no transfer is 0 mod 2pi; "
      "Ghat = 3/2 (direct), 2+sqrt2 (exchange); all momenta on the 8-torus grid")

# ---------------------------------------------------------------- E


def proj(k, s):
    return (I2 + s * hmat(k) / sp.sqrt(eps2(k))) / 2


def Aff(kp, k):
    return (hmat(kp) + hmat(k)) / 2


def galois_norm(v):
    """product of the four conjugates of v in Q(sqrt2, sqrt3); nonzero iff v != 0."""
    r2, r3 = sp.sqrt(2), sp.sqrt(3)
    out = sp.Integer(1)
    for a in (1, -1):
        for b in (1, -1):
            out *= v.subs({sp.sqrt(6): a * b * sp.sqrt(6)}).subs({r2: a * r2, r3: b * r3})
    return sp.nsimplify(sp.expand(out))


def amplitudes(k, m, kp, mp, s1, s2):
    Pi1, Pi2, Pf1, Pf2 = proj(k, s1), proj(m, s2), proj(kp, s1), proj(mp, s2)
    Ga, Gb = Ghat(vsub(kp, k)), Ghat(vsub(kp, m))
    A1, A2, B1, B2 = Aff(kp, k), Aff(mp, m), Aff(kp, m), Aff(mp, k)
    aa = sp.nsimplify(sp.simplify(Ga ** 2 * (Pf1 * A1 * Pi1 * A1.H).trace() * (Pf2 * A2 * Pi2 * A2.H).trace()))
    bb = sp.nsimplify(sp.simplify(Gb ** 2 * (Pf1 * B1 * Pi2 * B1.H).trace() * (Pf2 * B2 * Pi1 * B2.H).trace()))
    ab = sp.simplify(Ga * Gb * (Pf1 * A1 * Pi1 * B2.H * Pf2 * A2 * Pi2 * B1.H).trace())
    rab = sp.nsimplify(sp.simplify(sp.re(sp.expand(ab))))
    return {'dist': aa, 'sym': sp.nsimplify(sp.expand(aa + bb + 2 * rab)),
            'anti': sp.nsimplify(sp.expand(aa + bb - 2 * rab))}


okE, table = True, []
for s1 in (1, -1):
    for s2 in (1, -1):
        am = amplitudes(kw, mw, kpw, mpw, s1, s2)
        for sec, v in am.items():
            nrm = galois_norm(v)
            good = nrm.is_Rational and nrm != 0
            okE = okE and good and (sec != 'dist' or v == sp.Rational(9, 4))
            table.append((s1, s2, sec, v, float(v)))
check("E1", okE, "|<f|V|i>|^2 at the witness, all 4 band pairs: distinguishable = 9/4 each; "
      "symmetric/antisymmetric are elements of Q(sqrt2,sqrt3) with nonzero rational Galois norm")
for s1, s2, sec, v, fl in table:
    if (s1, s2) in ((1, 1), (1, -1)) and sec != 'dist':
        print(f"    ({s1:+d},{s2:+d}) {sec}: {sp.sstr(v)}  (~{fl:.4f})")
dg = [gi[a] - gf[a] for a in range(3)]
okE2 = dg == [1, -1, 0] and all(v != 0 for (_, _, _, v, _) in table)
check("E2", okE2, "on-shell O(lambda) books defect <f|C1_a|i> = (g_a(i) - g_a(f)) <f|V|i>, "
      "g(i) - g(f) = (1,-1,0): nonzero for a = 1, 2 in every sector and band pair")

# an off-grid witness (distinguishable records): Pythagorean angles, K1 = K2


def ang(sn, cs):
    return (F(sn), F(cs))


def a_sub(a, b):
    return (a[0] * b[1] - a[1] * b[0], a[1] * b[1] + a[0] * b[0])


Kp = [ang(F(8, 17), F(15, 17)), ang(F(8, 17), F(15, 17)), ang(F(7, 25), F(24, 25))]
kq = [ang(F(3, 5), F(4, 5)), ang(F(5, 13), F(12, 13)), ang(F(20, 29), F(21, 29))]
mq = [a_sub(Kp[a], kq[a]) for a in range(3)]
kpq, mpq = [kq[1], kq[0], kq[2]], [mq[1], mq[0], mq[2]]
e2k, e2m = sum(t[0] ** 2 for t in kq), sum(t[0] ** 2 for t in mq)
dot1 = sum(kq[a][0] * kpq[a][0] for a in range(3)) / e2k
dot2 = sum(mq[a][0] * mpq[a][0] for a in range(3)) / e2m
cp = sum(a_sub(kpq[a], kq[a])[1] for a in range(3))
gh = 1 / (1 - cp / 3)
v2 = gh ** 2 * e2k * (1 + dot1) / 2 * e2m * (1 + dot2) / 2
g_i = [kq[a][0] * kq[a][1] + mq[a][0] * mq[a][1] for a in range(3)]
g_f = [kpq[a][0] * kpq[a][1] + mpq[a][0] * mpq[a][1] for a in range(3)]
okE3 = (mpq == [a_sub(Kp[a], kpq[a]) for a in range(3)] and v2 > 0 and g_i != g_f
        and sum(t[0] ** 2 for t in kpq) == e2k and sum(t[0] ** 2 for t in mpq) == e2m)
check("E3", okE3, f"off-grid shell pair (sin,cos of k: 3/5,4/5; 5/13,12/13; 20/29,21/29; "
      f"K1=K2: 8/17,15/17; K3: 7/25,24/25), axes 1,2 swapped: g_1 - g_2 = {g_i[0] - g_i[1]}, "
      f"|v|^2 = Ghat^2 eps^2(1+n.n')/2 eps~^2(1+m.m')/2 = {v2} > 0 for every band pair")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print("SUMMARY: PARTIAL first-order books identity for two walkers under block 53's pull: "
          "for every placement of the pull's energy in ATTEMPT.md's class the O(lambda) part of "
          "[H', J'] has on-shell off-forward kernel (g(k) - g(k'))<b|V|a>, placement-independent; "
          "the Born amplitude is nonzero at exact shell pairs where g changes (E1-E3), so exact "
          "books first fail at first order in the coupling; the all-orders scattering form stays "
          "conditional on a long-range wave-operator bridge.")
    print("HIT: under block 53's pull V = sum G(x-y) e_x e_y two walkers lose exact books at "
          "first order: for placements with first moment (x+y)/2 + beta r + rho0(r), sum |G rho0| "
          "finite, plus finite-range and one-body terms keeping the free books, the O(lambda) part "
          "of [H', J'] is (g(k) - g(k'))<b|V|a> on the shell off forward; at K = (pi/4,pi/4,3pi/4), "
          "k = (0,pi/2,pi/4) -> (pi/2,0,pi/4) the Born amplitude is nonzero (|v|^2 = 9/4; nonzero "
          "in both exchange sectors) while g changes by (1,-1,0); on every torus with 8 | L no "
          "J(lambda) = sum P + O(lambda) commutes with H2 + lambda V.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed exact check above")
