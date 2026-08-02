# Physical Mixed-Frame Assembly-Defect Census: the Family Law — Cycle 712

**Claim type: bounded_theorem.** Finite, recomputed statements about the landed
Cycle-696 open-coframe endpoint compiler chain at box sizes L ∈ {3, 4, 5, 6, 7}.
The twelve-family decomposition of the assembly defect, the box-descriptor
mechanism behind it, and the closed-form counting polynomials are exact finite
statements verified by complete scan; the wall-family and edge-family pair
magnitudes are measured, not derived.

## What Cycle 711 left open

The Cycle-711 exact stencil swap law (stem
`PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02`,
in flight) derived the mixed-frame comparator −4 exactly and recorded its
census as measured, not derived: per-frame counts 64/224/136 at L = 3 and
1728/4896/4056 at L = 7 for the rounded magnitudes 4/3/2, argmax family 128 and
3456. This cycle derives those counts. Every one of them is the value of an
explicit counting polynomial in the box size L, and the polynomial is produced
by a positional mechanism — product boxes of base sites with per-axis wall pins
and fixed-margin growing intervals — extracted at intermediate sizes and
verified by extrapolation both down to L = 3 and up to L = 7. These are
computational identities of the landed compiler chain.

## Setup

The compiler chain is the landed Cycle-696 static-sector assembler: path-simplex
templates on the open box, spatial edge classes (axis, face-diagonal,
body-diagonal), and the assembled static Hessian Q, where the tick multiplier
LT = 2 and the central finite-difference step 1.0e-04 are supplied compiler
constants. Frames are the 24 proper cubic rotations of the landed Cycle-576
table; the transport permutation Π_g is the bounding-box dof relabeling of
Cycle 710, and the assembly defect is E_g = Π_g^T Q Π_g − Q. The six
constant-sign frames (the sextet) have defect ceiling below 1.0e-09 and are
exact zeros of the law; the census lives on the 18 mixed frames. For an entry
(i, j) the defect value is the difference of the entry pair
(a, b) = (Q[m_i, m_j], Q[i, j]); the pair classifier below uses the smaller of
(|a|, |b|) with supplied cuts 0.5 and 10.

## Theorem I — the twelve-family decomposition

Over all five box sizes and all 18 mixed frames, every large defect entry
(789120 of them in the complete scan) falls into exactly one of twelve signed
families — six unsigned families times a sign — keyed by

- **exact magnitude**: |E| ∈ {2, 2·√2, 2·√3, 4}, matched within 2.0e-07
  (per-surd maxima 5.7e-08, 3.0e-08, 6.1e-08, 1.3e-08; distance to the
  second-nearest magnitude at least 5.4e-01), and
- **pair class**: *swap* (the partner side is small — a value-for-zero swap, as
  in the Cycle-711 argmax law), *wall* (both sides order one:
  5.857096565429 and 8.685523719688), or *edge* (both sides large, diagonal
  i == j on axis (NN) classes: 22.150846413069 and 24.150846469784).

There are no outliers. The per-family counts are identical across all 18 mixed
frames at every L (frame uniformity), and the plus and minus families are in
bijection (sign bijection). The six unsigned families are: (4, swap),
(2·√3, swap), (2·√2, swap), (2·√2, wall), (2, swap), (2, edge).

## Theorem II — the box-descriptor mechanism

Fix a family and a template (the class pair and site offset of its entries).
The set of base sites carrying that template is a product box, and each axis of
the box is one of exactly two kinds:

- a **wall pin** P: the coordinate is frozen at 0 or L − 1;
- a **growing interval** G(s): the coordinate ranges over a full interval with
  fixed margins, contributing a factor (L − s) with s independent of L.

The canonical form — per box the sorted multiset of axis descriptors — is
invariant across the 18 mixed frames and across box sizes. Per sign the six
families decompose into 8/8/12/16/20/4 boxes carrying 0/0/0/1/0/2 wall pins per
box respectively: the three bulk swap families are pin-free product boxes, the
wall family carries exactly one pin per box (wall-anchored plaquettes), and the
edge family carries two pins per box (box-edge lines of diagonal entries).
Descriptors are extracted at L ∈ {4, 5, 6}; L = 3 (where the interior interval
of a growing axis degenerates) and L = 7 are held out and used as genuine
extrapolation checks.

## Theorem III — the census laws

Summing the descriptor factors gives, per sign:

| family | counting law | counts at L = 3..7 |
|---|---|---|
| (4, swap) | 8(L−1)³ | 64, 216, 512, 1000, 1728 |
| (2·√3, swap) | 8(L−1)³ | 64, 216, 512, 1000, 1728 |
| (2·√2, swap) | 12(L−1)³ | 96, 324, 768, 1500, 2592 |
| (2·√2, wall) | 16(L−1)² | 64, 144, 256, 400, 576 |
| (2, swap) | 12(L−1)³ + 8(L−1)²(L−2) | 128, 468, 1152, 2300, 4032 |
| (2, edge) | 4(L−1) | 8, 12, 16, 20, 24 |

Each law is verified three ways: the measured count equals the descriptor
prediction equals the stated polynomial, at every L in {3, 4, 5, 6, 7}, and the
descriptor prediction equals the polynomial identically for L = 3..10.

**Corollaries — the Cycle-711 census derived.** Rounding mixes the two middle
surds (2·√2 and 2·√3 both round to 3), so the rounded buckets are, per sign:

- **±4**: 8(L−1)³ — 64 at L = 3, 1728 at L = 7;
- **±3**: 20(L−1)³ + 16(L−1)² — 224 at L = 3, 4896 at L = 7;
- **±2**: 12(L−1)³ + 8(L−1)²(L−2) + 4(L−1) — 136 at L = 3, 4056 at L = 7;
- **argmax family** (both signs of (4, swap)): 16(L−1)³ — 128 at L = 3, 3456
  at L = 7.

All four reproduce the Cycle-711 anchors exactly, and the bucket-composition
gate confirms the identification family-by-family.

**Finite-difference provenance of the ±2 bucket.** The magnitude-2 entries sit
at offsets in (1.7e-09, 5.7e-08] strictly above 2: the FD truncation of the
compiler chain pushes this family consistently upward, so the Cycle-711 census
cut at 2.0e+00 is deterministic, not knife-edge.

**Rejector.** Under a 1.7 diagonal perturbation of the assembled operator, 2
entries leave the exact magnitude set at distance 3.0e-01: the family law is a
property of the landed operator, not of the classifier.

## Honest boundary

- **The wall and edge pair magnitudes are measured, not derived.** The values
  5.857096565429 / 8.685523719688 (wall, spreads 8.5e-11 / 1.2e-11) and
  22.150846413069 / 24.150846469784 (edge, spreads 1.2e-10 / 0.0e+00) are
  L-independent and frame-independent to the stated spreads, but no stencil
  evaluation is given for them here. The Cycle-711 two-incidence computation
  that produced the exact −4 is the template; running it per family is the
  named next target.
- **The counting laws are finite statements.** Verified for L = 3..7 under the
  supplied compiler constants; the polynomial identity for L = 3..10 is a
  consistency identity between the descriptor form and the stated polynomial,
  not an independent measurement. No continuum statement is made.
- **The mechanism is positional, not yet stencil-resolved.** Theorem II says
  where the entries sit (bulk boxes, wall plaquettes, edge lines); it does not
  say which incidence cancellations produce each surd. That is the same gap as
  the pair magnitudes and has the same named target.

## The next paths opened

- **Per-family exact stencil evaluation.** Repeat the Cycle-711 two-incidence
  stencil computation for the wall family and the edge family: derive
  5.857096565429 / 8.685523719688 and 22.150846413069 / 24.150846469784 as
  exact surd combinations, upgrading Theorem I from measured magnitudes to
  derived ones.
- **Propagate the census to the response floor.** The Cycle-709 minus-branch
  floor (stem
  `PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02`,
  in flight) consumes the assembly defect through a solve; the family counts
  and their L-scaling are the natural input for a floor-scaling law.
- **Path-symmetrized assembly.** The wall and edge families are boundary
  populations (16(L−1)² and 4(L−1) against the 8(L−1)³ bulk); whether a
  re-anchored transport can remove the boundary families while preserving the
  bulk swap structure is a sharp, finite question.

## Relation to the interacting cycle

This cycle stays inside the static spatial sector of the landed 3+1 module. The
frame sextet that carries the exact zeros is the same constant-sign sextet
whose source-stabilizer role is analyzed in
[PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md);
the in-flight Cycle-708 classification (stem
`PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02`)
maps the same boundary at the signed level, and the in-flight Cycle-710
covariance-boundary census (stem
`PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_LAW_AND_COVARIANCE_BOUNDARY_CYCLE710_NOTE_2026-08-02`)
supplied the defect object this cycle counts.

## Runner

`scripts/physical_mixed_frame_defect_census_family_law_cycle712_2026_08_02.py`
— class-A finite check, stdlib + numpy. Gate groups: sextet exact zeros;
family-key completeness, frame uniformity, and sign bijection over the complete
scan; per-surd magnitude deviations with a wrong-surd gap; canonical
box-descriptor invariance across frames and sizes with the box-shape census;
the six counting laws at L = 3..7 with the polynomial identity at L = 3..10;
the Cycle-711 census, bucket-composition, and argmax anchors; the magnitude-2
FD window; wall and edge pair-value stability; and the perturbed-operator
rejector. Prints TOTAL: PASS=29 FAIL=0 with a JSON receipt in `outputs/`.
