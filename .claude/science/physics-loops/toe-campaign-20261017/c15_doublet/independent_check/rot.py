"""Rotation action: link signed permutations (consistent groups) x 2O on matter."""
AUDIT_TIMEOUT_SEC = 1800
import itertools, numpy as np
from mj import *
import matter as MT

ROTS = rotations()
def rkey(R): return tuple(int(x) for x in np.asarray(R).flatten())
RIDX = {rkey(R): i for i, R in enumerate(ROTS)}

def eps_choices(R):
    p = dir_perm(R); sg = perm_sign(p)
    return [e for e in itertools.product([1, -1], repeat=6) if np.prod(e) == sg]

def sp_compose(s2, s1):
    """apply s1 then s2; s = (perm tuple, eps tuple): b_d -> eps[d] b_{perm[d]}"""
    p1, e1 = s1; p2, e2 = s2
    return (tuple(p2[p1[d]] for d in range(6)), tuple(e1[d] * e2[p1[d]] for d in range(6)))

def gen_group(gens):
    idn = (tuple(range(6)), (1,) * 6)
    G = {idn}; frontier = [idn]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = sp_compose(g, x)
                if y not in G:
                    G.add(y); new.append(y)
        frontier = new
        if len(G) > 200: break
    return G

def find_rot(pred):
    for R in ROTS:
        if pred(R): return R

C4z = find_rot(lambda R: (R @ [1, 0, 0] == [0, 1, 0]).all() and (R @ [0, 0, 1] == [0, 0, 1]).all())
C3 = find_rot(lambda R: (R @ [1, 0, 0] == [0, 1, 0]).all() and (R @ [0, 1, 0] == [0, 0, 1]).all())

def consistent_link_groups():
    out = []
    p4 = tuple(dir_perm(C4z)); p3 = tuple(dir_perm(C3))
    for e4 in eps_choices(C4z):
        for e3 in eps_choices(C3):
            G = gen_group([(p4, e4), (p3, e3)])
            if len(G) == 48:
                out.append(G)
    return out

def perm_to_rot(p):
    M = np.zeros((3, 3), int)
    for c in range(3):
        M[:, c] = DIRS[p[c]]
    return M

class Action:
    """Full on-site action for rotation R: site perm v->Rv, link signed perm, matter SO(4)."""
    def __init__(s, lat, R, link_sp, M4):
        s.lat = lat; s.R = np.asarray(R); s.p, s.e = link_sp; s.M4 = M4
        s.cache = {}
        s.siteperm = np.array([lat.idx(s.R @ np.array(lat.coord(i))) for i in range(lat.N)])
    def img_major(s, k):
        if k < 6:
            return {1 << s.p[k]: float(s.e[k])}
        out = {}
        for j in range(4):
            c = s.M4[j, k - 6]
            if abs(c) > 1e-12: out[1 << (6 + j)] = c
        return out
    def img_site(s, mask):
        if mask in s.cache: return s.cache[mask]
        P = {0: 1.0 + 0j}
        for k in range(10):
            if mask >> k & 1:
                Q = s.img_major(k); R = {}
                for a, ca in P.items():
                    for b, cb in Q.items():
                        sg, ab = site_mul(a, b)
                        R[ab] = R.get(ab, 0) + ca * cb * sg
                P = {a: c for a, c in R.items() if abs(c) > 1e-13}
        s.cache[mask] = P; return P
    def conj_mono(s, coef, masks):
        N = s.lat.N
        sites = np.nonzero(masks)[0]
        per = []
        for st in sites:
            per.append((s.siteperm[st], list(s.img_site(int(masks[st])).items())))
        out = {}
        for combo in itertools.product(*[x[1] for x in per]):
            m = np.zeros(N, dtype=np.int64); c = coef
            for (ns, _), (mk, cc) in zip(per, combo):
                m[ns] = mk; c = c * cc
            k = tuple(m.tolist()); out[k] = out.get(k, 0) + c
        return out
    def conj(s, P):
        out = {}
        for k, c in P.items():
            for k2, c2 in s.conj_mono(c, np.array(k, dtype=np.int64)).items():
                out[k2] = out.get(k2, 0) + c2
        return {k: v for k, v in out.items() if abs(v) > 1e-12}

def matter_lifts():
    """for each rotation index: list of (q, D, M4) of the two 2O lifts"""
    Q = MT.quat_2O()
    out = {i: [] for i in range(24)}
    for q in Q:
        D = MT.su2(q); R = np.rint(MT.so3(D)).astype(int)
        U = MT.fock(D); M4 = MT.so4(U)
        out[RIDX[rkey(R)]].append((q, D, M4))
    return out

def c_dag(N, site, e):
    """c_e^dag at site = sum_s e_s c_s^dag ; c_s^dag = (chi_a - i chi_b)/2"""
    P = {}
    for s_, (a, b) in enumerate([(6, 7), (8, 9)]):
        if abs(e[s_]) < 1e-14: continue
        for k, c in [(a, 0.5), (b, -0.5j)]:
            m = np.zeros(N, dtype=np.int64); m[site] = 1 << k
            kk = tuple(m.tolist()); P[kk] = P.get(kk, 0) + e[s_] * c
    return P

def path_string(lat, x, y):
    """product of u_e along a lattice path from x to y (real-space lift)"""
    N = lat.N
    op = (1.0 + 0j, np.zeros(N, dtype=np.int64))
    v = list(x)
    for a in range(3):
        while v[a] != y[a]:
            step = 1 if y[a] > v[a] else -1
            if step == 1:
                op = mul(op, u_edge(lat, tuple(v), a))
            else:
                w = list(v); w[a] -= 1
                op = mul(op, u_edge(lat, tuple(w), a))
            v[a] += step
    return to_poly(op)

def pair_eig(G, act, A):
    Ap = act.conj(A)
    num, k1 = G.code_poly_value(poly_mul(poly_dag(A), Ap))
    den, k2 = G.code_poly_value(poly_mul(poly_dag(A), A))
    return num / den, abs(num / den)
