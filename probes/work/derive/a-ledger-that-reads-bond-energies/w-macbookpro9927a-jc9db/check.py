#!/usr/bin/env python3
"""a-ledger-that-reads-bond-energies, attempt a2 (worker w-macbookpro9927a-jc9db, claude-opus-5-5).

A relabelling moves the walk's clock phi into phi - Lam_xi, a bond operator.  Its bond part kappa_b
is the ledger's bond field; the content's response to it is 2 eps_b.  Exact arithmetic (Fractions,
Gaussian rationals, ranks certified modulo a prime against exact kernels) for every claim.  R4 is a
floating control and is evidence only.
"""
import random
import sys
import time
from fractions import Fraction as Fr
from itertools import product

import numpy as np

T0 = time.time()
random.seed(20260924)
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


# ---------------------------------------------------------------- Gaussian rationals
class GQ:
    __slots__ = ("r", "i")

    def __init__(s, r=0, i=0):
        s.r = r if isinstance(r, Fr) else Fr(r)
        s.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(a, b):
        if not isinstance(b, GQ):
            return GQ(a.r + b, a.i)
        return GQ(a.r + b.r, a.i + b.i)

    __radd__ = __add__

    def __sub__(a, b):
        if not isinstance(b, GQ):
            return GQ(a.r - b, a.i)
        return GQ(a.r - b.r, a.i - b.i)

    def __mul__(a, b):
        if not isinstance(b, GQ):
            return GQ(a.r * b, a.i * b)
        return GQ(a.r * b.r - a.i * b.i, a.r * b.i + a.i * b.r)

    __rmul__ = __mul__

    def __neg__(a):
        return GQ(-a.r, -a.i)

    def conj(a):
        return GQ(a.r, -a.i)

    def nz(a):
        return a.r != 0 or a.i != 0

    def __eq__(a, b):
        b = b if isinstance(b, GQ) else GQ(b)
        return a.r == b.r and a.i == b.i


ZERO = GQ(0)
MIH = GQ(0, Fr(-1, 2))   # 1/(2i) = -i/2


def rgq(m=3):
    return GQ(random.randint(-m, m), random.randint(-m, m))


# ---------------------------------------------------------------- torus and the walk
class Tor:
    def __init__(s, L):
        s.L = L
        s.S = list(product(range(L), repeat=3))
        s.ix = {x: i for i, x in enumerate(s.S)}
        s.N = len(s.S)
        s.nb = [[(s.ix[s.sh(x, a, 1)], s.ix[s.sh(x, a, -1)]) for a in range(3)] for x in s.S]

    def sh(s, x, a, m=1):
        y = list(x)
        y[a] = (y[a] + m) % s.L
        return tuple(y)

    def up(s, i, a, m=1):
        for _ in range(m % s.L):
            i = s.nb[i][a][0]
        return i


def sig(a, sp):
    p, q = sp
    if a == 0:
        return (q, p)
    if a == 1:
        return (GQ(q.i, -q.r), GQ(-p.i, p.r))   # (-i q, i p)
    return (p, -q)


def vadd(u, v):
    return [(x[0] + y[0], x[1] + y[1]) for x, y in zip(u, v)]


def vsub(u, v):
    return [(x[0] - y[0], x[1] - y[1]) for x, y in zip(u, v)]


def vmul(f, v):   # site function times a vector
    return [(f[i] * v[i][0], f[i] * v[i][1]) for i in range(len(v))]


def vscal(c, v):
    return [(c * x[0], c * x[1]) for x in v]


def inner(u, v):
    t = GQ(0)
    for x, y in zip(u, v):
        t = t + x[0].conj() * y[0] + x[1].conj() * y[1]
    return t


def spdot(p, q):   # p^dagger q for spinors
    return p[0].conj() * q[0] + p[1].conj() * q[1]


def S_(t, a, v):   # (S_a v)(x) = (v(x+e_a) - v(x-e_a))/(2i)
    return [((v[t.nb[i][a][0]][0] - v[t.nb[i][a][1]][0]) * MIH,
             (v[t.nb[i][a][0]][1] - v[t.nb[i][a][1]][1]) * MIH) for i in range(t.N)]


def C_(t, a, vb, v):   # (C_a[vb] v)(x) = (vb(x) v(x+e_a) + vb(x-e_a) v(x-e_a))/2, vb on bonds (x, a)
    out = []
    for i in range(t.N):
        u, d = t.nb[i][a]
        out.append(((vb[i] * v[u][0] + vb[d] * v[d][0]) * Fr(1, 2),
                    (vb[i] * v[u][1] + vb[d] * v[d][1]) * Fr(1, 2)))
    return out


def H_(t, v):
    out = [(ZERO, ZERO)] * t.N
    for a in range(3):
        out = vadd(out, [sig(a, sp) for sp in S_(t, a, v)])
    return out


def HB_(t, B, v):   # block 64: H[B] = H + sum_{a,j} sigma_a (1/2){C_a[B_a^j], S_j}
    out = H_(t, v)
    for a in range(3):
        for j in range(3):
            w = vadd(C_(t, a, B[a][j], S_(t, j, v)), S_(t, j, C_(t, a, B[a][j], v)))
            out = vadd(out, [sig(a, (sp[0] * Fr(1, 2), sp[1] * Fr(1, 2))) for sp in w])
    return out


def dphi(t, phi, j):
    return [phi[t.nb[i][j][0]] - phi[i] for i in range(t.N)]


def G_(t, xi, v):   # G_xi = (1/2) sum_j {xi_j, S_j}
    out = [(ZERO, ZERO)] * t.N
    for j in range(3):
        out = vadd(out, vscal(Fr(1, 2), vadd(vmul(xi[j], S_(t, j, v)), S_(t, j, vmul(xi[j], v)))))
    return out


def Lam_(t, phi, xi, v):   # Lam_xi = (1/2) sum_j {xi_j, C_j[d_j phi]}
    out = [(ZERO, ZERO)] * t.N
    for j in range(3):
        dp = dphi(t, phi, j)
        out = vadd(out, vscal(Fr(1, 2), vadd(vmul(xi[j], C_(t, j, dp, v)), C_(t, j, dp, vmul(xi[j], v)))))
    return out


def dkstar(t, phi, xi):   # the transported clock's bond part: -(1/2) d_j phi (xi_j(x) + xi_j(x+e_j))
    return [[-Fr(1, 2) * (phi[t.nb[i][j][0]] - phi[i]) * (xi[j][i] + xi[j][t.nb[i][j][0]])
             for i in range(t.N)] for j in range(3)]


def K_(t, kap, v):   # K = sum_b kappa_b h_b = sum_j C_j[kappa_j]
    out = [(ZERO, ZERO)] * t.N
    for j in range(3):
        out = vadd(out, C_(t, j, kap[j], v))
    return out


def bond_eps(t, psi, chi):   # eps_(x,j) = (1/2) Re[psi(x+e_j)^+ chi(x) + psi(x)^+ chi(x+e_j)]
    return [[Fr(1, 2) * (spdot(psi[t.nb[i][j][0]], chi[i]) + spdot(psi[i], chi[t.nb[i][j][0]])).r
             for i in range(t.N)] for j in range(3)]


def currents(t, c):   # block 63: J_a^j(x) = (1/2)Re[c(x+e_a)^+ s_a (S_j c)(x) + (S_j c)(x+e_a)^+ s_a c(x)]
    Sc = [S_(t, j, c) for j in range(3)]
    J = [[[None] * t.N for j in range(3)] for a in range(3)]
    for a in range(3):
        for j in range(3):
            for i in range(t.N):
                u = t.nb[i][a][0]
                J[a][j][i] = Fr(1, 2) * (spdot(c[u], sig(a, Sc[j][i])) + spdot(Sc[j][u], sig(a, c[i]))).r
    return J


def force66(t, phi, psi, chi):   # block 66: f_j = Re[(C_j[d_j phi]psi)^+ chi + psi^+ C_j[d_j phi] chi]
    f = []
    for j in range(3):
        dp = dphi(t, phi, j)
        Cp, Cc = C_(t, j, dp, psi), C_(t, j, dp, chi)
        f.append([(spdot(Cp[i], chi[i]) + spdot(psi[i], Cc[i])).r for i in range(t.N)])
    return f


def rand_state(t, m=3):
    return [(rgq(m), rgq(m)) for _ in range(t.N)]


def distinct_rates(t, den):   # rational clock roots with no two sites equal: no flat bond
    vals = random.sample(range(den), t.N)
    return [1 + Fr(v, den) for v in vals]


def rand_xi(t, m=3):
    return [[Fr(random.randint(-m, m)) for _ in range(t.N)] for j in range(3)]


def basis(t, i, c):
    v = [(ZERO, ZERO)] * t.N
    v[i] = (GQ(1), ZERO) if c == 0 else (ZERO, GQ(1))
    return v


# ---------------------------------------------------------------- modular ranks
P = 2147483647


def modp(q):
    q = Fr(q)
    return (q.numerator % P) * pow(q.denominator % P, P - 2, P) % P


def rank_modp(M):
    M = M.copy() % P
    n, m = M.shape
    r = 0
    for c in range(m):
        if r == n:
            break
        nz = np.nonzero(M[r:, c])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            M[[r, pr]] = M[[pr, r]]
        M[r] = (M[r] * pow(int(M[r, c]), P - 2, P)) % P
        rows = np.nonzero(M[:, c])[0]
        rows = rows[rows != r]
        if len(rows):
            M[rows] = (M[rows] - np.outer(M[rows, c], M[r]) % P) % P
        r += 1
    return r


def gram_rank(rows, ncol):   # rows: list of dict col -> Fraction; rank of the Gram matrix mod P
    G = np.zeros((ncol, ncol), dtype=np.int64)
    for row in rows:
        it = [(c, modp(v)) for c, v in row.items() if v != 0]
        for c1, v1 in it:
            for c2, v2 in it:
                G[c1, c2] = (G[c1, c2] + v1 * v2) % P
    return rank_modp(G)


# ================================================================= Q: the content and the clock's bond part
t4 = Tor(4)
phi4 = distinct_rates(t4, 97)
xi4 = rand_xi(t4)
# Q1: i[phi, G_xi] = -Lam_xi as operators; Lam_xi = sum_b (1/2) d_j phi_b (xi_j(x)+xi_j(x+e_j)) h_b
ok1 = ok2 = True
beta = [[Fr(1, 2) * (phi4[t4.nb[i][j][0]] - phi4[i]) * (xi4[j][i] + xi4[j][t4.nb[i][j][0]])
         for i in range(t4.N)] for j in range(3)]
for i in range(t4.N):
    for c in (0, 1):
        e = basis(t4, i, c)
        comm = vsub(vmul(phi4, G_(t4, xi4, e)), G_(t4, xi4, vmul(phi4, e)))
        lhs = [(GQ(0, 1) * p[0], GQ(0, 1) * p[1]) for p in comm]
        lam = Lam_(t4, phi4, xi4, e)
        ok1 &= all(x[0] == -y[0] and x[1] == -y[1] for x, y in zip(lhs, lam))
        bf = K_(t4, beta, e)
        ok2 &= all(x[0] == y[0] and x[1] == y[1] for x, y in zip(lam, bf))
        ok2 &= not (lam[i][0].nz() or lam[i][1].nz())    # no diagonal part
check("Q1 moved clock", ok1 and ok2, "i[phi,G_xi] = -Lam_xi on all 128 basis vectors of 4^3; Lam_xi is a pure bond "
      "operator with bond weights (1/2)d_j phi (xi_j(x)+xi_j(x+e_j))")

# Q2: responses of E_c = <psi|Phi H[B] Phi|psi>, Phi = phi + K, at B = 0, K = 0
psi = rand_state(t4)
cphi = vmul(phi4, psi)
chi = H_(t4, cphi)
eps = bond_eps(t4, psi, chi)
rho = [(spdot(psi[i], chi[i])).r for i in range(t4.N)]
kap = [[Fr(random.randint(-4, 4), 3) for _ in range(t4.N)] for j in range(3)]
Kp = K_(t4, kap, psi)
Ep = inner(vadd(cphi, Kp), H_(t4, vadd(cphi, Kp)))
Em = inner(vsub(cphi, Kp), H_(t4, vsub(cphi, Kp)))
okk = (Ep - Em) * Fr(1, 2) == GQ(sum(2 * kap[j][i] * eps[j][i] for j in range(3) for i in range(t4.N)))
Bf = [[[Fr(random.randint(-3, 3), 2) for _ in range(t4.N)] for j in range(3)] for a in range(3)]
J4 = currents(t4, cphi)
E0 = inner(cphi, chi)
EB = inner(cphi, HB_(t4, Bf, cphi))
okb = EB - E0 == GQ(sum(Bf[a][j][i] * J4[a][j][i] for a in range(3) for j in range(3) for i in range(t4.N)))
dl = [Fr(random.randint(-3, 3), 7) for _ in range(t4.N)]
Pp, Pm = vmul([phi4[i] + dl[i] for i in range(t4.N)], psi), vmul([phi4[i] - dl[i] for i in range(t4.N)], psi)
okf = (inner(Pp, H_(t4, Pp)) - inner(Pm, H_(t4, Pm))) * Fr(1, 2) == GQ(sum(2 * dl[i] * rho[i] for i in range(t4.N)))
check("Q2 responses", okk and okb and okf, "dE/dkappa_b = 2 eps_b, dE/dB = J[phi psi], dE/dphi_x = 2 rho_x "
      "(so dE/du_x = energy density), exact symmetric differences on 4^3")

# Q3: the content's relabelling identity and block 106's bond form of the force
Gp = G_(t4, xi4, psi)
Hwp = vmul(phi4, chi)
ddt = GQ(2) * GQ(inner(Gp, Hwp).i)            # d<G_xi>/dt = <i[H_w, G_xi]> = 2 Im<G psi|H_w psi>
dk = dkstar(t4, phi4, xi4)
curr = sum((xi4[j][t4.nb[i][a][0]] - xi4[j][i]) * J4[a][j][i] for a in range(3) for j in range(3) for i in range(t4.N))
bond = sum(2 * eps[j][i] * dk[j][i] for j in range(3) for i in range(t4.N))
f66 = force66(t4, phi4, psi, chi)
fb = [[(phi4[t4.nb[i][j][0]] - phi4[i]) * eps[j][i] + (phi4[i] - phi4[t4.nb[i][j][1]]) * eps[j][t4.nb[i][j][1]]
       for i in range(t4.N)] for j in range(3)]
okT2 = all(f66[j][i] == fb[j][i] for j in range(3) for i in range(t4.N))
fsum = sum(xi4[j][i] * fb[j][i] for j in range(3) for i in range(t4.N))
check("Q3 content identity", okT2 and ddt == GQ(curr - fsum) and (-ddt).r + curr + bond == 0,
      "f = d_j phi eps_j(x) + d_j phi eps_j(x-e_j) at all 192 site-directions; d<G>/dt = sum(d xi)J - sum xi f; "
      "<i[G,H_w]> + sum(d xi)J + sum 2 eps dkappa* = 0 (value of d<G>/dt here: %s)" % float(ddt.r))


# ================================================================= I, R: the ledger's invariants and its identity
def inv_rows(t, phi):
    """the 9N curls and the 9N bond invariants as sparse linear functionals of (B, kappa)."""
    vb = lambda a, j, i: ("B", a, j, i)
    vk = lambda j, i: ("k", j, i)
    rows = []
    for i in range(t.N):
        for a in range(3):
            for b in range(a + 1, 3):
                for j in range(3):   # F_ab^j(x) = d_a B_b^j - d_b B_a^j
                    r = {}
                    for key, c in ((vb(b, j, t.nb[i][a][0]), 1), (vb(b, j, i), -1), (vb(a, j, t.nb[i][b][0]), -1), (vb(a, j, i), 1)):
                        r[key] = r.get(key, 0) + c
                    rows.append((i, {k: Fr(v) for k, v in r.items() if v}))
        for a in range(3):
            for j in range(3):   # Itilde_aj(x)
                ia, ij = t.nb[i][a][0], t.nb[i][j][0]
                p0 = phi[ij] - phi[i]
                p1 = phi[t.nb[ia][j][0]] - phi[ia]
                r = {}
                for key, c in ((vk(j, ia), -2 * p0), (vk(j, i), 2 * p1), (vb(a, j, i), -p0 * p1), (vb(a, j, ij), -p0 * p1)):
                    r[key] = r.get(key, 0) + c
                rows.append((i, {k: v for k, v in r.items() if v != 0}))
    return rows


def gauge(t, phi, xi):   # V(xi): B += d xi, kappa += dkappa*(xi)
    z = {}
    for i in range(t.N):
        for a in range(3):
            for j in range(3):
                z[("B", a, j, i)] = xi[j][t.nb[i][a][0]] - xi[j][i]
    dk = dkstar(t, phi, xi)
    for j in range(3):
        for i in range(t.N):
            z[("k", j, i)] = dk[j][i]
    return z


def ev(row, z):
    return sum(c * z.get(k, 0) for k, c in row.items())


for L in (3, 4):
    t = Tor(L)
    phi = distinct_rates(t, 97)
    rows = inv_rows(t, phi)
    keys = [("B", a, j, i) for a in range(3) for j in range(3) for i in range(t.N)] + [("k", j, i) for j in range(3) for i in range(t.N)]
    z = {k: Fr(random.randint(-5, 5), random.randint(1, 3)) for k in keys}
    xi = rand_xi(t)
    g = gauge(t, phi, xi)
    zg = {k: z[k] + g[k] for k in keys}
    okI1 = all(ev(r, z) == ev(r, zg) for _, r in rows)
    # F_2 = (1/2) sum_rows w_x row(z)^2; gradient; the identity in site form
    w = [p * p for p in phi]
    grad = {k: Fr(0) for k in keys}
    for i, r in rows:
        val = w[i] * ev(r, z)
        for k, c in r.items():
            grad[k] += val * c
    okI2 = True
    for j in range(3):
        for i in range(t.N):
            divE = sum(grad[("B", a, j, i)] - grad[("B", a, j, t.nb[i][a][1])] for a in range(3))
            im = t.nb[i][j][1]
            rhs = -Fr(1, 2) * ((phi[t.nb[i][j][0]] - phi[i]) * grad[("k", j, i)] + (phi[i] - phi[im]) * grad[("k", j, im)])
            okI2 &= divE == rhs
    # R1-R2: A V = 0 on every gauge basis vector; ranks certify ker A = span V exactly
    col = {k: n for n, k in enumerate(keys)}
    okR1 = True
    Vrows = []
    for jj in range(3):
        for y in range(t.N):
            e = [[Fr(0)] * t.N for _ in range(3)]
            e[jj][y] = Fr(1)
            gv = gauge(t, phi, e)
            okR1 &= all(ev(r, gv) == 0 for _, r in rows)
            Vrows.append({col[k]: v for k, v in gv.items() if v != 0})
    # rank V: Gram of V's columns (3N vectors) = rank of the 3N x 12N matrix whose rows are V(e)
    VT = np.zeros((3 * t.N, 12 * t.N), dtype=np.int64)
    for n, row in enumerate(Vrows):
        for c, v in row.items():
            VT[n, c] = modp(v)
    rV = rank_modp(VT)
    rA = gram_rank([{col[k]: v for k, v in r.items()} for _, r in rows], 12 * t.N)
    check("I1-I2 L=%d" % L, okI1 and okI2, "the %d curls and %d bond invariants are unchanged by a finite relabelling; "
          "the member's identity div E^j = -(1/2)[d_j phi K_(x,j) + d_j phi(x-e_j) K_(x-e_j,j)] at all %d site-directions"
          % (9 * t.N, 9 * t.N, 3 * t.N))
    check("R1-R2 L=%d" % L, okR1 and rV == 3 * t.N and rA == 9 * t.N,
          "A V = 0 on all %d gauge vectors; rank V = %d, rank A = %d = 12N - 3N: ker A = span V, "
          "so the static equations are solvable iff the walk's law holds" % (3 * t.N, rV, rA))

# I3: the demand, with E = -J[phi psi], K = -2 eps, the residual paired with xi is d<G_xi>/dt (4^3 data above)
R = []
for j in range(3):
    for i in range(t4.N):
        divE = sum(-J4[a][j][i] + J4[a][j][t4.nb[i][a][1]] for a in range(3))
        im = t4.nb[i][j][1]
        R.append(divE + Fr(1, 2) * ((phi4[t4.nb[i][j][0]] - phi4[i]) * (-2 * eps[j][i]) + (phi4[i] - phi4[im]) * (-2 * eps[j][im])))
pair = sum(xi4[j][i] * R[j * t4.N + i] for j in range(3) for i in range(t4.N))
check("I3 demand", pair == ddt.r and ddt.r != 0, "with the static equations the identity's residual is -div J[phi psi] - f "
      "and pairs with xi to d<G_xi>/dt exactly; a non-stationary random state leaves it nonzero")

# R4 (floating control, evidence only): stationary states of H_w on 5^3 (a torus with an odd side, see S2)
SG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], dtype=complex)]


def box(Ls):
    sites = list(product(*[range(l) for l in Ls]))
    ixb = {x: i for i, x in enumerate(sites)}
    Nb = len(sites)
    up = np.array([[ixb[tuple((x[k] + (k == a)) % Ls[k] for k in range(3))] for a in range(3)] for x in sites])
    dn = np.array([[ixb[tuple((x[k] - (k == a)) % Ls[k] for k in range(3))] for a in range(3)] for x in sites])
    S = []
    for a in range(3):
        M = np.zeros((Nb, Nb), dtype=complex)
        M[np.arange(Nb), up[:, a]] += -0.5j
        M[np.arange(Nb), dn[:, a]] += 0.5j
        S.append(M)
    return Nb, up, dn, sum(np.kron(S[a], SG[a]) for a in range(3))


def sources_all(Nb, up, dn, H, ph, V):   # eps (3, N, m) and J (3, 3, N, m) for the columns of V
    m = V.shape[1]
    ps = V.reshape(Nb, 2, m)
    cp = ph[:, None, None] * ps
    ch = (H @ cp.reshape(2 * Nb, m)).reshape(Nb, 2, m)
    eps = np.array([0.5 * np.real(np.sum(ps[up[:, j]].conj() * ch + ps.conj() * ch[up[:, j]], axis=1)) for j in range(3)])
    Sc = [(cp[up[:, j]] - cp[dn[:, j]]) * (-0.5j) for j in range(3)]
    J = np.array([[0.5 * np.real(np.sum(cp[up[:, a]].conj() * np.einsum("cd,ndm->ncm", SG[a], Sc[j])
                                        + Sc[j][up[:, a]].conj() * np.einsum("cd,ndm->ncm", SG[a], cp), axis=1))
                   for j in range(3)] for a in range(3)])
    return eps, J


t5r = Tor(5)
phi5r = distinct_rates(t5r, 251)
N5, up5, dn5, H5 = box((5, 5, 5))
ph5 = np.array([float(p) for p in phi5r])
P5 = np.kron(np.diag(ph5), np.eye(2))
vals5, vecs5 = np.linalg.eigh(P5 @ H5 @ P5)
rows5 = inv_rows(t5r, phi5r)
keys5 = [("B", a, j, i) for a in range(3) for j in range(3) for i in range(N5)] + [("k", j, i) for j in range(3) for i in range(N5)]
col5 = {k: n for n, k in enumerate(keys5)}
A5 = np.zeros((len(rows5), len(keys5)))
W5 = np.zeros(len(rows5))
for n, (i, r) in enumerate(rows5):
    W5[n] = float(phi5r[i]) ** 2
    for k, c in r.items():
        A5[n, col5[k]] = float(c)
M5 = A5.T @ (W5[:, None] * A5)
e5all, J5all = sources_all(N5, up5, dn5, H5, ph5, vecs5)
best = int(np.argmax([np.linalg.norm(e5all[:, :, n]) for n in range(2 * N5)]))
rng = np.random.default_rng(7)
vr = rng.normal(size=(2 * N5, 1)) + 1j * rng.normal(size=(2 * N5, 1))
vr /= np.linalg.norm(vr)
er, Jr = sources_all(N5, up5, dn5, H5, ph5, vr)
res = []
for ee, JJ in ((e5all[:, :, best:best + 1], J5all[:, :, :, best:best + 1]), (er, Jr)):
    rhs = np.zeros(len(keys5))
    for a in range(3):
        for j in range(3):
            rhs[[col5[("B", a, j, i)] for i in range(N5)]] = -JJ[a, j, :, 0]
    for j in range(3):
        rhs[[col5[("k", j, i)] for i in range(N5)]] = -2 * ee[j, :, 0]
    zz = np.linalg.lstsq(M5, rhs, rcond=None)[0]
    res.append((np.linalg.norm(rhs), np.linalg.norm(M5 @ zz - rhs) / np.linalg.norm(rhs)))
print("R4 control (float, evidence): the member's static equations on 5^3; eigenstate of H_w with the largest bond "
      "energy (|sources| %.2f): relative residual %.1e; random state: %.2f" % (res[0][0], res[0][1], res[1][1]))

# ================================================================= N: which transports demand f at every state
def spatial_S(t, a):
    M = {}
    for i in range(t.N):
        M[(i, t.nb[i][a][0])] = GQ(0, Fr(-1, 2))
        M[(i, t.nb[i][a][1])] = M.get((i, t.nb[i][a][1]), ZERO) + GQ(0, Fr(1, 2))
    return M


def smul(A, B):
    Bi = {}
    for (i, j), v in B.items():
        Bi.setdefault(i, []).append((j, v))
    C = {}
    for (i, k), v in A.items():
        for j, u in Bi.get(k, ()):
            C[(i, j)] = C.get((i, j), ZERO) + v * u
    return {k: v for k, v in C.items() if v.nz()}


def Qmap(t, phi, dPhi, Sa):   # spatial coefficient of sigma_a in dPhi H phi + phi H dPhi
    left = smul(dPhi, Sa)
    right = smul(Sa, dPhi)
    Q = {}
    for (i, j), v in left.items():
        Q[(i, j)] = Q.get((i, j), ZERO) + v * phi[j]
    for (i, j), v in right.items():
        Q[(i, j)] = Q.get((i, j), ZERO) + phi[i] * v
    return {k: v for k, v in Q.items() if v.nz()}


def dPhi_of(t, D, kap):
    M = {}
    for i in range(t.N):
        if D[i] != 0:
            M[(i, i)] = GQ(D[i])
        for j in range(3):
            if kap[j][i] != 0:
                u = t.nb[i][j][0]
                M[(i, u)] = M.get((i, u), ZERO) + GQ(kap[j][i] / 2)
                M[(u, i)] = M.get((u, i), ZERO) + GQ(kap[j][i] / 2)
    return M


# N1: block structure on 5^3 against the stated formulas
t5 = Tor(5)
phi5 = distinct_rates(t5, 197)
D = [Fr(random.randint(-4, 4), 5) for _ in range(t5.N)]
kp = [[Fr(random.randint(-4, 4), 3) for _ in range(t5.N)] for j in range(3)]
S5 = [spatial_S(t5, a) for a in range(3)]
okN1 = True


def kfun(t, kp, i, tt, b):   # kappa of the bond from site i in direction t*e_b
    return kp[b][i] if tt == 1 else kp[b][t.nb[i][b][1]]


for a in range(3):
    Qa = Qmap(t5, phi5, dPhi_of(t5, D, kp), S5[a])
    F = {}
    for i in range(t5.N):
        for s in (1, -1):
            y = t5.up(i, a, s % 5)
            F[(i, y)] = F.get((i, y), ZERO) + GQ(0, Fr(-s, 2)) * (D[i] * phi5[y] + phi5[i] * D[y])
            for b in range(3):
                for tt in (1, -1):
                    if b == a and tt != s:
                        continue
                    ia = t5.up(i, a, s % 5)
                    y2 = t5.up(ia, b, tt % 5)
                    F[(i, y2)] = F.get((i, y2), ZERO) + GQ(0, Fr(-s, 4)) * (kfun(t5, kp, i, tt, b) * phi5[y2] + phi5[i] * kfun(t5, kp, ia, tt, b))
    F = {k: v for k, v in F.items() if v.nz()}
    okN1 &= set(F) == set(Qa) and all(F[k] == Qa[k] for k in F)
check("N1 block formulas", okN1, "on 5^3, dPhi H phi + phi H dPhi = sum_a sigma_a Q_a with Q_a's reach-1 blocks from the "
      "site part only and its reach-0/2 blocks from the bond part only, as stated in step 9")

# N2: a two-site state has zero energy density everywhere and a force
y0 = t5.ix[(0, 0, 0)]
a = 2
y2 = t5.up(y0, a, 2)
ps = [(ZERO, ZERO)] * t5.N
ps[y0] = (GQ(1), ZERO)
ps[y2] = (GQ(0, 1), ZERO)
ch5 = H_(t5, vmul(phi5, ps))
en = [phi5[i] * spdot(ps[i], ch5[i]).r for i in range(t5.N)]
e5 = bond_eps(t5, ps, ch5)
f5 = force66(t5, phi5, ps, ch5)
fa = f5[a][y0]
check("N2 two-site witness", all(v == 0 for v in en) and fa == (phi5[t5.nb[y0][a][0]] - phi5[y0]) * phi5[y2] / 4 and fa != 0,
      "psi = (1,0) at y, (i,0) at y+2e_3 on 5^3: energy density 0 at all 125 sites, f_3(y) = d_3 phi(y) phi(y+2e_3)/4 = %s"
      % fa)


def null_dim(t, phi):
    S = [spatial_S(t, a) for a in range(3)]
    unknown = [("D", i) for i in range(t.N)] + [("k", j, i) for j in range(3) for i in range(t.N)]
    rows = {}
    for n, u in enumerate(unknown):
        Dv = [Fr(0)] * t.N
        kv = [[Fr(0)] * t.N for _ in range(3)]
        if u[0] == "D":
            Dv[u[1]] = Fr(1)
        else:
            kv[u[1]][u[2]] = Fr(1)
        dP = dPhi_of(t, Dv, kv)
        for a in range(3):
            for (i, j), v in Qmap(t, phi, dP, S[a]).items():
                for part, val in (("r", v.r), ("i", v.i)):
                    if val != 0:
                        rows.setdefault((a, i, j, part), {})[n] = val
    return len(unknown) - gram_rank(list(rows.values()), len(unknown)), S


nd5, _ = null_dim(t5, phi5)
t6 = Tor(6)
phi6 = distinct_rates(t6, 401)
nd6, S6 = null_dim(t6, phi6)
gam = [Fr((-1) ** sum(x)) * phi6[i] for i, x in enumerate(t6.S)]
okg = all(not Qmap(t6, phi6, dPhi_of(t6, gam, [[Fr(0)] * t6.N] * 3), S6[a]) for a in range(3))
one = [Fr(1)] * t6.N
nd6u, _ = null_dim(t6, one)
stag = [Fr((-1) ** sum(x)) for x in t6.S]
oku = all(not Qmap(t6, one, dPhi_of(t6, [Fr(0)] * t6.N, [stag if j == b else [Fr(0)] * t6.N for j in range(3)]), S6[a])
          for b in range(3) for a in range(3))
# the rate condition of step 11 holds for these random rates: every bond (x,b) has a transverse a with
# d_b u(x) + d_b u(x+e_a) != 0, i.e. phi(x+e_a+e_b) phi(x+e_b) != phi(x) phi(x+e_a)
cond = all(any(phi6[t6.up(t6.up(i, a), b)] * phi6[t6.up(i, b)] != phi6[i] * phi6[t6.up(i, a)] for a in range(3) if a != b)
           for i in range(t6.N) for b in range(3))
check("N3 null directions", nd5 == 0 and nd6 == 1 and okg and nd6u == 4 and oku and cond,
      "dim N(phi) = %d on 5^3 and %d on 6^3 (spanned by Gamma phi) for random rates; %d at uniform rates on 6^3 "
      "(Gamma phi and the three staggered bond fields)" % (nd5, nd6, nd6u))

# ================================================================= C: the continuum reading of the moved bond part
import sympy as sp

h = sp.symbols("h")
PD, XD, SD = sp.symbols("p0:4"), sp.symbols("x0:4"), sp.symbols("s0:4")   # derivatives 0..3 at x


def tay(c, D):   # value at x + c h through order h^3
    return sum(D[n] * (c * h) ** n / sp.factorial(n) for n in range(4))


def kf(c):   # moved bond part on the bond from x + c h to x + (c+1) h
    return -sp.Rational(1, 2) * (tay(c + 1, PD) - tay(c, PD)) * (tay(c, XD) + tay(c + 1, XD))


Kpsi = (kf(0) * tay(1, SD) + kf(-1) * tay(-1, SD)) / 2
expr = sp.expand(Kpsi + h * XD[0] * PD[1] * SD[0])
check("C1 continuum", all(sp.expand(expr.coeff(h, n)) == 0 for n in range(3)),
      "on smooth amplitudes the moved bond part acts as -h xi phi' + O(h^3): the clock carried along, phi(x - h xi)")

# ================================================================= E: block 106's two plane waves
t = t4
one4 = [Fr(1)] * t.N
wA = [((GQ(0, 1) if x[0] % 4 == 1 else GQ(-1) if x[0] % 4 == 2 else GQ(0, -1) if x[0] % 4 == 3 else GQ(1)),) for x in t.S]
psA = [(p[0], p[0]) for p in wA]                         # k = (pi/2,0,0), spinor (1,1)
wB = [((GQ(0, 1) if x[1] % 4 == 1 else GQ(-1) if x[1] % 4 == 2 else GQ(0, -1) if x[1] % 4 == 3 else GQ(1)),) for x in t.S]
psB = [(p[0], p[0] * GQ(0, 1)) for p in wB]              # k = (0,pi/2,0), spinor (1,i)
out = []
for pw in (psA, psB):
    chp = H_(t, pw)
    stat = all(chp[i][0] == pw[i][0] and chp[i][1] == pw[i][1] for i in range(t.N))
    enp = {spdot(pw[i], chp[i]).r for i in range(t.N)}
    Jp = currents(t, pw)
    jz = all(Jp[a][j][i] == 0 for a in range(3) for j in range(3) for i in range(t.N))
    ep = {v for v in bond_eps(t, pw, chp)[0]}
    out.append((stat, enp, jz, ep))
check("E1 plane waves", all(o[0] and o[2] for o in out) and out[0][1] == out[1][1] == {2} and out[0][3] == {0} and out[1][3] == {2},
      "energy one, energy density 2 and zero current at every site for both; bond energy along e_1: 0 and 2")

# ================================================================= S: tori with every side even (side result)
t = t4
phiS = distinct_rates(t, 97)


def U_(c, v):   # U_c = sigma_c Gamma_a Gamma_b, {a, b, c} = {1, 2, 3}
    ab = [k for k in range(3) if k != c]
    return [tuple(q * ((-1) ** (x[ab[0]] + x[ab[1]])) for q in sig(c, v[i])) for i, x in enumerate(t.S)]


def Th_(v):   # Theta = sigma_2 K
    return [sig(1, (p[0].conj(), p[1].conj())) for p in v]


def Hw_(v):
    return vmul(phiS, H_(t, vmul(phiS, v)))


def veq(u, v, sgn=1):
    return all(p[0] == q[0] * sgn and p[1] == q[1] * sgn for p, q in zip(u, v))


okS = True
for i in range(t.N):
    for cc in (0, 1):
        e = basis(t, i, cc)
        for c in range(3):
            okS &= veq(U_(c, Hw_(e)), Hw_(U_(c, e))) and veq(Th_(U_(c, e)), U_(c, Th_(e)), -1) and veq(U_(c, U_(c, e)), e)
        okS &= veq(Th_(Hw_(e)), Hw_(Th_(e)))
        okS &= veq(U_(0, U_(1, e)), [(GQ(0, 1) * p[0], GQ(0, 1) * p[1]) for p in U_(2, e)])
# sign pattern of the bond operators h_(x,j) and of block 63's current operators sigma_a (1/2){h_(x,a), S_j};
# both are Theta-even; checked on every basis vector their columns can reach
for i in (0, t.ix[(1, 0, 0)]):
    for j in range(3):
        kj = [[Fr(0)] * t.N for _ in range(3)]
        kj[j][i] = Fr(1)
        for ii in (i, t.nb[i][j][0]):
            for cc in (0, 1):
                e = basis(t, ii, cc)
                okS &= veq(Th_(K_(t, kj, e)), K_(t, kj, Th_(e)))
                for c in range(3):
                    okS &= veq(U_(c, K_(t, kj, U_(c, e))), K_(t, kj, e), 1 if j == c else -1)
        for a in range(3):
            ka = [[Fr(0)] * t.N for _ in range(3)]
            ka[a][i] = Fr(1)
            O = lambda v: [sig(a, (q[0] * Fr(1, 2), q[1] * Fr(1, 2))) for q in vadd(K_(t, ka, S_(t, j, v)), S_(t, j, K_(t, ka, v)))]
            ia = t.nb[i][a][0]
            reach = {i, ia, t.nb[i][j][0], t.nb[i][j][1], t.nb[ia][j][0], t.nb[ia][j][1]}
            for ii in reach:
                for cc in (0, 1):
                    e = basis(t, ii, cc)
                    okS &= veq(Th_(O(e)), O(Th_(e)))
                    for c in range(3):
                        okS &= veq(U_(c, O(U_(c, e))), O(e), 1 if j == c else -1)
check("S1 doubler symmetries", okS, "on 4^3 with random rates: U_c = sigma_c Gamma_a Gamma_b and Theta = sigma_2 K commute "
      "with H_w, U_1U_2 = iU_3, Theta U_c = -U_c Theta; h_(x,j) and the current operators are Theta-even, commute "
      "with U_j and anticommute with U_c, c != j")
out = []
for Ls in ((3, 3, 3), (5, 5, 5), (6, 5, 4), (4, 4, 4), (4, 4, 6), (6, 6, 6)):
    Nb, upb, dnb, Hb = box(Ls)
    phb = 1 + np.random.default_rng(sum(Ls)).random(Nb)
    Pb = np.kron(np.diag(phb), np.eye(2))
    wb, Vb = np.linalg.eigh(Pb @ Hb @ Pb)
    eb, Jb = sources_all(Nb, upb, dnb, Hb, phb, Vb)
    lev = np.split(wb, np.nonzero(np.diff(wb) > 1e-9)[0] + 1)
    mult = max(len(g) for g in lev if abs(g[0]) > 1e-9)
    out.append("%dx%dx%d: %.0e/%.0e/%d" % (Ls + (np.abs(eb).max(), np.abs(Jb).max(), mult)))
print("S2 (float, evidence) max|eps|/max|J| over all eigenstates, largest nonzero level: " + "; ".join(out))

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PROVED (a): a relabelling moves the walk's clock phi to phi - Lam_xi, whose bond part "
      "kappa_b -> kappa_b - (1/2)d_j phi(x)(xi_j(x)+xi_j(x+e_j)) is a bond field with source 2 eps_b; every ledger "
      "unchanged by B -> B + d xi with kappa so moved has static equations that demand exactly div J[phi psi] = -f "
      "at every site, for every state and positive rate field; a local member (9 curls and 9 bond invariants per "
      "site, weighted by the rates) has static equations solvable iff that law holds, for rates with no flat bond on "
      "L^3, L >= 3; with fields (B, u, kappa) every other linear transport fails for some state, up to the staggered "
      "rate direction Gamma (L >= 5, the step-11 rate condition). Side: on tori with every side even, twofold levels "
      "of H_w carry no bond energy and no current")
print("HIT: the walk's lattice force is demanded exactly by a ledger whose bond field is the moved clock's bond part: "
      "sourced by 2 eps_b, moved by -(1/2)d_j phi (xi_j(x)+xi_j(x+e_j)); a local blind member's static equations are "
      "solvable iff div J[phi psi] = -f; without a bond field no transport of the rates demands f (two-site witness)")
