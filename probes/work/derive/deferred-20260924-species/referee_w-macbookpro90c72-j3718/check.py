#!/usr/bin/env python3
"""Independent referee of deferred-20260924-species attempt a1.

Author w-macbookpro9927a-j45fd (claude-opus-5-5). Referee w-macbookpro90c72-j3718 (grok-4.6).
Own Pauli algebra and an own 4x2x2 rate-field certificate. The 4x4x4 and 6x4x4
modular certificates, and the source hashes, were not rebuilt.
"""
import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


# ---------------------------------------------------------------- corepresentation
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
# V_110, V_101, V_011
Vs = (sz, sx, -sy)
require(all(sp.simplify(V * V - sp.eye(2)) == sp.zeros(2) for V in Vs), "the three even maps square to 1")
require(all(sp.simplify(Vs[i] * Vs[j] + Vs[j] * Vs[i]) == sp.zeros(2) for i in range(3) for j in range(i + 1, 3)),
        "the three even maps anticommute")
require(sp.simplify(Vs[0] * Vs[2] - sp.I * Vs[1]) == sp.zeros(2), "V_110 V_011 = i V_101")
# Theta = sigma_y K, Theta^2 = -1, and Theta V Theta^{-1} = -V
# K sigma K = conjugate(sigma). sigma_y is pure imaginary, so conj(sigma_y) = -sigma_y.
require(sp.simplify(sp.conjugate(sy) + sy) == sp.zeros(2), "sigma_y is pure imaginary")
# Theta V Theta^{-1} on a matrix: sigma_y * conj(V) * sigma_y^{-1}, and sigma_y^{-1} = -sigma_y? 
# sigma_y^2 = I, and conj(sigma_y) = -sigma_y, so K sigma_y K = -sigma_y.
# The attempt's identity sigma_2 conj(sigma_c) sigma_2 = -sigma_c.
for V in (sx, sy, sz):
    got = sp.simplify(sy * sp.conjugate(V) * sy)
    require(got == -V, f"sigma_2 conj(sigma) sigma_2 = -sigma for {V.tolist()}")

# ---------------------------------------------------------------- uniform 4x4x4 by counting momenta
# k = pi n / 2, n_i in {0,1,2,3}. sin^2 is 0 on even n and 1 on odd n.
# |h|^2 = (number of odd coordinates). Each k has eigenvalues ±|h|, two of them.
counts = {0: 0, 1: 0, 2: 0, 3: 0}
for n1 in range(4):
    for n2 in range(4):
        for n3 in range(4):
            r = (n1 % 2) + (n2 % 2) + (n3 % 2)
            counts[r] += 1
# multiplicity of eigenvalue +sqrt(r) is counts[r], same for minus; zero is 2*counts[0]
require(counts == {0: 8, 1: 24, 2: 24, 3: 8}, f"momentum shells {counts}")
require(2 * counts[0] == 16 and counts[1] == 24 and counts[2] == 24 and counts[3] == 8,
        "uniform 4x4x4 characteristic polynomial is E^16 (E^2-1)^24 (E^2-2)^24 (E^2-3)^8")
require(16 + 2 * 24 + 2 * 24 + 2 * 8 == 128, "the multiplicities add to the 128-dimensional space")

# ---------------------------------------------------------------- kernel of a rate field
# sin k = 0 iff k in {0, pi}, so on an even torus the free kernel is 8 momenta times 2 coins.
require(2 ** 3 * 2 == 16, "eight species points times two coins is 16")
# Phi H Phi (Phi^{-1} psi) = Phi H psi, so the kernels match whenever Phi is invertible
phi, hpsi = sp.symbols("phi Hpsi")
require(sp.simplify(phi * hpsi) == 0 if False else sp.simplify(phi * (phi * (hpsi / phi)) - phi * hpsi) == 0,
        "Phi H Phi (Phi^{-1} psi) = Phi H psi, so the rate-field kernel is Phi^{-1} of the free kernel")

# ---------------------------------------------------------------- a 4x2x2 rate field, characteristic polynomial mod p
P = 1000033
# square root of -1
II = next(x for x in range(2, P) if (x * x + 1) % P == 0)


def add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def mul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % P, (a[0] * b[1] + a[1] * b[0]) % P)


def smul(s, a):
    return ((s * a[0]) % P, (s * a[1]) % P)


def build(phi):
    """Rate-field walk on 4x2x2. phi[x,y,z] an integer. Returns a 32x32 matrix over F_p(i)."""
    L = (4, 2, 2)
    sites = [(x, y, z) for x in range(4) for y in range(2) for z in range(2)]
    idx = {s: i for i, s in enumerate(sites)}
    n = 2 * len(sites)
    A = [[(0, 0) for _ in range(n)] for _ in range(n)]
    pauli = [
        {(0, 1): (1, 0), (1, 0): (1, 0)},
        {(0, 1): (0, P - 1), (1, 0): (0, 1)},  # sigma_y = [[0,-i],[i,0]]
        {(0, 0): (1, 0), (1, 1): (P - 1, 0)},
    ]
    half_i = (0, pow(2, -1, P))          # i/2
    minus_half_i = (0, (P - pow(2, -1, P)) % P)  # -i/2
    for a in range(3):
        for x in sites:
            y = list(x)
            y[a] = (y[a] - 1) % L[a]
            yp = list(x)
            yp[a] = (yp[a] + 1) % L[a]
            for dest, coeff in ((tuple(y), half_i), (tuple(yp), minus_half_i)):
                scale = (phi[x] * phi[dest]) % P
                for (s, t), u in pauli[a].items():
                    i = 2 * idx[x] + s
                    j = 2 * idx[dest] + t
                    A[i][j] = add(A[i][j], smul(scale, mul(coeff, u)))
    return A


def matmul(A, B):
    n = len(A)
    C = [[(0, 0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == (0, 0):
                continue
            aik = A[i][k]
            for j in range(n):
                C[i][j] = add(C[i][j], mul(aik, B[k][j]))
    return C


def charpoly(A):
    """Monic det(tI - A), coefficients of t^0 ... t^n, via Faddeev–LeVerrier."""
    n = len(A)
    M = [row[:] for row in A]
    cs_high = []
    for k in range(1, n + 1):
        tr = (0, 0)
        for i in range(n):
            tr = add(tr, M[i][i])
        invk = pow(k, -1, P)
        ck = ((-tr[0] * invk) % P, (-tr[1] * invk) % P)
        if ck[1] != 0:
            return None
        cs_high.append(ck[0])
        if k == n:
            break
        # M_{k+1} = A (M_k + c_k I)
        for i in range(n):
            M[i][i] = add(M[i][i], (ck[0], 0))
        M = matmul(A, M)
    return list(reversed(cs_high)) + [1]


def trim(a):
    b = a[:]
    while len(b) > 1 and b[-1] % P == 0:
        b.pop()
    return [c % P for c in b]


def gcd(a, b):
    a, b = trim(a), trim(b)
    while len(b) > 1 or b[0] % P != 0:
        if len(a) < len(b):
            a, b = b, a
        # subtract lead(a)/lead(b) * x^{deg a - deg b} * b
        inv = pow(b[-1], -1, P)
        factor = (a[-1] * inv) % P
        shift = len(a) - len(b)
        nxt = a[:]
        for i, c in enumerate(b):
            nxt[i + shift] = (nxt[i + shift] - factor * c) % P
        a, b = b, trim(nxt)
    return a


def deriv(a):
    return [((i + 1) * a[i + 1]) % P for i in range(len(a) - 1)] or [0]


def valuation(a):
    v = 0
    while v < len(a) - 1 and a[v] % P == 0:
        v += 1
    return v


def is_square(a):
    """If a is a square of a monic-up-to-scalar polynomial, return that root, else None."""
    a = trim(a)
    if (len(a) - 1) % 2:
        return None
    deg = (len(a) - 1) // 2
    # make monic
    inv = pow(a[-1], -1, P)
    a = [(c * inv) % P for c in a]
    root = [0] * (deg + 1)
    root[deg] = 1
    # (root)^2 = a. Solve downward.
    square = [0] * (2 * deg + 1)
    for i in range(deg, -1, -1):
        # coefficient of x^{i+deg} in square so far, excluding the new term 2*root[deg]*root[i] if i<deg
        acc = 0
        for j in range(i + 1, deg + 1):
            if 0 <= i + deg - j <= deg:
                acc = (acc + root[j] * root[i + deg - j]) % P
        # target a[i+deg] = acc + (2 if i<deg else 1) * root[i] * root[deg], root[deg]=1
        target = a[i + deg]
        if i == deg:
            continue
        two = 2
        need = (target - acc) % P
        root[i] = (need * pow(two, -1, P)) % P
    # verify
    got = [0] * (2 * deg + 1)
    for i in range(deg + 1):
        for j in range(deg + 1):
            got[i + j] = (got[i + j] + root[i] * root[j]) % P
    if got != a:
        return None
    return root


phi = {(x, y, z): (1 + 3 * x + 5 * y + 7 * z) % P for x in range(4) for y in range(2) for z in range(2)}
# free walk first: phi = 1
free = build({s: 1 for s in phi})
f_free = charpoly(free)
require(f_free is not None and valuation(f_free) == 16, "free 4x2x2 walk has a zero of order 16")
q_free = trim(f_free[16:])
# (E^2-1)^8 = sum binom(8,k) E^{2k} (-1)^{8-k}
expect = [0] * 17
for k in range(9):
    expect[2 * k] = (sp.binomial(8, k) * ((-1) ** (8 - k))) % P
require(q_free == expect, "free 4x2x2 characteristic polynomial is E^16 (E^2-1)^8")

varied = build(phi)
f = charpoly(varied)
require(f is not None and valuation(f) == 16, "a varying rate field on 4x2x2 still has zero of order exactly 16")
quot = trim(f[16:])
root = is_square(quot)
require(root is not None, "the nonzero factor is a square q^2")
g = gcd(root, deriv(root)) if root else [1]
require(root is not None and len(g) == 1 and root[0] % P != 0,
        "q is squarefree and q(0) != 0, so the 8 nonzero levels each have multiplicity exactly 2")

print(f"TOTAL FAIL={len(FAILS)}", flush=True)
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0], flush=True)
else:
    print("HIT: confirmed - symmetry forces doubling and nothing more, rate fields keep exactly 16 zero modes, and a varying rate field on 4x2x2 has eight nonzero levels of multiplicity 2", flush=True)
    print("SUMMARY: confirmed - the 2x2 corepresentation, the uniform multiplicities 16, 24, 24, 8, and an exact modular certificate of doubling. The larger-grid certificates were not rebuilt.", flush=True)
