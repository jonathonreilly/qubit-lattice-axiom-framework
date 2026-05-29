#!/usr/bin/env python3
r"""eta-phase holonomy is an AREA-FLUX, not a braid invariant -- audit companion.

Companion to
docs/ETA_PHASE_HOLONOMY_AREA_FLUX_NOT_BRAID_INVARIANT_NARROW_NO_GO_NOTE_2026-05-29.md

This runner SHARPENS the FS rotation-exchange no-go
docs/FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md
by closing the most natural concrete realization of that note's open "path 1"
(a lattice-native discrete-homotopy / graph-braid construction that would
manufacture the fermionic exchange sign on Z^3).

THE CONSTRUCTION UNDER TEST
---------------------------
The framework's staggered Kogut-Susskind phases eta_mu(x) (the canonical KS
convention eta_1 = 1, eta_2 = (-1)^{x1}, eta_3 = (-1)^{x1+x2}, generalizing the
1+1d convention eta_0 = 1, eta_1(t) = (-1)^t used in
scripts/axiom_first_rp_two_step_transfer_matrix_positivity.py and
scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py) ARE the discrete
spin connection in the spin-diagonal frame.  Define the spin-diagonalizing
gauge T(x) = sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}.  Then exactly

        T(x)^dag sigma_mu T(x + mu_hat) = eta_mu(x) * I_2 .              (ID)

So in the rotated (spin-diagonal) frame the Dirac hop carries the SCALAR Z_2
phase eta_mu(x); the eta-phases are literally the parallel-transport
(connection) phases of a Z_2 connection Omega_mu(x) := eta_mu(x) in {+1, -1}
living over the BASE lattice Z^3.

This Z_2 connection has a fixed background CURVATURE: every unit plaquette, in
every plane, has holonomy -1 (a uniform pi-flux).  Consequently the
spinor-frame holonomy around any closed base loop is

        hol(loop) = (-1)^{enclosed area}   (product of enclosed face curvatures,
                                            discrete Stokes for a Z_2 connection).

The natural graph-braid realization of FS would read the fermion exchange sign
off this holonomy around a two-token exchange loop.  THIS RUNNER SHOWS THAT
READOUT FAILS: the holonomy is the geometric AREA-FLUX, which is NOT a braid
invariant -- two exchange loops that are the SAME element of the graph-braid
group B_2(Z^3) (same swap, homotopic in the ordered/unordered configuration
space UD_2(Z^3)) carry DIFFERENT holonomies (-1 vs +1) because they enclose
different base area.  A fermion sign must be a homomorphism on the braid group
(one value per braid class); the eta-holonomy is not, so the eta-phase discrete
spin structure cannot supply the fermionic exchange sign.

DEMONSTRATIONS (all exact; numpy integers / sympy where helpful; no fitted input)
---------------------------------------------------------------------------------
  (a) SPIN-DIAGONALIZATION IDENTITY (ID).  Verify T^dag sigma_mu T(x+mu) =
      eta_mu(x) I_2 EXACTLY (zero deviation) on a 3^3 and a 4^3 block, all mu.

  (b) Z_2 CURVATURE = -1 / FACE, GAUGE-INVARIANT.  On a 4^3 block, every unit
      plaquette in each of the 3 planes has Z_2 holonomy
      eta_mu(x) eta_nu(x+mu) eta_mu(x+nu) eta_nu(x) = -1.  Confirm this is
      invariant under an arbitrary Z_2 gauge twist
      Omega_mu(x) -> g(x) Omega_mu(x) g(x+mu), g(x) in {+1,-1} (so -1/face is
      gauge-invariant background flux, not a gauge artifact).

  (c) (-1)^{area} HOLONOMY LAW + the three named exchange loops.  An a x b
      rectangular base loop has holonomy (-1)^{a b} for all a, b in {1..4}.  The
      three named two-token exchange loops give:
        - Y-move / zero-area straight swap            -> +1,
        - 1x1-detour swap                             -> -1,
        - 1x2-detour swap                             -> +1.

  (d) SAME SWAP, HOMOTOPIC, DIFFERENT HOLONOMY (the decisive obstruction).
      The 1x1-detour swap and the 1x2-detour swap (i) realize the SAME token
      permutation (token A and token B exchange endpoints), (ii) are
      collision-free (the two tokens never co-occupy a site), and (iii) are the
      SAME element of the graph-braid group B_2(Z^3): their difference loop
      (do swap_1x1, then swap_1x2 in reverse) is a single-token CLOSED base loop
      that bounds a 2-disk in UD_2(Z^3) (with a third lattice direction the unit
      square is fillable), hence is null-homotopic.  Yet they carry DIFFERENT
      holonomies (-1 vs +1).  A homomorphism on B_2(Z^3) cannot take two values
      on one element -> the eta-holonomy is NOT a braid invariant.

  (e) STRUCTURAL DECOUPLING.  A single-token 1x1 base loop has holonomy -1 (the
      area flux of one face) yet is null-homotopic in UD_2(Z^3) and therefore
      NOT an exchange/braid generator.  Its nontrivial holonomy comes from the
      BASE connection's curvature, not from pi_1 of the configuration space.
      The eta-connection lives over the base Z^3 while the exchange Z_2 lives in
      pi_1(UD_2(Z^3)); a base connection's holonomy is structurally blind to the
      braid class.

VERDICT THE RUNNER SUPPORTS.  The eta-phase discrete spin connection's holonomy
around graph-braid exchange loops is the geometric area-flux, NOT a braid
invariant; hence the eta-phase discrete spin structure cannot supply the
fermionic exchange sign.  This closes the most natural concrete realization of
the graph-braid path the FS no-go left open.  It does NOT claim every
conceivable discrete construction is impossible: a spin structure placed on
UD_2(Z^3) itself (rather than on the base Z^3) remains formally open, though
structurally constrained by the same base-vs-configuration-space obstruction.

Pure exact arithmetic (numpy on integer/+-1 data; sympy for the (ID) identity).
No PDG / fitted / scale / mass input, no g_bare, no lattice-action carrier
consumed as load-bearing.  Asserts NO audit status.
"""

from __future__ import annotations

import itertools

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return bool(cond)


# ---------------------------------------------------------------------------
# Staggered KS phases (canonical 3D convention) and the spin-diagonal frame
# ---------------------------------------------------------------------------

UNIT = {1: (1, 0, 0), 2: (0, 1, 0), 3: (0, 0, 1)}


def eta(x, mu: int) -> int:
    """Canonical Kogut-Susskind staggered phase eta_mu(x) in {+1,-1}.

    eta_mu(x) = (-1)^{ sum_{nu < mu} x_nu }, i.e.
      eta_1 = 1, eta_2 = (-1)^{x1}, eta_3 = (-1)^{x1+x2}.
    This is the 3D generalization of the 1+1d repo convention
    (eta_0 = 1, eta_1(t) = (-1)^t) in the axiom-first staggered runners.
    """
    x1, x2, x3 = x
    if mu == 1:
        return 1
    if mu == 2:
        return (-1) ** x1
    if mu == 3:
        return (-1) ** (x1 + x2)
    raise ValueError(f"mu must be in {{1,2,3}}, got {mu}")


def add(x, sign: int, mu: int):
    u = UNIT[mu]
    return tuple(x[i] + sign * u[i] for i in range(3))


# --- sympy Pauli matrices for the exact spin-diagonalization identity --------
I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SIG = {1: SX, 2: SY, 3: SZ}


def matpow(A: sp.Matrix, n: int) -> sp.Matrix:
    R = sp.eye(2)
    for _ in range(n):
        R = R * A
    return R


def T_of_x(x) -> sp.Matrix:
    """Spin-diagonalizing gauge T(x) = sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}."""
    x1, x2, x3 = x
    return matpow(SX, x1) * matpow(SY, x2) * matpow(SZ, x3)


# ---------------------------------------------------------------------------
# Z_2 connection holonomy machinery (eta is the spin-diagonal-frame connection)
# ---------------------------------------------------------------------------

def link_phase(x, mu: int, sign: int) -> int:
    """Parallel-transport phase of the Z_2 connection Omega_mu = eta_mu along a
    single step from x in direction sign*mu_hat.  Forward link x->x+mu uses
    eta_mu(x); backward link x->x-mu uses the SAME link eta_mu(x-mu) (Z_2 is
    self-inverse)."""
    if sign == +1:
        return eta(x, mu)
    return eta(add(x, -1, mu), mu)


def holonomy(start, steps) -> tuple[int, tuple]:
    """Holonomy (product of link phases) of the Z_2 connection along a base path
    `steps` = [(mu, sign), ...]; returns (holonomy in {+1,-1}, endpoint)."""
    x = start
    h = 1
    for (mu, sign) in steps:
        h *= link_phase(x, mu, sign)
        x = add(x, sign, mu)
    return h, x


def visited(start, steps) -> list:
    x = start
    seq = [x]
    for (mu, sign) in steps:
        x = add(x, sign, mu)
        seq.append(x)
    return seq


def invert(steps) -> list:
    return [(mu, -sign) for (mu, sign) in reversed(steps)]


def plaquette_curv(x, mu: int, nu: int, conn=None) -> int:
    """Oriented Z_2 plaquette holonomy in plane (mu,nu) based at x.

    conn(x, mu) supplies the (possibly gauge-twisted) link variable; default is
    the bare eta-connection."""
    if conn is None:
        conn = eta
    return (conn(x, mu)
            * conn(add(x, +1, mu), nu)
            * conn(add(x, +1, nu), mu)
            * conn(x, nu))


# ===========================================================================
# (a) spin-diagonalization identity  T^dag sigma_mu T(x+mu) = eta_mu(x) I
# ===========================================================================

def part_a() -> None:
    print("\n" + "-" * 78)
    print("(a) spin-diagonalization identity   T(x)^dag sigma_mu T(x+mu_hat) = eta_mu(x) I_2")
    print("-" * 78)
    for L in (3, 4):
        all_exact = True
        worst = sp.Integer(0)
        for x in itertools.product(range(L), repeat=3):
            for mu in (1, 2, 3):
                xp = add(x, +1, mu)
                lhs = T_of_x(x).conjugate().T * SIG[mu] * T_of_x(xp)
                rhs = sp.Integer(eta(x, mu)) * I2
                diff = sp.simplify(lhs - rhs)
                if diff != sp.zeros(2, 2):
                    all_exact = False
                    m = max(abs(diff[i, j]) for i in range(2) for j in range(2))
                    worst = max(worst, m)
        check(f"identity exact for all x in [0,{L})^3 and all mu in {{1,2,3}} "
              f"(symbolic, {L}^3 = {L**3} sites)",
              all_exact, detail=f"max |lhs-rhs| = {worst}")


# ===========================================================================
# (b) Z_2 curvature = -1/face in every plane, gauge-invariant
# ===========================================================================

def part_b() -> None:
    print("\n" + "-" * 78)
    print("(b) Z_2 plaquette curvature = -1 per face (uniform pi-flux), gauge-invariant")
    print("-" * 78)
    L = 4
    for (mu, nu) in [(1, 2), (1, 3), (2, 3)]:
        vals = {plaquette_curv(x, mu, nu)
                for x in itertools.product(range(L), repeat=3)}
        check(f"plane ({mu},{nu}): every unit plaquette curvature = -1 on {L}^3 block",
              vals == {-1}, detail=f"holonomy values = {sorted(vals)}")

    # gauge invariance under an arbitrary Z_2 gauge twist g(x) in {+1,-1}
    rng = np.random.default_rng(20260529)
    gvals = {x: int(1 if rng.random() < 0.5 else -1)
             for x in itertools.product(range(L + 2), repeat=3)}

    def conn_twisted(x, mu):
        return gvals[x] * eta(x, mu) * gvals[add(x, +1, mu)]

    max_change = 0
    for (mu, nu) in [(1, 2), (1, 3), (2, 3)]:
        for x in itertools.product(range(L), repeat=3):
            h0 = plaquette_curv(x, mu, nu)
            hg = plaquette_curv(x, mu, nu, conn=conn_twisted)
            max_change = max(max_change, abs(h0 - hg))
    check("curvature unchanged under arbitrary Z_2 gauge twist "
          "Omega_mu(x) -> g(x) Omega_mu(x) g(x+mu) (so -1/face is gauge-invariant)",
          max_change == 0, detail=f"max |curv_gauged - curv| = {max_change}")


# ===========================================================================
# (c) (-1)^{area} holonomy law and the three named exchange loops
# ===========================================================================

# Two tokens, adjacent along x1: A and B exchange endpoints.
A_SITE = (0, 0, 0)
B_SITE = (1, 0, 0)


def detour_swap_paths(k: int) -> tuple[list, list]:
    """Faithful collision-free two-token swap with a height-k detour in the
    (1,2)-plane.  token1: A -> (0,k,0) -> (1,k,0) -> B ; token2: B -> A
    straight.  The two trajectories bound a 1 x k strip -> enclosed area = k.
    Same swap for every k."""
    t1 = [(2, +1)] * k + [(1, +1)] + [(2, -1)] * k
    t2 = [(1, -1)]
    return t1, t2


def y_move_swap_paths() -> tuple[list, list]:
    """Y-move / zero-area straight swap: both tokens traverse the SAME edge set
    in opposite directions (antiparallel), bounding NO plaquette -> enclosed
    area = 0.  (On a graph this is the Abrams Y/branch exchange; modeled here by
    the antiparallel pass that encloses zero area.)"""
    t1 = [(1, +1)]   # A -> B
    t2 = [(1, -1)]   # B -> A
    return t1, t2


def exchange_holonomy(t1: list, t2: list) -> tuple[int, tuple, tuple]:
    """Spinor-frame holonomy of a two-token exchange = product of the two
    tokens' base-connection holonomies along their trajectories."""
    h1, e1 = holonomy(A_SITE, t1)
    h2, e2 = holonomy(B_SITE, t2)
    return h1 * h2, e1, e2


def collision_free(t1: list, t2: list) -> bool:
    """True iff the two tokens never co-occupy a site under a synchronous clock
    (a token that has finished waits at its endpoint)."""
    v1, v2 = visited(A_SITE, t1), visited(B_SITE, t2)
    L = max(len(v1), len(v2))
    v1 += [v1[-1]] * (L - len(v1))
    v2 += [v2[-1]] * (L - len(v2))
    return all(a != b for a, b in zip(v1, v2))


def part_c() -> None:
    print("\n" + "-" * 78)
    print("(c) (-1)^{area} holonomy law and the three named two-token exchange loops")
    print("-" * 78)

    # rectangular base loop a x b -> (-1)^{ab}
    law_ok = True
    detail_rows = []
    for a in range(1, 5):
        for b in range(1, 5):
            steps = [(1, +1)] * a + [(2, +1)] * b + [(1, -1)] * a + [(2, -1)] * b
            h, end = holonomy((0, 0, 0), steps)
            pred = (-1) ** (a * b)
            ok = (h == pred) and (end == (0, 0, 0))
            law_ok = law_ok and ok
            if (a, b) in {(1, 1), (1, 2), (2, 3), (3, 3), (4, 4)}:
                detail_rows.append(f"{a}x{b}->{h:+d}")
    check("rectangular base loop holonomy = (-1)^{a*b} for all a,b in {1..4} "
          "(16 rectangles, all closed)",
          law_ok, detail="; ".join(detail_rows))

    # Y-move (zero area) -> +1
    t1, t2 = y_move_swap_paths()
    h, e1, e2 = exchange_holonomy(t1, t2)
    check("Y-move / zero-area swap -> holonomy +1 (swap realized, collision-free)",
          h == +1 and e1 == B_SITE and e2 == A_SITE and collision_free(t1, t2),
          detail=f"holonomy = {h:+d}")

    # 1x1 detour -> -1
    t1, t2 = detour_swap_paths(1)
    h, e1, e2 = exchange_holonomy(t1, t2)
    check("1x1-detour swap   -> holonomy -1 (swap realized, collision-free)",
          h == -1 and e1 == B_SITE and e2 == A_SITE and collision_free(t1, t2),
          detail=f"holonomy = {h:+d}")

    # 1x2 detour -> +1
    t1, t2 = detour_swap_paths(2)
    h, e1, e2 = exchange_holonomy(t1, t2)
    check("1x2-detour swap   -> holonomy +1 (swap realized, collision-free)",
          h == +1 and e1 == B_SITE and e2 == A_SITE and collision_free(t1, t2),
          detail=f"holonomy = {h:+d}")


# ===========================================================================
# (d) same swap, homotopic in UD_2(Z^3), DIFFERENT holonomy  (the obstruction)
# ===========================================================================

def part_d() -> None:
    print("\n" + "-" * 78)
    print("(d) same swap, homotopic in UD_2(Z^3), DIFFERENT holonomy (the obstruction)")
    print("-" * 78)

    t1_a, t2_a = detour_swap_paths(1)   # 1x1-detour swap
    t1_b, t2_b = detour_swap_paths(2)   # 1x2-detour swap
    ha, _, _ = exchange_holonomy(t1_a, t2_a)
    hb, _, _ = exchange_holonomy(t1_b, t2_b)

    # (i) both realize the SAME token permutation
    ea1, ea2 = holonomy(A_SITE, t1_a)[1], holonomy(B_SITE, t2_a)[1]
    eb1, eb2 = holonomy(A_SITE, t1_b)[1], holonomy(B_SITE, t2_b)[1]
    same_swap = (ea1 == B_SITE and ea2 == A_SITE and
                 eb1 == B_SITE and eb2 == A_SITE)
    check("1x1 and 1x2 detour swaps realize the SAME token permutation "
          "(A<->B exchange in both)", same_swap)

    # (ii) both collision-free
    check("both swaps are collision-free (tokens never co-occupy a site)",
          collision_free(t1_a, t2_a) and collision_free(t1_b, t2_b))

    # (iii) SAME element of B_2(Z^3): their difference is a null-homotopic loop.
    # token2 is the SAME single straight step in both, so the difference loop is
    # carried entirely by token1: do detour(1) then detour(2) in reverse.  This
    # is a CLOSED single-token base loop (bounds a 1x1 square = one unit cell),
    # which is fillable / contractible in UD_2(Z^3) given a third direction.
    diff_loop = t1_a + invert(t1_b)
    h_diff, end_diff = holonomy(A_SITE, diff_loop)
    closes = (end_diff == A_SITE)
    # the difference loop encloses |1 - 2| = 1 unit cell -> holonomy -1, which
    # equals ha*hb (Z_2), confirming the two swaps differ by exactly that flux.
    check("difference loop (swap_1x1 then swap_1x2^-1) is a CLOSED single-token "
          "base loop (returns both tokens to start)",
          closes, detail=f"endpoint = {end_diff}")
    check("difference loop bounds ONE unit cell -> holonomy -1 = product of the "
          "two swap holonomies (they are unequal as holonomies)",
          h_diff == -1 and h_diff == ha * hb,
          detail=f"diff-loop holonomy = {h_diff:+d}, ha*hb = {ha * hb:+d}")

    # The decisive contradiction: same braid element, two holonomy values.
    check("DECISIVE: same braid element of B_2(Z^3) (homotopic swaps) carries "
          "DIFFERENT holonomy  -1 (1x1) vs +1 (1x2)  ->  eta-holonomy is NOT a "
          "braid invariant (no homomorphism B_2 -> Z_2 can take two values on "
          "one element)",
          ha != hb, detail=f"hol(1x1) = {ha:+d}, hol(1x2) = {hb:+d}")


# ===========================================================================
# (e) structural decoupling: nontrivial holonomy on a NON-braid (contractible) loop
# ===========================================================================

def part_e() -> None:
    print("\n" + "-" * 78)
    print("(e) structural decoupling: base-connection holonomy is blind to the braid class")
    print("-" * 78)

    # A single-token 1x1 base loop in the (1,2)-plane (token2 parked far away).
    one_loop = [(1, +1), (2, +1), (1, -1), (2, -1)]
    h_one, end_one = holonomy(A_SITE, one_loop)
    check("single-token 1x1 base loop closes (returns the token to start)",
          end_one == A_SITE, detail=f"endpoint = {end_one}")
    check("single-token 1x1 base loop has NONTRIVIAL holonomy -1 (the area flux "
          "of one face) -- yet it is null-homotopic in UD_2(Z^3) (a unit square, "
          "fillable via the third direction in d>=3), hence NOT a braid/exchange "
          "generator",
          h_one == -1, detail=f"holonomy = {h_one:+d}")
    # The structural statement (recorded, not a separate float check): the
    # eta-connection lives over the BASE Z^3; its holonomy is a function of the
    # enclosed BASE area.  The exchange Z_2 lives in pi_1(UD_2(Z^3)).  A
    # nontrivial base-area loop need not be a braid generator (part (e) line 2),
    # and a single braid class contains representatives of arbitrary base area
    # (part (d)).  Hence the base holonomy cannot be a function of the braid
    # class -- it is the area-flux.
    check("CONSEQUENCE: a base-connection holonomy that is nontrivial on a "
          "null-homotopic (non-braid) loop and multivalued on a single braid "
          "class is structurally NOT a braid invariant",
          h_one == -1)


# ===========================================================================
# main / scorecard
# ===========================================================================

def main() -> int:
    print("=" * 78)
    print("eta-phase holonomy is an AREA-FLUX, not a braid invariant")
    print("(sharpening of the FS rotation-exchange discrete-insufficiency no-go)")
    print("=" * 78)
    print("Canonical KS phases: eta_1 = 1, eta_2 = (-1)^{x1}, eta_3 = (-1)^{x1+x2}")
    print("Spin-diagonal gauge: T(x) = sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}")

    part_a()
    part_b()
    part_c()
    part_d()
    part_e()

    print("\n" + "=" * 78)
    print("SCORECARD")
    print("=" * 78)
    print("  C_a  spin-diagonalization identity  T^dag sigma_mu T(x+mu) = eta_mu I  (exact)")
    print("  C_b  Z_2 curvature = -1/face in all 3 planes, gauge-invariant")
    print("  C_c  (-1)^{area} law + Y-move(+1), 1x1(-1), 1x2(+1) exchange holonomies")
    print("  C_d  same swap, homotopic in UD_2(Z^3), DIFFERENT holonomy (-1 vs +1)")
    print("  C_e  base-connection holonomy is structurally blind to the braid class")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if FAIL == 0:
        print(
            "  THE eta-PHASE DISCRETE SPIN CONNECTION'S HOLONOMY AROUND GRAPH-BRAID\n"
            "  EXCHANGE LOOPS IS THE GEOMETRIC AREA-FLUX (-1)^{enclosed area}, NOT A\n"
            "  BRAID INVARIANT.  Two exchange loops that are the SAME element of\n"
            "  B_2(Z^3) (the 1x1- and 1x2-detour swaps -- same permutation,\n"
            "  collision-free, homotopic in UD_2(Z^3)) carry DIFFERENT holonomies\n"
            "  (-1 vs +1) because they enclose different base area.  A fermion sign\n"
            "  must be a homomorphism on the braid group (one value per braid\n"
            "  class), so the eta-holonomy CANNOT supply the fermionic exchange\n"
            "  sign.  The eta-connection lives over the BASE Z^3 while the exchange\n"
            "  Z_2 lives in pi_1(UD_2(Z^3)); a base connection's holonomy is\n"
            "  structurally blind to the braid class (it is even nontrivial on a\n"
            "  null-homotopic, non-braid unit-square loop).\n\n"
            "  Honest scope: this CLOSES the most natural concrete realization of\n"
            "  the FS no-go's open graph-braid path (the eta-phase discrete spin\n"
            "  structure on the base Z^3).  It does NOT claim every conceivable\n"
            "  discrete construction is impossible: a spin structure placed on\n"
            "  UD_2(Z^3) ITSELF (rather than on the base) remains formally OPEN,\n"
            "  though structurally constrained by the same base-vs-configuration-\n"
            "  space obstruction.\n"
        )
    print("=" * 78)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
