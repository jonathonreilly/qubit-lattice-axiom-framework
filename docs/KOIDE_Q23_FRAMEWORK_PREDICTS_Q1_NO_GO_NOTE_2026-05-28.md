# Koide Q=2/3 — final no-go: the framework natively predicts Q=1

**Date:** 2026-05-28
**Claim type:** retained_no_go (derivation of Q=2/3 from A1+A2+retained);
the framework's native prediction is Q=1. The import needed for Q=2/3 is
named explicitly. Promotion would require NEW structure (named below), so
this is a no-go on the *current* axioms, not a permanent lock on the
question.
**Status authority:** independent audit lane. Imports no axiom/comparator/
convention; promotes no row. Local-branch working note (campaign capstone).
**Runner:** `scripts/koide_kahler_decider_consistent_counting_2026_05_28.py`;
cache `logs/runner-cache/koide_kahler_decider_consistent_counting_2026_05_28.txt`.
**Campaign chain (all 2026-05-28):** equipartition derivation → block-weight
hardening → F1-selection panel → U(1)_b wall relocation → kinematic no-go →
two-channel obstruction → **this (quantum/Kähler decider)**.

## The question, fully reduced
Charged-lepton `Q = 1/3 + (2/3)(|b|²/a²)` for the Hermitian C₃-circulant
packet. `Q=2/3 ⟺ r:=|b|²/a²=1/2` (F1). Isotype energies `E_+ = 3a²`
(trivial, 1 real dim) and `E_⊥ = 6|b|²` (doublet, 2 real dim). The whole
program = does A1+A2+retained force F1?

## Verdict: NO. Framework predicts Q=1 (F3). Q=2/3 needs a named import.
The deciding workflow (Kähler-quantization, 4 angles, **0 F1 / 4 F3**)
closes the last uncovered escape. The result is a clean, airtight negative.

### The decisive argument: any *consistent* counting gives F3
`E_+ = 3a²` is 1 real dim = ½ complex dim; `E_⊥ = 6|b|²` is 2 real dim = 1
complex dim. Balance the isotype energies under a *consistent* dimension
count:
- **count both by REAL dimension** → weights (1, 2) → `r=1` → **F3**;
- **count both by COMPLEX dimension** (a real line is *half* a complex
  line) → weights (½, 1) → `r=1` → **F3**.

Both consistent countings give the 2:1 ratio = F3 (Q=1). **Only the
*inconsistent asymmetric* count** — doublet by its complex dim (1), singlet
by its real dim (1) — gives `r=1/2` = F1. That asymmetry is precisely the
tuned isotype weight `κ = 2μ/ν` of the prior weight-audit; it is not a
counting rule, it is the answer assumed.

### Why A1's quantum structure does NOT supply the asymmetry
The last hope was that A1 being a *qubit* (Kähler state space, `i = ω` the
Cl(3,0) pseudoscalar) canonically forces a holomorphic measure counting the
doublet as one complex unit. It does not:
1. **`ω` is central → uniform.** `[ω, eᵢ]=0` for all grade-1 basis vectors
   (verified); `ω` acts as the *same* scalar `i·Id₃` on grade-1. It
   complexifies the singlet `a` and the doublet `b` **equally**, so it
   halves both channels uniformly — ratio preserved → **F3**. It cannot
   produce the doublet-only asymmetry F1 needs.
2. **The F1-giving `J` is C₃-sourced, not A1-sourced.** The operator that
   fixes the singlet and pairs only the doublet is `J` = the π/2 rotation
   about the body diagonal (the grade-2 bivector dual to `n=(1,1,1)`),
   forced by C₃ generation symmetry — a *different* operator from `ω`
   (verified `J·n=n`, `J²|_doublet=−Id`). Polarizing w.r.t. `J` rather than
   `ω` is a free choice = the posited holomorphic measure.
3. **BKS / Stone–von Neumann:** real (Lagrangian) and Kähler polarizations
   give unitarily equivalent Hilbert spaces, so `E_⊥/E_+` is a polarization
   *invariant* = 2. Holomorphy *relabels* 2 real modes as 1 complex mode;
   it does not *reduce* the count.
4. **Factor-2 rigidity:** `E_⊥ = 6|b|² = 3|b|² + 3|b|²` over the conjugate
   pair `{C, C²}`; the "2" in 6=2·3 *is* the doublet's two real dimensions.
   Holomorphic "count once" cannot remove it from the weight while leaving
   it in the Hermitian operator's energy.
5. **Odd-dimensional packet:** `{(a,b): a∈ℝ, b∈ℂ} = ℝ³` is odd-real-dim and
   admits no global complex structure; `ω=i` lives in the qubit state
   space, not on the mass-operator parameter space.

## What it would take to get Q=2/3 (the named import)
A forced complex structure that pairs **only** the generation doublet
(counting it as one complex unit) while leaving the singlet real — i.e.
polarizing w.r.t. the C₃-sourced `J`, equivalently adopting the asymmetric
isotype weight `(w_+, w_⊥)=(1,1)`. A1+A2+retained do not supply it: `ω=i`
gives only the uniform `i·Id₃`. Positing it is an import; engineering a Z³
potential to land at `r=1/2` is fitting (the Z³-potential minimum lands at
the wrong point). This is the same residual two independent lanes
(this campaign + the sister weight-audit ND4) converged on.

## Status and honest bottom line
**retained_no_go** on deriving `Q=2/3` from A1+A2+retained. Taken with any
*consistent* measure — classical/real, dynamical (perturbative +
nonperturbative), and the genuinely quantum/Kähler measure built from A1's
own `ω=i` — the framework predicts **Q=1 (r=1, F3)**, not the observed
`Q≈2/3`. The observed value requires new structure: a complex structure on
the generation sector that pairs only the doublet, which the current axioms
do not force. The widely-cited "Koide = 45° / equal-magnitude" condition is
exactly this asymmetric weight, published as a description, not derived.

This closes the charged-lepton Koide derivation program on the current
axiom set: **the framework's honest prediction is Q=1; Q=2/3 is an import.**
