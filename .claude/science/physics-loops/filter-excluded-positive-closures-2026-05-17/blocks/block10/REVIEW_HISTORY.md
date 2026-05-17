# Block 10 — Review History (V1-V5)

**Target:** `alpha_s_derived_note` (parent), via narrow theorem
`ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17`.
**Date:** 2026-05-17.

## V1. Independence from block 08

**PASS.** Block 08 closed an operator-level lemma on the staggered Dirac
operator:

- S1: `D' = dD/dA|_{A=0}` is exactly degree-1 in `U` (vertex degree).
- S2: `Pi = -Tr[D^{-1} D' D^{-1} D']` has log-log slope = 2 in lambda.
- S3: `n_link(VP) = 2 * n_link(hopping)`.

These are numerical lattice-operator tests of vertex degree.

Block 10 closes a *partition-function-side* algebraic step:

- Given the retained CMT correlator identity `<O(U)> = u_0^{n_link} <O_V(V)>_eff`
  plus the standard convention split (I2), (I3), derive
  `alpha_eff = alpha_bare / u_0^{n_link}`.

Different theorem, different surface, different proof technique
(pure algebraic substitution on rational-function field vs. operator
log-log slope on staggered Dirac matrix). The `n_link = 2` value
appears in both blocks but block 10's proof is independent of `n_link`
in its body; specialization to 2 is one corollary.

## V2. A_min compliance

**PASS.** Runner uses only sympy. No PDG values. No fitted alpha_s.
No `canonical_plaquette_surface` import. No audit-data touches. No
network, no observational data, no physical constants. Pure symbolic
algebra over abstract positive-real and positive-integer symbols.

Verified in runner source: `grep -nE "import|from"`
shows only `from sympy import ...`. No other dependencies.

## V3. Honest tier

**PASS.** Source note explicitly states:

- "**Type:** positive_theorem (bounded under named admissions)"
- "**Status authority:** independent audit lane only. This source note
  does not set or predict an audit outcome."
- Four admissions named in §"Admissions":
  1. CMT correlator identity (I1) consumed from retained source
  2. Bare normalization convention (I2)
  3. Kinematic-factor equality K_U = K_V (I3)
  4. n_link as operator-level link count

The theorem is genuinely narrow and bounded. It does NOT claim to
close the parent `alpha_s_derived_note` row, which inherits at least
three additional bounded/open dependencies (plaquette analytic
insertion, running bridge, staggered Dirac gate).

## V4. Distinctness from existing narrow theorems

**PASS.** Existing narrow theorems in the chain:

- `ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md` proves
  `alpha_LM^2 = alpha_bare * alpha_s(v)` and `alpha_s(v)/alpha_LM = 1/u_0`
  from DEFINITIONS (D1), (D2). Pure substitution algebra at the level
  of final coupling symbols. **Does not derive (D1), (D2) from the
  CMT identity.**

- `ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`
  treats `n_link = 2` as an algebraic exponent definition, not a
  derivation. (Block 08 closed the operator-level derivation of this
  count.)

- `YT_VERTEX_POWER_DERIVATION.md` step 5 asserts
  `alpha_eff = alpha_bare / u_0^{n_link}` without proof.

- `YT_EW_COLOR_PROJECTION_THEOREM.md` Section 1.3 cites
  `YT_VERTEX_POWER_DERIVATION.md` for the assertion; Section 2.4 proves
  the *correlator-level* CMT identity but does not bridge to the
  coupling-rescaling map.

Block 10 closes the **CMT correlator identity ⟹ coupling-rescaling
map** step that has been an unstated assumption in all the above.
That step's proof is the body of the present theorem. Distinct
contribution.

## V5. Runner is non-trivial

**PASS.** Runner `frontier_alpha_s_cmt_coupling_map_derivation.py`
executes 7 exact-symbolic tests:

- **T1 (derivation):** Given (I2), (I3), and (I1), sympy `solve`
  uniquely yields `alpha_eff = alpha_bare / u_0^{n_link}` (residual
  = 0 after `simplify`).
- **T2 (round-trip):** Substituting (M) back reproduces (I1) exactly.
- **T3 (n_link = 1):** Specialization yields `alpha_LM = alpha_bare/u_0`
  (matches (D1)).
- **T4 (n_link = 2):** Specialization yields `alpha_s(v) = alpha_bare/u_0^2`
  (matches (D2)).
- **T5 (composition with (P1)):** `alpha_LM^2 = alpha_bare * alpha_s(v)`
  closes self-consistently when (D1) and (D2) come from (M).
- **T6 (direction check):** `alpha_eff/alpha_bare = u_0^{-n_link} > 1`
  when `0 < u_0 < 1`, matching the expected tadpole-improvement
  direction.
- **T7 (counterfactual):** Reversed CMT identity (`<O(U)> = u_0^{-n_link}
  <O_V(V)>_eff`) gives `alpha_eff = alpha_bare * u_0^{n_link}` instead,
  proving the direction in (I1) is load-bearing.

Result: **7/7 PASS** in 0.26 s. Output cached at
`logs/runner-cache/frontier_alpha_s_cmt_coupling_map_derivation.txt`
via `scripts/cached_runner_output.py --refresh`.

The runner is non-trivial in that it (a) performs an actual `solve`
that could in principle fail to be unique, (b) checks the round-trip
direction, (c) covers two physically distinct specializations,
(d) checks a counterfactual that distinguishes the result from a
convention-free coincidence. T7 in particular shows the asymmetry of
(I1) — the direction of rescaling is genuine physics, not a notation
convention.

## V1-V5 Overall

**PASS** on all five gates. Source note + runner + cache + block
artifacts cleared for PR.

## Notes on the contribution scope

This is a narrow positive theorem closing one previously-assertion-only
algebraic step. It does not promote the parent row. It does close a
genuine missing brick that has been implicitly assumed in adjacent
notes for at least a month. The contribution is structural-completeness:
the chain CMT correlator → coupling map → coupling-chain identities
is now algebraically closed end-to-end at the level of bounded
narrow theorems, modulo the named admissions.

The next-block recommendations in `CLAIM_STATUS_CERTIFICATE.md`
identify two more narrow targets (Wilson `u_0 = <P>^{1/4}` derivation,
kinematic-factor invariance K_U = K_V derivation) that, if closed,
would further reduce the admission count on the chain.
