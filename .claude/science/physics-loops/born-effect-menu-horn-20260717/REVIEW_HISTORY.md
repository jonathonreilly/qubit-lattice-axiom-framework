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

# Block03 review history

## Round 0 — supervisor pre-battery (before authoring)

10/10 from planning: f-complement/endpoints/denominator; the four exact
f-values; the 41/56-vs-125/152 non-affinity; the 4/7 ternary violation; the
merge-lemma elimination; the merged element's distinct nonzero eigenvalues;
the halved axis identity.

## Mutation checks (block03) — executed, all FAIL as required

| Family | Mutation | Result |
|---|---|---|
| F | completed-square constant 1/4 -> 1/2 | FAIL F2-identity (+F2-lower-bound) |
| T1 | sigma0 z-coefficient 1/2 -> 1 | FAIL T1a (+T1c cascade) |
| T2 | binary regrouping normalization = 2 | FAIL T2a |
| T3b | merge equation drops the a2 term | FAIL T3b-two-direction |
| T3c | halved axis element /2 -> /3 | FAIL T3c-axis-symbolic |
| T3d | complement equation = 2 | FAIL T3d-positive |
| T4a | expected eigenvalue sqrt(2) -> sqrt(3) | FAIL T4a-spectrum |
| T4c | nonparallel witness -> parallel e_z | FAIL T4c-projector-piece (the lemma's own content) |
| T5 | target eigenvalue (1-c) -> (1-2c) | FAIL T5a-spectrum |
| N | needle string perturbed | FAIL N2 |

Unmutated runner: `TOTAL: PASS=42 FAIL=0` (worker + supervisor re-runs);
cache SHA-pinned and verified; `__TOTAL__` resolved to 42 only after the
runner was final.

## Round 1 — block03 four-lens adversarial panel (delivered; synthesized)

- Lens 1 (convention/sign): 0/0/0 — recomputed sigma0, merge/axis signs
  (incl. a flip-sign self-test), T4c eigenvalues, T5 spectra.
- Lens 3 (independent algebra): no counterexample vs T1-T5; four repairs:
  cleaner coin-based T1 refutation; region-general G1-G2 restatement;
  merge-lemma coverage for trace>1 elements (separate-outcomes route);
  sign(0) omission clause; T5 c=0 endpoint mention.
- Lens 4 (governance): FAIL as written — T4 lacked its own N4/N6/N7
  entries; "force nothing beyond the complement law" overbroad; dimension
  mismatch; trace-gate single-target ambiguity; "classification"/"OPEN"
  collided with controlled vocabulary. All corrected.
- Lens 5 (overclaim + parent characterization): runner total confirmed;
  parent quotes accurate; converged with lens 3 on the T1 refutation
  route, the step-(B) iterated-pairwise-homogeneity wording, the D_mix
  representation route, and "map completion" softened to planned-slices
  completion.

### Dispositions (all applied before the PR)

1. T1 refutation now coin-primary (`w0((1/4)1) = 1/28` vs trace `1/4`,
   gated T1f with a generic-state derivation) with the three-point exhibit
   corrected (azimuth clause). 2. "Force nothing beyond the complement
   law" narrowed to "do not force the Born trace form" everywhere.
3. G1-G2 stated on finite-region effect algebras; witnesses labeled
   one-site; T2 forcing claim scoped accordingly with iterated-pairwise
   homogeneity replacing "steps (B)-(E) apply unchanged". 4. D_mix
   representation argued by the separate-outcomes refinement, gated on a
   trace-7/5 element (T3f). 5. sign(0) qualifier added to the halved axis
   display. 6. T5 endpoint parenthetical fixed. 7. N4/N6/N7 completed for
   T4 (PSD-parallelism steelman). 8. Certificate cluster-cap wording
   de-collided ("distinct artifact kind (content sense)"; "OPEN-the-PR");
   trace-gate primary/secondary target note added.

Post-fix: runner `TOTAL: PASS=44 FAIL=0` (42 + T1f + T3f); both new
families mutation-probed FAIL correctly; cache re-pinned; note total
synced to 44.

### Round 1 disposition after fixes: pass

## Round 2 (block01) — external reviewer reconciliation finding: REPAIRED

Finding (reviewer, via owner): block01's T3 witness was extended to
non-product projections by the constant 1/2 while the note's framing left
the landed H2 readable as GLOBAL orthogonal additivity; under that reading
the extension violates additivity exactly — for `R = |00><00|`,
`P = |psi+><psi+|`, `Q = R + P`: `W(Q) − W(R) − W(P) = 1/2 − 1 − 1/2 = −1`
— and the 54/0 runner never tested the extension against global
additivity. Supervisor verification: exact (R ⊥ P; Q rank 2, non-product
by partial-trace spectrum {3/2, 1/2}; defect −1). Deeper consequence
identified during repair: under the global-additivity reading the T3
boundary is not merely unwitnessed but FALSE — global additivity plus
normalization makes any weight a frame function on Proj(M_4) (finite
induction over orthogonal sums), where the landed Gleason bridge input
forces the trace form regardless of menu eligibility. The menu-family
restriction is meaningful only with menu-carried additivity.

Repair (this round, on the block01 branch / PR #5472):
- T3's hypothesis surface stated exactly: menu-carried additivity
  (normalization over eligible product menus plus within-family
  coarse-grainings whose merged element is again a product projector);
  global orthogonal additivity explicitly not retained, with the
  trivialization argument in the note (preamble + T3c) and claim_scope.
- T3b now states the extension's exact status: within-family additive
  (both classified merge cases gated, T3j) and provably not globally
  additive (the reviewer witness gated exactly, T3k, including the
  non-product status of Q via partial-trace spectrum {3/2,1/2} vs the
  product rank-2 spectrum {2,0}); a globally additive completion cannot
  exist, by the frame-function argument.
- Runner: +2 gates (T3j, T3k); mutations for both families FAIL correctly
  (within-family residual perturbed; psi+ degraded to a product vector,
  which kills the non-product gate); total 54 -> 56; cache re-pinned;
  note verification inventory and measured total synced.
- Block02 (#5476) audited for reliance: it reuses only block01's ONE-SITE
  rogue (R1 lineage) and T1-side text, never pair-level T3; its own
  boundary carries the self-contained cubic witness. No mathematical
  change needed; the stack is merged forward so its branch carries the
  corrected parent. Block03 likewise does not lean on block01-T3.

Lesson recorded for memory: when a panel demands a witness be extended to
a larger domain, RE-CHECK every remaining hypothesis against the extended
object — the extension satisfied the domain demand and silently broke a
differently-read hypothesis; and state additivity's carrier (menus vs
global) explicitly whenever restricting menu families.