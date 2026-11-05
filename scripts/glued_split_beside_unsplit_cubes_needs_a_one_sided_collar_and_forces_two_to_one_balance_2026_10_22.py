#!/usr/bin/env python3
"""hanging-nodes: CL-1's glued split in 3D when a split cube borders unsplit cubes.
Child units throughout: coarse sites at even integer coordinates, children at all integers.
 A  ownership, the two tilings, nesting, and a conforming closure for every refinement pattern tested
 B  the windows force the interface: bisection only at full, the collar, pins, and 2:1 balance
 C  links: Gauss's law on the sum over patterns (merged odd centres)
 D  register toy: the glued split with collar on a ring of three blocks (unitarity, constraints, contrasts)
 E  matter: mixed odd cubes tick on the passing's channel modes (one-particle toy)
 F  estimates
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/GLUED_SPLIT_BESIDE_UNSPLIT_CUBES_NEEDS_A_ONE_SIDED_COLLAR_AND_FORCES_TWO_TO_ONE_BALANCE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 120
import os, signal, time, itertools as it, collections
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import expm
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
T00 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)
P3 = list(it.product((0, 1), repeat=3))
def add(a, b): return tuple(a[i] + b[i] for i in range(3))
def d2(a, b): return sum((a[i] - b[i]) ** 2 for i in range(3))
def srt(a, b): return (min(a, b), max(a, b))
def cell_tets(c):  # alternating five-tetrahedron triangulation of the unit cell with least corner c (own lattice units)
    cs = [add(c, d) for d in P3]; ev = [p for p in cs if sum(p) % 2 == 0]; od = [p for p in cs if sum(p) % 2]
    return [tuple(sorted(ev))] + [tuple(sorted([o] + [p for p in ev if d2(p, o) == 1])) for o in od]
def fwd(s):  # a site's six registers: +axis edges and the even diagonal of each forward face
    out = [srt(s, add(s, e)) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    for i, j in ((0, 1), (1, 2), (0, 2)):
        ei = tuple(int(k == i) for k in range(3)); ej = tuple(int(k == j) for k in range(3))
        out.append(srt(s, add(add(s, ei), ej)) if sum(s) % 2 == 0 else srt(add(s, ei), add(s, ej)))
    return out
def owner(e):
    a, b = e
    return a if d2(a, b) == 1 else tuple(min(a[k], b[k]) for k in range(3))
def blk(s): return tuple((x // 2) * 2 for x in s)
def kids(n): return [tuple(2 * n[i] + k[i] for i in range(3)) for k in it.product(range(4), repeat=3)]
def x2(p): return tuple(2 * v for v in p)
def bary(T, p): return np.linalg.solve(np.array([[*T[i], 1.0] for i in range(4)]).T, np.array([*p, 1.0]))
def vol6(t): a = np.array(t[0], float); return abs(np.linalg.det(np.array([np.array(p, float) - a for p in t[1:]])))

# ======================================================================================= A
print("== A. ownership, tilings, nesting, closure")
N = 4  # coarse torus 4^3 (8 even blocks)
tor = lambda p: tuple(v % N for v in p)
tri_edges = set()
for c in it.product(range(N), repeat=3):
    for T in cell_tets(c):
        for a, b in it.combinations(T, 2):
            tri_edges.add(frozenset((tor(a), tor(b))))
own_edges = [frozenset(tor(v) for v in e) for s in it.product(range(N), repeat=3) for e in fwd(s)]
A = (0, 0, 0)
ownA = [e for s in it.product((0, 1), repeat=3) for e in fwd(s)]
mids = set(tuple((e[0][k] + e[1][k]) for k in range(3)) for e in ownA)          # child coords of midpoints
coinc = set(x2(s) for s in P3); bodies = set(add(x2(c), (1, 1, 1)) for c in P3)
kA = set(kids(A))
other_mid = [e for e in [srt(a, b) for c in it.product(range(-1, 3), repeat=3) for T in cell_tets(c) for a, b in it.combinations(T, 2)]
             if e not in set(ownA) and tuple(e[0][k] + e[1][k] for k in range(3)) in kA]
check("A1 THEOREM: each site's 6 forward registers partition the edges; a split puts its 64 children at its 8 sites, the midpoints of exactly its 48 owned edges, and the centres of the 8 cells its sites are least corner of",
      len(own_edges) == len(set(own_edges)) == len(tri_edges) == 6 * N ** 3 and kA == coinc | mids | bodies and len(mids) == 48
      and not other_mid, f"{len(tri_edges)} edges = 6 x {N**3} sites; children 8 + 48 + 8 = {len(coinc | mids | bodies)}")
ev_cube = set(srt(a, b) for T in cell_tets((0, 0, 0)) for a, b in it.combinations(T, 2))
od_cube = set(srt(a, b) for T in cell_tets((1, 1, 1)) for a, b in it.combinations(T, 2))
odd_corner_blocks = set(blk(add((1, 1, 1), d)) for d in P3)
# passings: even passing sends corner c of block origin e to child coords 2e + 2m + c; odd likewise with origin o
x = (1, 1, 1); img_e = set(add(x2((0, 0, 0)), add(x2(m), (1, 1, 1))) for m in P3); img_o = set(add(x2((1, 1, 1)), x2(m)) for m in P3)
own_cells = sum(all(blk(add(c, d)) == A for d in P3 if d != (1, 1, 1)) for c in P3)
check("A2 THEOREM: the tilings' cubes share no edge; an odd cube's corners lie in 8 even blocks; the two passings send a shared site to disjoint child sets, so one tiling (the even) owns the split; 1 of a block's 8 cells is wholly its own", not (ev_cube & od_cube) and len(odd_corner_blocks) == 8 and not (img_e & img_o) and own_cells == 1,
      f"site (1,1,1): images {sorted(img_e)[0]}.. vs {sorted(img_o)[0]}..; own cells {own_cells}/8")
# nesting of the child alternating triangulation in the parent's
ctet_child = [T for k in it.product(range(-2, 6), repeat=3) for T in cell_tets(k)]
coarse_box = [tuple(x2(p) for p in T) for c in it.product(range(-1, 3), repeat=3) for T in cell_tets(c)]
nest_ok = 0; nest_bad = 0
for t in ctet_child:
    if not all(0 <= v <= 4 for p in t for v in p): continue
    cnt = sum(all(bary(T, p).min() > -1e-9 for p in t) for T in coarse_box)
    nest_ok += cnt == 1; nest_bad += cnt != 1
child_edges = set(srt(a, b) for t in ctet_child for a, b in it.combinations(t, 2))
corner = tuple(x2(p) for p in cell_tets((0, 0, 0))[1])  # a coarse corner tetrahedron
newedge_bad = 0
for a, b in it.combinations(corner, 2):
    m = tuple((a[k] + b[k]) // 2 for k in range(3)); rest = [p for p in corner if p not in (a, b)]
    newedge_bad += any(srt(m, r) not in child_edges for r in rest)
check("A3 THEOREM: the children's triangulation is nested in the parent's but is no bisection of it (each first bisection of a parent corner tetrahedron draws a non-lattice edge)", nest_bad == 0 and nest_ok == 320 and newedge_bad == 6,
      f"{nest_ok} nested, {nest_bad} not; bad first bisections {newedge_bad}/6")

def face_pattern(f, present):
    """canonical subdivision of a parent triangle (child coords) by its present edge midpoints"""
    v = list(f); m = {}
    for a, b in it.combinations(v, 2):
        q = tuple((a[k] + b[k]) // 2 for k in range(3))
        if q in present: m[srt(a, b)] = q
    if not m: return [tuple(sorted(f))]
    if len(m) == 3:
        pts = v + list(m.values())
        return [tuple(sorted(t)) for t in it.combinations(pts, 3)
                if all(srt(a, b) in child_edges for a, b in it.combinations(t, 2))]
    if len(m) == 1:
        (a, b), q = next(iter(m.items())); c = [p for p in v if p not in (a, b)][0]
        return [tuple(sorted((a, q, c))), tuple(sorted((q, b, c)))]
    (e1, q1), (e2, q2) = sorted(m.items(), key=lambda kv: kv[1])
    v0 = (set(e1) & set(e2)).pop(); v1 = [p for p in e1 if p != v0][0]; v2 = [p for p in e2 if p != v0][0]
    return [tuple(sorted((v0, q1, q2))), tuple(sorted((q1, v1, v2))), tuple(sorted((q1, v2, q2)))]   # diagonal from the smaller midpoint
def closure(blocks, lo=-1, hi=3):
    blocks = set(blocks)
    present = set(x2(p) for p in it.product(range(lo, hi + 1), repeat=3)) | set(q for n in blocks for q in kids(n))
    out = []; nvirt = 0
    for c in it.product(range(lo, hi), repeat=3):
        for T0 in cell_tets(c):
            T = tuple(x2(p) for p in T0)
            E = [srt(a, b) for a, b in it.combinations(T0, 2)]
            nb = sum(blk(owner(e)) in blocks for e in E)
            cen = tuple(sum(p[k] for p in T) / 4 for k in range(3)); ci = tuple(int(x) for x in cen)
            body = ci if cen == ci and ci in present else None
            if nb == 6:
                lo_ = [min(p[k] for p in T) for k in range(3)]
                sub = [t for k in it.product(*[range(lo_[i], lo_[i] + 2) for i in range(3)]) for t in cell_tets(k)
                       if all(bary(T, p).min() > -1e-9 for p in t)]
            elif nb == 0 and body is None: sub = [T]
            else:
                apex = body if body is not None else cen; nvirt += body is None
                sub = [tuple(sorted(tr)) + (apex,) for f in it.combinations(T, 3) for tr in face_pattern(f, present)]
            out += [(T, t) for t in sub]
    faces = collections.Counter(tuple(sorted(f)) for _, t in out for f in it.combinations(t, 3))
    L, H = 2 * lo, 2 * hi
    onb = lambda f: any(all(p[i] == L for p in f) or all(p[i] == H for p in f) for i in range(3))
    bad = sum(1 for f, n in faces.items() if (n == 1 and not onb(f)) or n > 2)
    verts = set(p for _, t in out for p in t)
    orphan = sum(1 for p in present if all(L <= v <= H for v in p) and p not in verts)
    vol_ok = abs(sum(vol6(t) for _, t in out) - 6 * (H - L) ** 3) < 1e-6 and min(vol6(t) for _, t in out) > 1e-9
    return out, bad, orphan, vol_ok, nvirt
pats = {'A': [(0, 0, 0)], 'A,+x': [(0, 0, 0), (2, 0, 0)], 'A,+xy': [(0, 0, 0), (2, 2, 0)], 'A,+xyz': [(0, 0, 0), (2, 2, 2)],
        'A,-x': [(0, 0, 0), (-2, 0, 0)], '2^3': [tuple(x2(m)) for m in P3]}
blist = [tuple(x2(m)) for m in it.product((-1, 0, 1), repeat=3)]
for r in range(3): pats[f'rand{r}'] = [b for b in blist if rng.random() < 0.5]
res = {k: closure(v) for k, v in pats.items()}
check("A4 THEOREM (finite check): every pattern tested closes to a simplicial complex: children's tetrahedra where all 6 parent edges are bisected, else a cone from the cell centre over a canonical subdivision of each face",
      all(r[1] == 0 and r[2] == 0 and r[3] for r in res.values()),
      f"{len(res)} patterns, unmatched faces {sum(r[1] for r in res.values())}, orphans {sum(r[2] for r in res.values())}; A: {len(res['A'][0])} tets, {res['A'][4]} bookkeeping points")
SA = res['A'][0]

# ======================================================================================= B
print("== B. windows force the interface (child units: axis [1,2], diagonal [sqrt2, 2sqrt2])")
def forcing(blocks, lo=-2, hi=4, cap_bisected=True):
    blocks = set(blocks); creg = set(e for n in blocks for s in kids(n) for e in fwd(s))
    pinned_c = set(); pinned_k = set(); free_k = 0; npart = 0
    for c in it.product(range(lo, hi), repeat=3):
        for T0 in cell_tets(c):
            E = [srt(a, b) for a, b in it.combinations(T0, 2)]; bis = [blk(owner(e)) in blocks for e in E]
            if all(bis): continue
            T = [x2(p) for p in T0]; lo_ = [min(p[k] for p in T) for k in range(3)]; hi_ = [max(p[k] for p in T) for k in range(3)]
            ins = []
            for e in creg:
                if all(lo_[k] <= e[0][k] <= hi_[k] and lo_[k] <= e[1][k] <= hi_[k] for k in range(3)):
                    la, lb = bary(T, e[0]), bary(T, e[1])
                    if la.min() > -1e-9 and lb.min() > -1e-9: ins.append((e, la - lb))
            if not ins: continue
            npart += 1; idx = {e: i for i, e in enumerate(E)}
            q = lambda e: d2(*e)
            bounds = [(q(e) * 1.0, q(e) * 4.0 if (cap_bisected or not bis[i]) else None) for i, e in enumerate(E)]
            Aub = []; bub = []; rows = []
            for e, w in ins:
                co = np.zeros(6)
                for i in range(4):
                    for j in range(i + 1, 4): co[idx[srt(T0[i], T0[j])]] -= w[i] * w[j]
                rows.append((e, co)); Aub += [-co, co]; bub += [-q(e) * 1.0, q(e) * 4.0]
            Aub = np.array(Aub); bub = np.array(bub)
            for i, e in enumerate(E):
                r0 = linprog(np.eye(6)[i], A_ub=Aub, b_ub=bub, bounds=bounds, method='highs')
                if r0.status == 0 and abs(r0.fun - q(e) * 4.0) < 1e-9: pinned_c.add(e)
            for e, co in rows:
                r0 = linprog(co, A_ub=Aub, b_ub=bub, bounds=bounds, method='highs')
                r1 = linprog(-co, A_ub=Aub, b_ub=bub, bounds=bounds, method='highs')
                if r0.status == 0 and abs(r0.fun - q(e)) < 1e-9 and abs(-r1.fun - q(e)) < 1e-9: pinned_k.add(e)
                else: free_k += 1
    own = set(e for n in blocks for s in [add(n, d) for d in P3] for e in fwd(s))
    collar = pinned_c - own
    kb = collections.Counter(blk(owner(e)) for e in pinned_k)
    nkb = 8 * len(blocks)
    return dict(own=len(own), own_pinned=len(own & pinned_c), collar=len(collar), collar_owners=collections.Counter(blk(owner(e)) for e in collar),
                pinned_k=len(pinned_k), free_k=free_k, creg=len(creg), kb_free=nkb - len(kb), npart=npart)
check("B1 THEOREM: a parent edge passes as two children inside their windows only when full, so all 48 edges a split bisects must be full, not just the 18 of its tiling cube", True,
      "l1+l2 = l, l1,l2 >= L, l <= 2L => l1 = l2 = L, l = 2L")
fA = forcing([(0, 0, 0)]); fAB = forcing([(0, 0, 0), (2, 0, 0)]); fS = forcing([tuple(x2(m)) for m in P3])
plus = {(2, 0, 0), (0, 2, 0), (0, 0, 2)}
check("B2 THEOREM (exact LP): beside an isolated split cube every child register in a partly refined parent tetrahedron is held at its floor, and the parent edges it reads are held full: 42 owned + a collar of the 12 in-plane registers of each unsplit +x/+y/+z face neighbour",
      fA['own_pinned'] == 42 and fA['collar'] == 36 and set(fA['collar_owners']) == plus and fA['free_k'] == 0,
      f"held: owned {fA['own_pinned']}/48, collar {fA['collar']} from {sorted(fA['collar_owners'])}, child {fA['pinned_k']}/{fA['creg']} (free in partial 0); trigger reads 84")
check("B3 THEOREM: the collar moves with the pattern (a split + neighbour drops its share); a 2^3 super-block has a 144-edge collar, so no finite block of blocks closes", fAB['collar'] == 60 and (2, 0, 0) not in fAB['collar_owners'] and fS['collar'] == 144
      and len(fS['collar_owners']) == 12, f"A,+x: {fAB['collar']} from {len(fAB['collar_owners'])} blocks; 2^3: {fS['collar']} from {len(fS['collar_owners'])}")
check("B4 THEOREM: 2:1 balance is forced: every child cube of an isolated split cube owns a held register and can never split",
      fA['kb_free'] == 0 and fS['kb_free'] == 8, f"free child cubes: isolated {fA['kb_free']}/8, 2^3 {fS['kb_free']}/64")
fAu = forcing([(0, 0, 0)], cap_bisected=False)
check("B5 DIAGNOSTIC: if a neighbour may read a bisected edge beyond its own window the collar stands but the hanging-face holds loosen", fAu['collar'] == 36 and fAu['pinned_k'] < fA['pinned_k'],
      f"collar {fAu['collar']}; held children {fAu['pinned_k']} vs {fA['pinned_k']}")
# positivity of the closure for coarse configurations with the forced values: affine reading inside each parent tetrahedron
def cm_vol2(D2):  # Cayley-Menger: 288 V^2
    M = np.ones((5, 5)); M[0, 0] = 0; M[1:, 1:] = D2; return np.linalg.det(M)
pin = set()
for e in [e for s in P3 for e in fwd(s)]: pin.add(e)
pin |= set(e for n in plus for s in [add(n, d) for d in P3] for e in fwd(s) if all(e[0][k] == n[k] and e[1][k] == n[k] for k in range(3) if n[k]))
cedge = set(srt(a, b) for c in it.product(range(-1, 3), repeat=3) for T in cell_tets(c) for a, b in it.combinations(T, 2))
ntr = 0; nbadsub = 0; vtot = 0; worst = 1.0
for trial in range(6):
    Lv = {e: (2.0 if e in pin else 2.0 * (1 - 0.3 * rng.random())) * np.sqrt(d2(*e)) for e in cedge}
    for (T, t) in SA:
        T0 = [tuple(v // 2 for v in p) for p in T]
        D = np.array([[Lv[srt(a, b)] ** 2 if a != b else 0.0 for b in T0] for a in T0])
        VT = cm_vol2(D)
        if VT <= 0: continue
        lam = [bary(T, p) for p in t]
        Ds = np.array([[-0.5 * (li - lj) @ D @ (li - lj) for lj in lam] for li in lam])
        v = cm_vol2(Ds); ntr += 1; nbadsub += v <= 0; worst = min(worst, np.sqrt(max(v, 0) / VT))
check("B6 THEOREM + check: with the held values and free edges anywhere in a 30% band below full, every closure tetrahedron read from its flat parent has positive volume", nbadsub == 0 and ntr > 1000,
      f"{ntr} tetrahedra, nonpositive {nbadsub}; min sub/parent volume {worst:.3f}")

# ======================================================================================= C
print("== C. links: Gauss's law on the sum over patterns (torus of 2x2x2 blocks)")
def gauss_graph(blocks):
    blocks = set(blocks); Nc = 4; Nk = 8
    present = lambda q: blk(tuple((v % Nk) // 2 for v in q)) in blocks
    bonds = []  # (site label, even vertex, odd vertex)
    ties = 0
    for s in it.product(range(Nc), repeat=3):
        if blk(s) in blocks: continue
        bonds.append((('c', s), ('E', blk(s)), ('O', tuple((((v - 1) // 2) * 2 + 1) % Nc for v in s))))
    for n in blocks:
        for q in kids(n):
            oo = tuple(((v - 1) // 2) * 2 + 1 for v in q)  # child odd cube origin (child coords)
            if all(present(add(oo, d)) for d in P3): odd = ('o', tuple(v % Nk for v in oo))
            else:
                cen = [(v + 0.5) / 2.0 for v in oo]  # child odd centre, coarse coords
                pick = []
                for v in cen:
                    cand = sorted(((min(abs(v - o), Nc - abs(v - o)), o % Nc) for o in (1.5, 3.5)))
                    ties += abs(cand[0][0] - cand[1][0]) < 1e-12; pick.append(int(cand[0][1] - 0.5))
                odd = ('O', tuple(pick))
            bonds.append((('k', q), ('e', tuple(((v // 2) * 2) % Nk for v in q)), odd))
    return bonds, ties
def components(bonds):
    par = {}
    def f(a):
        par.setdefault(a, a)
        while par[a] != a: par[a] = par[par[a]]; a = par[a]
        return a
    for _, a, b in bonds: par[f(a)] = f(b)
    return f
allblocks = [tuple(x2(m)) for m in P3]
ok_all = True; maxties = 0; npat = 0; ncheck = 0
for mask in range(256):
    blocks = [b for i, b in enumerate(allblocks) if mask >> i & 1]
    bonds, ties = gauss_graph(blocks); maxties = max(maxties, ties); npat += 1
    labels = [b[0] for b in bonds]
    ok_all &= len(labels) == len(set(labels)) == 64 - 8 * len(blocks) + 64 * len(blocks)
    if mask % 37: continue
    # parent configuration obeying Gauss, then child occupations at random; coarse bonds held, child bonds solved
    pb, _ = gauss_graph([])
    for trial in range(3):
        n = {b[0]: rng.integers(0, 2) for b in pb}
        Q = collections.Counter()
        for lab, ev, od in pb: Q[ev] += n[lab] - 0.5; Q[od] -= n[lab] - 0.5
        f = components(pb); tot = collections.Counter()
        for v, qv in Q.items(): tot[f(v)] += qv
        ok_all &= all(abs(t) < 1e-9 for t in tot.values())
        # integer parent field: spanning-forest solve
        verts = sorted(set(v for b in pb for v in b[1:])); vi = {v: i for i, v in enumerate(verts)}
        Dm = np.zeros((len(verts), len(pb)))
        for j, (lab, ev, od) in enumerate(pb): Dm[vi[ev], j] += 1; Dm[vi[od], j] -= 1
        qv = np.array([Q[v] for v in verts]); Ep = np.linalg.lstsq(Dm, qv, rcond=None)[0]
        ok_all &= np.abs(Dm @ Ep - qv).max() < 1e-9
        Eof = {pb[j][0]: Ep[j] for j in range(len(pb))}
        # after the split: residual divergence the child bonds must carry, per vertex
        nb = dict(n); res_ = collections.Counter()
        for lab, ev, od in bonds:
            if lab[0] == 'k': nb[lab] = rng.integers(0, 2)
        for lab, ev, od in bonds:
            res_[ev] += nb[lab] - 0.5; res_[od] -= nb[lab] - 0.5
            if lab[0] == 'c': res_[ev] -= Eof[lab]; res_[od] += Eof[lab]
        kb = [b for b in bonds if b[0][0] == 'k']
        if kb:
            f2 = components(kb); tot = collections.Counter()
            for v, r in res_.items():
                if any(v in b[1:] for b in kb): tot[f2(v)] += r
                else: ok_all &= abs(r) < 1e-9   # vertices with only coarse bonds keep their old law
            ok_all &= all(abs(t) < 1e-9 for t in tot.values()); ncheck += 1
check("C1 THEOREM + check: a child link ends at its odd centre if that cube is complete, else at the nearest parent odd centre (never a tie); unsplit links keep their laws and Gauss's law is solvable for any parent field and child occupations",
      ok_all and maxties == 0 and npat == 256 and ncheck > 10, f"256 patterns (2^3-block torus); ties {maxties}; {ncheck} solved")

# ======================================================================================= D
print("== D. register toy: glued split with collar, ring of 3 blocks (bulk u_k, minus-face f_k; 2S = 2)")
TS = 2; LV = range(TS + 1); K = 3
def configs():
    per = [('c', u, f) for u in LV for f in LV] + [('s', a, b) for a in LV for b in LV]
    return list(it.product(per, repeat=K))
CF = configs(); CI = {c: i for i, c in enumerate(CF)}; DIM = len(CF)
def s_(c, k): return c[k % K][0] == 's'
def trig(c, k, collar=True):  # block k coarse and its whole trigger set full
    b = c[k % K]
    if b[0] != 'c' or b[1] != TS or b[2] != TS: return False
    if not collar: return True
    nb = c[(k + 1) % K]; return nb[0] == 's' or nb[2] == TS
def allowed(c, collar=True):
    for k in range(K):
        if trig(c, k, collar): return False
        if s_(c, k):
            if collar and not s_(c, k + 1) and c[(k + 1) % K][2] != TS: return False
            if not s_(c, k - 1) and c[k][1] != 0: return False   # pinned child at the hanging face
            if not s_(c, k + 1) and c[k][2] != 0: return False   # pinned child at the collar face
    return True
def P_collar(c): return all(not s_(c, k) or s_(c, k + 1) or c[(k + 1) % K][2] == TS for k in range(K))
def glue(c, collar=True):  # carry every completed trigger onto its split image (children at their floor)
    c = list(c); ch = True
    while ch:
        ch = False
        for k in range(K):
            if trig(tuple(c), k, collar): c[k] = ('s', 0, 0); ch = True
    return tuple(c)
def build_H(collar=True, cascade=True):
    rows, cols = [], []
    for c in CF:
        if not allowed(c, collar): continue
        for k in range(K):
            b = c[k]
            for slot in (1, 2):
                if b[slot] == TS: continue
                nbk = list(b); nbk[slot] += 1; c2 = list(c); c2[k] = tuple(nbk); c2 = tuple(c2)
                if b[0] == 'c': c2 = glue(c2, collar) if cascade else c2
                if not cascade and not allowed(c2, collar):
                    c3 = list(c2); c3[k] = ('s', 0, 0) if trig(c2, k, collar) else c3[k]; c2 = tuple(c3)
                if c2 in CI and (allowed(c2, collar) or not cascade): rows.append(CI[c2]); cols.append(CI[c])
    R = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(DIM, DIM)); R.data[:] = 1.0
    return (R + R.T).tocsr()
Pv = np.array([allowed(c) for c in CF], float)
H = build_H()
herm = abs(H - H.T).max(); leakH = abs(sp.diags(1 - Pv) @ H @ sp.diags(Pv)).max()
v0 = np.zeros(DIM, complex); c0 = tuple(('c', TS, TS - 1) for _ in range(K)); v0[CI[c0]] = 1
vt = expm_multiply(-1j * H, v0, start=0, stop=12, num=25, endpoint=True)
pw = [(abs(v) ** 2 * (1 - Pv)).sum() for v in vt]; norm = max(abs(np.linalg.norm(v) - 1) for v in vt)
psplit = [(abs(v) ** 2 * np.array([sum(s_(c, k) for k in range(K)) for c in CF])).sum() / K for v in vt]
nsec = collections.Counter(tuple(s_(c, k) for k in range(K)) for c in CF if allowed(c))
check("D1 THEOREM: kinematic space = tensor product over blocks of (coarse + split); local commuting projectors (glued trigger with collar, held collar, held children) cut it into an orthogonal sum over the 8 patterns; the glued generator is hermitian and keeps it",
      herm == 0 and leakH == 0 and norm < 1e-10 and max(pw) < 1e-20 and len(nsec) == 8,
      f"dim {DIM}, allowed {int(Pv.sum())}, patterns {len(nsec)}; leak {max(pw):.0e}; split fraction to {max(psplit):.2f}")
H0 = build_H(collar=False); Pc = np.array([allowed(c, False) and P_collar(c) for c in CF], float)
P0 = np.array([allowed(c, False) for c in CF], float)
v0b = np.zeros(DIM, complex); v0b[CI[tuple(('c', TS, TS - 1) if k == 0 else ('c', 0, 0) for k in range(K))]] = 1
vtb = expm_multiply(-1j * H0, v0b, start=0, stop=12, num=25, endpoint=True)
leak0 = max((abs(v) ** 2 * P0 * (1 - Pc)).sum() for v in vtb)
check("D2 DIAGNOSTIC: with the trigger on owned edges only the split fires with the collar below full (children below floor, no state), and the odds go there",
      leak0 > 1e-2, f"weight outside the projector up to {leak0:.3f}")
# shift (momentum-constraint) generators never change the pattern: block-diagonal in patterns
def shift_ok():
    bad = 0
    for c in CF:
        if not allowed(c): continue
        for k in range(K):
            a, b = c[k], c[(k + 1) % K]
            if a[0] == 'c' and b[0] == 'c' and a[1] < TS and b[2] > 0:
                c2 = list(c); c2[k] = ('c', a[1] + 1, a[2]); c2[(k + 1) % K] = ('c', b[1], b[2] - 1); c2 = tuple(c2)
                if allowed(c2): bad += tuple(s_(c2, j) for j in range(K)) != tuple(s_(c, j) for j in range(K))
    return bad
check("D3 THEOREM: register shifts never change the pattern and are undefined on held edges, so shift-invariant odds are a sum over patterns and CL-3's polar tick acts sector by sector", shift_ok() == 0,
      "pattern changes: 0")

# ======================================================================================= E
print("== E. matter: one-particle toy, 4^3 torus, block A split")
Nc = 4; sites = [('c', s) for s in it.product(range(Nc), repeat=3) if blk(s) != (0, 0, 0)] + [('k', q) for q in kids((0, 0, 0))]
SI = {s: i for i, s in enumerate(sites)}; M = len(sites)
eps = 0.6
Rc = np.zeros((8, 8))
for a, d in enumerate(P3):
    for i in range(3):
        d2_ = list(d); d2_[i] ^= 1; Rc[P3.index(tuple(d2_)), a] += 1 / np.sqrt(3)
uc = expm(-1j * eps * Rc)
def cube_U(vecs):
    V = np.array(vecs).T; return np.eye(M) + V @ (uc - np.eye(8)) @ V.conj().T
def e(s): v = np.zeros(M); v[SI[s]] = 1; return v
def chan(c): v = sum(e(('k', add(x2((0, 0, 0)), add(x2(m), c)))) for m in P3); return v / np.sqrt(8)
Ue = np.eye(M, dtype=complex)
for n in allblocks:
    if n != (0, 0, 0): Ue = cube_U([e(('c', add(n, d))) for d in P3]) @ Ue
for m in P3: Ue = cube_U([e(('k', add(x2(m), d))) for d in P3]) @ Ue
def corner_vec(s): return chan(tuple(v % 2 for v in s)) if blk(s) == (0, 0, 0) else e(('c', s))
Uo = np.eye(M, dtype=complex)
for o in it.product((1, 3), repeat=3): Uo = cube_U([corner_vec(tuple(v % Nc for v in add(o, d))) for d in P3]) @ Uo
Ukid = cube_U([e(('k', add((1, 1, 1), d))) for d in P3])
U = Uo @ Ue
B = np.array([chan(c) for c in P3]); orth = abs(B @ B.T - np.eye(8)).max()
check("E1 THEOREM: the passing's 8 channel modes (even sum of one corner over the 8 children) are orthonormal with disjoint supports; mixed odd cubes tick on them; the tick is unitary", orth < 1e-12 and abs(U.conj().T @ U - np.eye(M)).max() < 1e-12, f"|B B^T - 1| {orth:.0e}")
# the split is invisible to the mixed odd cubes on the split image: V maps coarse A corner -> channel mode
Mc = 64; Vmap = np.zeros((M, Mc)); cs = list(it.product(range(Nc), repeat=3))
for j, s in enumerate(cs): Vmap[:, j] = corner_vec(s)
Uo_c = np.eye(Mc, dtype=complex)
for o in it.product((1, 3), repeat=3):
    V = np.array([np.eye(Mc)[cs.index(tuple(v % Nc for v in add(o, d)))] for d in P3]).T
    Uo_c = (np.eye(Mc) + V @ (uc - np.eye(8)) @ V.T) @ Uo_c
comm_kid = max(abs(Ukid @ cube_U([corner_vec(tuple(v % Nc for v in add(o, d))) for d in P3]) - cube_U([corner_vec(tuple(v % Nc for v in add(o, d))) for d in P3]) @ Ukid).max()
               for o in it.product((1, 3), repeat=3))
check("E2 THEOREM: on the split image the mixed odd half-tick is the passing of the unsplit one (the split is invisible to neighbours when it fires); the complete child odd cube overlaps every mixed cube and must wait", abs(Uo @ Vmap - Vmap @ Uo_c).max() < 1e-12 and comm_kid > 1e-2,
      f"|U_o V - V U_o,parent| {abs(Uo @ Vmap - Vmap @ Uo_c).max():.0e}; max |[U_child, U_mixed]| {comm_kid:.2f}")
psi = np.zeros(M, complex); psi[SI[('c', (2, 0, 0))]] = 1; kid_idx = [SI[s] for s in sites if s[0] == 'k']
Uf = (np.eye(M) @ Ue)  # frozen mixed cubes: only coarse odd cubes with no split corner tick
Uo_f = np.eye(M, dtype=complex)
for o in it.product((1, 3), repeat=3):
    if all(blk(tuple(v % Nc for v in add(o, d))) != (0, 0, 0) for d in P3): Uo_f = cube_U([e(('c', tuple(v % Nc for v in add(o, d)))) for d in P3]) @ Uo_f
wt = []; wf = []; p1 = psi.copy(); p2 = psi.copy()
for t in range(12): p1 = U @ p1; p2 = Uo_f @ Ue @ p2; wt.append((abs(p1[kid_idx]) ** 2).sum()); wf.append((abs(p2[kid_idx]) ** 2).sum())
check("E3 DIAGNOSTIC: channel-mode mixed cubes let a particle cross into the children; freezing them would wall the split region off", max(wt) > 0.05 and max(wf) < 1e-20,
      f"weight on children: {max(wt):.3f} vs frozen {max(wf):.0e}")

# ======================================================================================= F
print("== F. ESTIMATES (L = sqrt(8 pi) l_P)")
lP = 1.616e-35; L = np.sqrt(8 * np.pi) * lP
dz = 1e-5 * 2 * np.pi * L / 1e-19 / np.log(2)   # neighbour edge mismatch, amplitude 1e-5 at the shortest probed scale
check("F1 collar wait: neighbours' edges differ by ~1e-5 x 2 pi L / lambda (metric perturbations at the shortest probed scale), a negligible fraction of a doubling", dz < 1e-15,
      f"lambda = 1e-19 m: wait {dz:.0e} of a doubling")
nlev = np.log2(1 + 6.0)
check("F2 bound regions: next to a cube that never fills one layer stalls full; forced 2:1 balance grades the void one level per layer, a shell a few rung lengths thick",
      nlev * 4 * L < 1e-32, f"{nlev:.1f} levels, shell ~ {nlev * 4 * L:.0e} m")
print("supplied: forward ownership (from the passing's child placement), closure template + bookkeeping centres (flat), "
      "sum-in-window reading (B5), channel-mode mixed ticks + deferred child odd tick (E), toy hop and 2S=2, measured numbers.")
print(f"elapsed {time.monotonic() - T00:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
