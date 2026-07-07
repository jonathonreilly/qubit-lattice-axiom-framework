# Gauge-Link Record Step: Binary Registration Capacity Pins the Native Step Kernel

**Date:** 2026-07-02
**Claim type:** bounded_theorem
**Audit status:** set only by the independent audit lane. This source note does
not set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/gauge_link_binary_registration_capacity_step_kernel_pin_2026_07_02.py`](../scripts/gauge_link_binary_registration_capacity_step_kernel_pin_2026_07_02.py)

## Purpose

This note asks a narrow per-step question:

What registration softness do the axioms support per step on the native
gauge-link carrier?

The answer is that there is no nontrivial softness below the native kernel on
this carrier. The admissibility-supported family is the two-member family
{trivial, binary}. The binary member is already saturated by the native
carrier's one-sided central content, so the per-informative-step kernel is
pinned to T_V.

The composed informative-step set is exact. It stays strictly above the unit
variance point. The rate dial therefore does not sit inside the informative
kernel itself; it relocates to the informative-step fraction p.

The row
`NATIVE_CARRIER_REGISTRATION_KERNEL_RATE_VS_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`
is named here as prose context only, not a citation-graph dependency.
The row
`GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02.md`
is named here as prose context only, not a citation-graph dependency.
The row
`GAUGE_LINK_PER_RECORD_STEP_RATE_DIAL_UNIT_VARIANCE_POINT_THEOREM_NOTE_2026-07-02.md`
is named here as prose context only, not a citation-graph dependency.

All constructions needed for this packet are re-derived here and checked by the
primary runner.

## Supplied surfaces (cited at audited scope)

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  supplies the Qubit, Admissibility, and Record premises used for the capacity
  statement.
- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  supplies the 3+1 base split used as the native carrier's central content.
- [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md)
  supplies the canonical generator normalization and the zero-sum logarithm
  branch convention used for finite-link moments.
- [`RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md`](RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md)
  supplies the finite record-step channel form.
- [`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
  supplies the respected boundary separating record tokens from supplied rates
  and stochastic dynamics.

## Theorem 1 (binary per-step capacity)

The Qubit premise says:

> "The full one-site possibility domain has algebraic presentation `M_2(C)`."

The backticked algebra token inside this quotation is not a citation-graph
dependency.

The Record premise says:

> "a record locks exactly one admissible local possibility"

The one-site possibility domain is therefore two-dimensional at full
resolution, and a record, when present, locks one available local possibility
from the Admissibility-available subset.

Two elementary lemmas fix the capacity.

First, rank counting on C^2: an orthogonal pointer partition on C^2 has at most
two nonzero cells. Three nonzero mutually orthogonal projectors would have rank
sum at least 3, which cannot fit under the identity on a two-dimensional space.

Second, pullback cell counting: if a pointer partition is pulled back through a
channel onto another carrier, the pullback has no more cells than the source
partition. The effects may change, but the indexed family is still the pulled
back indexed family.

Hence one record step supports, on any registered carrier, at most a binary
pointer partition. The per-step options are exactly:

- trivial, when no record is present or the available subset is singleton;
- binary, when the record distinguishes two admissible local possibilities.

## Theorem 2 (saturation: the per-step kernel is pinned)

The native link carrier's one-sided gauge-central content is exactly the binary
partition {P_3, P_1}, the 3+1 base split.

That binary partition saturates the axiom capacity from Theorem 1. There is no
third nonzero cell to soften into at this one-record-step resolution.

On holonomy configurations X_U = rho(U), the one-sided Kraus family
{P_3 tensor I, P_1 tensor I} acts identically to the full two-sided sector Kraus
family {P_ij}.

The one-line proof is block diagonality. Since rho(U) and rho(W) preserve the
P_3 and P_1 blocks, the two-sided amplitude with i != j vanishes, while the
i = j terms reproduce the one-sided amplitudes.

Thus the induced kernel is the same kernel:

    T_V(x) = (|chi_3(x)|^2 + 1) / 2
           = 1 + chi_8(x) / 2.

Consequently, on this carrier, "soft registration at
admissibility-supported resolution" degenerates to the two-member family:

    {delta, T_V}.

The trivial member is delta. The nontrivial member is binary. The
per-informative-step kernel is pinned.

## Theorem 3 (exact composed family and the unit point)

The spectral algebra gives:

    w_8(T_V) = 1/16 exactly.

Therefore the k-step composition has:

    w_8(k) = 16^(-k)

and its chi_8 coefficient is:

    8 / 16^k.

On the canonical zero-sum minimal branch, with the naive-principal companions
reported for comparison, the exact integral identities are:

    <chi_8 s2_naive>_Haar = 4/9
    <s2_naive>_Haar       = pi^2 - 4/9
    <chi_8 s2_min>_Haar   = 16/27
    <s2_min>_Haar         = 9.466227112

The last line is the external numeric anchor for the zero-sum minimal branch,
equivalently:

    m^2_Haar = 2.366557.

Combining the chi_8 coefficient with the exact chi_8 moment gives the closed
form:

    m^2(k) = m^2_Haar + (2/27) * 16^(1-k),    k >= 1.

In particular:

    m^2(1) = m^2_Haar + 2/27
           = 2.440631.

This reproduces the native-kernel row number from the row named in Purpose as
prose context only.

The pure informative-step composition family is therefore contained in:

    (m^2_Haar, m^2(1)] = (2.366557, 2.440631].

Every member exceeds the unit value 1 by more than a factor 2.36.

Scoped negative corollary: within this reading, this carrier, and this
registration-step family, no composition of admissibility-capacity registration
steps attains the unit-variance point.

This corollary does not close the following routes:

- deriving p from record-formation or occupancy statistics of admissible
  configurations;
- composite multi-cube carriers whose central content is richer than binary;
- alternative licensed readout families.

## Theorem 4 (the informative-fraction dial)

The full admissibility-supported per-step family is the lazy mixture:

    (1-p) delta + p T_V,

where p is the informative-step fraction: the fraction of record steps whose
available subset is non-singleton.

Per-step variance is linear:

    <s2>_p = p <s2>_T_V.

Since:

    <s2>_T_V = 9.466227 + 8/27,

the unit-variance point corresponds to exactly one interior value:

    p* = 4 / <s2>_T_V
       = 4 / (9.466227 + 8/27)
       = 0.409731.

The Admissibility surface supplies no:

> "transition probabilities or weights"

Therefore p is a registered or dynamical datum, not an axiom-supplied
constant.

Dial discipline: p* is located on the dial, not forced. It is not a
distinguished setting; in particular it is not 0, 1/2, or 1.

The final per-step rate form on the native carrier is the informative-step
fraction.

## Boundary

- This note does not claim: that a record step occurs. It does not derive that
  a record step occurs; the semigroup boundary is respected.
- This note does not claim: position-classicality between steps.
- This note does not claim: a derivation of p, or that p* is selected.
- This note does not claim: that the scoped negative corollary constrains
  alternative readout families, composite carriers, or non-registration
  dynamical components.
- This note does not claim: branch-independent moment identities. The identities
  are stated on the named zero-sum canonical branch, with naive-principal
  companions reported.
- This note does not claim: Wilson action-surface selection. The row
  `G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md` is named
  here as prose context only, not a citation-graph dependency.
- This note does not claim: a continuum limit.
- The unit-point calibration in this note is stated for the total
  step-kernel variance, the transfer-level quantity. The Record axiom now
  states that a readout value is determined by record content alone; the
  record-determined per-step share under that clause is left outside this
  note. This bullet does not create a citation-graph dependency.
- This note does not claim: an audit verdict or any effective-status promotion.

Forward surface:

- derive p from record-formation or occupancy statistics of admissible
  configurations;
- study composite multi-cube carriers whose central content is richer than
  binary, where the softness dial genuinely unfreezes;
- test alternative licensed readout families.

## Falsifiers

- Section A falsifier: a three-cell nonzero orthogonal pointer partition fits
  under I on C^2, or channel pullback increases the source cell count.
- Section B falsifier: the native carrier Casimir spectrum is not
  {4/3 x6, 0 x2}, the one-sided/two-sided collapse fails on holonomy
  configurations, or the grid identity for T_V fails.
- Section C falsifier: either exact identity misses its tolerance on the
  M = 3200 grid, the M = 3200 error is not smaller than the M = 1600 error, or
  the Weyl density mean is not 1.
- Section D falsifier: w_8(T_V) is not 1/16, the k = 2 eigenvalue-power gate
  fails, the independent Monte Carlo composition estimate misses the closed
  target, or the first six composed moments fail monotonicity or unit-margin
  gates.
- Section E falsifier: p* is not 0.409731 within tolerance, is not interior, or
  collapses to a distinguished setting 0, 1/2, or 1.

## Verification

Command:

    python3 scripts/gauge_link_binary_registration_capacity_step_kernel_pin_2026_07_02.py

Expected total:

    TOTAL: PASS=60 FAIL=0
