# β₂/β₃ Are Scheme Convention; the Invariant Running Content Is Exactly the Bounded b₀/b₁ Set

**Date:** 2026-06-08
**Type:** bounded theorem (a demarcation/relocation of the L3/L4 "MS-bar structural gap")
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_beta23_scheme_convention_demarcation_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_beta23_scheme_convention_demarcation_2026_06_08.txt`
**Status:** source proposal. Everything is exact symbolic algebra (sympy; runner
`PASS=15 FAIL=0`). Authority role: source proposal; audit lane sets status.

## The wall this demarcates

The per-loop decomposition
([`ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop`](ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop.md))
found: **L1** (1-loop `b₀`) and **L2** (2-loop `b₁`) are algebraically available in the
bounded QCD-running context, while **L3/L4** (3-/4-loop `b₂, b₃`) *"require MS-bar
dimensional-regularization machinery … a structural obstruction."* This note demarcates
that obstruction **exactly**: the boundary between the bounded algebraic coefficient
content and the missing conversion dictionary coincides with the boundary between
**scheme-invariant** and **scheme-convention** content.

## What is proved (exact symbolic — runner `PASS=15 FAIL=0`)

Write `β(α) = −α²(b₀ + b₁α + b₂α² + b₃α³ + …)` and consider every
**normalization-preserving** coupling reparametrization
`α′ = α + c₁α² + c₂α³ + c₃α⁴ + …` (the standard scheme transformations; the inverse series
is solved exactly, order by order).

1. **(T1) Universality is *derived*, not asserted:** `b₀′ = b₀` and `b₁′ = b₁`
   **identically** — zero dependence on `(c₁, c₂, c₃)`.

2. **(T2) `b₂, b₃` are pure convention.** The exact laws
   `b₂′ = b₂ − b₁c₁ + b₀(c₂ − c₁²)` and
   `b₃′ = b₃ − 2b₂c₁ + b₁c₁² + b₀(2c₃ − 6c₁c₂ + 4c₁³)`
   contain the free parameters `c₂, c₃` **linearly** with coefficients `b₀` and `2b₀`. So
   for `b₀ ≠ 0` the pair `(b₂′, b₃′)` reaches **any prescribed values** — in particular
   `(0,0)`, the **'t Hooft scheme**, by an explicit linear solve, for *every* `c₁` (a
   one-parameter family of such schemes). At the framework point and `c₁=0`:
   `c₂ = −b₂/7`, `c₃ = −b₃/14` — exact rationals. The pair carries **no invariant
   content**.

3. **(T3) Asymptotic freedom is the solvability condition.** The solve's denominators are
   exactly `b₀` and `2b₀`; at `b₀ = 0` the `c₂/c₃` freedom drops out of `(b₂′, b₃′)`
   entirely (control included). The inherited QCD-running context has `b₀ = 7 > 0`, so
   this bounded context supplies the condition.

4. **(T4) The demarcation.** The retained-Casimir closed forms
   `b₀ = (11C_A − 4T_F N_f)/3 = 7` and `b₁ = (34/3)C_A² − 4C_F T_F N_f − (20/3)C_A T_F N_f
   = 26` (recomputed exactly, `N_f = 6`) coincide with the invariant set (T1). Within the
   inherited bounded QCD-running context, the algebraic coefficient content is exactly the
   reparametrization-invariant set; the L3/L4 gap consists of convention-side coefficients.

5. **(T5) Teeth.** `b₁` has identically zero `c`-dependence — the demarcation line sits
   exactly at `n ≥ 2` and cannot be moved. And a leading **rescaling** `α′ = λα` *does*
   change `b₀` (`→ b₀/λ`): that freedom is the separate `g_bare` **normalization**
   convention layer, excluded from scheme maps here and kept distinct (stated, not blurred).

## The relocation (what this means at fixed spacing)

On the framework's fixed-spacing baseline — the lattice is physical, and the spacing is
not removed — the coefficient-level invariant content is `(b₀, b₁)`. Reproducing the
**MS-bar labels** `β₂^{MS̄}, β₃^{MS̄}` is a **literature-comparison dictionary**:
the scheme-conversion structural form already exists
([`CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a`](CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a.md)
isolates the conversion to the two lattice integrals `Z₁₀, Z₂₀`), and those integrals are
the **named admission**. The honest restatement of L3/L4: *"a conversion dictionary
remains imported,"* not *"the invariant running content is structurally incomplete."*

## What this does NOT claim (boundary)

- **L3/L4 are NOT "closed."** The `α_s(M_Z)` certificate's imports — the conversion
  dictionary (`Z₁₀, Z₂₀`, **not computed here**), the running infrastructure, the
  thresholds, the Sommer scale — are **unchanged** and remain named admissions.
- The physical-color/QCD-coupling bridge, `g_bare` normalization, and other inherited
  gates of the parent `α_s` running context are not retired by this note.
- **Physical observables are scheme-invariant** as always; the demarcation is at the
  **coefficient** level (which coefficients carry invariant information).
- The sister `b₃` lane (`QCD_BETA_3_PURE_GAUGE_VS_FULL_SM`, the `N_f`-dependence
  `11 → 7`) is **untouched** — different content.
- The 't Hooft-scheme construction is standard QFT ('t Hooft 1977), cited as **method**;
  the demarcation against the framework's derived set is the framework-facing content.
- No new axiom or import; no PDG value consumed.

## Cross-references

- The wall being demarcated: [`ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop`](ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop.md)
- The conversion dictionary's home (the named admission): [`CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a`](CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a.md)
- The QCD-running parent and inline coefficient provenance: [`ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop`](ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop.md), [`SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md`](SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md)
- Untouched sister lane: [`QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02`](QCD_BETA_3_PURE_GAUGE_VS_FULL_SM_NARROW_THEOREM_NOTE_2026-06-02.md)
- Standard method (not imports): scheme transformations of β-coefficients; the 't Hooft scheme ('t Hooft 1977).
