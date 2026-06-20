# Single-Clock B-AXIS wall — review history

## Block 01 review (adversarial)

**Reviewer role:** hostile independent reviewer (review-loop backpressure).
**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block01-20260620` (HEAD d60f597ee)
**Deliverable under review:** `docs/SINGLE_CLOCK_BAXIS_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`
**Runners re-run with python3 (live), all reproduce the claimed counts and match cached logs:**
- `scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py` → PASS=36 FAIL=0
- `scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` → PASS=20 FAIL=0
- `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py` → PASS=17 FAIL=0
- `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` → PASS=16 FAIL=0
- Aggregate 89/89, cracks=0, confirmed live.

### DISPOSITION: `passed_with_notes`

No crack is overstated, no no-go is rendered premature, and no load-bearing hidden
import was found. Two genuine-but-minor honesty blemishes (one vacuous check, one
hardcoded-`True` conclusion in N2b) and one loosely-worded "S4-isotropic" claim in
the note prose (contradicted by the runner's own E2/E8 trivial-stabilizer output)
must be corrected in the note, but none changes any outcome. Block02 consolidation
MAY proceed.

---

### Per-route findings

#### R-N5-IRR (`single_clock_n5_irreducibility_factor_clock_2026_06_20.py`) — SOUND
- **Honest direction.** The runner asserts the *negative* throughout and prints
  `N5_CLOSED_BY_A_MIN = FALSE`, `SECOND_PHYSICAL_CLOCK_EXCLUDED = FALSE`
  (lines 482, 485). It does NOT falsely close N5; it sharpens the wall by exhibiting
  a genuine commuting second clock `n_0` with independent record content
  (CONTENT block: freezes ⟨n_1⟩ while H_hat moves it; min over swept t = 0.4407;
  L1 record-profile distance = 1.9988). This is the correct no-go-*supporting*
  shape: A_min fails to *exclude* a second clock.
- **No hidden import.** `E(p)=arcsinh(√(m²+sin²p))` is recomputed; T̂²=exp(-2a_τH_hat)
  verified to resid 2.8e-17; tensor factorization exact (resid 0); span rank = L_s
  confirmed for L_s∈{3,4}. The [GAUGE] leg correctly falsifies the gauge-collapse
  hypothesis (all 3/3, 4/4 mode generators escape span{I,H_hat}; n_0 best-fit
  residual 0.6727).
- **Note prose nit (not in runner):** the note labels the outcome "walled_named /
  no-go for N5" (note line 90). A skim-reader could misread that as "second clock
  excluded," which is the OPPOSITE of what the runner shows. The runner's own VERDICT
  lines are scrupulously correct; recommend the note adopt the runner's wording
  ("N5 exclusion FAILS without an unsupplied admission ray") rather than "no-go for N5."

#### R-N4-REGDIR (`single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py`) — SOUND
- **No hidden import that is load-bearing.** The transverse-field Ising H in [DYN]
  and the RNG probe in [PROD] are explicitly NON-load-bearing: H is supplied
  precisely to *demonstrate* the circularity (W-conjugate H' gives an identical cone,
  cone_diff < 1e-9), and the RNG (line 424, seed 0) only probes an arbitrary test
  matrix for covariance. The conclusion ("you need a generator / arrow / pointer-axis
  datum, all open gates") is the named wall, not a smuggled input.
- **Discriminating falsifiers present:** [W] naive unsigned swap fails (resid > 1),
  signed W exact (resid 1e-13); [PROD] axis-symmetric dephasing W-covariant (resid 0)
  vs asymmetric pointer break = 3.44. Genuine relocation to the record-production
  OPEN GATE; honestly NOT a crack.

#### R-N2b-JOINT (`single_clock_n2b_joint_clock_unit_check_2026_06_20.py`) — SOUND result, TWO cosmetic-PASS blemishes
- **Load-bearing result is real and discriminating.** block_B computes exact joint-
  rescaling invariance of T2, K, and T2⊗K (all max-delta < 1e-16). I verified the
  test has discriminating power: a malformed rescaling (a_τ scaled, H not) yields a
  0.245 delta, so the 0 deltas are a genuine computed gauge, not a built-in identity.
  block_C correctly shows dimensionful gap/relax CHANGE while their ratio is invariant.
- **BLEMISH 1 (vacuous check), n2b line 267:** `if abs(nu_per_block - nu_per_block) > 1e-15`
  compares a constant to itself → always False → the "count datum is clock-free" PASS
  tests nothing. The asserted claim is true, but the check is empty.
- **BLEMISH 2 (hardcoded conclusion), n2b line 281:** `record("no A_min observable
  returns a unit-bearing 1/time number -> c free", True, ...)` asserts the central N2b
  thesis as a literal `True` with no computation behind it. The thesis is supported by
  block_B/block_C, but stating it as a PASS line inflates the PASS count with a
  non-load-bearing assertion.
- **Required fix:** demote lines 267 and 281 to comments or replace with real checks
  (e.g. recompute nu from a constructed record stream under rescaling; verify no
  constructed A_min observable carries inverse-time units). PASS count drops by ≤2;
  conclusion unaffected.

#### R-N4-AUT (`single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`) — steelman GENUINE, but note prose OVERSTATES "S4-isotropic"
- **Steelman is genuine, not cherry-picked.** It computes the FULL bare automorphism
  group |G_bare| = 384 (= 24 axis-perms × 16 reflections, the entire B_4; every
  candidate admitted) and verifies S4-transitivity. It enumerates 8 enrichments
  including ones (E2 Laplacian, E8 diagonal graph) that a priori *could* break
  symmetry — not only known-symmetric ones. The crack criterion
  (`selects_exactly_one_axis`, lines 215-239) is the correct group-theoretic
  signature (fixes exactly one axis, transitive on the rest) and correctly rejects
  the trivial-stabilizer false-positive that E2/E8 would otherwise present.
- **ADVERSARIAL FINDING (note imprecision, not a crack):** For E2 (cubic Laplacian)
  and E8 (diagonal graph) — both enrichments A_min *does* supply — the JOINT
  stabilizer inside G_bare is the **identity alone** (axis image size 1, reflections
  {(1,1,1,1)}). I verified: the plain swap preserves the Laplacian but breaks the
  staggered hop (resid 22.6); the dressed W01 preserves the hop but breaks the
  Laplacian (resid 45.3); NO non-identity axis-perm in B_4 preserves both. So the
  axis-exchange W *is broken* by these A_min enrichments. The note (lines 256, 299,
  and "every A_min enrichment ... is S4-isotropic", line 256/299) and the table
  classification gloss this as "S4-isotropic," which is FALSE for E2/E8 — their joint
  stabilizers are TRIVIAL, not S4.
- **Why it is nonetheless NOT a crack (verified):** the breaking is symmetric — there
  is no surviving symmetry that fixes one axis while permuting the others. The
  Laplacian is fully S4-isotropic on its own (24 plain perms) and the hop is
  S4-isotropic via dressed perms; the trivial *joint* stabilizer treats all four axes
  on equal footing, so no axis is *selected*. The genuine crack criterion (a sub-S4
  stabilizer fixing exactly one axis) is met ONLY by E7, which is the supplied
  (A,P,P,P) BC datum — and E7 is verified S4-transportable (W01 maps (A,P,P,P)→
  (P,A,P,P), resid 0) and outside A_min. The steelman conclusion (no A_min enrichment
  selects an axis) holds.
- **Required fix:** reword note (and runner E2/E8 PASS labels) from "S4-isotropic"
  to "trivial joint stabilizer → symmetric (non-selecting) breaking of W." The
  conclusion "selects no axis" is correct; the *reason* stated is wrong for E2/E8.
- **Scope honesty: GOOD.** The even-extent boundary is explicitly recorded (odd
  L=(3,3,3,3) falsifier returns resid 6.0; note section "Even-extent scope boundary").
  The S4-transitivity certificate is correctly scoped to even extent, not overclaimed.

---

### Could the audit lane complete any of these from standard math (performativity check)?
- N2b (dimensional analysis: no inverse-time observable) and N4-AUT (signed
  hyperoctahedral B_4 stabilizer computation) are arguably standard-math reachable in
  outline, but each is anchored to the framework's specific supplied objects (the
  blocked-time T̂², the staggered-Dirac M_KS, GATE-S/GATE-R). They are not performative:
  they answer "does the framework's *own* surface escape the wall," which standard math
  cannot answer without those primitives.
- N5 and N4-REGDIR are framework-specific (supplied T̂², record axiom, W certificate)
  and not standard-math substitutable.

### Block-level claim: "N1 ≥5-route enumeration and N7 steelman weak points are honestly closed"
- **N1: JUSTIFIED with one caveat.** Four distinct, genuinely-built route mechanisms
  now back the enumeration (source-surface transfer irreducibility; LR causal-cone
  monotone; joint two-rate-gate unit-pinning; full-automorphism-group enrichment
  search). These are mechanistically distinct, not relabelings. A consolidated B-AXIS
  no-go is NOT premature on enumeration count.
- **N7: JUSTIFIED.** The four strongest pro-derivation moves were built and falsified
  (or relocated), not deferred. The N4-AUT steelman in particular is the real article
  (full 384-element group, includes a-priori-risky enrichments).
- **Caveat:** none of the four is "superficial," but the N4-AUT note prose currently
  *misdescribes* its own strongest negative result (E2/E8 trivial stabilizer mislabeled
  S4-isotropic). That is a presentation defect that, if carried verbatim into a
  consolidated no-go, would understate how aggressively A_min enrichments disturb W and
  could invite a later "but you said isotropic" challenge. Fix the wording before
  consolidation cites it.

### Required fixes before the note is cited by a consolidated no-go
1. N2b: replace the vacuous self-comparison (line 267) and the hardcoded-`True`
   conclusion (line 281) with real checks or demote to comments.
2. N4-AUT + note: correct "S4-isotropic" → "trivial joint stabilizer / symmetric
   non-selecting W-breaking" for E2 and E8.
3. N5 note prose: align "no-go for N5" wording with the runner's correct
   "N5 exclusion FAILS / second clock not excluded by A_min."

None of these is a crack; none changes any outcome or the disposition.

### Block02 consolidation: MAY PROCEED
with the three wording fixes folded in. No premature no-go; no overstated crack; no
load-bearing hidden import.

---

## Block 02 review (adversarial — unified no_go note)

**Reviewer role:** HOSTILE independent auditor (attempting to REJECT the consolidated
no_go as premature / overbroad / improperly grounded).
**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block02-20260620` (HEAD 1384247ea)
**Deliverable under review:**
- `docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`
- `scripts/single_clock_baxis_obstruction_unified_2026_06_20.py`
- `.claude/science/physics-loops/single-clock-baxis-wall/CLAIM_STATUS_CERTIFICATE_block02.md`

**Runners re-run live with python3 (all reproduce the claimed counts):**
- consolidated `single_clock_baxis_obstruction_unified_2026_06_20.py` → **PASS=27 FAIL=0**
  (matches note line 21 / certificate line 7).
- absorbed `single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` → **PASS=17**
- absorbed `single_clock_n5_irreducibility_factor_clock_2026_06_20.py` → **PASS=36**
- absorbed `single_clock_n2b_joint_clock_unit_check_2026_06_20.py` → **PASS=18**
- absorbed `single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` → **PASS=20**
- Aggregate of the four absorbed = **91/91 FAIL=0**, matching the note (line 25 / 724)
  and certificate (line 9). NOTE: block01 review re-ran two of these at 16/17 (aggregate
  89); they are now 17/18 (aggregate 91). This is a CONSISTENT, BENIGN delta — see
  Finding A: the block01 required fixes were applied and ADDED real discriminating
  sub-checks, raising the counts rather than (as block01 review predicted) lowering them.

### DISPOSITION: `passed_with_notes`

I tried hard to reject this note and could not. The headline facts are genuinely
computed (not asserted), the three walls are independent, no load-bearing hidden import
was found, scope is honestly confined to the even-extent surface, source-discipline is
clean, and status hygiene holds. The block01 required fixes were folded in. I could not
name a plausible un-tried A_min-internal route. Findings below are honesty/precision
notes, none of which changes any outcome or blocks shipping to the audit lane.

---

### Axis 1 — PREMATURE NO-GO (N1/N7): could NOT reject

- **Route counts are real, not padding.** N4 = 12, N5 = 6, N2b = 5 (note §8 N1).
  Spot-checking the N4 column, the routes are mechanistically distinct (OS/GNS transport;
  durability monotonicity; cone circularity; anomaly count-not-label; KMS/APBC covariance;
  APBC-alone falsified-by-symmetric-restoration; non-transportable BC datum; reality/CPT
  W-inertness; Wilson labeled-choice; crossing-link/cocycle isotropy; full-automorphism
  enrichment search; derived registration-direction bridge). These are not relabelings of
  one another — they attack different candidate anchors.
- **Steelman (N7) is REAL, built and falsified by computation, not strawmanned.** The
  N4-AUT steelman computes the FULL 384-element B₄ group by BFS-solving the Z₂ sign field
  per relabeling (runner build_G_bare, lines 192-212) — confirmed a genuine enumeration,
  not an assertion — and includes a-priori-risky enrichments (E2 cubic Laplacian, E8
  face-diagonal graph) that *could* have broken symmetry asymmetrically. N5-IRR builds the
  framework's OWN supplied `T̂²` and falsifies both irreducibility and gauge. N2b-JOINT
  builds the strongest single-clock coupling (`K=exp(2a_τ Q)`) most likely to
  over-determine `a_τ`. All three are the strongest hostile pro-derivation moves.
- **Un-tried route hunt — FAILED to find one.** I probed the most plausible omission: a
  **Perron-Frobenius / transfer-contraction-direction selector** (the axis along which the
  transfer operator is a strict contraction vs the spatial directions). It is subsumed:
  building the transfer matrix presupposes the cut, and W transports the OS half-space
  package — reflection, one-particle kernel `W M⁻¹ Wᵀ = M⁻¹` (resid ~2.7e-15), spectra,
  positivity — to any axis with resid 0 (note §5.3 route 1). I could name no A_min-internal
  route the note did not consider. **The "premature no-go" objection FAILS.**

### Axis 2 — RUNNER HONESTY: facts COMPUTED, one assert-by-group-theory nuance

- **N5 factorization (§6, runner section_N5) is genuinely computed:** Stone identity
  `T̂²=exp(-2a_τĤ)` resid 3.14e-17; pairwise commutation resid 0.00e+00; generator-span
  rank = 3 = L_s (real `matrix_rank`); n_0 escapes span{I,Ĥ} resid 1.319 (>1e-6, a real
  least-squares residual). Not hardcoded.
- **N2b (runner section_N2) is computed and DISCRIMINATING:** joint-rescale invariance
  max Δ 2.37e-16 vs malformed rescaling move 1.567 — the discriminator proves the gauge
  zero is a real computed fact, not a built-in identity. Thresholds are NOT vacuously
  loose: every `< 1e-9/1e-12` exact-zero check fires against actual residuals of 0 or
  ~1e-17, and every `> 1e-6/> 1.0` break check fires against actual 22.6 / 11.3 / 8.0 /
  6.0 / 1.319 / 1.567.
- **FINDING B (minor, runner-honesty nuance — N4 S₄-transitivity).** The consolidated
  runner's transitivity PASS (line 141) checks only that the three ADJACENT exchanges
  (0,1),(1,2),(2,3) preserve the hop (resid 0), then ASSERTS in a comment "adjacent
  transpositions generate S_4 -> orbit is all four axes." I independently verified that the
  bare NON-adjacent signed exchanges do NOT preserve the hop ((0,2) resid 27.7, (0,3) 32.0,
  (1,3) 27.7), so transitivity is NOT a direct one-step fact — it rests on the group-theory
  generation lemma. I then verified the lemma holds on this surface: the COMPOSITION
  W01·W12·W01 (realizing the (0,2) transposition) preserves the hop with resid 0.00e+00.
  So the conclusion is TRUE and the absorbed R-N4-AUT runner computes the full group
  explicitly. The nuance: the consolidated runner *imports a math lemma* rather than
  computing the composed symmetry. This is sound (the lemma is standard and the absorbed
  runner backs it) but the consolidated runner would be strictly stronger if it checked one
  composed non-adjacent exchange. NOT load-bearing for the no-go; OPTIONAL hardening.

### Axis 3 — WALL-INDEPENDENCE (N2): walls are genuinely THREE

N2b (a missing *unit*, gauge `a_τ→c·a_τ`), N4 (a missing *label*, gauge = the S₄ orbit),
N5 (a missing *factor count*, gauge = the L_s-dim factor span) are mutually independent:
supplying the axis (N4) leaves `a_τ` rescaling free (N2b) and the commuting factor clocks
present (N5); none is a corollary of another. The note does NOT inflate the obstruction
count. Note §8 N2 table is accurate.

### Axis 4 — HIDDEN IMPORT (N3): none load-bearing in the wrong direction

The only physics on the load-bearing surfaces is the staggered-Dirac object itself
(dispersion `E(p)=arcsinh(√(m²+sin²p))`, the supplied `T̂²`, the staggered hop `M_KS`),
which is the retained (R-RP2)/(R-SC2)/(R-CL3) surface the no-go is explicitly ABOUT. The
note discloses this exactly (§8 N3: "the one place physics could be smuggled is the
staggered-Dirac surface itself; but it is the retained object"). The N5 factorization is
used to show A_min FAILS to exclude a second clock (a negative, no-go-SUPPORTING use), not
to derive anything. No supplied generator/metric/observed-value is load-bearing in a
derivation direction.

### Axis 5 — SCOPE OVERREACH (N5): honestly confined, NOT an impossibility proof

Every exact-zero is bounded to even cubic-symmetric staggered-Dirac blocks; the odd-L
falsifier `‖W M Wᵀ − M‖ = 6.000` at (3,3,3,3) is recomputed live (runner [SCOPE], confirmed
resid 6.000) and carried in the prose (note §10.1, §7). The note repeatedly states it is a
"no-go ABOUT the retained surface, NOT a framework-wide impossibility proof" (lines 5-9,
42, 499, 670-673) and carves out off-surface dimension-selection as axiomatic. Correctly a
no-go-about-the-retained-surface.

### Axis 6 — SOURCE DISCIPLINE: clean

- NO load-bearing edge to the conditional parent keystone
  (`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`), the
  unaudited finite-speed cone note, or the downstream ANOMALY_FORCES_TIME consumer. The
  [SRC] runner block machine-asserts this and the regex guard for
  "derived from ... anomaly_forces_time" returns 0 violations (verified live).
  ANOMALY_FORCES_TIME appears only inside the §11 disclaimer.
- Authorities it DOES lean on are verified `retained_no_go` in `docs/audit/AUDIT_LEDGER.md`:
  `single_clock_kms_apbc_axis_supplier_no_go_note_2026-06-16` (retained_no_go, Class A,
  cross_family) and `single_clock_uniqueness_scope_boundary_2026-06-06` (retained_no_go,
  Class A, fresh_context). The unified note is correctly NOT yet in the ledger
  (AUDIT_LEDGER_WRITTEN=FALSE).

### Axis 7 — STATUS HYGIENE: holds

`proposal_allowed=false`, `bare_retained_allowed=false`,
`audit_required_before_effective_retained=true`, and "independent audit lane is the sole
status authority" all present (note lines 10-12, 43-44, 646, 659, 771-772; certificate
lines 23-26). The one "retained" token in the **Status:** line (line 7) is the adjective
"the retained ... surface" (the retained reconstruction surface), NOT a bare status
assertion — acceptable. No audit-lane / publication file was modified (git status shows
only branch-local science files + the three deliverables).

### Finding A (benign PASS-count delta vs block01 review)

Block01 review flagged two cosmetic-PASS blemishes in the n2b runner (vacuous
self-comparison; hardcoded `True`) and predicted demoting them would DROP the PASS count
by ≤2. The fixes were instead applied by REPLACING them with real discriminating checks
(count-gauge dev computed under actual rescaling 2.2e-16; malformed-dev discriminator
0.50; explicit "every invariant observable is dimensionless / every 1/time quantity moves
only via the hand-inserted a_τ"), which RAISED n2b PASS 17→18 and n4_aut 16→17. I verified
the new checks are genuine computations, not new hardcodes. The block01 "S4-isotropic"
wording fix is also folded in (E2/E8 now "trivial-joint (symmetric W-break)" in both note
table §5.2 and runner labels). All three block01 required fixes are satisfied.

### Required fixes before block03

- **NONE blocking.** The note is shippable as a `no_go` to the audit lane as-is.
- **OPTIONAL hardening (Finding B):** add one composed-non-adjacent-exchange check
  (e.g. W01·W12·W01 preserves the hop, resid 0) to the consolidated runner's [N4] block so
  S₄-transitivity is computed rather than imported as a generation lemma. The absorbed
  R-N4-AUT runner already computes the full group, so this is belt-and-suspenders, not a
  correctness gap.

### Shippability verdict

The note is a sound, honestly-scoped `no_go` (negative_route_pruning over B-AXIS
N2b/N4/N5, plus the N2a exact-support pin). It is **shippable to the audit lane** as a
branch-local review artifact. The independent audit lane remains the sole status authority;
this review sets no status.

## Block 03 review (firewall widening — local spot-check)

**Disposition: pass.** Block 03 is a mechanical consumer-firewall-coverage block;
the heavy adversarial review was applied to the block02 no_go note it cites. Local
checks: (1) all 11 consumer-doc edits verified PURELY ADDITIVE via
`git diff --numstat` (insertions only, 0 deletions); (2) coverage runner
`single_clock_baxis_consumer_firewall_coverage_2026_06_20.py` reproduces PASS=34
FAIL=0; (3) inserted B-AXIS-premise blockquotes cite the unified obstruction note
and correctly state B-AXIS is consumed as a declared premise, not derived;
(4) the 9 already-firewalled docs were NOT re-edited (conflict avoidance with the
unmerged firewall branch) and are flagged repoint-to-unified-pending-integration;
(5) no forbidden audit-lane/publication file touched. Triage method sound (reverse
dep-edge BFS over the read-only ledger; 24 direct / 960 cone matches the ~959 target).
