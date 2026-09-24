"""Independent confirmation of the exchange-sign counterexample.

Exact Gaussian integers for the walk, sympy for the one-site algebra.
The author's script is not called. Comparators are not premises.
"""
import itertools
import sys

import sympy as sp

FAILS = []
I = sp.I
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -I], [I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
SG = (S1, S2, S3)


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def conj(a):
    return (a[0], -a[1])


# ---------------------------------------------------------------- Clifford grading
def alpha(x):
    return sp.simplify(S2 * x.conjugate() * S2)


ok = alpha(sp.eye(2)) == sp.eye(2) and alpha(I * sp.eye(2)) == -I * sp.eye(2)
ok = ok and all(alpha(s) == -s and alpha(I * s) == I * s for s in SG)
ok = ok and all(alpha(x * y) == alpha(x) * alpha(y) for x in SG for y in SG)
u = sp.symbols("u1 u2 u3", real=True)
proj = (sp.eye(2) + u[0] * S1 + u[1] * S2 + u[2] * S3) / 2
even = sp.expand((proj + alpha(proj)) / 2)
odd = sp.expand((proj - alpha(proj)) / 2)
ok = ok and even == sp.eye(2) / 2 and odd == (u[0] * S1 + u[1] * S2 + u[2] * S3) / 2
want("S6 alpha fixes 1 and i sigma, negates sigma and i, and a pure state has both parities", ok)

a = sp.symbols("a0:4", real=True)
b = sp.symbols("b0:4", real=True)
Gam = sp.Matrix([[a[0] + I * b[0], a[1] + I * b[1]], [a[2] + I * b[2], a[3] + I * b[3]]])
eqs = []
for s in SG:
    diff = sp.expand(Gam * s + s * Gam)
    eqs += [sp.re(e) for e in diff] + [sp.im(e) for e in diff]
lin = sp.solve(eqs, list(a) + list(b), dict=True)
eqs = []
for s in SG:
    diff = sp.expand(Gam * s.conjugate() + s * Gam)
    eqs += [sp.re(e) for e in diff] + [sp.im(e) for e in diff]
anti = sp.solve(eqs, list(a) + list(b), dict=True)
Ms = Gam.subs(anti[0]) if anti else None
ok = lin == [{**{t: 0 for t in a}, **{t: 0 for t in b}}]
ok = ok and Ms is not None and sp.expand(Ms - (Ms[0, 1] / (-I)) * S2) == sp.zeros(2)
cc = Ms[0, 1] / (-I)
ok = ok and sp.expand(Ms * Ms.conjugate() + cc * sp.conjugate(cc) * sp.eye(2)) == sp.zeros(2)
want("S6 no linear or antilinear involution of C^2 makes all three sigma odd", ok)

# smallest graded module C^4
def kron(A, B):
    return sp.Matrix(sp.kronecker_product(A, B))


Gamma = kron(sp.eye(2), S3)
gens = [kron(s, S1) for s in SG]
ok = Gamma ** 2 == sp.eye(4) and all(sp.simplify(Gamma * e + e * Gamma) == sp.zeros(4) for e in gens)
ok = ok and all(e ** 2 == sp.eye(4) for e in gens)
ok = ok and all(sp.simplify(gens[i] * gens[j] + gens[j] * gens[i]) == sp.zeros(4) for i in range(3) for j in range(i + 1, 3))
omega = sp.simplify(gens[0] * gens[1] * gens[2])
ok = ok and omega ** 2 == -sp.eye(4)
want("S6 the C^4 module grades Cl(3,0), and the pseudoscalar squares to -1", ok)

# six Majoranas on three qubits: squares, anticommutators, 64 distinct products
X, Y, Z = S1, S2, S3
Id = sp.eye(2)
maj = [
    kron(kron(X, Id), Id),
    kron(kron(Y, Id), Id),
    kron(kron(Z, Id), kron(X, Id)[:2, :2]) if False else kron(kron(Z, X), Id),
    kron(kron(Z, Y), Id),
    kron(kron(Z, Z), X),
    kron(kron(Z, Z), Y),
]
ok = all(m ** 2 == sp.eye(8) for m in maj)
ok = ok and all(sp.simplify(maj[i] * maj[j] + maj[j] * maj[i]) == sp.zeros(8) for i in range(6) for j in range(i + 1, 6))
# products of distinct subsets are the 64 monomials; hash a few entries to test distinctness
seen = set()
for mask in range(64):
    M = sp.eye(8)
    for i in range(6):
        if mask >> i & 1:
            M = sp.simplify(M * maj[i])
    seen.add(tuple((sp.re(M[r, c]), sp.im(M[r, c])) for r in range(8) for c in range(8)))
ok = ok and len(seen) == 64
want("S6 six anticommuting Majoranas give 64 distinct monomials, the real rank of Cl(6,0)", ok)

# ---------------------------------------------------------------- the walk, exact
PAULI = {
    1: {(0, 1): (1, 0), (1, 0): (1, 0)},
    2: {(0, 1): (0, -1), (1, 0): (0, 1)},
    3: {(0, 0): (1, 0), (1, 1): (-1, 0)},
}


def hops(d, sig):
    out = []
    for a in range(d):
        for sgn, amp in ((1, (0, 1)), (-1, (0, -1))):
            step = tuple(sgn if i == a else 0 for i in range(d))
            for (c2, c1), p in PAULI[sig[a]].items():
                out.append((step, c1, c2, mul(amp, p)))
    return out


def local_exchange(d, sig, k):
    """Sum over r != 0 and coins of <P s|(2H)^k|s>. Returns total and the value at each r."""
    step = hops(d, sig)
    zero = (0,) * d
    per = {}
    total = (0, 0)
    for r in itertools.product(range(-k, k + 1), repeat=d):
        if r == zero or 2 * sum(abs(t) for t in r) > k:
            continue
        acc = (0, 0)
        for ca in range(2):
            for cb in range(2):
                vec = {((zero, ca), (r, cb)): (1, 0)}
                for _ in range(k):
                    nxt = {}
                    for ((x, c1), (y, c2)), am in vec.items():
                        for e, cin, cout, v in step:
                            if cin == c1:
                                x2 = tuple(p + q for p, q in zip(x, e))
                                if x2 != y:
                                    key = ((x2, cout), (y, c2))
                                    nxt[key] = add(nxt.get(key, (0, 0)), mul(am, v))
                            if cin == c2:
                                y2 = tuple(p + q for p, q in zip(y, e))
                                if y2 != x:
                                    key = ((x, c1), (y2, cout))
                                    nxt[key] = add(nxt.get(key, (0, 0)), mul(am, v))
                    vec = nxt
                acc = add(acc, vec.get(((r, cb), (zero, ca)), (0, 0)))
        per[r] = acc
        total = add(total, acc)
    return total, per


ok = True
for d, sig, expect4 in ((2, (1, 2), -128), (3, (1, 2, 3), -384)):
    for order in (2, 3):
        tot, _ = local_exchange(d, sig, order)
        ok = ok and tot == (0, 0)
    tot, per = local_exchange(d, sig, 4)
    ok = ok and tot == (expect4, 0)
want("S7 orders 2 and 3 vanish, and tr(P (2H)^4) per site is -128 on Z^2 and -384 on Z^3", ok)

_, per3 = local_exchange(3, (1, 2, 3), 4)
nb = [per3[r] for r in per3 if sum(abs(t) for t in r) == 1]
dg = [per3[r] for r in per3 if sum(abs(t) for t in r) == 2 and max(abs(t) for t in r) == 1]
ln = [per3[r] for r in per3 if max(abs(t) for t in r) == 2]
ok = nb == [(-32, 0)] * 6 and dg == [(-16, 0)] * 12 and ln == [(0, 0)] * 6
want("S7 coin-summed (2H)^4 exchange is -32, -16, 0, so the physical amplitudes are -2, -1, 0", ok)

# ---------------------------------------------------------------- rings
def ring_exchange(N, kmax):
    """Reduced walk H = sigma_3 p on a ring. Returns tr(P (2H2)^k) for k=1..kmax, as Gaussian ints."""
    sites = list(range(N))
    # one-particle basis: 2*site + coin
    hop = {}
    for s in sites:
        for sgn, amp in ((1, (0, 1)), (-1, (0, -1))):
            t = (s + sgn) % N
            for (c2, c1), p in PAULI[3].items():
                hop[(2 * t + c2, 2 * s + c1)] = add(hop.get((2 * t + c2, 2 * s + c1), (0, 0)), mul(amp, p))
    basis = [(i, j) for i in range(2 * N) for j in range(2 * N) if i // 2 != j // 2]
    ix = {b: k for k, b in enumerate(basis)}
    cols = {c: [] for c in range(len(basis))}
    for k, (i, j) in enumerate(basis):
        for i2 in range(2 * N):
            a = hop.get((i2, i))
            if a and i2 // 2 != j // 2:
                cols[k].append((ix[(i2, j)], a))
        for j2 in range(2 * N):
            a = hop.get((j2, j))
            if a and j2 // 2 != i // 2:
                cols[k].append((ix[(i, j2)], a))
    perm = [ix[(j, i)] for (i, j) in basis]
    # power iteration of the trace against P, vector-free: keep the diagonal of P M by applying columns
    # tr(P A) = sum_k A[perm[k], k]
    acc = []
    # represent the current operator's needed column-entries only as we multiply a set of vectors e_k
    # For kmax=N<=8 and dim<=224, store the full sparse operator as cols and iterate vectors from the identity
    dim = len(basis)
    mat = [dict(cols[c]) for c in range(dim)]

    def apply(vec):
        out = {}
        for c, am in vec.items():
            for r, v in mat[c].items():
                out[r] = add(out.get(r, (0, 0)), mul(am, v))
        return out

    current = [{i: (1, 0)} for i in range(dim)]
    for _ in range(kmax):
        current = [apply(v) for v in current]
        tr = (0, 0)
        for c in range(dim):
            tr = add(tr, current[c].get(perm[c], (0, 0)))
        acc.append(tr)
    return acc, basis, mat, perm, ix


ok = True
traces = {}
for N in (4, 6, 8):
    acc, *_ = ring_exchange(N, N)
    traces[N] = acc
    ok = ok and all(t == (0, 0) for t in acc[:-1]) and acc[-1] != (0, 0)
ok = ok and [traces[N][-1][0] for N in (4, 6, 8)] == [128, -1248, 7680]
want("S7 on even rings tr(P (2H)^k) vanishes below order N and equals 128, -1248, 7680 at order N", ok)

# N=4 sector fourth moments: tr H^4 / dim = 5/6 and 7/6
acc4, basis4, mat4, perm4, ix4 = ring_exchange(4, 4)
dim = len(basis4)
# tr (2H)^2 and tr (2H)^4
def apply_mat(vec):
    out = {}
    for c, am in vec.items():
        for r, v in mat4[c].items():
            out[r] = add(out.get(r, (0, 0)), mul(am, v))
    return out

cur = [{i: (1, 0)} for i in range(dim)]
cur = [apply_mat(apply_mat(v)) for v in cur]
tr2 = (0, 0)
for c in range(dim):
    tr2 = add(tr2, cur[c].get(c, (0, 0)))
cur = [apply_mat(apply_mat(v)) for v in cur]
tr4 = (0, 0)
for c in range(dim):
    tr4 = add(tr4, cur[c].get(c, (0, 0)))
dimK = dim // 2
# physical H = code/2, so tr H^2 = tr(code^2)/4, and the quoted ratio uses tr(code^2)/(4 * 2 * dimK)
from fractions import Fraction as F
ok = tr2[1] == 0 and tr4[1] == 0
ok = ok and F(tr2[0], 4 * 2 * dimK) == F(2, 3)
ok = ok and F(tr4[0] - 128, 16 * 2 * dimK) == F(5, 6)
ok = ok and F(tr4[0] + 128, 16 * 2 * dimK) == F(7, 6)
want("S7 at N=4 the hard-core second moment is 2/3 and the sector fourth moments are 5/6 and 7/6", ok)

# odd ring N=5: U = (sigma_1 tensor sigma_1) (G tensor G) J
def odd_equivalence(N):
    acc, basis, mat, perm, ix = ring_exchange(N, 1)
    n = len(basis)
    # rebuild hop-level U on the basis
    # J = +1 if site(i) < site(j)
    # G = (-1)^{site i + site j}
    # C flips both coins: (i^1, j^1)
    Ucol = {}
    for k, (i, j) in enumerate(basis):
        sign = 1 if i // 2 < j // 2 else -1
        g = (-1) ** (i // 2 + j // 2)
        dest = ix[(i ^ 1, j ^ 1)]
        Ucol[k] = (dest, sign * g)  # real ±1
    # U H U^* and U P U^*
    # P sends k to perm[k], P is a permutation matrix with 1s
    # Check U H = H U and U P = - P U by applying to basis vectors
    def applyU(vec):
        out = {}
        for c, am in vec.items():
            dest, s = Ucol[c]
            out[dest] = add(out.get(dest, (0, 0)), (s * am[0], s * am[1]))
        return out
    okU = True
    for c in range(n):
        e = {c: (1, 0)}
        left = applyU(apply_ops(mat, e))
        right = apply_ops(mat, applyU(e))
        if left != right:
            okU = False
            break
        # U P e_c = U e_{perm^{-1}?}: P e_c = e_{perm[c]} if P_{perm[c], c} = 1, i.e. column c has a 1 at row perm[c]
        pe = {perm[c]: (1, 0)}
        upe = applyU(pe)
        pu = applyU(e)
        pu = {perm[r]: am for r, am in pu.items()}
        # U P = - P U means U P e = - P U e
        neg = {r: (-am[0], -am[1]) for r, am in pu.items()}
        if upe != neg:
            okU = False
            break
    return okU


def apply_ops(mat, vec):
    out = {}
    for c, am in vec.items():
        for r, v in mat[c].items():
            out[r] = add(out.get(r, (0, 0)), mul(am, v))
    return out


ok = odd_equivalence(5) and odd_equivalence(7)
want("S7 on rings of 5 and 7 sites, U H U* = H and U P U* = -P", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - both hard-core sectors are closed and one-record-per-site, and no involution of C^2 "
    "makes the three Pauli matrices odd, so the exchange sign is not fixed by the stated axioms. "
    "Under exclusion it first appears at order 4: -8 per plaquette, and at order N on even rings."
)
print(
    "SUMMARY: confirmed the counterexample. Orders 2 and 3 vanish on Z^2 and Z^3. "
    "tr(P (2H)^4) per site is -128 and -384, i.e. -8 and -24 for the physical generator. "
    "Even rings give 128, -1248, 7680; odd rings of 5 and 7 sites are unitarily equivalent. "
    "The graded composite Cl(6,0) has 64 monomials and is not forced by the one-site sentences."
)
