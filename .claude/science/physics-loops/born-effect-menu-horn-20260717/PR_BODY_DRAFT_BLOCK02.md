# PR body draft — block02 (final numbers synced before opening)

**Stacked PR**: base = `physics-loop/born-effect-menu-horn-block01-20260717`
(block01, PR #5472). This block cites the block01 note and must land after
it.

## Summary

Block 02 of the Born-wall menu-grade lane: thins the effect-horn premise on
the exact surface block01 named untested ("classical mixtures of projective
menus and other intermediate families"). One bounded theorem note plus an
exact runner:

- **T1 — Exact family characterization.** The scaled-projector family
  (nonnegative multiples of one-site rank-1 projectors and of the identity):
  a finite family is a menu iff its weighted directions cancel and its
  scalar parts sum correctly (vector-zero + scalar-two conditions). The
  family contains projective menus, coins, same-direction splits,
  axis-cancellation menus, and coplanar three-element menus, and excludes
  every effect with two distinct nonzero eigenvalues — strictly between the
  projective and effect poles.
- **T2 — Forcing with zero literature input.** On this family, menu
  normalization plus effect-functionality forces the Born trace form on the
  domain at a single M_2 site. New proof mechanism (not the five-step Busch
  route): ray additivity from same-direction splits, complement, then a
  single **axis-cancellation menu** per direction forces affinity
  `g(n) = (1 + n·s)/2` in one elimination. The forcing runs on scaled
  rank-1 menus alone — no unsharp effects, no coins load-bearing, no
  composite, finite menus only.
- **T3 — Paired-menu boundary (bounded negative, constructive).** The
  paired subfamily (equal-weight antipodal pairs + identity multiples — the
  shape of unsplit classical mixing) does not force: the landed hemisphere
  rogue extends to it explicitly. So some unpaired menu is necessary, and
  the two unpaired schemas the proof uses are exactly where the forcing
  lives.
- **T4 — Dial recalibration.** Sitewise Born form-fixing needs neither the
  full effect algebra nor unsharp effects; the registration question
  narrows to whether supplied menus ever leave the paired subfamily. No
  family selected; minimality not claimed; Wright-Weigert 2019 comparator
  only (their class differently delimited; native translation re-parked).

## Changes

- `docs/BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`
- `scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py` (60 gates)
- `logs/runner-cache/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.txt` (SHA-pinned)
- `docs/audit/data/citation_graph_manifest.json` (stage-18 refresh: 1 added node relative to block01)
- Loop pack block02 files under `.claude/science/physics-loops/born-effect-menu-horn-20260717/`

## Value gate and no-go gate

V1-V5 in `CLAIM_STATUS_CERTIFICATE_BLOCK02.md` (V1 quotes the parent's
named-untested text verbatim). N1-N8 for the T3a negative inline in the
note.

## Review rounds applied

Supervisor independent sympy battery (9/9) before worker completion.
Five-lens adversarial panel: lens 3 (independent algebra) PASS with its own
re-proof of T1-T3 and three failed non-affine attack candidates, plus a
contributed second paired-boundary witness (the cubic assignment), adopted
into T3a with three new runner gates; 12 findings across the other lenses
all fixed before commit (rank-1-alone narrowing, dependency declaration,
T3b family-level restatement, Verification coverage wording, sign-hardened
axis helpers, trace-gate prose). Full synthesis: REVIEW_HISTORY.md.

## Mutation checks

Eleven families, one load-bearing mutation each, all FAIL correctly
(including the new cubic-witness family); table in REVIEW_HISTORY.md.

## Test plan

- [x] Runner `TOTAL: PASS=60 FAIL=0`; cache SHA-pinned fresh and verified
- [x] Pipeline clean on stacked branch; derived churn restored to the
      block01 branch state; locally seeded shards dropped; only the
      manifest delta staged (1 added node)
- [x] audit_lint --strict OK; vocab_lint clean
- [x] Quotes machine-verified bidirectionally (parent + axiom memo)

Independent audit remains required; landing is not ratification.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
