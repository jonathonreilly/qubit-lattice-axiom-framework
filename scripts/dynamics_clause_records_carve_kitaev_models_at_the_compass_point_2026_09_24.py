#!/usr/bin/env python3
"""Records carve Kitaev models at the compass point of the dynamics clause.

Supplied and not adopted: the fully soldered dynamics clause of open PR 9040 at
its compass point (J = D = 0), H = K sum_bonds (e.s_x)(e.s_{x+e}), and records
acting as fields (open PR 9041): a record with content q on a bond along e
exerts the field K e (e.q) on its unrecorded neighbour. A carving is a set U of
unrecorded sites in which every site has exactly one U-neighbour along each
axis; it is zero-field when every record's content can be chosen orthogonal to
every axis along which it touches U. Then the unrecorded generator is exactly
Kitaev's bond-dependent model on the U-graph, with bond type = axis.

Checks:

A. Carvings (python-sat). With zero fields required, the complete enumeration
   of carvings through a fixed site on the 4x4x4 and 5x5x5 tori (112 and 1984)
   and 1500 sampled carvings on 6x6x6 have every component either finite or
   winding in one lattice direction (winding rank <= 1); one-direction tubes
   occur. Without the zero-field requirement, components winding in three
   directions occur (sizes printed), and each such carving has a record
   touching U along all three axes.
A'. Why (a proof, checked on every enumerated zero-field carving): each
   carved site u has partners along x, y, z; call the unit square spanned by
   two of its partner bonds closed when its fourth corner is carved. The
   recorded site behind u along an axis touches U along that axis, so the
   zero-field condition forces one of u's two squares containing that axis to
   be closed; hence at least two of u's three squares are closed. The carved
   sites, partner bonds and closed squares then form a surface with boundary
   (vertices in three squares are interior, in two squares on the boundary),
   and counting gives Euler characteristic chi = (number of interior sites)/4
   >= 0. A torus or Klein bottle would need chi = 0 with no boundary, which
   is impossible; so the winding rank is at most 1, and a winding component
   has chi = 0 with every site on the boundary: a strip one square wide.
B. Zero fields: on the staircase tube (4x4x4) and the cube cluster, contents
   orthogonal to the touched axes exist and cancel every field.
C. Exact solvability: on the cube and on periodic staircase tubes of 8 and 12
   sites, the loop operators commute with H and with each other, and the
   exact ground energy equals the smallest free-Majorana ground energy over all
   Z2 gauge configurations. A field on one site breaks some loop operator.
D. The infinite staircase tube: in the four translation-invariant flux sectors
   the Majorana ground energy per cell is lowest with pi flux through both
   plaquette types (-3.35522 |K|), where the Majorana spectrum has gap 2|K|;
   the zero-flux sector is gapless.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from collections import deque
from functools import reduce

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    'docs/DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_ZERO_FIELD_CARVINGS_ARE_CUBES_AND_TUBES_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)

import numpy as np
import scipy.sparse as sps
from pysat.solvers import Glucose4

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------- carvings
def carvings(Ls, zero_field, maxsol):
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx = {s: i + 1 for i, s in enumerate(sites)}

    def nb(s, ax, d):
        t = list(s)
        t[ax] = (t[ax] + d) % Ls[ax]
        return tuple(t)

    cls = []
    for s in sites:
        u = idx[s]
        for ax in range(3):
            p, m = idx[nb(s, ax, 1)], idx[nb(s, ax, -1)]
            cls.append([-u, p, m])
            cls.append([-u, -p, -m])
        if zero_field:
            for dx, dy, dz in itertools.product((1, -1), repeat=3):
                cls.append([u, -idx[nb(s, 0, dx)], -idx[nb(s, 1, dy)], -idx[nb(s, 2, dz)]])
    cls.append([idx[(0, 0, 0)]])
    g = Glucose4(bootstrap_with=cls)
    out, complete = [], False
    while len(out) < maxsol:
        if not g.solve():
            complete = True
            break
        m = g.get_model()
        U = frozenset(s for s in sites if m[idx[s] - 1] > 0)
        out.append(U)
        g.add_clause([-idx[s] if s in U else idx[s] for s in sites])
    g.delete()
    return out, complete


def components(U, Ls):
    res, seen = [], set()
    for s in sorted(U):
        if s in seen:
            continue
        pos = {s: (0, 0, 0)}
        q = deque([s])
        wind = set()
        while q:
            v = q.popleft()
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
                    if w not in U:
                        continue
                    pw = tuple(pos[v][i] + off[i] for i in range(3))
                    if w in pos:
                        if pos[w] != pw:
                            wind.add(tuple(pw[i] - pos[w][i] for i in range(3)))
                    else:
                        pos[w] = pw
                        q.append(w)
        seen |= set(pos)
        rank = int(np.linalg.matrix_rank(np.array(sorted(wind)))) if wind else 0
        res.append((len(pos), rank))
    return res


def touched_axes(U, Ls):
    """For each recorded site, the set of axes along which it touches U."""
    out = {}
    for s in itertools.product(*[range(l) for l in Ls]):
        if s in U:
            continue
        axes = set()
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + d) % Ls[ax]
                if tuple(t) in U:
                    axes.add(ax)
        out[s] = axes
    return out


print("A. carvings of the lattice by records")
summary = []
all_ok, tube_seen = True, False
for Ls, maxsol, want_complete in (((4, 4, 4), 5000, True), ((5, 5, 5), 5000, True), ((6, 6, 6), 1500, False)):
    sols, complete = carvings(Ls, True, maxsol)
    ranks = [r for U in sols for (n, r) in components(U, Ls)]
    all_ok &= max(ranks) <= 1 and (complete or not want_complete)
    tube_seen |= 1 in ranks
    summary.append(f"{'x'.join(map(str, Ls))}: {len(sols)}{' (complete)' if complete else ' sampled'}, ranks {sorted(set(ranks))}")
check("zero-field carvings: every component is finite or winds in one direction", all_ok and tube_seen,
      "; ".join(summary))


def surface_data(U, Ls):
    """Per component: (sites, interior sites, Euler characteristic, winding rank, min closed squares)."""
    def partner(u, ax):
        for d in (1, -1):
            t = list(u)
            t[ax] = (t[ax] + d) % Ls[ax]
            if tuple(t) in U:
                return d
        raise ValueError("not a carving")
    out = []
    comps_rank = {}
    for (n, r), members in zip(components(U, Ls), component_members(U, Ls)):
        Dsizes = []
        for u in members:
            sg = [partner(u, ax) for ax in range(3)]
            k = 0
            for a_, b_ in ((0, 1), (0, 2), (1, 2)):
                t = list(u)
                t[a_] = (t[a_] + sg[a_]) % Ls[a_]
                t[b_] = (t[b_] + sg[b_]) % Ls[b_]
                k += tuple(t) in U
            Dsizes.append(k)
        V = len(members)
        F = sum(Dsizes) / 4
        chi = V - 1.5 * V + F
        out.append((V, sum(1 for k in Dsizes if k == 3), chi, r, min(Dsizes)))
    return out


def component_members(U, Ls):
    res, seen = [], set()
    for s in sorted(U):
        if s in seen:
            continue
        comp, q = {s}, deque([s])
        while q:
            v = q.popleft()
            for ax in range(3):
                for d in (1, -1):
                    t = list(v)
                    t[ax] = (t[ax] + d) % Ls[ax]
                    w = tuple(t)
                    if w in U and w not in comp:
                        comp.add(w)
                        q.append(w)
        seen |= comp
        res.append(sorted(comp))
    return res


surf_ok, types = True, set()
for Ls, maxsol in (((4, 4, 4), 5000), ((5, 5, 5), 5000), ((6, 6, 6), 300)):
    sols, _ = carvings(Ls, True, maxsol)
    for U in sols:
        for V, nint, chi, r, mind in surface_data(U, Ls):
            surf_ok &= mind >= 2 and abs(chi - nint / 4) < 1e-12 and r <= 1 and (r == 0 or nint == 0)
            types.add((V, nint, chi, r) if r == 0 else ('tube', nint, chi, r))
fin = sorted(t for t in types if t[0] != 'tube')
tub = sorted(set(t[1:] for t in types if t[0] == 'tube'))
check("proof step: every carved site has >= 2 closed squares; chi = interior/4; winding components are strips (no interior sites)",
      surf_ok and len(tub) > 0, f"finite component types (sites, interior, chi, rank) {fin}; tube (interior, chi, rank) {tub}")
three_d, forced, sizes = 0, True, {}
for Ls in ((4, 4, 4), (5, 5, 5)):
    sols, complete = carvings(Ls, False, 5000)
    for U in sols:
        comps = components(U, Ls)
        if any(r == 3 for n, r in comps):
            three_d += 1
            sizes.setdefault('x'.join(map(str, Ls)), set()).update(n for n, r in comps if r == 3)
            forced &= any(len(ax) == 3 for ax in touched_axes(U, Ls).values())
check("without zero fields, three-direction networks occur and each forces a record touching all three axes",
      three_d > 0 and forced, f"{three_d} carvings with a three-direction component; sizes "
      + "; ".join(f"{k}: {sorted(v)}" for k, v in sizes.items()))

# --------------------------------------------------------------- B: zero fields
print("B. contents that cancel every field")
L4 = (4, 4, 4)
tube_U = frozenset((x, (3 - z + r) % 4, z) for z in range(4) for x in (0, 1) for r in (0, 1))
# check it is a carving: one U-neighbour per axis
def one_per_axis(U, Ls):
    for s in U:
        for ax in range(3):
            c = 0
            for d in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + d) % Ls[ax]
                c += tuple(t) in U
            if c != 1:
                return False
    return True


E = np.eye(3)
fields_ok = one_per_axis(tube_U, L4) and components(tube_U, L4) == [(16, 1)]
worst = 0.0
for U, Ls in ((tube_U, L4), (frozenset(itertools.product((0, 1), repeat=3)), (4, 4, 4))):
    ta = touched_axes(U, Ls)
    content = {}
    for r, axes in ta.items():
        free = [a for a in range(3) if a not in axes]
        content[r] = E[free[0]] if free else None
    if any(c is None for c in content.values()):
        fields_ok = False
        continue
    for s in U:
        h = np.zeros(3)
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + d) % Ls[ax]
                t = tuple(t)
                if t not in U:
                    h += E[ax] * (E[ax] @ content[t])
        worst = max(worst, np.abs(h).max())
check("staircase tube (16 sites on 4^3) and cube: contents orthogonal to touched axes cancel every field",
      fields_ok and worst == 0.0, f"largest residual field {worst}")

# ------------------------------------------------------- C: exact solvability
print("C. exact solvability")
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
SS = [sps.csr_matrix(m) for m in S]
I2s = sps.identity(2, dtype=complex, format="csr")


def site_op(n, placed):
    return reduce(lambda A, B: sps.kron(A, B, format="csr"), [placed.get(k, I2s) for k in range(n)])


def compass(n, bonds, K=1.0):
    H = sps.csr_matrix((2 ** n, 2 ** n), dtype=complex)
    for (j, k, a) in bonds:
        H = H + K * site_op(n, {j: SS[a], k: SS[a]})
    return H


def majorana_ground(n, bonds, u, K=1.0):
    A = np.zeros((n, n))
    for (j, k, a), ujk in zip(bonds, u):
        A[j, k] += -2 * K * ujk
        A[k, j] -= -2 * K * ujk
    ev = np.linalg.eigvalsh(1j * A)
    return -0.5 * ev[ev > 1e-12].sum()


def loops(n, bonds):
    """Loop operators of 4-cycles: product over the cycle's sites of the Pauli
    along the site's bond that leaves the cycle."""
    adj = {v: {} for v in range(n)}
    for (j, k, a) in bonds:
        adj[j][k] = a
        adj[k][j] = a
    cyc = set()
    for v in range(n):
        for w1 in adj[v]:
            for w2 in adj[w1]:
                if w2 == v:
                    continue
                for w3 in adj[w2]:
                    if w3 in (v, w1):
                        continue
                    if v in adj[w3]:
                        und = frozenset(frozenset(e) for e in ((v, w1), (w1, w2), (w2, w3), (w3, v)))
                        cyc.add(und)
    ops = []
    for und in cyc:
        placed = {}
        vs = {v for e in und for v in e}
        for v in vs:
            used = {adj[v][w] for e in und if v in e for w in e if w != v}
            out = [a for a in range(3) if a not in used]
            placed[v] = SS[out[0]]
        ops.append(site_op(n, placed))
    return ops


def cube_graph():
    V = list(itertools.product((0, 1), repeat=3))
    ix = {v: i for i, v in enumerate(V)}
    bonds = []
    for v in V:
        for a in range(3):
            if v[a] == 0:
                w = list(v)
                w[a] = 1
                bonds.append((ix[v], ix[tuple(w)], a))
    return 8, bonds


def staircase(N):
    sites = {}
    for z in range(N):
        for x in (0, 1):
            for r in (0, 1):
                sites[(x, r, z)] = len(sites)
    bonds = []
    for z in range(N):
        bonds.append((sites[(0, 0, z)], sites[(1, 0, z)], 0))
        bonds.append((sites[(0, 1, z)], sites[(1, 1, z)], 0))
        for x in (0, 1):
            bonds.append((sites[(x, 0, z)], sites[(x, 1, z)], 1))
            bonds.append((sites[(x, 0, z)], sites[(x, 1, (z + 1) % N)], 2))
    return len(sites), bonds


loops_ok, energy_ok, details = True, True, []
for name, (n, bonds) in (("cube", cube_graph()), ("tube, 8 sites", staircase(2)), ("tube, 12 sites", staircase(3))):
    H = compass(n, bonds)
    Ws = loops(n, bonds)
    for W in Ws:
        loops_ok &= abs((H @ W - W @ H)).max() < 1e-12
    for W1, W2 in itertools.combinations(Ws, 2):
        loops_ok &= abs((W1 @ W2 - W2 @ W1)).max() < 1e-12
    E0 = np.linalg.eigvalsh(H.toarray().real)[0]
    best = min(majorana_ground(n, bonds, u) for u in itertools.product((1, -1), repeat=len(bonds)))
    energy_ok &= abs(E0 - best) < 1e-9
    details.append(f"{name}: {len(Ws)} loops, E0 {E0:.8f}")
check("loop operators commute with H and each other", loops_ok, "; ".join(d.split(',')[0] + ',' + d.split(',')[1] for d in details))
check("exact ground energy = least free-Majorana ground energy over Z2 gauge configurations", energy_ok,
      "; ".join(details))
n, bonds = cube_graph()
H = compass(n, bonds) + 0.3 * site_op(n, {0: SS[0]})
broken = sum(abs((H @ W - W @ H)).max() > 1e-6 for W in loops(n, bonds))
check("a field on one site breaks loop operators", broken > 0, f"{broken} of 6 cube loops no longer commute")

# ------------------------------------------------------- D: the infinite tube
print("D. Majorana bands of the infinite staircase tube")
cellbonds = [(0, 1, 0), (2, 3, 0), (0, 2, 0), (1, 3, 0), (0, 2, 1), (1, 3, 1)]   # (j, k, cell offset of k)
ks = np.linspace(-np.pi, np.pi, 4001)[:-1]
sectors = {}
for u in itertools.product((1, -1), repeat=6):
    e0, gap = 0.0, 9.0
    for k in ks:
        A = np.zeros((4, 4), dtype=complex)
        for (j, kk, dz), ujk in zip(cellbonds, u):
            t = -2 * ujk * np.exp(1j * k * dz)
            A[j, kk] += t
            A[kk, j] -= np.conj(t)
        ev = np.linalg.eigvalsh(1j * A)
        e0 += -0.5 * ev[ev > 0].sum()
        gap = min(gap, np.min(np.abs(ev)))
    e0 /= len(ks)
    fxy = u[0] * u[3] * u[1] * u[2]
    fxz = u[4] * u[1] * u[5] * u[0]
    sectors.setdefault((fxy, fxz), set()).add((round(e0, 6), round(gap, 6)))
spread = max(max(e for e, g in v) - min(e for e, g in v) + max(g for e, g in v) - min(g for e, g in v)
             for v in sectors.values())
ground = min(sectors, key=lambda s: min(e for e, g in sectors[s]))
e_pi, g_pi = min(sectors[(-1, -1)])
e_0, g_0 = min(sectors[(1, 1)])
check("each flux sector's Majorana ground energy and gap are gauge invariant", spread < 1e-5,
      f"largest spread over configurations {spread:.1e}")
check("lowest Majorana ground energy per cell has pi flux through both plaquette types, with gap 2|K|",
      ground == (-1, -1) and abs(g_pi - 2.0) < 1e-6 and abs(e_pi + 3.35522) < 1e-5,
      f"E0/cell {e_pi} (pi, pi), {min(sectors[(1, -1)])[0]} (0, pi), {e_0} (0, 0); gap {g_pi}")
check("the zero-flux sector is gapless", g_0 < 5e-3, f"smallest |eps| on a 4000-point grid {g_0}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
