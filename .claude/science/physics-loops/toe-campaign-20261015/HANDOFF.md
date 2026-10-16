# Handoff — toe-campaign-20261015

Branch `claude/toe-campaign-24h-20261015` (cut from the hygiene branch of
PR #9625). Window 2026-10-15T23:30Z – 2026-10-16T23:00Z. Nothing here is
adopted; every result is unaudited bounded support with its evidence level
stated in the note.

## Delivered blocks

| Block | Note | Runner | Headline |
|---|---|---|---|
| B1 | `docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/cubic_covariant_qubit_walk_cell_classification_2026_10_16.py` (PASS=31) | One qubit per site: no unitary tick on the 27-point cell that is covariant under the proper cubic group (any of the four soldering actions) moves. T also freezes; D4 allows axial shifts only; motion in 3D survives under C3, C4, D2 only. Independent Singular re-derivation agrees. |
| B2 | `docs/ORDER_BLIND_POSITIVE_FORMATION_IS_A_ONE_DEPENDENT_GIBBS_FIELD_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/order_blind_formation_one_dependent_record_field_2026_10_16.py` (PASS=17) | Positive order-blind formation = one consistent 1-dependent record field whose full conditionals are the rule (static = formation); no long-range order, power laws or pinch points. |
| B3 | `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md` | `scripts/two_qubit_cubic_dirac_tick_2026_10_16.py` (PASS=39) | A two-qubit site (parked M_4(C) fork) admits exactly O-covariant moving ticks; Clifford family classified by a Gram criterion; explicit member with one massless isotropic Dirac cone and gapped doublers; speed <= 1 with axis doublers at 2 arcsin s; unique light-speed member over Q(sqrt 5); exact chirality freezes motion; W3 = 0; quadratic (not linear) anisotropy. Independent check agrees (and corrected one statement). |

## Synthesis for the TOE program (implications, not adoptions)

- **Discrete-time one-qubit matter cannot be exactly cubic covariant at cell
  range.** Options that do allow covariant motion: continuous time (unbounded
  range per unit time), breaking the cubic group to order <= 4 (which forces a
  linear handed dispersion term), or a doubled site (Dirac structure forced).
  Block B4 tests a fourth option: a 2-site cell (staggering) with one qubit per
  site.
- **Chirality wall, sharpened.** On a two-qubit site, exactly chiral covariant
  ticks are frozen; moving ones are vector-like with Wilson-type chirality
  breaking, and every member of the classified family has W3 = 0.
- **Emergent isotropy budget (B3 Theorem 7).** On the two-qubit site the
  k^4 cubic anisotropy of the Dirac cone can be cancelled exactly (plane
  b0 = b1 + 2 b2), but only for cone speed |s| <= sqrt(2/3) (sharp, attained
  over Q(sqrt6, sqrt15)), and the k^6 anisotropy -(s^2/360)|k|^2 sum k^4 is
  then unavoidable. Light speed and k^4 isotropy exclude each other.
- **Ceiling for one-qubit motion (B1 Theorems 4-5).** Exact: no subgroup of O
  of order >= 6 lets a one-qubit cell tick move in more than one direction
  (D4 axis shifts, D3 body-diagonal shifts); O stays frozen at range two.
- **Coulomb lane.** Strictly positive order-blind formation cannot produce
  Coulomb-phase correlations; hard constraints or order sensitivity are needed.

## Open obligations

- One-qubit freeze at every finite range. Exact now at range one (cell, all
  four actions) and range two per axis (O, full action; Theorem 4 by line
  branches, runner `scripts/cubic_covariant_qubit_walk_line_branch_certificates_2026_10_16.py`
  PASS=16, which also proves Theorem 5: D3 cell walks are constant or
  body-diagonal shifts; this corrected the earlier numerical 'D3: none').
  Range three is running (`scratchpad/walk/rangeR3.log`).
- Whether every two-qubit O-covariant cell walk is Clifford-form up to flavor
  gauge (all hits tested so far are).
- Irreducible 4-dimensional coin: no moving walk found (search only).
  Doubled spin-1 site: none in 16 + 12 + 12 starts (delta 0.05 / 0.2 / 0.5).

## Next decision

Read the B4 staggered results (`scratchpad/walk/stag_*.log`); if moving
staggered walks exist, characterize them as in B3 and compare with the
staggered-Dirac open gate named in the axiom memo.
