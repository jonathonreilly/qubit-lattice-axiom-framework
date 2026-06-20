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
