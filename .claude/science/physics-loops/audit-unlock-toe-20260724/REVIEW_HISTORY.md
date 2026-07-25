# Review History — audit-unlock-toe-20260724

## Block 1 — KCPT Unit 20

- 2026-07-24 planner review (Fable): note read line-by-line against the recon
  ground truth; runner read line-by-line (construction verbatim from the U19
  runner; gates G01-G19 + G-PIN-1..6 + G-PIN-LINKS discriminating); own re-run
  `TOTAL: PASS=26 FAIL=0`; PRESERVE/FORBIDDEN greps clean; cited-basename disk
  check clean (both U18/U19 dependency basenames exist on main). One threshold
  deviation investigated and resolved as honest: the G15 wrong-normalization
  contrast rejector fires at 0.0732 against a >1e-6 bar — discrimination at
  ~1e10 times the locked residual scale; load-bearing tolerances untouched.
- 2026-07-24 adversarial-verification pass (3 independent lenses:
  fabrication-hunt, algebra-re-derive, framing-audit): completed; synthesized
  by the planner before commit.
- 2026-07-24 codex review-loop on PR #5586: closed-not-merged = science
  salvage-landed on main (1aec7a71a3). Block 1 CLOSED.

## Block 2 — KCPT Unit 21

- 2026-07-24 planner review (Fable): note and runner read line-by-line; 9-section
  review battery (5 PRESERVE greps present, 8 forbidden strings absent, markdown
  link inventory exactly the 2 intended dependency edges U19+U20, cited-basename
  disk check clean for all 6 backticked notes plus the U20 runner, spec-leak scan
  clean, sibling-runner grep returns only the new pair); own re-run
  `TOTAL: PASS=38 FAIL=0`. One hardening applied: the census SV-gap certificate
  made unconditional for dim-0 census results (a conditional gate would silently
  skip exactly the load-bearing zero-dimension rows).
- 2026-07-24 discriminating-gate perturbation test: post-construction 1%
  corruption of J_bulk produces targeted failures (G01e, G06d) and exit 1 —
  gates live; construction-level corruptions crash before the gates and prove
  nothing on their own.
- 2026-07-24 adversarial-verification pass (3 independent lenses): fabrication
  lens clean (independent re-run reproduced PASS=38); framing and algebra lenses
  drove 3 pre-commit repairs (T1 parent-note attribution corrected — the
  chiral-parity note constructs H itself, so T1's new content is the exact
  1536-element census + gated multiplicativity + the s = chi_sgn identification;
  T4 fusion-exclusivity wording — both chi_sgn-odd generators named; Z^T -> Z^dag
  at 4 sites). Runner unchanged by the repairs.
- PR #5588 OPEN (commit 44e3031341); codex review-loop worker dispatched.
  Verdict to be recorded here.

## Lane A — audit-loop drain

- 2026-07-24: worker `audit-w-20260724-a` dispatched on a clean origin/main
  clone (tip f8f995774b at dispatch).
- 2026-07-24 exit summary: 18 rows audited and landed on main by the
  independent lane — 11 audited_conditional, 3 audited_clean,
  3 audited_renaming, 1 audited_failed (grades are the audit lane's own
  outputs, recorded verbatim from its log). 7 same-row collisions with the
  concurrent pipeline resolved as `remote_state_superseded` (authoritative).
  1 schema-invalid row quarantined
  (`microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18`).
  Stop cause: push retries exhausted on
  `universal_gr_stress_ward_transverse_seagull_bounded_theorem_note_2026-06-08`
  (main moving fast under concurrent audit traffic); rollback verified clean.
  632 ready rows remaining at exit; clone clean at origin/main 385da716ab.

## Lane B — audit-loop drain (second pass)

- 2026-07-24: worker `audit-w-20260724-b` dispatched on a fresh clean clone
  (synced to e3edf71f9d). Exit summary to be recorded here.
