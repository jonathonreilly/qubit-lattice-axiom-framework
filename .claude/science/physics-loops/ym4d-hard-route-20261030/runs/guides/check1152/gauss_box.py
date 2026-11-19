# GUIDE only: checks the Section 14 Gaussian identities of row 1151 on small boxes.
import itertools, math
import numpy as np

def box(a):
    V = list(itertools.product(range(a[0]), range(a[1]), range(a[2])))
    idx = {v: i for i, v in enumerate(V)}
    E = []
    for v in V:
        for d in range(3):
            w = list(v); w[d] += 1; w = tuple(w)
            if w in idx:
                E.append((v, d))
    eidx = {e: i for i, e in enumerate(E)}
    P = []
    for v in V:
        for d1 in range(3):
            for d2 in range(d1 + 1, 3):
                w1 = list(v); w1[d1] += 1; w1 = tuple(w1)
                w2 = list(v); w2[d2] += 1; w2 = tuple(w2)
                if w1 in idx and w2 in idx:
                    # plaquette edges: (v,d1) + (v+d1,d2) - (v+d2,d1) - (v,d2)
                    P.append([((v, d1), 1), ((w1, d2), 1), ((w2, d1), -1), ((v, d2), -1)])
    grad = np.zeros((len(E), len(V)))
    for i, (v, d) in enumerate(E):
        w = list(v); w[d] += 1; w = tuple(w)
        grad[i, idx[w]] += 1; grad[i, idx[v]] -= 1
    curl = np.zeros((len(P), len(E)))
    for j, p in enumerate(P):
        for e, sgn in p:
            curl[j, eidx[e]] += sgn
    return V, E, P, idx, eidx, grad, curl

def comb_tree(V, E, idx, eidx):
    # comb: all 1-links on line x2=x3=0, all 2-links on plane x3=0, all 3-links
    T = set()
    for (v, d) in E:
        if d == 2: T.add(eidx[(v, d)])
        elif d == 1 and v[2] == 0: T.add(eidx[(v, d)])
        elif d == 0 and v[1] == 0 and v[2] == 0: T.add(eidx[(v, d)])
    assert len(T) == len(V) - 1
    return T

def gaussian_logdet(a, s):
    V, E, P, idx, eidx, grad, curl = box(a)
    T = comb_tree(V, E, idx, eidx)
    free_sp = [i for i in range(len(E)) if i not in T]
    root = idx[(0, 0, 0)]
    free_v = [i for i in range(len(V)) if i != root]
    nsp, nv = len(free_sp), len(free_v)
    nper = nsp + nv
    dim = s * nper
    Q = np.zeros((dim, dim))
    def xcol(t, k): return (t % s) * nper + k
    def pcol(t, k): return (t % s) * nper + nsp + k
    # spatial plaquettes at each t
    for t in range(s):
        for j in range(len(P)):
            row = np.zeros(dim)
            for kk, ei in enumerate(free_sp):
                if curl[j, ei] != 0: row[xcol(t, kk)] += curl[j, ei]
            Q += np.outer(row, row)
    # temporal plaquettes: x_{t+1}(e) - x_t(e) - (grad phi_t)(e)
    for t in range(s):
        for ei in range(len(E)):
            row = np.zeros(dim)
            if ei in free_sp:
                kk = free_sp.index(ei)
                row[xcol(t + 1, kk)] += 1; row[xcol(t, kk)] -= 1
            for vi in range(len(V)):
                if grad[ei, vi] != 0 and vi != root:
                    row[pcol(t, free_v.index(vi))] -= grad[ei, vi]
            Q += np.outer(row, row)
    sign, ld = np.linalg.slogdet(Q)
    assert sign > 0
    return ld, dim

def mode_sum(a, m):
    V, E, P, idx, eidx, grad, curl = box(a)
    # projection onto ker grad^*
    U, S, Vt = np.linalg.svd(grad, full_matrices=True)
    r = int((S > 1e-9).sum())
    Kc = U[:, r:]  # basis of ker grad^T (orthogonal complement of range grad)
    L = Kc.T @ curl.T @ curl @ Kc
    lam = np.linalg.eigvalsh(L)
    om = np.arccosh(1 + lam / 2)
    return float(np.sum(np.log((1 + np.exp(-m * om)) / (1 - np.exp(-m * om))))), lam

def hodge_check(a):
    V, E, P, idx, eidx, grad, curl = box(a)
    D1 = grad @ grad.T + curl.T @ curl
    ev = np.sort(np.linalg.eigvalsh(D1))
    pred = []
    for d in range(3):
        rng = [range(1, a[k]) if k == d else range(0, a[k]) for k in range(3)]
        for q in itertools.product(*rng):
            pred.append(sum(4 * math.sin(math.pi * q[k] / (2 * a[k])) ** 2 for k in range(3)))
    pred = np.sort(np.array(pred))
    return float(np.max(np.abs(ev - pred)))

# 1. periodic determinant identity
for s in [1, 2, 3, 5, 8]:
    for w in [0.1, 0.7, 2.0]:
        lhs = sum(math.log(2 * math.cosh(w) - 2 * math.cos(2 * math.pi * k / s)) for k in range(s))
        rhs = s * w + 2 * math.log(1 - math.exp(-s * w))
        assert abs(lhs - rhs) < 1e-9, (s, w, lhs, rhs)
print("periodic determinant identity: OK")
# 2. Hodge Laplacian on product of paths
for a in [(2, 3, 4), (3, 3, 3), (4, 2, 3)]:
    print("hodge", a, "max eigen mismatch", hodge_check(a))
# 3. exact cancellation: 2 log G_m - log G_2m (one color, beta = 1) vs mode sum
for a in [(2, 2, 3), (3, 3, 3)]:
    for m in [1, 2, 3]:
        ld1, d1 = gaussian_logdet(a, m)
        ld2, d2 = gaussian_logdet(a, 2 * m)
        assert d2 == 2 * d1
        lhs = -ld1 + 0.5 * ld2  # 2*(-1/2 ld1) - (-1/2 ld2); 2pi factors cancel since d2 = 2 d1
        rhs, lam = mode_sum(a, m)
        print("box", a, "m", m, "2logG_m-logG_2m (one colour) =", round(lhs, 10), " mode sum =", round(rhs, 10), " min lambda", round(float(lam.min()), 6))
