# GUIDE only (pure Python, no numpy). Checks on small lattices:
#  (a) periodic rectangles: log det K = 2 log det' Lap - log V   (file L73)
#  (b) open b^4 box: log det K_open = 4 log b + sum_{m!=0} (r(m)-2) log lambda_m  (file L106-111)
import itertools, math, sys

def lattice(sides, periodic=True):
    D = len(sides)
    verts = list(itertools.product(*[range(s) for s in sides]))
    vid = {v: i for i, v in enumerate(verts)}
    edges = []
    eid = {}
    for v in verts:
        for mu in range(D):
            w = list(v); w[mu] += 1
            if w[mu] == sides[mu]:
                if not periodic:
                    continue
                w[mu] = 0
            eid[(v, mu)] = len(edges)
            edges.append((vid[v], vid[tuple(w)], mu, v))
    plaq = []
    for v in verts:
        for mu in range(D):
            for nu in range(mu + 1, D):
                vm = list(v); vm[mu] += 1
                vn = list(v); vn[nu] += 1
                if not periodic and (vm[mu] >= sides[mu] or vn[nu] >= sides[nu]):
                    continue
                vm[mu] %= sides[mu]; vn[nu] %= sides[nu]
                plaq.append([(eid[(v, mu)], 1), (eid[(tuple(vm), nu)], 1),
                             (eid[(tuple(vn), mu)], -1), (eid[(v, nu)], -1)])
    return verts, vid, edges, eid, plaq

def comb_tree(sides, eid, verts):
    D = len(sides)
    tree = set()
    for v in verts:
        for mu in range(D):
            if all(v[k] == 0 for k in range(mu)) and v[mu] < sides[mu] - 1:
                tree.add(eid[(v, mu)])
    return tree

def gram_free(plaq, free):
    # K = A^T A with A = d1 restricted to free edge columns; sparse build
    pos = {k: i for i, k in enumerate(free)}
    M = len(free)
    K = [[0.0] * M for _ in range(M)]
    for p in plaq:
        ent = [(pos[k], s) for (k, s) in p if k in pos]
        for (i, si) in ent:
            for (j, sj) in ent:
                K[i][j] += si * sj
    return K

def logdet_spd(A):
    # Cholesky; returns log det, raises if not SPD
    n = len(A)
    L = [row[:] for row in A]
    ld = 0.0
    for j in range(n):
        Lj = L[j]
        s = Lj[j] - sum(Lj[k] * Lj[k] for k in range(j))
        if s <= 1e-12:
            raise ValueError("not SPD at %d: %g" % (j, s))
        d = math.sqrt(s)
        Lj[j] = d
        ld += 2 * math.log(d)
        for i in range(j + 1, n):
            Li = L[i]
            t = Li[j] - sum(Li[k] * Lj[k] for k in range(j))
            Li[j] = t / d
    return ld

def logdetprime_lap_periodic(sides):
    tot = 0.0
    for m in itertools.product(*[range(s) for s in sides]):
        if all(x == 0 for x in m):
            continue
        lam = sum(2 - 2 * math.cos(2 * math.pi * mi / s) for mi, s in zip(m, sides))
        tot += math.log(lam)
    return tot

def run_periodic(sides):
    verts, vid, edges, eid, plaq = lattice(sides, True)
    V = len(verts); E = len(edges)
    tree = comb_tree(sides, eid, verts)
    assert len(tree) == V - 1
    base = set(eid[(tuple((sides[mu] - 1) if k == mu else 0 for k in range(4)), mu)] for mu in range(4))
    free = [k for k in range(E) if k not in tree and k not in base]
    K = gram_free(plaq, free)
    ldK = logdet_spd(K)
    pred = 2 * logdetprime_lap_periodic(sides) - math.log(V)
    print("periodic", sides, "V", V, "M", len(free), "logdetK %.10f" % ldK,
          "2logdet'Lap-logV %.10f" % pred, "diff %.2e" % (ldK - pred), flush=True)

def run_open(b):
    sides = (b, b, b, b)
    verts, vid, edges, eid, plaq = lattice(sides, False)
    V = len(verts); E = len(edges)
    tree = comb_tree(sides, eid, verts)
    assert len(tree) == V - 1
    free = [k for k in range(E) if k not in tree]
    K = gram_free(plaq, free)
    ldK = logdet_spd(K)
    pred = 4 * math.log(b)
    for m in itertools.product(range(b), repeat=4):
        if m == (0, 0, 0, 0):
            continue
        lam = 4 * sum(math.sin(math.pi * mi / (2 * b)) ** 2 for mi in m)
        r = sum(1 for mi in m if mi > 0)
        pred += (r - 2) * math.log(lam)
    print("open b", b, "free", len(free), "logdetK %.10f" % ldK, "formula %.10f" % pred,
          "diff %.2e" % (ldK - pred), flush=True)

if __name__ == "__main__":
    for b in [2, 3]:
        run_open(b)
    for s in [(3, 3, 3, 3), (3, 3, 3, 4), (4, 3, 3, 3)]:
        run_periodic(s)
