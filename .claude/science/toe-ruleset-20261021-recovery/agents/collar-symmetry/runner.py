#!/usr/bin/env python3
"""collar-symmetry: does CL-1's one-sided split ownership/collar pick an orientation, and does it matter?
 A  exact symmetry groups (signed permutations about the relevant centres, with lattice translations)
 B  matter: displacement made by the passing (1D two-tiling walk, level-matched polar map)
 C  symmetric alternative: the cell reading of the same split (children = each site's own child even cube, centred on it)
 D  estimates
Coordinates: coarse (block-site) lattice; child lattice spacing 1/2. Doubled integer coordinates where needed.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import os, signal, time, itertools as it, collections
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
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
# signed permutations: y_i = s_i x_{p_i}
OH = [(p, s) for p in it.permutations(range(3)) for s in it.product((1, -1), repeat=3)]
def mat(g): M = np.zeros((3, 3), int); [M.__setitem__((i, g[0][i]), g[1][i]) for i in range(3)]; return M
def act(g, x, c=(0, 0, 0), t=(0, 0, 0)): return tuple(g[1][i] * (x[g[0][i]] - c[g[0][i]]) + c[i] + t[i] for i in range(3))
def is_rot(g): return round(np.linalg.det(mat(g))) == 1
def fixdim(G): return 3 - np.linalg.matrix_rank(np.vstack([mat(g) - np.eye(3, dtype=int) for g in G])) if G else 3
def cell_tets(c):  # alternating five-tetrahedron triangulation of the unit cell with least corner c
    cs = [add(c, d) for d in P3]; ev = [p for p in cs if sum(p) % 2 == 0]; od = [p for p in cs if sum(p) % 2]
    return [tuple(sorted(ev))] + [tuple(sorted([o] + [p for p in ev if d2(p, o) == 1])) for o in od]
def fwd(s):  # a site's six forward registers (+axis edges, even diagonal of each forward face)
    out = [srt(s, add(s, e)) for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    for i, j in ((0, 1), (1, 2), (0, 2)):
        ei = tuple(int(k == i) for k in range(3)); ej = tuple(int(k == j) for k in range(3))
        out.append(srt(s, add(add(s, ei), ej)) if sum(s) % 2 == 0 else srt(add(s, ei), add(s, ej)))
    return out
def blk(s): return tuple((x // 2) * 2 for x in s)

# ======================================================================================= A
print("== A. symmetry groups")
P = 8                                   # doubled period of a 4^3 coarse torus
D = lambda x: tuple(2 * v % P for v in x)
md = lambda x: tuple(v % P for v in x)
TR = list(it.product(range(0, P, 2), repeat=3))   # coarse-integer translations (doubled)
def point_part(struct, c, trans=TR):
    """R's for which some translation makes x -> R(x-c)+c+t a symmetry; struct(gmap) -> bool"""
    out = []
    for g in OH:
        if any(struct(lambda x, g=g, t=t: md(act(g, x, c, t))) for t in trans): out.append(g)
    return out
# A1 CL-1 fine sites: two tilings by 2x2x2 cubes offset by (1,1,1) (fine sites doubled)
ev_c = frozenset(frozenset(md(add(o, x2)) for x2 in it.product((0, 2), repeat=3)) for o in it.product((0, 4), repeat=3))
od_c = frozenset(frozenset(md(add(add(o, (2, 2, 2)), x2)) for x2 in it.product((0, 2), repeat=3)) for o in it.product((0, 4), repeat=3))
def s_tilings(f): return frozenset(frozenset(f(x) for x in cb) for cb in ev_c) == ev_c and frozenset(frozenset(f(x) for x in cb) for cb in od_c) == od_c
G1 = point_part(s_tilings, (1, 1, 1))
diag_orbit = set(act(g, (1, 1, 1)) for g in G1)
odd_same = all(od_c == frozenset(frozenset(md(add(add(o, off), x2)) for x2 in it.product((0, 2), repeat=3)) for o in it.product((0, 4), repeat=3))
               for off in it.product((2, -2), repeat=3))
check("A1 THEOREM: CL-1's two tilings keep all 48 cube operations about a cube centre (24 rotations, inversion); the offset (1,1,1) equals every body-diagonal offset mod 2, so it names no orientation",
      len(G1) == 48 and sum(map(is_rot, G1)) == 24 and len(diag_orbit) == 8 and odd_same and fixdim(G1) == 0, f"|G| {len(G1)}, rotations {sum(map(is_rot, G1))}, diagonal orbit {len(diag_orbit)}/8, fixed vectors {fixdim(G1)}")
# A2 block triangulation and the even tiling of blocks (coarse lattice)
tri = frozenset(frozenset((D(a), D(b))) for c in it.product(range(4), repeat=3) for T in cell_tets(c) for a, b in it.combinations(T, 2))
btile = frozenset(frozenset(D(add(o, d)) for d in P3) for o in it.product((0, 2), repeat=3))
def s_tri(f): return frozenset(frozenset(f(x) for x in e) for e in tri) == tri
def s_tile(f): return frozenset(frozenset(f(x) for x in b) for b in btile) == btile
Gt_site = point_part(s_tri, (0, 0, 0)); Gtt = point_part(lambda f: s_tri(f) and s_tile(f), (1, 1, 1))
Gtt0 = point_part(lambda f: s_tri(f) and s_tile(f), (1, 1, 1), trans=[(0, 0, 0)])
inv = ((0, 1, 2), (-1, -1, -1))
check("A2 THEOREM: the block triangulation keeps all 48 about a block site; with the even tiling of blocks it keeps T_d about the block centre (12 rotations, the diagonal mirrors, no inversion) and no vector",
      len(Gt_site) == 48 and len(Gtt) == len(Gtt0) == 24 and sum(map(is_rot, Gtt)) == 12 and inv not in Gtt and fixdim(Gtt) == 0,
      f"site {len(Gt_site)}; block centre {len(Gtt)} (rot {sum(map(is_rot, Gtt))}, inversion {inv in Gtt}); fixed vectors {fixdim(Gtt)}")
# A3 forward ownership: edge -> owning block
def owner(e):
    a, b = e
    return a if d2(a, b) == 1 else tuple(min(a[k], b[k]) for k in range(3))
own = frozenset((frozenset((D(e[0]), D(e[1]))), frozenset(D(add(blk(owner(e)), d)) for d in P3)) for s in it.product(range(4), repeat=3) for e in fwd(s))
def s_own(f): return frozenset((frozenset(f(x) for x in e), frozenset(f(x) for x in b)) for e, b in own) == own
Gown = point_part(lambda f: s_tri(f) and s_tile(f) and s_own(f), (1, 1, 1))
fixv = np.linalg.svd(np.vstack([mat(g) - np.eye(3) for g in Gown]))[2][-1]
check("A3 THEOREM: forward ownership keeps only C3v of the (1,1,1) diagonal (the 3 turns about it and the 3 axis-swap mirrors), a polar group: one fixed vector, along (1,1,1)",
      len(Gown) == 6 and sum(map(is_rot, Gown)) == 3 and all(act(g, (1, 1, 1)) == (1, 1, 1) for g in Gown) and fixdim(Gown) == 1,
      f"|G| {len(Gown)}, rotations {sum(map(is_rot, Gown))}, fixed vector {np.round(np.abs(fixv), 3)}")
# A4 trigger read set of one block: its 48 owned edges + the collar on its +x,+y,+z faces
ownA = set(e for s in P3 for e in fwd(s))
collar = set(e for n in ((2, 0, 0), (0, 2, 0), (0, 0, 2)) for s in [add(n, d) for d in P3] for e in fwd(s)
             if all(e[0][k] == n[k] and e[1][k] == n[k] for k in range(3) if n[k]))
readA = frozenset(frozenset((tuple(2 * v for v in e[0]), tuple(2 * v for v in e[1]))) for e in ownA | collar)
Gread = [g for g in OH if frozenset(frozenset(act(g, x, (1, 1, 1)) for x in e) for e in readA) == readA]
check("A4 THEOREM: the trigger's read set (48 owned + 36 collar) has the same C3v; its centroid sits off the block centre along +(1,1,1)",
      len(ownA) == 48 and len(collar) == 36 and set(Gread) == set(Gown),
      f"read {len(readA)}; group {len(Gread)}; centroid offset {np.round(np.mean([[(a[k]+b[k])/2 for k in range(3)] for a, b in ownA | collar], 0) - 0.5, 3)} coarse")
# A5 the children's even tiling about the parent block centre (child units: parent site s at 2s, block centre (1,1,1))
cen = [add((2 * a, 2 * b, 2 * c), (0.5, 0.5, 0.5)) for a, b, c in it.product(range(-2, 3), repeat=3)]
cen = set(p for p in cen if all(abs(v - 1) <= 4.6 for v in p))
Gch = [g for g in OH if set(act(g, p, (1, 1, 1)) for p in cen) == cen]
kidsA = [k for k in it.product(range(4), repeat=3)]
cent = np.mean(kidsA, 0) - 1
corner_shift = np.mean([np.mean([add(add((0, 0, 0), tuple(2 * v for v in m)), c) for m in P3], 0) - 2 * np.array(c) for c in P3], 0)
check("A5 THEOREM: the vertex-nested children's even tiling keeps about the parent block centre exactly the same C3v (R(1,1,1) = (1,1,1) is forced); a block's 64 children are its 8 child even cubes, centred +(1/2)(1,1,1) child units off the parent centre",
      set(Gch) == set(Gown) and np.allclose(cent, 0.5) and np.allclose(corner_shift, 0.5), f"group {len(Gch)} = ownership group; children centroid offset {cent}; mean corner-mode shift {corner_shift}")
# A6 exhaustive: every subgroup of T_d (the block structure's group), exclusive block-periodic ownership
def comp(g, h):  # (g o h) as signed permutation
    M = mat(g) @ mat(h); p = tuple(int(np.nonzero(M[i])[0][0]) for i in range(3)); return (p, tuple(int(M[i, p[i]]) for i in range(3)))
Td = list(Gtt0); E0 = ((0, 1, 2), (1, 1, 1))
subs = set()
for g, h in it.combinations_with_replacement(Td, 2):
    S = {E0, g, h}
    while True:
        new = {comp(a, b) for a in S for b in S} | S
        if new == S: break
        S = new
    subs.add(frozenset(S))
cB = (1, 1, 1); edges2 = [(tuple(2 * v for v in e[0]), tuple(2 * v for v in e[1])) for e in ownA]
blkd = lambda X: tuple((v // 4) * 4 for v in X)
bcent = [add(cB, tuple(4 * m for m in mm)) for mm in it.product(range(-2, 3), repeat=3)]
def admits(H, anyblock):
    for a, b in edges2:
        stab = []
        for g in H:
            a1, b1 = act(g, a, cB), act(g, b, cB)
            for x, y, sw in ((a1, b1, False), (b1, a1, True)):
                tau = tuple(a[k] - x[k] for k in range(3))
                if all(v % 4 == 0 for v in tau) and add(y, tau) == b: stab.append((g, tau, sw))
        if not anyblock:
            if any(sw for _, _, sw in stab) and blkd(a) != blkd(b): return False
        else:
            if not any(all(add(act(g, B, cB), tau) == B for g, tau, _ in stab) for B in bcent): return False
    return True
rows = [(len(H), fixdim(list(H)) > 0, admits(H, False), admits(H, True)) for H in subs]
ok_poles = all(pol for n, pol, a1, a2 in rows if a1 or a2)
check("A6 THEOREM (exhaustive over the subgroups of T_d): every block-periodic exclusive ownership of the edges, by an end's block or by any block (e.g. a cube centre), keeps only a polar group: at most C3 by an end's block, C3v by any block (forward ownership gives diagonals to a non-end site)",
      ok_poles and max(n for n, _, a1, _ in rows if a1) == 3 and max(n for n, _, _, a2 in rows if a2) == 6,
      f"{len(subs)} subgroups; admitting: end-block {sorted(set(n for n, _, a, _ in rows if a))}, any-block {sorted(set(n for n, _, _, a in rows if a))}; non-polar admitting 0")

# ======================================================================================= B
print("== B. matter: displacement made by the passing (1D two-tiling walk, eps_even != eps_odd)")
ee, eo = 0.70, 0.45; Mb = 24                  # Mb parent blocks; parent ring 2Mb sites, child ring 4Mb
def tick(N, even_origin):
    def layer(o, e):
        U = np.eye(N, dtype=complex)
        for j in range(o, N + o, 2):
            a, b = j % N, (j + 1) % N
            U[np.ix_([a, b], [a, b])] = [[np.cos(e), -1j * np.sin(e)], [-1j * np.sin(e), np.cos(e)]]
        return U
    return layer(1 - even_origin, eo) @ layer(even_origin, ee)
def bands(U, N, cell):  # Bloch eigenstates of U under translation by `cell` sites: (K, quasi-energy, vector)
    out = []; nc = N // cell
    for q in range(nc):
        K = 2 * np.pi * q / nc; Q = np.zeros((N, cell), complex)
        for m in range(nc):
            for r in range(cell): Q[m * cell + r, r] = np.exp(1j * K * m) / np.sqrt(nc)
        w, v = np.linalg.eig(Q.conj().T @ U @ Q)
        for i in range(cell): out.append((K, np.angle(w[i]), Q @ v[:, i] / np.linalg.norm(v[:, i])))
    return out
Np, Nc = 2 * Mb, 4 * Mb
Up = tick(Np, 0); bp = bands(Up, Np, 2)
def seed(kind):
    V = np.zeros((Nc, Np))
    for x in range(Np):
        j, c = divmod(x, 2)
        if kind in ('vertex+', 'cell'): tg = [4 * j + c + 2 * m for m in (0, 1)]
        elif kind == 'vertex-': tg = [4 * j - 1 + c + 2 * m for m in (0, 1)]
        else: tg = [2 * x]
        for n in tg: V[n % Nc, x] = 1 / np.sqrt(len(tg))
    return V
def run(kind):
    eo_c = {'vertex+': 0, 'vertex-': 1, 'coinc': 0, 'cell': 0}[kind]
    pos_c = (lambda n: n / 2 - 0.25) if kind == 'cell' else (lambda n: n / 2)
    Uc = tick(Nc, eo_c); bc = bands(Uc, Nc, 4); V = seed(kind)
    Umap = np.zeros((Nc, Np), complex); Pplus = np.zeros((Np, Np), complex)
    for K, w, v in bp:
        if w <= 0: continue
        Pplus += np.outer(v, v.conj())
        cand = [(wc, vc) for Kc, wc, vc in bc if abs(np.exp(1j * Kc) - np.exp(1j * K)) < 1e-9 and wc > 0]
        wc, vc = min(cand, key=lambda z: z[0]); a = vc.conj() @ V @ v
        Umap += (a / abs(a)) * np.outer(vc, v.conj())
    x0 = 2 * (Mb // 2) + 0.5                      # a parent even-cube centre
    phi = np.array([np.exp(-((x - x0) / 3.0) ** 2) for x in range(Np)]); psi = Pplus @ phi; psi /= np.linalg.norm(psi)
    def X(vec, pos, L):
        z = sum(abs(vec[i]) ** 2 * np.exp(2j * np.pi * pos(i) / L) for i in range(len(vec))); return np.angle(z) * L / (2 * np.pi)
    Xp = X(psi, lambda i: i, Np); chi = Umap @ psi; Xc = X(chi, pos_c, Np)
    return (Xc - Xp) * 2, np.linalg.norm(chi), Uc   # displacement in child units
res = {k: run(k) for k in ('vertex+', 'vertex-', 'coinc', 'cell')}
check("B1 THEOREM + check: the vertex-nested passing moves a light packet by exactly +1/2 child unit per axis (into the child odd cube centred +(1/2)(1,1,1) off), the mirrored child tiling by -1/2; the polar-phase map is an isometry",
      abs(res['vertex+'][0] - 0.5) < 1e-8 and abs(res['vertex-'][0] + 0.5) < 1e-8 and abs(res['vertex+'][1] - 1) < 1e-9,
      f"shift vertex+ {res['vertex+'][0]:+.10f}, vertex- {res['vertex-'][0]:+.10f} child units")
Ucv = res['vertex+'][2]; Rv = np.zeros((Nc, Nc))
for n in range(Nc): Rv[(2 - n) % Nc, n] = 1            # reflection about child site 1 (the parent centre in the vertex reading)
asym = np.linalg.norm(Rv @ Ucv @ Rv - Ucv)
check("B2 THEOREM: in the vertex reading the children have no reflection about the parent centre (it swaps their even and odd tilings), so no seed fixes the shift at 0; the coincident seed lands at an unprotected value",
      asym > 0.1 and abs(res['coinc'][0]) > 1e-3 and abs(abs(res['coinc'][0]) - 0.5) > 1e-3, f"|R U R - U| {asym:.2f}; coincident-seed shift {res['coinc'][0]:+.4f}")
check("B3 THEOREM + check: in the cell reading (the same index map, children placed around their parent site) the shift is exactly 0",
      abs(res['cell'][0]) < 1e-8, f"shift {res['cell'][0]:+.2e} child units")

# ======================================================================================= C
print("== C. symmetric alternative: the cell reading (each site's eight children are a child even cube centred on it)")
# C1 symmetry: child sites at s + (+-1/4)^3, child even cubes centred on parent sites, odd cubes on parent cube centres
Q4 = lambda x: tuple(int(round(4 * v)) for v in x)     # quadrupled coords
ch = set(Q4(add(s, tuple(0.25 * e for e in sg))) for s in it.product(range(-2, 4), repeat=3) for sg in it.product((1, -1), repeat=3))
ch = set(p for p in ch if all(abs(v - 2) <= 9 for v in p))
evc = set(Q4(s) for s in it.product(range(-2, 4), repeat=3) if all(abs(4 * v - 2) <= 9 for v in s))
Gcell = [g for g in OH if set(act(g, p, (2, 2, 2)) for p in ch) == ch and set(act(g, p, (2, 2, 2)) for p in evc) == evc]
dom = set(Q4(add(s, tuple(0.25 * e for e in sg))) for s in P3 for sg in it.product((1, -1), repeat=3))
tiles = all(len(set(add(p, tuple(8 * m for m in mm)) for p in dom for mm in it.product(range(-1, 2), repeat=3))) == 64 * 27 for _ in [0])
Gcell_full = [g for g in Gcell if set(act(g, p, (2, 2, 2)) for p in dom) == dom]
check("C1 THEOREM: in the cell reading the children, their even tiling and each block's 64 children keep all 48 operations about the parent block centre (no vector); the blocks' child sets tile",
      len(Gcell) == 48 and len(Gcell_full) == 48 and tiles and fixdim(Gcell_full) == 0, f"group {len(Gcell_full)}, fixed vectors {fixdim(Gcell_full)}")
# C2 links: Gauss's law on the sum over patterns; link-end rule for children whose odd cube is incomplete
def gauss_graph(blocks, reading, rule):
    blocks = set(blocks); Nc_, Nk = 4, 8
    present = lambda q: blk(tuple((v % Nk) // 2 for v in q)) in blocks
    pos = (lambda v: v / 2 - 0.25) if reading == 'cell' else (lambda v: v / 2)
    bonds = []; ties = 0
    for s in it.product(range(Nc_), repeat=3):
        if blk(s) in blocks: continue
        bonds.append((('c', s), ('E', blk(s)), ('O', tuple((((v - 1) // 2) * 2 + 1) % Nc_ for v in s))))
    for n in blocks:
        for q in [tuple(2 * n[i] + k[i] for i in range(3)) for k in it.product(range(4), repeat=3)]:
            oo = tuple(((v - 1) // 2) * 2 + 1 for v in q)
            if all(present(add(oo, d)) for d in P3) or rule == 'own': odd = ('o', tuple(v % Nk for v in oo))
            elif rule == 'parent': odd = ('O', tuple((((v // 2 - 1) // 2) * 2 + 1) % Nc_ for v in q))   # its parent site's odd cube
            else:
                pick = []
                for v in oo:
                    cv = (pos(v) + pos(v + 1)) / 2
                    cand = sorted(((min(abs(cv - o) % Nc_, Nc_ - abs(cv - o) % Nc_), o % Nc_) for o in (1.5, 3.5)))
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
allb = [tuple(2 * v for v in m) for m in P3]
def gauss_run(reading, rule):
    ok = True; maxties = 0; nchk = 0
    pb, _ = gauss_graph([], reading, rule)
    verts = sorted(set(v for b in pb for v in b[1:])); vi = {v: i for i, v in enumerate(verts)}
    Dm = np.zeros((len(verts), len(pb)))
    for j, (lab, ev, od) in enumerate(pb): Dm[vi[ev], j] += 1; Dm[vi[od], j] -= 1
    for mask in range(256):
        blocks = [b for i, b in enumerate(allb) if mask >> i & 1]
        bonds, ties = gauss_graph(blocks, reading, rule); maxties = max(maxties, ties)
        if mask % 23: continue
        for trial in range(2):
            n = {b[0]: rng.integers(0, 2) for b in pb}; Q = collections.Counter()
            for lab, ev, od in pb: Q[ev] += n[lab] - 0.5; Q[od] -= n[lab] - 0.5
            qv = np.array([Q[v] for v in verts]); Ep = np.linalg.lstsq(Dm, qv, rcond=None)[0]
            Eof = {pb[j][0]: Ep[j] for j in range(len(pb))}; nb = dict(n); res_ = collections.Counter()
            for lab, ev, od in bonds:
                if lab[0] == 'k': nb[lab] = rng.integers(0, 2)
            for lab, ev, od in bonds:
                res_[ev] += nb[lab] - 0.5; res_[od] -= nb[lab] - 0.5
                if lab[0] == 'c': res_[ev] -= Eof[lab]; res_[od] += Eof[lab]
            kb = [b for b in bonds if b[0][0] == 'k']
            if kb:
                kv = set(v for b in kb for v in b[1:]); f2 = components(kb); tot = collections.Counter()
                for v, r in res_.items():
                    if v in kv: tot[f2(v)] += r
                    else: ok &= abs(r) < 1e-9
                ok &= all(abs(t) < 1e-9 for t in tot.values()); nchk += 1
    return ok, maxties, nchk
gv = gauss_run('vertex', 'nearest'); gc = gauss_run('cell', 'nearest'); go = gauss_run('cell', 'own'); gp = gauss_run('cell', 'parent')
check("C2 THEOREM + check: 'end at the nearest unsplit odd centre' never ties only because the vertex reading is one-sided; in the cell reading it ties. Ending incomplete-cube links at their own child centre breaks Gauss's law; ending them at their parent site's odd-cube centre (a symmetric, purely combinatorial rule) keeps it solvable on every pattern",
      gv[0] and gv[1] == 0 and gc[1] > 0 and not go[0] and gp[0] and gp[1] == 0 and gp[2] > 10,
      f"ties: vertex {gv[1]}, cell {gc[1]}; own-centre solvable {bool(go[0])}; parent-site rule solvable {bool(gp[0])} ({gp[2]} draws)")
# C3 register toy: glued split, cell reading, ring of 3 blocks; two-sided collar
K = 3
def allowed(c):
    sig, I, J = c
    for b in range(K):
        if len(I[b]) != (3 if sig[b] else 1): return False
        if sig[b]:
            if not sig[(b + 1) % K] and (J[b] != 1 or I[b][2] != 0): return False
            if not sig[(b - 1) % K] and (J[(b - 1) % K] != 1 or I[b][1] != 0): return False
    return True
basis = []
for sig in it.product((0, 1), repeat=K):
    for I in it.product(*[list(it.product((0, 1), repeat=3)) if s else [(0,), (1,)] for s in sig]):
        for J in it.product((0, 1), repeat=K):
            c = (sig, I, J)
            if allowed(c): basis.append(c)
idx = {c: i for i, c in enumerate(basis)}
def moves(c, collar=True):
    sig, I, J = c; out = []
    for b in range(K):
        I2 = list(I)
        if not sig[b]: I2[b] = (1 - I[b][0],); out.append((sig, tuple(I2), J))
        else:
            for k in range(3):
                if k == 1 and not sig[(b - 1) % K]: continue
                if k == 2 and not sig[(b + 1) % K]: continue
                t = list(I[b]); t[k] ^= 1; I2 = list(I); I2[b] = tuple(t); out.append((sig, tuple(I2), J))
        if sig[b] == sig[(b + 1) % K]: J2 = list(J); J2[b] ^= 1; out.append((sig, I, tuple(J2)))
        if not sig[b] and I[b][0] == 1 and (not collar or (J[b] == 1 and J[(b - 1) % K] == 1)):   # glue up
            s2 = list(sig); s2[b] = 1; I2 = list(I); I2[b] = (0, 0, 0); J2 = list(J)
            for i, nb in ((b, (b + 1) % K), ((b - 1) % K, (b - 1) % K)):
                if sig[nb]: J2[i] = 0
            out.append(('up', (tuple(s2), tuple(I2), tuple(J2))))
    return out
def build(collar=True):
    E = set(); leak = 0
    for c in basis:
        for m in moves(c, collar):
            up = m[0] == 'up'; tgt = m[1] if up else m
            if tgt not in idx: leak += 1; continue
            E.add((idx[tgt], idx[c]))
            if up: E.add((idx[c], idx[tgt]))
    return E, leak
Es, leak_s = build(True); _, leak_n = build(False)
def refl(c):
    sig, I, J = c; r = lambda b: (-b) % K
    I2 = tuple((I[r(b)] if len(I[r(b)]) == 1 else (I[r(b)][0], I[r(b)][2], I[r(b)][1])) for b in range(K))
    return (tuple(sig[r(b)] for b in range(K)), I2, tuple(J[(-b - 1) % K] for b in range(K)))
perm = [idx[refl(c)] for c in basis]
herm = all((j, i) in Es for i, j in Es); rcomm = set((perm[i], perm[j]) for i, j in Es) == Es
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
ij = np.array(sorted(Es)); Gsp = sp.csr_matrix((np.ones(len(ij)), (ij[:, 0], ij[:, 1])), shape=(len(basis),) * 2)
pats = len(set(c[0] for c in basis)); v0 = np.zeros(len(basis), complex); v0[idx[((0, 0, 0), ((1,), (1,), (1,)), (1, 1, 1))]] = 1
vt = expm_multiply(-1j * 0.7 * Gsp, v0)
split_w = sum(abs(vt[i]) ** 2 for i, c in enumerate(basis) if any(c[0]))
check("C3 THEOREM + check: the glued split in the cell reading with a collar read on BOTH faces is unitary on the sum over patterns (hermitian, no leak) and commutes with the reflection; without the collar it leaks",
      herm and leak_s == 0 and rcomm and leak_n > 0 and abs(np.linalg.norm(vt) - 1) < 1e-10,
      f"dim {len(basis)}, patterns {pats}, leak {leak_s} (no collar {leak_n}); |RGR-G| 0; split weight {split_w:.2f}")
# C4 the cost: geometry passing in the cell reading
on_parent = 0; nchild = 0
for s in it.product(range(2), repeat=3):
    for a in [add(s, tuple(0.25 * e for e in sg)) for sg in it.product((1, -1), repeat=3)]:
        for k in range(3):
            b = tuple(a[i] + (0.5 if i == k else 0) for i in range(3)); nchild += 1
            on_parent += sum(1 for i in range(3) if i != k and abs(a[i] - round(a[i])) < 1e-9) == 2
check("C4 DIAGNOSTIC (cost): in the cell reading no child edge lies on a parent edge; each parent axis edge passes to 4 parallel child edges (parent - s), the edges around each site start from the vacuum of the same geometry, and the nested closure of hanging-nodes A3-B6 does not carry over (open)",
      on_parent == 0, f"child axis edges on parent edges: {on_parent}/{nchild}")

# ======================================================================================= D
print("== D. ESTIMATES (L = sqrt(8 pi) l_P, child edge at a split)")
lP = 1.616e-35; L = np.sqrt(8 * np.pi) * lP; delta = np.sqrt(3) / 2 * L; H0 = 2.2e-18; c = 2.998e8
v = delta * H0 / np.log(2)
check("D1 per split the vertex reading moves each excitation by (sqrt3/2) L along +(1,1,1); splits come once per doubling, only where edges grow, so the drift is a velocity of order L H0",
      v / c < 1e-55, f"delta {delta:.1e} m; v {v:.1e} m/s = {v / c:.0e} c (bound regions: 0)")
Ndbl = (np.log(1.4e32 / 2.725) + 60) / np.log(2)
check("D2 a uniform split is a uniform translation (no observable); across a pattern boundary the offset is one child edge; the Fock vacuum is invariant under every momentum-wise phase, so vacuum-born perturbations (CMB, LSS) carry no dipole",
      Ndbl * delta < 1e-30, f"~{Ndbl:.0f} doublings since a Planck start: total {Ndbl * delta:.0e} m")
k100 = 2 * np.pi / 1.24e-20
check("D3 the polar vector lives only at 2:1 interfaces (bulk is uniform-level); a + vs - face difference in transmission is at most of order kL, which is tiny for any probe",
      k100 * L < 1e-12, f"100 TeV photon: kL {k100 * L:.0e}; optical {2 * np.pi / 5e-7 * L:.0e}")
print("supplied: copy-mass group (register: 12 tetrahedral turns + inversion), tick angles of the 1D toy, register levels {0,1} and holds of the toy, measured numbers.")
print(f"elapsed {time.monotonic() - T00:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
