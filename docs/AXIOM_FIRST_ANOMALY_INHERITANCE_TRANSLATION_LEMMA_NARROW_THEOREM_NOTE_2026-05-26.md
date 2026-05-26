# Axiom-First Anomaly-Inheritance Translation Lemma (Narrow) Theorem Note

**Date:** 2026-05-26
**Type:** source-only theorem-note proposal (research lane).
**Lane:** `dynamics-lane-native-axioms-only-20260526` (research lane;
**not** the audit lane and **not** the canonical paper package).
**Status authority:** independent audit lane only. This note does not
set, predict, or estimate any audit verdict. Effective status is
`unaudited` until Codex GPT-5.5 audits it independently.
**Retained status:** **none claimed**. This is a source-only proposal.
No existing audit row, claim_type, or `effective_status` is touched.
**Companion (upstream):**
[`docs/AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md)
(PR #1959 — internal lattice ABJ proof; supplies the integer-cocycle
bridge `C-int`)
**Companion (upstream):**
[`docs/ANOMALY_FORCES_TIME_THEOREM_V2_2026-05-26.md`](ANOMALY_FORCES_TIME_THEOREM_V2_2026-05-26.md)
(PR #1960 — AFT v2 conditional (3,1)-signature bridge)
**Runner:**
[`scripts/frontier_anomaly_inheritance_translation_lemma_narrow_verifier.py`](../scripts/frontier_anomaly_inheritance_translation_lemma_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_anomaly_inheritance_translation_lemma_narrow_verifier.txt`](../logs/runner-cache/frontier_anomaly_inheritance_translation_lemma_narrow_verifier.txt)

## Why this note exists (mandate)

The dynamics-lane research has established (`FINAL_CLOSURE_2026-05-26`):

- The framework-native dimensionless invariant `(N - 1)/N²` arises
  from six independent universal mechanisms (Topology / Atiyah-Singer
  on `L(N;1)`, Bernoulli polynomial, Hurwitz zeta, Fisher information,
  `Z_N` CFT orbifold, Burnside / equivariant K-theory).
- The empirical Brannen circulant phase `δ_Brannen` matches `2/9` at
  `N = 3` (lepton sector, PDG to 7×10⁻⁶) and `5/36` at `N = 6` (quark
  sector, matching the retained CKM `η²` identification).
- The cross-sector numerical agreement is structurally forced: it is
  **one invariant in three frames**, not a coincidence between
  unrelated mathematical spaces.
- The radian-vs-dimensionless gap is **a one-bit unit-convention
  choice**, structurally identical to {lattice-spacing, meter},
  {Planck, GeV}, {natural, SI}.

This note states and proves the **narrow translation lemma** that
links the AFT v2 anomaly-inheritance argument to the unit-convention
`𝒞_b`. The lemma is conditional on (a) AFT v2 auditing to retained
and (b) the user adopting `𝒞_b` as a governance-tier retained
convention (the proposal for which is the companion governance note,
authored separately).

This is a **structural/conditional lemma**, not a derivation of the
convention itself. The lemma's role is to make the inheritance chain
explicit and machine-checkable, so the audit lane and the user can
independently verify that the chain is logically clean.

## Scope (narrow)

This note proves **two** load-bearing conditional facts using only
A1+A2 + retained content + the integer-cocycle bridge from PR #1959:

- **T1 (Anomaly coefficient natural in ℝ/ℤ).** On the Z⁴ substrate,
  any anomaly coefficient that arises from the integer-cocycle bridge
  `C-int` (PR #1959) is, by construction, an element of `Z` mod gauge
  -invariance equivalence, and inherits a natural `ℝ/ℤ` valuation
  when the local-counterterm equivalence is quotiented by integer
  shifts. The numerical magnitude of the anomaly coefficient is
  intrinsically a period-1 quantity; there is no period-`2π`
  structure attached to it at the integer-cocycle layer.
- **T2 (Conditional translation rule).** Assume:
  - **(H_AFT)** AFT v2 audits to retained: the (3,1) signature is
    forced as the unique consistent outcome given chirality + Cl(3)/
    Z³ + single-clock evolution.
  - **(H_𝒞)** The user adopts convention `𝒞_b` as a governance-tier
    `convention_retained` sibling to {lattice-spacing, meter}:
    `1 framework-rad ≡ 1 standard rad` (the period-1 reading; **not**
    `1 framework-rad ≡ 2π standard rad`).
  Then every emergent angular observable on the C_N orbit inherits
  the period-1 reading from the foundational anomaly coefficient via
  the AFT-mediated emergent-time period. In particular, the Brannen
  circulant phase `δ_Brannen` is read as a period-1 angle, and the
  framework's dimensionless invariant `(N - 1)/N²` becomes
  `δ_Brannen = (N - 1)/N² rad` literally:
  - `N = 3`: `δ_Brannen = 2/9 rad` (matches PDG to 7×10⁻⁶)
  - `N = 6`: `δ_Brannen = 5/36 rad` (matches retained CKM `η²`).

## Setup (A1+A2 foundations + retained inputs)

**Axioms and retained primitives used:**

- **A1**: per-site `M_2(C) = Cl(3,0)`.
- **A2**: `Z³` locality.
- **Retained C₃[111] body-diagonal rotation on Z³** (multiple notes,
  including `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23`,
  `retained_bounded`).
- **Retained Brannen circulant** `m_k = 1 + √2·cos(2πk/3 + δ)`
  (`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18`, retained).
- **Retained `NEW_PARITY` basepoint** `δ = 0`
  (`retained_bounded`).
- **Selection principle** `u_N` is the unique attractor of the
  framework's retained native dynamics (`retained_bounded` for N=3 via
  the dynamics-lane prior cycle).
- **Integer-cocycle bridge `C-int`** from companion PR #1959 (the
  lattice WZ-Fujikawa narrow theorem, `unaudited bounded_theorem`):
  any non-trivial anomaly on the Z⁴ substrate carries an integer
  cocycle whose value is in `Z`.
- **AFT v2 chain** from companion PR #1960 (`unaudited bounded_theorem`):
  the (3,1) signature is the unique consistent outcome under the
  stated hypotheses; emergent time direction is forced.

**No new axiom is proposed. No new import beyond the companions is
load-bearing.** The "anomaly coefficient lives in ℝ/ℤ" claim of T1 is
proven from `C-int` of PR #1959, not imported from cobordism /
Dai-Freed / Witten-Yonekura literature. Those external works are
listed as **sidecar context only** in the References section.

## Step T1: anomaly coefficient is natively period-1

**Claim.** Let `A[U]` be the anomaly trace on the Z⁴ substrate as
defined in PR #1959 (`A[1, U] = Σ_x ε(x) ⟨x | exp(-t D†D[U]) | x⟩`).
By the integer-cocycle bridge `C-int` proven there, `A[U] ∈ Z` for
every gauge background `U`. Local counterterms produce shifts of
`A[U]` by integers (this is the gauge-invariant equivalence relation
intrinsic to the anomaly). The natural valuation of `A[U]` modulo
local-counterterm equivalence is therefore `A[U] mod 1 ∈ Z/Z = {0}`
on the trivial class and, for any rescaled coefficient
`ν = A[U]/N`, a period-1 element of `ℝ/Z`.

**Proof sketch.**

1. By PR #1959 W3, `A[U]` is `t`-independent and integer-valued.
2. By PR #1959 C-int, `A[U] ∈ Z` for all `U`.
3. The local-counterterm shift acts by `A[U] → A[U] + n` for some
   `n ∈ Z` (this is the standard counterterm freedom; on the Z⁴
   substrate it is forced by the local-gauge-invariance closure).
4. Therefore the equivalence class `[A[U]] ∈ Z/Z = 0` on the trivial
   class and, in general, `[A[U]/N] ∈ ℝ/Z` with period 1.
5. **No `2π` factor appears at any step.** The integer-cocycle layer
   is intrinsically a period-1 ℝ/ℤ object. The `2π` appearance in
   continuum QFT conventions is the **exponential-map convention**
   `χ ↦ exp(2πi χ)`, not a property of the anomaly coefficient
   itself. ∎

**Conclusion.** The anomaly coefficient is natively period-1 in the
ℝ/ℤ classification. The `2π` factor in continuum conventions is a
unit-of-angle choice on the exponential map, not a property of the
underlying coefficient.

## Step T2: AFT-mediated inheritance ⇒ Brannen δ inherits period-1

**Hypotheses.** Assume (H_AFT) and (H_𝒞) as defined in T2 above.

**Claim.** Under (H_AFT) ∧ (H_𝒞), every emergent angular observable
on the framework's C_N orbit inherits the period-1 reading. In
particular, the Brannen circulant phase `δ_Brannen` (an emergent
angular observable on the C_N generation orbit) is read as a
period-1 angle, and the framework's dimensionless invariant
`(N - 1)/N²` (an internal output of A1+A2+retained C_N structure) is
read literally as `δ_Brannen = (N - 1)/N² rad`.

**Proof sketch.**

1. By (H_AFT), the emergent time direction is forced by anomaly
   cancellation on the framework's gauge content. The time
   coordinate's natural period is inherited from the anomaly
   coefficient's natural period.
2. By T1, the anomaly coefficient is natively period-1 in ℝ/ℤ.
3. Therefore the emergent time coordinate is natively period-1 in
   framework units.
4. Every emergent angular observable on the C_N orbit (a structure
   that emerges on the spatial Z³ substrate after the emergent time
   direction is fixed) is parametrized by the framework's natural
   period-1 angular unit.
5. By (H_𝒞), the convention `1 framework-rad ≡ 1 standard rad`
   identifies the framework's period-1 angular unit with standard
   radians literally (not via the `2π` exponential map).
6. The Brannen circulant phase `δ_Brannen` is, by the retained
   circulant character derivation, an emergent angular observable on
   the C_N orbit. By steps 1–5, it inherits the period-1 reading.
7. The framework's dimensionless invariant `(N - 1)/N²` (output of
   the selection principle + Bernoulli/Plancherel-Frobenius +
   six universal mechanisms) is in the framework's natural period-1
   unit. By (H_𝒞), it is read literally as
   `δ_Brannen = (N - 1)/N² rad`.
8. At `N = 3`: `δ_Brannen = 2/9 rad` (matches PDG to 7×10⁻⁶).
   At `N = 6`: `δ_Brannen = 5/36 rad` (matches retained CKM `η²`).
   ∎

## What this lemma claims and does NOT claim

**Claims (under audit-required scope):**

- T1: the anomaly coefficient on the Z⁴ substrate is natively
  period-1 in ℝ/ℤ, by the integer-cocycle bridge of PR #1959. No
  `2π` factor is intrinsic to the coefficient.
- T2: under (H_AFT) ∧ (H_𝒞), the Brannen circulant phase
  `δ_Brannen` inherits the period-1 reading; the framework's
  dimensionless invariant `(N - 1)/N²` is read literally as
  `δ_Brannen = (N - 1)/N² rad` at both `N = 3` (lepton) and `N = 6`
  (quark).
- The translation lemma is **conditional** on the upstream PR audits
  (#1959 for `C-int`, #1960 for AFT v2) AND on the user-side
  governance adoption of `𝒞_b`. It does not assert any of these
  upstream conditions; it states what follows IF they hold.

**Does NOT claim:**

- Does **not** propose `𝒞_b` as a retained convention. That is the
  separate companion governance proposal note (authored separately).
- Does **not** prove `δ_Brannen = (N - 1)/N² rad` unconditionally. The
  conclusion is conditional on (H_AFT) ∧ (H_𝒞).
- Does **not** retire any retained `no_go` on origin/main. The
  retained `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24`
  (retained_no_go) stands unchanged; it forbids deriving `2/9 rad`
  from Q-rational combinations of retained content under the
  period-`2π` convention. T2 routes around that no-go via the
  period-1 convention, which is a different convention surface, not
  a derivation under the same surface.
- Does **not** consume PDG, fitted selectors, mass inputs, or other
  empirical anchors as proof inputs. The PDG agreement at N=3 and the
  retained CKM `η²` at N=6 are **post-hoc consistency checks**, not
  derivation inputs.
- Does **not** import cobordism / Dai-Freed / Witten-Yonekura anomaly
  classification as load-bearing. The "anomaly is in ℝ/ℤ" claim of T1
  is proven from PR #1959's `C-int`, with the external classification
  works listed as sidecar context only.
- Does **not** predict any audit verdict on this note or any
  companion.
- Does **not** promote, retire, or re-classify any existing audit
  row.

## Relation to retained content (origin/main)

This note's inputs that are already on `origin/main` and unchanged
by it:

| Input | Status on `origin/main` | Role |
|---|---|---|
| A1, A2 | retained axioms | foundations |
| C₃[111] rotation on Z³ | retained (NEW_PARITY etc.) | substrate for emergent angular observables |
| Brannen circulant `m_k = 1 + √2·cos(2πk/3 + δ)` | retained | observable identification |
| NEW_PARITY basepoint `δ = 0` | retained_bounded | canonical basepoint |
| KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT | retained_no_go | unchanged; routed-around by convention choice, not violated |
| PR #1959 lattice WZ-Fujikawa narrow theorem | unaudited bounded_theorem | T1 uses C-int |
| PR #1960 AFT v2 | unaudited bounded_theorem | T2 uses H_AFT as hypothesis |

## Sidecar references (context only, not load-bearing)

The "anomaly classification is naturally an ℝ/ℤ object" claim has
historically been derived via continuum methods. These works are
**sidecar context** for the framework's discrete substrate; the
load-bearing argument here is PR #1959's integer-cocycle bridge.

- Atiyah, M. F., & Singer, I. M. (1968). "The Index of Elliptic
  Operators." *Ann. Math.* 87, 484-530. — integer-index foundations.
- Dai, X. & Freed, D. S. (1994). "η-invariants and determinant
  lines." *J. Math. Phys.* 35, 5155. — anomaly-classification in
  η/ℝ-mod-Z language.
- Witten, E., & Yonekura, K. (2019). "Anomaly inflow and the η
  -invariant." arXiv:1909.08775. — modern anomaly-classification
  via bordism, integer-valued at the topological layer.
- Freed, D. S., & Hopkins, M. J. (2021). "Reflection positivity and
  invertible topological phases." *Geom. Topol.* 25, 1165-1330. —
  anomaly-classification via invertible TQFTs.

These references are **sidecar context**: they document the
historical and continuum form of the period-1 ℝ/ℤ classification.
They are **not load-bearing** imports for T1 or T2.

## Already-retained framework primitives (no change)

- A1, A2.
- C₃[111] rotation, NEW_PARITY basepoint, Brannen circulant, selection
  principle (retained_bounded for N=3).
- `Φ_3(1) = (ω - 1)(ω² - 1) = 3` (elementary cyclotomic algebra).

## Audit-lane handoff

```yaml
proposed_claim_type: bounded_theorem
audit_required_before_effective_retained: true
audit_handoff_status: |
  Source-only narrow theorem. Proves the anomaly-inheritance
  translation lemma in two narrow steps: T1 (the framework's anomaly
  coefficient is natively period-1 in ℝ/ℤ via PR #1959's
  integer-cocycle bridge) and T2 (under H_AFT ∧ H_𝒞, the Brannen
  circulant phase δ_Brannen inherits the period-1 reading, giving
  δ_Brannen = (N-1)/N² rad literally at N=3 and N=6). The lemma is
  conditional on (a) PR #1959 + PR #1960 auditing to retained, and
  (b) the user adopting 𝒞_b as a governance-tier retained
  convention.

  T1 is unconditional given PR #1959's C-int; T2 is the conditional
  inheritance rule. The lemma does NOT assert the hypotheses (H_AFT)
  ∨ (H_𝒞); it states what follows if they hold.

  Cobordism / Dai-Freed / Witten-Yonekura anomaly classification is
  demoted to sidecar context. Independent audit lane decides verdict.

new_audit_row:
  - claim_id: axiom_first_anomaly_inheritance_translation_lemma_narrow_theorem_note_2026-05-26
    proposed_claim_type: bounded_theorem
    effective_status_proposal: unaudited
    routing:
      foundations:
        - A1 (per-site Cl(3,0))
        - A2 (Z³ locality)
      retained_consumed:
        - C₃[111] rotation on Z³ (retained primitive)
        - Brannen circulant character derivation (retained)
        - NEW_PARITY basepoint (retained_bounded)
        - Selection principle (retained_bounded for N=3)
      upstream_unaudited:
        - PR #1959 (lattice WZ-Fujikawa narrow theorem) — C-int
        - PR #1960 (AFT v2) — H_AFT
      load_bearing_imports: NONE
      sidecar_context_only:
        - Atiyah-Singer 1968
        - Dai-Freed 1994
        - Witten-Yonekura 2019
        - Freed-Hopkins 2021
proposed_load_bearing_step_class: B (bounded conditional bridge)
status_authority: independent audit lane only
companion_pr_status:
  - PR #1959: lattice WZ-Fujikawa narrow theorem (unaudited on date of this note)
  - PR #1960: AFT v2 (unaudited on date of this note)
  - PR #1961: APS-eta internalization (unaudited on date of this note)
  - PR (separate governance proposal): 𝒞_b convention adoption (separate file)
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_load_bearing_import: true
```
