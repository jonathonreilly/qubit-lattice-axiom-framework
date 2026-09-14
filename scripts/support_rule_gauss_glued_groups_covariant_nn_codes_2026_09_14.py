#!/usr/bin/env python3
"""Support-rule block: Gauss's law as glued support (exact finite runner).

Covariant nearest-neighbour support rules on record alphabets Z_2 and Z_3
over the open 2x2x2 and 3x3x3 windows of Z^3.  Sections:
  S1 geometry, the 24 proper rotations, pattern orbits;
  S2 covariant pattern codes (rotation-invariant subgroups of Z_q^7) and the
     cube census of group-closed rules;
  S3 divergence reading of a record-derived edge field, both exterior
     conventions, exact kernel dimensions against the cycle-space dimension;
  S4 glued groups as minimal codewords (exact census by weight);
  S5 role-carried flux: the Gauss support on the superlattice 3x3x3 window
     (roles supplied), its glued groups = circuits and charged paths;
  S6 sequential realisability and finished-record statistics on the 3x3
     plane window (all 9! formation orders, exact rationals).
Class-A finite check; prints TOTAL: PASS=N FAIL=0.
"""
from __future__ import annotations

import itertools
import time
from fractions import Fraction
from math import factorial

import numpy as np

T0 = time.time()
PASS = 0
FAIL = 0


def check(name: str, cond: bool) -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")


# ---------------------------------------------------------------- S1 geometry
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def window(nx: int, ny: int, nz: int):
    sites = [(x, y, z) for x in range(nx) for y in range(ny) for z in range(nz)]
    idx = {s: i for i, s in enumerate(sites)}
    nbrs = []
    for s in sites:
        row = []
        for d in DIRS:
            row.append(idx.get((s[0] + d[0], s[1] + d[1], s[2] + d[2]), -1))
        nbrs.append(row)
    edges = sorted({tuple(sorted((i, j))) for i, row in enumerate(nbrs)
                    for j in row if j >= 0})
    return sites, idx, nbrs, edges


def rotations():
    rots = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if round(float(np.linalg.det(M))) == 1:
                rots.append(M)
    return rots


def dir_perm(M):
    out = []
    for d in DIRS:
        v = tuple(int(x) for x in M @ np.array(d))
        out.append(DIRS.index(v))
    return out


ROTS = rotations()
DPERMS = [dir_perm(M) for M in ROTS]
# action on the 7-slot pattern (own value at slot 0, neighbour k at slot 1+k)
PPERMS = [[0] + [1 + p[k] for k in range(6)] for p in DPERMS]


def act(perm, x):
    y = [0] * len(x)
    for i, pi in enumerate(perm):
        y[pi] = x[i]
    return tuple(y)


def orbit_count(q: int, n: int, perms) -> int:
    # Burnside: number of orbits of Z_q^n under the permutation group
    tot = 0
    for p in perms:
        seen = [False] * n
        cyc = 0
        for i in range(n):
            if not seen[i]:
                cyc += 1
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = p[j]
        tot += q ** cyc
    assert tot % len(perms) == 0
    return tot // len(perms)


check("S1: 24 proper rotations, transitive on the six directions, direction stabiliser of order 4",
      len(ROTS) == 24 and len({p[0] for p in DPERMS}) == 6 and sum(1 for p in DPERMS if p[0] == 0) == 4)
nb2 = orbit_count(2, 6, DPERMS)
nb3 = orbit_count(3, 6, DPERMS)
check("S1 six-neighbour patterns: 10 binary and 57 ternary rotation orbits (Burnside)", nb2 == 10 and nb3 == 57)
print(f"S1 classes (own value x neighbour orbit): binary {2 * nb2}, ternary {3 * nb3}")

CUBE = window(2, 2, 2)
BOX = window(3, 3, 3)
PLANE = window(3, 3, 1)
for name, W, ne, degs in (("2x2x2", CUBE, 12, {3: 8}), ("3x3x3", BOX, 54, {3: 8, 4: 12, 5: 6, 6: 1})):
    sites, idx, nbrs, edges = W
    dd = {}
    for row in nbrs:
        k = sum(1 for j in row if j >= 0)
        dd[k] = dd.get(k, 0) + 1
    check(f"S1 {name}: {len(sites)} sites, {ne} edges, window degrees {degs}",
          len(edges) == ne and dd == degs)


# ------------------------------------------------- GF(q) linear algebra (exact)
def rref_mod(M, q: int):
    M = [[x % q for x in row] for row in M]
    rows = len(M)
    cols = len(M[0]) if rows else 0
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = pow(M[r][c], -1, q)
        M[r] = [(x * inv) % q for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(a - f * b) % q for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M[:r], piv


def kernel_mod(M, ncols: int, q: int):
    if not M:
        return [[1 if j == i else 0 for j in range(ncols)] for i in range(ncols)]
    R, piv = rref_mod(M, q)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][f]) % q
        basis.append(v)
    return basis


def span_key(vectors, q: int):
    vs = [list(v) for v in vectors if any(v)]
    if not vs:
        return ()
    R, _ = rref_mod(vs, q)
    return tuple(tuple(r) for r in R)


def all_codewords(basis, q: int):
    if not basis:
        return [tuple([0] * 0)]
    n = len(basis[0])
    B = np.array(basis, dtype=np.int64)
    words = []
    for coef in itertools.product(range(q), repeat=len(basis)):
        words.append(tuple(int(x) for x in (np.array(coef) @ B) % q))
    return words


# ------------------------------------------- S2 covariant pattern codes (T1, T2)
def invariant_functionals(q: int):
    out = []
    for c in itertools.product(range(q), repeat=7):
        if all(act(p, c) == c for p in PPERMS):
            out.append(c)
    return out


def lines_up_to_units(vectors, q: int):
    seen = set()
    for v in vectors:
        if any(v):
            seen.add(min(tuple((u * x) % q for x in v) for u in range(1, q)))
    return seen


def invariant_subspaces(q: int):
    """All rotation-invariant subgroups of Z_q^7 (own value + six neighbour slots)."""
    cyclic = set()
    for v in itertools.product(range(q), repeat=7):
        orbit = {act(p, v) for p in PPERMS}
        cyclic.add(span_key(orbit, q))
    subs = set(cyclic)
    frontier = set(cyclic)
    while frontier:
        new = set()
        for a in frontier:
            for b in cyclic:
                k = span_key(list(a) + list(b), q)
                if k not in subs:
                    new.add(k)
        subs |= new
        frontier = new
    return subs


INV = {}
SUMS_OK = []
for q in (2, 3):
    F = invariant_functionals(q)
    L = lines_up_to_units(F, q)
    check(f"S2 q={q}: invariant linear checks = a*r_v + b*sum(nbrs) ({q * q} functionals, {q + 1} lines)", len(F) == q * q and len(L) == q + 1
          and all(len(set(c[1:])) == 1 for c in F))
    INV[q] = invariant_subspaces(q)
    dims = {}
    for S in INV[q]:
        dims[len(S)] = dims.get(len(S), 0) + 1
    print(f"S2 q={q}: rotation-invariant subgroups of Z_{q}^7 by dimension: "
          + ", ".join(f"{d}:{dims[d]}" for d in sorted(dims)))
    SUMS_OK.append(all(span_key(S, q) == S for S in INV[q] if S))
    INV[q] = sorted(INV[q], key=len)
check("S2: every rotation-invariant subgroup (q=2,3) is closed under sums (rref)", len(SUMS_OK) == 2 and all(SUMS_OK))


def neighbour_module_summands(q: int):
    # invariant subgroups of the six neighbour slots alone (own slot zero)
    return [S for S in INV[q] if all(r[0] == 0 for r in S)]


print("S2 invariant subgroups on the six neighbour slots only: "
      + ", ".join(f"q={q}: {len(neighbour_module_summands(q))}" for q in (2, 3)))


# ----------------------------- cube census: all rules on cube-visible classes (q=2)
def corner_class_binary(own: int, nbr_vals) -> tuple:
    return (own, sum(nbr_vals))


def cube_satisfying_set(rule_classes: frozenset):
    sites, idx, nbrs, edges = CUBE
    out = []
    for bits in range(256):
        cfg = [(bits >> i) & 1 for i in range(8)]
        ok = True
        for v in range(8):
            m = sum(cfg[u] for u in nbrs[v] if u >= 0)
            if (cfg[v], m) not in rule_classes:
                ok = False
                break
        if ok:
            out.append(bits)
    return frozenset(out)


def is_subgroup_bits(S: frozenset) -> bool:
    if 0 not in S:
        return False
    return all((a ^ b) in S for a in S for b in S)


CLASSES = [(o, m) for o in (0, 1) for m in range(4)]
check("S2 cube: visible binary classes are (own value, occupied in-window neighbours): 8",
      len(CLASSES) == 8)
census = {}
group_sets = {}
for k in range(256):
    R = frozenset(c for i, c in enumerate(CLASSES) if (k >> i) & 1)
    S = cube_satisfying_set(R)
    census[R] = S
    if is_subgroup_bits(S):
        group_sets.setdefault(S, []).append(R)
n_group_rules = sum(len(v) for v in group_sets.values())
print(f"S2 cube census: {len(census)} rules; {n_group_rules} group-closed; "
      f"{len(group_sets)} distinct subgroups realised; orders "
      f"{sorted(len(S) for S in group_sets)}")


def pattern_code_cube_classes(S, q: int):
    # classes (own, m) visible on the cube from an invariant subgroup S of Z_q^7 (q=2)
    words = all_codewords([list(r) for r in S], q) if S else [tuple([0] * 7)]
    cls = set()
    corner = (1, 3, 5)  # slots of directions +x,+y,+z
    ext = (2, 4, 6)
    for w in words:
        if all(w[e] == 0 for e in ext):
            cls.add((w[0], sum(w[c] for c in corner)))
    return frozenset(cls)


from_codes = {}
for S in INV[2]:
    R = pattern_code_cube_classes(S, 2)
    from_codes[R] = census[R]
code_sets = set(from_codes.values())
check("S2 cube: every pattern-code rule has a group-closed satisfying set on the cube",
      all(is_subgroup_bits(S) for S in code_sets))
extra = [S for S in group_sets if S not in code_sets]
print(f"S2 cube: subgroups from pattern codes {len(code_sets)}; others "
      f"from any pattern code {len(extra)} (orders {sorted(len(S) for S in extra)})")
check("S2 cube: every group-closed satisfying set is a linear pattern code (orders 1,2,4,16,256)",
      len(extra) == 0 and sorted(len(S) for S in group_sets) == [1, 2, 4, 16, 256]
      and n_group_rules == 41)


# =============================================================================
# S3  divergence reading of the pair field, exterior conventions, flux counting
# =============================================================================
print("\n== S3: divergence reading, exterior conventions, incidence and flux ==")


def adjacency_matrices(W):
    sites, idx, nbrs, edges = W
    n = len(sites)
    A = [[0] * n for _ in range(n)]
    D = [[0] * n for _ in range(n)]
    for v in range(n):
        for u in nbrs[v]:
            if u >= 0:
                A[v][u] = 1
                D[v][v] += 1
    return A, D


def mat_add(X, Y, q):
    return [[(a + b) % q for a, b in zip(rx, ry)] for rx, ry in zip(X, Y)]


def mat_scale(X, c, q):
    return [[(c * a) % q for a in row] for row in X]


def ident(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def rank_mod(M, q):
    R, piv = rref_mod(M, q)
    return len(piv)


def kernel_dim(M, q):
    return len(M[0]) - rank_mod(M, q)


def mat_vec(M, v, q):
    return [sum(a * b for a, b in zip(row, v)) % q for row in M]


def brute_kernel_size(M, q):
    n = len(M[0])
    cnt = 0
    for vec in itertools.product(range(q), repeat=n):
        if all(x == 0 for x in mat_vec(M, vec, q)):
            cnt += 1
    return cnt


KDIM = {}
KOK = []
for wname, W in (("cube", CUBE), ("box", BOX)):
    A, D = adjacency_matrices(W)
    n = len(A)
    for q in (2, 3):
        mats = {"A": A, "D+A": mat_add(D, A, q), "I+A": mat_add(ident(n), A, q)}
        if q == 3:
            mats["I-A"] = mat_add(ident(n), mat_scale(A, 2, 3), 3)
        for mname, M in mats.items():
            d = kernel_dim(M, q)
            KDIM[(wname, q, mname)] = d
            basis = kernel_mod(M, n, q)
            ok = len(basis) == d and all(all(x == 0 for x in mat_vec(M, b, q)) for b in basis)
            ok = ok and rank_mod(basis, q) == d if basis else ok
            if wname == "cube":
                ok = ok and brute_kernel_size(M, q) == q ** d
            KOK.append(ok)
check("S3: all 14 divergence kernels (cube/box; q=2,3; A, D+A, I+A, I-A) verified; cube sizes brute-forced", len(KOK) == 14 and all(KOK))
# exterior conventions for the divergence reading of e_uv = b(r_u + r_v):
#   exterior-empty (exterior sites carry the empty value 0): full 6-star, 6 = 0 mod q  -> A
#   exterior-unrecorded (exterior edges carry no field): in-window star            -> D + A
check("S3 cube (degree 3): exterior-unrecorded rule D+A = I+A for q=2 and = A (exterior-empty) for q=3",
      KDIM[("cube", 2, "D+A")] == KDIM[("cube", 2, "I+A")]
      and mat_add(*adjacency_matrices(CUBE)[::-1], 2) == mat_add(ident(8), adjacency_matrices(CUBE)[0], 2)
      and mat_add(*adjacency_matrices(CUBE)[::-1], 3) == [[x % 3 for x in r] for r in adjacency_matrices(CUBE)[0]])
box_diff = {q: KDIM[("box", q, "A")] != KDIM[("box", q, "D+A")] for q in (2, 3)}
print(f"S3 box: exterior-empty vs -unrecorded divergence kernel dims differ: {box_diff}")
for wname in ("cube", "box"):
    print(f"S3 {wname} kernel dims: " + ", ".join(f"q={q} {m}:{KDIM[(wname, q, m)]}"
          for q in (2, 3) for m in ("A", "D+A", "I+A", "I-A") if (wname, q, m) in KDIM))
# plain sum rules a*r_v + b*sum(recorded nbrs) never see the convention: both give aI + bA
def plain_rule_matrix(W, a, b, q, convention):
    """a*r_v + b*sum over neighbours; exterior-empty adds b*0 per exterior neighbour,
    exterior-unrecorded skips unrecorded (exterior) neighbours: both give aI + bA_W"""
    sites, idx, nbrs, edges = W
    n = len(sites)
    M = [[0] * n for _ in range(n)]
    for v in range(n):
        M[v][v] = (M[v][v] + a) % q
        for u in nbrs[v]:
            if u >= 0:
                M[v][u] = (M[v][u] + b) % q
            elif convention == "empty":
                M[v][v] = (M[v][v] + b * 0) % q
    return M


plain_same = all(plain_rule_matrix(W, a, b, q, "empty") == plain_rule_matrix(W, a, b, q, "unrecorded")
                 == mat_add(mat_scale(ident(len(W[0])), a, q), mat_scale(adjacency_matrices(W)[0], b, q), q)
                 for W in (CUBE, BOX) for q in (2, 3) for a in range(q) for b in range(q) if (a, b) != (0, 0))
check("S3: plain sum rules a*r_v + b*sum(nbrs) = aI + bA under both conventions (only div sees degree)", plain_same)


# ------------------------------------------------- incidence, cycle space, flux
def incidence(W):
    sites, idx, nbrs, edges = W
    B = []
    for (u, v) in edges:
        row = [0] * len(sites)
        row[u] = 1
        row[v] = 1
        B.append(row)
    return B


def spanning_tree_cycles(W):
    """fundamental cycles (as edge index sets) of a BFS spanning tree"""
    sites, idx, nbrs, edges = W
    eidx = {e: i for i, e in enumerate(edges)}
    n = len(sites)
    parent = {0: None}
    order = [0]
    tree = set()
    frontier = [0]
    while frontier:
        nxt = []
        for v in frontier:
            for u in nbrs[v]:
                if u >= 0 and u not in parent:
                    parent[u] = v
                    tree.add(eidx[tuple(sorted((u, v)))])
                    nxt.append(u)
        frontier = nxt

    def path_to_root(v):
        p = []
        while parent[v] is not None:
            p.append(eidx[tuple(sorted((v, parent[v])))])
            v = parent[v]
        return p

    cycles = []
    for i, (u, v) in enumerate(edges):
        if i in tree:
            continue
        pu, pv = path_to_root(u), path_to_root(v)
        cyc = set(pu) ^ set(pv)
        cyc.add(i)
        cycles.append(frozenset(cyc))
    return cycles, tree


FLUX = {}
FLUX_OK = {2: [], 3: []}
FLUX_ROW = {2: [], 3: []}
for wname, W in (("cube", CUBE), ("box", BOX)):
    sites, idx, nbrs, edges = W
    nV, nE = len(sites), len(edges)
    for q in (2, 3):
        B = incidence(W)
        rB = rank_mod(B, q)
        kerB = kernel_mod(B, nV, q)
        par = [sum(s) % 2 for s in sites]
        if q == 2:
            expect = [[1] * nV]
        else:
            expect = [[1 if p == 0 else 2 for p in par]]
        span_ok = span_key(kerB, q) == span_key(expect, q)
        inc_ok = rB == nV - 1 and span_ok
        beta = nE - nV + 1
        cycles, tree = spanning_tree_cycles(W)
        dof_ok = nE - rB == beta == len(cycles)
        # circulation map C: edge fields -> Z_q^beta (unsigned sums around fundamental cycles)
        C = [[1 if e in cyc else 0 for e in range(nE)] for cyc in cycles]
        CB = [[sum(C[i][e] * B[e][v] for e in range(nE)) % q for v in range(nV)] for i in range(beta)]
        rCB = rank_mod(CB, q)
        rC = rank_mod(C, q)
        FLUX[(wname, q)] = (rC, rCB, beta)
        # Model P flux dim = dim of C(im B) = rCB ; Model R flux dim = dim C(all edge fields) = rC
        FLUX_OK[q].append(inc_ok and dof_ok and rC == beta and ((rCB == 0) if q == 2 else (0 < rCB)))
        FLUX_ROW[q].append((rB, beta, rCB, rC))
for q in (2, 3):
    rows = FLUX_ROW[q]
    fmt = lambda i: ", ".join(str(r[i]) for r in rows)
    if q == 2:
        check(f"S3 q=2 (cube, box): incidence rank {fmt(0)} = |V|-1 (kernel constants); cycle dim {fmt(1)}; "
              f"pair field exact (C B = 0); flux 0 vs {fmt(3)}", len(rows) == 2 and all(FLUX_OK[q]))
    else:
        check(f"S3 q=3 (cube, box): incidence rank {fmt(0)} (kernel staggered constants); cycle dim {fmt(1)}; "
              f"pair-field circulation rank {fmt(2)} (not exact); flux {fmt(2)} vs {fmt(3)}",
              len(rows) == 2 and all(FLUX_OK[q]))


# =============================================================================
# S4  glued groups = minimal codewords; cycle code of the cube graph = loops
# =============================================================================
print("\n== S4: glued groups as minimal codewords ==")


def supports_of(words):
    """distinct nonzero supports (as bitmasks) with the number of words per support"""
    sup = {}
    for w in words:
        m = 0
        for i, x in enumerate(w):
            if x:
                m |= 1 << i
        if m:
            sup[m] = sup.get(m, 0) + 1
    return sup


def minimal_supports(sup):
    """supports containing no other nonzero support (glued groups)"""
    masks = np.array(sorted(sup), dtype=np.int64)
    out = []
    for m in masks:
        smaller = masks[(masks & ~m) == 0]
        if len(smaller) == 1:  # only itself
            out.append(int(m))
    return out


def weight_hist(masks):
    h = {}
    for m in masks:
        w = bin(m).count("1")
        h[w] = h.get(w, 0) + 1
    return dict(sorted(h.items()))


def simple_cycles(W):
    """all simple cycles of the window graph as frozensets of edge indices (DFS)"""
    sites, idx, nbrs, edges = W
    eidx = {e: i for i, e in enumerate(edges)}
    n = len(sites)
    found = set()
    for s in range(n):
        stack = [(s, [s])]
        while stack:
            v, path = stack.pop()
            for u in nbrs[v]:
                if u < 0:
                    continue
                if u == s and len(path) >= 3:
                    cyc = frozenset(eidx[tuple(sorted((path[i], path[(i + 1) % len(path)])))]
                                    for i in range(len(path)))
                    found.add(cyc)
                elif u > s and u not in path:
                    stack.append((u, path + [u]))
    return found


sites, idx, nbrs, edges = CUBE
Bc = incidence(CUBE)
BT = [[Bc[e][v] for e in range(len(edges))] for v in range(len(sites))]
cycle_basis = kernel_mod(BT, len(edges), 2)
check("S4 cube graph: cycle code = ker(B^T) over GF(2) has dim 5 (32 words)", len(cycle_basis) == 5)
cyc_words = all_codewords(cycle_basis, 2)
cyc_sup = supports_of(cyc_words)
cyc_min = minimal_supports(cyc_sup)
dfs_cycles = simple_cycles(CUBE)
dfs_masks = {sum(1 << e for e in c) for c in dfs_cycles}
check(f"S4 cube graph: minimal cycle-code words = the {len(dfs_cycles)} DFS simple cycles", set(cyc_min) == dfs_masks)
print(f"S4 cube graph: simple cycles by length {weight_hist(cyc_min)}; nonzero cycle-space elements "
      f"{len(cyc_sup)}; non-simple {len(cyc_sup) - len(cyc_min)}")
check("S4 cube graph: non-minimal cycle-space elements = unions of two opposite faces (3)",
      all(bin(m).count('1') == 8 and any((m & c) == c and (m & ~c) in dfs_masks for c in dfs_masks)
          for m in cyc_sup if m not in set(cyc_min))
      and len(cyc_sup) - len(cyc_min) == 3)

# glued groups of the site codes (Model P) on the cube: the 5 subgroups of S2
per_order = []
for S in sorted(group_sets, key=len):
    words = [tuple((b >> i) & 1 for i in range(8)) for b in S]
    sup = supports_of(words)
    mins = minimal_supports(sup) if sup else []
    per_order.append(f"{len(S)}:{len(mins)} {weight_hist(mins)}")
print("S4 cube site codes (q=2), glued groups per subgroup order (count, weights): " + "; ".join(per_order))
glued16 = None
for S in group_sets:
    if len(S) == 16:
        words16 = [tuple((b >> i) & 1 for i in range(8)) for b in S]
        glued16 = weight_hist(minimal_supports(supports_of(words16)))
check("S4 cube site codes: order-16 subgroup ker(I+A) has 14 glued groups, all weight 4 (rigid clusters)", glued16 == {4: 14})

# glued groups of the divergence-reading kernels on the 3x3x3 window
SITE_GLUED = {}
A3, D3 = adjacency_matrices(BOX)
for q in (2, 3):
    for mname, M in (("A", A3), ("D+A", mat_add(D3, A3, q))):
        basis = kernel_mod(M, 27, q)
        if len(basis) > 12:
            continue
        words = all_codewords(basis, q)
        sup = supports_of(words)
        mins = minimal_supports(sup)
        SITE_GLUED[(q, mname)] = (len(basis), len(sup), len(mins), weight_hist(mins))
        wh = ",".join(f"{k}:{v}" for k, v in sorted(weight_hist(mins).items()))
        print(f"S4 box q={q} ker({mname}): dim {len(basis)}, supports {len(sup)}, glued groups {len(mins)}, weights {wh}")
check("S4 box: every divergence-reading site code of dim <= 12 was censused for glued groups",
      len(SITE_GLUED) == 4)


# =============================================================================
# S5  role-carrying Gauss support on the 3x3x3 superlattice cube (Model R)
# =============================================================================
print("\n== S5: role-carrying Gauss support on 3x3x3 (Model R) ==")
# supplied roles (role-pattern note): parity of the coordinates
#   V = all even (8 superlattice vertices), L = one odd (12 links), P = two odd (6 plaquettes),
#   C = three odd (1 cube centre).  Recorded alphabet Z_2 on every site.
sites3, idx3, nbrs3, edges3 = BOX
ROLE = []
for s in sites3:
    k = sum(c % 2 for c in s)
    ROLE.append("VLPC"[k])
role_count = {r: ROLE.count(r) for r in "VLPC"}
roles_ok = role_count == {"V": 8, "L": 12, "P": 6, "C": 1}
V_SITES = [i for i, r in enumerate(ROLE) if r == "V"]
L_SITES = [i for i, r in enumerate(ROLE) if r == "L"]
PC_SITES = [i for i, r in enumerate(ROLE) if r in "PC"]
check("S5 box: parity roles V=8, L=12, P=6, C=1; each L has two V neighbours, each V three L neighbours",
      roles_ok and all(sum(1 for u in nbrs3[l] if u >= 0 and ROLE[u] == "V") == 2 for l in L_SITES)
      and all(sum(1 for u in nbrs3[v] if u >= 0 and ROLE[u] == "L") == 3 for v in V_SITES))


def gauss_matrix(convention):
    """rows = V sites: n_V + sum over recorded L neighbours (exterior handled per convention);
    exterior sites contribute 0 (empty) or nothing (unrecorded): identical linear rows"""
    rows = []
    for v in V_SITES:
        row = [0] * 27
        row[v] = 1
        for u in nbrs3[v]:
            if u >= 0 and ROLE[u] == "L":
                row[u] = 1
            elif u < 0 and convention == "empty":
                pass  # empty exterior link carries e = 0
        rows.append(row)
    return rows


G_E = gauss_matrix("empty")
G_U = gauss_matrix("unrecorded")
check("S5 box: Gauss check matrices coincide under exterior-empty and exterior-unrecorded", G_E == G_U)
gauss_basis = kernel_mod(G_E, 27, 2)
check("S5 box: S_Gauss = ker over GF(2) has dim 19 = 12 links + 6 plaquettes + 1 centre (rank 8)",
      len(gauss_basis) == 19 and rank_mod(G_E, 2) == 8)
# the satisfying set is a group: closed under pointwise addition (linear kernel)
gauss_words = all_codewords(gauss_basis, 2)
n_gauss_words = len(gauss_words)
# glued groups: brute force over the VL subcode (P/C zero) 2^12 words, plus units
VL_basis = [b for b in gauss_basis if all(b[i] == 0 for i in PC_SITES)]
check("S5 box: S_Gauss = 2^19 records (graph of div: links and P/C fix the V values); VL subcode dim 12",
      n_gauss_words == 2 ** 19 and len(VL_basis) == 12)
vl_words = all_codewords(VL_basis, 2)
vl_sup = supports_of(vl_words)
vl_min = minimal_supports(vl_sup)
# classify minimal VL supports: pure link sets (closed loops of the superlattice Q_3) or dipoles
Lset = set(L_SITES)
Vset = set(V_SITES)
loops = [m for m in vl_min if all(not (m >> v) & 1 for v in V_SITES)]
dipoles = [m for m in vl_min if any((m >> v) & 1 for v in V_SITES)]
# superlattice graph Q_3: vertices V, edges = L sites (each joins its two V neighbours)
SL_edges = []
for l in L_SITES:
    ends = tuple(sorted(u for u in nbrs3[l] if u >= 0 and ROLE[u] == "V"))
    SL_edges.append(ends)
SL_V = {v: i for i, v in enumerate(V_SITES)}
SL_nbrs = [[-1] * 6 for _ in V_SITES]
for li, (a, b) in enumerate(SL_edges):
    for x, y in ((a, b), (b, a)):
        d = tuple((sites3[y][k] - sites3[x][k]) // 2 for k in range(3))
        SL_nbrs[SL_V[x]][DIRS.index(d)] = SL_V[y]
SL = ([sites3[v] for v in V_SITES], SL_V, SL_nbrs,
      sorted({tuple(sorted((SL_V[a], SL_V[b]))) for a, b in SL_edges}))
sl_cycles = simple_cycles(SL)
sl_cycle_masks = set()
for cyc in sl_cycles:
    m = 0
    for ei in cyc:
        a, b = SL[3][ei]
        va, vb = V_SITES[a], V_SITES[b]
        li = [l for l, ends in enumerate(SL_edges) if ends == tuple(sorted((va, vb)))][0]
        m |= 1 << L_SITES[li]
    sl_cycle_masks.add(m)
check(f"S5 box: link-only glued groups = the 28 simple loops of the superlattice cube {weight_hist(loops)}", set(loops) == sl_cycle_masks and len(loops) == 28)


def simple_paths(W):
    """simple paths with >= 1 edge as (frozenset of edge idx, endpoints) via DFS"""
    sites, idx, nbrs, edges = W
    eidx = {e: i for i, e in enumerate(edges)}
    out = set()
    for s in range(len(sites)):
        stack = [(s, [s])]
        while stack:
            v, path = stack.pop()
            for u in nbrs[v]:
                if u < 0 or u in path:
                    continue
                newp = path + [u]
                if u > s:
                    es = frozenset(eidx[tuple(sorted((newp[i], newp[i + 1])))] for i in range(len(newp) - 1))
                    out.add((es, frozenset((s, u))))
                stack.append((u, newp))
    return out


sl_paths = simple_paths(SL)
path_masks = set()
for es, ends in sl_paths:
    m = 0
    for ei in es:
        a, b = SL[3][ei]
        va, vb = V_SITES[a], V_SITES[b]
        li = [l for l, e2 in enumerate(SL_edges) if e2 == tuple(sorted((va, vb)))][0]
        m |= 1 << L_SITES[li]
    for x in ends:
        m |= 1 << V_SITES[x]
    path_masks.add(m)
check(f"S5 box: glued groups with matter = the {len(path_masks)} simple paths (dipoles: charge pair + string)",
      set(dipoles) == path_masks)
print(f"S5 box: dipole glued groups by number of links {weight_hist([m & sum(1 << l for l in L_SITES) for m in dipoles])}")
# units: plaquette and centre single-site words are codewords and minimal
unit_masks = {1 << i for i in PC_SITES}
full_sup = supports_of(gauss_words)
check("S5 box: the 7 plaquette/centre singletons are codewords (free roles: no check touches them)",
      all(m in full_sup for m in unit_masks))
# minimality over the full code: any word with both a PC part and a VL part contains its VL part
vl_masks = set(vl_sup)
mixed_nonminimal = all(((m & ~sum(1 << i for i in PC_SITES)) in vl_masks or (m & ~sum(1 << i for i in PC_SITES)) == 0)
                       for m in full_sup)
check(f"S5 box: codewords split (PC)+(VL); glued groups = 7 units + {len(loops)} loops + "
      f"{len(dipoles)} dipoles = {7 + len(loops) + len(dipoles)}",
      mixed_nonminimal and len(vl_min) == len(loops) + len(dipoles))
# flux: Model R link fields are unconstrained (matter absorbs the divergence): flux dim = beta = 5
check("S5 box: Model R flux dim 5 (superlattice cycle space) vs 0 for Model P pair field (q=2)", FLUX[("cube", 2)][0] == 5 and FLUX[("cube", 2)][1] == 0)


# =============================================================================
# S6  sequential realisability and hole statistics of the order-blind hard rule
# =============================================================================
print("\n== S6: sequential realisability and hole statistics (Model R) ==")
# pure-gauge (charge-free) flux report on the superlattice cube graph
B_SL = incidence(SL)
BT_SL = [list(col) for col in zip(*B_SL)]
cyc_SL = kernel_mod(BT_SL, len(SL[3]), 2)
gram = [[sum(a * b for a, b in zip(r1, r2)) % 2 for r2 in cyc_SL] for r1 in cyc_SL]
gram_rank = rank_mod(gram, 2)
print(f"S6 charge-free sector of Model R on the superlattice cube: dim {len(cyc_SL)}, flux image dim "
      f"= GF(2) rank of cycle Gram matrix = {gram_rank}")


def role_window(W):
    """roles by coordinate parity; checks[v] = {v} + in-window L neighbours; checks_of[s] = V's whose check has s"""
    sites, idx, nbrs, edges = W
    role = ["VLPC"[sum(c % 2 for c in s)] for s in sites]
    Vs = [i for i, r in enumerate(role) if r == "V"]
    Ls = [i for i, r in enumerate(role) if r == "L"]
    checks = {v: [v] + [u for u in nbrs[v] if u >= 0 and role[u] == "L"] for v in Vs}
    checks_of = {s: [v for v in Vs if s in checks[v]] for s in range(len(sites))}
    return role, Vs, Ls, checks, checks_of


ROLE_P, VP, LP, CHK_P, CHKOF_P = role_window(PLANE)
plane_roles_ok = (len(VP), len(LP), ROLE_P.count("P")) == (4, 4, 1) and all(len(CHKOF_P[l]) == 2 for l in LP)


def gauss_set(n, checks):
    return {p for p in itertools.product((0, 1), repeat=n)
            if all(sum(p[m] for m in mem) % 2 == 0 for mem in checks.values())}


S_plane = gauss_set(9, CHK_P)
check("S6 plane: roles V=4, L=4, P=1, every L in two checks; |S_Gauss| = 32 = 2^(9-4)",
      plane_roles_ok and len(S_plane) == 32)


def realisable(p, n, role, checks, checks_of):
    """rule: L/P free; a V site forms only after all its in-window L neighbours, with the parity they force"""
    FULL = (1 << n) - 1
    memo = {}

    def reach(F):
        if F == FULL:
            return True
        if F in memo:
            return memo[F]
        ok = False
        for s in range(n):
            if (F >> s) & 1:
                continue
            if role[s] == "V":
                mem = checks[s]
                if not all((F >> u) & 1 for u in mem if u != s):
                    continue
                if sum(p[m] for m in mem) % 2 != 0:
                    continue
            if reach(F | (1 << s)):
                ok = True
                break
        memo[F] = ok
        return ok
    return reach(0)


R_plane = {p for p in itertools.product((0, 1), repeat=9) if realisable(p, 9, ROLE_P, CHK_P, CHKOF_P)}
check("S6 plane: rule 'V forms after its L neighbours with forced parity' realises exactly S_Gauss (512)", R_plane == S_plane)


def double_closer_count(order, Ls, checks, checks_of):
    """d = number of links that form last within the union of their two checks"""
    pos = {s: i for i, s in enumerate(order)}
    d = 0
    for l in Ls:
        union = set()
        for v in checks_of[l]:
            union.update(checks[v])
        if all(pos[m] <= pos[l] for m in union):
            d += 1
    return d


def hole_sim_all_coins(order, n, checks, checks_of):
    """hard completed-check rule for ALL 2^n coin vectors at once (numpy).
    The forming site's support = values meeting every check it completes (it is last in the check);
    two conflicting completed checks => empty support => the site stays unrecorded (a hole).
    Returns (#fully recorded coin vectors, distinct fully recorded patterns, their multiplicities)."""
    N = 1 << n
    ar = np.arange(N, dtype=np.int64)
    pos = {s: i for i, s in enumerate(order)}
    rec = [None] * n
    hole = np.zeros(N, dtype=bool)
    for s in order:
        demands = []
        for v in checks_of[s]:
            mem = checks[v]
            if all(pos[m] <= pos[s] for m in mem):
                acc = np.zeros(N, dtype=np.int8)
                for m in mem:
                    if m != s:
                        assert rec[m] is not None
                        acc ^= rec[m]
                demands.append(acc)
        if not demands:
            rec[s] = ((ar >> s) & 1).astype(np.int8)
        elif len(demands) == 1:
            rec[s] = demands[0]
        else:
            hole |= demands[0] != demands[1]
            rec[s] = demands[0]
    full = ~hole
    pat = np.zeros(N, dtype=np.int64)
    for s in range(n):
        pat |= rec[s].astype(np.int64) << s
    uniq, counts = np.unique(pat[full], return_counts=True)
    return int(full.sum()), uniq, counts


def gauss_ok_ints(uniq, checks):
    ok = np.ones(len(uniq), dtype=bool)
    for mem in checks.values():
        par = np.zeros(len(uniq), dtype=np.int64)
        for m in mem:
            par ^= (uniq >> m) & 1
        ok &= par == 0
    return bool(ok.all())


# exact d-histogram over all 9! formation orders of the plane
t1 = time.time()
hist_plane = {}
samples = {}
for perm in itertools.permutations(range(9)):
    d = double_closer_count(perm, LP, CHK_P, CHKOF_P)
    hist_plane[d] = hist_plane.get(d, 0) + 1
    if len(samples.get(d, [])) < 3:
        samples.setdefault(d, []).append(perm)
print(f"S6 plane: d-histogram over 9! orders {dict(sorted(hist_plane.items()))}")
check("S6 plane: d <= 2 (two double closers cannot share a V) and every d in 0..2 occurs",
      set(hist_plane) == {0, 1, 2} and sum(hist_plane.values()) == factorial(9))
E_plane = sum(Fraction(c, 2 ** d) for d, c in hist_plane.items()) / factorial(9)
print(f"S6 plane: P(fully recorded and in S_Gauss) averaged over 9! orders = {E_plane} = {float(E_plane):.6f}")
ok_all = True
for d, orders in sorted(samples.items()):
    for order in orders:
        nfull, uniq, counts = hole_sim_all_coins(order, 9, CHK_P, CHKOF_P)
        pats = {tuple((int(u) >> s) & 1 for s in range(9)) for u in uniq}
        ok_all &= (nfull == 512 // 2 ** d and pats == S_plane and len(set(counts.tolist())) == 1
                   and gauss_ok_ints(uniq, CHK_P))
check("S6 plane: 9 sample orders (3 per d), all 512 coins: full-record fraction 2^-d, patterns = S_Gauss, "
      "uniform", ok_all)


# =============================================================================
# S6b  exact hole statistics over ALL formation orders: DP over formed-site subsets
# =============================================================================
def sub_window(W):
    """restrict a role window to its V and L sites (P/C sites touch no check): re-indexed checks,
    checks_of, link list and req[l] = bitmask of the other sites in the union of l's two checks"""
    role, Vs, Ls, checks, checks_of = role_window(W)
    keep = sorted(Vs + Ls)
    new = {s: i for i, s in enumerate(keep)}
    ch = {new[v]: [new[m] for m in checks[v]] for v in Vs}
    cho = {new[s]: [new[v] for v in checks_of[s]] for s in keep}
    Ln = [new[l] for l in Ls]
    req = {}
    for l in Ln:
        u = set()
        for v in cho[l]:
            u.update(ch[v])
        u.discard(l)
        req[l] = sum(1 << m for m in u)
    return len(keep), ch, cho, Ln, req


def d_histogram_dp(n, req, dmax):
    """number of formation orders of n sites with exactly d double closers (links last within req[l]),
    by dynamic programming over the set of already-formed sites: cnt[d, mask]"""
    N = 1 << n
    ar = np.arange(N, dtype=np.int64)
    pop = np.zeros(N, dtype=np.int8)
    for s in range(n):
        pop += ((ar >> s) & 1).astype(np.int8)
    cnt = np.zeros((dmax + 1, N), dtype=np.int64)
    cnt[0, 0] = 1
    for k in range(n):
        layer = ar[pop == k]
        for s in range(n):
            sub = layer[((layer >> s) & 1) == 0]
            if sub.size == 0:
                continue
            tgt = sub | (1 << s)
            if s in req:
                dbl = (sub & req[s]) == req[s]
                for d in range(dmax + 1):
                    vals = cnt[d, sub]
                    if d < dmax:
                        cnt[d + 1, tgt[dbl]] += vals[dbl]
                    else:
                        assert not vals[dbl].any(), "d exceeds dmax"
                    cnt[d, tgt[~dbl]] += vals[~dbl]
            else:
                for d in range(dmax + 1):
                    cnt[d, tgt] += cnt[d, sub]
    return [int(cnt[d, N - 1]) for d in range(dmax + 1)]


nP8, chP8, choP8, LP8, reqP8 = sub_window(PLANE)
hist_dp_plane = d_histogram_dp(nP8, reqP8, 2)
check("S6 plane: DP over the 8 V/L sites = 9!-order d-histogram / 9 (P site inert)",
      nP8 == 8 and hist_dp_plane == [hist_plane.get(d, 0) // 9 for d in range(3)]
      and all(hist_plane.get(d, 0) % 9 == 0 for d in range(3)))

nC20, chC20, choC20, LC20, reqC20 = sub_window(BOX)
union_sizes = sorted({bin(r).count("1") + 1 for r in reqC20.values()})
hist_cube = d_histogram_dp(nC20, reqC20, 4)
E_d_cube = Fraction(sum(d * c for d, c in enumerate(hist_cube)), factorial(20))
E_cube = sum(Fraction(c, 2 ** d) for d, c in enumerate(hist_cube)) / factorial(20)
print(f"S6 cube (20 V/L sites): d-histogram over 20! orders {dict(enumerate(hist_cube))}")
check(f"S6 cube: d <= 4 (double closers = a matching of Q_3), all d occur, sum = 20!, E[d] = 12/7 "
      f"(7-site unions), E[2^-d] = {E_cube} = {float(E_cube):.6f}",
      nC20 == 20 and union_sizes == [7] and all(c > 0 for c in hist_cube) and sum(hist_cube) == factorial(20)
      and E_d_cube == Fraction(12, 7))

# all 2^20 coin vectors on the 20-site cube sub-window, one seeded sample order per d = 0..4
import random
rng = random.Random(20260914)
sample_cube = {}
tries = 0
while len(sample_cube) < 5 and tries < 20000:
    tries += 1
    order = list(range(nC20))
    rng.shuffle(order)
    d = double_closer_count(order, LC20, chC20, choC20)
    sample_cube.setdefault(d, order)
cube_ok = sorted(sample_cube) == [0, 1, 2, 3, 4]
for d, order in sorted(sample_cube.items()):
    nfull, uniq, counts = hole_sim_all_coins(order, nC20, chC20, choC20)
    cube_ok &= (nfull == 2 ** (20 - d) and len(uniq) == 2 ** 12 and set(counts.tolist()) == {2 ** (8 - d)}
                and gauss_ok_ints(uniq, chC20))
check("S6 cube: one sample order per d = 0..4, all 2^20 coins: fully recorded fraction 2^-d, 4096 patterns "
      "= S_Gauss (2^12), uniform (2^(8-d) each)", cube_ok)

print("SUMMARY Model P (site alphabet): rigid clusters, flux 0; Model R (roles, Gauss support): 28 loops + 444 dipoles "
      f"+ 7 free units, flux 5; order dependence = hole mass 3/8 (plane), 1-{E_cube} (cube)")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"elapsed {time.time() - T0:.1f} s")
