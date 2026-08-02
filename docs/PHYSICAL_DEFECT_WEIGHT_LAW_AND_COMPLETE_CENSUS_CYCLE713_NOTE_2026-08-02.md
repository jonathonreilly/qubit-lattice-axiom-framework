# Physical Assembly-Defect Weight Law and the Complete Census — Cycle 713

**Claim type: bounded_theorem.** Finite, recomputed statements about the landed
Cycle-696 open-coframe endpoint compiler chain at box sizes L ∈ {3, 4, 5, 6, 7,
8, 9}. The magnitude law, its support-signature resolution, the closed-form
census polynomials, and the codimension grading are exact finite statements
verified by complete scan over all 18 mixed frames; the identification of the
compiler chain with the static spatial sector is inherited, not re-derived here.

## What Cycles 711 and 712 left open

The Cycle-711 exact stencil swap law (stem
`PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02`,
in flight) derived the mixed-frame comparator −4 exactly and recorded its
per-sign census as measured, not derived. The Cycle-712 family law (stem
`PHYSICAL_MIXED_FRAME_DEFECT_CENSUS_FAMILY_LAW_CYCLE712_NOTE_2026-08-02`, in
flight) derived those counts from a positional box-descriptor mechanism, but
took the four magnitudes {2, 2·√2, 2·√3, 4} themselves as a measured menu, and
counted only the entries above the supplied cut 2.0e+00 — the sub-cut
population was never classified at all.

This cycle derives the menu, classifies every remaining entry, and gives the
census in closed form. The magnitude of a defect entry is a function of the two
edge classes it connects, and of nothing else: it factorizes over the two
coframe legs. All statements below are computational identities of the landed
compiler chain, recomputed in this cycle's runner.

## Setup

The compiler chain is the landed Cycle-696 static-sector assembler: path-simplex
templates on the open box, spatial edge classes, and the assembled static
Hessian Q, with tick multiplier LT = 2 and central finite-difference step
1.0e-04 as supplied compiler constants. Each coframe variable i carries a
spatial direction vector v_i fixed by its edge class, with **support**
s_i = |v_i|² ∈ {1, 2, 3}: support 1 for the three axis classes, 2 for the six
face-diagonal classes, 3 for the body-diagonal class. Frames are the 24 proper
cubic rotations of the landed Cycle-576 table; the transport permutation Π_g is
the bounding-box dof relabeling of Cycle 710, and the assembly defect is
E_g = Π_g^T Q Π_g − Q. The six constant-sign frames (the sextet) have defect
ceiling below 1.0e-09 and are exact zeros; the census lives on the 18 mixed
frames.

## Theorem I — the weight law

For every mixed frame and every box size in the scan, **every** nonzero entry of
the assembly defect satisfies

> |E_ij| = w · LT · |v_i| · |v_j| = w · LT · √(s_i s_j),  w ∈ {1, 1/2},

matched within 2.0e-07, with worst deviation 6.1e-08 over all 2418192 nonzero
entries scanned, and **zero** entries left unclassified. Two facts sharpen it:

- **Half weight is axis-locked.** The realized signature set of the w = 1/2
  population is exactly {(1, 1)} — half weight occurs on axis-by-axis pairs and
  nowhere else. Its magnitude is therefore always 1.0e+00.
- **Three signatures are never realized.** The w = 1 population realizes exactly
  the signatures (1,1), (1,2), (2,1), (1,3), (3,1), (2,2); the signatures
  (2,3), (3,2), (3,3) carry no defect entry at any frame or size.

Consequently the magnitude is determined by the support signature alone, and the
Cycle-712 menu is the list of values LT·√(s_i s_j) that the realized signatures
produce: (1,1) → 2, (1,2) and (2,1) → 2·√2, (1,3) and (3,1) → 2·√3, (2,2) → 4,
plus the half-weight value 1 that the Cycle-712 cut had removed. The cut 2.0e+00
is exactly the full/half separator: the largest half-weight magnitude is
1.0e+00 and the smallest full-weight magnitude is 2.0e+00, so the entries above
the Cycle-712 cut coincide with the full-weight entries at every frame and size.

The law is not a fit to a plausible-looking form. The additive alternative
LT·√(s_i + s_j) — which agrees at signature (2,2), where both read 4 — misses by
at least 0.54 wherever the two differ. Swapping the axis and body-diagonal
support assignments leaves 1656 entries outside the law at a single frame and
size. A site-graded diagonal ramp on Q, which the relabeling does not commute
with, leaves 272 entries outside it. A uniform diagonal shift, by contrast,
leaves the defect exactly unchanged — the relabeling is a permutation, so a
multiple of the identity cancels between the two terms of E_g.

## Theorem II — the complete census in closed form

Per mixed frame, and identically for all 18 of them, the counts are exact
polynomials in the box size:

| population | per sign | L = 3 … 9 |
|---|---|---|
| full weight | 48(L−1)³ + 8(L−1)² + 4(L−1) | 424, 1380, 3216, 6220, 10680, 16884, 25120 |
| half weight | 16(L−1)² | 64, 144, 256, 400, 576, 784, 1024 |
| all nonzeros (both signs) | 96(L−1)³ + 48(L−1)² + 8(L−1) | 976, 3048, 6944, 13240, 22512, 35336, 52288 |

Plus and minus counts are equal for both weights at every size and frame. The
magnitude-resolved census follows from Theorem I, one polynomial per magnitude,
per sign:

| magnitude | signature | per sign |
|---|---|---|
| 4 | (2,2) | 8(L−1)³ |
| 2·√3 | (1,3), (3,1) | 8(L−1)³ |
| 2·√2 | (1,2), (2,1) | 12(L−1)³ + 16(L−1)² |
| 2 | (1,1), w = 1 | 20(L−1)³ − 8(L−1)² + 4(L−1) |
| 1 | (1,1), w = 1/2 | 16(L−1)² |

The four full-weight rows partition the full-weight population, and their
cubic coefficients 8 + 8 + 12 + 20 = 48, quadratic coefficients 16 − 8 = 8, and
linear coefficient 4 reassemble the full-weight polynomial exactly.

The laws were fitted on L ∈ {3, 4, 5, 6} and then tested against L = 7, 8 and 9.
A cubic interpolated through the four fitting sizes predicts the full-weight
count and the nonzero count at all three held-out sizes with no residual;
L = 8 and L = 9 were measured by no earlier cycle. Independently, the
polynomials reproduce the landed Cycle-711 per-sign census totals 424 at L = 3
and 10680 at L = 7, and — after the two magnitudes 2·√2 and 2·√3 are merged, as
the Cycle-711 rounded buckets merge them — its bucket composition as well.

## Theorem III — codimension grading and the carrier

The three polynomial degrees are the three codimensions of the box. The leading
term is a bulk density: **96 nonzero defect entries per unit cell per mixed
frame**, 48 per sign, independent of L. The quadratic term 48(L−1)² is a surface
population and the linear term 8(L−1) an edge population; in the Cycle-712
box-descriptor language the degree is 3 minus the number of pinned axes, so the
wall family sits at degree 2 and the edge family at degree 1.

The carrier is small and frame-independent: exactly **30 ordered edge-class
pairs** carry full-weight entries, at every frame and every size, partitioned by
support signature as 8 pairs of type (1,1), 7 each of types (1,2) and (2,1), 2
each of types (1,3) and (3,1), and 4 of type (2,2). Seven spatial classes admit
49 ordered pairs; 19 of them never carry a defect entry.

The bulk-extensivity statement has a direct consequence for the transport
question. A re-anchoring of the transport at the box boundary can move at most
the surface and edge populations, 48(L−1)² + 8(L−1) entries per frame. The
bulk term 96(L−1)³ is untouched by any boundary convention, so the assembly
defect is not a boundary artifact of the open box at any size.

## Boundary — what this cycle does not establish

- **The weight bit is measured, not derived.** Theorem I says that w ∈ {1, 1/2}
  and that w = 1/2 occurs exactly on axis-by-axis pairs. It does not derive
  *why* the axis-by-axis population splits into a full and a half branch while
  every other signature carries only the full branch.
- **The three absent signatures are a fact, not yet a mechanism.** That (2,3),
  (3,2) and (3,3) never appear is a complete-scan statement over the sizes and
  frames listed; the incidence reason is not given here.
- **Signs are not classified.** The census is sign-balanced, and the magnitudes
  are fully determined, but which entry carries which sign is left to the
  Cycle-711 swap law and the Cycle-712 descriptor.
- **Finite scan, not induction.** The polynomials are verified at seven sizes,
  three of them held out from the fit. That is strong evidence and a clean
  extrapolation, not a proof for all L.
- **This is the static spatial sector.** No dynamical or interacting statement
  is made, and no claim about the wrapped stencil, which the Cycle-696 header
  places outside the executed path.

## The next paths opened

- **Derive the weight bit.** The half branch is exactly the axis-by-axis
  signature and exactly the 16(L−1)² surface population — the same quadratic
  that carries the Cycle-712 wall family. Testing whether the half branch *is*
  the wall family, entry for entry, is a sharp finite question and would turn
  the weight bit into a positional statement.
- **Derive the three absent signatures.** The face-diagonal-by-body-diagonal and
  body-diagonal-by-body-diagonal pairs would carry magnitudes 2·√6 and 6. Their
  absence is an incidence cancellation of the same kind the Cycle-711 stencil
  computation resolved for the comparator, and is the natural next target for
  that machinery.
- **Propagate the bulk density to the response floor.** The Cycle-709
  minus-branch floor (stem
  `PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02`,
  in flight) consumes the assembly defect through a solve. A defect with an
  exact bulk density and a factorized magnitude law is a much stronger input to
  a floor-scaling law than a measured count was.
- **Test the factorization against the source-side census.** The magnitude
  factorizes over the two coframe legs, so it carries no direction-pair
  correlation beyond the product of the leg lengths. Whether the same
  factorization holds for the source-side edit sets is a direct question for the
  Cycle-708 signed classification.

## Relation to the interacting cycle

This cycle stays inside the static spatial sector of the landed 3+1 module. The
frame sextet that carries the exact zeros of the weight law is the same
constant-sign sextet whose source-stabilizer role is analyzed in
[PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md);
the in-flight Cycle-708 classification (stem
`PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02`)
maps the same boundary at the signed level, and the in-flight Cycle-710
covariance-boundary census (stem
`PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_LAW_AND_COVARIANCE_BOUNDARY_CYCLE710_NOTE_2026-08-02`)
supplied the defect object this cycle now classifies completely.

## Runner

`scripts/physical_defect_weight_law_and_complete_census_cycle713_2026_08_02.py`
— class-A finite check, stdlib + numpy, self-contained against the Cycle-696
compiler chain. Gate groups: sextet exact zeros and relabeling bijectivity;
complete magnitude classification with zero unclassified entries and the
weight-law deviation ceiling; half-weight signature locking, realized full
signatures, and absent signatures; the additive-law rejector, the full/half
separator, and the coincidence of the Cycle-712 cut with the weight split; sign
balance and frame uniformity; the three census polynomials and the four
magnitude polynomials at L = 3..9; held-out cubic extrapolation to L = 7, 8, 9;
the Cycle-711 census anchors; carrier size and carrier signature partition; and
three operator-level rejectors — support shuffle, uniform-shift invariance, and
a site-graded ramp. Prints TOTAL: PASS=28 FAIL=0 with a JSON receipt in
`outputs/`.
