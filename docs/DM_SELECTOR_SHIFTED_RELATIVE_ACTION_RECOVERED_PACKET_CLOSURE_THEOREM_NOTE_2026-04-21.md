# DM Shifted Relative-Action Comparison on a Finite Recovered Packet

**Date:** 2026-04-21; scope corrected 2026-10-21
**Type:** bounded_theorem
**Status:** conditional numerical support; physical selector and DM closure open.
**Primary runner:** `scripts/frontier_dm_selector_shifted_relative_action_recovered_packet_closure_2026_04_21.py`

## Supplied construction

Take the supplied seed matrix `H_seed` and finite recovered bank of five matrices `H_i`. Adopt the objective

```text
S_rel(H || H_seed) = Tr(H_seed^(-1) H) - log det(H_seed^(-1) H) - 3.
```

Its positive-cone matrix identity does not derive a physical minimization rule. The upstream off-seed source uses local numerical optimization and an imposed `eta/eta_obs=1` equality. It is neither an independent yield prediction nor an exact, unique physical selector.

For comparison windows where both shifted arguments are positive definite, define

```text
A_mu(H) = H + mu I,
S_mu(H || H_seed) = Tr(A_mu(H_seed)^(-1) A_mu(H))
                   - log det(A_mu(H_seed)^(-1) A_mu(H)) - 3.
```

The shift must make the seed and every compared bank matrix positive definite. A sufficient condition is `mu > max(-lambda_min(H_seed), max_i[-lambda_min(H_i)])`. The chosen shifts and numerical implementation remain supplied inputs, not physical principles.

## Finite numerical comparison

The paired runner evaluates this objective on the five recovered lifts at its named `SHIFT_OFFSETS` and finite stress-sweep shifts. In those tested comparisons it reports:

- lift0 is the unique minimizer within the finite bank, with positive numerical gaps;
- the same index persists at the sampled stress shifts;
- lift0 is also the unique recovered-bank point on the positive side of the supplied doublet-block sign boundary `Im(K_Z3[1,2])=0`.

These are finite numerical comparisons. A dense sample does not establish all-shift persistence, a global source-space minimizer, or a physical selector. The label “same law” means that the same analytic logdet expression was adopted after shifting; it does not show that the shift or minimization prescription is forced.

## Dependencies and interpretation

The relative-action source, recovered bank, projection metrics and sign map are supplied by the cited packets below. The repaired relative-action and recovered-branch notes supply numerical source/comparison definitions, not exact selector authority. The same finite-index agreement can be useful for a later hypothesis about source selection, but it cannot close the DM flagship lane or eliminate the native A-BCC physical residual.

Open obligations include the physical generator/readout, the minimization and shift prescriptions, source-chart admissibility, point selection beyond the finite bank, and any continuum-of-shifts or exact uniqueness certificate. This note does not inherit physical closure from an empirical target-surface fit or an interval claim elsewhere.

## Recovery and verification

The older “current-package selector residue closed” and “DM flagship lane closed” claims are withdrawn. They are recoverable at Git revision `f24d17d97d372df977476e4a69674577f31af575` under this note's path.

Run `PYTHONPATH=scripts python3 scripts/frontier_dm_selector_shifted_relative_action_recovered_packet_closure_2026_04_21.py`. The revised finite numerical companion reports `PASS=10 FAIL=0`, including positivity of all compared matrices at the tested shifts. Obsolete prose-endorsement checks were removed; no failed numerical predicate was removed or relaxed. This does not certify physical selection.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [dm_leptogenesis_pmns_observable_relative_action_law_note_2026-04-16](DM_LEPTOGENESIS_PMNS_OBSERVABLE_RELATIVE_ACTION_LAW_NOTE_2026-04-16.md)
- [dm_selector_relative_action_recovered_branch_separation_support_theorem_note_2026-04-21](DM_SELECTOR_RELATIVE_ACTION_RECOVERED_BRANCH_SEPARATION_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- [dm_selector_relative_action_recovered_projection_support_theorem_note_2026-04-21](DM_SELECTOR_RELATIVE_ACTION_RECOVERED_PROJECTION_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- [dm_selector_shifted_doublet_imag_sign_support_theorem_note_2026-04-21](DM_SELECTOR_SHIFTED_DOUBLET_IMAG_SIGN_SUPPORT_THEOREM_NOTE_2026-04-21.md)
- [dm_abcc_exact_target_surface_source_cubic_closure_theorem_note_2026-04-21](DM_ABCC_EXACT_TARGET_SURFACE_SOURCE_CUBIC_CLOSURE_THEOREM_NOTE_2026-04-21.md)
