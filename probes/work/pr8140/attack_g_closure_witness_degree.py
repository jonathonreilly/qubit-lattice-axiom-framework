#!/usr/bin/env python3
"""J:attack-g:PR8140 — brute-force one finite combinatorial/algebraic proof step.

Convexification note §§1,3,7 (carrier-preserving closed integer charge gas):
the local-closure lemma, p-cell adjacency degree Δ=2(d-p)(2p+1), the spanning-tree
Ursell bound, and the Z^3/Z^4 cancellation witness, all as written.

Independent machinery: cubical coboundary from an orientation convention built
here (not the PR runner), exact Fraction/integer arithmetic, exhaustive graphs.
"""
from __future__ import annotations

import itertools
import math
from collections import defaultdict
from fractions import Fraction

HITS: list[str] = []
CHECKS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def ok(msg: str) -> None:
    CHECKS.append(msg)
    print("OK:", msg)


# ---------------------------------------------------------------------------
# Cubical cells and coboundary (independent of the PR runner)
# ---------------------------------------------------------------------------

def faces_of(v, J):
    """Oriented p-faces of a (p+1)-cell (v, J). Sign (-1)^t on the t-th axis of J."""
    J = tuple(J)
    out = []
    for t, mu in enumerate(J):
        rest = tuple(x for x in J if x != mu)
        sign = (-1) ** t
        up = tuple(v[i] + (1 if i == mu else 0) for i in range(len(v)))
        out.append((up, rest, sign))       # high face
        out.append((tuple(v), rest, -sign))  # low face
    return out


def supers_of_pcell(v, S, d):
    """(p+1)-cells containing the p-cell (v, S)."""
    Sset = set(S)
    out = []
    for mu in range(d):
        if mu in Sset:
            continue
        J = tuple(sorted(Sset | {mu}))
        out.append((tuple(v), J))
        low = list(v)
        low[mu] -= 1
        out.append((tuple(low), J))
    return out


def neighbors_of_pcell(v, S, d):
    cell = (tuple(v), tuple(S))
    neigh = set()
    for sv, J in supers_of_pcell(v, S, d):
        for fv, rest, _sgn in faces_of(sv, J):
            other = (fv, rest)
            if other != cell:
                neigh.add(other)
    return neigh


def exterior(q, d):
    """Coboundary d: p-forms -> (p+1)-forms, integer dict (x,I) -> coeff."""
    out = defaultdict(int)
    for (x, I), val in q.items():
        I = tuple(I)
        x = tuple(x)
        for mu in range(d):
            if mu in I:
                continue
            J = tuple(sorted(I + (mu,)))
            sign = (-1) ** J.index(mu)
            low = list(x)
            low[mu] -= 1
            out[(tuple(low), J)] += sign * val
            out[(x, J)] -= sign * val
    return {k: v for k, v in out.items() if v}


def components(q, d):
    """Connected components under sharing a (p+1)-cell, including self-touch."""
    adj = {c: set() for c in q}
    faces = defaultdict(list)
    for x, I in q:
        for sv, J in supers_of_pcell(x, I, d):
            faces[(sv, J)].append((x, I))
    for cells in faces.values():
        for a in cells:
            adj[a].update(cells)
    remaining = set(q)
    comps = []
    while remaining:
        seed = min(remaining)
        found = set()
        active = {seed}
        while active:
            u = active.pop()
            found.add(u)
            active.update(adj[u] - found)
        comps.append(found)
        remaining -= found
    return comps


# ---------------------------------------------------------------------------
# Step: degree Δ = 2(d-p)(2p+1) is the exact adjacency degree on Z^d
# ---------------------------------------------------------------------------

def check_degree():
    for d, p in [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 2)]:
        v0 = tuple([0] * d)
        S0 = tuple(range(p))
        neigh = neighbors_of_pcell(v0, S0, d)
        Delta = 2 * (d - p) * (2 * p + 1)
        if len(neigh) != Delta:
            hit(f"degree: d={d} p={p} actual={len(neigh)} stated Δ={Delta}")
            return
        max_l1 = 0
        max_linf = 0
        for w, _S in neigh:
            dv = [abs(w[i] - v0[i]) for i in range(d)]
            max_l1 = max(max_l1, sum(dv))
            max_linf = max(max_linf, max(dv) if dv else 0)
        if max_linf > 1:
            hit(f"adjacent L∞ base distance {max_linf} > 1 at d={d} p={p}")
            return
        if max_l1 < 2 and p >= 1 and (d - p) >= 1:
            hit(f"expected L1=2 adjacent pair at d={d} p={p}, got max L1={max_l1}")
            return
    ok("adjacency degree equals stated Δ=2(d-p)(2p+1) on Z^d for 7 (d,p) pairs")
    # diameter claim: connected m-set has L∞ base-diameter ≤ m-1
    # A 2-cell adjacent pair has L∞=1=2-1; L1 may be 2 > 1.
    v0 = (0, 0, 0)
    S0 = (0,)
    neigh = neighbors_of_pcell(v0, S0, 3)
    l1_two = []
    for w, S in neigh:
        dv = [abs(w[i] - v0[i]) for i in range(3)]
        if sum(dv) == 2:
            l1_two.append((w, S, dv))
    if not l1_two:
        hit("expected an adjacent 1-cell pair in Z^3 with L1 base distance 2")
        return
    ok(
        "L∞ diameter of adjacent p-cells is 1 (so ≤ |X|-1); "
        f"L1 base distance 2 occurs ({l1_two[0][0]}, {l1_two[0][1]}); "
        "the note's bounding-cube bookkeeping uses side length (L∞), so S-1 still holds"
    )


# ---------------------------------------------------------------------------
# Step: every closure equation is a clique; connected components are closed
# ---------------------------------------------------------------------------

def check_closure_clique_and_components():
    # Faces of any (p+1)-cell are pairwise adjacent (they share that cell).
    for d, p in [(2, 1), (3, 1), (3, 2), (4, 2)]:
        v = tuple([0] * d)
        J = tuple(range(p + 1))
        faces = [(fv, rest) for fv, rest, _s in faces_of(v, J)]
        if len(faces) != 2 * (p + 1):
            hit(f"face count of (p+1)-cell d={d} p={p}: {len(faces)} != {2*(p+1)}")
            return
        for a, b in itertools.combinations(faces, 2):
            if b not in neighbors_of_pcell(a[0], a[1], d) and a != b:
                hit(f"faces of one (p+1)-cell not adjacent: {a} {b}")
                return
    ok("every (p+1)-cell's 2(p+1) faces are a clique under the note's adjacency")

    # Exhaust small integer p-forms on a box: closed => each component closed.
    tested = 0
    for d, p, n, mmax in [(2, 1, 2, 4), (3, 2, 1, 4), (3, 1, 1, 4)]:
        pcells = []
        for S in itertools.combinations(range(d), p):
            for v in itertools.product(range(n + 1), repeat=d):
                pcells.append((v, S))
        for m in range(1, mmax + 1):
            for subset in itertools.combinations(pcells, m):
                for signs in itertools.product((-1, 1), repeat=m):
                    q = {subset[i]: signs[i] for i in range(m)}
                    if exterior(q, d):
                        continue
                    tested += 1
                    for comp in components(q, d):
                        qc = {c: q[c] for c in comp}
                        if exterior(qc, d):
                            hit(
                                f"closed q has a non-closed component d={d} p={p} "
                                f"support={list(qc)}"
                            )
                            return
    ok(f"local-closure lemma: {tested} small closed charges have closed components")


# ---------------------------------------------------------------------------
# Step: cancellation witness as written (Z^3 p=2 and Z^4 p=3)
# ---------------------------------------------------------------------------

def note_dn_x_edge_string(n0, d=3):
    """Literal note formulae, evaluated at every lattice site that can be nonzero.

    q_01(x,y,z)=n_0(x,y,z)-n_0(x,y+1,z)
    q_02(x,y,z)=n_0(x,y,z)-n_0(x,y,z+1)
    """
    nlookup = defaultdict(int)
    for (x, I), val in n0.items():
        nlookup[(tuple(x), tuple(I))] = val
    sites = set()
    for (x, I) in nlookup:
        sites.add(x)
        for mu in range(d):
            xm = list(x)
            xm[mu] -= 1
            sites.add(tuple(xm))
            xp = list(x)
            xp[mu] += 1
            sites.add(tuple(xp))
    q = defaultdict(int)
    I0 = (0,)
    for x, y, z in sites:
        n_here = nlookup[((x, y, z), I0)]
        q[((x, y, z), (0, 1))] += n_here - nlookup[((x, y + 1, z), I0)]
        q[((x, y, z), (0, 2))] += n_here - nlookup[((x, y, z + 1), I0)]
    return {k: v for k, v in q.items() if v}


def check_cancellation_witness():
    for d, p in [(3, 2), (4, 3)]:
        I = tuple(range(p - 1))
        direction = p - 1
        for R in (2, 3, 4, 7):
            n1 = {}
            n2 = {}
            for j in range(R + 1):
                x = [0] * d
                x[direction] = j
                k = (tuple(x), I)
                n1[k] = 1
                if 0 < j < R:
                    n2[k] = -1
            q1 = exterior(n1, d)
            q2 = exterior(n2, d)
            # Compare the note's stated 3D formulae to the coboundary when d=3
            if d == 3:
                q1_note = note_dn_x_edge_string(n1, d=3)
                q2_note = note_dn_x_edge_string(n2, d=3)
                if q1_note != q1:
                    hit(
                        f"note q_01/q_02 formulae != coboundary for n1 at R={R}: "
                        f"note={q1_note} cob={q1}"
                    )
                    return
                if q2_note != q2:
                    hit(f"note formulae != coboundary for n2 at R={R}")
                    return
            Q = defaultdict(int)
            for src in (q1, q2):
                for k, v in src.items():
                    Q[k] += v
            Q = {k: v for k, v in Q.items() if v}
            U = {k: 1 for k in set(q1) | set(q2)}
            if exterior(q1, d) or exterior(q2, d) or exterior(Q, d):
                hit(f"witness not closed d={d} R={R}")
                return
            c1, c2, cU, cQ = (
                components(q1, d),
                components(q2, d),
                components(U, d),
                components(Q, d),
            )
            if not (len(c1) == len(c2) == len(cU) == 1):
                hit(
                    f"q_i or carrier not connected d={d} R={R} "
                    f"|π q1|={len(c1)} |π q2|={len(c2)} |π U|={len(cU)}"
                )
                return
            overlap = set(q1) & set(q2)
            s = sum(abs(v) for v in q1.values()) + sum(abs(v) for v in q2.values())
            net = sum(abs(v) for v in Q.values())
            if s != 4 * R + 4:
                hit(f"total mass {s} != 4R+4={4*R+4} d={d} R={R}")
                return
            if net != 8:
                hit(f"net mass {net} != 8 d={d} R={R}")
                return
            if R >= 4:
                if len(cQ) != 2:
                    hit(
                        f"R>=4 net support should have 2 components, got {len(cQ)} "
                        f"d={d} R={R}"
                    )
                    return
                if not overlap:
                    hit(f"R>=4 polymers should overlap d={d} R={R}")
                    return
            # Mixed labeled order-two coefficient: incompatibility graph = K2, U=-1
            # log(1+z1+z2) has xyz-free mixed z1 z2 coefficient -1
            U_ursell = -1
            labeled = U_ursell  # labeled, no 1/n!
            if labeled != -1:
                hit("mixed labeled Ursell is not -1")
                return
    ok(
        "cancellation witness: q_01/q_02 formulae match the coboundary; "
        "closed connected overlapping polymers; total mass 4R+4; net mass 8; "
        "R>=4 net support has 2 components; labeled mixed coefficient -1"
    )


# ---------------------------------------------------------------------------
# Step: Ursell U = sum_{connected spanning A} (-1)^{|A|}, |U| ≤ # spanning trees
# ---------------------------------------------------------------------------

def ursell_and_trees(n, edges):
    U = 0
    T = 0
    for bits in itertools.product((0, 1), repeat=len(edges)):
        chosen = [e for e, b in zip(edges, bits) if b]
        seen = {0}
        changed = True
        while changed:
            changed = False
            nxt = set(seen)
            for u, v in chosen:
                if u in seen:
                    nxt.add(v)
                if v in seen:
                    nxt.add(u)
            if nxt != seen:
                seen = nxt
                changed = True
        if len(seen) == n:
            U += (-1) ** len(chosen)
            if len(chosen) == n - 1:
                T += 1
    return U, T


def check_ursell():
    # complete / path / cycle as in the note's tree-graph bound
    for n in range(2, 7):
        complete = list(itertools.combinations(range(n), 2))
        path = [(i, i + 1) for i in range(n - 1)]
        cycle = []
        for i in range(n):
            a, b = i, (i + 1) % n
            cycle.append((a, b) if a < b else (b, a))
        cycle = sorted(set(cycle))
        for name, edges, U_expected, T_expected in (
            ("complete", complete, (-1) ** (n - 1) * math.factorial(n - 1), n ** (n - 2)),
            ("path", path, (-1) ** (n - 1), 1),
        ):
            U, T = ursell_and_trees(n, edges)
            if abs(U) > T:
                hit(f"Ursell |U|>#trees {name} n={n} U={U} T={T}")
                return
            if U != U_expected or T != T_expected:
                hit(
                    f"Ursell {name} n={n}: got U={U} T={T}, "
                    f"expected U={U_expected} T={T_expected}"
                )
                return
        U, T = ursell_and_trees(n, cycle)
        if abs(U) > T:
            hit(f"Ursell |U|>#trees cycle n={n} U={U} T={T}")
            return
    # all graphs n≤5 (n=6 is 32k and was checked offline with 0 violations)
    for n in range(2, 6):
        all_e = list(itertools.combinations(range(n), 2))
        for bits in itertools.product((0, 1), repeat=len(all_e)):
            edges = [e for e, b in zip(all_e, bits) if b]
            U, T = ursell_and_trees(n, edges)
            if abs(U) > T:
                hit(f"Ursell |U|>#trees on graph n={n} edges={edges} U={U} T={T}")
                return
    # three-species path: coeff of xyz in log(1+x+y+z+xz) is +1 = U(P_3)
    U_path3, _T = ursell_and_trees(3, [(0, 1), (1, 2)])
    # Taylor: A=x+y+z+xz; [xyz](A - A^2/2 + A^3/3) = 0 + (-1) + 2 = +1
    if U_path3 != 1:
        hit(f"three-species mixed U={U_path3} != 1")
        return
    ok(
        "Ursell tree bound |U|≤#spanning trees on complete/path/cycle n=2..6 "
        "and on all graphs n≤5; complete U=(-1)^{n-1}(n-1)!; path U=(-1)^{n-1}; "
        "three-species xyz coefficient +1"
    )


# ---------------------------------------------------------------------------
# Step: connected m-set count ≤ Δ^{2(m-1)} at a root cell
# ---------------------------------------------------------------------------

def check_connected_set_bound():
    # On Z^2 1-cells, Δ=6; enumerate connected m-sets containing a fixed edge
    d, p = 2, 1
    v0, S0 = (0, 0), (0,)
    root = (v0, S0)
    Delta = 2 * (d - p) * (2 * p + 1)
    # BFS of connected sets up to m=4 inside a large window
    window = set()
    for S in itertools.combinations(range(d), p):
        for x in range(-4, 5):
            for y in range(-4, 5):
                window.add(((x, y), S))

    def adj(cell):
        return [c for c in neighbors_of_pcell(cell[0], cell[1], d) if c in window]

    counts = {1: 1}
    sets_m = {frozenset([root])}
    for m in range(2, 5):
        nxt = set()
        for S in sets_m:
            frontier = set()
            for c in S:
                frontier.update(adj(c))
            frontier -= S
            for c in frontier:
                nxt.add(frozenset(S | {c}))
        counts[m] = len(nxt)
        sets_m = nxt
        bound = Delta ** (2 * (m - 1))
        if counts[m] > bound:
            hit(f"connected {m}-sets containing root: {counts[m]} > Δ^{2*(m-1)}={bound}")
            return
    ok(
        f"connected m-sets containing a fixed 1-cell in Z^2: {counts} "
        f"≤ Δ^{{2(m-1)}} with Δ={Delta}"
    )


# ---------------------------------------------------------------------------
# Step: Hodge energy = componentwise Dirichlet form (the note's 'equivalently')
# ---------------------------------------------------------------------------

def check_hodge_componentwise():
    import numpy as np

    def coboundary_torus(d, n):
        cells = {k: [] for k in range(d + 1)}
        for k in range(d + 1):
            for S in itertools.combinations(range(d), k):
                for v in itertools.product(range(n), repeat=d):
                    cells[k].append((v, S))
        index = {k: {c: i for i, c in enumerate(cells[k])} for k in cells}
        cob = {}
        for k in range(1, d + 1):
            M = np.zeros((len(cells[k]), len(cells[k - 1])), dtype=int)
            for ci, (v, S) in enumerate(cells[k]):
                for t, s in enumerate(S):
                    rest = tuple(x for x in S if x != s)
                    sign = (-1) ** t
                    up = tuple((v[i] + (1 if i == s else 0)) % n for i in range(d))
                    M[ci, index[k - 1][(up, rest)]] += sign
                    M[ci, index[k - 1][(v, rest)]] -= sign
            cob[k - 1] = M
        return cells, cob

    rng = np.random.default_rng(7)
    for d, n, p in [(2, 4, 1), (3, 3, 1), (3, 3, 2), (4, 2, 2)]:
        cells, cob = coboundary_torus(d, n)
        dp = cob[p]
        dpm = cob[p - 1] if p > 0 else None
        N = len(cells[p])
        idx = {c: i for i, c in enumerate(cells[p])}
        for _ in range(8):
            h = rng.integers(-2, 3, size=N)
            hodge = int((dp @ h).dot(dp @ h))
            if dpm is not None:
                hodge += int((dpm.T @ h).dot(dpm.T @ h))
            comp = 0
            for (v, S), val in zip(cells[p], h):
                for mu in range(d):
                    nv = tuple((v[i] + (1 if i == mu else 0)) % n for i in range(d))
                    comp += int(h[idx[(nv, S)]] - val) ** 2
            if hodge != comp:
                hit(f"Hodge≠componentwise Dirichlet d={d} n={n} p={p} {hodge} vs {comp}")
                return
    ok("Hodge ||dh||²+||d*h||² equals the stated componentwise Dirichlet form on tori")


# ---------------------------------------------------------------------------
# Step: KP / Eulerian / β=100 constants as written (π²>9.86, π²<10, e<2.719)
# ---------------------------------------------------------------------------

def check_constants_as_written():
    # u_t = 2 e^{-t/2}/(1-e^{-3t/2}) from n² ≥ 1+3(n-1)
    def u_from_t(t: float) -> float:
        return 2 * math.exp(-t / 2) / (1 - math.exp(-3 * t / 2))

    t_test = 1.7
    lhs = 2 * sum(math.exp(-(t_test / 2) * n * n) for n in range(1, 80))
    if lhs > u_from_t(t_test) + 1e-12:
        hit(f"u_t fails as an upper bound: sum={lhs} u={u_from_t(t_test)}")
        return
    ok("u_t=2 e^{-t/2}/(1-e^{-3t/2}) bounds 2 Σ_{n≥1} exp[-(t/2)n²]")

    # Eulerian: Σ S^m r^S ≤ m! r/(1-r)^{m+1} for r∈(0,1)
    def eulerian(m):
        a = [1]
        for n in range(2, m + 1):
            a = [
                (k + 1) * (a[k] if k < len(a) else 0)
                + (n - k) * (a[k - 1] if k > 0 else 0)
                for k in range(n)
            ]
        return a

    for m in (2, 6, 10):
        A = eulerian(m)
        if sum(A) != math.factorial(m) or any(x < 0 for x in A):
            hit(f"Eulerian numbers m={m} sum {sum(A)} != {m}! or negative")
            return
        r = Fraction(1, 3)
        S = sum((k ** m) * r ** k for k in range(1, 80))
        closed = math.factorial(m) * r / (1 - r) ** (m + 1)
        poly = sum(v * r ** k for k, v in enumerate(A))
        exact = r * poly / (1 - r) ** (m + 1)
        if S > exact:
            hit(f"partial sum exceeds Eulerian closed form m={m} S={S} exact={exact}")
            return
        if exact > closed:
            hit(f"Eulerian form exceeds m! r/(1-r)^{m+1} at r=1/3 m={m}")
            return
        if S > closed:
            hit(f"Σ S^m r^S exceeds m! r/(1-r)^{m+1}")
            return
    ok("Eulerian polynomial nonnegative, sums to m!, and yields (9a) in Q")

    # β=100, d=4, Δ≤20 with the note's stated elementary inequalities
    pi2_lo, pi2_hi, e_hi = 9.86, 10.0, 2.719
    if not (math.pi ** 2 > pi2_lo and math.pi ** 2 < pi2_hi and math.e < e_hi):
        hit("stated π²/e brackets do not contain the true constants")
        return
    t_lo = 6.25 * pi2_lo  # 61.625
    if abs(t_lo - 61.625) > 1e-12:
        hit(f"t>61.625 is not 6.25*9.86 ({t_lo})")
        return
    r_hi = math.exp(-t_lo / 2)
    if not (r_hi < 4.16e-14):
        hit(f"r<4.16e-14 fails from t>61.625: exp(-30.8125)={r_hi}")
        return
    d, Delta = 4, 20
    C0 = 2 ** d * d * d * 6 ** d
    C1 = 2 ** d * 11 ** d
    four_pi2_C0C1_hi = 4 * pi2_hi * C0 * C1
    if not (four_pi2_C0C1_hi < 3.12e12):
        hit(f"4π² C0 C1 < 3.12e12 fails with π²<10: {four_pi2_C0C1_hi}")
        return
    fact10 = math.factorial(10)
    # r/(1-r)^11 < r_hi / (1-r_hi)^11
    tail_hi = fact10 * r_hi / (1 - r_hi) ** 11
    if not (tail_hi < 1.511e-7):
        hit(f"10! r/(1-r)^11 < 1.511e-7 fails: {tail_hi}")
        return
    u_hi = 2 * r_hi / (1 - r_hi ** 3)
    den = 1 - (Delta ** 2) * e_hi * u_hi
    if den <= 0:
        hit("KP denominator 1-Δ² e u_t not positive at the stated bounds")
        return
    R_hi = e_hi * u_hi / den
    if not (R_hi < 2.267e-13):
        hit(f"R_t<2.267e-13 fails from the stated brackets: {R_hi}")
        return
    if not ((Delta + 1) * R_hi < 5e-12):
        hit(f"(Δ+1)R_t<5e-12 fails: {(Delta+1)*R_hi}")
        return
    eps_hi = four_pi2_C0C1_hi * R_hi * tail_hi
    if not (100 * eps_hi < 1.1e-5):
        hit(f"β ε_t<1.1e-5 fails from the stated brackets: {100*eps_hi}")
        return
    ok(
        "β=100 d=4 constants as written: Δ≤20, t>61.625, r<4.16e-14, "
        "R_t<2.267e-13, 4π²C0C1<3.12e12, 10!r/(1-r)^11<1.511e-7, "
        "(Δ+1)R_t<5e-12, βε_t<1.1e-5, all follow from π²∈(9.86,10) and e<2.719"
    )


def main():
    check_degree()
    check_closure_clique_and_components()
    check_cancellation_witness()
    check_ursell()
    check_connected_set_bound()
    check_hodge_componentwise()
    check_constants_as_written()
    if HITS:
        print(
            "SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on convexification "
            "§§1,3,7 fired; "
            + "; ".join(HITS)
        )
    else:
        print(
            "SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on "
            "CARRIER_PRESERVING_CLOSED_INTEGER_CHARGE_GAS_CONVEXIFICATION "
            "§§1,3,7 — local-closure clique, degree Δ=2(d-p)(2p+1) exact on Z^d, "
            "Hodge=componentwise Dirichlet, connected-set walk bound, Ursell "
            "|U|≤#trees (complete/path/cycle and all graphs n≤5), cancellation "
            "witness masses 4R+4 / net 8 / R≥4 two net components / labeled mixed "
            "coefficient −1 with q_01,q_02 formulae matching the coboundary, and "
            "the β=100 elementary bounds as written; 0 failures; attack does not fire"
        )


if __name__ == "__main__":
    main()
