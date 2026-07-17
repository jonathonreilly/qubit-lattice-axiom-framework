# Review History — block01

## Round 0 — supervisor independent verification (before worker completion)

Independent sympy battery, written by the supervisor from the note text
alone (not from the worker's runner): T2b forced value 1/2; T3g tree-menu
normalizations under only the complement law (all five shapes); T3h
pair-restriction affinity at d=4; T3a projector trace formula; T3b product
trace factorization; T3i Bell Schmidt rank 2; T3f mixed rank-2 sum is not
the identity; T5 Pauli-conjugation commutant is scalar (`{a: b, c: 0,
d: 0}`). All verified `ALL: True`. This is the redundancy channel: the same
identities must independently pass in the worker's runner.

## Round 1 — five-lens adversarial panel (delivered; synthesized below)

Lenses (codex read-only workers; verdict synthesis supervisor-owned):

1. convention/sign — Bloch/lex-tuple conventions, projector formulas,
   antipodal orthogonality, tie-set handling.
2. licensing/quotes — every quoted sentence verified verbatim against the
   cited file at HEAD; frontmatter fields; link targets tracked.
3. independent algebra — re-derive T2b forced value, one T3g normalization,
   the C1/C2 Gram nonsingularity, and the D1 Bloch solve independently.
4. governance/manifest — no forbidden surfaces staged; vocabulary; status
   wording; N1-N8 presence for the T3 negative; non-claims completeness.
5. overclaim — scope of every "forced"/"necessary"/"nothing" sentence vs
   what the runner actually certifies.

### Verdicts (raw outputs in lens{1..5}_out.txt; verdict synthesis supervisor-owned)

- Lens 1 (convention/sign): 0/0/0 — conventions independently recomputed
  clean (lex tuple, tensor ordering, forced sign, D2/D3 coefficients, T5
  conjugation direction).
- Lens 2 (licensing/quotes): 0/0/1 — all quotes verbatim; all cited-note
  characterizations verified against source text (including the 2026-05-20
  routing and countable-additivity reading). Minor: "exact shape of H1-H3"
  understated that universal menu eligibility lives in H4.
- Lens 3 (independent algebra, note-only): 0/1/1 — independently re-proved
  T1(A-C) soundness, the full T3a classification (own case analysis, no
  counterexample), T3b normalizations, and the pair-trace refutation; major:
  the T3 witness must state its full-projection-domain completion; minor:
  "necessary" stronger than proven.
- Lens 4 (governance/status): 2 blockers / 2 major / 1 minor — the same two
  substantive items (scope broadening via "necessary"; witness-domain
  completeness in N3) plus wording ("registers", "binary"), a certificate
  marker-summary mismatch, and a vocabulary flag on loop-pack yaml labels.
- Lens 5 (overclaim): 0/1/2 — same "necessary" major; "force nothing"
  literalism; "exact open binary" inconsistency; full strong-word
  disposition table otherwise (a)/(b)-supported; runner total confirmed
  54/0 by the lens's own execution.

### Dispositions (all applied before commit)

1. "necessary at 2x2" family (L3-min, L4-B1, L5-maj) — FIXED everywhere to
   the proven form: "H4's menu family cannot be weakened all the way to
   product-projector menus at 2x2; whether full H4 or an intermediate
   family is minimal is untested." Note claim_scope, Purpose, T3c, T4,
   TRACE_GATE, GOAL, NO_GO_LEDGER, ROUTE_PORTFOLIO, PR body draft updated.
2. Witness domain (L3-maj, L4-B2) — FIXED: T3 preamble + T3b now state the
   restricted menu family leaves non-product values unconstrained and
   exhibit the explicit constant-1/2 extension to the full projection
   domain; N3 updated to reference it.
3. "force nothing" (L5-min) — FIXED to "do not force the Born trace form"
   in every location.
4. "exact open binary" / "registers it" (L4-maj, L5-min) — FIXED to "open
   item of the declared specification burden ... records two bounded horns
   and selects no grade"; hypotheses/scope now name the two grades as poles
   with intermediate families untested.
5. E1-E2 attribution (L2-min) — FIXED: eligibility strength attributed to
   an H4-style clause, quoted.
6. Certificate N1-marker summary (L4-min) — FIXED to the actual markers.
7. Loop-pack yaml labels `bounded-support` / `trace_class` enumerations
   (L4-maj) — REJECTED with reason: these exact enumerations are mandated
   by the physics-loop skill's required status/trace schemas for
   branch-local loop state (`actual_current_surface_status:
   open|no-go|exact-support|bounded-support|...`; `trace_class:
   direct_blocker_closure|upstream_support|negative_route_pruning|...`);
   the note itself introduces no such vocabulary.

### Round 1 disposition after fixes: pass

Post-fix checks: runner re-run PASS=54 FAIL=0; vocab_lint clean;
audit_lint --strict OK; quotes re-verified bidirectionally after edits.

## Mutation checks (PREFLIGHT item 8) — executed, all FAIL as required

One load-bearing mutation per gate family (scratch copy inside the worktree,
removed after each run):

| Family | Mutation | Result |
|---|---|---|
| A | menu remainder `I - E1 - E2` -> `I - E1 - 2*E2` | FAIL A3-d2 (53/1) |
| B | squeeze scaling `(t - q1)*E` -> `(q1 - t)*E` | FAIL B3 (53/1) |
| B (2nd probe) | `q2 = 2/3` -> `1/3` (empties the interval) | FAIL B3 (53/1) |
| C | basis `(sx, sy, sz)` -> `(sx, sx, sz)` (dependent) | FAIL C1-gram |
| D | Bloch coefficient `(2*w_x - 1)` -> `(2*w_x + 1)` | FAIL D1 (53/1) |
| E | projector `psi*psi.H` -> `psi*psi.T` (no conjugate) | FAIL E2 (53/1) |
| T2 | lex tuple `(nz, ny, nx)` -> `(nx, ny, nz)` | FAIL T2a + T3h (52/2) |
| T3c | third antipode `b3 = -b1` -> `b3 = +b1` | FAIL T3c (53/1) |
| T3g | drop one leaf from the site-1 tree menu | FAIL T3g-tree4 (53/1) |
| T5 | invariance group `{sx,sy,sz}` -> `{sz}` only | FAIL T5a + T5b (52/2) |
| N | perturb the N1 needle string | FAIL N1 (53/1) |

Finding from the first B probe: the original `nonnegative_between` was
vacuously true on an empty interval; supervisor hardened the gate with an
interval-nonemptiness guard (runner edit after worker delivery), after which
both B probes fail correctly. Unmutated runner: `TOTAL: PASS=54 FAIL=0`.

# Block02 review history

## Round 0 — supervisor independent verification (before worker completion)

Independent sympy battery from the note text alone, 9/9: axis-cancellation
menu sums to identity (symbolic positive octant); affinity elimination
g(n) = (1 + n·s)/2; the T1 characterization identity; paired-menu rogue
normalization; the coplanar three-element menu; octant witness coefficients
in (0,1] and menu identity; ray-additivity elimination; the zero-component
axis menu.

## Mutation checks (block02) — executed, all FAIL as required

| Family | Mutation | Result |
|---|---|---|
| D | traceless recovery /2 -> /3 | FAIL D1 (56/1) |
| T1a | scalar condition /2 -> /3 | FAIL T1a (56/1) |
| T1c | c0 = 2/(1+L) -> 1/(1+L) | FAIL T1c-generic + T2d-generic (55/2) |
| T2a | second split normalization = 2 | FAIL T2a (56/1) |
| T2b | squeeze scaling sign flip | FAIL T2b-squeeze + T2e-squeeze (55/2) |
| T2d | complement equation = 2 | FAIL T2d-generic (56/1) |
| T2f | sigma sign flip | FAIL T2f-representation (56/1) |
| T3a | paired scalar condition = 2 | FAIL T3a + T3d (55/2) |
| T3b | lex tuple order flipped | FAIL T3b-hemisphere + T3d (55/2) |
| N | needle string perturbed | FAIL N2 (56/1) |
| T3a-ind (post-panel) | cubic exponent 3 -> 2 | FAIL T3a-ind-complement (59/1) |

Unmutated runner at worker delivery: `TOTAL: PASS=57 FAIL=0`; after the
panel-adopted cubic-witness gates and sign-hardening: `TOTAL: PASS=60
FAIL=0` (supervisor re-runs).
Cache SHA-pinned and verified equal to the committed runner SHA. The note's
`__TOTAL__` placeholder was resolved to 57 only after the runner was final
(block01 placeholder lesson applied).


## Round 1 — block02 five-lens adversarial panel (delivered; synthesized)

### Verdicts (raw outputs in lens{1..5}_b02_out.txt; synthesis supervisor-owned)

- Lens 1 (convention/sign): 0/0/1 — all load-bearing conventions verified
  including the (L^2-1) = 2(ab+ac+bc) and (3-L^2) sum-of-squares
  certificates; minor: the axis helpers silently defaulted undecidable
  component signs to negative (no current call site affected).
- Lens 2 (licensing/quotes): clean on quotes/links/characterizations; one
  finding: claim_scope's "forcing runs on scaled rank-1 menus alone /
  no genuinely unsharp effect" was stronger than the body (coins determine
  the identity ray of the representation).
- Lens 3 (independent algebra, note-only): PASS — independently re-proved
  T1, T2 (ray additivity, squeeze, axis-cancellation validity incl. octant
  and zero-component handling, positivity, uniqueness), T3a for arbitrary
  finite paired menus; three non-affine attack candidates all failed at an
  identified menu; contributed an independent smooth witness
  g_c(n) = (1 + n_z^3)/2 refuting its unique trace candidate at
  m = (sqrt(3)/2, 0, 1/2) (9/16 vs 3/4).
- Lens 4 (governance): three findings — the parent note is a load-bearing
  dependency missing from frontmatter upstream_dependencies; one backticked
  class-word in TRACE_GATE_BLOCK02 prose; certificate disposition
  procedurally unfinished. Confirmed the note's descriptive names are not
  coined governance tiers and N1-N8 is complete.
- Lens 5 (overclaim): runner total confirmed by its own execution; six
  narrowings — "rank-1 menus alone" (full-domain false), "no bridge input"
  heading vs bridge-conditional scope, Verification "re-derives every
  load-bearing identity" overstated runner coverage, T3b universal wording,
  "exactly such menus" vs degenerate instances, "exactly witnessed line"
  vs necessary-not-sufficient.

### Dispositions (all applied before commit)

1. Rank-1-alone family (L2, L5-1): FIXED — claim_scope, Purpose, and T4
   wording now state: scaled rank-1 menus carry the form-forcing; coin
   menus determine only the identity ray; "genuinely unsharp" replaced by
   "effect with two distinct nonzero eigenvalues".
2. "No bridge input" heading (L5-2): FIXED to "without an imported
   literature theorem" (T2 heading) and "With No Literature Bridge Input"
   (title); the established phrase "no literature bridge input" retained.
3. Verification coverage (L5-3): FIXED to "exactly checks the listed
   algebraic reductions and representative witnesses; the
   arbitrary-finite-family and all-real-parameter steps are carried by the
   written proof".
4. T3b universal wording (L5-4): FIXED to the family-level statement (any
   eligible family contained in the paired subfamily admits the witness;
   forcing families must contain an unpaired menu).
5. "Exactly such menus" / "exactly witnessed line" (L5-5, L5-6): FIXED to
   nontrivial/non-axis instances and to "witnessed necessary condition …
   no sufficiency boundary established".
6. Missing dependency (L4-1): FIXED — parent claim_id added to
   upstream_dependencies; TRACE_GATE_BLOCK02 lineage note added; T3a made
   additionally self-contained by adopting the lens-3 cubic witness with
   three new runner gates (T3a-ind-*), so the negative no longer rests on
   the parent's construction alone.
7. Backticked class-word in trace-gate prose (L4-2): FIXED to descriptive
   prose.
8. Sign-defaulting helpers (L1-1): FIXED — both axis helpers now raise on
   undecidable signs; runner re-run.

Post-fix: runner `TOTAL: PASS=60 FAIL=0` (57 + 3 cubic-witness gates); new
mutation probe (cubic exponent 3 -> 2) FAILS correctly; cache regenerated
and SHA-verified; note total synced to 60.

### Round 1 disposition after fixes: pass
