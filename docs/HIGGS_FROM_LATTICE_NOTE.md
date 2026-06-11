# Higgs From Lattice: Bounded Quantitative Support

**Date:** 2026-04-15 (originally); 2026-06-11 (audit-requested repair:
authority dependency edge wired + boundary inputs declared — see
changelog); 2026-06-11 compute repair (runner timeout removed)
**Status:** bounded quantitative support only
**Primary runner:** `scripts/frontier_higgs_mass_derived.py`

## Changelog (2026-06-11 audit-requested repair)

The 2026-06-11 conditional audit recorded `missing_dependency_edge`:
the authority boundary `HIGGS_MASS_DERIVED_NOTE.md` was referenced in
prose only (no citation-graph edge), and the support runner's
quantitative inputs (SM couplings, `y_t`, `lambda_bare`, `m_sq_bare`,
matching and particle-content choices) were silent imports. This
repair:

1. wires the authority note as an explicit one-hop markdown dependency
   below. The reversed support pointer inside
   `HIGGS_MASS_DERIVED_NOTE.md` is simultaneously demoted to a
   backticked file pointer in the same change, so the previously
   recorded cycle-0046 does not reappear — the edge now runs only in
   the canonical support-cites-authority direction;
2. declares the runner's quantitative inputs as explicit boundary
   inputs (B1–B4 below), in the house declared-boundary-input pattern.
   **None of them is claimed as derived by this note**;
3. cites the retained-tier IR-finiteness authority for the lattice CW
   momentum sums (B4).

The substantive posture of the note (bounded support, no `m_H`
authority) is unchanged.

## Compute Repair (2026-06-11)

The support runner was timing out under the audit runner inventory because
each scan point evaluated dense field grids before extracting the CW minimum.
The runner now computes the same bounded Coleman-Weinberg readout by direct
bounded scalar minimization and local curvature evaluation. This is a compute
repair only: it does not add dependencies, does not promote this support note,
and keeps the exact SM crossing as an open/bounded consistency question rather
than a closed Higgs-mass derivation.

## Authority Rule

Use [`HIGGS_MASS_DERIVED_NOTE.md`](HIGGS_MASS_DERIVED_NOTE.md) for the
current Higgs authority boundary. Its per-input authority table is the
canonical routing for the accepted `y_t(v)` route, the EW
gauge-coupling inputs, the `alpha_s(v)` input, and the vev scale; this
note does not restate those routes. This note exists only to summarize
the current bounded quantitative posture of the lattice
Coleman-Weinberg support runner.

## Declared boundary inputs (B1–B4)

The support runner `scripts/frontier_higgs_mass_derived.py` evaluates
an exploratory lattice Coleman-Weinberg potential over these declared
inputs. None of them is claimed as derived by this note; the
framework-side authority routing for the accepted values lives in the
authority note's per-input table.

- **B1 (top-Yukawa anchor).** The runner anchors
  `Y_TOP_MZ = sqrt(2) · M_T / v ≈ 0.994` from its SM reference block
  and scans the CW curve `m_H(y_t)` around it; the framework-side
  accepted route `y_t(v) = 0.9176` (with its inherited precision
  caveat) is routed via the authority note's table, not re-derived
  here. Both values enter this note only as declared scan anchors.
- **B2 (SM/PDG reference block — quarantined external comparators).**
  The runner consumes the SM anchor set
  `M_Z = 91.1876`, `M_W = 80.377`, `M_H = 125.25`, `M_T = 173.0`,
  `v = 246.22 GeV`, `ALPHA_S_MZ = 0.1179`,
  `sin²θ_W = 0.23122`, `ALPHA_EM = 1/127.951`, and the SM
  particle-content degrees of freedom (`N_W = 6`, `N_Z = 3`,
  `N_TOP = −12`, `N_HIGGS = 1`, `N_GOLDSTONE = 3`). These are
  **declared external comparator inputs** (PDG-anchored), quarantined
  to this bounded support surface: they calibrate the exploratory
  scan and the comparison axis, and no claim of this note rests on
  them beyond bounded consistency. The CW/particle-content
  identification is a declared structural choice here, not a derived
  theorem.
- **B3 (bare scalar parameters).** `lambda_bare` and `m_sq_bare` are
  scan variables of the CW potential (the runner explores the
  `m_H(y_t, lambda_bare, m_sq_bare)` response surface); they are
  inputs by construction, not derived quantities.
- **B4 (lattice CW bridge).** The lattice momentum sums use the
  standard kernel `k̂² = 2 Σ_μ (1 − cos k_μ)`; their IR-finiteness at
  `d ≥ 3` is the retained-tier threshold statement of
  [`AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_COLEMAN_MERMIN_WAGNER_THEOREM_NOTE_2026-04-29.md).
  The lattice-to-continuum matching factors are applied at the stated
  couplings; no closed-form matching derivation is provided or claimed
  in this packet.

## Safe Statement

Within the declared boundaries (B1–B4), the runner exhibits nontrivial
lattice Coleman-Weinberg behavior.

What remains true on the current package:

- the quantitative Higgs output moves materially with the accepted
  `y_t(v)` route (B1) and the comparison inputs (B2)
- the runner supports bounded consistency studies, not one exact `m_H`
  authority
- exact Higgs-mass closure therefore remains outside the retained
  flagship surface; the authority boundary is
  [`HIGGS_MASS_DERIVED_NOTE.md`](HIGGS_MASS_DERIVED_NOTE.md)

## Packaging Boundary

This note is part of the support stack for the bounded Higgs lane. It
is not a standalone promotion surface.

<!--
Cycle history: a 2026-05-06 cycle-break removed this note's back-edge
to HIGGS_MASS_DERIVED_NOTE.md while the authority note kept a markdown
link to this note (cycle-0046, docs/audit/data/cycle_inventory.json).
The 2026-06-11 audit-requested repair flips the orientation: this
support note now carries the markdown authority edge (as the audit's
missing_dependency_edge repair target requires), and the authority
note's pointer to this note is demoted to a backticked file pointer in
the same change, keeping the citation graph acyclic.
-->
