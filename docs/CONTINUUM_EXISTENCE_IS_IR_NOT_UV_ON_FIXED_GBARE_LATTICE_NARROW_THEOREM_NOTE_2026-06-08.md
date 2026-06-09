# Interacting-Continuum Existence Is IR-Emergence, Not a UV Limit, on the Fixed-`g_bare` Lattice

**Date:** 2026-06-08
**Type:** narrow theorem (relocation of the existence question) + named open input
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_continuum_existence_ir_not_uv_fixed_gbare_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_continuum_existence_ir_not_uv_fixed_gbare_2026_06_08.txt`
**Status:** source proposal. The derived β-coefficients, the AF⇔continuum-exists link,
the dimensional-transmutation scale, and the scaling-onset diagnostic are exact/computed.
The relocation reading rests on the baseline physical-lattice semantics + the retained
`g_bare=1` convention. Authority role: source proposal; audit lane sets status.

## Claim under test (the §3 strategic question, made rigorous)

The hardest obstruction to interacting 4D QFT is the **UV continuum limit**: removing the
cutoff (`a→0`) while keeping the theory non-trivial — the Clay Yang–Mills problem. The
campaign's §3 asks whether, on a framework where the lattice is **physical** (baseline
semantics, `PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE`), the existence question
**relocates** from a UV-continuum construction to an IR-emergence statement — with
asymptotic freedom as the lever. **Derive it, don't assume it.**

## Verdict

**Yes — and asymptotic freedom is exactly the hinge.** AF (derived) is the *condition*
under which the standard `a→0` continuum exists; the framework's retained `g_bare=1≠0`
does **not** execute that limit; so the framework defines a **fixed-spacing** interacting
theory whose existence question is **IR** (mass gap / clustering at β=6), sidestepping the
UV-continuum construction. The existence question is **relocated and well-posed**, not
closed.

## What is shown (exact / computed — runner `PASS=14 FAIL=0`)

1. **The β-coefficients are derived from retained Casimirs.** `b₀=(11C_A−4T_F N_f)/3 = 7`
   (1-loop) and `b₁ = (34/3)C_A² − 4C_F T_F N_f − (20/3)C_A T_F N_f = 26` (2-loop) at
   `N_f=6`, from `C_A=3, C_F=4/3, T_F=1/2` (cf. `SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE`,
   retained_bounded). **`b₀ > 0`: asymptotic freedom.**

2. **The continuum limit is the `g_bare→0` endpoint.** The asymptotic lattice scaling
   `a(g) ∼ exp(−1/(2b₀g²)) (b₀g²)^{−b₁/2b₀²}` → 0 monotonically as `g→0` (essential
   singularity); `a(g=10⁻³) < 10⁻¹⁰⁰`. The continuum is reached **only** at `g=0`.

3. **AF ⇔ the continuum exists.** With `b₀>0` (AF), `a→0` as `g→0`. With `b₀<0` (not AF),
   the same formula gives `a→∞` (Landau pole) — **no** continuum. So AF is precisely the
   condition for the standard continuum limit to exist.

4. **The framework fixes `g_bare=1 ≠ 0` (β=6) — it does NOT take the limit.** `β=2N_c/g_bare²=6`
   (retained convention, `G_BARE_DERIVATION_NOTE`). `g_bare=1≠0` ⇒ fixed spacing `a>0`,
   not `a→0`. **Honest diagnostic:** at `α_bare=g_bare²/4π=1/4π`, the 2-loop/1-loop β ratio
   `|b₁α_bare|/b₀ ≈ 0.30` — so **β=6 is the *onset* of asymptotic scaling**, a *finite
   physical* coupling, not an asymptotically-deep point. (This *reinforces* the reading:
   the framework lives at a finite physical β, not on the asymptotic continuum trajectory.)

5. **Dimensional transmutation → a finite emergent IR scale.** 1-loop running from the
   lattice scale (`α_bare=1/4π≈0.08`) toward the IR reaches `α_s∼1` at
   `μ_conf/μ_lattice = exp(−10.4) ≈ 3×10⁻⁵` — a **finite, computable** IR/UV separation.
   The confinement scale *emerges* from the fixed bare coupling; no continuum is needed.

## The relocation (Part 6)

- **Standard (Clay):** construct the `a→0` continuum interacting Yang–Mills (requires `g→0`).
- **Framework:** `g_bare=1` fixed ⇒ a fixed-`a` theory ⇒ existence = **IR** (mass gap /
  clustering at β=6). AF's role here is **not** cutoff-removal but (i) the *condition* that
  the standard continuum would exist (`b₀>0`), and (ii) keeping the fixed UV anchor weakly
  coupled (`α_bare=1/4π`) with the coupling growing toward IR confinement.

This converts the hardest constructive-QFT problem (UV continuum of interacting YM) into a
**fixed-`a` IR statement** — exactly the §3 reframe, now derived from the AF structure
rather than assumed.

## What this does NOT claim (boundary)

- **No proof that the IR theory exists.** The pure-gauge gap `Δ_gauge(β=6)>0` is **open**;
  only the matter-sector floor is retained (`INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE`,
  retained_bounded, `Δ_T^matter ≥ arcsinh(m)/a_τ`). Existence is **relocated and well-posed**,
  not closed.
- **No new axiom or import.** β-coefficients are derived from retained Casimirs; the RG
  integration / asymptotic scaling are standard math; `g_bare=1` and the physical-lattice
  reading are existing retained/baseline content.
- **No claim that β=6 is on the asymptotic continuum trajectory** — the opposite is stated
  honestly (Part 4: β=6 = scaling onset).
- Does not contradict the standard a→0 continuum mathematics; it shows the framework does
  not invoke it.

## Cross-references

- Matter floor / open gauge gap (retained): [`INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30`](INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30.md)
- Derived β-coefficients (retained_bounded): [`SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10`](SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md)
- Baseline physical lattice: [`PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08`](PHYSICAL_LATTICE_FOUNDATIONAL_INTERPRETATION_NOTE_2026-05-08.md)
- `g_bare=1` convention (retained_bounded): [`G_BARE_DERIVATION_NOTE`](G_BARE_DERIVATION_NOTE.md)
- §3 companions (action sector): PR #3338 (action-form no-go scoped), PR #3339 (heat-kernel = unique diffusion-kernel)
- Standard method (not imports): lattice asymptotic scaling / dimensional transmutation (Creutz 1980; standard QCD RG).
