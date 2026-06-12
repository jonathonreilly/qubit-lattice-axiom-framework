#!/usr/bin/env python3
"""Multi-plaquette cross-plane narrowing under the adjacency license.

Bounded-theorem runner. It extends the landed single-plaquette cross-plane
absence (theta_cross_plane_term_absent_in_supplied_per_plaquette_class,
2026-06-09) from single-plaquette terms to LOCAL MULTI-PLAQUETTE terms,
inside the unit-neighborhood link-support license of the landed
per_plaquette_from_adjacency_license note (2026-06-09).

Three layers, all finite and exhaustively checked:

  (V) VERBATIM COMPOSITE LIFT - the license condition applied unchanged to
      the total link support of a candidate local term. Result: the
      licensed loop-carrying supports are exactly single plaquettes, at ALL
      loop lengths (a pairwise-distance-2 lemma makes the classification
      finite), and no two-plaquette union passes at any relative placement.
      The multi-plaquette cross-plane reopening is therefore EMPTY inside
      the verbatim-licensed class.

  (W) PAIRWISE-PROXIMITY WEAKENING - each plaquette factor individually
      licensed, every factor PAIR mutually unit-proximate. Genuine
      multi-plaquette products now exist (domino / bent / stacked
      witnesses), but complementary-plane plaquette pairs fail at EVERY
      relative translation (an L1 projection lemma), so no W-licensed
      product's plane set contains a complementary pair and all three
      cross-plane FtildeF monomial coefficients vanish identically, at
      every factor order.

  (X) HONEST COMPLEMENT - chain-connected clusters (connectivity instead
      of pairwise proximity) DO reopen the slot: an explicit 3-factor chain
      with plane set {01,12,23} is exhibited whose unrestricted product
      carries a nonzero F01*F23 coefficient. The 2026-06-07 clover pair is
      shown to be license-external (fails both V and W) - its admissibility
      in the unrestricted local class is preserved, not contradicted.

The runner derives nothing about the license's own status: the license is
the consumed input (retained_bounded support note). No audit status is set.
Memory: tiny (small combinatorics + sympy polynomials; nothing dense).
"""
from __future__ import annotations

import itertools
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  --  {detail}" if detail else ""
    print(f"  [{tag}] {label}{suffix}")
    return bool(ok)


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


# ----------------------------------------------------------------------------
# Lattice primitives (Z^d, 6-NN style cubic adjacency in each dimension d)
# ----------------------------------------------------------------------------

def d1(p: tuple, q: tuple) -> int:
    """Cubic graph distance on Z^d = L1 distance."""
    return sum(abs(a - b) for a, b in zip(p, q))


def unit(d: int, k: int) -> tuple:
    e = [0] * d
    e[k] = 1
    return tuple(e)


def add(p: tuple, q: tuple) -> tuple:
    return tuple(a + b for a, b in zip(p, q))


def norm_link(a: tuple, b: tuple) -> tuple:
    return (a, b) if a <= b else (b, a)


def plaquette_sites(d: int, mu: int, nu: int, base: tuple) -> list:
    emu, enu = unit(d, mu), unit(d, nu)
    return [base, add(base, emu), add(add(base, emu), enu), add(base, enu)]


def plaquette_links(d: int, mu: int, nu: int, base: tuple) -> list:
    s = plaquette_sites(d, mu, nu, base)
    return [norm_link(s[i], s[(i + 1) % 4]) for i in range(4)]


# ----------------------------------------------------------------------------
# The verbatim unit-neighborhood link-support license, lifted to a composite
# support exactly as written in the per-plaquette license note:
#   for every target link l=(a,b) in the support, every endpoint p of every
#   support link must obey min(d(p,a), d(p,b)) <= 1.
# ----------------------------------------------------------------------------

def license_verbatim(links: list) -> bool:
    endpoints = set()
    for a, b in links:
        endpoints.add(a)
        endpoints.add(b)
    for a, b in links:
        for p in endpoints:
            if min(d1(p, a), d1(p, b)) > 1:
                return False
    return True


def support_sites(links: list) -> set:
    s = set()
    for a, b in links:
        s.add(a)
        s.add(b)
    return s


# ----------------------------------------------------------------------------
# Rooted simple closed loop enumeration (anchor regression vs license note)
# ----------------------------------------------------------------------------

def rooted_simple_loops(d: int, length: int) -> list:
    """Rooted simple closed loops at the origin: directed, no immediate
    backtracking, no repeated undirected edge, sites distinct except for the
    closing return to the origin. Matches the license note's domain."""
    origin = tuple([0] * d)
    steps = []
    for k in range(d):
        steps.append(unit(d, k))
        steps.append(tuple(-x for x in unit(d, k)))
    loops = []

    def dfs(path, used_edges):
        cur = path[-1]
        if len(path) - 1 == length:
            if cur == origin:
                loops.append(list(path))
            return
        for s in steps:
            nxt = add(cur, s)
            edge = norm_link(cur, nxt)
            if edge in used_edges:
                continue
            if nxt != origin and nxt in path:
                continue
            if nxt == origin and len(path) - 1 != length - 1:
                continue
            if d1(nxt, origin) > length // 2:
                continue
            dfs(path + [nxt], used_edges | {edge})

    dfs([origin], frozenset())
    return loops


def loop_links(path: list) -> list:
    return [norm_link(path[i], path[i + 1]) for i in range(len(path) - 1)]


def is_plaquette_loop(path: list) -> bool:
    if len(path) != 5:
        return False
    sites = set(path[:-1])
    dirs = set()
    for i in range(4):
        diff = tuple(b - a for a, b in zip(path[i], path[i + 1]))
        dirs.add(tuple(abs(x) for x in diff))
    return len(sites) == 4 and len(dirs) == 2


# ----------------------------------------------------------------------------
# Complete licensed-loop classification (all lengths) via the distance-2 lemma
# ----------------------------------------------------------------------------

def licensed_loops_all_lengths(d: int) -> tuple:
    """Enumerate ALL rooted simple closed loops at the origin whose support
    can satisfy the verbatim license. The license forces every pair of
    support sites to be at distance <= 2 (lemma checked separately), so the
    support lies in the ball B2(origin) and the enumeration is finite at all
    lengths. Returns (licensed_loops, examined_count)."""
    origin = tuple([0] * d)
    ball = [p for p in itertools.product(range(-2, 3), repeat=d)
            if d1(p, origin) <= 2]
    steps = []
    for k in range(d):
        steps.append(unit(d, k))
        steps.append(tuple(-x for x in unit(d, k)))
    licensed = []
    examined = 0

    def pairwise_ok(site, others):
        return all(d1(site, q) <= 2 for q in others)

    def dfs(path, used_edges):
        nonlocal examined
        cur = path[-1]
        if cur == origin and len(path) >= 5:
            examined += 1
            if license_verbatim(loop_links(path)):
                licensed.append(list(path))
            return
        for s in steps:
            nxt = add(cur, s)
            if d1(nxt, origin) > 2:
                continue
            edge = norm_link(cur, nxt)
            if edge in used_edges:
                continue
            if nxt != origin and nxt in path:
                continue
            if not pairwise_ok(nxt, path):
                continue
            dfs(path + [nxt], used_edges | {edge})

    dfs([origin], frozenset())
    return licensed, examined


# ----------------------------------------------------------------------------
# Pairwise mutual unit-proximity (the W lift)
# ----------------------------------------------------------------------------

def mutually_unit_proximate(sites_a: list, sites_b: list) -> bool:
    fwd = all(min(d1(p, q) for q in sites_b) <= 1 for p in sites_a)
    bwd = all(min(d1(q, p) for p in sites_a) <= 1 for q in sites_b)
    return fwd and bwd


def planes(d: int) -> list:
    return list(itertools.combinations(range(d), 2))


def complementary_pairs(d: int) -> list:
    out = []
    for p1, p2 in itertools.combinations(planes(d), 2):
        if not (set(p1) & set(p2)):
            out.append((p1, p2))
    return out


def main() -> int:
    print("=" * 88)
    print("THETA MULTI-PLAQUETTE CROSS-PLANE NARROWING UNDER THE ADJACENCY LICENSE")
    print("=" * 88)

    # ------------------------------------------------------------------
    section("(A) Anchors: regression against the per-plaquette license note (d=3)")
    d3 = 3
    plaq = plaquette_links(d3, 0, 1, (0, 0, 0))
    check("single plaquette passes the verbatim license (d=3)",
          license_verbatim(plaq))

    loops4 = rooted_simple_loops(d3, 4)
    check("length-4 rooted simple loops at origin: 24, all plaquettes, all licensed (d=3)",
          len(loops4) == 24
          and all(is_plaquette_loop(p) for p in loops4)
          and all(license_verbatim(loop_links(p)) for p in loops4),
          detail=f"count={len(loops4)}")

    loops6 = rooted_simple_loops(d3, 6)
    check("length-6 rooted simple loops at origin: 264, none licensed (d=3)",
          len(loops6) == 264
          and not any(license_verbatim(loop_links(p)) for p in loops6),
          detail=f"count={len(loops6)}")

    # ------------------------------------------------------------------
    section("(B) Distance-2 lemma: the verbatim license bounds the support")
    # Lemma: if S is licensed then any two support sites p, q are at
    # distance <= 2. Proof shape: q is an endpoint of some link (q, q') with
    # d(q, q') = 1; the license gives min(d(p,q), d(p,q')) <= 1, hence
    # d(p,q) <= d(p,q') + d(q',q) <= 1 + 1 = 2. Verified here on every
    # licensed support produced by the anchor enumerations.
    lemma_ok = True
    for p in loops4:
        links = loop_links(p)
        if license_verbatim(links):
            sites = list(support_sites(links))
            for a, b in itertools.combinations(sites, 2):
                if d1(a, b) > 2:
                    lemma_ok = False
    check("every licensed support has pairwise site distance <= 2 (lemma instance check)",
          lemma_ok)
    # The lemma's logical core, checked exhaustively on a window: for sites
    # p, q, q' with d(q, q') = 1, min(d(p,q), d(p,q')) <= 1 implies
    # d(p,q) <= 2 (triangle inequality through q'). This grounds the DFS
    # pruning used in section (C).
    core_ok = True
    win3 = [p for p in itertools.product(range(-2, 3), repeat=3)]
    for q in win3:
        for k in range(3):
            qp = add(q, unit(3, k))
            for p in win3:
                if min(d1(p, q), d1(p, qp)) <= 1 and d1(p, q) > 2:
                    core_ok = False
    check("lemma core: min(d(p,q), d(p,q')) <= 1 with d(q,q') = 1 forces"
          " d(p,q) <= 2 (exhaustive window)",
          core_ok)

    # ------------------------------------------------------------------
    section("(C) Complete licensed-loop classification at ALL lengths (V lift)")
    for d in (3, 4):
        licensed, examined = licensed_loops_all_lengths(d)
        all_plaq = all(is_plaquette_loop(p) for p in licensed)
        n_planes = len(planes(d))
        expected = n_planes * 4 * 2  # plaquettes through origin x 2 orientations
        check(f"d={d}: licensed loops (all lengths) = plaquettes only",
              all_plaq and len(licensed) == expected,
              detail=f"licensed={len(licensed)} expected={expected} examined_closed_loops={examined}")

    # ------------------------------------------------------------------
    section("(D) Neighborhood-intersection lemma: a licensed support containing"
            " a plaquette is that plaquette")
    d = 4
    P = plaquette_links(d, 0, 1, tuple([0] * d))
    P_sites = set(plaquette_sites(d, 0, 1, tuple([0] * d)))
    window = [p for p in itertools.product(range(-3, 5), repeat=d)]
    allowed = []
    for p in window:
        if all(min(d1(p, a), d1(p, b)) <= 1 for a, b in P):
            allowed.append(p)
    check("sites within distance 1 of ALL four plaquette edges = exactly the 4 plaquette sites",
          set(allowed) == P_sites,
          detail=f"allowed={sorted(allowed)}")
    extra_links = []
    for a, b in itertools.combinations(sorted(P_sites), 2):
        if d1(a, b) == 1 and norm_link(a, b) not in P:
            extra_links.append((a, b))
    check("the only lattice links among those sites are the 4 plaquette edges"
          " (no diagonals on the 6-NN lattice)",
          len(extra_links) == 0)

    # ------------------------------------------------------------------
    section("(E) Verbatim pair scan: no two-plaquette union is licensed (d=4)")
    # Window completeness: plaquette site offsets o obey |o|_inf <= 1, so for
    # two plaquettes at relative base translation t every cross pair of sites
    # has L1 distance >= |t|_inf - 2. The license needs pairwise distance
    # <= 2 (lemma B), impossible once |t|_inf >= 5; the W lift needs <= 1,
    # impossible once |t|_inf >= 4. Scanning |t|_inf <= 4 is exhaustive.
    offsets = [tuple([0] * d)]
    max_off = 0
    for mu, nu in planes(d):
        for o in plaquette_sites(d, mu, nu, tuple([0] * d)):
            max_off = max(max_off, max(abs(x) for x in o))
    check("plaquette site offsets obey |o|_inf <= 1 (window-completeness input)",
          max_off == 1)

    t_window = list(itertools.product(range(-4, 5), repeat=d))
    pls = planes(d)
    verbatim_passes = []
    w_passes = []
    pairs_scanned = 0
    for i, (m1, n1) in enumerate(pls):
        A_links = plaquette_links(d, m1, n1, tuple([0] * d))
        A_sites = plaquette_sites(d, m1, n1, tuple([0] * d))
        for j, (m2, n2) in enumerate(pls):
            if j < i:
                continue
            for t in t_window:
                if (m1, n1) == (m2, n2) and t == tuple([0] * d):
                    continue  # identical plaquette, not a pair
                B_links = plaquette_links(d, m2, n2, t)
                B_sites = plaquette_sites(d, m2, n2, t)
                pairs_scanned += 1
                if license_verbatim(A_links + B_links):
                    verbatim_passes.append(((m1, n1), (m2, n2), t))
                if mutually_unit_proximate(A_sites, B_sites):
                    w_passes.append(((m1, n1), (m2, n2), t))
    check("ZERO two-plaquette unions pass the verbatim composite license"
          " (all plane pairs, all |t|_inf <= 4)",
          len(verbatim_passes) == 0,
          detail=f"pairs_scanned={pairs_scanned}")

    # ------------------------------------------------------------------
    section("(F) Conclusion V + the cross-plane mixed-derivative core (reproven)")
    Fv = {pl: sp.symbols(f"F{pl[0]}{pl[1]}") for pl in pls}
    f = sp.Function("f")
    action = sum(f(x) for x in Fv.values())
    cps = complementary_pairs(d)
    derivs = {f"{a}|{b}": sp.simplify(sp.diff(action, Fv[a], Fv[b])) for a, b in cps}
    check("sum of one-plane functions: all three cross-plane mixed derivatives vanish",
          all(v == 0 for v in derivs.values()),
          detail=str(derivs))
    check("ASSEMBLED (V): verbatim-licensed local terms are single-plaquette,"
          " so the landed cross-plane absence covers the WHOLE verbatim class"
          " (the multi-plaquette reopening is empty inside it)",
          len(verbatim_passes) == 0 and all(v == 0 for v in derivs.values()))

    # ------------------------------------------------------------------
    section("(G) W lift is not vacuous: genuine multi-plaquette witnesses pass")
    o4 = tuple([0] * 4)
    e0, e1, e2, e3 = (unit(4, k) for k in range(4))
    domino = (plaquette_sites(4, 0, 1, o4), plaquette_sites(4, 0, 1, e0))
    bent = (plaquette_sites(4, 0, 1, o4), plaquette_sites(4, 0, 2, o4))
    stacked = (plaquette_sites(4, 0, 1, o4), plaquette_sites(4, 0, 1, e2))
    check("domino, bent, and stacked plaquette pairs all pass the W lift"
          " (each factor licensed; pair mutually unit-proximate)",
          mutually_unit_proximate(*domino)
          and mutually_unit_proximate(*bent)
          and mutually_unit_proximate(*stacked))

    # ------------------------------------------------------------------
    section("(H) Complementary-plane exclusion under W (projection lemma)")
    comp_w_passes = [(p1, p2, t) for (p1, p2, t) in w_passes
                     if not (set(p1) & set(p2))]
    check("complementary-plane plaquette pairs fail the W lift at EVERY"
          " relative translation (exhaustive window)",
          len(comp_w_passes) == 0,
          detail=f"w_passes_total={len(w_passes)}")
    # Projection core: the (mu,nu)-projection of one factor is the four
    # corners of a unit square; the other factor projects to a single point;
    # L1 distance only grows under adding the remaining coordinates. No
    # integer point is within L1 distance 1 of all four unit-square corners.
    corners = [(0, 0), (1, 0), (0, 1), (1, 1)]
    covers = [c for c in itertools.product(range(-3, 5), repeat=2)
              if all(abs(c[0] - x) + abs(c[1] - y) <= 1 for x, y in corners)]
    check("no integer point lies within L1 distance 1 of all four unit-square"
          " corners (projection-lemma core; window exhaustive, tail monotone)",
          len(covers) == 0)

    # ------------------------------------------------------------------
    section("(I) Criterion: every W-licensed plaquette pair shares a direction")
    check("every W-pass plane pair shares >= 1 lattice direction",
          all(set(p1) & set(p2) for (p1, p2, t) in w_passes),
          detail=f"w_pass_plane_pairs={sorted(set((p1, p2) for (p1, p2, t) in w_passes))}")
    # In d=4 two distinct coordinate planes either share a direction or are
    # complementary, so "no complementary pair" <=> "pairwise sharing".
    check("d=4 plane dichotomy: distinct coordinate planes share a direction"
          " XOR are complementary",
          all((len(set(p1) & set(p2)) == 1) != (len(set(p1) & set(p2)) == 0)
              for p1, p2 in itertools.combinations(pls, 2)))

    # ------------------------------------------------------------------
    section("(J) Plane-set criterion for products (sympy, generic factors)")
    # Generic one-plane factors g_i = a_i + b_i*F_i + c_i*F_i**2; a product
    # over a plane set S carries a cross-plane monomial F_ab*F_cd iff S
    # contains the complementary pair {ab, cd}.
    def product_over(plane_set):
        expr = sp.Integer(1)
        for k, pl in enumerate(sorted(plane_set)):
            a, b, c = sp.symbols(f"a{k} b{k} c{k}")
            expr *= a + b * Fv[pl] + c * Fv[pl] ** 2
        return expr

    bad = []
    good_nonzero = []
    for r in range(1, 4):
        for S in itertools.combinations(pls, r):
            has_comp = any(not (set(p1) & set(p2))
                           for p1, p2 in itertools.combinations(S, 2))
            expr = product_over(S)
            coeffs = [expr.diff(Fv[a], Fv[b]).subs(
                {v: 0 for v in Fv.values()}) for a, b in cps
                if a in S and b in S]
            any_nonzero = any(sp.simplify(cf) != 0 for cf in coeffs)
            if not has_comp:
                full = [sp.simplify(expr.diff(Fv[a], Fv[b]))
                        for a, b in cps]
                if any(cf != 0 for cf in full):
                    bad.append(S)
            else:
                if any_nonzero:
                    good_nonzero.append(S)
    check("every pairwise-direction-sharing plane set (size <= 3): all three"
          " cross-plane coefficients vanish identically",
          len(bad) == 0)
    check("positive control: complementary-containing plane sets DO carry a"
          " nonzero cross-plane coefficient (the slot has teeth outside the license)",
          ((0, 1), (2, 3)) in [tuple(sorted(S)) for S in good_nonzero]
          or any(set([(0, 1), (2, 3)]).issubset(set(S)) for S in good_nonzero),
          detail=f"nonzero_sets={good_nonzero[:6]}")

    # ------------------------------------------------------------------
    section("(K) Assembled W theorem at every factor order")
    # The W condition is PAIRWISE: a complementary pair inside any W-licensed
    # multi-factor term would be a W-licensed complementary plaquette pair,
    # excluded by (H) at every translation. Belt-and-braces: enumerate all
    # W-licensed clusters of <= 3 factors anchored at a fixed first factor.
    anchor = ((0, 1), o4)
    anchor_sites = plaquette_sites(4, 0, 1, o4)
    partners = []
    for (m2, n2) in pls:
        for t in itertools.product(range(-3, 4), repeat=4):
            if (m2, n2) == (0, 1) and t == o4:
                continue
            B_sites = plaquette_sites(4, m2, n2, t)
            if mutually_unit_proximate(anchor_sites, B_sites):
                partners.append(((m2, n2), t, B_sites))
    triple_bad = 0
    triples = 0
    for (pa, ta, sa), (pb, tb, sb) in itertools.combinations(partners, 2):
        if mutually_unit_proximate(sa, sb):
            triples += 1
            plane_set = {(0, 1), pa, pb}
            if any(not (set(x) & set(y))
                   for x, y in itertools.combinations(plane_set, 2)):
                triple_bad += 1
    check("all W-licensed 2- and 3-factor clusters (anchored scan) have"
          " pairwise direction-sharing plane sets - no complementary pair",
          all(set((0, 1)) & set(p) for (p, t, s) in partners) and triple_bad == 0,
          detail=f"partners={len(partners)} licensed_triples={triples}")

    # ------------------------------------------------------------------
    section("(L) Hostile witness: the 06-07 clover cross-plane pair is license-external")
    C1 = plaquette_links(4, 0, 1, o4)
    C1s = plaquette_sites(4, 0, 1, o4)
    C2 = plaquette_links(4, 2, 3, o4)
    C2s = plaquette_sites(4, 2, 3, o4)
    clover_expr = product_over([(0, 1), (2, 3)])
    cl_coeff = sp.simplify(clover_expr.diff(Fv[(0, 1)], Fv[(2, 3)]).subs(
        {v: 0 for v in Fv.values()}))
    check("corner-touching 01 x 23 plaquette pair: fails verbatim license,"
          " fails W lift, yet its UNRESTRICTED product carries a nonzero"
          " F01*F23 coefficient (06-07 clover reopening preserved as"
          " license-external)",
          (not license_verbatim(C1 + C2))
          and (not mutually_unit_proximate(C1s, C2s))
          and cl_coeff != 0,
          detail=f"unrestricted_coeff={cl_coeff}")

    # ------------------------------------------------------------------
    section("(M) Boundary witness: chained clusters reopen the slot (X complement)")
    P1s = plaquette_sites(4, 0, 1, o4)
    P2s = plaquette_sites(4, 1, 2, o4)
    P3s = plaquette_sites(4, 2, 3, o4)
    chain_expr = product_over([(0, 1), (1, 2), (2, 3)])
    ch_coeff = sp.simplify(chain_expr.diff(Fv[(0, 1)], Fv[(2, 3)]).subs(
        {v: 0 for v in Fv.values()}))
    check("explicit 3-factor chain {01,12,23}: adjacent pairs W-pass, end pair"
          " W-fails, and the chained product carries a nonzero F01*F23"
          " coefficient - chain-connected clusters are the named open complement",
          mutually_unit_proximate(P1s, P2s)
          and mutually_unit_proximate(P2s, P3s)
          and (not mutually_unit_proximate(P1s, P3s))
          and ch_coeff != 0,
          detail=f"chain_coeff={ch_coeff}")

    # ------------------------------------------------------------------
    section("(N) d=3 corollary: no complementary spatial plane pair exists")
    check("d=3: among the 3 spatial coordinate planes, every pair shares a"
          " direction (the cross-plane pairing needs 4 distinct directions)",
          len(complementary_pairs(3)) == 0)

    # ------------------------------------------------------------------
    section("(O) Interface pins on the consumed dependency notes")
    lic_note = (DOCS / "PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md").read_text()
    check("license note pin: verbatim license condition string present",
          "min(d(p,a), d(p,b)) <= 1" in lic_note
          and "Unit-neighborhood link-support license" in lic_note)
    cp_note = (DOCS / "THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md").read_text()
    check("cross-plane note pin: the multi-plaquette reopening boundary this"
          " runner narrows is present verbatim",
          "Multi-plaquette terms, clover products, or any other action term with" in cp_note
          and "no local cross-plane `F tilde F` slot" in cp_note)

    # ------------------------------------------------------------------
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    if FAIL == 0:
        print(
            "VERDICT (bounded): within the adjacency-licensed action class the\n"
            "cross-plane FtildeF absence EXTENDS to local multi-plaquette terms:\n"
            "verbatim composite license -> single plaquettes only (all loop\n"
            "lengths; reopening empty); pairwise-proximity weakening -> genuine\n"
            "multi-plaquette products exist but complementary-plane pairs are\n"
            "excluded at every translation, so no cross-plane monomial at any\n"
            "factor order. The theta_gauge residual on this surface narrows to:\n"
            "(i) chain-connected non-pairwise-proximate cluster terms (explicit\n"
            "witness; license-external, as is the 06-07 clover), and (ii) the\n"
            "global winding-sector / emergent-Q bridge data. No license\n"
            "derivation, no theta closure, no audit status is claimed."
        )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
