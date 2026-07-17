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
