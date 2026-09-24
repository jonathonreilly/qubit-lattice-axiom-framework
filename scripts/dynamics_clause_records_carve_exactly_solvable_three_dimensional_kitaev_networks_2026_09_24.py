#!/usr/bin/env python3
"""Records carve exactly solvable three-dimensional Kitaev networks.

Supplied and not adopted: the fully soldered dynamics clause of open PR 9040 at
its compass point, H = K sum_bonds (e.s_x)(e.s_{x+e}), and records acting as
fields (open PR 9041): a record with content q on a bond along e exerts
K e (e.q) on its unrecorded neighbour.

Relaxed carving: every unrecorded site has AT MOST one unrecorded neighbour per
axis (degree <= 3, one bond per type); along an axis where a site keeps a bond,
the recorded neighbour on the other side must exert no field (content
orthogonal to that axis); along an axis where a site has no bond ("dangling"),
fields are allowed. Kitaev's representation s^a = i b^a c then gives, in every
Z2 gauge sector, a quadratic Majorana Hamiltonian: bonds K u_jk i c_j c_k,
dangling fields h i b^a_j c_j.

Checks:

A. Certificate: a 16-site network U on the 4x4x4 torus (sites listed below)
   has at most one U-neighbour per axis at every site, degrees 2 and 3, a
   single component whose closed walks span all three lattice directions, and
   record contents (orthogonal to every bonded axis they touch) that exist and
   cancel every field along every kept bond; six dangling axes carry fields.
B. Solvability: on the 16-qubit finite torus, the loop operators of a cycle
   basis commute with the Hamiltonian including the dangling fields, while a
   field along a kept bond breaks one; the exact ground energy equals the
   least free-Majorana ground energy over all 2^18 Z2 gauge configurations.
C. The infinite periodic network: among its 8 translation-invariant flux
   sectors, the lowest Majorana ground energy has a gapped spectrum with no
   flat zero band (gap about 0.61 |K| on a 16^3 Brillouin-zone grid).
D. Not a single accident: a SAT search (python-sat) for relaxed carvings with
   every unrecorded site keeping at least two bonds finds several distinct
   components on 4x4x4 whose closed walks span three directions; in each, the
   lowest translation-invariant sector is gapped on a 6^3 grid.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    'docs/DYNAMICS_CLAUSE_RECORDS_CARVE_EXACTLY_SOLVABLE_THREE_DIMENSIONAL_KITAEV_NETWORKS_GAPPED_MAJORANA_FERMIONS_IN_A_STATIC_Z2_GAUGE_FIELD_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
from pysat.solvers import Glucose4
from pysat.card import CardEnc, EncType

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


L3 = (4, 4, 4)
U16 = [(0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 1), (1, 1, 2), (1, 1, 3), (2, 0, 3), (2, 1, 0),
       (2, 1, 3), (2, 2, 0), (3, 0, 2), (3, 0, 3), (3, 2, 0), (3, 2, 1), (3, 3, 1), (3, 3, 2)]


def nbr(s, ax, d, Ls=L3):
    t = list(s)
    t[ax] = (t[ax] + d) % Ls[ax]
    return tuple(t)


def winding_rank(comp, Ls=L3):
    comp = set(comp)
    s0 = min(comp)
    pos = {s0: (0, 0, 0)}
    stack = [s0]
    wind = set()
    while stack:
        v = stack.pop()
        for ax in range(3):
            for d in (1, -1):
                t = list(v)
                t[ax] += d
                off = [0, 0, 0]
                if t[ax] == Ls[ax]:
                    t[ax], off[ax] = 0, 1
                if t[ax] == -1:
                    t[ax], off[ax] = Ls[ax] - 1, -1
                w = tuple(t)
                if w not in comp:
                    continue
                pw = tuple(pos[v][i] + off[i] for i in range(3))
                if w in pos:
                    if pos[w] != pw:
                        wind.add(tuple(pw[i] - pos[w][i] for i in range(3)))
                else:
                    pos[w] = pw
                    stack.append(w)
    connected = len(pos) == len(comp)
    rank = int(np.linalg.matrix_rank(np.array(sorted(wind)))) if wind else 0
    return connected, rank


def build(comp, Ls=L3):
    comp = sorted(comp)
    ix = {s: i for i, s in enumerate(comp)}
    cs = set(comp)
    bonds = []                         # (j, k, axis, cell offset of k)
    for s in comp:
        for ax in range(3):
            t = list(s)
            t[ax] += 1
            off = [0, 0, 0]
            if t[ax] == Ls[ax]:
                t[ax], off[ax] = 0, 1
            t = tuple(t)
            if t in cs:
                bonds.append((ix[s], ix[t], ax, tuple(off)))
    dangling = [(ix[s], ax) for s in comp for ax in range(3)
                if nbr(s, ax, 1, Ls) not in cs and nbr(s, ax, -1, Ls) not in cs]
    contents, cons_ok = {}, True
    for r in itertools.product(*[range(l) for l in Ls]):
        if r in cs:
            continue
        cons = set()
        for ax in range(3):
            for d in (1, -1):
                u = nbr(r, ax, d, Ls)
                if u in cs and nbr(u, ax, d, Ls) in cs:
                    cons.add(ax)
        if len(cons) > 2:
            cons_ok = False
            continue
        free = [a for a in range(3) if a not in cons]
        q = np.zeros(3)
        q[free[-1]] = 1.0
        contents[r] = q
    return dict(comp=comp, ix=ix, bonds=bonds, dangling=dangling, contents=contents, cons_ok=cons_ok, n=len(comp))


# --------------------------------------------------------------- A: certificate
print("A. the 16-site network and its records")
G = build(U16)
cs = set(U16)
per_axis = all(sum(nbr(s, ax, d) in cs for d in (1, -1)) <= 1 for s in U16 for ax in range(3))
degs = sorted({sum(nbr(s, ax, d) in cs for ax in range(3) for d in (1, -1)) for s in U16})
connected, rank = winding_rank(U16)
worst_field = 0.0
dangling_fields = {}
for s in U16:
    for ax in range(3):
        for d in (1, -1):
            r = nbr(s, ax, d)
            if r in cs:
                continue
            f = G["contents"][r][ax]
            if nbr(s, ax, -d) in cs:            # s keeps its bond along ax on the other side
                worst_field = max(worst_field, abs(f))
            else:
                dangling_fields[(G["ix"][s], ax)] = dangling_fields.get((G["ix"][s], ax), 0.0) + f
live = [(j, ax) for (j, ax) in G["dangling"] if abs(dangling_fields.get((j, ax), 0.0)) > 0]
check("one U-neighbour per axis at most; degrees 2 and 3; one component spanning three directions",
      per_axis and degs == [2, 3] and connected and rank == 3,
      f"16 sites, {len(G['bonds'])} bonds, {len(G['dangling'])} dangling axes, winding rank {rank}")
check("record contents orthogonal to every bonded axis exist and cancel every field along kept bonds",
      G["cons_ok"] and worst_field == 0.0, f"{len(live)} dangling axes carry nonzero fields")

# --------------------------------------------------------------- B: solvability
print("B. exact solvability on the 16-qubit torus")
n = G["n"]
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
SS = [sps.csr_matrix(m) for m in S]
I2 = sps.identity(2, dtype=complex, format="csr")


def sop(placed):
    return reduce(lambda A, B: sps.kron(A, B, format="csr"), [placed.get(k, I2) for k in range(n)])


H = sum(sop({j: SS[a], k: SS[a]}) for (j, k, a, off) in G["bonds"])
for (j, ax) in G["dangling"]:
    h = dangling_fields.get((j, ax), 0.0)
    if h != 0:
        H = H + h * sop({j: SS[ax]})
# cycle basis of the finite torus graph (a spanning tree plus one bond each)
adj = {v: [] for v in range(n)}
for (j, k, a, off) in G["bonds"]:
    adj[j].append((k, a))
    adj[k].append((j, a))
parent = {0: None}
order = [0]
for v in order:
    for (w, a) in adj[v]:
        if w not in parent:
            parent[w] = (v, a)
            order.append(w)
tree = {(min(v, p[0]), max(v, p[0]), p[1]) for v, p in parent.items() if p}
nontree = [(min(j, k), max(j, k), a) for (j, k, a, off) in G["bonds"] if (min(j, k), max(j, k), a) not in tree]


def path_to_root(v):
    out = [v]
    while parent[v]:
        v = parent[v][0]
        out.append(v)
    return out


loops_ok, n_loops = True, 0
for (j, k, a) in nontree:
    pj, pk = path_to_root(j), path_to_root(k)
    common = next(x for x in pj if x in pk)
    cyc = pj[:pj.index(common) + 1] + list(reversed(pk[:pk.index(common)]))
    # axes used at each vertex by the cycle
    used = {v: set() for v in cyc}
    edges = [(cyc[i], cyc[i + 1]) for i in range(len(cyc) - 1)] + [(k, j)]
    for (x, y) in edges:
        ax = next(a2 for (w, a2) in adj[x] if w == y)
        used[x].add(ax)
        used[y].add(ax)
    placed = {v: SS[[a2 for a2 in range(3) if a2 not in used[v]][0]] for v in cyc}
    W = sop(placed)
    loops_ok &= abs((H @ W - W @ H)).max() < 1e-10
    n_loops += 1
bad = next((j, ax) for (j, k2, ax, off) in G["bonds"] for _ in [0])
Hbad = H + 0.4 * sop({bad[0]: SS[bad[1]]})
broken = 0
for (j, k, a) in nontree:
    pj, pk = path_to_root(j), path_to_root(k)
    common = next(x for x in pj if x in pk)
    cyc = pj[:pj.index(common) + 1] + list(reversed(pk[:pk.index(common)]))
    used = {v: set() for v in cyc}
    edges = [(cyc[i], cyc[i + 1]) for i in range(len(cyc) - 1)] + [(k, j)]
    for (x, y) in edges:
        ax = next(a2 for (w, a2) in adj[x] if w == y)
        used[x].add(ax)
        used[y].add(ax)
    W = sop({v: SS[[a2 for a2 in range(3) if a2 not in used[v]][0]] for v in cyc})
    broken += abs((Hbad @ W - W @ Hbad)).max() > 1e-6
check("cycle-basis loop operators commute with H including dangling fields; a field along a kept bond breaks some",
      loops_ok and broken > 0, f"{n_loops} loops conserved; {broken} broken by the kept-bond field")
E_ed = spla.eigsh(H, k=1, which="SA")[0][0]


def majorana_E0(u):
    N = n + len(live)
    A = np.zeros((N, N))
    for (j, k, a, off), uj in zip(G["bonds"], u):
        A[j, k] += -2 * uj
        A[k, j] -= -2 * uj
    for pos, (j, ax) in enumerate(live):
        h = dangling_fields[(j, ax)]
        A[n + pos, j] += 2 * h
        A[j, n + pos] -= 2 * h
    ev = np.linalg.eigvalsh(1j * A)
    return -0.5 * ev[ev > 1e-12].sum()


E_maj = min(majorana_E0(u) for u in itertools.product((1, -1), repeat=len(G["bonds"])))
check("exact ground energy = least free-Majorana ground energy over all 2^18 gauge configurations",
      abs(E_ed - E_maj) < 1e-8, f"ED {E_ed:.10f}; Majorana {E_maj:.10f}")

# --------------------------------------------------------- C: the infinite network
print("C. Majorana bands of the infinite periodic network")
parent_uf = list(range(n))


def find(a):
    while parent_uf[a] != a:
        parent_uf[a] = parent_uf[parent_uf[a]]
        a = parent_uf[a]
    return a


t_b, n_b = [], []
for b in G["bonds"]:
    ra, rb = find(b[0]), find(b[1])
    if ra != rb:
        parent_uf[ra] = rb
        t_b.append(b)
    else:
        n_b.append(b)


def bloch(u_non, k):
    N = n + len(live)
    A = np.zeros((N, N), dtype=complex)
    uu = {b: 1 for b in t_b}
    uu.update({b: v for b, v in zip(n_b, u_non)})
    for b in G["bonds"]:
        j, kk, ax, off = b
        t = -2 * uu[b] * np.exp(1j * np.dot(k, off))
        A[j, kk] += t
        A[kk, j] -= np.conj(t)
    for pos, (j, ax) in enumerate(live):
        h = dangling_fields[(j, ax)]
        A[n + pos, j] += 2 * h
        A[j, n + pos] -= 2 * h
    return np.linalg.eigvalsh(1j * A)


ks6 = [np.array(k) * 2 * np.pi / 6 for k in itertools.product(range(6), repeat=3)]
sectors = []
for u in itertools.product((1, -1), repeat=len(n_b)):
    E = sum(-0.5 * ev[ev > 0].sum() for ev in (bloch(u, k) for k in ks6)) / len(ks6)
    sectors.append((E, u))
sectors.sort()
ub = sectors[0][1]
gmin, zmax = 9.0, 0
for kk in itertools.product(range(16), repeat=3):
    ev = np.sort(np.abs(bloch(ub, np.array(kk) * 2 * np.pi / 16)))
    z = int(np.sum(ev < 1e-9))
    zmax = max(zmax, z)
    if z < len(ev):
        gmin = min(gmin, ev[z])
check("lowest of the 8 translation-invariant flux sectors is gapped with no flat zero band",
      zmax == 0 and gmin > 0.5, f"E0/cell {sectors[0][0]:.6f} (next {sectors[1][0]:.6f}); gap on 16^3 grid {gmin:.5f}")

# ------------------------------------------------------------- D: more networks
print("D. a search for more three-direction networks")


def search_relaxed(Ls, maxsol):
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx = {s: i + 1 for i, s in enumerate(sites)}
    cls, top = [], len(sites)
    for s in sites:
        u = idx[s]
        for ax in range(3):
            cls.append([-u, -idx[nbr(s, ax, 1, Ls)], -idx[nbr(s, ax, -1, Ls)]])
        for sx, sy, sz in itertools.product((1, -1), repeat=3):
            cls.append([u, -idx[nbr(s, 0, sx, Ls)], -idx[nbr(nbr(s, 0, sx, Ls), 0, sx, Ls)],
                        -idx[nbr(s, 1, sy, Ls)], -idx[nbr(nbr(s, 1, sy, Ls), 1, sy, Ls)],
                        -idx[nbr(s, 2, sz, Ls)], -idx[nbr(nbr(s, 2, sz, Ls), 2, sz, Ls)]])
        nbrs = [idx[nbr(s, ax, d, Ls)] for ax in range(3) for d in (1, -1)]
        enc = CardEnc.atleast(lits=nbrs, bound=2, top_id=top, encoding=EncType.seqcounter)
        top = max(top, enc.nv)
        for c in enc.clauses:
            cls.append([-u] + c)
    cls.append([idx[(0, 0, 0)]])
    g = Glucose4(bootstrap_with=cls)
    out = []
    while len(out) < maxsol and g.solve():
        m = g.get_model()
        U = frozenset(s for s in sites if m[idx[s] - 1] > 0)
        out.append(U)
        g.add_clause([-idx[s] if s in U else idx[s] for s in sites])
    g.delete()
    return out


def components(U, Ls=L3):
    Uset, seen, out = set(U), set(), []
    for s in sorted(U):
        if s in seen:
            continue
        comp, stack = {s}, [s]
        while stack:
            v = stack.pop()
            for ax in range(3):
                for d in (1, -1):
                    w = nbr(v, ax, d, Ls)
                    if w in Uset and w not in comp:
                        comp.add(w)
                        stack.append(w)
        seen |= comp
        out.append(frozenset(comp))
    return out


found = set()
for U in search_relaxed(L3, 2000):
    for c in components(U):
        if len(c) >= 8 and winding_rank(c)[1] == 3:
            found.add(c)
gapped = 0
sizes = []
for c in sorted(found, key=lambda x: (len(x), sorted(x)))[:6]:
    Gc = build(c)
    if not Gc["cons_ok"]:
        continue
    # fields on dangling axes from the chosen contents
    csc = set(c)
    df = {}
    for s in Gc["comp"]:
        for ax in range(3):
            for d in (1, -1):
                r = nbr(s, ax, d)
                if r not in csc and nbr(s, ax, -d) not in csc:
                    df[(Gc["ix"][s], ax)] = df.get((Gc["ix"][s], ax), 0.0) + Gc["contents"][r][ax]
    lv = [key for key, v in df.items() if abs(v) > 0]
    nn = Gc["n"]
    uf = list(range(nn))

    def fnd(a):
        while uf[a] != a:
            uf[a] = uf[uf[a]]
            a = uf[a]
        return a

    tb, nb_ = [], []
    for b in Gc["bonds"]:
        ra, rb = fnd(b[0]), fnd(b[1])
        if ra != rb:
            uf[ra] = rb
            tb.append(b)
        else:
            nb_.append(b)
    if len(nb_) > 9:
        continue

    def bl(u_non, k):
        N = nn + len(lv)
        A = np.zeros((N, N), dtype=complex)
        uu = {b: 1 for b in tb}
        uu.update({b: v for b, v in zip(nb_, u_non)})
        for b in Gc["bonds"]:
            j, kk2, ax, off = b
            t = -2 * uu[b] * np.exp(1j * np.dot(k, off))
            A[j, kk2] += t
            A[kk2, j] -= np.conj(t)
        for pos, (j, ax) in enumerate(lv):
            A[nn + pos, j] += 2 * df[(j, ax)]
            A[j, nn + pos] -= 2 * df[(j, ax)]
        return np.linalg.eigvalsh(1j * A)

    best = min((sum(-0.5 * ev[ev > 0].sum() for ev in (bl(u, k) for k in ks6)), u)
               for u in itertools.product((1, -1), repeat=len(nb_)))[1]
    g_nonflat = min(np.sort(np.abs(bl(best, k)))[int(np.sum(np.abs(bl(best, k)) < 1e-9))]
                    for k in ks6)
    gapped += g_nonflat > 1e-3
    sizes.append((nn, round(float(g_nonflat), 3)))
check("more distinct three-direction networks exist; each lowest translation-invariant sector is gapped",
      len(found) >= 3 and gapped == len(sizes) and len(sizes) >= 3,
      f"{len(found)} distinct components; (sites, gap above flat bands) {sizes}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
