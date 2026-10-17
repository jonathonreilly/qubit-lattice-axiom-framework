"""C13 independent check, part (4): attack on 'minimal orbit four is a statement
about the bare site action only'.

(a) Edge model (one qubit per edge, the orbit note's own model): a
    vertex-centred CZ network composed with the bare edge permutation makes
    every one of the 60 codes O-invariant (both uniform sectors), and maps
    the code of any ordering o to the code of any other ordering o'.
(b) Half-edge model: the on-site CZ network V_{o->o'} maps code(o) to
    code(o') for all 8 sectors; so under on-site Cliffords the 60 codes are
    one class.
(c) Pair test (exploratory) under the honest on-site action U_R (eps=1) and
    under other consistent lifts, plus a bare P_R calibration.
"""
import itertools, json, random
from collections import Counter
import numpy as np
from model import HalfEdge, Edge, ROTS, rot_dir, rot_order, classify_rotation, compose_images
from paulialg import apply_clifford, mul, dag, SignedGroup, is_herm

random.seed(3)
info = json.load(open("codes.json"))["info"]
REPS = {sz: next(x for x in info if x["orbit_size"] == sz) for sz in (4, 6, 12)}
SECTORS = [(0, 0, 0), (1, 1, 1)]
ALLSEC = list(itertools.product((0, 1), repeat=3))
kinds = [classify_rotation(M) for M in ROTS]
out = {}


def log(*a):
    print(*a, flush=True)


def all_in(G, gens, imgs):
    return all(G.status(apply_clifford(g, *imgs)) == "in" for g in gens)


# (a) edge model, all 60 codes, L = 4 (full generator check), L = 6 reps
for L in (4, 6):
    codes = info if L == 4 else list(REPS.values())
    ok = tot = bare_ok = 0
    for x in codes:
        o = tuple(x["rep"])
        E = Edge(L, o)
        for sec in SECTORS:
            G = E.group(sec)
            assert not G.minus_one and E.n - G.rank == 3
            gens = [g for _, _, g in E.generators(sec)]
            for M in ROTS:
                Ro = rot_order(M, o)
                bare = E.bare_images(M)
                partners, inv = E.cz_partners(Ro, o)
                cz = E.cz_images(partners)
                U = compose_images(bare, cz, E.n)
                tot += 1
                ok += all_in(G, gens, U)
                bare_ok += all_in(G, gens, bare)
    log(f"edge model L={L}: CZ-network o bare permutation preserves signed group in {ok}/{tot} "
        f"(code, sector, R) cases; bare permutation alone: {bare_ok}/{tot}")
    out[f"edge_cz_L{L}"] = dict(ok=ok, tot=tot, bare_ok=bare_ok)

# CZ gate count per vertex for the rotated-ordering correction (locality data)
E = Edge(4, tuple(REPS[4]["rep"]))
ncz = Counter(len(E.cz_partners(rot_order(M, E.o), E.o)[1]) for M in ROTS)
log("CZ gates per vertex needed (D3 rep), distribution over 24 R:", dict(ncz))

# (b) all orderings are on-site-CZ equivalent: random pairs, edge and half-edge, all 8 sectors
okE = okH = tot = 0
orders = list(itertools.permutations(range(6)))
for _ in range(40):
    o, o2 = random.sample(orders, 2)
    E, E2 = Edge(4, o), Edge(4, o2)
    H, H2 = HalfEdge(4, o), HalfEdge(4, o2)
    for sec in ALLSEC:
        tot += 1
        G2 = E2.group(sec)
        partners, _ = E.cz_partners(o, o2)
        okE += all_in(G2, [g for _, _, g in E.generators(sec)], E.cz_images(partners))
        # half-edge on-site CZ
        GH2 = H2.group(sec)
        pf, pt = H.pos, H2.pos
        inv = [(d, e) for d in range(6) for e in range(d + 1, 6) if (pf[d] < pf[e]) != (pt[d] < pt[e])]
        part = [0] * H.n
        for s in range(H.lat.N):
            for d, e in inv:
                part[H.q(s, d)] ^= 1 << H.q(s, e); part[H.q(s, e)] ^= 1 << H.q(s, d)
        from paulialg import Z
        imgs = ([(1 << q, part[q], 0) for q in range(H.n)], [Z(q) for q in range(H.n)])
        okH += all_in(GH2, [g for _, _, g in H.generators(sec)], imgs)
log(f"code(o,s) -> code(o',s) under vertex CZ network: edge {okE}/{tot}, half-edge on-site {okH}/{tot} (40 random pairs x 8 sectors)")
out["cz_equivalence"] = dict(edge=okE, half=okH, tot=tot)


# (c) pair test
def hop(H, u, d):
    if d < 3:
        return H.A(u, d)
    return H.A(H.lat.shift(u, d), d - 3)


def path_string(H, x, y, axis_order):
    """Product of hops from unwrapped point x to unwrapped point y."""
    cur = list(x)
    S = (0, 0, 0)
    for a in axis_order:
        while cur[a] != y[a]:
            d = a if y[a] > cur[a] else a + 3
            S = mul(S, hop(H, H.lat.site(tuple(cur)), d))
            cur[a] += 1 if d < 3 else -1
    return S


def lam(H, G, imgs, M, x, axis_order):
    Rx = tuple(int(c) for c in M @ np.array(x))
    S = path_string(H, x, Rx, axis_order)
    SR = apply_clifford(S, *imgs)
    return G.status(mul(dag(S), SR))


L = 8
C2s = [j for j in range(24) if kinds[j].startswith("C2")]
xs = [(1, 2, 0), (2, 0, 1), (0, 1, 3), (-1, 2, 1)]
for sz, rep in REPS.items():
    o = tuple(rep["rep"])
    H = HalfEdge(L, o)
    bare_stab = [j for j in range(24) if rot_order(ROTS[j], o) in
                 [tuple(r["rep"]) for r in [rep]] or False]
    for sec in SECTORS:
        G = H.group(sec)
        row = {}
        for j in C2s:
            M = ROTS[j]
            U = H.majorana_images(M)
            vals = Counter()
            for x in xs:
                Rx = tuple(int(c) for c in M @ np.array(x))
                if Rx == x:
                    continue
                for ao in [(0, 1, 2), (2, 1, 0), (1, 0, 2)]:
                    vals[lam(H, G, U, M, x, ao)] += 1
            # bare calibration (only meaningful if the bare map preserves the group)
            B = H.bare_images(M)
            gens = [g for _, _, g in H.generators(sec, sites=[0])]
            bare_sym = all_in(G, gens, B)
            bvals = Counter()
            if bare_sym:
                for x in xs:
                    Rx = tuple(int(c) for c in M @ np.array(x))
                    if Rx == x:
                        continue
                    for ao in [(0, 1, 2), (2, 1, 0), (1, 0, 2)]:
                        bvals[lam(H, G, B, M, x, ao)] += 1
            row[f"R{j}:{kinds[j]}"] = dict(U=dict(vals), bare=dict(bvals) if bare_sym else "not a bare symmetry")
        log(f"pair test L={L} orbit{sz} sector{sec}:")
        for k, v in row.items():
            log("   ", k, v)
        out[f"pair_orb{sz}_sec{sec}"] = row

# (c') lift dependence: other consistent group actions (from check_grouplaw rules)
perm_of = []
for M in ROTS:
    pd = [rot_dir(M, d) for d in range(6)]
    perm_of.append(tuple(pd + [6 + x for x in pd]))
IDP = tuple(range(12)); MINUS = (IDP, 4095)


def compose(a, b):
    pa, Ta = a; pb, Tb = b
    p = tuple(pb[pa[i]] for i in range(12))
    T = 0
    for i in range(12):
        if ((Ta >> i) ^ (Tb >> pa[i])) & 1:
            T |= 1 << i
    return (p, T)


def closure(gens, cap=48):
    elems = {(IDP, 0)}; fr = [(IDP, 0)]
    while fr:
        nf = []
        for e in fr:
            for g in gens:
                h = compose(e, g)
                if h not in elems:
                    elems.add(h); nf.append(h)
                    if len(elems) > cap:
                        return None
        fr = nf
    return elems


adm = [T for T in range(4096) if all(((T >> a) ^ (T >> (a + 6)) ^ (T >> (a + 3)) ^ (T >> (a + 9))) & 1 == 0 for a in range(3))]
jC4 = next(j for j, M in enumerate(ROTS) if kinds[j] == "C4" and M[2, 2] == 1)
jC3 = next(j for j, M in enumerate(ROTS) if kinds[j] == "C3" and np.array_equal(M @ np.array([1, 1, 1]), np.array([1, 1, 1])))
samples = {"24 honest": [], "48 edge-1": [], "48 edge+1": []}
random.shuffle(adm)
for T4 in adm:
    for T3 in adm[:64]:
        Gp = closure([(perm_of[jC4], T4), (perm_of[jC3], T3)])
        if Gp is None:
            continue
        ker = {e for e in Gp if e[0] == IDP}
        if len(Gp) == 24 and len(ker) == 1:
            cat = "24 honest"
        elif len(Gp) == 48 and ker == {(IDP, 0), MINUS}:
            e = next(e for e in Gp if e[0] != IDP and kinds[perm_of.index(e[0])] == "C2edge")
            cat = "48 edge-1" if compose(e, e) == MINUS else "48 edge+1"
        else:
            continue
        if len(samples[cat]) < 4:
            samples[cat].append(Gp)
    if all(len(v) >= 4 for v in samples.values()):
        break

o = tuple(REPS[4]["rep"])
H = HalfEdge(L, o)
lift_res = {}
for sec in SECTORS:
    G = H.group(sec)
    for cat, groups in samples.items():
        for gi, Gp in enumerate(groups):
            res = Counter()
            for e in Gp:
                if e[0] == IDP:
                    continue
                j = perm_of.index(e[0])
                if not kinds[j].startswith("C2"):
                    continue
                T = e[1]
                eps = [(-1) ** (T >> i & 1) for i in range(12)]
                U = H.majorana_images(ROTS[j], eps[:6], eps[6:])
                M = ROTS[j]
                for x in xs[:2]:
                    Rx = tuple(int(c) for c in M @ np.array(x))
                    if Rx == x:
                        continue
                    res[(kinds[j], lam(H, G, U, M, x, (0, 1, 2)))] += 1
            lift_res[f"{sec} {cat} #{gi}"] = dict(res)
            log(f"lift dependence D3 rep sector{sec} {cat} #{gi}: {dict(res)}")
out["lift_dependence"] = {k: {str(a): b for a, b in v.items()} for k, v in lift_res.items()}
json.dump(out, open("check_attack_results.json", "w"), indent=1, default=str)
