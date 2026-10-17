"""Translation-invariant BKSF codes on the cubic lattice (qubit on each edge; edge (v, a) = v -> v + e_a).
Ordering: a total order on the six directions (+x,+y,+z,-x,-y,-z) used at every vertex.
A_(v,a) = X_(v,a) * prod Z over edges at v before +a * prod Z over edges at v+e_a before -a.
B_v = Z on the six edges at v. Plaquette stabilizers S = product of A around each plaquette."""
import itertools, sys, hashlib
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
E = [(1,0,0),(0,1,0),(0,0,1)]
DIRS = [(0,1),(1,1),(2,1),(0,-1),(1,-1),(2,-1)]     # (axis, sign)
def edge_at(v, d):
    a, s = DIRS[d]
    return (v, a) if s == 1 else (tuple(v[i] - E[a][i] for i in range(3)), a)
def mul(op, key, lab):
    c = op.get(key, 0)
    op[key] = lab if c == 0 else (0 if c == lab else 6 - c - lab)
    if op[key] == 0: del op[key]
def A(v, a, order):
    op = {}; mul(op, (v, a), 1)
    pos = {d: i for i, d in enumerate(order)}
    dplus = DIRS.index((a, 1)); dminus = DIRS.index((a, -1))
    w = tuple(v[i] + E[a][i] for i in range(3))
    for d in range(6):
        if pos[d] < pos[dplus]: mul(op, edge_at(v, d), 3)
        if pos[d] < pos[dminus]: mul(op, edge_at(w, d), 3)
    return op
def B(v):
    op = {}
    for d in range(6): mul(op, edge_at(v, d), 3)
    return op
def prod(*ops):
    out = {}
    for o in ops:
        for k, l in o.items(): mul(out, k, l)
    return out
def plaq(v, c, order):
    a, b = [k for k in range(3) if k != c]
    va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
    return prod(A(v, a, order), A(va, b, order), A(vb, a, order), A(v, b, order))
def anti(o1, o2): return sum(1 for k, l in o1.items() if o2.get(k, 0) not in (0, l)) % 2
def gens_at_origin(order):
    return [B((0,0,0))] + [plaq((0,0,0), c, order) for c in range(3)]
def torus_rows(gens, L):
    n = 3 * L**3; idx = lambda p, a: 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a; R = []
    for v in itertools.product(range(L), repeat=3):
        for g in gens:
            x = np.zeros(2*n, np.uint8)
            for (p, a), l in g.items():
                q = idx([v[i] + p[i] for i in range(3)], a)
                if l in (1, 2): x[q] ^= 1
                if l in (2, 3): x[n + q] ^= 1
            R.append(x)
    return np.array(R)
def rref_hash(M):
    A_ = M.copy() % 2; m, n = A_.shape; r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A_[i, c]), None)
        if p is None: continue
        A_[[r, p]] = A_[[p, r]]; rows = np.nonzero(A_[:, c])[0]; rows = rows[rows != r]; A_[rows] ^= A_[r]; r += 1
        if r == m: break
    return hashlib.sha1(np.packbits(A_[:r]).tobytes()).hexdigest(), r
