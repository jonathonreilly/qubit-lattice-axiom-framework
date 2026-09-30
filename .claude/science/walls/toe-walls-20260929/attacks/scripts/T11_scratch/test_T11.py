#!/usr/bin/env python3
"""T11 tests A-E. Pre-registered in PREREGISTER.md. Same-family check (Claude Sonnet 5.5)."""
import itertools, json, sys, time
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
import scipy.sparse as sp
import scipy.sparse.linalg as spla

OUT = {}

# ----------------------------------------------------------------- graphs
def path(n): return n, [(i, i + 1) for i in range(n - 1)]
def cycle(n): return n, [(i, (i + 1) % n) for i in range(n)]
def star(k): return k + 1, [(0, i) for i in range(1, k + 1)]
def cube():
    idx = lambda x, y, z: x + 2 * y + 4 * z
    E = []
    for x, y, z in itertools.product(range(2), repeat=3):
        for d in range(3):
            c = [x, y, z]
            if c[d] == 0:
                c2 = list(c); c2[d] = 1
                E.append((idx(x, y, z), idx(*c2)))
    return 8, E

def adj_of(n, E):
    A = [set() for _ in range(n)]
    for u, v in E:
        A[u].add(v); A[v].add(u)
    return A

# ------------------------------------------------ acyclic orientation counts
def chi_at(n, E, k):
    """chromatic polynomial by deletion-contraction, evaluated at k (simple graph)."""
    E = frozenset(frozenset(e) for e in E)
    def rec(nv, edges):
        if not edges:
            return k ** nv
        e = next(iter(edges))
        u, v = tuple(e)
        rest = edges - {e}
        # contraction: merge v into u
        new = set()
        for f in rest:
            g = frozenset(u if x == v else x for x in f)
            if len(g) == 2:
                new.add(g)
        return rec(nv, rest) - rec(nv - 1, frozenset(new))
    return rec(n, E)

def count_acyclic_bruteforce(n, E):
    m = len(E); cnt = 0
    for bits in range(1 << m):
        out = [[] for _ in range(n)]; indeg = [0] * n
        for j, (u, v) in enumerate(E):
            a, b = (u, v) if (bits >> j) & 1 else (v, u)
            out[a].append(b); indeg[b] += 1
        q = [i for i in range(n) if indeg[i] == 0]; seen = 0
        while q:
            a = q.pop(); seen += 1
            for b in out[a]:
                indeg[b] -= 1
                if indeg[b] == 0: q.append(b)
        cnt += (seen == n)
    return cnt

# ------------------------------------------------ law of a formation order
def law_exact(n, A, order):
    """exact final joint law (dict cfg->Fraction) when sites form in `order`, rule (2)."""
    law = {(): Fraction(1)}
    # build by sequential extension; cfg as dict via tuple aligned with `order`
    cur = {(): Fraction(1)}
    for i, v in enumerate(order):
        nxt = {}
        prior = order[:i]
        for cfg, p in cur.items():
            ap = sum(1 for j, u in enumerate(prior) if u in A[v] and cfg[j] == 1)
            am = sum(1 for j, u in enumerate(prior) if u in A[v] and cfg[j] == -1)
            wp, wm = 4 ** ap, 4 ** am
            for s, w in ((1, wp), (-1, wm)):
                nxt[cfg + (s,)] = nxt.get(cfg + (s,), 0) + p * Fraction(w, wp + wm)
        cur = nxt
    # reindex to site order
    out = {}
    for cfg, p in cur.items():
        full = [0] * n
        for j, v in enumerate(order): full[v] = cfg[j]
        out[tuple(full)] = p
    return out

_SGN = {}
def law_float_all(n, A, order):
    """numpy float law vector over 2^n configs (bit i -> site i, 1 = +1)."""
    N = 1 << n
    sgn = _SGN.get(n)
    if sgn is None:
        sgn = np.array([[1 if (c >> i) & 1 else -1 for i in range(n)] for c in range(N)]); _SGN[n] = sgn
    p = np.ones(N)
    rec = []
    for v in order:
        ap = np.zeros(N); am = np.zeros(N)
        for u in rec:
            if u in A[v]:
                ap += (sgn[:, u] == 1); am += (sgn[:, u] == -1)
        wp = 4.0 ** ap; wm = 4.0 ** am
        pv = np.where(sgn[:, v] == 1, wp, wm) / (wp + wm)
        p = p * pv
        rec.append(v)
    return p

def cfg_index(cfg):
    return sum((1 << i) for i, s in enumerate(cfg) if s == 1)

def orientation_sig(order, E):
    pos = {v: i for i, v in enumerate(order)}
    return tuple(sorted(((u, v) if pos[u] < pos[v] else (v, u)) for u, v in E))

def commutation_classes(n, E, perms):
    """partition permutations by BFS closure under swapping adjacent letters that are NOT adjacent in G."""
    Es = {frozenset(e) for e in E}
    permset = set(perms)
    cls = {}
    cid = 0
    for p in perms:
        if p in cls: continue
        stack = [p]; cls[p] = cid
        while stack:
            q = stack.pop()
            for i in range(n - 1):
                if frozenset((q[i], q[i + 1])) not in Es:
                    r = q[:i] + (q[i + 1], q[i]) + q[i + 2:]
                    if r not in cls:
                        cls[r] = cid; stack.append(r)
        cid += 1
    return cls, cid

# ----------------------------------------------------------------- TEST A
def test_A():
    res = {}
    graphs = {
        "P3": path(3), "P4": path(4), "C4": cycle(4), "K1,3": star(3),
        "K1,6": star(6), "Q3(cube)": cube(),
    }
    for name, (n, E) in graphs.items():
        t0 = time.time()
        A = adj_of(n, E)
        perms = list(itertools.permutations(range(n)))
        # partition 1: orientation signature; partition 2: commutation closure
        sig_of = {p: orientation_sig(p, E) for p in perms}
        cls2, ncls2 = commutation_classes(n, E, perms)
        sigs = {}
        for p in perms: sigs.setdefault(sig_of[p], []).append(p)
        # same partition?
        same = all(len({cls2[p] for p in ps}) == 1 for ps in sigs.values()) and len(sigs) == ncls2
        chi = abs(chi_at(n, E, -1))
        brute = count_acyclic_bruteforce(n, E) if len(E) <= 12 else None
        # laws
        exact = n <= 7
        laws = {}
        ok_within = True; maxdev = 0.0
        for sg, ps in sigs.items():
            if exact:
                ref = law_exact(n, A, ps[0]); vec = np.zeros(1 << n)
                for c, pr in ref.items(): vec[cfg_index(c)] = float(pr)
                for p in ps[1:]:
                    l2 = law_exact(n, A, p)
                    if l2 != ref: ok_within = False
                laws[sg] = (vec, ref)
            else:
                ref = law_float_all(n, A, ps[0])
                for p in ps[1:]:
                    d = np.abs(law_float_all(n, A, p) - ref).max(); maxdev = max(maxdev, d)
                    if d > 1e-13: ok_within = False
                laws[sg] = (ref, None)
        vecs = np.array([v for v, _ in laws.values()])
        distinct = len({tuple(np.round(v, 12)) for v in vecs})
        # max pairwise L1 spread across classes
        maxL1 = 0.0
        for i in range(len(vecs)):
            for j in range(i + 1, len(vecs)):
                maxL1 = max(maxL1, np.abs(vecs[i] - vecs[j]).sum())
        # depth (Foata height) distribution over classes
        def height(sg):
            succ = {}
            for u, v in sg: succ.setdefault(u, []).append(v)
            memo = {}
            def h(x):
                if x in memo: return memo[x]
                memo[x] = 1 + max([h(y) for y in succ.get(x, [])], default=0); return memo[x]
            return max(h(x) for x in range(n))
        heights = sorted({height(sg) for sg in sigs})
        res[name] = dict(n=n, edges=len(E), perms=len(perms), classes_by_orientation=len(sigs),
                         classes_by_commutation=ncls2, partitions_equal=same,
                         stanley_abs_chi_minus1=int(chi), acyclic_bruteforce=brute,
                         laws_equal_within_class=ok_within, exact_rational=exact,
                         max_dev_within_class_float=maxdev,
                         distinct_laws_across_classes=distinct, max_L1_between_class_laws=maxL1,
                         foata_heights_present=heights, secs=round(time.time() - t0, 1))
        print("A", name, res[name], flush=True)
        graphs[name] = (n, E, laws)
    return res, graphs

# ----------------------------------------------------------------- TEST B
def parallel_absorbed_law(n, A, q):
    """08-11 note eq (5): every empty site forms with prob q against the PRE-update configuration."""
    states = list(itertools.product((0, -1, 1), repeat=n))
    sidx = {s: i for i, s in enumerate(states)}
    S = len(states)
    rows, cols, vals = [], [], []
    for s in states:
        i = sidx[s]
        empties = [v for v in range(n) if s[v] == 0]
        # per-site options: stay empty (1-q), form s (q*p(s|pre-update nbrs))
        opts = []
        for v in empties:
            ap = sum(1 for u in A[v] if s[u] == 1); am = sum(1 for u in A[v] if s[u] == -1)
            wp, wm = 4.0 ** ap, 4.0 ** am
            opts.append([(0, 1 - q), (1, q * wp / (wp + wm)), (-1, q * wm / (wp + wm))])
        for combo in itertools.product(*opts) if empties else [()]:
            pr = 1.0; t = list(s)
            for v, (c, w) in zip(empties, combo):
                pr *= w; t[v] = c
            rows.append(i); cols.append(sidx[tuple(t)]); vals.append(pr)
    P = sp.csr_matrix((vals, (rows, cols)), shape=(S, S))
    absorbing = [sidx[s] for s in states if all(x != 0 for x in s)]
    absorbing_set = set(absorbing)
    transient = [i for i in range(S) if i not in absorbing_set]
    tpos = {i: k for k, i in enumerate(transient)}
    Q = P[transient][:, transient]
    R = P[transient][:, absorbing]
    start = tpos[sidx[tuple([0] * n)]]
    e = np.zeros(len(transient)); e[start] = 1.0
    y = spla.spsolve((sp.identity(len(transient)) - Q).T.tocsc(), e)
    fin = np.asarray(R.T @ y).ravel()
    law = np.zeros(1 << n)
    for k, a in enumerate(absorbing):
        law[cfg_index(states[a])] = fin[k]
    return law

def hull_L1(target, vecs):
    m, d = len(vecs), len(target)
    # variables: w (m), u (d), v (d) ; L^T w + u - v = target ; sum w = 1
    c = np.concatenate([np.zeros(m), np.ones(2 * d)])
    Aeq = np.zeros((d + 1, m + 2 * d)); beq = np.zeros(d + 1)
    for j in range(m): Aeq[:d, j] = vecs[j]
    Aeq[:d, m:m + d] = np.eye(d); Aeq[:d, m + d:] = -np.eye(d); beq[:d] = target
    Aeq[d, :m] = 1; beq[d] = 1
    r = linprog(c, A_eq=Aeq, b_eq=beq, bounds=(0, None), method="highs")
    return r.fun, r.x[:m]

def test_B(graphsA):
    res = {}
    for name in ["P3", "C4", "K1,3", "K1,6"]:
        n, E, laws = graphsA[name]
        A = adj_of(n, E)
        vecs = np.array([v for v, _ in laws.values()])
        # uniform random order law = mean over all permutations of class laws weighted by class size
        perms = list(itertools.permutations(range(n)))
        sizes = {}
        for p in perms: sizes[orientation_sig(p, E)] = sizes.get(orientation_sig(p, E), 0) + 1
        seq = sum(sizes[sg] * laws[sg][0] for sg in laws) / len(perms)
        r = {}
        for q in [2 / 3, 1 / 3, 0.1, 0.01, 0.001]:
            par = parallel_absorbed_law(n, A, q)
            d_seq = float(np.abs(par - seq).sum())
            d_hull, _ = hull_L1(par, vecs)
            r[f"q={q:.4g}"] = dict(L1_to_random_sequential=d_seq, L1_to_hull_of_class_laws=float(d_hull),
                                   E_prod_center_leaf=float(sum(par[c] * (1 if (c >> 0) & 1 else -1) * (1 if (c >> 1) & 1 else -1) for c in range(1 << n))))
        r["E_prod_center_leaf_random_sequential"] = float(sum(seq[c] * (1 if (c >> 0) & 1 else -1) * (1 if (c >> 1) & 1 else -1) for c in range(1 << n)))
        res[name] = r
        print("B", name, json.dumps(r, indent=1), flush=True)
    # K2 witness (2026-08-11 eq 9,10)
    n, E = path(2); A = adj_of(n, E)
    seq = 0.5 * law_float_all(n, A, (0, 1)) + 0.5 * law_float_all(n, A, (1, 0))
    Ecorr = lambda l: float(sum(l[c] * (1 if c & 1 else -1) * (1 if c & 2 else -1) for c in range(4)))
    hull2 = np.array([law_float_all(n, A, (0, 1)), law_float_all(n, A, (1, 0))])
    res["K2"] = {"E_sequential": Ecorr(seq)}
    for q in [1.0, 2 / 3, 0.5, 1 / 3, 0.01]:
        par = parallel_absorbed_law(n, A, q)
        res["K2"]["q=%.4g" % q] = dict(E_absorbed=Ecorr(par),
                                       closed_form=0.6 * 2 * (1 - q) / (2 - q),
                                       L1_to_hull=float(hull_L1(par, hull2)[0]))
    print("B K2", res["K2"])
    return res

# ----------------------------------------------------------------- TEST C
def test_C():
    # seed(+1)=site 0 adjacent to b=1 ; b=1 adjacent to c=2 ; seed not adjacent to c
    def law_bc(order):  # order: 'bc' or 'cb'; returns P over (b,c)
        out = {}
        for b in (1, -1):
            for c in (1, -1):
                if order == "bc":
                    ap, am = (1, 0)  # b sees seed + only
                    pb = Fraction(4 ** ap, 4 ** ap + 4 ** am) if b == 1 else Fraction(4 ** am, 4 ** ap + 4 ** am)
                    ap2 = 1 if b == 1 else 0; am2 = 1 - ap2
                    pc = Fraction(4 ** ap2, 4 ** ap2 + 4 ** am2) if c == 1 else Fraction(4 ** am2, 4 ** ap2 + 4 ** am2)
                    out[(b, c)] = pb * pc
                else:
                    pc = Fraction(1, 2)  # c has no recorded neighbour
                    ap = 1 + (1 if c == 1 else 0); am = (1 if c == -1 else 0)
                    pb = Fraction(4 ** ap, 4 ** ap + 4 ** am) if b == 1 else Fraction(4 ** am, 4 ** ap + 4 ** am)
                    out[(b, c)] = pc * pb
        return out
    Lbc, Lcb = law_bc("bc"), law_bc("cb")
    res = {}
    for lb, lc in [(1, 4), (1, 1), (4, 1), (10, 40), (40, 10), (1000, 1000)]:
        pbc = Fraction(lb, lb + lc)
        law = {k: pbc * Lbc[k] + (1 - pbc) * Lcb[k] for k in Lbc}
        res[f"lam_b={lb},lam_c={lc}"] = dict(ratio=lb / lc, P_b_plus_c_plus=float(law[(1, 1)]), P_b_plus=float(law[(1, 1)] + law[(1, -1)]))
    print("C", json.dumps(res, indent=1))
    return res

# ----------------------------------------------------------------- TEST D
def test_D(Ls=(4, 6, 8, 10, 16, 24), reps=20, seed=1):
    rng = np.random.default_rng(seed)
    res = {}
    for L in Ls:
        N = L ** 3
        coords = np.array(list(itertools.product(range(L), repeat=3)))
        idx = lambda x, y, z: (x % L) * L * L + (y % L) * L + (z % L)
        nbr = np.zeros((N, 6), dtype=np.int64)
        for i, (x, y, z) in enumerate(coords):
            nbr[i] = [idx(x + 1, y, z), idx(x - 1, y, z), idx(x, y + 1, z), idx(x, y - 1, z), idx(x, y, z + 1), idx(x, y, z - 1)]
        def depth(label):
            order = np.argsort(label, kind="stable")
            d = np.ones(N, dtype=np.int64)
            for v in order:
                m = 0
                for u in nbr[v]:
                    if label[u] < label[v] and d[u] > m: m = d[u]
                d[v] = m + 1
            return int(d.max())
        iid = [depth(rng.random(N)) for _ in range(reps)]
        parity = (coords.sum(axis=1) % 2).astype(float)
        checker = depth(parity + 1e-6 * rng.random(N))       # even before odd
        lex = depth(np.arange(N, dtype=float))               # lexicographic sweep
        res[f"L={L}"] = dict(N=N, iid_mean=float(np.mean(iid)), iid_max=max(iid), checkerboard=checker, lexicographic=lex)
        print("D", L, res[f"L={L}"], flush=True)
    return res

# ----------------------------------------------------------------- TEST E (hops on a ring)
def test_E(N=12, K=0.7, npart=4):
    states = [sum(1 << i for i in c) for c in itertools.combinations(range(N), npart)]
    sidx = {s: i for i, s in enumerate(states)}; S = len(states)
    occ = lambda s, i: (s >> (i % N)) & 1
    energy = lambda s: -K * sum(occ(s, i) * occ(s, i + 1) for i in range(N))
    w = np.array([np.exp(-energy(s)) for s in states]); pi = w / w.sum()
    def swap(s, b):
        i, j = b % N, (b + 1) % N
        if occ(s, i) == occ(s, j): return None
        return s ^ ((1 << i) | (1 << j))
    def M(b):  # Metropolis single-bond move, stochastic matrix
        T = np.zeros((S, S))
        for s in states:
            t = swap(s, b); i = sidx[s]
            if t is None: T[i, i] = 1.0; continue
            a = 1.0 / (1.0 + np.exp(energy(t) - energy(s)))  # heat-bath (Glauber) acceptance, always <1
            T[i, sidx[t]] += a; T[i, i] += 1 - a
        return T
    Ms = [M(b) for b in range(N)]
    def stat(T):
        # solve v (T - I) = 0, sum v = 1 (least squares); also report the number of unit eigenvalues
        Aeq = np.vstack([(T.T - np.eye(S)), np.ones((1, S))]); b = np.zeros(S + 1); b[-1] = 1
        v = np.linalg.lstsq(Aeq, b, rcond=None)[0]
        return v
    tv = lambda a, b: 0.5 * float(np.abs(a - b).sum())
    res = {}
    # commutation of bond moves
    comm = {}
    for d in range(1, 6):
        comm[f"dist={d}"] = float(np.abs(Ms[0] @ Ms[d] - Ms[d] @ Ms[0]).max())
    res["commutator_max_abs_by_bond_distance"] = comm
    # S: random sequential
    TS = sum(Ms) / N
    n1 = lambda T: int(np.sum(np.abs(np.linalg.eigvals(T) - 1) < 1e-9))
    res["unit_eigenvalues(random_seq, colour3, simultaneous)"] = None
    res["random_sequential_TV_to_Gibbs"] = tv(stat(TS), pi)
    # C3: colour classes mod 3, each a product of commuting moves
    def cls(c):
        T = np.eye(S)
        for b in range(N):
            if b % 3 == c: T = T @ Ms[b]
        return T
    TC = cls(0) @ cls(1) @ cls(2)
    res["colour3_sweep_TV_to_Gibbs"] = tv(stat(TC), pi)
    # P: simultaneous updating of all even bonds, then all odd bonds, each bond deciding on PRE-update energies
    def sim(parity):
        T = np.zeros((S, S))
        bonds = [b for b in range(N) if b % 2 == parity]
        for s in states:
            i = sidx[s]
            props = []
            for b in bonds:
                t = swap(s, b)
                a = 0.0 if t is None else 1.0 / (1.0 + np.exp(energy(t) - energy(s)))
                props.append((b, a, t is not None))
            active = [(b, a) for b, a, ok in props if ok]
            for mask in itertools.product((0, 1), repeat=len(active)):
                pr = 1.0; t = s
                for (b, a), m in zip(active, mask):
                    pr *= a if m else 1 - a
                    if m: t = t ^ ((1 << (b % N)) | (1 << ((b + 1) % N)))
                T[i, sidx[t]] += pr
        return T
    TP = sim(0) @ sim(1)
    res["simultaneous_even_odd_TV_to_Gibbs"] = tv(stat(TP), pi)
    # single simultaneous class of pairwise-independent bonds (distance>=3) = sequential
    res["unit_eigenvalues(random_seq, colour3, simultaneous)"] = [n1(TS), n1(TC), n1(TP)]
    res["pi_is_invariant_residuals"] = [float(np.abs(pi @ TS - pi).max()), float(np.abs(pi @ TC - pi).max()), float(np.abs(pi @ TP - pi).max())]
    print("E", json.dumps(res, indent=1))
    return res

if __name__ == "__main__":
    which = sys.argv[1:] or ["A", "B", "C", "D", "E"]
    gA = None
    if "A" in which or "B" in which:
        OUT["A"], gA = test_A()
    if "B" in which: OUT["B"] = test_B(gA)
    if "C" in which: OUT["C"] = test_C()
    if "D" in which: OUT["D"] = test_D()
    if "E" in which: OUT["E"] = test_E()
    json.dump(OUT, open("test_T11_results.json", "w"), indent=1, default=str)
