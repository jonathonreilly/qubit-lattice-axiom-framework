"""T49 Part A: which fermion bilinears does axiom covariance allow?

Model (see PREREG.md): one mode per coarse vertex of an L^3 torus, KS pi-flux
hopping, group = translations + 24 proper cubic rotations acting as real signed
permutations c_v -> s(v) c_{g v}.  For every displacement class D count the
independent real invariants of a pairing form (antisymmetric) and of a hopping
form (symmetric, control).
"""
import itertools, sys
import numpy as np

L = int(sys.argv[1]) if len(sys.argv) > 1 else 8
RMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 3  # need 2*RMAX < L so d and -d stay distinct
N = L ** 3


def idx(x, y, z):
    return ((x % L) * L + (y % L)) * L + (z % L)


def coords(i):
    return (i // (L * L), (i // L) % L, i % L)


def eta(a, v):
    x, y, z = v
    if a == 0:
        return 1
    if a == 1:
        return -1 if x % 2 else 1
    return -1 if (x + y) % 2 else 1


# hopping signs on NN bonds: h[(i,j)] = eta_a(v) for j = i + e_a
hop = {}
for i in range(N):
    v = coords(i)
    for a in range(3):
        w = list(v)
        w[a] += 1
        j = idx(*w)
        e = eta(a, v)
        hop[(i, j)] = e
        hop[(j, i)] = e

# 24 proper signed permutation matrices
rots = []
for perm in itertools.permutations(range(3)):
    sgnp = np.linalg.det(np.eye(3)[list(perm)])
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for r in range(3):
            M[r, perm[r]] = signs[r]
        if round(np.linalg.det(M)) == 1:
            rots.append(M)
assert len(rots) == 24


def make_generator(kind):
    if kind == "tx":
        f = lambda v: (v[0] + 1, v[1], v[2])
    elif kind == "ty":
        f = lambda v: (v[0], v[1] + 1, v[2])
    elif kind == "tz":
        f = lambda v: (v[0], v[1], v[2] + 1)
    elif kind == "c4z":
        f = lambda v: (-v[1], v[0], v[2])
    elif kind == "c4x":
        f = lambda v: (v[0], -v[2], v[1])
    elif kind == "c3":
        f = lambda v: (v[1], v[2], v[0])
    perm = np.array([idx(*f(coords(i))) for i in range(N)])
    return perm


def solve_signs(perm):
    """s_v s_w = h_vw * h_{pv,pw} on every NN bond; BFS; return s or None."""
    s = np.zeros(N, dtype=int)
    s[0] = 1
    stack = [0]
    nbrs = [[] for _ in range(N)]
    for (i, j) in hop:
        nbrs[i].append(j)
    while stack:
        v = stack.pop()
        for w in nbrs[v]:
            want = hop[(v, w)] * hop[(perm[v], perm[w])]
            val = s[v] * want
            if s[w] == 0:
                s[w] = val
                stack.append(w)
            elif s[w] != val:
                return None
    return s


gens = {}
for kind in ["tx", "ty", "tz", "c4z", "c4x", "c3"]:
    perm = make_generator(kind)
    s = solve_signs(perm)
    if s is None:
        print("generator", kind, "is NOT a symmetry of the KS hopping (inconsistent signs)")
        sys.exit(1)
    # check invariance
    for (i, j), val in hop.items():
        assert s[i] * s[j] * hop[(perm[i], perm[j])] == val
    gens[kind] = (perm, s)
print("all six generators are symmetries of the KS hopping (signed permutations), L =", L)
MASSIVE = len(sys.argv) > 3 and sys.argv[3] == "massive"
if MASSIVE:
    def compose(g2, g1):
        p1, s1 = g1; p2, s2 = g2
        return (p2[p1], s1 * s2[p1])
    tx, ty, tz = gens["tx"], gens["ty"], gens["tz"]
    new = {"c4z": gens["c4z"], "c4x": gens["c4x"], "c3": gens["c3"]}
    new["tx2"] = compose(tx, tx); new["ty2"] = compose(ty, ty); new["tz2"] = compose(tz, tz)
    new["txty"] = compose(ty, tx); new["tytz"] = compose(tz, ty)
    gens = new
    print("MASSIVE: group restricted to elements preserving eps_v (even translation sum); generators:", list(gens))


class UF:
    """weighted union-find: x_a = w[a] * x_{p[a]}."""
    def __init__(self):
        self.p = {}
        self.w = {}
        self.bad = set()

    def find(self, a):
        if a not in self.p:
            self.p[a] = a
            self.w[a] = 1
            return a, 1
        # iterative find with path compression
        path = []
        cur = a
        while self.p[cur] != cur:
            path.append(cur)
            cur = self.p[cur]
        root = cur
        # sign of each node relative to root
        acc = 1
        for node in reversed(path):
            acc *= self.w[node]
            self.w[node] = acc
            self.p[node] = root
        return root, (self.w[a] if a != root else 1)

    def union(self, a, b, sigma):
        """impose x_a = sigma * x_b."""
        ra, sa = self.find(a)  # x_a = sa x_ra
        rb, sb = self.find(b)  # x_b = sb x_rb
        if ra == rb:
            if sa != sigma * sb:
                self.bad.add(ra)
            return
        # x_ra = sa * x_a = sa * sigma * x_b = sa*sigma*sb * x_rb
        self.p[ra] = rb
        self.w[ra] = sa * sigma * sb
        if ra in self.bad:
            self.bad.add(rb)

    def count(self, nodes):
        roots = set()
        for n in nodes:
            r, _ = self.find(n)
            roots.add(r)
        good = 0
        for r in roots:
            rr, _ = self.find(r)
            if rr not in self.bad and r not in self.bad:
                good += 1
        return good, len(roots)


def classes(rmax):
    seen = set()
    out = []
    for d in itertools.product(range(-rmax, rmax + 1), repeat=3):
        if d == (0, 0, 0) or d in seen:
            continue
        orb = set(tuple(int(t) for t in M @ np.array(d)) for M in rots)
        neg = set(tuple(-t for t in o) for o in orb)
        cls = orb | neg
        seen |= cls
        rep = sorted(orb, key=lambda t: (-t[0], -t[1], -t[2]))[0]
        out.append((rep, cls, (tuple(-t for t in rep) in orb)))
    out.sort(key=lambda t: (sum(x * x for x in t[0]), t[0]))
    return out


def census(kappa):
    """kappa = +1 hopping (symmetric), -1 pairing (antisymmetric)."""
    res = []
    for rep, cls, neg_in_orbit in classes(RMAX):
        uf = UF()
        nodes = set()
        for i in range(N):
            v = coords(i)
            for d in cls:
                j = idx(v[0] + d[0], v[1] + d[1], v[2] + d[2])
                if i < j:
                    nodes.add((i, j))
        for (i, j) in nodes:
            uf.find((i, j))
        for kind, (perm, s) in gens.items():
            for (i, j) in nodes:
                pi, pj = perm[i], perm[j]
                sg = s[i] * s[j]  # x_{pi,pj} = sg * x_{i,j}
                if pi < pj:
                    uf.union((int(pi), int(pj)), (i, j), sg)
                else:
                    # x_{pi,pj} = kappa * x_{pj,pi}
                    uf.union((int(pj), int(pi)), (i, j), sg * kappa)
        good, total = uf.count(nodes)
        res.append((rep, sum(x * x for x in rep), neg_in_orbit, good))
    return res


hop_res = census(+1)
pair_res = census(-1)
print("\nclass rep     |d|^2  -d in O.d   hopping invariants   pairing invariants")
tot_pair_short = 0
for (r1, n2, neg, gh), (r2, _, _, gp) in zip(hop_res, pair_res):
    assert r1 == r2
    print(f"{str(r1):12s} {n2:4d}   {str(neg):6s}      {gh:4d}                 {gp:4d}")
    if n2 < 14:
        tot_pair_short += gp
print("\nNN hopping control (1,0,0) invariants:", [g for (r, n, ng, g) in hop_res if r == (1, 0, 0)])
print("pairing invariants summed over all classes with |d|^2 < 14:", tot_pair_short)
print("classes with pairing invariants > 0:", [(r, g) for (r, n, ng, g) in pair_res if g > 0])
print("classes with -d in O.d that still have pairing > 0:", [(r, g) for (r, n, ng, g) in pair_res if g > 0 and ng])
print("classes with -d NOT in O.d that have pairing == 0:", [(r, g) for (r, n, ng, g) in pair_res if g == 0 and not ng])
