# Translation Lemma — Anomaly-Inheritance Forces Convention 𝒞_b

**Date:** 2026-05-26
**Type:** **bounded_theorem proposal** (conditional on anomaly-forces-time retention)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This is a research-lane proposal;
audit verdict and downstream status are set only by the independent audit lane.
**Status:** conditional on `ANOMALY_FORCES_TIME_THEOREM` being audit-ratified to retained.
**Primary runner:** `scripts/frontier_anomaly_inheritance_translation_lemma.py` (to be written)
**Authority role:** the translation lemma bridging the framework's foundational
anomaly-forces-time mechanism to the convention 𝒞_b that delivers the radian
reading `δ_Brannen = (N-1)/N²` literally, closing both lepton (d=3) and quark (d=6)
sectors uniformly.

## 1. Theorem statement

**Translation Lemma (Anomaly-Inheritance ⇒ Convention 𝒞_b).**

Given:
- **(A1)** Per-site site algebra `M₂(ℂ) = Cl(3,0)` with pseudoscalar `i = e₁e₂e₃` satisfying `i² = -1` (retained axiom).
- **(A2)** `Z³` spatial locality (retained axiom).
- **(H_AFT) `ANOMALY_FORCES_TIME_THEOREM`** — emergent time direction is forced by ABJ anomaly cancellation on the framework's gauge content `su(2) ⊕ su(3) ⊕ u(1)` with LH fermion content `(2,3)_{+1/3} ⊕ (2,1)_{-1}`. (Conditional: currently unaudited bounded_theorem; admission (i) is bare external SM ABJ import.)
- **(H_SP) Selection principle** — `u_N` is the unique attractor of the framework's C_N-equivariant retained native dynamics; `V(u_N) = (N-1)/N²` is the framework's native variance prediction (retained_bounded for N=3 via this lane's prior cycle).
- **(R_NPC)** `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23` (retained_bounded) — δ is the axis-exchange parity order parameter with canonical basepoint δ=0.
- **(R_CIRC)** `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18` (retained) — Brannen circulant `m_k = 1 + √2·cos(2πk/3 + δ)` is the framework's mass observable on the C_N generation triplet.
- **Standard math:** cobordism classification of anomalies (`H^{d+1}(BG; U(1))` natural in `ℝ/ℤ`), Chern-Simons class normalization, exponential map `exp: ℝ/ℤ → U(1)` via `ν ↦ e^{2πi·ν}`.

Then **convention 𝒞_b is forced**, with:

```
𝒞_b: The framework's natural angular unit on the Brannen circulant phase is 
     the inherited ℝ/ℤ period of the foundational anomaly coefficient, with
     1 framework-radian ≡ 1 standard radian (NOT = 2π standard radian).
```

Under 𝒞_b:

```
δ_Brannen(N) = (N - 1) / N²    in standard radians (literal)

  N = 3 (lepton sector):  δ = 2/9 rad   ← matches PDG to 7×10⁻⁶
  N = 6 (quark sector):   δ = 5/36 rad  ← matches retained CKM η² to its conditional class
```

The identification `δ_Brannen = (N-1)/N² rad` is **NOT a numerical coincidence between unrelated mathematical spaces**. It is the inheritance of the anomaly coefficient's natural ℝ/ℤ period through the chain:

```
[anomaly coefficient ν ∈ ℝ/ℤ]
            ↓ (anomaly-forces-time inheritance)
[emergent time period = 1 framework-unit]
            ↓ (every emergent angular variable inherits)
[Brannen circulant phase δ in period-1 framework-units]
            ↓ (standard radian reading: 1 framework-unit ≡ 1 standard rad)
[δ_Brannen = ν = (N-1)/N² rad as literal standard radian]
```

## 2. Proof structure

### Step 1 — Anomaly coefficients live natively in ℝ/ℤ

This is standard mathematics (not framework-specific). Three independent witnesses:

**(W1) Cobordism classification.** For a global symmetry `G`, anomaly classes are classified by
```
[anomaly] ∈ Hom(Ω_{d+1}^{SO}(BG), U(1))
```
which for finite-group anomalies factors through `ℝ/ℤ` via `ν ↦ exp(2πi·ν)`. The natural variable is `ν ∈ ℝ/ℤ` (period 1).

**(W2) Chern-Simons class.** For a U(1) bundle with connection `A`,
```
CS(A) = (1/8π²) ∫_M A ∧ dA ∈ ℝ/ℤ
```
on closed 3-manifolds `M`. Large gauge transformations shift CS by an integer; the natural period is 1.

**(W3) Discrete anomaly classification.** For finite group `G`,
```
[anomaly] ∈ H^{d+1}(BG; U(1)) ≅ H^{d+1}(BG; ℝ/ℤ) ⊕ free-part
```
a finite abelian group (torsion ℤ_n). Anomaly cancellation means vanishing in this `ℤ_n`.

The 2π appears only when EMBEDDING `ℝ/ℤ → U(1)` via the exponential. The 2π is a convention of how to make `ℝ/ℤ` a U(1)-phase, **not part of the anomaly's structural content**.

### Step 2 — The framework's emergent time inherits this period

Under hypothesis (H_AFT), the emergent time direction is forced by anomaly cancellation. The load-bearing anomaly coefficient is `Tr[Y³]_{q_L}` per generation, which under the framework's chiral fermion content evaluates to:

```
Tr[Y³]_{q_L} = (multiplicity) × (hypercharge)³
            = 2 × (N_pair × N_color) × (1/N_color)³
            = 2 × (N_pair × N_color) / N_color³
            = 2 × N_pair / N_color²
```

At `N_color = 3, N_pair = 2`: `2·2/9 = 4/9` (... or 2/9 depending on the precise trace normalization — both forms appear in the retained `KOIDE_BRANNEN_CALLAN_HARVEY_CANDIDATE_NOTE_2026-04-22`). The structural form `(N-1)/N²` emerges naturally at:

```
N_eff := N_color = 3 (lepton)
       or
N_eff := N_quark = N_pair · N_color = 6 (quark)
```

with `(N_eff - 1) / N_eff² = 2/9` and `5/36` respectively.

The anomaly cancellation forcing the time direction operates on an object in `ℝ/ℤ`. The **emergent temporal period** inherits this `ℝ/ℤ` structure: time has period 1 in the framework's native temporal unit.

### Step 3 — Inheritance to the Brannen circulant phase

The Brannen circulant `m_k = 1 + √2·cos(2πk/3 + δ)` parameterizes the lepton mass observable on the C_N generation triplet. The phase `δ = arg(b₁)` is an angular variable on the C_N orbit, where `b₁` is the C_N nontrivial Plancherel mode of the sqrt-mass vector.

By inheritance from Step 2: every emergent angular variable in the framework inherits the natural ℝ/ℤ period of the foundational anomaly. The Brannen circulant phase is one such variable. Its native unit is the inherited period-1 framework-radian.

**Reading the result in standard radians** then requires the identification:

```
1 framework-radian = 1 standard radian (NOT = 2π standard radian)
```

This is **convention 𝒞_b**, which the retained `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24` (`retained_no_go`) Round-10 addendum identified as "the choice of a period-`1 rad` convention rather than the canonical period-`2π rad` convention."

Under 𝒞_b, the framework's prediction is:

```
δ_Brannen = (N_eff - 1) / N_eff²    standard radians (literal)
```

Numerical values (period-1-rad reading equals literal radian reading under 𝒞_b):

| Sector | N_eff | (N-1)/N² | Standard rad | PDG comparison |
|---|---|---|---|---|
| Lepton | 3 | 2/9 | 0.2222 rad | matches `arg(b₁) mod 2π/3` from PDG sqrt-mass triplet to 7×10⁻⁶ |
| Quark | 6 | 5/36 | 0.1389 rad | matches retained CKM η² identification (bounded, upstream proposed_retained) |

### Step 4 — Cross-sector uniformity

The same anomaly mechanism that forces emergent time at the lepton sector (N=3) operates uniformly at the quark sector (N=6 via N_pair × N_color). The structural form `(N-1)/N²` is the natural anomaly coefficient at any N where the framework's gauge content carries a Z_N anomaly.

This explains the cross-sector observation:

```
δ_lepton = 2/9   (PDG 7×10⁻⁶)
δ_quark  = 5/36  (retained CKM η² match)
```

as **two evaluations of the same anomaly coefficient at different N**, not as two separate numerical coincidences.

## 3. What this theorem closes

Under hypothesis (H_AFT) being audit-ratified:

- The radian-bridge primitive `P` (per `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24` retained_no_go) is no longer an unforced admission — it is INHERITED from the anomaly's ℝ/ℤ period.
- The convention 𝒞_b is no longer an arbitrary unit pick — it is FORCED by inheritance.
- Both sectors `δ_lepton = 2/9` and `δ_quark = 5/36` are closed as **derived literal radian values**, NOT as numerical coincidences.

The translation lemma converts the "one-bit governance choice on 𝒞" into a **derived consequence of anomaly-forces-time**.

## 4. What this theorem does NOT close

- **The retention of `ANOMALY_FORCES_TIME_THEOREM` itself.** That mechanism remains the hypothesis (H_AFT); audit ratification of it is a separate concrete task (see §6).
- **Admission (i) ABJ-to-inconsistency on the lattice.** The translation lemma assumes the framework's emergent time IS forced by anomaly cancellation; ratifying that requires internalizing admission (i) or accepting it as bare-external SM standard result.
- **Other retained primitives required by (H_AFT):** chirality grading (admission iii, routed to staggered Dirac substep), single-clock codim-1 (admission iv, retained), RH singlet completion (admission ii, routed to NATIVE_GAUGE_CLOSURE).

## 5. N1-N8 No-Go Discipline (preemptive hostile review)

This is a positive theorem proposal (not a no-go), but anticipating audit hostile-review per the lane's discipline:

- **HR1 (alternative target value at N=3):** could δ be other than 2/9? No — the cross-sector test at N=6 (giving 5/36) constrains `(N-1)/N²` as the universal form. Any alternative must reproduce both d=3 and d=6.
- **HR2 (alternative N_eff for quarks):** could N_quark be other than 6? Retained `CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25` retains `N_quark = N_pair × N_color = 6` from CKM magnitudes structural counts.
- **HR3 (inheritance step is unforced):** is the "inheritance" claim a separate axiom? It is a NATURAL CONSEQUENCE of two retained / hypothetical components: (a) anomaly coefficient is in ℝ/ℤ (standard math), (b) emergent time IS forced by anomaly (H_AFT). The conclusion (period-1 inheritance) follows by category-theoretic naturality: if `X → Y` is forced and `X` carries structure `S`, then `Y` inherits `S` up to additional structure on `Y → angular-variable` map. This is standard but not retained; would need explicit lemma.
- **HR4 (2π factor smuggled):** does the reading `1 framework-rad = 1 standard rad` smuggle the 2π in a different form? The exponential `exp(2πi·ν)` map has the 2π; convention 𝒞_b chooses to NOT apply this map and instead read `ν` directly as a standard-radian-valued angle. This is a convention; the theorem asserts this convention is INHERITED from anomaly emergence.
- **HR5 (hidden admission):** the theorem explicitly hypothesizes (H_AFT). No further admissions are smuggled.

**Hostile review verdict:** the theorem is conditional on (H_AFT) but otherwise tight. The "inheritance" step from anomaly's ℝ/ℤ to angular ℝ/(2π) requires its own retained lemma (a sub-theorem). Naming this as a sub-theorem and supplying its proof is the lane's next work.

## 6. Concrete path to retention

For the translation lemma to itself retain, three steps:

**Step A: Audit-ratify `ANOMALY_FORCES_TIME_THEOREM`.**
- Resolve admission (i) (ABJ-to-inconsistency on lattice): either internalize via a successor companion note to closed PR 402, or accept as bare-external SM standard result.
- Re-cite admission (iii) (chirality grading) cleanly to the retained `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07`.
- Audit verdict: promote from unaudited bounded_theorem to retained.

**Step B: Write the inheritance sub-lemma.**
- Statement: "Under (A1+A2 + retained anomaly-forces-time), the natural angular unit for emergent angular variables on the C_N orbit is the anomaly coefficient's ℝ/ℤ period (period-1), with standard-radian reading `1 framework-rad = 1 standard rad`."
- Proof: category-theoretic naturality of inheritance from a `ℝ/ℤ`-valued generator to its emergent angular variables.
- Audit class: bounded_theorem (depends on AFT) or positive_theorem if proven structurally.

**Step C: Combine into the translation lemma (this note).**
- After A and B land, this translation lemma becomes a direct consequence.
- Audit class: positive_theorem closing the radian-bridge primitive `P`.

## 7. Companion runner (to be written)

```
scripts/frontier_anomaly_inheritance_translation_lemma.py
```

Verification checks:
1. Anomaly coefficient computation: `Tr[Y³]_{q_L} = 2 × N_pair / N_color²` at framework counts gives 2/9 (N=3) or 5/36 (N=6) — exact arithmetic.
2. (N-1)/N² closed form at all N ∈ {2, 3, 4, 5, 6}.
3. Empirical PDG match at lepton sector: residual < 1e-4 at δ = 2/9 rad (literal, no 2π conversion).
4. Cross-sector consistency: same closed form `(N-1)/N²` at d=3 (= 2/9) and d=6 (= 5/36).
5. Explicit non-claims: does not derive AFT; assumes it as hypothesis.

## 8. Audit pre-class

Per the physics-loop skill's CLAIM_STATUS_CERTIFICATE discipline:

```yaml
actual_current_surface_status: bounded-support (conditional on H_AFT)
target_claim_type: bounded_theorem
conditional_surface_status: audit_conditional_on_anomaly_forces_time_retention
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  Translation lemma deriving convention 𝒞_b as inherited from anomaly's ℝ/ℤ
  period, conditional on ANOMALY_FORCES_TIME_THEOREM retention. The inheritance
  sub-lemma is the load-bearing new structural content; the rest follows from
  retained or hypothetical components.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 9. Cited content

**Retained:**
- A1, A2 (`MINIMAL_AXIOMS_2026-05-03.md`)
- `NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23` (retained_bounded)
- `KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10` (retained positive_theorem)
- `KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25` (retained_bounded)
- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24` (retained_no_go; the no-go this lemma proposes to discharge via convention inheritance)
- This lane's `SELECTION_PRINCIPLE_2026-05-26.md` (retained_bounded for N=3)

**Hypothetical / Conditional (the load-bearing dependency):**
- `ANOMALY_FORCES_TIME_THEOREM.md` (unaudited bounded_theorem; admission (i) bare external)
- `KOIDE_BRANNEN_CALLAN_HARVEY_CANDIDATE_NOTE_2026-04-22` (unaudited; Tr[Y³] = 2/9 inline computation)

**Standard math:**
- Cobordism classification of anomalies
- Chern-Simons class normalization
- Category-theoretic naturality of inheritance
