# Occupancy from Locked Record Outcomes: Flavor Piece (i) Bridge (Bounded Note)

**Date:** 2026-07-03
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets no audit
outcome and changes no registry row.

**Primary runner:**
[`scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py`](../scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py)

## Question

Does the generation-sector statistical measure attach to locked
record-outcomes, with one slot per locked admissible possibility, rather than
to the real-analytic mode count of the fluctuation energy?

The bridge candidate tested here is narrow:

> The generation-sector statistical measure is graded by locked
> record-outcomes, one slot per locked admissible possibility, hence one
> K/CPT orbit, not by the real-analytic mode count of the fluctuation energy.

The question is downstream of the first-order determinant construction in
[`KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md`](KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md),
the static-readout walls in
[`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md),
and the sector-versus-orbit occupancy atom in
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md).
The two live Record sentences are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), and the runner
guards them at runtime:

> "When present, a record locks exactly one admissible local possibility."

> "A readout value is determined by record content
> alone."

## Result

**T1: channel-generality for the localization.** For a family of exact real
small-matrix channels
`A_X(a,b,c) = a I + b X + c X^T`, the runner computes the determinant formulas
symbolically. With `c` independent, every determinant is harmonic in
`(Re b, Im b)` and has no `bbar` coefficient. On the K-real section
`c = conj(b)`, the mixed `b,bbar` term appears exactly:

```text
cycle:        d_b d_bbar det = -3a
two_step_path d_b d_bbar det = -2a
single_edge:  d_b d_bbar det = -a
two_edge_star d_b d_bbar det = -2a
```

The runner also includes a conjugate-contaminated negative control. If a channel
imports `bbar` before the K-real restriction, the off-line mixed curvature is
nonzero, so the localization test is not vacuous.

This closes the 2026-06-11 note's declared residual only at this bounded level:
the localization is not special to one hand-picked rotation channel inside this
reciprocal real-channel family.

**T2: two-records collision exhibit.** Under the stated reading

```text
one record = one locked admissible local possibility = one statistical slot,
```

the sector grading requires one complex locked value `b` to be read as two
independent registered data, `(Re b, Im b)`. That is a collision exhibit with
the two Record sentences above: one locked possibility is assigned two slots,
and the slot multiplicity is changed by the real-coordinate split rather than
by record content alone. The orbit grading assigns one slot to the locked
outcome and respects both sentences under the same reading.

The runner's T2 negative control shows the difference is load-bearing:
`Z_sector / Z_orbit = 2`, giving exactly `r = 1` for sector slotting and
`r = 1/2` for orbit slotting through the landed `rho` arithmetic.

The honesty boundary is sharp. T2 is not a full derivation unless the
one-record-one-slot identification is supplied. The remaining bridge is:

> one record locking one admissible local possibility is one statistical slot,
> and the relevant locked possibilities for the generation doublet are the
> K/CPT record-outcome orbits rather than the real components of the
> fluctuation coordinate.

## Boundaries

Wall 1 from the static-readout no-go is avoided by counting record-outcomes,
not by counting algebraic components:

> "Transferring an operator-symmetry onto "the energy counts `b` once" is a category slip and is **circular** (it assumes the asymmetric `(1,1)` split it claims to derive)."

This note never argues that `b` counts once because it is one complex number.
It argues only the conditional Record-side claim: if one locked admissible
possibility is one statistical slot, then the slot follows the locked outcome,
not the real-coordinate split of the fluctuation energy.

Wall 2 from the static-readout no-go is avoided by not using the native complex
structure as a selector:

> "A static complex structure that commutes with `M` and preserves every measure can **define** a holomorphic readout but provably cannot **select** it — both `(1,1)` and `(1,2)` are `J_cs`-invariant."

The runner does not invoke `J_cs` to choose the count. T1 uses the exact
independent-channel versus K-real-section distinction; T2 uses the live Record
sentences plus the explicitly named one-record-one-slot reading.

This note does not derive the generation Yukawa form, species content, the
R-eta construction, or a physical horn. It does not change audit data or any
registry entry. It does not consume PDG values, fitted numbers, or empirical
comparators.

## Residues

- The remaining supplied bridge is: one record locking one admissible local
  possibility is one statistical slot, and the relevant locked possibilities
  for the generation doublet are the K/CPT record-outcome orbits rather than
  the real components of the fluctuation coordinate.
- The R-eta atoms A1/A2 are untouched.
- The species piece is untouched.
- The audit lane owns statuses.

## Primary Runner

Run:

```bash
python3 scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py
```

Expected terminal form: `CHECK NN: PASS/FAIL -- <description>` lines followed
by the five-line summary whose final line is `TOTAL: PASS=13 FAIL=0`.
