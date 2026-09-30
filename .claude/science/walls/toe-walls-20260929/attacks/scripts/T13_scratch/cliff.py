"""Test 4: which real Clifford algebras (full or even part) are M_2(C)?
Also: Herm(2) has det of signature (1,3) and PSD cone = future light cone.
Convention: e_i^2 = +1 for i < p, -1 for the last q generators.  M_2(C) <=> real dim 8 and
centre = C (a centre element with z^2 = -1), because a real algebra of dim 8 that is semisimple
(all Clifford algebras are) with centre C is central simple over C of complex dim 4.
"""
import itertools
import numpy as np


def blade_mul(a, b, p, q):
    """product of basis blades a,b (bitmasks) -> (sign, blade)."""
    # reordering sign
    s = 1
    x = a >> 1
    while x:
        # number of pairs (i in a, j in b) with i > j
        s *= (-1) ** bin(x & b).count("1")
        x >>= 1
    common = a & b
    n = p + q
    for i in range(n):
        if common >> i & 1 and i >= p:
            s *= -1
    return s, a ^ b


def mul_table(p, q):
    n = p + q
    N = 1 << n
    T = np.zeros((N, N, N))
    for a in range(N):
        for b in range(N):
            s, c = blade_mul(a, b, p, q)
            T[a, b, c] = s
    return T


def mult(T, x, y):
    return np.einsum("a,b,abc->c", x, y, T)


def centre_and_type(p, q, even=False):
    n = p + q
    N = 1 << n
    T = mul_table(p, q)
    idx = [a for a in range(N) if (not even) or bin(a).count("1") % 2 == 0]
    dim = len(idx)
    gens = idx  # commute with every basis blade of the (sub)algebra
    rows = []
    for g in gens:
        eg = np.zeros(N); eg[g] = 1
        # x -> x*g - g*x restricted to subalgebra coordinates
        M = np.zeros((N, dim))
        for k, a in enumerate(idx):
            ea = np.zeros(N); ea[a] = 1
            M[:, k] = mult(T, ea, eg) - mult(T, eg, ea)
        rows.append(M)
    M = np.vstack(rows)
    u, s, vt = np.linalg.svd(M)
    null = vt[(s < 1e-9).sum() * 0 + np.sum(s > 1e-9):]
    cdim = null.shape[0]
    if cdim == 1:
        ctype = "R"
    elif cdim == 2:
        # centre basis: 1 and z; find z orthogonal to identity within centre
        cen = [np.zeros(N) for _ in range(cdim)]
        for r in range(cdim):
            for k, a in enumerate(idx):
                cen[r][a] = null[r, k]
        one = np.zeros(N); one[0] = 1
        # project to remove identity component
        z = None
        for c in cen:
            w = c - c[0] * one
            if np.linalg.norm(w) > 1e-9:
                z = w
        z2 = mult(T, z, z)
        # z2 = a*1 + b*z
        a = z2[0]
        rest = z2 - a * one
        b = 0.0 if np.linalg.norm(rest) < 1e-9 else (rest @ z) / (z @ z)
        disc = b * b + 4 * a
        ctype = "C" if disc < -1e-9 else ("R+R" if disc > 1e-9 else "R[eps]")
    else:
        ctype = f"dim{cdim}"
    return dim, cdim, ctype


def name(dim, cdim, ctype):
    if ctype == "C" and dim == 8:
        return "M_2(C)"
    return f"dim={dim} centre={ctype}"


print("Clifford algebras with real dimension 8 and centre C  (= M_2(C)):")
found = []
for n in range(0, 6):
    for p in range(0, n + 1):
        q = n - p
        for even in (False, True):
            dim, cdim, ctype = centre_and_type(p, q, even)
            if dim == 8 and ctype == "C":
                found.append((n, p, q, "even" if even else "full"))
for f in found:
    print("  n=%d (p,q)=(%d,%d) %s" % f)

pred = {(3, 3, 0, "full"), (3, 1, 2, "full"), (4, 3, 1, "even"), (4, 1, 3, "even")}
print("predicted set  :", sorted(pred))
print("found set      :", sorted(set(found)))
print("MATCH:", set(found) == pred)

# a few explicit rows for the report
for (p, q, even) in [(3, 0, False), (1, 2, False), (2, 1, False), (0, 3, False), (3, 1, True), (1, 3, True), (2, 2, True), (4, 0, True), (0, 4, True), (3, 2, True)]:
    d, c, t = centre_and_type(p, q, even)
    print(f"  Cl{'^0' if even else ''}({p},{q}): dim {d}, centre {t}")

# Herm(2)
sig = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], complex)
s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex)
rng = np.random.default_rng(3)
mis = 0
for _ in range(20000):
    a, b1, b2, b3 = rng.normal(size=4)
    X = a * s0 + b1 * s1 + b2 * s2 + b3 * s3
    ev = np.linalg.eigvalsh(X)
    psd = ev.min() >= 0
    cone = (np.linalg.det(X).real >= 0) and (np.trace(X).real >= 0)
    detq = np.linalg.det(X).real - (a * a - b1 * b1 - b2 * b2 - b3 * b3)
    assert abs(detq) < 1e-9
    if psd != cone:
        mis += 1
print("Herm(2): det = a^2 - |b|^2 (signature (1,3)); PSD vs {det>=0,tr>=0} mismatches:", mis)
