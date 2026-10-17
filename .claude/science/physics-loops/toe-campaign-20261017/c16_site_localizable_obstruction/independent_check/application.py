#!/usr/bin/env python3
"""Independent check of item 5 (application), written from scratch.

Part A (half-edge model, L=4, Paulis with phases): B_v about the fixed site v=0 is
mapped to +B_v by the bare site permutation P_R and by V_R P_R (V_R = on-site CZ network
on direction pairs whose relative order differs between o and Ro); V_R P_R maps every
generator (B, R, S^o) to + a generator.
Part B (edge BKSF model): classify the 60 codes, their stabilizers; for the BARE permutation
test whether P_R maps the term set {B} u {S^o_p} onto itself and whether the clean
single-fermion pattern at v (only B_v violated w.r.t. H^o) is P_R-invariant.
"""
import itertools, sys
import numpy as np

DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
DIDX = {d: i for i, d in enumerate(DIRS)}
POS = {0: 0, 1: 2, 2: 4}  # +a index for axis a

O = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1:
            O.append(M)
def rtype(M):
    if np.array_equal(M, np.eye(3, dtype=int)): return "e"
    t = int(np.trace(M))
    if t == -1: return "C2axis" if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else "C2edge"
    return {0: "C3", 1: "C4"}[t]
TYPES = [rtype(M) for M in O]
def Rdir(M, d):
    return DIDX[tuple(int(x) for x in M @ np.array(DIRS[d]))]

out = []
def report(s):
    print(s); sys.stdout.flush(); out.append(s)

# ------------------------------------------------------------ Pauli with phase: i^k X^x Z^z
class Pauli:
    def __init__(self, n, x=None, z=None, k=0):
        self.x = np.zeros(n, bool) if x is None else x.copy()
        self.z = np.zeros(n, bool) if z is None else z.copy()
        self.k = k % 4
    def __mul__(self, o):
        # X^x1 Z^z1 X^x2 Z^z2 = (-1)^{z1.x2} X^{x1+x2} Z^{z1+z2}
        s = int(np.sum(self.z & o.x)) % 2
        return Pauli(len(self.x), self.x ^ o.x, self.z ^ o.z, self.k + o.k + 2 * s)
    def eq(self, o):
        return np.array_equal(self.x, o.x) and np.array_equal(self.z, o.z) and self.k == o.k
    def eq_unsigned(self, o):
        return np.array_equal(self.x, o.x) and np.array_equal(self.z, o.z)
    def permute(self, pi):  # qubit q -> pi[q]
        x = np.zeros_like(self.x); z = np.zeros_like(self.z)
        x[pi] = self.x; z[pi] = self.z
        return Pauli(len(x), x, z, self.k)
    def cz(self, a, b):
        x, z = self.x.copy(), self.z.copy()
        k = self.k + 2 * (int(x[a]) * int(x[b]))
        if x[a]: z[b] ^= True
        if x[b]: z[a] ^= True
        return Pauli(len(x), x, z, k)

# ------------------------------------------------------------ Part A: half-edge model
def halfedge(L, o):
    rank = {d: i for i, d in enumerate(o)}
    sites = list(itertools.product(range(L), repeat=3))
    sidx = {v: i for i, v in enumerate(sites)}
    n = 6 * len(sites)
    q = lambda v, d: 6 * sidx[tuple(c % L for c in v)] + d
    add = lambda v, a: tuple((v[i] + (1 if i == a else 0)) % L for i in range(3))
    def A(v, a):
        P = Pauli(n); w = add(v, a); pa, ma = POS[a], POS[a] + 1
        P.x[q(v, pa)] = True; P.x[q(w, ma)] = True
        for d in range(6):
            if rank[d] < rank[pa]: P.z[q(v, d)] = True
            if rank[d] < rank[ma]: P.z[q(w, d)] = True
        return P
    B = {}
    for v in sites:
        P = Pauli(n); P.z[[q(v, d) for d in range(6)]] = True; B[v] = P
    Rr = {}
    for v in sites:
        for a in range(3):
            P = Pauli(n); P.z[q(v, POS[a])] = True; P.z[q(add(v, a), POS[a] + 1)] = True; Rr[(v, a)] = P
    S = {}
    for v in sites:
        for a, b in [(0, 1), (0, 2), (1, 2)]:
            S[(v, a, b)] = A(v, a) * A(add(v, a), b) * A(add(v, b), a) * A(v, b)
    return dict(n=n, sites=sites, q=q, B=B, R=Rr, S=S, A=A, rank=rank)

def site_perm(L, M, sites, q):
    pi = np.zeros(6 * len(sites), int)
    for v in sites:
        Rv = tuple(int(c) % L for c in M @ np.array(v))
        for d in range(6):
            pi[q(v, d)] = q(Rv, Rdir(M, d))
    return pi

def part_A(L=4, orderings=None):
    if orderings is None:
        orderings = [(0, 1, 2, 3, 4, 5), (2, 4, 0, 5, 1, 3), (5, 0, 3, 1, 4, 2)]
    nfail_bare_B = nfail_cl_B = nfail_cl_gen = 0; ncheck = 0
    for o in orderings:
        m = halfedge(L, o)
        for Mi, M in enumerate(O):
            pi = site_perm(L, M, m["sites"], m["q"])
            Ro = tuple(Rdir(M, d) for d in o)
            rk_o = m["rank"]; rk_Ro = {d: i for i, d in enumerate(Ro)}
            flips = [(d, e) for d in range(6) for e in range(d + 1, 6)
                     if (rk_o[d] < rk_o[e]) != (rk_Ro[d] < rk_Ro[e])]
            def U(P):
                P = P.permute(pi)
                supp = {qq // 6 for qq in np.nonzero(P.x | P.z)[0]}
                for v in [m["sites"][si] for si in sorted(supp)]:
                    for d, e in flips:
                        P = P.cz(m["q"](v, d), m["q"](v, e))
                return P
            v0 = (0, 0, 0)
            # bare permutation on B_v0
            if not m["B"][v0].permute(pi).eq(m["B"][v0]): nfail_bare_B += 1
            if not U(m["B"][v0]).eq(m["B"][v0]): nfail_cl_B += 1
            # every generator -> +generator under V_R P_R (sample: all generators near origin + random)
            gens = []
            for v in m["sites"]:
                if max(min(c, L - c) for c in v) <= 1:
                    gens.append(("B", v)); gens += [("R", (v, a)) for a in range(3)]
                    gens += [("S", (v, a, b)) for a, b in [(0, 1), (0, 2), (1, 2)]]
            allgen = [("B", k) for k in m["B"]] + [("R", k) for k in m["R"]] + [("S", k) for k in m["S"]]
            for typ, k in gens:
                img = U(m[typ][k])
                ok = any(img.eq(m[t2][k2]) for t2, k2 in allgen if t2 == typ)
                ncheck += 1
                if not ok: nfail_cl_gen += 1
    report(f"[A] half-edge L={L}, {len(orderings)} orderings x 24 rotations about v=0:")
    report(f"[A]   bare P_R: B_v -> +B_v failures: {nfail_bare_B}")
    report(f"[A]   V_R P_R:  B_v -> +B_v failures: {nfail_cl_B}")
    report(f"[A]   V_R P_R:  generator -> +generator (same type) failures: {nfail_cl_gen} of {ncheck} checks")

# ------------------------------------------------------------ Part B: edge BKSF model (GF(2), unsigned)
def edge_model(L, o):
    rank = {d: i for i, d in enumerate(o)}
    sites = list(itertools.product(range(L), repeat=3))
    sidx = {v: i for i, v in enumerate(sites)}
    ne = 3 * len(sites)
    mod = lambda v: tuple(c % L for c in v)
    def edge_of(v, d):  # edge at v in direction d
        a = d // 2
        if d % 2 == 0: return 3 * sidx[mod(v)] + a
        w = list(v); w[a] -= 1
        return 3 * sidx[mod(w)] + a
    add = lambda v, a: mod(tuple(v[i] + (1 if i == a else 0) for i in range(3)))
    def A(v, a):  # returns (xset, zset)
        w = add(v, a); pa, ma = POS[a], POS[a] + 1
        X = {edge_of(v, pa)}; Z = set()
        for d in range(6):
            if rank[d] < rank[pa]: Z ^= {edge_of(v, d)}
            if rank[d] < rank[ma]: Z ^= {edge_of(w, d)}
        return X, Z
    def toint(X, Z):
        r = 0
        for e in X: r |= 1 << e
        for e in Z: r |= 1 << (ne + e)
        return r
    B = {v: toint(set(), {edge_of(v, d) for d in range(6)}) for v in sites}
    Aint = {(v, a): toint(*A(v, a)) for v in sites for a in range(3)}
    S = {}
    for v in sites:
        for a, b in [(0, 1), (0, 2), (1, 2)]:
            S[(v, a, b)] = Aint[(v, a)] ^ Aint[(add(v, a), b)] ^ Aint[(add(v, b), a)] ^ Aint[(v, b)]
    return dict(ne=ne, sites=sites, sidx=sidx, B=B, S=S, A=Aint, edge_of=edge_of, add=add)

def rref(vecs):
    piv = {}
    for v in vecs:
        while v:
            h = v.bit_length() - 1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; break
    # full reduction
    for h in sorted(piv):
        for h2 in piv:
            if h2 > h and (piv[h2] >> h) & 1:
                piv[h2] ^= piv[h]
    return tuple(sorted(piv.values()))

def edge_perm_int(L, M, m, x):
    """Bare permutation of edge qubits (as undirected edges) applied to an int-encoded Pauli."""
    ne = m["ne"]; res = 0
    cache = m.setdefault("_pi", {})
    key = tuple(M.flatten())
    if key not in cache:
        pi = [0] * ne
        for v in m["sites"]:
            for a in range(3):
                e = m["edge_of"](v, 2 * a)
                Rv = tuple(int(c) % L for c in M @ np.array(v))
                pi[e] = m["edge_of"](Rv, Rdir(M, 2 * a))
        cache[key] = pi
    pi = cache[key]
    for e in range(ne):
        if (x >> e) & 1: res |= 1 << pi[e]
        if (x >> (ne + e)) & 1: res |= 1 << (ne + pi[e])
    return res

def symp(a, b, ne):
    mask = (1 << ne) - 1
    ax, az, bx, bz = a & mask, a >> ne, b & mask, b >> ne
    return (bin(ax & bz).count("1") + bin(az & bx).count("1")) % 2

def part_B(L=4, Lpat=8):
    orders = list(itertools.permutations(range(6)))
    codes = {}
    models = {}
    for o in orders:
        m = edge_model(L, o); models[o] = m
        key = rref(list(m["B"].values()) + list(m["S"].values()))
        codes.setdefault(key, []).append(o)
    report(f"[B] edge BKSF L={L}: {len(orders)} orderings -> {len(codes)} distinct codes; "
           f"orderings per code: {sorted({len(v) for v in codes.values()})}")
    code_of = {o: k for k, os_ in codes.items() for o in os_}
    # intertwining check on a sample: P_R(A^o_e) == A^{Ro}_{Re}
    bad = 0
    for o in orders[::97]:
        for M in O:
            Ro = tuple(Rdir(M, d) for d in o)
            m, mR = models[o], models[Ro]
            for (v, a), x in list(m["A"].items())[::7]:
                img = edge_perm_int(L, M, m, x)
                if img not in set(mR["A"].values()): bad += 1
    report(f"[B] intertwining P_R A^o_e = A^(Ro)_(Re) (sampled): failures {bad}")
    # stabilizers
    stab = {}
    for k, os_ in codes.items():
        o = os_[0]
        stab[k] = [i for i, M in enumerate(O) if code_of[tuple(Rdir(M, d) for d in o)] == k]
    from collections import Counter
    report(f"[B] stabilizer orders: {dict(Counter(len(s) for s in stab.values()))}")
    # term-set test (bare P_R): exists ordering in class with {S^{Ro}} == {S^o}?
    summary = Counter(); pairs_clean = Counter(); pair_total = Counter()
    full_inv = Counter()
    for k, os_ in codes.items():
        st = stab[k]; n = len(st)
        stype = {6: "D3", 4: "D2", 2: "C2"}[n]
        preserved_by = {}
        for o in os_:
            Sset = set(models[o]["S"].values())
            pres = []
            for i in st:
                Ro = tuple(Rdir(O[i], d) for d in o)
                if set(models[Ro]["S"].values()) == Sset: pres.append(i)
            preserved_by[o] = pres
        c2s = [i for i in st if TYPES[i].startswith("C2")]
        for i in c2s:
            pair_total[stype] += 1
            if any(i in preserved_by[o] for o in os_): pairs_clean[stype] += 1
        if any(len(p) == n for p in preserved_by.values()): full_inv[stype] += 1
        summary[stype] += 1
    report(f"[B] codes by stabilizer: {dict(summary)}")
    report(f"[B] (code,C2) pairs where SOME ordering's plaquette term set is P_R-invariant: "
           f"{dict(pairs_clean)} of {dict(pair_total)}")
    report(f"[B] codes with an ordering whose term set {{B}}u{{S^o}} is invariant under the WHOLE stabilizer (bare P_R): "
           f"{dict(full_inv)} of {dict(summary)}")
    # clean single-fermion pattern test at L=Lpat: hop string E^o from v=0 to w=(Lpat/2,0,0)
    rep_codes = {}
    for k, os_ in codes.items():
        stype = {6: "D3", 4: "D2", 2: "C2"}[len(stab[k])]
        rep_codes.setdefault(stype, []).append(k)
    res = Counter(); tot = Counter()
    for stype, ks in rep_codes.items():
        for k in ks[:4]:
            for o in codes[k][:3]:
                m = edge_model(Lpat, o)
                E = 0
                for t in range(Lpat // 2):
                    E ^= m["A"][((t, 0, 0), 0)]
                ne = m["ne"]
                # verify E syndrome under H^o: only B_0 and B_w
                viol = [v for v, b in m["B"].items() if symp(E, b, ne)]
                violS = [p for p, s in m["S"].items() if symp(E, s, ne)]
                assert sorted(viol) == sorted([(0, 0, 0), (Lpat // 2, 0, 0)]) and not violS, (viol, violS)
                for i in stab[k]:
                    if TYPES[i] == "e": continue
                    img = edge_perm_int(Lpat, O[i], m, E)
                    near = [p for p, s in m["S"].items()
                            if max(min(c, Lpat - c) for c in p[0]) <= 2 and symp(img, s, ne)]
                    tot[(stype, TYPES[i])] += 1
                    if near: res[(stype, TYPES[i])] += 1
    report(f"[B] bare P_R, L={Lpat}: clean fermion at v (only B_v violated w.r.t. H^o) mapped to a pattern with "
           f"plaquette violations within distance 2 of v, count/(tested) by (stabilizer, element):")
    for key in sorted(tot):
        report(f"[B]    {key}: {res[key]}/{tot[key]}")

if __name__ == "__main__":
    part_A()
    part_B()
    open(__file__.replace("application.py", "application.out"), "w").write("\n".join(out) + "\n")
