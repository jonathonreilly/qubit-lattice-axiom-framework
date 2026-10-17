"""Brute-force check of the group-cohomology step (claim (c)).
H^2(G; Z2) for G = Z2xZ2 and G = S3 (=D3) by enumerating normalized
2-cocycles modulo coboundaries; test whether the class is determined by the
squares w(g,g) of the involutions, and compute the class of the SU(2)
restriction (w2) on the cubic D2 {1, C2z, C2_(110), C2_(1-10)} and D3."""
import itertools
import numpy as np

def cohomology(elems, mul, inv_list):
    n = len(elems); e = 0
    pairs = [(a, b) for a in range(n) for b in range(n)]
    # cocycle condition w(a,b)+w(ab,c) = w(b,c)+w(a,bc) (mod 2), normalized w(e,.)=w(.,e)=0
    free = [(a, b) for (a, b) in pairs if a != e and b != e]
    cocycles = []
    for bits in itertools.product([0, 1], repeat=len(free)):
        w = {p: 0 for p in pairs}
        for p, v in zip(free, bits): w[p] = v
        if all((w[(a, b)] + w[(mul[a][b], c)] + w[(b, c)] + w[(a, mul[b][c])]) % 2 == 0
               for a in range(n) for b in range(n) for c in range(n)):
            cocycles.append(w)
    cob = set()
    for nu in itertools.product([0, 1], repeat=n - 1):
        nuf = (0,) + nu
        cob.add(tuple((nuf[a] + nuf[b] + nuf[mul[a][b]]) % 2 for (a, b) in pairs))
    classes = {}
    for w in cocycles:
        key = min(tuple((w[p] + c[i]) % 2 for i, p in enumerate(pairs)) for c in cob)
        classes.setdefault(key, w)
    return classes, pairs

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
    classes, pairs = cohomology(G, mul, None)
    invol = [i for i, g in enumerate(G) if i != 0 and mul[i][i] == 0]
    sq = {}
    for k, w in classes.items():
        sq[k] = tuple(w[(i, i)] for i in invol)
    print(name, "| order", len(G), "| #H^2 classes:", len(classes), "| involutions:", len(invol),
          "| squares-pattern determines class:", len(set(sq.values())) == len(classes))
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
