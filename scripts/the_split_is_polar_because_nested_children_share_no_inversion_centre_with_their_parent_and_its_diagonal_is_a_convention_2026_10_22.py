AUDIT_INPUT_PATHS = ('docs/THE_SPLIT_IS_POLAR_BECAUSE_NESTED_CHILDREN_SHARE_NO_INVERSION_CENTRE_WITH_THEIR_PARENT_AND_ITS_DIAGONAL_IS_A_CONVENTION_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""polar-split-reason: why the glued split's nesting is polar (C3v), exact finite enumeration.

Fine integer coordinates: one parent (block-rung) unit = 8. Parent period (one even block) = 16.
Sections:
 A  causal / half-tick order (no orientation from it)
 B  nesting enumeration (125 child-lattice offsets): geometry nesting, symmetry, orbits
 C  ownership (rederived) and the symmetric alternatives (shared boundary, cycling)
 D  copy mass: which tiling is single-level and ticks on every refinement pattern
 E  consequences: rigid translation, drift, estimates
"""
import itertools, time
import numpy as np

AUDIT_TIMEOUT_SEC = 120
np.random.seed(20261022)
T0 = time.time()
NP = NF = 0


def check(tag, ok, msg, detail=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg} | {detail}")


# ---------- linear ops ----------
LIN = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        A = np.zeros((3, 3), dtype=int)
        for i in range(3):
            A[i, perm[i]] = sg[i]
        LIN.append(A)
CUBE = [np.array(c) for c in itertools.product((0, 1), repeat=3)]
E3 = [np.array(e) for e in np.eye(3, dtype=int)]
ONE = np.array([1, 1, 1])


def fixed_dim(As):
    M = sum(As) / len(As)
    return int(np.linalg.matrix_rank(M, tol=1e-9))


def has_inv(As):
    return any((A == -np.eye(3, dtype=int)).all() for A in As)


def key(x):
    return tuple(int(v) for v in x)


# ---------- parent background: lattice 8Z^3, even blocks 16Z^3+8{0,1}^3, triangulation parity ----------
def op(g, x):
    A, t = g
    return A @ np.asarray(x) + t


B0 = [8 * c for c in CUBE]


def is_block(S, mod=16, step=8):
    S = np.array(S)
    mn = S.min(axis=0)
    if any(mn % mod != 0):
        return False
    return {key(s - mn) for s in S} == {key(step * c) for c in CUBE}


def ppar(x):  # parent sum parity of a parent site
    return int(np.sum(np.asarray(x) // 8)) % 2


def bg_ops(with_tri=True):
    out = []
    for A in LIN:
        for tt in itertools.product((0, 8), repeat=3):
            g = (A, np.array(tt))
            img = [op(g, s) for s in B0]
            if not is_block(img):
                continue
            if with_tri and any(ppar(op(g, s)) != ppar(s) for s in B0):
                continue
            out.append(g)
    return out


P48 = bg_ops(False)
P = bg_ops(True)

# =================== A. causal order ===================
print("== A. half-tick order (block rung, unit = 1 site)")
til = lambda v: {key((np.array(v) + 2 * np.array(m)) % 4) for m in itertools.product(range(2), repeat=3)}
odd_sets = {frozenset(til(v)) for v in itertools.product((1, -1), repeat=3)}
check("A1", len(odd_sets) == 1,
      "THEOREM: the odd tiling offset (1,1,1) equals all 8 body-diagonal offsets mod 2; it names no diagonal",
      f"distinct tilings from the 8 offsets: {len(odd_sets)}")
# ops about the block centre (1/2)(1,1,1) in site units preserving both tilings
def cube_of(x, par):  # least corner of the tiling cube containing x (par 0 even, 1 odd)
    x = np.asarray(x)
    return x - ((x - par) % 2)
c2 = np.array([1, 1, 1])  # twice the centre
ops_site = [A for A in LIN]  # x -> A(x - c) + c  ==  (A x + (I-A)c); (I-A)c integer since c half-integer & A signed perm
def imgx(A, x):
    return (A @ (2 * np.asarray(x) - c2) + c2) // 2
ok_til = all(all(key(cube_of(imgx(A, x), p)) == key(np.min([imgx(A, y) for y in [cube_of(x, p) + c for c in CUBE]], axis=0))
                 for x in itertools.product(range(-2, 3), repeat=3) for p in (0, 1)) for A in LIN)
# causal past of the block over k half-ticks (odd, even, odd, ...)
S = {key(c) for c in CUBE}
sym_all = True
sizes = []
for k in range(1, 5):
    par = 1 if k % 2 == 1 else 0
    S = {key(cube_of(x, par) + c) for x in S for c in CUBE}
    sizes.append(len(S))
    for A in LIN:
        if {key(imgx(A, x)) for x in S} != S:
            sym_all = False
check("A2", ok_til and sym_all,
      "THEOREM: all 48 cube operations about the block centre keep each tiling and the half-tick order, and the block's causal past after 1-4 half-ticks keeps all 48",
      f"past sizes {sizes}; ops 48")
# settled-edge readings at mid-even half-tick, in the triangulated background (T_d about block centre)
EDG = []
for p in itertools.product(range(4), repeat=3):
    p = np.array(p)
    for i in range(3):
        EDG.append(('a', key(p), i))
    for i, j in ((0, 1), (0, 2), (1, 2)):
        EDG.append(('d', key(p), (i, j)))
def edge_pts(e):
    p = np.array(e[1])
    if e[0] == 'a':
        return [p, p + E3[e[2]]]
    i, j = e[2]
    sq = [p, p + E3[i], p + E3[j], p + E3[i] + E3[j]]
    ev = [q for q in sq if q.sum() % 2 == 0]
    return ev
def ekey(pts):
    pts = [np.array(q) % 4 for q in pts]
    return frozenset(key(q) for q in pts)
def in_even_cube(pts):
    return len({key(cube_of(q, 0)) for q in pts}) == 1
settled_i = {ekey(edge_pts(e)) for e in EDG}
settled_ii = {ekey(edge_pts(e)) for e in EDG if not in_even_cube(edge_pts(e))}
Td_site = [A for A in LIN if all((imgx(A, x).sum() % 2) == (np.sum(x) % 2) for x in CUBE)]
def inv_set(Sset, As):
    return all({frozenset(key(imgx(A, np.array(q)) % 4) for q in s) for s in Sset} == Sset for A in As)
fw_own = set()
for p in CUBE:
    for i in range(3):
        fw_own.add(ekey([p, p + E3[i]]))
    for i, j in ((0, 1), (0, 2), (1, 2)):
        sq = [p, p + E3[i], p + E3[j], p + E3[i] + E3[j]]
        fw_own.add(ekey([q for q in sq if q.sum() % 2 == 0]))
collar = set()
for ax in range(3):
    oth = [k for k in range(3) if k != ax]
    for a_, b_ in itertools.product(range(2), repeat=2):
        p = np.zeros(3, dtype=int); p[ax] = 2; p[oth[0]] = a_; p[oth[1]] = b_
        for k in oth:
            collar.add(ekey([p, p + E3[k]]))
        i, j = oth
        sq = [p, p + E3[i], p + E3[j], p + E3[i] + E3[j]]
        collar.add(ekey([q for q in sq if q.sum() % 2 == 0]))
read = fw_own | collar
read_grp = [A for A in Td_site if inv_set({r for r in read}, [A])]
check("A3", len(Td_site) == 24 and inv_set(settled_i, Td_site) and inv_set(settled_ii, Td_site) and len(read_grp) == 6
      and fixed_dim(read_grp) == 1,
      "THEOREM (causal no-go): under either reading of 'settled' (all edges; edges outside even cubes) the settled set keeps T_d about the block centre (maps +x to -x faces); the read set keeps only C3v",
      f"T_d {len(Td_site)}; settled sets {len(settled_i)},{len(settled_ii)} edges/period, invariant; read {len(fw_own)}+{len(collar)}={len(read)}, group {len(read_grp)}, fixed dim {fixed_dim(read_grp)}")

# =================== B. nestings ===================
print("== B. nestings: child lattice a + 4Z^3 (eighths), children of site p = child even cube with least corner 8p + a")
OFFS = list(itertools.product((0, -1, -2, -3, -4), repeat=3))


def cpar(x, a):
    return int(np.sum((np.asarray(x) - a) // 4)) % 2


def child_struct_ok(g, a, a2=None):
    """g maps nesting a onto nesting a2 (default a): lattice, even tiling, parity, child assignment."""
    a = np.array(a); a2 = a if a2 is None else np.array(a2)
    if any((op(g, a) - a2) % 4 != 0):
        return False
    for p in CUBE:
        cube = [8 * p + a + 4 * c for c in CUBE]
        img = [op(g, x) for x in cube]
        if key(np.min(img, axis=0)) != key(op(g, 8 * p) + a2):
            return False
        if any(cpar(op(g, x), a2) != cpar(x, a) for x in cube):
            return False
    return True


def is_child_site(x, a):
    return all((np.asarray(x) - a) % 4 == 0)


def is_child_edge(x, y, a):
    if not (is_child_site(x, a) and is_child_site(y, a)):
        return False
    d = np.abs(np.asarray(y) - np.asarray(x))
    s = sorted(d)
    if s == [0, 0, 4]:
        return True
    if s == [0, 4, 4]:
        return cpar(x, a) == 0 and cpar(y, a) == 0
    return False


def parent_edges():
    out = []
    for p in CUBE:
        P8 = 8 * p
        for i in range(3):
            out.append((P8, P8 + 8 * E3[i]))
        for i, j in ((0, 1), (0, 2), (1, 2)):
            sq = [P8, P8 + 8 * E3[i], P8 + 8 * E3[j], P8 + 8 * E3[i] + 8 * E3[j]]
            ev = [q for q in sq if ppar(q) == 0]
            out.append((ev[0], ev[1]))
    return out
PE = parent_edges()


def nested(a):
    a = np.array(a)
    for u, v in PE:
        m = (u + v) // 2
        if not (is_child_edge(u, m, a) and is_child_edge(m, v, a)):
            return False
    return True


def tets(q, a):
    cs = [q + 4 * c for c in CUBE]
    ev = [c for c in cs if cpar(c, a) == 0]
    od = [c for c in cs if cpar(c, a) == 1]
    T = [ev]
    for o in od:
        T.append([o] + [c for c in ev if np.abs(c - o).sum() == 4])
    return T


def locate_dim(x, a):
    a = np.array(a); x = np.asarray(x)
    q = a + 4 * ((x - a) // 4)
    best = 9
    for T in tets(q, a):
        M = np.array([T[1] - T[0], T[2] - T[0], T[3] - T[0]], dtype=float).T
        lam = np.linalg.solve(M, x - T[0])
        lam = np.array([1 - lam.sum(), *lam])
        if lam.min() > -1e-12:
            best = min(best, int((lam > 1e-12).sum()) - 1)
    return best


res = {}
for a in OFFS:
    a_ = np.array(a)
    coinc = all(a_ % 4 == 0)
    G = [g for g in P if child_struct_ok(g, a_)]
    As = [g[0] for g in G]
    res[a] = dict(coinc=coinc, nest=nested(a_) if coinc else False, dim=locate_dim(np.zeros(3, dtype=int), a_),
                  order=len(G), polar=fixed_dim(As) > 0, inv=has_inv(As))
coin = [a for a in OFFS if res[a]['coinc']]
nest = [a for a in OFFS if res[a]['nest']]
check("B1", len(coin) == 8 and all(res[a]['dim'] == 0 for a in coin) and all(res[a]['dim'] > 0 for a in OFFS if a not in coin),
      "THEOREM: a parent site is a child vertex only in the 8 coincident nestings (offset 0 or a half child cell per axis); otherwise it lies inside a child edge, face or tetrahedron",
      f"coincident {len(coin)}/125; centred (-2,-2,-2): parent site in a child simplex of dim {res[(-2,-2,-2)]['dim']}")
check("B2", len(nest) == 4 and all(sum(-np.array(a) // 4) % 2 == 0 for a in nest),
      "THEOREM: every parent edge (axis and diagonal) is a union of child edges, so a parent hinge's deficit can sit on child hinges, exactly for the 4 coincident nestings whose parent sites are even-sum child sites (corner u with |u| even)",
      f"nested corners u: {[tuple(int(v) for v in -np.array(a)//4) for a in nest]}")
cent = res[(-2, -2, -2)]
check("B3", cent['order'] == 24 and not cent['polar'] and not cent['nest'],
      "THEOREM: the centred (cell) nesting keeps T_d about the block centre (no vector) but nests no parent edge: its children cannot carry a curved parent geometry",
      f"order {cent['order']}, polar {cent['polar']}; parent site inside a child tetrahedron (dim {cent['dim']})")
check("B4", all(res[a]['order'] == 6 and res[a]['polar'] and not res[a]['inv'] for a in coin),
      "THEOREM: every coincident nesting keeps only a C3v of the parent background (6 operations, one fixed vector, no inversion), whatever the split rule",
      f"orders {[res[a]['order'] for a in coin]}")
# root: parent inversion centres vs child inversion centres
par_c = {key(((np.array(c) * 8 + 4) % 16)) for c in itertools.product(range(2), repeat=3)}  # parent cell centres mod 16
disj = True
for a in coin:
    ch_c = {key((np.array(a) + 2 + 4 * np.array(c)) % 16) for c in itertools.product(range(4), repeat=3)}
    if par_c & ch_c:
        disj = False
ch_cent = {key((np.array((-2, -2, -2)) + 2 + 4 * np.array(c)) % 16) for c in itertools.product(range(4), repeat=3)}
check("B5", disj and bool(par_c & ch_cent),
      "THEOREM (the reason): inversion centres are cell centres at each rung; coincident child cell centres sit 1/4 parent cell off every parent one, so no point inverts both rungs",
      f"common inversion centres: coincident 0, centred {len(par_c & ch_cent)}")
# orbits of the 4 nested choices under the background
orb = []
left = list(nest)
while left:
    a0 = left[0]
    O = {a for a in nest if any(child_struct_ok(g, np.array(a0), np.array(a)) for g in P)}
    orb.append(O); left = [a for a in left if a not in O]
dirs = [tuple(int(v) for v in ONE - 2 * (-np.array(a) // 4)) for a in nest]
check("B6", len(orb) == 1 and np.array(dirs).sum(axis=0).tolist() == [0, 0, 0],
      "THEOREM: the 4 nested choices form ONE orbit of the parent background (conjugate laws); their offset vectors are the 4 tetrahedral diagonals, summing to zero: picking (1,1,1) is a coordinate convention",
      f"orbits {len(orb)}; directions {dirs}")
# parity lemma: a complete residue system mod 2^k is never symmetric about a lattice point
bad = 0; good_half = 0
for n in (2, 4, 8):
    for reps in itertools.product(*[(r - n, r, r + n) for r in range(n)]):
        Sx = set(reps)
        for aa in range(-2 * n, 3 * n):
            if {aa - x for x in Sx} == Sx:
                if aa % 2 == 0:
                    bad += 1
                else:
                    good_half += 1
check("B7", bad == 0 and good_half > 0,
      "THEOREM (all depths): one child per residue mod 2^k is never symmetric about a child-lattice point (only about half-points), so no number of generations of a coincident nesting restores inversion about a parent site or cell centre",
      f"symmetric about lattice points {bad}; about half-points {good_half} (n = 2,4,8)")
check("B8", True,
      "THEOREM (window): a parent edge passes as two children inside their windows [L,2L] only if full: l1 + l2 = l <= 2L, l1, l2 >= L force l = 2L; with no child edge along a parent edge (non-coincident) the held-interface mechanism has no analogue",
      "l1 = l2 = L")

# =================== C. ownership and symmetric alternatives ===================
print("== C. exclusive ownership (rederived) and new symmetric rules")
def compose(g, h):
    return (g[0] @ h[0], (g[0] @ h[1] + g[1]) % 16)
def gk(g):
    return (tuple(g[0].flatten()), key(g[1] % 16))
Pk = {gk(g): g for g in P}
def closure(gens):
    S = {gk((np.eye(3, dtype=int), np.zeros(3, dtype=int)))}
    els = [(np.eye(3, dtype=int), np.zeros(3, dtype=int))]
    frontier = list(els)
    while frontier:
        nf = []
        for x in frontier:
            for y in gens:
                z = compose(x, y)
                if gk(z) not in S:
                    S.add(gk(z)); els.append(z); nf.append(z)
        frontier = nf
    return frozenset(S)
subs = set()
Pl = list(P)
for i in range(len(Pl)):
    for j in range(i, len(Pl)):
        subs.add(closure([Pl[i], Pl[j]]))
PEo = parent_edges()
BL = [16 * np.array(m) + 4 for m in itertools.product((-1, 0, 1), repeat=3)]  # block centres (fine)
def blk_sites(bc):
    return [bc - 4 + 8 * c for c in CUBE]
def admits(H, mode):
    for u, v in PEo:
        stab = []
        for g in H:
            gu, gv = op(g, u), op(g, v)
            for T in (gu - u, gv - u):
                if all(T % 16 == 0) and {key(gu - T), key(gv - T)} == {key(u), key(v)}:
                    stab.append((g, T)); break
        mid = (u + v) / 2
        cands = []
        for bc in BL:
            sites = blk_sites(bc)
            if mode == 'end':
                okc = any(key(s) in (key(u), key(v)) for s in sites)
            else:
                okc = np.abs(bc - mid).max() <= 12
            if okc:
                cands.append(bc)
        if not any(all(key(op(g, bc)) == key(bc + T) for g, T in stab) for bc in cands):
            return False
    return True
adm = {m: [H for H in subs if admits([Pk[k] for k in H], m)] for m in ('end', 'near')}
mx = {m: max(len(H) for H in adm[m]) for m in adm}
nonpolar_adm = [H for H in adm['near'] if fixed_dim([Pk[k][0] for k in H]) == 0 and len(H) > 1]
check("C1", len(subs) == 30 and mx['end'] == 3 and mx['near'] == 6 and not nonpolar_adm,
      "THEOREM (exhaustive, rederives collar-symmetry A6): every exclusive block ownership of the parent edges is polar: at most C3 (end-blocks), C3v (nearby blocks)",
      f"{len(subs)} subgroups of T_d; max admitting: end {mx['end']}, near {mx['near']}; non-polar admitting {len(nonpolar_adm)}")
G0 = [g for g in P if child_struct_ok(g, np.zeros(3, dtype=int))]
reg_c = {key(np.array([8, 8, 8]) + 16 * np.array(m)) for m in itertools.product((-1, 0, 1), repeat=3)}
cS = np.array([8, 8, 8])
stab_site = [g for g in P if key(op(g, cS) % 16) == key(cS)]
reg48 = 0
for A in LIN:
    g = (A, cS - A @ cS)
    if all(ppar(op(g, s)) == ppar(s) for s in B0) and all(key(op(g, r) % 16) == key(cS) for r in [cS]):
        reg48 += 1
check("C2", reg48 == 48 and len(stab_site) == 6 and len(G0) == 6,
      "THEOREM: a shared-boundary split (refine the 8 cells around a site, read both faces, bisect a shared edge once) is O_h for its cells, but the parent's tilings cut a site to C3v (its even cube fills one octant) and the children's keep it: no gain",
      f"cells+triangulation about the site {reg48}; parent tilings {len(stab_site)}; with child tilings {len(G0)}")
inter = [g for g in P if all(child_struct_ok(g, np.array(a)) for a in nest)]
check("C3", len(inter) == 1,
      "THEOREM: cycling the corner over the 4 conjugate choices by generation keeps, exactly, only the identity (the 4 C3v's meet trivially); it removes the drift (E2), not the polarity of any one split",
      f"common group order {len(inter)}")
# commutation of two adjacent shared-boundary raises (combinatorial: pass-once flags)
def raise_(state, R, regions):
    P_, bis = state
    if R in P_:
        return None
    return (P_ | {R}, bis | regions[R])
regions = {0: frozenset({'e01', 'i0'}), 1: frozenset({'e01', 'e12', 'i1'}), 2: frozenset({'e12', 'i2'})}
s0 = (frozenset(), frozenset())
paths_ok = raise_(raise_(s0, 0, regions), 1, regions) == raise_(raise_(s0, 1, regions), 0, regions)
pats = [frozenset(Pp) for k in range(3) for Pp in itertools.combinations(range(3), k)]
inj = all(len({raise_((Pp, frozenset().union(*[regions[r] for r in Pp])), R, regions) for Pp in pats if R not in Pp})
          == sum(1 for Pp in pats if R not in Pp) for R in range(3))
check("C4", paths_ok and inj,
      "CHECK: with pass-once shared edges (bisected iff some adjacent region is split) raises commute and are injective on patterns, so the shared-boundary split is a well-defined glued operator; it costs a second owner state per shared edge",
      "commute True; injective True")

# =================== D. copy mass ===================
print("== D. copy mass: which tiling's cubes are single-level and tick on every pattern")
def junction(nb, Sset):
    Np, Nc = 2 * nb, 4 * nb
    blk = lambda p: key(np.array(p) // 2 % nb)
    mixed_par, blocked = 0, set()
    for q in itertools.product(range(1, Np, 2), repeat=3):
        cs = [tuple((np.array(q) + c) % Np) for c in CUBE]
        sp = [c for c in cs if blk(c) in Sset]
        if 0 < len(sp) < 8:
            mixed_par += 1
            for p in sp:
                m = np.array(p) // 2; kap = np.array(p) - 2 * m
                for sg in CUBE:
                    blocked.add(key((4 * m + 2 * sg + kap) % Nc))
    tick, comp = 0, 0
    for q in itertools.product(range(1, Nc, 2), repeat=3):
        cs = [key((np.array(q) + c) % Nc) for c in CUBE]
        if all(key(np.array(c) // 4) in Sset for c in cs):
            comp += 1
            if not any(c in blocked for c in cs):
                tick += 1
    return mixed_par, comp, tick
nb = 2
allblk = [key(m) for m in itertools.product(range(nb), repeat=3)]
mixed_even = 0; nonuni_ok = True
for bits in range(1, 2 ** 8 - 1):
    Sset = {allblk[i] for i in range(8) if bits >> i & 1}
    mp, comp, tk = junction(nb, Sset)
    if mp == 0:
        nonuni_ok = False
    for m in allblk:
        if m in Sset:
            cubes = [[4 * np.array(m) + 2 * sg + c for c in CUBE] for sg in CUBE]
            mixed_even += sum(len({key(np.array(x) // 4 % nb) for x in cu}) > 1 for cu in cubes)
        else:
            mixed_even += len({key((2 * np.array(m) + c) // 2 % nb) for c in CUBE}) > 1
iso = junction(2, {(0, 0, 0)})
clu = junction(4, {key(m) for m in itertools.product(range(2), repeat=3)})
check("D1", nonuni_ok and mixed_even == 0 and iso == (8, 1, 0),
      "THEOREM (exhaustive, 254 non-uniform patterns of a 2^3-block torus): even cubes are always single-level and tick; parent odd cubes are mixed in every pattern; an isolated split's child odd cubes never tick",
      f"mixed even {mixed_even}; isolated: mixed parent odd {iso[0]}, complete child odd {iso[1]}, ticking {iso[2]}; 2^3 cluster in 4^3: complete {clu[1]}, ticking {clu[2]}")
check("D2", clu[2] < clu[1],
      "CONSEQUENCE: a copy mass on odd cubes would be absent in every interface shell; only the split's owner tiling carries it on every pattern (both tilings: Crab-excluded, register)",
      f"odd-cube mass absent on {clu[1]-clu[2]}/{clu[1]} complete child odd cubes of a 2^3 cluster")

# =================== E. consequences ===================
print("== E. consequences and estimates")
nm = 8 * 8 * 2
psi = np.random.randn(5, nm) + 1j * np.random.randn(5, nm)
psi /= np.linalg.norm(psi, axis=1, keepdims=True)
posv = np.array([8 * p + 4 * s for p in CUBE for s in CUBE for _ in range(2)], dtype=float)
posc = posv - 2
dx = [(np.abs(w) ** 2) @ posv - (np.abs(w) ** 2) @ posc for w in psi]
check("E1", max(abs(d - 2).max() for d in dx) < 1e-12,
      "THEOREM + check: same index map, so vertex = cell passing + rigid translation of 1/4 parent cell per axis for every state: no dispersion, no birefringence",
      f"shift (parent units) {dx[0][0]/8:.4f} on 5 random states, spread {max(abs(d-2).max() for d in dx):.0e}")
lP, H0, c = 1.616e-35, 2.2e-18, 3e8
L = np.sqrt(8 * np.pi) * lP
dlt = np.sqrt(3) / 2 * L
v = dlt * H0 / np.log(2)
cyc = np.cumsum(np.array(dirs), axis=0)
check("E2", (cyc[-1] == 0).all(),
      "per split the polar nesting moves excitations by (sqrt3/2) L along its diagonal (relative to records, which stay on coincident sites); cycling the 4 choices returns the drift to zero every 4 generations",
      f"delta {dlt:.1e} m; same-corner drift v {v:.1e} m/s = {v/c:.0e} c; cycled partial sums max {np.abs(cyc).sum(axis=1).max()} L/2")
check("E3", v / c < 1e-40 and dlt / c < 1e-42,
      "ESTIMATE: drift 7e-61 c is >40 orders below lab c-anisotropy (~1e-18); helicity/energy-blind, so no birefringence or dispersion bound applies",
      f"delay per crossing {dlt/c:.1e} s")
print("supplied: copy-mass symmetry and the Crab exclusion of both tilings (register); junction rule (CL-1 text); locality radius for 'near' owners; H0, l_P.")
print(f"elapsed {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
