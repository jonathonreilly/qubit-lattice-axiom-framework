# Anomaly-Forces-Time admission (iii) routing correction

**Date:** 2026-05-17

**Claim type:** meta
**Status:** audit-prep routing correction; not a new science claim. Records the
re-routing of `ANOMALY_FORCES_TIME_THEOREM.md`'s admission (iii) from
`CPT_EXACT_NOTE.md` (incorrect — does not establish chirality) to
`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
(correct — derives `{epsilon, D_staggered} = 0`).

**Status authority:** independent audit lane only. This note does not set or
predict an audit outcome.

## The bug being corrected

Per the hostile audit findings ([PR #1262](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262), finding F-C),
`docs/CPT_EXACT_NOTE.md` contains **zero occurrences** of `gamma_5` /
`gamma5` / `γ_5` / `γ5`. The file establishes `epsilon(x)` only in its
charge-conjugation role (`C H C = -H` spectral flip). The parent theorem
`ANOMALY_FORCES_TIME_THEOREM.md` was citing this file as the source for
its chirality-grading premise (admission iii) — at lines 36, 104, 139,
241, 242, 325 of the pre-correction state.

The framework actually has the chirality grading derivation, just in a
different file:
`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
Step 4 derives `{epsilon, D_staggered} = 0` from site-chirality
assignment plus retained no-rooting irreducibility. That IS the chirality
grading premise admission (iii) needs.

The bug is a **citation-routing error**, not a science gap.

## Why `epsilon(x)` plays two roles

The same sublattice parity function `epsilon(x) := (-1)^{x_1+x_2+x_3}`
on Z^3 plays two algebraically orthogonal roles in the framework:

1. **Chirality grading** (`{epsilon, D_staggered} = 0`) — needed for ABJ
   anomaly trace evaluation. Established by
   `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`.

2. **Charge conjugation** (`C H C = -H` where `C := epsilon`) —
   establishes CPT exactness. Established by `CPT_EXACT_NOTE.md`.

These do not collide because they act on different operator structures
(chirality anticommutes with `D_staggered`; charge conjugation flips
its sign on `H`). Both roles use the same site-function but the
operator-algebra relations are distinct.

## Why per-site `gamma_5` is not the chirality

Per `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`, the Cl(3)
algebra on R^3 has its volume element `omega = sigma_1 sigma_2 sigma_3`
in the **center** (not anti-commuting with the generators) — odd-dim
Clifford has no internal `gamma_5`. So the chirality grading **cannot**
live in the per-site Cl(3) algebra; it must live on the staggered
lattice / taste-reconstructed Dirac. The Kawamoto-Smit substep 2
derivation establishes exactly that staggered-lattice chirality.

The sister theorem
`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10`
explicitly disclaims any identification of the Clifford volume element
with the staggered `epsilon(x)` realization — consistent with the
correct routing established here.

## Edits applied to the parent theorem

`docs/ANOMALY_FORCES_TIME_THEOREM.md` (6 sites):

1. Admission (iii) description (line ~34) — corrected description +
   citation
2. Step 5 of admission summary (line ~85) — separated admission (ii)
   from admission (iii); explained the re-routing
3. Theorem statement body (line ~103) — corrected citation, noted
   orthogonal roles
4. `admission_routing_status` YAML block (line ~136) — `routed_to`
   target + `routing_history` block with prior routing + correction date
5. Remark on chirality mechanisms (line ~268) — corrected explanation
   pointing to staggered lattice as the chirality home, not per-site
   Cl(3)
6. Proof chain diagram (line ~362) — replaced the CPT_EXACT_NOTE arrow
   with the Kawamoto-Smit arrow + a `NO_PER_SITE_CHIRALITY` reference

Plus the new "Citation correction 2026-05-17" paragraph in the bounded
theorem submission justification.

## What this PR does NOT establish

- A new positive theorem
- A change in audit verdict for the parent theorem
- Closure of admission (i) (the ABJ-to-inconsistency bare admission)
- A claim that the parent theorem's bounded status changes; only the
  citation target for premise (iii) changes

The bounded_theorem submission status, the load-bearing class B, and
the conditioning on independent audit ratification all remain
unchanged. This is a citation-correctness fix.

## Verification

`scripts/frontier_anomaly_forces_time_admission_iii_routing_correction.py`
programmatically checks:

- `CPT_EXACT_NOTE.md` contains zero `gamma_5` occurrences (the original
  F-C finding remains true)
- `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
  derives `{epsilon, D_staggered} = 0` (the correct chirality routing)
- `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md` rules out per-site
  `gamma_5` (consistency with the staggered-lattice chirality)
- The parent theorem no longer cites CPT_EXACT_NOTE as the chirality
  source (corrected)

## Cross-references (non-load-bearing)

- `docs/ANOMALY_FORCES_TIME_THEOREM.md` (parent theorem, modified)
- `docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md` (new routing target)
- `docs/CPT_EXACT_NOTE.md` (prior incorrect routing target; retains its
  charge-conjugation role)
- `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md` (why chirality
  cannot live in per-site Cl(3))
- `docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md` (sister theorem, disclaims the identification)
- [PR #1262](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1262) (original F-A/F-B/F-C/F-E hostile audit findings)
