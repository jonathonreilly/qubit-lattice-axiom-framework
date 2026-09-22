#!/usr/bin/env python3
"""J:derive:moving-what-fixes-the-scale:a4 -- exact checks.

Block 39's law with vacancies: a site is empty or carries one record with content s in the six axes (antipode s^1);
a record weighs z (fugacity), two neighbouring records weigh c*omega(s,t) with omega = p, q, r for equal, opposite,
orthogonal contents, and a bond with an empty end weighs 1.  A1 = p+q+4r, c0 = 6/A1.
All arithmetic is exact: sympy for identities in the symbols p, q, r, c, z, x; Fractions for window enumerations.
"""
import sys
from fractions import Fraction as F
from itertools import product
import sympy as sy

OUT = []
FAIL = []


def rec(msg):
    OUT.append(msg)


def need(cond, msg):
    if not cond:
        FAIL.append(msg)


M = 6
p, q, r, c, z, x = sy.symbols("p q r c z x", positive=True)


def omega(s, t, P=p, Q=q, R=r):
    return P if s == t else (Q if s == (t ^ 1) else R)


Om = sy.Matrix(M, M, lambda i, j: omega(i, j))
A1 = p + q + 4 * r
lam2, lam3 = p + q - 2 * r, p - q

# ------------------------------------------------ S1 the spectral table of omega
ones = sy.Matrix([1] * M)
Pu = ones * ones.T / 6
P2 = sy.Matrix(M, M, lambda i, j: sy.Rational(1, 2) * (1 if i // 2 == j // 2 else 0) - sy.Rational(1, 6))
P3 = sy.Matrix(M, M, lambda i, j: (sy.Rational(1, 2) if i == j else (-sy.Rational(1, 2) if i == (j ^ 1) else 0)))
ok = sy.expand(Om - (A1 * Pu + lam2 * P2 + lam3 * P3)) == sy.zeros(M)
ok &= all(sy.expand(Pk * Pk - Pk) == sy.zeros(M) for Pk in (Pu, P2, P3))
ok &= all(sy.expand(Pa * Pb) == sy.zeros(M) for Pa, Pb in ((Pu, P2), (Pu, P3), (P2, P3)))
ok &= (Pu + P2 + P3) == sy.eye(M) and [Pk.trace() for Pk in (Pu, P2, P3)] == [1, 2, 3]
need(ok, "S1 spectral decomposition")
# a2's degree-2 branches in spectral form: at c0, c0^2 (Om^2)_ab / 6 = 1 + 6(lam2^2 P2 + lam3^2 P3)_ab / A1^2
c0 = 6 / A1
ok = True
for (a, b) in ((0, 0), (0, 1), (0, 2)):
    lhs = c0 ** 2 * (Om * Om)[a, b] / 6
    rhs = 1 + 6 * (lam2 ** 2 * P2[a, b] + lam3 ** 2 * P3[a, b]) / A1 ** 2
    ok &= sy.simplify(lhs - rhs) == 0
ok &= sy.expand(12 * r * (p + q + r) - A1 ** 2 + lam2 ** 2) == 0
need(ok, "S1 degree-2 branches")
rec("ok S1 omega = A1*Pu + (p+q-2r)*P2 + (p-q)*P3 (orthogonal projectors of ranks 1, 2, 3; entries by pair class "
    "equal/opposite/orthogonal: Pu 1/6; P2 1/3, 1/3, -1/6; P3 1/2, -1/2, 0); at c0 an averaged record between two "
    "records weighs 1 + (2l2^2+3l3^2)/A1^2, 1 + (2l2^2-3l3^2)/A1^2, 1 - l2^2/A1^2: an orthogonal pair sees only "
    "the l2 = p+q-2r mode: a2's orthogonal branch (l2 = 0) and block 39's RP side condition (l2 >= 0) are "
    "conditions on one eigenvalue")


# ------------------------------- S2 the occupancy marginal: bare coupling c/c0 and scale-free loop factors
def mk(n, edges):
    adj = [[] for _ in range(n)]
    for (u, v) in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def clusters(occ, adj):
    seen, out = set(), []
    for s0 in occ:
        if s0 in seen:
            continue
        comp, stack = [], [s0]
        seen.add(s0)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if v in occ and v not in seen:
                    seen.add(v)
                    stack.append(v)
        out.append(comp)
    return out


_ZC = {}


def content_sum(sites, edges, P, Q, R):
    """Z(omega) of the occupied set: sum over its contents of prod omega over its internal bonds (an integer)"""
    key = (tuple(sorted(sites)), tuple(edges), P, Q, R)
    if key not in _ZC:
        ib = [(u, v) for (u, v) in edges if u in sites and v in sites]
        tot = 0
        for cont in product(range(M), repeat=len(sites)):
            s = dict(zip(sites, cont))
            w = 1
            for (u, v) in ib:
                w *= omega(s[u], s[v], P, Q, R)
            tot += w
        _ZC[key] = tot
    return _ZC[key]


def occ_weights(n, edges, P, Q, R, cc, zz):
    """exact occupancy marginal weights of the law with vacancies: z^k c^b Z(omega) of the occupied set"""
    out = {}
    for occ_t in product((0, 1), repeat=n):
        occ = [i for i in range(n) if occ_t[i]]
        b = sum(1 for (u, v) in edges if occ_t[u] and occ_t[v])
        out[occ_t] = zz ** len(occ) * cc ** b * content_sum(occ, edges, P, Q, R)
    return out


def loop_factor(comp, edges, P, Q, R):
    """L_C = Z_C(omega) * 6^(b-k) / A1^b, the scale-free factor of a cluster (1 on trees)"""
    nb = sum(1 for (u, v) in edges if u in comp and v in comp)
    A = P + Q + 4 * R
    return (F(content_sum(comp, edges, P, Q, R)) * F(6) ** (nb - len(comp)) / F(A) ** nb,
            nb == len(comp) - 1)


WINDOWS = [("path4", 4, [(0, 1), (1, 2), (2, 3)]), ("star4", 4, [(0, 1), (0, 2), (0, 3)]),
           ("comb6", 6, [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5)]), ("2x2", 4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
           ("2x3", 6, [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)])]
TRIPLES = [(3, 1, 2), (5, 2, 4), (7, 3, 5)]
fact_ok = tree_ok = True
Lvals = {}
for (P, Q, R) in TRIPLES:
    A = P + Q + 4 * R
    cz = F(6, A)
    for (cc, zz) in ((cz, F(1, 3)), (2 * cz, F(2, 5)), (cz / 3, F(7, 2))):
        for (nm, n, E) in WINDOWS:
            adj = mk(n, E)
            ow = occ_weights(n, E, P, Q, R, cc, zz)
            for occ_t, w in ow.items():
                occ = set(i for i in range(n) if occ_t[i])
                b = sum(1 for (u, v) in E if occ_t[u] and occ_t[v])
                prod_L = F(1)
                for comp in clusters(occ, adj):
                    L, is_tree = loop_factor(comp, E, P, Q, R)
                    prod_L *= L
                    if is_tree:
                        tree_ok &= L == 1
                    elif cc == cz and zz == F(1, 3):
                        Lvals[(P, Q, R, nm, len(comp))] = L
                fact_ok &= w == (6 * zz) ** len(occ) * (cc / cz) ** b * prod_L
need(fact_ok and tree_ok, "S2 occupancy factorisation")
L4, L6 = Lvals[(3, 1, 2, "2x2", 4)], Lvals[(3, 1, 2, "2x3", 6)]
need(L4 == F(1299, 1296) and L4 == F(20784, 20736), "S2 plaquette loop factor")
ok = True
for (P, Q, R) in TRIPLES:                                  # a single cycle: L = 1 + (2 l2^4 + 3 l3^4) / A1^4
    ok &= Lvals[(P, Q, R, "2x2", 4)] == 1 + F(2 * (P + Q - 2 * R) ** 4 + 3 * (P - Q) ** 4, (P + Q + 4 * R) ** 4)
need(ok, "S2 cycle formula")
rec("ok S2 on path4, star4, comb6, 2x2 and 2x3, at (3,1,2), (5,2,4), (7,3,5) and three (c,z) each, the occupancy "
    "marginal is exactly (6z)^|n| (c/c0)^(occupied bonds) prod_clusters L_C with L_C = Z_C(omega) 6^(b-k)/A1^b "
    "free of c and z; L_C = 1 for every tree cluster; the 4-cycle has L = 1 + (2 l2^4 + 3 l3^4)/A1^4 (plaquette "
    "%s at (3,1,2)); the full 2x3 cluster %s" % (L4, L6))

# S3 consequences at c0: Bernoulli on forests, correlated on cycles, and no scale does better unless p = q = r
P_, Q_, R_ = 3, 1, 2
cz = F(1, 2)
zz = F(1, 3)
bern = True
for (nm, n, E) in WINDOWS[:3]:
    ow = occ_weights(n, E, P_, Q_, R_, cz, zz)
    Zt = sum(ow.values())
    pocc = 6 * zz / (6 * zz + 1)
    bern &= all(w / Zt == pocc ** sum(o) * (1 - pocc) ** (n - sum(o)) for o, w in ow.items())
ow = occ_weights(4, WINDOWS[3][2], P_, Q_, R_, cz, zz)
Zt = sum(ow.values())
p_all = ow[(1, 1, 1, 1)] / Zt
pocc = 6 * zz / (6 * zz + 1)
need(bern and p_all != pocc ** 4 and p_all > pocc ** 4, "S3 Bernoulli on forests only")
rec("ok S3 at c0 = 1/2, z = 1/3, (3,1,2): the occupancy is exactly i.i.d. Bernoulli(6z/(6z+1) = 2/3) on path4, "
    "star4 and comb6, but on the plaquette P(all four occupied) = %s > (2/3)^4: content correlation around a cycle "
    "binds records at every scale; independence on a cycle would need (c/c0)^b L = 1 for the pair (c = c0) and "
    "the cycle (L = 1, i.e. l2 = l3 = 0, i.e. p = q = r)" % p_all)


# ------------------------------------ S4 (e): the length unit -- exact decimation of the chain
# on span{u, e_empty} (u = uniform record) the bond kernel is B = [[x, sqrt6], [sqrt6, 1]], x = c*A1, and the
# site weights are D = diag(z, 1); summing every other site gives B D B; gauge the empty state by g and normalise
s6 = sy.sqrt(6)
B = sy.Matrix([[x, s6], [s6, 1]])
Dz = sy.diag(z, 1)
B2 = B * Dz * B
g = (z * x + 1) / (6 * z + 1)
lamn = (z * x + 1) ** 2 / (6 * z + 1)
B2n = sy.diag(1, g) * B2 * sy.diag(1, g) / lamn
xp = sy.simplify(B2n[0, 0])
ok = sy.simplify(B2n[0, 1] - s6) == 0 and sy.simplify(B2n[1, 1] - 1) == 0
ok &= sy.simplify(xp - 6 - z * (x - 6) ** 2 / (z * x + 1) ** 2) == 0
zp = z * g ** 2
ok &= sy.simplify(zp.subs(x, 6) - z) == 0 and sy.simplify(xp.subs(x, 6) - 6) == 0
ok &= sy.simplify(sy.Matrix([[6, s6], [s6, 1]]) - sy.Matrix([s6, 1]) * sy.Matrix([[s6, 1]])) == sy.zeros(2)
# the full 7-state kernel at (3,1,2) and (5,2,4): decimation by 2 and by 3 keeps c*A1 = 6 and z at c0 only
def K7(P, Q, R, cc):
    K = sy.zeros(7)
    for i in range(M):
        for j in range(M):
            K[i, j] = cc * omega(i, j, P, Q, R)
        K[i, 6] = K[6, i] = 1
    K[6, 6] = 1
    return K


def decimate(K, zz, blocks):
    Dm = sy.diag(*([zz] * M + [1]))
    Kb = K
    for _ in range(blocks - 1):
        Kb = Kb * Dm * K
    a, e = Kb[0, 6], Kb[6, 6]                            # record-empty (constant) and empty-empty entries
    gg = a / e
    lam_ = gg * a
    Kn = sy.diag(*([1] * M + [gg])) * Kb * sy.diag(*([1] * M + [gg])) / lam_
    xn = sum(Kn[0, j] for j in range(M))                  # c'*A1' = row sum of the record-record block
    return sy.nsimplify(xn), sy.nsimplify(zz * gg ** 2), Kn


for (P, Q, R) in ((3, 1, 2), (5, 2, 4)):
    A = P + Q + 4 * R
    for zz in (sy.Rational(1, 3), sy.Rational(5, 2)):
        for blocks in (2, 3):
            xn, zn, Kn = decimate(K7(P, Q, R, sy.Rational(6, A)), zz, blocks)
            ok &= xn == 6 and zn == zz and all(sy.simplify(Kn[i, 6] - 1) == 0 for i in range(7))
            cls = {}                                     # the decimated record block depends on the pair class only
            for i in range(M):
                for j in range(M):
                    cls.setdefault(0 if i == j else (1 if i == (j ^ 1) else 2), set()).add(sy.nsimplify(Kn[i, j]))
            ok &= all(len(v) == 1 for v in cls.values())
            xn1, zn1, _ = decimate(K7(P, Q, R, sy.Rational(12, A)), zz, blocks)
            ok &= xn1 != 12 and zn1 != zz and xn1 > 6
need(ok, "S4 decimation")
rec("ok S4 (e) exact decimation of the chain: on span{uniform record, empty} the kernel is [[x,sqrt6],[sqrt6,1]] "
    "with x = c(p+q+4r); summing every other site and re-normalising gives x' = 6 + z(x-6)^2/(zx+1)^2 and "
    "z' = z((zx+1)/(6z+1))^2, so x = 6 (c = c0) is the only scale and the only fugacity-preserving point that a "
    "change of the length unit leaves fixed (the block is rank one there, so every block size keeps it); every other "
    "scale flows (x' >= 6 after one step, then decreasing); checked on the 7-state kernels at (3,1,2), (5,2,4), "
    "z = 1/3, 5/2, blocks of 2 and 3")

# (b) strict contraction: the chain's transfer matrix D^(1/2) K D^(1/2) at (3,1,2)
lam = sy.symbols("lam")
ok = True
for cc in (sy.Rational(1, 2), sy.Rational(1, 4), 1):
    Kz = K7(3, 1, 2, cc)
    Dh = sy.diag(*([sy.sqrt(sy.Rational(1, 3))] * M + [1]))
    cp = sy.factor((Dh * Kz * Dh).charpoly(lam).as_expr())
    ev = sy.roots(sy.Poly(cp, lam))
    top = max(ev, key=lambda e: sy.N(e))
    rest = [e for e in ev if e != top]
    ok &= all(sy.N(abs(e)) < sy.N(top) for e in rest)
    if cc == sy.Rational(1, 2):
        ok &= set(ev) == {3, 0, sy.Rational(1, 3)} and ev[3] == 1 and ev[sy.Rational(1, 3)] == 3 and ev[0] == 3
need(ok, "S4 contraction")
rec("ok S4 (b) the chain's transfer matrix at (3,1,2), z = 1/3 is a strict contraction off its top state at "
    "c = 1/4, 1/2, 1 alike (Perron-Frobenius); at c0 its spectrum is 3 (top), 1/3 (x3, the l3 mode), 0 (x3: the l2 "
    "mode, which is 0 at (3,1,2), and the empty-record direction): c0 marks where a transfer eigenvalue reaches "
    "0 (block 39's RP threshold), not where contraction starts")

print("\n".join(OUT))
print("SUMMARY: " + ("ROUTE FAILS AT " + FAIL[0] if FAIL else
      "PARTIAL c/c0 is exactly the bare per-bond binding of the occupancy pattern: the occupancy marginal is "
      "(6z)^|n| (c/c0)^b prod L_C with scale-free loop factors that are 1 on trees, so c0 is the unique scale with "
      "no bare binding (Bernoulli occupancy on forests), no scale removes the binding on cycles unless p=q=r, and "
      "c0 is the unique scale left fixed by an exact change of length unit on the chain; the p+q=2r conditions "
      "are one eigenvalue."))
if not FAIL:
    print("HIT: for block 39's law with vacancies the occupancy marginal on any window is exactly "
          "(6z)^|n| (c/c0)^b prod_C L_C, b = occupied bonds, L_C = Z_C(omega) 6^(b_C-k_C)/(p+q+4r)^b_C independent "
          "of c and z and equal to 1 on every tree cluster (an l-cycle: 1 + (2(p+q-2r)^l + 3(p-q)^l)/(p+q+4r)^l); so "
          "c0 is the unique scale with no bare record-record binding, and on a window of Z^d with a cycle (all "
          "cycles even) no scale gives independent occupancy unless p = q = r.")
    print("HIT: candidate (e): on the chain, exact decimation maps x = c(p+q+4r) to 6 + z(x-6)^2/(zx+1)^2 and "
          "z to z((zx+1)/(6z+1))^2, so c0 is the only binding scale (and the only point with invariant fugacity) "
          "that a change of the length unit leaves fixed (the decimated chain stays in the (p,q,r) family); in "
          "d >= 2 the property behind it, independent occupancy, fails at every scale on windows with a plaquette.")
sys.exit(1 if FAIL else 0)
