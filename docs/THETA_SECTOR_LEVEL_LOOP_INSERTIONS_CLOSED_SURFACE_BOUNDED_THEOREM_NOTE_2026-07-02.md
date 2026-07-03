# Loop Insertions Act at Sector Level on Closed Glued Surfaces: Abelian Insertions Are Label Shifts in the Finite Enumerated Window, Nonabelian Insertions Open the Fusion Channels at Class Trace, and the Generic-Argument Gluing Sketch Is Rejected (Bounded Theorem)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (finite-window abelian enumeration theorem
plus quadrature-verified nonabelian edge identities; the two-cell assembly
is a structural consequence, stated as such).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_sector_level_loop_insertions_closed_surface_2026_07_02.py`](../scripts/theta_sector_level_loop_insertions_closed_surface_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_sector_level_loop_insertions_closed_surface_2026_07_02.txt`](../logs/runner-cache/theta_sector_level_loop_insertions_closed_surface_2026_07_02.txt)

## Question

The campaign's residual (i-b''-b) asked for the sector-level closed-surface
statement: how do loop insertions — the objects that carry the campaign's
frame-transport and path data — act on the sector decomposition that gluing
derives on closed surfaces? Question answered here for the fully glued 2D
surface, with abelian finite-window label shifts and nonabelian class-trace
edge identities, while locating the recoupling boundary honestly.

## Answer

(Runner 8/8; two spec-level expectations corrected by the computation, both
documented: the abelian loop-shift sign was pinned by an honest FAIL, and
the spec's generic-argument nonabelian gluing sketch was tested and
REJECTED — the measured coefficient is not argument-independent — with the
correct class-trace convention derived in its place.)

1. **Abelian insertions are label shifts, sector-diagonally in the
   finite enumerated window.** On the 2x2 torus dual with Wilson
   coefficients (quadrature Bessel, `beta = 0.7`, label window
   `|n| <= 6`), a charge-`q` loop around one plaquette shifts that
   plaquette's effective constraint label so the surviving assignments have
   the enclosed bare label offset by `q` from the common exterior sector
   label `n`:

   ```text
   Z_q = sum_n c_n^{V-1} c_{n+q}        (V = 4),
   ```

   verified against the finite-window constrained enumeration to 1e-13 for
   `q = 0, 1, 2`, with the wrong-fusion rejector (`q = 1` form against the
   `q = 2` enumeration) failing by a relative margin of order one, and —
   the sector-level statement — the enumeration grouped by exterior label
   matches `c_n^3 c_{n+q}` TERM BY TERM (~1e-17): the insertion acts
   diagonally in the sector sum; abelian fusion is a label shift of the
   enclosed region (runner A1-A4). Conjugation equivariance is exact: the
   `q -> -q` per-sector table maps `n -> -n` (B1).

2. **Nonabelian insertions open exactly the fusion channels (edge-level
   identities, quadrature).** With heat-kernel weights on SU(2): the
   no-insertion shared-edge gluing is character orthonormality
   (`int chi_{j1}(U) chi_{j2}(U^dag) = delta`, verified across the spin
   window), forcing label MATCHING — the landed mechanism. With a spin-1/2
   loop on the shared edge, the derived class-trace identity

   ```text
   int dU chi_{j1}(U) chi_{1/2}(U) chi_{j2}(U^dag) = N^{j2}_{1/2, j1}
   ```

   equals the exact fusion multiplicity on all tested fusion pairs (worst
   deviation 7.1e-4 at grid-norm floor 7.1e-4) and vanishes at the
   non-fusion pair `(0, 3/2)` at 2e-15 — the discriminating zero (C1).
   Assembling the two-cell insertion from these verified identities gives
   the sector-level structure: contributions are indexed by sector pairs
   `(j1, j2)` with `j2 in 1/2 x j1` only (C2; the assembled value is a
   structural consequence of the verified edge identities, not an
   independent partition-function measurement — stated as such).

3. **The recoupling boundary, located.** The dispatch spec's
   generic-argument sketch
   `int chi_{j1}(XU) chi_{1/2}(U) chi_{j2}(U^dag Y) ~ [N/d] chi_{j2}(XY)`
   was tested by the runner's C3 rejector and is FALSE as written: the
   measured coefficient varies with `(X, Y)` by order-one margins.
   Three-character gluing with generic
   arguments is intertwiner-valued — exactly the recoupling structure the
   campaign's link-star analysis identified as the 4D wall — and only the
   class-trace (closed-loop) projection is a bare fusion multiplicity. The
   sector-level statement on closed surfaces is thereby honest about its
   boundary: sector-diagonal fusion weights are exact at the class-trace
   level; generic-argument transport re-enters the recoupling account.

**Consequence for (i-b''-b).** On fully glued closed 2D surfaces the
sector-level statement is settled within this bounded surface: insertions
act within the sector decomposition — abelian ones as finite-window label
shifts (per-sector diagonality proven by enumeration), nonabelian ones by
opening the fusion channels with multiplicity weights (edge identities with
a discriminating zero). The 4D version inherits the named boundary:
generic-argument
(open-path) transport is recoupling-valued, so the closed-surface
sector-level statement in 4D must route path data through class-trace
(closed-loop) projections — consistent with the campaign's loop-insertion
path-data results.

## Source surface

**Record axiom** (approved axiom node `minimal_axioms`,
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)) —
background discipline only; record occurrence is not claimed. All
coefficients and identities are earned inline (quadrature Bessel;
finite-window constrained enumeration; S^3 Haar midpoint quadrature with
the measured grid-norm floor reported). Deterministic; no scipy, no Monte
Carlo, no external comparator, no fitted number. No unaudited note is
consumed as a premise, and no infinite-label U(1) tail bound is claimed.

## What moves

| Prior state | After this note |
|---|---|
| (i-b''-b) — open: how do loop insertions act on sectors? | settled on this closed 2D bounded surface: abelian = finite-window label shift (per-sector, by enumeration); nonabelian = class-trace fusion channels with multiplicity weights (edge identities + discriminating zero) |
| loop insertions as path data (campaign chain) | their sector action identified: diagonal with computable per-sector weights; conjugation-equivariant |
| generic-argument gluing (spec sketch) | REJECTED by measurement: intertwiner-valued — the recoupling boundary located exactly where the campaign's star analysis put it |

## What remains

```text
(i-b''-b residual): the 4D closed-surface assembly — route open-path
    (recoupling-valued) transport through class-trace projections on the
    flux-sector decomposition; the 2D finite-window mechanism and its
    boundary are now explicit.
```

## Non-claims

This note does not claim: the 4D sector-level assembly (the residual); that
the two-cell assembled value is an independently measured partition
function (it is the structural consequence of the verified edge
identities); validity of the generic-argument gluing sketch (measured
false; documented); Strong-CP closure or theta retirement; records
registering any object; any new axiom, import, primitive, or admission.

## No-Go Discipline Gate

**Gate result:** bounded scoping only. Negative content: the generic-argument
three-character gluing is not proportional to the transported character —
it is intertwiner-valued (measured, order-one coefficient
variation); sector-diagonal fusion weights exist exactly at class-trace
level.

**N1 routes:** class-trace insertions — exact (this note); abelian
enumeration — finite-window exact; generic-argument transport —
recoupling-valued (the
located boundary; not foreclosed, routed to the recoupling account); 4D
assembly — open residual. **N2:** binds nothing else; the rejection is a
convention statement about a specific integral form. **N3:** the two
spec-corrections (shift sign; rejected sketch) are documented in the
runner docstring and here; the grid-norm floor is measured and reported as
the honest tolerance base. **N4:** consumes (i-b''-b), returns the 2D
statement settled with the 4D residual named; matches the campaign's
recoupling-wall localization. **N5:** no closure rhetoric; the assembly's
status is stated precisely. **N6:** live paths: the 4D class-trace
routing; higher-spin insertions; SU(3) edge identities. **N7:** steelman —
"2D character calculus is classical": the deliverables are the finite-window
per-sector diagonality by enumeration, the discriminating-zero fusion
verification, and the measured rejection of the generic-argument form,
wired to (i-b''-b). **N8:** echo guard — never cite the generic-argument
gluing form; route open-path transport through the recoupling account;
per-sector claims require term-by-term enumeration matches, not just
totals.

## Verification

Run:

```bash
python3 scripts/theta_sector_level_loop_insertions_closed_surface_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=8 FAIL=0
```

Sections: A U(1) enumeration vs closed form (q = 0, 1, 2; wrong-fusion
rejector; per-sector term-by-term diagonality); B conjugation equivariance
(per-sector table maps n -> -n under q -> -q); C SU(2) fusion at sector
level (class-trace fusion-gluing identity with discriminating zero;
orthonormality; two-cell assembly structure; generic-argument coefficient
rejector).
