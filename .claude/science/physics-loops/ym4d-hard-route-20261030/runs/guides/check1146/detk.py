# GUIDE only: check det K = (det' Delta)^2 / V on small periodic 4D rectangles,
# and det K_open = b^4 prod_{m != 0} lambda_m^(r(m)-2) on small open boxes.
import itertools, sys
import numpy as np

def lattice(sides, periodic=True):
    D = len(sides)
    verts = list(itertools.product(*[range(s) for s in sides]))
    vid = {v: i for i, v in enumerate(verts)}
    edges = []  # (tail, head, dir)
    for v in verts:
        for mu in range(D):
            w = list(v); w[mu] += 1
            if w[mu] == sides[mu]:
                if not periodic:
                    continue
                w[mu] = 0
            edges.append((vid[v], vid[tuple(w)], mu, v))
    eid = {}
    for k, (a, b, mu, v) in enumerate(edges):
        eid[(v, mu)] = k
    plaq = []
    for v in verts:
        for mu in range(D):
            for nu in range(mu + 1, D):
                # edges: (v,mu), (v+mu,nu), (v+nu,mu) reversed, (v,nu) reversed
                vm = list(v); vm[mu] += 1
                vn = list(v); vn[nu] += 1
                ok = True
                if not periodic and (vm[mu] >= sides[mu] or vn[nu] >= sides[nu]):
                    ok = False
                if not ok:
                    continue
                vm[mu] %= sides[mu]; vn[nu] %= sides[nu]
                plaq.append([(eid[(v, mu)], 1), (eid[(tuple(vm), nu)], 1),
                             (eid[(tuple(vn), mu)], -1), (eid[(v, nu)], -1)])
    return verts, vid, edges, eid, plaq

def comb_tree(sides, vid, eid, periodic=True):
    D = len(sides)
    tree = []
    for v in vid:
        # direction mu used at v if v has zeros in all coords < mu ... comb:
        # dir 0 edges: all v with v[0] < s0-1
        # dir mu edges: v with v[0..mu-1]=0 and v[mu] < s_mu - 1
        for mu in range(D):
            if all(v[k] == 0 for k in range(mu)) and v[mu] < sides[mu] - 1:
                tree.append(eid[(v, mu)])
    return sorted(set(tree))

def run_periodic(sides):
    verts, vid, edges, eid, plaq = lattice(sides, True)
    V = len(verts); E = len(edges)
    d0 = np.zeros((E, V))
    for k, (a, b, mu, v) in enumerate(edges):
        d0[k, b] += 1; d0[k, a] -= 1
    d1 = np.zeros((len(plaq), E))
    for i, p in enumerate(plaq):
        for (k, sgn) in p:
            d1[i, k] += sgn
    assert np.abs(d1 @ d0).max() == 0
    tree = comb_tree(sides, vid, eid)
    assert len(tree) == V - 1
    base = [eid[(tuple((sides[mu] - 1) if k == mu else 0 for k in range(4)), mu)] for mu in range(4)]
    fixed = set(tree) | set(base)
    free = [k for k in range(E) if k not in fixed]
    M = len(free)
    A = d1[:, free]
    K = A.T @ A
    sK, ldK = np.linalg.slogdet(K)
    lap = d0.T @ d0
    ev = np.linalg.eigvalsh(lap)
    ev = np.sort(ev)
    assert abs(ev[0]) < 1e-9 and ev[1] > 1e-9
    ldlap = np.sum(np.log(ev[1:]))
    pred = 2 * ldlap - np.log(V)
    print("periodic", sides, "V", V, "M", M, "3V-3", 3 * V - 3, "sign", sK,
          "logdetK", round(ldK, 8), "2logdet'Lap - logV", round(pred, 8), "diff", ldK - pred)

def run_open(b):
    sides = (b, b, b, b)
    verts, vid, edges, eid, plaq = lattice(sides, False)
    V = len(verts); E = len(edges)
    d1 = np.zeros((len(plaq), E))
    for i, p in enumerate(plaq):
        for (k, sgn) in p:
            d1[i, k] += sgn
    tree = comb_tree(sides, vid, eid, False)
    assert len(tree) == V - 1
    free = [k for k in range(E) if k not in set(tree)]
    A = d1[:, free]
    K = A.T @ A
    sK, ldK = np.linalg.slogdet(K)
    pred = 4 * np.log(b)
    for m in itertools.product(range(b), repeat=4):
        if m == (0, 0, 0, 0):
            continue
        lam = 4 * sum(np.sin(np.pi * mi / (2 * b)) ** 2 for mi in m)
        r = sum(1 for mi in m if mi > 0)
        pred += (r - 2) * np.log(lam)
    print("open b", b, "free", len(free), "sign", sK, "logdetK", round(ldK, 8),
          "formula", round(pred, 8), "diff", ldK - pred)

if __name__ == "__main__":
    for s in [(3, 3, 3, 3), (3, 3, 3, 4), (3, 4, 3, 5), (4, 4, 4, 3)]:
        run_periodic(s)
    for b in [2, 3]:
        run_open(b)
