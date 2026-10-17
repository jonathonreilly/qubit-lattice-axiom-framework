"""Brute-force check of the group-cohomology step (claim (c)).
H^2(G; Z2) for G = Z2xZ2 and G = S3 (=D3) by enumerating normalized
2-cocycles modulo coboundaries; test whether the class is determined by the
squares w(g,g) of the involutions, and compute the class of the SU(2)
restriction (w2) on the cubic D2 {1, C2z, C2_(110), C2_(1-10)} and D3."""
import itertools
import numpy as np

def rank2(vecs):
    piv = {}
    for v in vecs:
        while v:
            h = v.bit_length() - 1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; break
    return len(piv)

def nullspace2(rows, ncols):
    piv = {}
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h in piv: r ^= piv[h]
            else: piv[h] = r; break
    keys = sorted(piv)
    for k in keys:
        for k2 in keys:
            if k2 != k and (piv[k2] >> k) & 1: piv[k2] ^= piv[k]
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = 1 << f
        for k in keys:
            if (piv[k] >> f) & 1: v |= 1 << k
        basis.append(v)
    return basis

def cohomology(elems, mul, _):
    """Linear algebra over GF(2). Returns (dim H^2, cocycle basis, coboundary
    basis, pair index)."""
    n = len(elems)
    pairs = [(a, b) for a in range(1, n) for b in range(1, n)]
    pid = {p: i for i, p in enumerate(pairs)}
    def bit(a, b):
        return 0 if a == 0 or b == 0 else 1 << pid[(a, b)]
    rows = []
    for a in range(n):
        for b in range(n):
            for c in range(n):
                r = bit(a, b) ^ bit(mul[a][b], c) ^ bit(b, c) ^ bit(a, mul[b][c])
                if r: rows.append(r)
    Z = nullspace2(rows, len(pairs))
    Bv = []
    for g in range(1, n):
        v = 0
        for (a, b) in pairs:
            if (a == g) ^ (b == g) ^ (mul[a][b] == g):
                v |= 1 << pid[(a, b)]
        Bv.append(v)
    dimB = rank2(Bv)
    return len(Z) - dimB, Z, Bv, pid

def mats_group(gens):
    G = [np.eye(3, dtype=int)]
    changed = True
    while changed:
        changed = False
        for A in list(G):
            for g in gens:
                B = A @ g
                if not any((B == C).all() for C in G):
                    G.append(B); changed = True
    return G

def table(G):
    idx = lambda M: [i for i, C in enumerate(G) if (C == M).all()][0]
    return [[idx(A @ B) for B in G] for A in G]

C2z = np.diag([-1, -1, 1]); C2a = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]); C2b = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])
C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]); C2d = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]])  # C2 about (1,-1,0) is perpendicular to (1,1,1)
for name, gens in (("D2 (axis C2z + edge C2 (110), (1-10))", [C2z, C2a]), ("D3 (C3 about (111) + edge C2 (1-10))", [C3, C2d])):
    G = mats_group(gens); mul = table(G)
    dimH, Z, Bv, pid = cohomology(G, mul, None)
    pairs = [(a, b) for a in range(len(G)) for b in range(len(G))]
    invol = [i for i, g in enumerate(G) if i != 0 and mul[i][i] == 0]
    # square map on cocycles; injective on H^2 iff  dim(span(B + kernel of sq on Z)) == dim B
    def sq(w): return tuple((w >> pid[(i, i)]) & 1 for i in invol)
    # kernel of sq restricted to Z: brute force over Z (dim small)
    kerZ = []
    for bits in itertools.product([0, 1], repeat=len(Z)):
        w = 0
        for z, b in zip(Z, bits):
            if b: w ^= z
        if not any(sq(w)): kerZ.append(w)
    injective = rank2(Bv + kerZ) == rank2(Bv)
    print(name, "| order", len(G), "| dim H^2(G;Z2) =", dimH, "| involutions:", len(invol),
          "| class determined by squares of involutions:", injective)
    # SU(2) restriction: lift each rotation to SU(2); cocycle w(a,b) from lift(a)lift(b) = (-1)^w lift(ab)
    def su2(R):
        # quaternion from rotation matrix (one of +-)
        tr = np.trace(R)
        w = np.sqrt(max(0, 1 + tr)) / 2
        if w > 1e-9:
            x = (R[2, 1] - R[1, 2]) / (4 * w); y = (R[0, 2] - R[2, 0]) / (4 * w); z = (R[1, 0] - R[0, 1]) / (4 * w)
        else:
            x = np.sqrt(max(0, (1 + R[0, 0] - R[1, 1] - R[2, 2]))) / 2
            y = np.sqrt(max(0, (1 - R[0, 0] + R[1, 1] - R[2, 2]))) / 2
            z = np.sqrt(max(0, (1 - R[0, 0] - R[1, 1] + R[2, 2]))) / 2
            # fix relative signs
            if x > 1e-9: y = np.copysign(y, R[0, 1] + R[1, 0]); z = np.copysign(z, R[0, 2] + R[2, 0])
            elif y > 1e-9: z = np.copysign(z, R[1, 2] + R[2, 1])
        q = np.array([w, x, y, z])
        I2 = np.eye(2); sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
        return q[0] * I2 - 1j * (q[1] * sx + q[2] * sy + q[3] * sz)
    lifts = [su2(g) for g in G]
    w2 = {}
    for (a, b) in pairs:
        P = lifts[a] @ lifts[b]; Q = lifts[mul[a][b]]
        w2[(a, b)] = 0 if np.allclose(P, Q) else (1 if np.allclose(P, -Q) else None)
    assert None not in w2.values()
    print("   w2 restricted: squares of involution lifts =", [(-1) ** w2[(i, i)] for i in invol],
          "| nontrivial class:", any(w2[(i, i)] for i in invol))
