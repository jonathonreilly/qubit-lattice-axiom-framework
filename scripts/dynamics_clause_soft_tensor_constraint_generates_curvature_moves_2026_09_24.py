#!/usr/bin/env python3
"""A soft vector constraint and slot fields generate the landed tensor field's curvature moves at twelfth order.

Open PR 9077 showed that the landed tensor field (slots E_ij on vertex and
face sites, the vector constraint (G E)_j = d_i E_ij on link sites) cannot be
moved by the two-site clause or by any single neighbourhood. Open PR 9066
showed the U(1) link field gets its ring at fourth order from a soft vertex
Gauss energy and record fields. This runner does the same for the tensor
field (supplied models, finite diagnostics, no physical reading):
H = U sum_rows (G v)_row^2 - h sum_slots (X_s + X_s^dag), where v is the
change of the slots from a constraint-satisfying configuration and X_s
shifts slot s by one. Each row is a one-neighbourhood term on its link site.

1. Leading moves: the smallest L1 norm of a nonzero integer change with
   G v = 0 is 12 (mixed-integer programs through a diagonal and a face slot,
   radius-2 box). A complete enumeration finds exactly 6 such moves through
   a diagonal slot and 4 through a face slot, all planar pieces of the
   landed scalar-gauge pattern (open PR 9077).
2. The path sum: the leading amplitude is g = A h^12 / U^11 with
   A = sum over the monotone paths of prod 1 / |G v_k|^2 over the 11
   intermediate partial moves, none of which satisfies the constraint.
   Exactly A = 111150053/31850496. The same sum for the U(1) plaquette ring
   gives 5/2, which is open PR 9066's 5/32 with fields h s^x = (h/2) sigma^x.
3. Exact diagonalization on the path box (2304 states, reflection symmetric)
   confirms it: the splitting over 2 A (h/U)^12 tends to 1 as h/U -> 0.
4. Two-level (qubit) slots allow only unit changes. The smallest unit moves
   have 20 slots (radius-2 box here; a radius-3 box gives the same), so they
   appear at order 20. Two shapes occur: a spatial one with path sum 0.926
   and a planar one, in one lattice plane, with path sum 510.6.
5. Diagonal energies: for unbounded (rotor) slots every constraint-satisfying
   configuration has the same excitation energies, since |G v|^2 depends
   only on the change v, so no diagonal term arises at any order. For qubit
   slots each slot flips one way only, and the fourth-order diagonal energy
   changes between the two end configurations of a 20-slot move by up to
   about 3 h^4/U^3 (in units with unit step), far above the move itself.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from fractions import Fraction

AUDIT_TIMEOUT_SEC = 600

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csr_matrix

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


E3 = np.eye(3, dtype=int)
PAIRS = [(0, 1), (1, 2), (0, 2)]


def key(x, i, j):
    return (tuple(int(c) for c in x), (min(i, j), max(i, j)))


def row_terms(x, j):
    """The landed vector row (G p)_j(x) = p_jj(x + e_j) - p_jj(x) + sum_{i != j} [p_ij(x) - p_ij(x - e_i)]."""
    x = np.array(x)
    t = [(key(x + E3[j], j, j), 1), (key(x, j, j), -1)]
    for i in range(3):
        if i != j:
            t += [(key(x, i, j), 1), (key(x - E3[i], i, j), -1)]
    return t


def planar(x, n_):
    """The planar piece of the landed scalar-gauge pattern at x, in the plane normal to axis n_."""
    a, b = [c for c in range(3) if c != n_]
    x = np.array(x)
    v = {}
    for (j, i) in ((a, b), (b, a)):
        for s in (1, -1):
            v[key(x + s * E3[i], j, j)] = v.get(key(x + s * E3[i], j, j), 0) + 1
        v[key(x, j, j)] = v.get(key(x, j, j), 0) - 2
    i, j = min(a, b), max(a, b)
    for sh, c in [((0, 0, 0), -1), (tuple(-E3[i]), 1), (tuple(-E3[j]), 1), (tuple(-E3[i] - E3[j]), -1)]:
        k = key(x + np.array(sh), i, j)
        v[k] = v.get(k, 0) + c
    return {k: c for k, c in v.items() if c}


def box(R):
    cells = list(itertools.product(range(-R, R + 1), repeat=3))
    slots = [key(x, j, j) for x in cells for j in range(3)] + [key(x, i, j) for x in cells for (i, j) in PAIRS]
    sid = {k: n for n, k in enumerate(slots)}
    rows = []
    for x in itertools.product(range(-R - 1, R + 2), repeat=3):
        for j in range(3):
            v = {}
            for k, c in row_terms(x, j):
                if k in sid:
                    v[sid[k]] = v.get(sid[k], 0) + c
            if v:
                rows.append(v)
    G = np.zeros((len(rows), len(slots)))
    for r, v in enumerate(rows):
        for s, c in v.items():
            G[r, s] = c
    return slots, sid, G


# ------------------------------------------------ 1. the leading moves
slots2, sid2, G2 = box(2)
nS = len(slots2)
KS = [-2, -1, 1, 2]
Dm = np.zeros((nS, 4 * nS))
for s in range(nS):
    for a, k in enumerate(KS):
        Dm[s, 4 * s + a] = k
Gs = csr_matrix(G2) @ csr_matrix(Dm)
one = np.zeros((nS, 4 * nS))
for s in range(nS):
    one[s, 4 * s:4 * s + 4] = 1
l1 = np.array([abs(k) for _ in range(nS) for k in KS], dtype=float)


def min_l1(s0):
    """Smallest L1 norm of an integer move through slot s0 (|entries| <= 4, positive at s0)."""
    cost = np.ones(2 * nS)
    A = np.vstack([np.hstack([G2, -G2]), np.eye(1, 2 * nS, s0) - np.eye(1, 2 * nS, nS + s0)])
    sol = milp(cost, constraints=LinearConstraint(A, [0] * len(G2) + [1], [0] * len(G2) + [2]),
               integrality=np.ones(2 * nS), bounds=Bounds(0, 4), options={"time_limit": 300})
    return sol.status, int(round(sol.fun))


def enumerate_l1(s0, bound):
    cons = [LinearConstraint(Gs, 0, 0), LinearConstraint(csr_matrix(one), 0, 1),
            LinearConstraint(l1[None, :], 1, bound)]
    pos = np.zeros(4 * nS)
    pos[4 * s0 + 2] = pos[4 * s0 + 3] = 1
    cons.append(LinearConstraint(pos[None, :], 1, 1))
    found = []
    while len(found) < 30:
        sol = milp(l1, constraints=cons, integrality=np.ones(4 * nS), bounds=Bounds(0, 1), options={"time_limit": 300})
        if sol.status != 0:
            break
        b = np.round(sol.x).astype(int)
        d = Dm @ b
        found.append({slots2[s]: int(d[s]) for s in range(nS) if d[s]})
        cons.append(LinearConstraint(np.where(b == 1, -1.0, 1.0)[None, :], 1 - b.sum(), np.inf))
    return found


pieces = [planar(x, n_) for x in itertools.product(range(-1, 2), repeat=3) for n_ in range(3)]


def is_piece(mv):
    return any(mv == p or mv == {k: -c for k, c in p.items()} for p in pieces)


d0, f0 = sid2[key((0, 0, 0), 0, 0)], sid2[key((0, 0, 0), 0, 1)]
mins = [min_l1(d0), min_l1(f0)]
through_d, through_f = enumerate_l1(d0, 12), enumerate_l1(f0, 12)
check("the leading moves have L1 norm 12 and are exactly the planar pieces: 6 through a diagonal slot, 4 through a face slot",
      mins == [(0, 12), (0, 12)] and len(through_d) == 6 and len(through_f) == 4
      and all(is_piece(m) for m in through_d + through_f),
      f"smallest L1 through a diagonal and a face slot {[m[1] for m in mins]}; moves of L1 12 found {len(through_d)} and {len(through_f)}, all planar pieces")


# ------------------------------------------------ 2. the path sum
def local_rows(move):
    sl = list(move)
    si = {k: n for n, k in enumerate(sl)}
    rows = {}
    for x0 in {k[0] for k in sl}:
        for dd in itertools.product((-1, 0, 1), repeat=3):
            x = tuple(np.array(x0) + np.array(dd))
            for j in range(3):
                r = {}
                for k, c in row_terms(x, j):
                    if k in si:
                        r[si[k]] = r.get(si[k], 0) + c
                r = {a: b for a, b in r.items() if b}
                if r:
                    rows[(x, j)] = r
    G = np.zeros((len(rows), len(sl)), dtype=int)
    for n, r in enumerate(rows.values()):
        for a, b in r.items():
            G[n, a] = b
    return sl, G


def path_sum(G, d, exact=True):
    mags, sg = np.abs(d), np.sign(d)
    A, inter_zero = {}, 0
    for idx in sorted(itertools.product(*[range(m + 1) for m in mags]), key=sum):
        if sum(idx) == 0:
            A[idx] = Fraction(1) if exact else 1.0
            continue
        tot = sum((A[tuple(i - (k == s) for k, i in enumerate(idx))] for s in range(len(d)) if idx[s] > 0),
                  Fraction(0) if exact else 0.0)
        E = int(np.sum((G @ (sg * np.array(idx))) ** 2))
        if sum(idx) == mags.sum():
            A[idx] = tot
        else:
            inter_zero += E == 0
            A[idx] = tot / (Fraction(E) if exact else E)
    return A[tuple(mags)], inter_zero, len(A)


piece = planar((0, 0, 0), 2)
sl10, G10 = local_rows(piece)
d10 = np.array([piece[k] for k in sl10])
A10, z10, n10 = path_sum(G10, d10)
ring_G = np.array([[1, 0, 0, -1], [-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1]])
A_ring, _, _ = path_sum(ring_G, np.array([1, 1, 1, 1]))
check("the order-12 path sum is A = 111150053/31850496; the U(1) ring's is 5/2, matching open PR 9066's 5/32",
      A10 == Fraction(111150053, 31850496) and z10 == 0 and A_ring == Fraction(5, 2) and A_ring / 16 == Fraction(5, 32),
      f"A = {A10} = {float(A10):.6f} over {n10} partial moves, none constraint-satisfying; ring {A_ring}, (h/2)^4 form {A_ring / 16}")

# ------------------------------------------------ 3. exact diagonalization on the path box
mags, sg = np.abs(d10), np.sign(d10)
confs = list(itertools.product(*[range(m + 1) for m in mags]))
cid = {c: i for i, c in enumerate(confs)}
diag = np.array([np.sum((G10 @ (sg * np.array(c))) ** 2) for c in confs], dtype=float)
T = np.zeros((len(confs), len(confs)))
for c in confs:
    for s in range(len(c)):
        if c[s] < mags[s]:
            c2 = list(c)
            c2[s] += 1
            T[cid[c], cid[tuple(c2)]] = T[cid[tuple(c2)], cid[c]] = 1.0
ratios = []
for hU in (0.1, 0.15, 0.2):
    w = np.linalg.eigvalsh(np.diag(diag) - hU * T)
    ratios.append((w[1] - w[0]) / (2 * float(A10) * hU ** 12))
xs = np.array([0.1, 0.15, 0.2]) ** 2
fit = np.polyfit(xs, ratios, 2)
check("exact diagonalization on the 2304-state path box: the splitting over 2 A (h/U)^12 tends to 1",
      int(np.sum(diag == 0)) == 2 and abs(fit[-1] - 1) < 2e-3 and ratios[0] > ratios[1] > ratios[2],
      f"zero-energy configurations {int(np.sum(diag == 0))}; ratio at h/U = 0.1, 0.15, 0.2: "
      + ", ".join(f"{r:.4f}" for r in ratios) + f"; extrapolated to h = 0: {fit[-1]:.4f}")

# ------------------------------------------------ 4. qubit slots: unit moves
def min_unit_support(G, s0):
    n = G.shape[1]
    A = np.vstack([np.hstack([G, np.zeros((len(G), n))]), np.hstack([np.eye(n), -np.eye(n)]),
                   np.hstack([-np.eye(n), -np.eye(n)]), np.eye(1, 2 * n, s0)])
    lb = [0] * len(G) + [-np.inf] * (2 * n) + [1]
    ub = [0] * len(G) + [0] * (2 * n) + [1]
    sol = milp(np.concatenate([np.zeros(n), np.ones(n)]), constraints=LinearConstraint(A, lb, ub),
               integrality=np.ones(2 * n), bounds=Bounds(np.concatenate([-np.ones(n), np.zeros(n)]), np.ones(2 * n)),
               options={"time_limit": 300})
    d = np.round(sol.x[:n]).astype(int)
    return sol.status, {slots2[s]: int(d[s]) for s in range(n) if d[s]} if G is G2 else None


st_d, mv_d = min_unit_support(G2, d0)
st_f, mv_f = min_unit_support(G2, f0)


def unit_path_sum(move):
    sl, G = local_rows(move)
    d = np.array([move[k] for k in sl])
    n = len(d)
    masks = np.arange(1 << n, dtype=np.int64)
    bits = ((masks[:, None] >> np.arange(n)) & 1).astype(np.int64)
    E = np.sum(((bits * d[None, :]) @ G.T) ** 2, axis=1)
    pc = bits.sum(axis=1)
    A = np.zeros(1 << n)
    A[0] = 1.0
    for k in range(1, n + 1):
        layer = masks[pc == k]
        acc = np.zeros(len(layer))
        for s in range(n):
            acc += np.where((layer >> s) & 1, A[layer ^ (1 << s)], 0.0)
        A[layer] = acc if k == n else acc / E[layer]
    return A[-1], int(np.sum((E == 0) & (pc > 0) & (pc < n)))


ps_d, z_d = unit_path_sum(mv_d)
ps_f, z_f = unit_path_sum(mv_f)
# a planar 20-slot unit move (xy plane), found by the same program with another variable order
M_PLANAR = {((-2, -2, 0), (0, 1)): 1, ((-2, -1, 0), (1, 1)): -1, ((-2, 0, 0), (1, 1)): -1, ((-2, 0, 0), (0, 1)): -1,
            ((-1, -2, 0), (0, 0)): -1, ((-1, -1, 0), (0, 0)): 1, ((-1, -1, 0), (1, 1)): 1, ((-1, 0, 0), (0, 0)): 1,
            ((-1, 0, 0), (1, 1)): 1, ((-1, 1, 0), (0, 0)): -1, ((0, -2, 0), (0, 0)): -1, ((0, -2, 0), (0, 1)): -1,
            ((0, -1, 0), (0, 0)): 1, ((0, -1, 0), (1, 1)): 1, ((0, 0, 0), (0, 0)): 1, ((0, 0, 0), (1, 1)): 1,
            ((0, 0, 0), (0, 1)): 1, ((0, 1, 0), (0, 0)): -1, ((1, -1, 0), (1, 1)): -1, ((1, 0, 0), (1, 1)): -1}
slp, Gp = local_rows(M_PLANAR)
planar_ok = not np.any(Gp @ np.array([M_PLANAR[k] for k in slp])) and {k[0][2] for k in M_PLANAR} == {0}
ps_p, z_p = unit_path_sum(M_PLANAR)
spatial = [min(len({k[0][a] for k in mv}) for a in range(3)) > 1 for mv in (mv_d, mv_f)]
check("qubit slots allow only unit changes: the smallest unit moves have 20 slots, so they appear at order 20",
      st_d == 0 and st_f == 0 and len(mv_d) == 20 and len(mv_f) == 20 and z_d == z_f == z_p == 0 and planar_ok
      and len(M_PLANAR) == 20,
      f"unit-move supports through a diagonal and a face slot {len(mv_d)}, {len(mv_f)} (optimal, spatial {spatial}); "
      f"path sums {ps_d:.4g} and {ps_f:.4g}; a planar 20-slot unit move has path sum {ps_p:.4g}; "
      f"no constraint-satisfying partial move")


# ------------------------------------------------ 5. diagonal energies
def rows_touching(slotset):
    rows = {}
    for x0 in {k[0] for k in slotset}:
        for dd in itertools.product((-1, 0, 1), repeat=3):
            x = tuple(np.array(x0) + np.array(dd))
            for j in range(3):
                terms = row_terms(x, j)
                if any(k in slotset for k, _ in terms):
                    rows[(x, j)] = terms
    return rows


def e4_change(move, trials, rng):
    """Fourth-order diagonal energy change (units h^4/U^3) between the move's end configurations, qubit slots."""
    r1 = rows_touching(set(move))
    N1 = sorted({k for t in r1.values() for k, _ in t})
    rows = rows_touching(set(N1))
    sl = sorted({k for t in rows.values() for k, _ in t})
    si = {k: n for n, k in enumerate(sl)}
    G = np.zeros((len(rows), len(sl)), dtype=int)
    for r, t in enumerate(rows.values()):
        for k, c in t:
            G[r, si[k]] += c
    sup = [si[k] for k in move]
    out = [si[k] for k in N1 if k not in move]
    pairs = [(s, t) for s in sup for t in out if np.any(G[:, s] * G[:, t])]

    def pe(s, t, a, b):
        Es, Et = float(np.sum(G[:, s] ** 2)), float(np.sum(G[:, t] ** 2))
        Est = float(np.sum((a * G[:, s] + b * G[:, t]) ** 2))
        return -(1 / (Es * Est * Et) + 1 / (Es * Est * Es) + 1 / (Et * Est * Es) + 1 / (Et * Est * Et))

    diffs = []
    for _ in range(trials):
        sig = {t: int(rng.choice([-1, 1])) for t in out}
        for k, c in move.items():
            sig[si[k]] = c
        diffs.append(sum(pe(s, t, -sig[s], sig[t]) - pe(s, t, sig[s], sig[t]) for s, t in pairs))
    return np.array(diffs), len(pairs)


rng = np.random.default_rng(20260924)
dq, npairs = e4_change(mv_d, 100, rng)
check("qubit slots get fourth-order diagonal potentials: the end configurations of a 20-slot move differ by order h^4/U^3",
      np.max(np.abs(dq)) > 1.0,
      f"{npairs} slot pairs across the move's edge; change over 100 random surroundings from {dq.min():.2f} to {dq.max():.2f} "
      f"h^4/U^3 (unit step), against a move amplitude of order h^20/U^19")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
