#!/usr/bin/env python3
"""Records carve exactly solvable three-dimensional Kitaev networks.

Supplied and not adopted: the fully soldered dynamics clause of open PR 9040 at
its compass point, H = K sum_bonds (e.s_x)(e.s_{x+e}) (K = 1 below), and records
acting as fields (open PR 9041): a record with content q on a bond along e
exerts K e (e.q) on its unrecorded neighbour.

Relaxed carving: every unrecorded site has AT MOST one unrecorded neighbour per
axis; along an axis where a site keeps a bond, the recorded neighbour on the
other side exerts no field (content orthogonal to that axis); along a
"dangling" axis (no bond) fields are allowed. Kitaev's representation
s^a = i b^a c then gives, in every Z2 gauge sector, a quadratic Majorana
Hamiltonian. A network's local loops per cell are beta1 - 3, where beta1 is
the cycle rank of its cell graph and 3 is the winding rank: they carry the
gauge-invariant Z2 flux of the infinite network.

Checks:

A. Two certificates on the 4x4x4 torus, both single components whose closed
   walks span three directions, with record contents that cancel every field
   along kept bonds: a 20-site network with one local loop per cell and a
   16-site network with none (its infinite lift is a tree).
B. Exact solvability: for the 16-site network the cycle-basis loop operators
   commute with H (a field along a kept bond breaks some) and the exact
   ground energy equals the least free-Majorana energy over all 2^18 gauge
   configurations; for the 20-site network the exact ground energy (matrix-
   free Lanczos on 20 qubits) equals the least free-Majorana energy over its
   16 gauge classes.
C. The 20-site network: its translation-invariant flux sectors split by the
   local flux; the lowest has two flat zero-mode bands per cell (localized
   Majorana zero modes) and a gap above them; in a 2x2x2 supercell flipping
   any bond on a local loop (a vison) costs a positive energy while every
   other flip costs 0; cells doubled along x, y or z find no lower flux
   pattern. The 16-site tree has all flux sectors degenerate (pure gauge).
D. A SAT search (python-sat) finds more distinct three-direction networks on
   4x4x4, most with local loops; each lowest translation-invariant sector is
   gapped above its flat zero-mode bands on a 6^3 grid.

Record contents are generic: (1, sqrt 2, sqrt 3) projected orthogonal to each
record's constrained axes, so every dangling axis carries a nonzero field and
no dangling Majorana is left decoupled.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 1200
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
# generic record contents: the fixed direction (1, sqrt 2, sqrt 3) projected
# orthogonal to each record's constrained axes; its components are positive,
# so the two records on a dangling axis never cancel
V_GENERIC = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0)]) / np.sqrt(6.0)
N20 = [(0, 0, 0), (0, 0, 3), (0, 1, 0), (0, 2, 1), (0, 2, 2), (0, 3, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0),
       (1, 1, 1), (1, 2, 1), (2, 0, 1), (2, 0, 2), (2, 1, 1), (2, 1, 2), (3, 0, 0), (3, 1, 2), (3, 2, 2),
       (3, 3, 0), (3, 3, 1)]
N16 = [(0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 1), (1, 1, 2), (1, 1, 3), (2, 0, 3), (2, 1, 0),
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
    rank = int(np.linalg.matrix_rank(np.array(sorted(wind)))) if wind else 0
    return len(pos) == len(comp), rank


def build(comp, Ls=L3):
    comp = sorted(comp)
    ix = {s: i for i, s in enumerate(comp)}
    cs = set(comp)
    bonds = []
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
        q = V_GENERIC.copy()
        for a in cons:
            q[a] = 0.0
        contents[r] = q / np.linalg.norm(q)
    kept_field, dfield = 0.0, {}
    for s in comp:
        for ax in range(3):
            for d in (1, -1):
                r = nbr(s, ax, d, Ls)
                if r in cs:
                    continue
                f = contents[r][ax] if r in contents else 0.0
                if nbr(s, ax, -d, Ls) in cs:
                    kept_field = max(kept_field, abs(f))
                else:
                    dfield[(ix[s], ax)] = dfield.get((ix[s], ax), 0.0) + f
    live = [key for key, v in dfield.items() if abs(v) > 0]
    uf = list(range(len(comp)))

    def fnd(a):
        while uf[a] != a:
            uf[a] = uf[uf[a]]
            a = uf[a]
        return a

    tree, non = [], []
    for b in bonds:
        ra, rb = fnd(b[0]), fnd(b[1])
        if ra != rb:
            uf[ra] = rb
            tree.append(b)
        else:
            non.append(b)
    per_axis = all(sum(nbr(s, ax, d, Ls) in cs for d in (1, -1)) <= 1 for s in comp for ax in range(3))
    return dict(comp=comp, ix=ix, n=len(comp), bonds=bonds, dfield=dfield, live=live, tree=tree, non=non,
                cons_ok=cons_ok, kept_field=kept_field, per_axis=per_axis,
                ndangling=sum(1 for s in comp for ax in range(3)
                              if nbr(s, ax, 1, Ls) not in cs and nbr(s, ax, -1, Ls) not in cs))


def majorana_matrix(G, u_all, k=None):
    n = G["n"]
    N = n + len(G["live"])
    A = np.zeros((N, N), dtype=complex)
    for (j, kk, ax, off), ub in zip(G["bonds"], u_all):
        t = -2 * ub * (np.exp(1j * np.dot(k, off)) if k is not None else 1.0)
        A[j, kk] += t
        A[kk, j] -= np.conj(t)
    for pos, (j, ax) in enumerate(G["live"]):
        h = G["dfield"][(j, ax)]
        A[n + pos, j] += 2 * h
        A[j, n + pos] -= 2 * h
    return A


def u_from_non(G, u_non):
    uu = {b: 1 for b in G["tree"]}
    uu.update({b: v for b, v in zip(G["non"], u_non)})
    return [uu[b] for b in G["bonds"]]


def E_finite(G, u_all):
    ev = np.linalg.eigvalsh(1j * majorana_matrix(G, u_all))
    return -0.5 * ev[ev > 1e-12].sum()


def bloch(G, u_non, k):
    return np.linalg.eigvalsh(1j * majorana_matrix(G, u_from_non(G, u_non), np.array(k, dtype=float)))


# --------------------------------------------------------------- A: certificates
print("A. two three-direction networks on the 4x4x4 torus")
G20, G16 = build(N20), build(N16)
info = {}
okA = True
for name, comp, G in (("20-site", N20, G20), ("16-site", N16, G16)):
    conn, rank = winding_rank(comp)
    beta1 = len(G["bonds"]) - G["n"] + 1
    info[name] = (beta1 - 3, G["ndangling"], len(G["live"]))
    okA &= conn and rank == 3 and G["per_axis"] and G["cons_ok"] and G["kept_field"] == 0.0
check("both are relaxed carvings spanning three directions, with fields cancelled along kept bonds", okA,
      "; ".join(f"{k}: local loops/cell {v[0]}, dangling axes {v[1]}, dangling fields {v[2]}" for k, v in info.items()))
check("the 20-site network has one local loop per cell; the 16-site network has none (its lift is a tree)",
      info["20-site"][0] == 1 and info["16-site"][0] == 0, "local loops = cycle rank of the cell graph - 3")

# --------------------------------------------------------------- B: solvability
print("B. exact solvability")
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
SS = [sps.csr_matrix(m) for m in S]
I2 = sps.identity(2, dtype=complex, format="csr")


def sop(n, placed):
    return reduce(lambda A, B: sps.kron(A, B, format="csr"), [placed.get(k, I2) for k in range(n)])


n16 = G16["n"]
H16 = sum(sop(n16, {j: SS[a], k: SS[a]}) for (j, k, a, off) in G16["bonds"])
for (j, ax), h in G16["dfield"].items():
    if h != 0:
        H16 = H16 + h * sop(n16, {j: SS[ax]})
adj = {v: [] for v in range(n16)}
for (j, k, a, off) in G16["bonds"]:
    adj[j].append((k, a))
    adj[k].append((j, a))
parent = {0: None}
order = [0]
for v in order:
    for (w, a) in adj[v]:
        if w not in parent:
            parent[w] = (v, a)
            order.append(w)
tree_e = {(min(v, p[0]), max(v, p[0]), p[1]) for v, p in parent.items() if p}


def root_path(v):
    out = [v]
    while parent[v]:
        v = parent[v][0]
        out.append(v)
    return out


def loop_op(j, k):
    pj, pk = root_path(j), root_path(k)
    common = next(x for x in pj if x in pk)
    cyc = pj[:pj.index(common) + 1] + list(reversed(pk[:pk.index(common)]))
    used = {v: set() for v in cyc}
    for (x, y) in [(cyc[i], cyc[i + 1]) for i in range(len(cyc) - 1)] + [(k, j)]:
        ax = next(a2 for (w, a2) in adj[x] if w == y)
        used[x].add(ax)
        used[y].add(ax)
    return sop(n16, {v: SS[[a2 for a2 in range(3) if a2 not in used[v]][0]] for v in cyc})


Ws = [loop_op(j, k) for (j, k, a, off) in G16["bonds"] if (min(j, k), max(j, k), a) not in tree_e]
loops_ok = all(abs((H16 @ W - W @ H16)).max() < 1e-10 for W in Ws)
j0, a0 = G16["bonds"][0][0], G16["bonds"][0][2]
Hbad = H16 + 0.4 * sop(n16, {j0: SS[a0]})
broken = sum(abs((Hbad @ W - W @ Hbad)).max() > 1e-6 for W in Ws)
E16 = spla.eigsh(H16, k=1, which="SA")[0][0]
M16 = min(E_finite(G16, u) for u in itertools.product((1, -1), repeat=len(G16["bonds"])))
check("16-site: loops conserved with dangling fields; a kept-bond field breaks some; ED = Majorana over 2^18",
      loops_ok and broken > 0 and abs(E16 - M16) < 1e-8,
      f"{len(Ws)} loops, {broken} broken; ED {E16:.10f}, Majorana {M16:.10f}")

n20 = G20["n"]
Nst = 1 << n20
idx = np.arange(Nst, dtype=np.int64)


def bitm(j):
    return 1 << (n20 - 1 - j)


terms = []
for (j, k, a, off) in G20["bonds"]:
    zj = 1 - 2 * ((idx & bitm(j)) > 0)
    zk = 1 - 2 * ((idx & bitm(k)) > 0)
    if a == 2:
        terms.append(("d", None, (zj * zk).astype(float)))
    elif a == 0:
        terms.append(("f", bitm(j) | bitm(k), np.ones(Nst)))
    else:
        terms.append(("f", bitm(j) | bitm(k), -(zj * zk).astype(float)))
for (j, ax), h in G20["dfield"].items():
    if h == 0:
        continue
    zj = 1 - 2 * ((idx & bitm(j)) > 0)
    if ax == 2:
        terms.append(("d", None, h * zj.astype(float)))
    elif ax == 0:
        terms.append(("f", bitm(j), h * np.ones(Nst)))
    else:
        terms.append(("f", bitm(j), h * 1j * zj))


def matvec(v):
    out = np.zeros(Nst, dtype=complex)
    for kind, mask, coef in terms:
        if kind == "d":
            out += coef * v
        else:
            out[idx ^ mask] += coef * v
    return out


E20 = spla.eigsh(spla.LinearOperator((Nst, Nst), matvec=matvec, dtype=complex), k=1, which="SA", tol=1e-10)[0][0]
M20 = min(E_finite(G20, u_from_non(G20, u)) for u in itertools.product((1, -1), repeat=len(G20["non"])))
check("20-site: exact ground energy (matrix-free Lanczos, 20 qubits) = least Majorana energy over its gauge classes",
      abs(E20 - M20) < 1e-8, f"ED {E20:.10f}; Majorana {M20:.10f} over {2 ** len(G20['non'])} classes")

# --------------------------------------------------------- C: gapped Z2 medium
print("C. bands, local flux and visons")
ks6 = [np.array(k) * 2 * np.pi / 6 for k in itertools.product(range(6), repeat=3)]


def sector_energies(G):
    out = []
    for u in itertools.product((1, -1), repeat=len(G["non"])):
        E = sum(-0.5 * ev[ev > 0].sum() for ev in (bloch(G, u, k) for k in ks6)) / len(ks6)
        out.append((E, u))
    return sorted(out)


def gap_scan(G, u, g):
    gmin, zmax = 9.0, 0
    for kk in itertools.product(range(g), repeat=3):
        ev = np.sort(np.abs(bloch(G, u, np.array(kk) * 2 * np.pi / g)))
        z = int(np.sum(ev < 1e-9))
        zmax = max(zmax, z)
        if z < len(ev):
            gmin = min(gmin, ev[z])
    return gmin, zmax


sec20 = sector_energies(G20)
levels = sorted({round(e, 6) for e, u in sec20})
split = levels[1] - levels[0] if len(levels) > 1 else 0.0
g20, z20 = gap_scan(G20, sec20[0][1], 16)
check("20-site: flux sectors split by the local flux; the lowest has 2 flat zero-mode bands and a gap above them",
      len(levels) == 2 and split > 0.05 and z20 == 2 and g20 > 0.5,
      f"sector energies/cell {levels} (local flux costs {split:.6f}); flat zero modes/cell {z20}; "
      f"gap above them on 16^3 grid {g20:.5f}")
# visons in the 2x2x2 supercell
ucell = {(G20["comp"][b[0]], b[2]): ub for b, ub in zip(G20["bonds"], u_from_non(G20, sec20[0][1]))}
U2 = {tuple(s[i] + 4 * sh[i] for i in range(3)) for s in N20 for sh in itertools.product(range(2), repeat=3)}
G2 = build(U2, (8, 8, 8))
u2 = [ucell[(tuple(c % 4 for c in G2["comp"][j]), ax)] for (j, kk, ax, off) in G2["bonds"]]
kp = [np.array(k) * np.pi for k in itertools.product(range(2), repeat=3)]


def E_super(uall):
    tot = 0.0
    for k in kp:
        ev = np.linalg.eigvalsh(1j * majorana_matrix(G2, uall, k))
        tot += -0.5 * ev[ev > 0].sum()
    return tot / len(kp)


E2 = E_super(u2)
costs = []
for i in range(len(u2)):
    uu = list(u2)
    uu[i] = -uu[i]
    costs.append(E_super(uu) - E2)
costs = np.array(costs)
posc = costs[costs > 1e-9]
check("20-site: a vison (one flipped bond on a local loop, 2x2x2 supercell) costs a positive energy; other flips cost 0",
      len(posc) > 0 and np.all(np.abs(costs[costs <= 1e-9]) < 1e-9) and posc.min() > 0.05,
      f"{len(posc)} flips cost {posc.min():.5f} to {posc.max():.5f}; {np.sum(np.abs(costs) < 1e-9)} cost 0")


def lowest_cell_energy(comp_set, Ls, grid):
    G = build(comp_set, Ls)
    ks = [np.array(k) * 2 * np.pi / np.array(grid) for k in itertools.product(*[range(x) for x in grid])]
    best = None
    for u in itertools.product((1, -1), repeat=len(G["non"])):
        E = sum(-0.5 * ev[ev > 0].sum() for ev in (bloch(G, u, k) for k in ks)) / len(ks)
        best = E if best is None or E < best else best
    return best


doubled = []
for mult in ((2, 1, 1), (1, 2, 1), (1, 1, 2)):
    Ls2 = tuple(4 * m for m in mult)
    Ud = {tuple(s[i] + 4 * sh[i] for i in range(3)) for s in N20 for sh in itertools.product(*[range(m) for m in mult])}
    doubled.append(lowest_cell_energy(Ud, Ls2, tuple(3 if m == 2 else 6 for m in mult)) / 2)
check("20-site: cells doubled along x, y or z find no lower flux pattern",
      all(abs(e - sec20[0][0]) < 1e-6 for e in doubled), f"{sec20[0][0]:.6f}; doubled {', '.join(f'{e:.6f}' for e in doubled)}")
sec16 = sector_energies(G16)
spread16 = sec16[-1][0] - sec16[0][0]
g16, z16 = gap_scan(G16, sec16[0][1], 16)
check("16-site tree: every flux sector has the same energy (pure gauge); gapped above its flat zero modes",
      abs(spread16) < 1e-9 and g16 > 0.3, f"spread {spread16:.1e}; flat zero modes/cell {z16}; gap {g16:.5f}")

# ------------------------------------------------------------- D: more networks
print("D. a search for more three-direction networks")


def search_relaxed(Ls, maxsol):
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx_s = {s: i + 1 for i, s in enumerate(sites)}
    cls, top = [], len(sites)
    for s in sites:
        u = idx_s[s]
        for ax in range(3):
            cls.append([-u, -idx_s[nbr(s, ax, 1, Ls)], -idx_s[nbr(s, ax, -1, Ls)]])
        for sx, sy, sz in itertools.product((1, -1), repeat=3):
            cls.append([u, -idx_s[nbr(s, 0, sx, Ls)], -idx_s[nbr(nbr(s, 0, sx, Ls), 0, sx, Ls)],
                        -idx_s[nbr(s, 1, sy, Ls)], -idx_s[nbr(nbr(s, 1, sy, Ls), 1, sy, Ls)],
                        -idx_s[nbr(s, 2, sz, Ls)], -idx_s[nbr(nbr(s, 2, sz, Ls), 2, sz, Ls)]])
        enc = CardEnc.atleast(lits=[idx_s[nbr(s, ax, d, Ls)] for ax in range(3) for d in (1, -1)], bound=2,
                              top_id=top, encoding=EncType.seqcounter)
        top = max(top, enc.nv)
        for c in enc.clauses:
            cls.append([-u] + c)
    cls.append([idx_s[(0, 0, 0)]])
    g = Glucose4(bootstrap_with=cls)
    out = []
    while len(out) < maxsol and g.solve():
        m = g.get_model()
        U = frozenset(s for s in sites if m[idx_s[s] - 1] > 0)
        out.append(U)
        g.add_clause([-idx_s[s] if s in U else idx_s[s] for s in sites])
    g.delete()
    return out


def components(U):
    Uset, seen, out = set(U), set(), []
    for s in sorted(U):
        if s in seen:
            continue
        comp, stack = {s}, [s]
        while stack:
            v = stack.pop()
            for ax in range(3):
                for d in (1, -1):
                    w = nbr(v, ax, d)
                    if w in Uset and w not in comp:
                        comp.add(w)
                        stack.append(w)
        seen |= comp
        out.append(frozenset(comp))
    return out


found = set()
for U in search_relaxed(L3, 2500):
    for c in components(U):
        if len(c) >= 8 and winding_rank(c)[1] == 3:
            found.add(c)
rows, all_gapped = [], True
for c in sorted(found, key=lambda x: (len(x), sorted(x)))[:8]:
    G = build(c)
    if not G["cons_ok"] or len(G["non"]) > 8:
        continue
    secs = sector_energies(G)
    gmin, zmax = gap_scan(G, secs[0][1], 6)
    all_gapped &= gmin > 1e-3
    rows.append((G["n"], len(G["bonds"]) - G["n"] - 2, round(float(gmin), 3)))
with_loops = sum(1 for r in rows if r[1] >= 1)
check("more three-direction networks exist, most with local loops; each lowest sector is gapped above flat bands",
      len(found) >= 5 and all_gapped and with_loops >= 3,
      f"{len(found)} distinct; (sites, local loops, gap) {rows}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
