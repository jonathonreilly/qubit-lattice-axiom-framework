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
- 2026-07-25 codex review-loop verdict on PR #5588: `PASS WITH BOUNDED CLAIMS`;
  landed on main as 82af65ba7d plus reviewer fixes 7862bc299e (G07 evidence row
  spelled out the K†K = 4Q₂₄ singular-value derivation; G08 hardened to
  full-action eigenspace residuals). No audit verdict applied — the row lands
  unaudited. Block 2 CLOSED.

## Block 3 — KCPT Unit 22

- 2026-07-25 planner review (Fable): note and runner read line-by-line
  (runner construction section byte-identical to the U21 runner — 0-line
  diff verified); PRESERVE greps present, forbidden strings absent; markdown
  link inventory exactly the 2 intended dependency edges U20+U21; own re-run
  `TOTAL: PASS=47 FAIL=0`, exit 0.
- 2026-07-25 adversarial-verification pass (3 independent lenses):
  fabrication-hunt clean at high confidence (independent reproduction of
  every load-bearing number); algebra-re-derive clean at high confidence;
  framing-audit returned 3 minor findings, all fixed by the planner
  pre-commit — (1) the T3 H-class-function license rested on an ungated true
  premise (separator H-invariance): new discriminating gate B3 added
  (max_h ||h sep h^T - sep||_F < 1e-10, measured 4.48e-13), PASS 46->47;
  (2) spec meta-language comment removed from the runner; (3) opening scope
  narrowed to the single-ambient-element-extension family.
- 2026-07-25 discriminating-gate perturbation test: substituting an in-frame
  projector difference for the separator flips exactly 12 gates (A7, C4-C6,
  D2.1/D2.2, E2.2, E8.2, F1/F2, G2) and exits 1 — the battery discriminates;
  B3 correctly passes on it (its role is rejecting a non-H-invariant
  separator, not a wrong in-frame one).
- 2026-07-25 codex review-loop verdict on PR #5589: `PASS WITH BOUNDED CLAIMS`
  on the repaired integration (the original PR state did not pass review).
  Reviewer repairs before landing: an unsupported promotion from algebra
  membership to physical readout/Record claims removed; floating-point
  results reframed as tolerance-qualified numerical evidence; live SVD and
  cluster-separation margins added; bare gate names replaced with scientific
  labels; the citation-graph manifest update added; N1-N8 no-go discipline
  completed for the narrowed finite-algebra non-membership claim. Landed
  runner `TOTAL: PASS=49 FAIL=0`, cache SHA exact; audit pipeline full PASS,
  strict lint zero errors. Closed-not-merged = salvage-landed on main as
  dd9f6003e2 plus reviewer fixes b84a792204. No audit verdict applied — the
  row lands unaudited. Block 3 CLOSED.

## Block 4 — KCPT Unit 23

- 2026-07-25 planner review (Fable): note and runner read line-by-line
  against the recon ground truth; own independent re-run clean (exit 0,
  FAIL=0); PRESERVE/forbidden-string greps and dependency link inventory
  verified; 3-lens adversarial-verification pass (fabrication-hunt,
  algebra-re-derive, framing-audit) completed and synthesized by the
  planner before commit.
- 2026-07-25 codex review-loop verdict on PR #5590: `PASS WITH BOUNDED
  CLAIMS`; 2 review iterations (round-one review plus focused
  confirmation); 2 findings, both fixed; N1-N8 checklist PASS; live runner
  34/34 PASS after the fix, independent L=4/L=6 order cross-check PASS,
  cache SHA exact; audit pipeline full PASS, strict lint zero errors.
  Closed-not-merged = salvage-landed on main as 93586b92bb plus reviewer
  fix eaf6ea001f. No audit verdict applied — the row and its direct
  dependencies land unaudited. Block 4 CLOSED.

## Block 5 — KCPT Unit 24

- 2026-07-25 planner review (Fable): note and runner read line-by-line;
  the two spec-mandated LICENSING gates — L1 (sep6 H-invariance over
  generators plus inverses, measured 1.7e-14) and L2 ((dim C_g, omega)
  H-class-function check over 6 strata x 3 random conjugates) — were
  missing from the executor build and added in review, gate count 23 -> 25;
  the note's d(g) aggregate corrected to the measured 47-of-61 split at
  d=9 and CN_dg strengthened to pin the 14/61 split; one executor deviation
  accepted and disclosed (an RNG-free corner-center certificate substituted
  for the spec's two-seed central-idempotent clustering, which failed to
  converge on the 17-atom center; certificate reviewed line-by-line, a
  closed-flag guard added). Own re-run `TOTAL: PASS=25 FAIL=0`.
- 2026-07-25 adversarial-verification pass (3 independent lenses): algebra
  re-derivation clean; fabrication and framing lenses returned 5 minor
  findings, all repaired pre-commit (an unbacked DIAL orbit attribution
  softened to the census-backed statement; "every rho(h)" re-attributed
  from the sampled gate to the generating-set gate L1; "equals 4/15
  exactly" restated with the honest 7.4e-15 residual; CHR1/CHR2
  strengthened to pin size 72 / dim 108 on the four Delta-chi != 0 orbits
  and size 12 / dim 68 on the counterexample class). Runner re-run after
  strengthening: `TOTAL: PASS=25 FAIL=0`.
- 2026-07-25 codex review-loop verdict on PR #5591: `PASS WITH BOUNDED
  CLAIMS`; one remediation iteration, 4 findings fixed, 0 skipped
  (bounded_theorem claim typing added; H-class-function proof and gate
  strengthened; cap-600 closure gate corrected to track cap-600 misses;
  algebra dimensions clarified as complex). Landed runner
  `TOTAL: PASS=26 FAIL=0`, cache freshness verified. Closed-not-merged =
  salvage-landed on main as f1ebe0b00a plus reviewer fixes d127cf56df.
  No audit verdict applied — the row lands unaudited. Block 5 CLOSED.

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
  (synced to e3edf71f9d).
- 2026-07-25 exit summary: 19 rows audited and landed on main by the
  independent lane — 11 audited_conditional, 4 audited_failed,
  2 audited_clean, 1 audited_decoration, 1 audited_renaming (grades are the
  audit lane's own outputs, recorded verbatim from its log). 24 same-row
  collisions resolved as `remote_state_superseded` (authoritative). 1
  compute-required quarantine (`local_zsym_predictor_note` — needs a
  completed execution of `scripts/local_zsym_predictor.py` or an
  authenticated cached certificate for that exact run). Stop cause: push
  retries exhausted on `equivalence_principle_harness_note` (main moving
  fast under concurrent audit traffic); rollback verified clean at
  origin/main 969284052e. 624 ready rows remaining at exit (672 lane
  blockers); clone clean and synchronized.

## Lane C — audit-loop drain (third pass)

- 2026-07-25: worker `audit-w-20260725-c` dispatched on the same clone,
  re-synced clean to origin/main 7fdbbdd2c1 first.
- 2026-07-25 exit summary: 108 rows audited and landed on main by the
  independent lane — 64 audited_conditional, 19 audited_failed,
  15 audited_clean, 5 audited_renaming, 3 audited_numerical_match,
  2 audited_decoration (grades are the audit lane's own outputs, recorded
  verbatim from its log). Quarantines: 3 schema, 3 compute-required,
  1 blocked-row reentry. Zero coordinator failures and zero transaction
  quarantines; concurrent-worker collisions resolved as
  `remote_state_superseded` (authoritative) throughout. Stop cause:
  codex-API 503 outage (service circuit open; websocket and HTTPS
  reconnect attempts exhausted) — an external service outage, not a
  coordinator failure; the final round drained clean (4 verdicts) before
  the outage and the clone state was left clean. 219 dependency-ready
  targets remained at the last round start. 753,338 tokens.
