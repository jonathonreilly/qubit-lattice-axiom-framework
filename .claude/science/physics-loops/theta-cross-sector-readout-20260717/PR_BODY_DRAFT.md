# PR body draft — theta lane block01

## Summary

Block 01 of a new lane on the third foundation-surface derivation
obligation
(`THETA_QUARK_DETERMINANT_CROSS_SECTOR_READOUT_DERIVATION_OBLIGATION.md`).
One bounded theorem note plus a 26-gate exact runner giving the
obligation's *forcing* half an exact characterization:

- **T1 — Forcing-level characterization.** A supplied property set
  guarantees vanishing registered phase content for every functional
  satisfying it **iff** it contains K/CPT orbit constancy plus at least
  one odd-side ingredient (record-additivity with its conjugate-pair
  normalization, or the block homomorphism). Necessity is per role and
  per route, witnessed exactly (the k = 1 character; the sin(φ)
  consequence-level witness; the cos(arg z) hostile guard repositioned).
  No individual-functional biconditional: an exact silent witness
  (1 + |z|) outside both odd-side properties is gated.
- **T2 — Cross-sector reduction (a reduction, not a closure).** Under the
  identification the obligation names, its forcing half reduces to exactly
  one transported property: K/CPT orbit constancy on the quark determinant
  channel; the odd side is sector-local. The physical half (carrier
  construction, readout map, exhaustion — the axiom-update no-go's live
  routes 1-3) is untouched and named open, per the obligation's own
  closure criterion.
- **T3 — Theta-bar honesty guard.** Mass-side registered content only; the
  gauge slot and `theta_bar = theta_gauge + arg det(M_u M_d)` untouched.

Worker precision flag adopted into the note: oddness follows from
additivity only together with the conjugate-pair trivial-sector
normalization (both parts of the landed registrable shape); the runner
prints this flag in its own output.

## Changes

- `docs/THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md`
- `scripts/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.py` (30 gates, sympy-exact, single process)
- `logs/runner-cache/theta_cross_sector_determinant_forcing_property_characterization_2026_07_17.txt` (SHA-pinned)
- `docs/audit/data/citation_graph_manifest.json` (stage-18 refresh: 1 added node)
- Loop pack under `.claude/science/physics-loops/theta-cross-sector-readout-20260717/`

## Value gate and no-go gate

V1-V5 in the pack's `CLAIM_STATUS_CERTIFICATE.md` (V1 quotes the
obligation's forcing-half text verbatim). N1-N8 for the two necessity
negatives inline in the note. First PR in this family (no cluster cap).

## Review rounds applied

Supervisor pre-battery (9/9) before authoring; bidirectional machine quote
audit against all four cited theta surfaces; line-by-line runner review;
one combined adversarial lens (algebra + overclaim + governance —
disclosed as a reduced panel for a note of this size): 1 blocker / 6
major / 2 minor, ALL accepted and repaired before commit — the blocker
corrected T1's quantifier level (individual-functional iff was false;
exact silent counterexample adopted as a gate), W1 re-scoped to the
homomorphic route with sin(φ) covering the additive route, T2's
quark-side premise made explicit, phase-domain wrap/branch walls stated
and gated. Synthesis in REVIEW_HISTORY.md.

## Mutation checks

Ten families (C, P1, P2-det, W1, W2, T2, N, X1-wrap, X3-silent,
X4-sine), one load-bearing mutation each, all FAIL correctly; table in the pack's REVIEW_HISTORY.md.

## Test plan

- [x] Runner `TOTAL: PASS=30 FAIL=0`; cache SHA-pinned and verified
- [x] Pipeline clean; derived churn restored to origin/main; locally
      seeded shards dropped; only the manifest delta staged (1 node)
- [x] `repo_invariants_check.py --check` PASS; `audit_lint.py --strict` OK;
      vocab_lint clean
- [x] Quotes machine-verified bidirectionally

Independent audit remains required; landing is not ratification; the
obligation remains open exactly as stated.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
