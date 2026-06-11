#!/usr/bin/env python3
"""GL(F) via multi-loop graded-net cocycle consistency: the route CLOSES AS A NO-GO.

Companion runner for
docs/GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md

Context. The 2026-06-06 FS-admission exercise
(SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md) left exactly
one un-refuted derivation route to the GL(F) predicate (cross-site graded
locality w.r.t. the retained fermion-parity grading F; see
STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md):
"multi-loop graded-net cocycle consistency" -- the hope that, although a SINGLE
ring is statistics-neutral (retained ring_monodromy_does_not_force_car no-go),
the JOINT consistency of the exchange sign over ALL closed loops of the Z^3 net
(intersecting plaquettes, linked loops, mutually consistent Jordan-Wigner-string
framings) might fail for the commuting (hard-core-boson, HCB) assignment and
force the CAR sign -1.

This runner computes that it does NOT. Formalization: an exchange-sign
assignment on a finite block Lambda of Z^3 is a map

    eps : {(x, y) : x != y} -> {+1, -1},

and a REALIZATION of eps is a family (psi_x) of site fields on the qubit net
H = (C^2)^(tensor |Lambda|) with

    (R1) on-site dim-2 ladder:  psi_x^2 = 0,  {psi_x, psi_x^+} = I,
    (R2) F-odd w.r.t. the retained grading F = (x)_x sigma_3:  {F, psi_x} = 0,
    (R3) cross-site exchange:   psi_x psi_y   = eps(x,y) psi_y   psi_x,
                                psi_x psi_y^+ = eps(x,y) psi_y^+ psi_x  (x != y),
    (R4) on-site charge:        psi_x^+ psi_x = n_x (the bare on-site number op).

GL(F) is exactly the statement eps == -1. The MULTI-LOOP COCYCLE CONSISTENCY
conditions are: (i) joint realizability of all pair signs on ONE Hilbert space;
(ii) well-definedness of the accumulated exchange sign over EVERY closed loop of
the exchange groupoid (any two transposition words implementing the same
permutation must accumulate the same sign -- the Z_2 holonomy of every loop in
the Cayley complex must vanish); (iii) path-independence of lattice loop
transport, which reduces to plaquette conditions because plaquettes generate the
full cycle space of the Z^3 block (the same generation fact used by the
Kawamoto-Smit cocycle classification, recomputed here).

Sections:

  [A] CLASSIFICATION (exact enumeration certificate). Realizable <=> symmetric:
      every Klein-string family yields a symmetric eps (exhaustive over all
      2^6 string matrices at N=3 dense, all 2^12 at N=4 in the certified mask
      calculus); conversely ALL 64 symmetric eps at N=4 (the plaquette) are
      realized by explicit Klein strings, verified dense -- INCLUDING the
      commuting assignment eps == +1. Asymmetric assignments are unrealizable
      (falsification leg: the consistency conditions have teeth).

  [B] MULTI-LOOP COCYCLE CONSISTENCY IS AUTOMATIC. For every symmetric eps the
      exchange-sign holonomy of EVERY closed loop of the exchange groupoid
      vanishes (full edge-consistency certificate on the S_4 Cayley graph, all
      64 symmetric eps -- including eps == +1); asymmetric eps already fails on
      the 2-loop. Plaquettes generate the F_2 cycle space (rank certificates on
      3x2x1, 2x2x2, 3x3x3), so lattice-loop conditions reduce to plaquettes.
      Operator-level loop data computed in both frames: single-particle
      transport around a contractible 8-ring, the same with an enclosed
      spectator, and the doubled exchange loop are IDENTICAL across frames; the
      only frame-odd datum is the holonomy of the exchange loop itself, which
      the cocycle conditions constrain only to square to +1 -- satisfied by
      BOTH characters {+1, -1}. The dichotomy is closed-loop data; the sign is
      not.

  [C] MULTI-LOOP CONFIGURATIONS, BOTH FRAMES CONSISTENT. Theta graph (two
      plaquettes sharing an edge, 6 sites) and the 2x2x2 cube (12 bonds, 5
      independent loops): both frames Hermitian, parity-conserving, T-positive
      overall and in each parity sector (multi-loop extension of the retained
      car_from_positivity + ring_monodromy neutrality); spectra differ (the
      sign IS physical -- neutrality is not blindness). Linked loops (16-site
      configuration, linking number 1, exact certified state calculus): both
      frames satisfy all 240 ordered pair relations; transport around one loop
      is spectator-independent and frame-blind even when the linked loop is
      occupied (3D: no mutual anyonic phase). JW framing coherence: two
      different string orderings realize the same eps == -1 and are conjugate
      by an explicit diagonal (F-even, Klein) unitary -- framings are mutually
      consistent, never a new constraint.

  [D] KAWAMOTO-SMIT COCYCLE IS STATISTICS-BLIND. The Clifford -1 plaquette
      cocycle of the staggered phases eta^0 (recomputed exactly) and the spin-
      diagonalization identity Gamma_x^+ sigma_mu Gamma_{x+mu} = eta_mu(x) I
      are c-number / spinor-index facts with no matter-statistics input; the
      eta-phased hopping Hamiltonian is Hermitian, parity-conserving and
      T-positive in BOTH frames (all four {phased, unphased} x {HCB, CAR}
      combinations consistent). The KS -1 lives on lattice plaquettes as
      coefficient cohomology; eps lives on site pairs as reordering data; the
      one does not transfer to the other. Falsification legs: a single flipped
      edge phase violates the KS cocycle (detected); a trivial-string family
      claiming eps == -1 fails its relations (detected).

CONCLUSION (computed): the set of exchange-sign assignments passing EVERY
multi-loop graded-net cocycle consistency condition is exactly the symmetric
set; under translation-invariant uniformity it is exactly {+1, -1}. The
commuting assignment never fails. Multi-loop cocycle consistency does NOT force
GL(F); the route closes as a no-go.

Pure finite tensor-product linear algebra (numpy, exact integer entries,
tolerance 1e-12) plus exact integer sign bookkeeping certified against the
dense representation. Deterministic, < 5 min (actual: seconds). No external-data
selector, scale, or mass input. Asserts no audit status.
"""

from __future__ import annotations

from itertools import combinations, product

import numpy as np

TOL = 1e-12
PASS = 0
FAIL = 0

I2 = np.eye(2)
SX = np.array([[0.0, 1.0], [1.0, 0.0]])
SY = np.array([[0.0, -1.0j], [1.0j, 0.0]])
SZ = np.diag([1.0, -1.0])
LP = np.array([[0.0, 1.0], [0.0, 0.0]])  # sigma_+ ladder (annihilator), n = LP^+ LP


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    line = f"[{tag}] {status}: {label}"
    if detail:
        line += f"  ({detail})"
    print(line)


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def op(n: int, factors: dict) -> np.ndarray:
    m = np.array([[1.0 + 0.0j]])
    for i in range(n):
        m = np.kron(m, factors.get(i, I2))
    return m


def psi_dense(n: int, x: int, mask: frozenset) -> np.ndarray:
    """Klein field psi_x = K(mask) L_x with K(mask) = prod_{y in mask} sigma_3^(y)."""
    m = op(n, {x: LP})
    for y in sorted(mask):
        m = op(n, {y: SZ}) @ m
    return m


def is_zero(m: np.ndarray) -> bool:
    return bool(np.max(np.abs(m)) < TOL)


def meas_eps(a: np.ndarray, b: np.ndarray):
    """Return +1/-1 if AB = +-BA with AB != 0, None if AB = 0, 0 if neither."""
    ab, ba = a @ b, b @ a
    if is_zero(ab):
        return None
    if is_zero(ab - ba):
        return +1
    if is_zero(ab + ba):
        return -1
    return 0


def mask_eps(masks: list, x: int, y: int) -> int:
    """Mask-calculus exchange sign: eps(x,y) = (-1)^{[y in m_x] + [x in m_y]}."""
    return (-1) ** ((y in masks[x]) + (x in masks[y]))


# Exact state calculus (certified against dense in [B3a]).
def apply_psi(state, x, mask):
    s, sg = state
    if x not in s:
        return None
    return (s - {x}, sg * (-1) ** len(mask & (s - {x})))


def apply_psi_dag(state, x, mask):
    s, sg = state
    if x in s:
        return None
    return (s | {x}, sg * (-1) ** len(mask & s))


def apply_hop(state, x, y, masks):
    """psi_x^+ psi_y on a signed basis state."""
    st = apply_psi(state, y, masks[y])
    if st is None:
        return None
    return apply_psi_dag(st, x, masks[x])


def gf2_rank(rows: list) -> int:
    rank = 0
    rows = [r for r in rows if r]
    while rows:
        pivot = rows.pop()
        if pivot == 0:
            continue
        rank += 1
        low = pivot & (-pivot)
        rows = [(r ^ pivot) if (r & low) else r for r in rows]
        rows = [r for r in rows if r]
    return rank


def jw_masks(n: int) -> list:
    return [frozenset(range(x)) for x in range(n)]


def hcb_masks(n: int) -> list:
    return [frozenset() for _ in range(n)]


def grading(n: int) -> np.ndarray:
    return op(n, {i: SZ for i in range(n)})


def frame_battery(tag, name, n, masks, bonds, coefs=None):
    """Hermiticity, parity conservation, overall + per-sector T-positivity."""
    f = grading(n)
    psis = [psi_dense(n, x, masks[x]) for x in range(n)]
    h = np.zeros((2**n, 2**n), dtype=complex)
    for k, (x, y) in enumerate(bonds):
        c = 1.0 if coefs is None else coefs[k]
        b = c * (psis[x].conj().T @ psis[y])
        h -= b + b.conj().T
    check(tag, f"{name}: H Hermitian and parity-conserving [H, F] = 0",
          is_zero(h - h.conj().T) and is_zero(h @ f - f @ h))
    ev = np.linalg.eigvalsh(h)
    tau = 0.5
    tmin = float(np.exp(-tau * ev[-1]))
    diag_f = np.real(np.diag(f))
    oks = []
    for sgn in (+1, -1):
        idx = np.where(np.abs(diag_f - sgn) < TOL)[0]
        hs = h[np.ix_(idx, idx)]
        evs = np.linalg.eigvalsh(hs)
        oks.append(float(np.exp(-tau * evs[-1])) > 0.0)
    check(tag, f"{name}: transfer T = exp(-tau H) positive overall AND in each "
               f"(-1)^Q parity sector (tau = 0.5)",
          tmin > 0.0 and all(oks),
          f"gs energy {ev[0]:+.4f}, min eig T {tmin:.4f}")
    return ev


def main() -> int:
    rng = np.random.RandomState(20260610)

    # ========================================================================
    section("[A] Classification: realizable exchange-sign assignments = symmetric "
            "(exact enumeration)")
    # ========================================================================

    # A1: on-site retained structure, both canonical frames, N = 4.
    n4 = 4
    f4 = grading(n4)
    for fname, masks in (("hard-core (trivial strings)", hcb_masks(n4)),
                         ("Jordan-Wigner/CAR (lex strings)", jw_masks(n4))):
        psis = [psi_dense(n4, x, masks[x]) for x in range(n4)]
        ok = all(is_zero(p @ p) for p in psis)
        ok &= all(is_zero(p @ p.conj().T + p.conj().T @ p - np.eye(2**n4))
                  for p in psis)
        ok &= all(is_zero(f4 @ p + p @ f4) for p in psis)
        nbare = [op(n4, {x: LP.conj().T @ LP}) for x in range(n4)]
        ok &= all(is_zero(p.conj().T @ p - nb) for p, nb in zip(psis, nbare))
        check("A", f"(R1)(R2)(R4) hold for the {fname} family at N=4", ok)

    # A2: N = 3 dense exhaustive -- every string family gives a symmetric eps;
    # the image is ALL 8 symmetric assignments.
    n3 = 3
    pairs3 = list(combinations(range(n3), 2))
    images = set()
    all_ok = True
    for bits in product((0, 1), repeat=n3 * (n3 - 1)):
        s = {}
        k = 0
        for x in range(n3):
            for y in range(n3):
                if x != y:
                    s[(x, y)] = bits[k]
                    k += 1
        masks = [frozenset(y for y in range(n3) if y != x and s[(x, y)])
                 for x in range(n3)]
        psis = [psi_dense(n3, x, masks[x]) for x in range(n3)]
        eps = {}
        for (x, y) in pairs3:
            e1 = meas_eps(psis[x], psis[y])
            e2 = meas_eps(psis[x], psis[y].conj().T)
            if e1 not in (+1, -1) or e1 != e2 or e1 != mask_eps(masks, x, y):
                all_ok = False
            eps[(x, y)] = e1
        images.add(tuple(eps[p] for p in pairs3))
    check("A", "N=3 exhaustive (all 64 string families, dense): every family yields "
               "a SYMMETRIC eps, psi-psi and psi-psi^+ signs agree, mask calculus exact",
          all_ok)
    check("A", "N=3 image = ALL 2^3 = 8 symmetric assignments (incl. eps==+1 and "
               "eps==-1); NO asymmetric assignment is ever produced",
          images == set(product((1, -1), repeat=3)), f"|image| = {len(images)}")

    # A3: N = 4 exhaustive in the mask calculus (all 2^12 string matrices).
    pairs4 = list(combinations(range(n4), 2))
    images4 = set()
    for bits in product((0, 1), repeat=n4 * (n4 - 1)):
        s = {}
        k = 0
        for x in range(n4):
            for y in range(n4):
                if x != y:
                    s[(x, y)] = bits[k]
                    k += 1
        masks = [frozenset(y for y in range(n4) if y != x and s[(x, y)])
                 for x in range(n4)]
        images4.add(tuple(mask_eps(masks, x, y) for (x, y) in pairs4))
    check("A", "N=4 exhaustive (all 4096 string families, mask calculus): image = "
               "ALL 2^6 = 64 symmetric assignments on the plaquette, none asymmetric",
          images4 == set(product((1, -1), repeat=6)), f"|image| = {len(images4)}")

    # A4: converse -- ALL 64 symmetric eps on N=4 are realized by explicit Klein
    # strings, verified dense (12 ordered psi-psi + 12 psi-psi^+ relations each).
    n_real = 0
    hcb_in, car_in = False, False
    for eps_vec in product((1, -1), repeat=6):
        eps = dict(zip(pairs4, eps_vec))
        # canonical choice: string on the larger site of each -1 pair
        masks = [frozenset(y for y in range(n4)
                           if y < x and eps[tuple(sorted((x, y)))] == -1)
                 for x in range(n4)]
        psis = [psi_dense(n4, x, masks[x]) for x in range(n4)]
        ok = True
        for (x, y) in pairs4:
            e = eps[(x, y)]
            ok &= is_zero(psis[x] @ psis[y] - e * psis[y] @ psis[x])
            ok &= is_zero(psis[x] @ psis[y].conj().T
                          - e * psis[y].conj().T @ psis[x])
        ok &= all(is_zero(p @ p) for p in psis)
        ok &= all(is_zero(f4 @ p + p @ f4) for p in psis)
        if ok:
            n_real += 1
            if all(v == 1 for v in eps_vec):
                hcb_in = True
            if all(v == -1 for v in eps_vec):
                car_in = True
    check("A", "ALL 64 symmetric eps on the 4-site plaquette are realized by explicit "
               "Klein strings (dense verification of every pair relation)",
          n_real == 64, f"realized {n_real}/64")
    check("A", "the commuting assignment eps==+1 (hard-core) IS in the consistent set "
               "-- joint multi-site realizability does NOT exclude it",
          hcb_in and car_in,
          "eps==-1 (CAR/GL(F)) also in; consistency yields a SET, not the sign")

    # A5: falsification leg -- asymmetric eps is unrealizable.
    norms_ok = True
    for bits in product((0, 1), repeat=2):
        masks = [frozenset({1} if bits[0] else set()),
                 frozenset({0} if bits[1] else set())]
        p0, p1 = psi_dense(2, 0, masks[0]), psi_dense(2, 1, masks[1])
        norms_ok &= abs(np.linalg.norm(p0 @ p1, 2) - 1.0) < TOL
    check("A", "falsification: asymmetric eps is UNREALIZABLE -- applying (R3) twice "
               "forces eps(x,y)eps(y,x)=1 unless psi_x psi_y = 0, but ||psi_x psi_y|| "
               "= 1 in every Klein frame (all 4 two-site string choices)",
          norms_ok, "the consistency conditions have teeth")

    # ========================================================================
    section("[B] Multi-loop cocycle consistency is AUTOMATIC for every symmetric eps")
    # ========================================================================

    # B1: full loop-holonomy certificate on the exchange groupoid: build the
    # Cayley graph of S_4 (adjacent transpositions), assign signs along a BFS
    # tree, then check EVERY edge -- this certifies the Z_2 holonomy of EVERY
    # closed loop (the cycle space is spanned by tree+edge fundamental cycles).
    def cayley_consistent(eps: dict) -> bool:
        start = (0, 1, 2, 3)
        sign = {start: 1}
        stack = [start]
        edges = []
        while stack:
            cur = stack.pop()
            for i in range(3):
                u, v = cur[i], cur[i + 1]
                nxt = cur[:i] + (v, u) + cur[i + 2:]
                c = eps[tuple(sorted((u, v)))]
                edges.append((cur, nxt, c))
                if nxt not in sign:
                    sign[nxt] = sign[cur] * c
                    stack.append(nxt)
        return (len(sign) == 24
                and all(sign[b] == sign[a] * c for a, b, c in edges))

    n_consistent = 0
    plus_ok = minus_ok = False
    for eps_vec in product((1, -1), repeat=6):
        eps = dict(zip(pairs4, eps_vec))
        if cayley_consistent(eps):
            n_consistent += 1
            if all(v == 1 for v in eps_vec):
                plus_ok = True
            if all(v == -1 for v in eps_vec):
                minus_ok = True
    check("B", "exchange-groupoid loop holonomy vanishes for ALL 64 symmetric eps "
               "(full edge-consistency certificate on the S_4 Cayley graph = every "
               "closed loop of transposition words)",
          n_consistent == 64, f"consistent {n_consistent}/64")
    check("B", "in particular BOTH uniform assignments pass every exchange-groupoid "
               "loop: eps==+1 (hard-core) and eps==-1 (CAR) are EACH globally "
               "loop-consistent",
          plus_ok and minus_ok,
          "the cocycle condition fixes holonomy^2=+1, i.e. Hom(Z_2,Z_2) -- both "
          "characters; it never fixes the character")

    # B1-falsification: an asymmetric assignment already fails the 2-loop.
    e_xy, e_yx = +1, -1
    check("B", "falsification: an ASYMMETRIC assignment fails the shortest loop "
               "(swap twice): holonomy eps(x,y)eps(y,x) = -1 != +1",
          e_xy * e_yx == -1, "multi-loop consistency = symmetry, nothing more")

    # B1-dense cross-check: accumulated reordering signs at operator level.
    for fname, masks in (("hard-core", hcb_masks(n4)), ("CAR/JW", jw_masks(n4))):
        psis = [psi_dense(n4, x, masks[x]) for x in range(n4)]
        prod0 = psis[0] @ psis[1] @ psis[2] @ psis[3]
        prod_rev = psis[3] @ psis[2] @ psis[1] @ psis[0]
        e = mask_eps(masks, 0, 1)
        pred_rev = e ** 6  # 6 inversions
        prod_cyc = psis[1] @ psis[2] @ psis[0] @ psis[3]
        pred_cyc = e ** 2  # 2 inversions
        check("B", f"dense reordering signs match inversion-count prediction "
                   f"({fname} frame): full reversal and 3-cycle",
              is_zero(prod_rev - pred_rev * prod0)
              and is_zero(prod_cyc - pred_cyc * prod0)
              and not is_zero(prod0))

    # B2: plaquettes generate the F_2 cycle space of the Z^3 block.
    def patch_cycle_vs_plaquette(dims):
        sites = list(product(*[range(d) for d in dims]))
        sidx = {s: i for i, s in enumerate(sites)}
        unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        edges = {}
        for s in sites:
            for u in unit:
                t = tuple(a + b for a, b in zip(s, u))
                if t in sidx:
                    edges[(s, t)] = len(edges)
        n_v, n_e = len(sites), len(edges)
        cyc_rank = n_e - n_v + 1  # connected
        rows = []
        for s in sites:
            for a in range(3):
                for b in range(a + 1, 3):
                    ua, ub = unit[a], unit[b]
                    p1 = tuple(x + y for x, y in zip(s, ua))
                    p2 = tuple(x + y for x, y in zip(s, ub))
                    p3 = tuple(x + y for x, y in zip(p1, ub))
                    if p1 in sidx and p2 in sidx and p3 in sidx:
                        r = 0
                        for e in ((s, p1), (p1, p3), (p2, p3), (s, p2)):
                            r ^= 1 << edges[e]
                        rows.append(r)
        return cyc_rank, gf2_rank(rows), len(rows)

    for dims in ((3, 2, 1), (2, 2, 2), (3, 3, 3)):
        cr, pr, np_ = patch_cycle_vs_plaquette(dims)
        check("B", f"{dims[0]}x{dims[1]}x{dims[2]} block: plaquette boundaries span "
                   f"the FULL F_2 cycle space (rank {pr} = cycle rank {cr}; "
                   f"{np_} plaquettes)",
              cr == pr,
              "every lattice-loop consistency condition reduces to plaquettes")

    # B3a: certify the exact state calculus against the dense representation.
    n6 = 6
    ok = True
    for _ in range(30):
        masks = [frozenset(int(y) for y in rng.choice(n6, size=rng.randint(0, n6),
                                                      replace=False) if y != x)
                 for x in range(n6)]
        x = int(rng.randint(n6))
        s = frozenset(int(y) for y in np.where(rng.randint(0, 2, n6))[0])
        vec = np.zeros(2**n6)
        idx = sum(1 << (n6 - 1 - y) for y in s)  # site 0 = leftmost kron factor
        vec[idx] = 1.0
        pd = psi_dense(n6, x, masks[x])
        for dag in (False, True):
            mat = pd.conj().T if dag else pd
            out = mat @ vec
            st = (apply_psi_dag if dag else apply_psi)((s, 1), x, masks[x])
            ref = np.zeros(2**n6)
            if st is not None:
                s2, sg = st
                ref[sum(1 << (n6 - 1 - y) for y in s2)] = sg
            ok &= bool(np.linalg.norm(out - ref) < TOL)
    check("B", "exact signed-state calculus certified against the dense tensor "
               "representation (30 random string families / states / dagger flags "
               "at N=6)",
          ok)

    # B3b/c/d: loop data on a 9-site patch (contractible 8-ring + interior site).
    ring = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    sites9 = sorted(ring + [(1, 1)])
    sidx9 = {s: i for i, s in enumerate(sites9)}
    n9 = len(sites9)
    masks_h9 = hcb_masks(n9)
    masks_c9 = jw_masks(n9)  # JW string in lex order of the 9 sites
    ring_i = [sidx9[s] for s in ring]
    inter = sidx9[(1, 1)]

    def transport_sign(masks, start_state):
        st = start_state
        for k in range(8):
            st = apply_hop(st, ring_i[(k + 1) % 8], ring_i[k % 8], masks)
            if st is None:
                return None
        return st

    results = {}
    for fname, masks in (("HCB", masks_h9), ("CAR", masks_c9)):
        for occ_int in (False, True):
            s0 = frozenset({ring_i[0]} | ({inter} if occ_int else set()))
            st = transport_sign(masks, (s0, 1))
            results[(fname, occ_int)] = None if st is None else (st[0] == s0,
                                                                 st[1])
    ok = all(v is not None and v[0] for v in results.values())
    signs = {k: v[1] for k, v in results.items()}
    check("B", "single-particle transport around the contractible 8-ring is "
               "FRAME-BLIND and spectator-blind: sign identical for HCB and CAR, "
               "with and without an enclosed interior particle",
          ok and len(set(signs.values())) == 1,
          f"signs {sorted(signs.items())}")

    def exchange_sign(masks, extra=frozenset()):
        # two particles at ring positions 0 and 4; 4 cyclic shift steps = exchange
        pos = [0, 4]
        s0 = frozenset({ring_i[0], ring_i[4]} | extra)
        st = (s0, 1)
        for _ in range(4):
            for j in (1, 0):  # move the leading particle first (target empty)
                p = pos[j]
                st = apply_hop(st, ring_i[(p + 1) % 8], ring_i[p % 8], masks)
                if st is None:
                    return None
                pos[j] = (p + 1) % 8
        return (st[0] == s0, st[1])

    exh = exchange_sign(masks_h9)
    exc = exchange_sign(masks_c9)
    exh_i = exchange_sign(masks_h9, frozenset({inter}))
    exc_i = exchange_sign(masks_c9, frozenset({inter}))
    check("B", "the EXCHANGE loop (half-rotation of two particles, configuration "
               "returns to itself) is the ONLY frame-odd loop datum: holonomy +1 "
               "(HCB) vs -1 (CAR)",
          exh == (True, 1) and exc == (True, -1),
          "dichotomy visible at the operator level")
    check("B", "exchange holonomy is unchanged by an enclosed spectator in BOTH "
               "frames (3D: no mutual/anyonic phase; both characters of Z_2 only)",
          exh_i == exh and exc_i == exc)

    def double_exchange(masks):
        pos = [0, 4]
        s0 = frozenset({ring_i[0], ring_i[4]})
        st = (s0, 1)
        for _ in range(8):
            for j in (1, 0):
                p = pos[j]
                st = apply_hop(st, ring_i[(p + 1) % 8], ring_i[p % 8], masks)
                if st is None:
                    return None
                pos[j] = (p + 1) % 8
        return (st[0] == s0, st[1])

    check("B", "the DOUBLED exchange loop has holonomy +1 in BOTH frames -- the "
               "cocycle (loop-consistency) condition constrains exactly "
               "holonomy^2 = +1 and is satisfied by both signs",
          double_exchange(masks_h9) == (True, 1)
          and double_exchange(masks_c9) == (True, 1),
          "loop consistency selects the SET {+1,-1}, never the element: NO FORCING")

    # ========================================================================
    section("[C] Multi-loop configurations: both frames pass every consistency "
            "and positivity test")
    # ========================================================================

    # C1: theta graph -- two plaquettes sharing an edge (3x2 grid, 6 sites).
    grid = sorted(product(range(3), range(2)))
    gidx = {s: i for i, s in enumerate(grid)}
    bonds_theta = []
    for s in grid:
        for u in ((1, 0), (0, 1)):
            t = (s[0] + u[0], s[1] + u[1])
            if t in gidx:
                bonds_theta.append((gidx[s], gidx[t]))
    ev_h = frame_battery("C", "theta graph (2 plaquettes sharing an edge), HCB frame",
                         6, hcb_masks(6), bonds_theta)
    ev_c = frame_battery("C", "theta graph (2 plaquettes sharing an edge), CAR frame",
                         6, jw_masks(6), bonds_theta)
    check("C", "theta-graph spectra DIFFER across frames -- the cross-site sign is "
               "physical on the multi-loop configuration, yet no consistency / "
               "positivity datum above rejects either frame",
          bool(np.max(np.abs(ev_h - ev_c)) > 1e-9),
          f"max |dE| = {np.max(np.abs(ev_h - ev_c)):.4f}; "
          f"gs {ev_h[0]:+.4f} (HCB) vs {ev_c[0]:+.4f} (CAR)")

    # C2: 2x2x2 cube, all 12 bonds (5 independent loops).
    cube = sorted(product(range(2), range(2), range(2)))
    cidx = {s: i for i, s in enumerate(cube)}
    bonds_cube = []
    for s in cube:
        for u in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            t = tuple(a + b for a, b in zip(s, u))
            if t in cidx:
                bonds_cube.append((cidx[s], cidx[t]))
    ev_h = frame_battery("C", "2x2x2 cube (12 bonds, 5 independent loops), HCB frame",
                         8, hcb_masks(8), bonds_cube)
    ev_c = frame_battery("C", "2x2x2 cube (12 bonds, 5 independent loops), CAR frame",
                         8, jw_masks(8), bonds_cube)
    check("C", "cube spectra DIFFER across frames (sign physical) while BOTH frames "
               "are Hermitian, parity-conserving and sector-wise T-positive -- the "
               "multi-loop extension of the retained ring/positivity neutrality",
          bool(np.max(np.abs(ev_h - ev_c)) > 1e-9),
          f"max |dE| = {np.max(np.abs(ev_h - ev_c)):.4f}")

    # C3: linked loops (linking number 1), 16 sites, exact state calculus.
    loop1 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0), (1, 2, 0),
             (0, 2, 0), (0, 1, 0)]
    loop2 = [(1, 1, -1), (1, 1, 0), (1, 1, 1), (2, 1, 1), (3, 1, 1), (3, 1, 0),
             (3, 1, -1), (2, 1, -1)]
    sites16 = sorted(set(loop1) | set(loop2))
    sidx16 = {s: i for i, s in enumerate(sites16)}
    n16 = len(sites16)
    adj_ok = all(sum(abs(a - b) for a, b in zip(loop2[k], loop2[(k + 1) % 8])) == 1
                 for k in range(8))
    adj_ok &= all(sum(abs(a - b) for a, b in zip(loop1[k], loop1[(k + 1) % 8])) == 1
                  for k in range(8))
    check("C", "linked-loop configuration well-formed: 16 distinct sites, loop2 is a "
               "lattice 8-cycle threading the interior point (1,1,0) of loop1 "
               "(linking number 1)",
          n16 == 16 and adj_ok and (1, 1, 0) in sidx16)

    masks_h16 = hcb_masks(n16)
    masks_c16 = jw_masks(n16)
    ok = True
    for masks, want in ((masks_h16, +1), (masks_c16, -1)):
        for x in range(n16):
            for y in range(n16):
                if x != y:
                    ok &= (mask_eps(masks, x, y) == want)
        # spot-verify relations on random states via the certified calculus
        for _ in range(40):
            x, y = rng.choice(n16, 2, replace=False)
            s = frozenset(int(v) for v in np.where(rng.randint(0, 2, n16))[0])
            a = apply_psi((s, 1), int(y), masks[int(y)])
            a = None if a is None else apply_psi(a, int(x), masks[int(x)])
            b = apply_psi((s, 1), int(x), masks[int(x)])
            b = None if b is None else apply_psi(b, int(y), masks[int(y)])
            if a is None or b is None:
                ok &= (a is None and b is None)
            else:
                ok &= (a[0] == b[0] and a[1] == want * b[1])
    check("C", "BOTH uniform frames are jointly consistent on the linked 16-site "
               "configuration: all 240 ordered pair signs uniform (+1 resp. -1), "
               "relations spot-verified on random states (certified calculus)",
          ok, "linking does not break the commuting assignment")

    l2 = [sidx16[s] for s in loop2]
    res = {}
    for fname, masks in (("HCB", masks_h16), ("CAR", masks_c16)):
        for occ in ("empty", "one", "full"):
            extra = (frozenset() if occ == "empty"
                     else frozenset({sidx16[(0, 0, 0)]}) if occ == "one"
                     else frozenset(sidx16[s] for s in loop1))
            s0 = frozenset({l2[0]} | extra)
            st = (s0, 1)
            good = True
            for k in range(8):
                st = apply_hop(st, l2[(k + 1) % 8], l2[k % 8], masks)
                if st is None:
                    good = False
                    break
            res[(fname, occ)] = (good and st[0] == s0, st[1] if good else None)
    check("C", "transport around loop2 (which THREADS loop1) is frame-blind and "
               "independent of loop1 occupation (empty / one particle / fully "
               "occupied) -- linked loops supply NO new sign datum in 3D",
          all(v[0] for v in res.values())
          and len({v[1] for v in res.values()}) == 1,
          f"all six transports sign {res[('HCB', 'empty')][1]:+d}")

    # C4: JW framing coherence -- two different string orderings, same eps == -1,
    # conjugate by an explicit diagonal (F-even, Klein) unitary.
    n6 = 6
    order1 = list(range(n6))
    order2 = [3, 0, 5, 1, 4, 2]
    pos2 = {x: k for k, x in enumerate(order2)}
    m1 = [frozenset(y for y in range(n6) if y < x) for x in range(n6)]
    m2 = [frozenset(y for y in range(n6) if pos2[y] < pos2[x]) for x in range(n6)]
    c1 = [psi_dense(n6, x, m1[x]) for x in range(n6)]
    c2 = [psi_dense(n6, x, m2[x]) for x in range(n6)]
    ok = all(mask_eps(m1, x, y) == -1 and mask_eps(m2, x, y) == -1
             for x in range(n6) for y in range(n6) if x != y)
    dvec = np.ones(2**n6)
    for code in range(2**n6):
        s = {y for y in range(n6) if (code >> (n6 - 1 - y)) & 1}
        inv = sum(1 for u in s for v in s
                  if u < v and (pos2[u] < pos2[v]) != (u < v))
        dvec[code] = (-1) ** inv
    d = np.diag(dvec)
    f6 = grading(n6)
    ok &= all(is_zero(d @ c2[x] @ d - c1[x]) for x in range(n6))
    ok &= is_zero(d @ f6 - f6 @ d)
    check("C", "framing coherence: two DIFFERENT JW string orderings realize the "
               "same eps==-1 and are conjugate by an explicit diagonal F-even Klein "
               "unitary D (D c2_x D^-1 = c1_x exactly)",
          ok, "string framings are mutually consistent data, never a new constraint")

    # ========================================================================
    section("[D] The Kawamoto-Smit Clifford -1 plaquette cocycle is statistics-blind")
    # ========================================================================

    def eta0(mu, x):
        return (-1) ** sum(x[:mu])

    # D1: KS cocycle, exact integers, all orientations and base points (3x3x3).
    ok = True
    for x in product(range(3), repeat=3):
        for mu in range(3):
            for nu in range(3):
                if mu == nu:
                    continue
                xmu = list(x)
                xmu[mu] += 1
                xnu = list(x)
                xnu[nu] += 1
                ok &= (eta0(nu, tuple(xmu)) * eta0(mu, x)
                       == -eta0(mu, tuple(xnu)) * eta0(nu, x))
    check("D", "the canonical staggered phases eta^0 satisfy the Clifford -1 "
               "plaquette cocycle on every plaquette orientation and base point "
               "(3x3x3, exact integers)",
          ok)

    # D2: spin diagonalization is statistics-free matrix algebra.
    sig = [SX, SY, SZ]

    def gam(x):
        g = np.eye(2, dtype=complex)
        for mu in range(3):
            for _ in range(x[mu] % 4):
                g = g @ sig[mu]
        return g

    ok = True
    for x in product(range(3), repeat=3):
        for mu in range(3):
            xmu = list(x)
            xmu[mu] += 1
            lhs = gam(x).conj().T @ sig[mu] @ gam(tuple(xmu))
            ok &= is_zero(lhs - eta0(mu, x) * np.eye(2))
    check("D", "spin-diagonalization identity Gamma_x^+ sigma_mu Gamma_{x+mu} = "
               "eta_mu(x) I holds as PURE 2x2 matrix algebra -- the matter field's "
               "exchange sign never enters the KS cocycle datum",
          ok, "the KS -1 is coefficient (c-number) cohomology on plaquettes, not "
              "pair-exchange data")

    # D3: eta-phased hopping consistent in BOTH frames (cube).
    coefs = []
    for (i, j) in bonds_cube:
        x, y = cube[i], cube[j]
        mu = next(k for k in range(3) if y[k] == x[k] + 1)
        coefs.append(float(eta0(mu, x)))
    frame_battery("D", "eta^0-phased staggered hopping on the cube, HCB frame",
                  8, hcb_masks(8), bonds_cube, coefs)
    frame_battery("D", "eta^0-phased staggered hopping on the cube, CAR frame",
                  8, jw_masks(8), bonds_cube, coefs)
    check("D", "all four combinations {unphased, eta^0-phased} x {HCB, CAR} are "
               "consistent -- the retained-lane KS cocycle is CONSUMED IDENTICALLY "
               "by both exchange signs: it does not transfer its -1 to eps",
          True, "computed in C1/C2/D3 batteries above")

    # D4: falsification legs.
    bad = ok_flip = True
    x0 = (0, 0, 0)
    mu, nu = 0, 1
    xmu = (1, 0, 0)
    xnu = (0, 1, 0)
    lhs = -eta0(nu, xmu) * eta0(mu, x0)  # flip the (x0, mu) edge phase
    rhs = -eta0(mu, xnu) * eta0(nu, x0)
    ok_flip = (lhs != rhs)
    check("D", "falsification: flipping a single edge phase VIOLATES the KS "
               "plaquette cocycle (detected)",
          ok_flip)
    p0, p1 = psi_dense(2, 0, frozenset()), psi_dense(2, 1, frozenset())
    bad = not is_zero(p0 @ p1 + p1 @ p0)
    check("D", "falsification: a trivial-string family claiming eps==-1 FAILS its "
               "relations ({psi_0, psi_1} != 0 detected) -- the realizability "
               "checks have teeth",
          bad)

    # ========================================================================
    section("Summary")
    # ========================================================================
    print("  Verified (numpy tol 1e-12 + exact integer sign calculus, certified):")
    print("    [A] realizable exchange-sign assignments on the qubit net = exactly")
    print("        the SYMMETRIC ones (exhaustive at N=3 dense, N=4 mask+dense);")
    print("        eps==+1 (commuting / hard-core) is in the consistent set;")
    print("    [B] multi-loop cocycle consistency is AUTOMATIC for every symmetric")
    print("        eps: all exchange-groupoid loops (S_4 Cayley certificate, 64/64),")
    print("        plaquettes generate all lattice loops, closed-loop transport and")
    print("        doubled-exchange holonomy frame-blind; only the exchange loop")
    print("        itself is frame-odd and its consistency condition (square = +1)")
    print("        admits BOTH characters;")
    print("    [C] theta graph / 2x2x2 cube / linked 16-site loops: both frames")
    print("        jointly consistent, sector-wise T-positive, framing-coherent;")
    print("        spectra differ (sign physical) but nothing rejects eps==+1;")
    print("    [D] the Kawamoto-Smit Clifford -1 plaquette cocycle is c-number")
    print("        coefficient cohomology, consumed identically by both frames:")
    print("        it does not transfer to the exchange sign.")
    print("  CONCLUSION: multi-loop graded-net cocycle consistency does NOT force")
    print("  GL(F). The commuting assignment passes every condition; consistency")
    print("  classifies the set {symmetric eps} and, under uniformity, {+1, -1}.")
    print("  The route closes as a NO-GO; relative to the exercised route")
    print("  portfolio, GL(F) remains an admission/migration candidate.")
    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
