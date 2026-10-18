#!/usr/bin/env python3
"""Reviewer script rv1 (independent; imports nothing from the author's code).

E1: composite of the Chamon-string circuit prod_r exp(i pi/4 C_r) and the cuboctahedral circuit
prod_r exp(i pi/4 K_r) on one qubit per site of Z^3.  Explicit Pauli conjugation on the infinite
lattice with full Z4 phase tracking.

Pauli encoding: (k, {site: (x, z)}) means i^k * prod_site X^x Z^z  (Y = i X Z).
Conjugation identity used: for Pauli P with P^2 = 1, P Q = -Q P,
    exp(i th P) Q exp(-i th P) = exp(2 i th P) Q  ->  at th = pi/4: i P Q.
Translates of one string commute, so the anticommutation pattern of Q with the family is
unchanged after each factor, and alpha_P(Q) = prod_{r in A(Q)} (i P_r) . Q.

Soldering (C4 convention): beta_R: sigma_a at r -> sum_b Q(R)_{ba} sigma_b at R r;
full: Q = R; axis: Q = s(R)|R| with s the sign of the axis permutation of R.
"""
import itertools
import sys
import time

P_ = F_ = 0


def check(name, ok, extra=''):
    global P_, F_
    if ok:
        P_ += 1
        print('PASS', name, ('::' + extra) if extra else '')
    else:
        F_ += 1
        print('FAIL', name, ('::' + extra) if extra else '')
    sys.stdout.flush()


# ---------------- group O ----------------
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


O = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = [[0] * 3 for _ in range(3)]
        for c in range(3):
            M[perm[c]][c] = sg[c]          # column c -> row perm[c]
        if det3(M) == 1:
            O.append((M, perm))
assert len(O) == 24


def perm_sign(perm):
    s = 1
    p = list(perm)
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s


def Qmat(R, perm, action):
    if action == 'full':
        return R
    if action == 'axis':
        s = perm_sign(perm)
        return [[s * abs(R[i][j]) for j in range(3)] for i in range(3)]
    raise ValueError


def apply_R(R, r):
    return tuple(sum(R[i][j] * r[j] for j in range(3)) for i in range(3))


# ---------------- Pauli arithmetic ----------------
SIG = {0: (0, (1, 0)), 1: (1, (1, 1)), 2: (0, (0, 1))}   # X, Y=iXZ, Z  as (k, (x,z))


def mul(A, B):
    """A*B for Paulis (k, dict)."""
    k = A[0] + B[0]
    d = dict(A[1])
    for s, (c, dd) in B[1].items():
        if s in d:
            a, b = d[s]
            if b and c:
                k += 2
            nx, nz = a ^ c, b ^ dd
            if nx or nz:
                d[s] = (nx, nz)
            else:
                del d[s]
        else:
            d[s] = (c, dd)
    return (k % 4, d)


def lmul_inplace(Pk, Pd, Q):
    """Q <- P*Q in place; returns new phase.  Q = [k, dict]."""
    k = Pk + Q[0]
    d = Q[1]
    for s, (a, b) in Pd.items():
        if s in d:
            c, dd = d[s]
            if b and c:
                k += 2
            nx, nz = a ^ c, b ^ dd
            if nx or nz:
                d[s] = (nx, nz)
            else:
                del d[s]
        else:
            d[s] = (a, b)
    Q[0] = k % 4


def anticomm(Ad, Bd):
    s = 0
    if len(Ad) > len(Bd):
        Ad, Bd = Bd, Ad
    for site, (a, b) in Ad.items():
        if site in Bd:
            c, d = Bd[site]
            s ^= (a & d) ^ (b & c)
    return s


def site_pauli(a, site):
    k, xz = SIG[a]
    return (k, {site: xz})


def make_string(spec):
    """spec: list of (site, a) with a in {0,1,2}; product of Hermitian Paulis."""
    P = (0, {})
    for site, a in spec:
        P = mul(P, site_pauli(a, site))
    return P


def translate(P, t):
    return (P[0], {(s[0] + t[0], s[1] + t[1], s[2] + t[2]): v for s, v in P[1].items()})


def hermitian(P):
    y = sum(1 for v in P[1].values() if v == (1, 1))
    return (P[0] - y) % 2 == 0


def eq(A, B):
    return A[0] % 4 == B[0] % 4 and A[1] == B[1]


def beta(R, perm, action, P):
    Qm = Qmat(R, perm, action)
    img = {}
    for a in range(3):
        col = [Qm[b][a] for b in range(3)]
        b = [i for i in range(3) if col[i] != 0][0]
        img[a] = (col[b], b)              # sigma_a -> sign * sigma_b
    out = (P[0], {})
    for s, (x, z) in P[1].items():
        rs = apply_R(R, s)
        fac = (0, {})
        if x:
            sg, b = img[0]
            sp = site_pauli(b, rs)
            fac = mul(fac, ((sp[0] + (0 if sg == 1 else 2)) % 4, sp[1]))
        if z:
            sg, b = img[2]
            sp = site_pauli(b, rs)
            fac = mul(fac, ((sp[0] + (0 if sg == 1 else 2)) % 4, sp[1]))
        out = mul(out, fac)
    return out


# ---------------- the two strings ----------------
e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
C0 = make_string([((1, 0, 0), 0), ((-1, 0, 0), 0), ((0, 1, 0), 1), ((0, -1, 0), 1),
                  ((0, 0, 1), 2), ((0, 0, -1), 2)])
Kspec = []
for a in range(3):
    for s1 in (1, -1):
        for s2 in (1, -1):
            v = [0, 0, 0]
            others = [i for i in range(3) if i != a]
            v[others[0]] = s1
            v[others[1]] = s2
            Kspec.append((tuple(v), a))
K0 = make_string(Kspec)
assert len(C0[1]) == 6 and len(K0[1]) == 12

check('C_0 and K_0 Hermitian with P^2=1', hermitian(C0) and hermitian(K0)
      and eq(mul(C0, C0), (0, {})) and eq(mul(K0, K0), (0, {})))

ball = lambda rad: list(itertools.product(range(-rad, rad + 1), repeat=3))
for name, P0 in (('C', C0), ('K', K0)):
    ok = all(anticomm(P0[1], translate(P0, t)[1]) == 0 for t in ball(4))
    check(f'string {name}: all translates commute', ok)
    for action in ('axis', 'full'):
        ok = all(eq(beta(R, perm, action, P0), P0) for R, perm in O)
        check(f'string {name}: beta_R(P_0) = +P_0 for all 24 R ({action})', ok)
nac = [t for t in ball(4) if anticomm(C0[1], translate(K0, t)[1])]
check('C_0 anticommutes with exactly 24 translates of K', len(nac) == 24, str(len(nac)))


# ---------------- layers ----------------
def layer(P0, sign=+1):
    """alpha_P(Q) with th = sign*pi/4: anticommuting r contribute factor (sign*i) P_r."""
    offs = list(P0[1].keys())
    Pk = P0[0]
    Pd0 = P0[1]

    def act(Q):
        Qd = Q[1]
        cands = set()
        for s in Qd:
            for o in offs:
                cands.add((s[0] - o[0], s[1] - o[1], s[2] - o[2]))
        A = []
        for r in cands:
            par = 0
            for o, (a, b) in Pd0.items():
                st = (r[0] + o[0], r[1] + o[1], r[2] + o[2])
                v = Qd.get(st)
                if v is not None:
                    par ^= (a & v[1]) ^ (b & v[0])
            if par:
                A.append(r)
        out = [Q[0], dict(Qd)]
        ph = 1 if sign == 1 else 3
        for r in A:
            Pd = {(r[0] + o[0], r[1] + o[1], r[2] + o[2]): v for o, v in Pd0.items()}
            lmul_inplace((Pk + ph) % 4, Pd, out)
        return (out[0], out[1])
    return act


aC, aK = layer(C0), layer(K0)
aCi, aKi = layer(C0, -1), layer(K0, -1)
alpha = lambda Q: aC(aK(Q))          # Ad(U_C U_K)
alpha_inv = lambda Q: aKi(aCi(Q))
alpha2 = lambda Q: aK(aC(Q))         # other order

X0, Z0 = site_pauli(0, (0, 0, 0)), site_pauli(2, (0, 0, 0))
aX, aZ = alpha(X0), alpha(Z0)

# single-layer facts (C4)
for name, lay in (('C', aC), ('K', aK)):
    ok = eq(lay(lay(X0)), X0) and eq(lay(lay(Z0)), Z0)
    rad = max(max(abs(c) for c in s) for s in list(lay(X0)[1]) + list(lay(Z0)[1]))
    check(f'layer {name}: images have Chebyshev radius 2 and alpha^2 = id with phases (C4 [1],[2])',
          ok and rad == 2, f'radius {rad}')

check('composite images Hermitian', hermitian(aX) and hermitian(aZ))
check('alpha(X_0), alpha(Z_0) anticommute', anticomm(aX[1], aZ[1]) == 1)
ok = True
for t in ball(8):
    if t == (0, 0, 0):
        continue
    for A in (aX, aZ):
        for B in (aX, aZ):
            if anticomm(A[1], translate(B, t)[1]):
                ok = False
check('translates of images commute (t in [-8,8]^3 \\ 0): commutation preserved', ok)
check('alpha^{-1} alpha = id on X_0, Z_0 and alpha alpha^{-1} = id (with phases)',
      eq(alpha_inv(aX), X0) and eq(alpha_inv(aZ), Z0)
      and eq(alpha(alpha_inv(X0)), X0) and eq(alpha(alpha_inv(Z0)), Z0))

cheb = lambda P: max(max(abs(c) for c in s) for s in P[1])
rX, rZ = cheb(aX), cheb(aZ)
iX, iZ = alpha_inv(X0), alpha_inv(Z0)
print(f'|supp alpha(X0)| = {len(aX[1])}, |supp alpha(Z0)| = {len(aZ[1])}, radius {rX},{rZ}; '
      f'inverse radius {cheb(iX)},{cheb(iZ)}')
check('composite range 4 (Chebyshev), inverse range 4', max(rX, rZ) == 4 and max(cheb(iX), cheb(iZ)) == 4)
check('|supp alpha(X_0)| = |supp alpha(Z_0)| = 145', len(aX[1]) == 145 and len(aZ[1]) == 145)

# covariance with phases, both orders
for action in ('axis', 'full'):
    for nm, al in (('C.K', alpha), ('K.C', alpha2)):
        ok = True
        for R, perm in O:
            for G in (X0, Z0):
                if not eq(al(beta(R, perm, action, G)), beta(R, perm, action, al(G))):
                    ok = False
        check(f'composite {nm} O-covariant WITH phases, {action} action (24 R, X_0 and Z_0)', ok)

check('alpha_C and alpha_K do not commute as automorphisms', not eq(alpha(X0), alpha2(X0)) or not eq(alpha(Z0), alpha2(Z0)))

# trace polynomial
tau = set()
for s, (x, z) in aX[1].items():
    if x:
        tau ^= {s}
for s, (x, z) in aZ[1].items():
    if z:
        tau ^= {s}
orb = set()
for R, perm in O:
    orb.add(apply_R(R, (4, 2, 0)))
print('tau monomials:', sorted(tau))
check('O-orbit of (4,2,0) has 24 points', len(orb) == 24)
check('tau = O-orbit sum of (4,2,0) (24 monomials, nonconstant)', tau == orb)
check('all tau exponents even', all(c % 2 == 0 for s in tau for c in s))

# iterate alpha^n on X_0 and Z_0; check Chebyshev radius 4n, vertex monomials, Dickson recurrence
def polymul(A, B):
    out = set()
    for a in A:
        for b in B:
            out ^= {(a[0] + b[0], a[1] + b[1], a[2] + b[2])}
    return out


N = 8
QX, QZ = X0, Z0
D_prev, D_cur = set(), set(tau)      # D_0 = 0, D_1 = tau
radX, radZ, sizes = [], [], []
ok_trace = ok_vert = True
t0 = time.time()
for n in range(1, N + 1):
    QX, QZ = alpha(QX), alpha(QZ)
    radX.append(cheb(QX))
    radZ.append(cheb(QZ))
    sizes.append(len(QX[1]))
    trn = set()
    for s, (x, z) in QX[1].items():
        if x:
            trn ^= {s}
    for s, (x, z) in QZ[1].items():
        if z:
            trn ^= {s}
    if n >= 2:
        D_prev, D_cur = D_cur, polymul(tau, D_cur) ^ D_prev
    if trn != D_cur:
        ok_trace = False
    if not all(tuple(n * c for c in v) in trn for v in orb):
        ok_vert = False
    if not (hermitian(QX) and hermitian(QZ)):
        ok_trace = False
    print(f'n={n} |supp a^n X0|={len(QX[1])} |supp a^n Z0|={len(QZ[1])} radius X {radX[-1]} Z {radZ[-1]} '
          f'|tr M^n|={len(trn)}  ({time.time() - t0:.0f}s)')
    sys.stdout.flush()
check('tr(M^n) from iterates = Dickson D_n(tau), n=1..8 (and images stay Hermitian)', ok_trace)
check('all 24 vertex monomials n*v occur in tr(M^n), n=1..8 (Thm 2(c))', ok_vert)
check('Chebyshev radius of alpha^n(X_0) and alpha^n(Z_0) = 4n, n=1..8',
      radX == [4 * n for n in range(1, N + 1)] and radZ == [4 * n for n in range(1, N + 1)],
      f'{radX}')
check('|supp alpha^n(X_0)| = author list', sizes == [145, 633, 2449, 4369, 5921, 12841, 25089, 33697], str(sizes))
print(f'TOTAL: PASS={P_} FAIL={F_}')
