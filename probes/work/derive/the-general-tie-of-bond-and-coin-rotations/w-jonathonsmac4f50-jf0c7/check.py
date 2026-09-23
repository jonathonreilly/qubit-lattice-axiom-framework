#!/usr/bin/env python3
"""the-general-tie-of-bond-and-coin-rotations, attempt 1 (worker w-jonathonsmac4f50-jf0c7, claude-opus-5-5).

(a) exact: the constraint 'T^dagger J = 0 on every stationary state' for local ties T is a linear system whose coefficients lie in
    K = Q(i, sqrt2, sqrt3). Its rank is bounded BELOW by the rank of its image in F_p under a ring homomorphism (p = 1 mod 24, so
    i, sqrt2, sqrt3 exist in F_p): rank_K >= rank_Fp. With an exactly known solution subspace of dimension d, rank_Fp = ncols - d
    closes the solution space exactly. Integer arithmetic mod p throughout.
(b) exact: sympy symbols at leading order in the wave vector (block 64's family is a continuum family).
Step labels refer to ATTEMPT.md.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp
from sympy import isprime
from sympy.ntheory import sqrt_mod

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------- Step 1: the bond current's two-momentum symbol (exact on 4^3)
L = 4
N = L ** 3
sites = list(itertools.product(range(L), repeat=3))
ix = {x: i for i, x in enumerate(sites)}
sg = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def Tm(a):
    M = np.zeros((N, N), complex)
    for x in sites:
        y = tuple((x[i] + (1 if i == a else 0)) % L for i in range(3))
        M[ix[x], ix[y]] = 1
    return M


Tp = [Tm(a) for a in range(3)]
S = [(Tp[a] - Tp[a].conj().T) / 2j for a in range(3)]


def Cdelta(a, x0):
    M = np.zeros((N, N), complex)
    y = tuple((x0[i] + (1 if i == a else 0)) % L for i in range(3))
    M[ix[x0], ix[y]] += 0.5
    M[ix[y], ix[x0]] += 0.5
    return M


def pw(kv):
    return np.array([1j ** sum(kv[i] * x[i] for i in range(3)) for x in sites])


sym_ok = True
x0 = (1, 2, 3)
for (a, j) in ((0, 0), (0, 2), (1, 2), (2, 1)):
    Op = np.kron((Cdelta(a, x0) @ S[j] + S[j] @ Cdelta(a, x0)) / 2, sg[a])
    for kq, kp in (((1, 0, 3), (2, 1, 0)), ((0, 3, 1), (0, 3, 1)), ((3, 3, 2), (1, 0, 2))):
        for s1 in range(2):
            for s2 in range(2):
                u = np.zeros(2); u[s1] = 1
                up = np.zeros(2); up[s2] = 1
                ket = np.kron(pw(kq), u)
                bra = np.kron(pw(kp), up)
                lhs = np.vdot(bra, Op @ ket)
                ek = lambda n: 1j ** n
                sn = lambda n: (ek(n) - ek(-n)) / 2j
                q = [(kq[i] - kp[i]) for i in range(3)]
                rhs = (ek(sum(q[i] * x0[i] for i in range(3)))) * (ek(kq[a]) + ek(-kp[a])) * (sn(kq[j]) + sn(kp[j])) / 4 * (up @ sg[a] @ u)
                sym_ok &= abs(lhs - rhs) == 0
ok("1.1 <k',u'| s_a (1/2){C_a[delta_x], S_j} |k,u> = e^{iq.x} (e^{ik_a} + e^{-ik'_a})(sin k_j + sin k'_j)/4 u'^dag s_a u exactly (4^3 torus, unnormalised plane waves)", sym_ok)

# ---------------------------------------------------------------- Step 2: the linear system for ties, mod p
p = next(q for q in range(1 << 20, 1 << 21) if q % 24 == 1 and isprime(q))
Ii, R2, R3 = sqrt_mod(p - 1, p), sqrt_mod(2, p), sqrt_mod(3, p)
inv = lambda a: pow(int(a) % p, p - 2, p)
z6 = (1 + Ii * R3) * inv(2) % p
ok("2.1 the embedding K -> F_p: i^2 = -1, sqrt2^2 = 2, sqrt3^2 = 3 and zeta6 = (1 + i sqrt3)/2 a primitive sixth root, p = 1 mod 24",
   (Ii * Ii) % p == p - 1 and (R2 * R2) % p == 2 and (R3 * R3) % p == 3 and pow(z6, 6, p) == 1 and pow(z6, 3, p) == p - 1 and p % 24 == 1,
   f"p = {p}")
E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
l1 = lambda v: sum(abs(t) for t in v)
Dl = [[d for d in itertools.product(range(-2, 4), repeat=3) if min(l1(d), l1(tuple(d[i] - E[a][i] for i in range(3)))) <= 1] for a in range(3)]
cols = [(a, j, d) for a in range(3) for j in range(3) for d in Dl[a]]
cidx = {c: i for i, c in enumerate(cols)}
NC = len(cols)
ok("2.2 a tie reads theta at the 12 sites within one step of either end of its bond: 108 unknowns per rotation component b (the system is the same for each b)",
   all(len(x) == 12 for x in Dl) and NC == 108)
SIG = [[[0, 1], [1, 0]], [[0, (p - Ii) % p], [Ii, 0]], [[1, 0], [0, p - 1]]]
ID = [[1, 0], [0, 1]]
mm = lambda A, B: [[(A[i][0] * B[0][j] + A[i][1] * B[1][j]) % p for j in range(2)] for i in range(2)]
madd = lambda A, B: [[(A[i][j] + B[i][j]) % p for j in range(2)] for i in range(2)]
msc = lambda c, A: [[c * A[i][j] % p for j in range(2)] for i in range(2)]


def system(Lt):
    z = Ii if Lt == 4 else z6
    ks = list(itertools.product(range(Lt), repeat=3))
    ep = lambda n: pow(z, n % Lt, p)
    sn = lambda n: (ep(n) - ep(-n)) * inv(2 * Ii) % p
    shell = {}
    for kk in ks:
        cnt = sum(1 for n in kk if (2 * n) % Lt != 0)
        shell.setdefault(cnt, []).append((kk, [sn(n) for n in kk]))
    rows = []
    for cnt, lst in shell.items():
        if cnt == 0:
            branches = [None]  # the eight zeros: the whole coin space
        else:
            r = {1: 1, 2: R2, 3: R3}[cnt] if Lt == 4 else {1: R3 * inv(2) % p, 2: R2 * R3 * inv(2) % p, 3: 3 * inv(2) % p}[cnt]
            branches = [r, (p - r) % p]  # |s| and -|s|: the two eigenvalues of the shell
        for br in branches:
            Pt = {kk: (ID if br is None else madd(msc(br, ID), madd(msc(s[0], SIG[0]), madd(msc(s[1], SIG[1]), msc(s[2], SIG[2])))))
                  for kk, s in lst}
            for (k1, s1), (k2, s2) in itertools.product(lst, lst):
                q = tuple((k2[i] - k1[i]) % Lt for i in range(3))
                row = np.zeros((4, NC), dtype=np.int64)
                Xa = [mm(mm(Pt[k1], SIG[a]), Pt[k2]) for a in range(3)]
                for c, (a, j, d) in enumerate(cols):
                    f = pow(z, (-sum(q[i] * d[i] for i in range(3))) % Lt, p) * ((ep(k2[a]) + ep(-k1[a])) % p) % p * ((s2[j] + s1[j]) % p) % p
                    for e, (i1, i2) in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
                        row[e, c] = f * Xa[a][i1][i2] % p
                rows.append(row)
    return np.concatenate(rows)


def modrank(A):
    basis, piv = [], []
    A = A % p
    for s0 in range(0, A.shape[0], 4000):
        Cm = A[s0:s0 + 4000].copy()
        for b, pc in zip(basis, piv):
            Cm = (Cm - np.outer(Cm[:, pc], b)) % p
        for col in range(Cm.shape[1]):
            if col in piv:
                continue
            nz = np.nonzero(Cm[:, col])[0]
            if len(nz) == 0:
                continue
            r = Cm[nz[0]].copy() * inv(Cm[nz[0], col]) % p
            for i in range(len(basis)):
                if basis[i][col]:
                    basis[i] = (basis[i] - basis[i][col] * r) % p
            Cm = (Cm - np.outer(Cm[:, col], r)) % p
            basis.append(r)
            piv.append(col)
    return len(basis)


A4 = system(4)
A6 = system(6)
r4, r6 = modrank(A4), modrank(A6)
rb = modrank(np.concatenate([A4, A6]))
print(f"rows: 4^3 {A4.shape[0]}, 6^3 {A6.shape[0]}; ranks mod p: {r4}, {r6}, together {rb}")
# relabelling ties: B_a^j(x) = xi_j(x + e_a) - xi_j(x), xi_j = sum_{d' in star} m_j(d') theta_b(x + d')
star = [(0, 0, 0)] + [tuple(s * E[a][i] for i in range(3)) for a in range(3) for s in (1, -1)]
rel = []
for j0 in range(3):
    for dp in star:
        t = np.zeros(NC, dtype=np.int64)
        for a in range(3):
            t[cidx[(a, j0, tuple(E[a][i] + dp[i] for i in range(3)))]] += 1
            t[cidx[(a, j0, dp)]] -= 1
        rel.append(t % p)
rel = np.array(rel)
relrank = sp.Matrix([[int(v) if v < p // 2 else int(v) - p for v in row] for row in rel]).rank()
ok("2.3 the relabelling ties B = d(M theta), M reading theta on the 7-point star, form a 21-dimensional space of ties inside the 12-site reach",
   relrank == 21)
ok("2.4 every relabelling tie satisfies all constraints (mod p check of the theorem: T^dagger J = -M^dagger div J = 0 on stationary states, block 63)",
   int(np.count_nonzero((np.concatenate([A4, A6]) @ rel.T) % p)) == 0)
ok("2.5 on the 6^3 torus the constraint matrix has rank 87 mod p, so over K the ties form a space of dimension at most 108 - 87 = 21: exactly the relabelling ties",
   r6 == 87 and rb == 87)
ok("2.6 the 4^3 torus alone admits 27 (offsets 2 and -2 are one site there): six more per b, torus artefacts removed by the 6^3 torus", r4 == 81)


def eps(a, b, c):
    return int(round(np.linalg.det(np.eye(3)[[a, b, c]])))


viol = []
for b in range(3):
    t = np.zeros(NC, dtype=np.int64)
    for a in range(3):
        for j in range(3):
            if eps(a, b, j):
                t[cidx[(a, j, (0, 0, 0))]] += eps(a, b, j)
    viol.append(int(np.count_nonzero((A6 @ (t % p)) % p)))
ok("2.7 the forward-bond tie B_a^j(x) = eps_abj theta_b(x) (issue #8659) violates the constraints on the 6^3 torus", all(v > 0 for v in viol), f"violated rows {viol}")
print(f"exact part (a) done in {time.time() - T0:.1f} s")

# ---------------------------------------------------------------- Step 3 (b): the family that sees bond rotations
k = sp.symbols("k1:4", real=True)


def quadT(B, kv):
    Tt = {(j, a, b): sp.I * (kv[a] * B[b, j] - kv[b] * B[a, j]) for j in range(3) for a in range(3) for b in range(3)}
    cj = sp.conjugate
    T1 = sum(Tt[(j, a, b)] * cj(Tt[(j, a, b)]) for j in range(3) for a in range(3) for b in range(3))
    T2 = sum(Tt[(j, a, b)] * cj(Tt[(b, a, j)]) for j in range(3) for a in range(3) for b in range(3))
    V = [sum(Tt[(a, a, b)] for a in range(3)) for b in range(3)]
    T3 = sum(V[b] * cj(V[b]) for b in range(3))
    return [sp.expand(sp.re(sp.expand(zz))) for zz in (T1, T2, T3)]


c1, c2, c3 = sp.symbols("c1 c2 c3", real=True)
Sr = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"s{min(i, j)}{max(i, j)}", real=True))
al = sp.Matrix(sp.symbols("al1:4", real=True))
Aa = sp.Matrix(3, 3, lambda a, j: sum(sp.LeviCivita(a, j, b) * al[b] for b in range(3)))
fam = lambda q: c1 * q[0] + c2 * q[1] + c3 * q[2]
dA = sp.expand(fam(quadT(Sr + Aa, k)) - fam(quadT(Sr, k)))
sol = sp.solve(sp.Poly(dA, *k, *al, *list(set(Sr))).coeffs(), [c1, c2, c3], dict=True)
ok("3.1 the quadratic density is independent of the antisymmetric strain (bond rotations) iff (c1, c2, c3) is proportional to (1, 2, -4): block 64's blind ratio; every other member sees bond rotations",
   sol == [{c1: -c3 / 4, c2: -c3 / 2}])
kap = sp.symbols("kappa", positive=True)
xs = sp.symbols("x1:7", real=True)
Bt = sp.zeros(3, 3)
Bt[0, 0], Bt[0, 1], Bt[0, 2], Bt[1, 0], Bt[1, 1], Bt[1, 2] = xs  # bonds transverse to k = kappa e_3; B_3^j is a relabelling
M6 = sp.hessian(fam(quadT(Bt, (0, 0, kap))), xs) / 2
cp = sp.factor(M6.charpoly(sp.Symbol("lam")).as_expr())
lam = sp.Symbol("lam")
target = (lam - kap ** 2 * (2 * c1 - c2)) * (lam - kap ** 2 * (2 * c1 + c2)) ** 2 * (lam - kap ** 2 * (2 * c1 + c2 + c3)) ** 2 * (lam - kap ** 2 * (2 * c1 + c2 + 2 * c3))
ok("3.2 off the relabellings the static form has eigenvalues kappa^2 x {2c1 - c2, 2c1 + c2 (twice), 2c1 + c2 + c3 (twice), 2c1 + c2 + 2c3}: static equations solvable for every source iff all four are non-zero",
   sp.expand(cp - target) == 0)
ok("3.3 at the blind ratio the form has rank 3: two of the four factors vanish (2c1 - c2 and 2c1 + c2 + c3), so the blind member cannot balance a bond torque",
   M6.subs({c1: -c3 / 4, c2: -c3 / 2}).rank() == 3)
c4 = sp.symbols("c4", real=True)
beta = c4 / (4 * c1 + 2 * c2 + 4 * c3)
ok("3.4 block 64 T4's exponent beta = c4/(4c1 + 2c2 + 4c3) = c4/(2(2c1 + c2 + 2c3)): finite exactly when the last factor is non-zero; beta = 1 is the hyperplane c4 = 2(2c1 + c2 + 2c3), not forced",
   sp.simplify(beta - c4 / (2 * (2 * c1 + c2 + 2 * c3))) == 0 and sp.solve(sp.Eq(beta, 1), c4) == [4 * c1 + 2 * c2 + 4 * c3])

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL (a) decided exactly: every local tie of the three site rotations to the nine bond strains that reads theta within one step "
      "of its bond's ends and has T^dagger J = 0 on every stationary state of the 6^3 torus is a relabelling tie B = d(M theta) (dimension 21 per "
      "component, rank 87 of 108 mod p against 21 exact solutions), which makes the tied rotation pure gauge: the nine-plus-three variables are forced "
      "at this reach. (b) the field energies for nine-plus-three: block 64's family with c0 = 0, five numbers (c1..c5); it sees bond rotations iff "
      "(c1, c2, c3) is not along (1, 2, -4); its static equations are solvable for every source iff (2c1 - c2)(2c1 + c2)(2c1 + c2 + c3)(2c1 + c2 + 2c3) "
      "!= 0; beta = c4/(2(2c1 + c2 + 2c3)) is free, beta = 1 a hyperplane")
print("HIT: (a) decided exactly at reach one step from the bond's ends: the only ties with T^dagger J = 0 on every stationary state of the 6^3 torus "
      "are relabellings B = d(M theta) (21 per component), so the nine-plus-three variables are forced; (b) the nine-plus-three field energies: "
      "block 64's family off the blind ratio, solvable iff (2c1 - c2)(2c1 + c2)(2c1 + c2 + c3)(2c1 + c2 + 2c3) != 0, with beta = c4/(2(2c1 + c2 + 2c3)) free")
