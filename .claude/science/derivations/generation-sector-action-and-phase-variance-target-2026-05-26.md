# Derivation: The Generation-Sector Effective Potential Form, and the Crisp Dynamics-Lane Target (phase = variance)

## Date
2026-05-26

## Target Behavior

Step 1 of the **dynamics lane** (the asymptotic-safety / functional-RG route to the gauge-singlet
flavor *values*). Two things:

1. **Derive the FORM** of the generation-sector effective potential for the C₃ order parameter from
   A1 (qubit per site, M₂(ℂ)≅Cl(3,0)) + A2 (Z³) + the retained C₃ generation structure: show it is
   forced to be `V(δ) = A cos(3δ) + B cos(6δ) + …` (cosines only).
2. **State the decisive target precisely**, separating the *retained combinatorial* content from the
   *open dynamical* content. The retained charged-lepton derivation
   (`charged-lepton-koide-cone-2026-04-17.md`) fixes the **cone** (radial structure) but leaves the
   **phase** `δ = arg(z)` (the position on the cone) open. The lane's job is to fix that phase.

Quantitative anchors (from retained notes):
- Koide cone `Q = 2/3` ⟺ `|z|/a₀ = 1/√2` ⟺ `a₀² = 2|z|²` (retained, Steps 1–5 of the cone derivation).
- Bernoulli family (retained CKM structural counts): mean `M(N)=(N−1)/N`, variance `V(N)=(N−1)/N²`,
  universal relation `V(N)=M(N)/N`. At `N=N_gen=3`: `M(3)=2/3`, `V(3)=2/9`.
- Open: the Koide phase `δ = arg(z) ≈ 2/9 rad` (Brannen `√m_k ∝ 1 + √2 cos(δ + 2πk/3)`), the
  azimuthal position on the cone — unfixed on the retained surface (Step 7, `TRUE_NO_PREDICTION`).

## Axioms Used

- **A1** — per-site M₂(ℂ)≅Cl(3,0); the "i" is the Cl(3) pseudoscalar; complex structure ⇒ a U(1)
  phase exists per the relevant order parameter.
- **A2** — Z³ locality (nearest-neighbour effective operators; analyticity in the order parameter).
- **Retained C₃ generation structure** — the hw=1 BZ-corner triplet with the induced `C₃[111]`
  cycle `P_i → P_{i+1}`; the real, symmetric, C₃-covariant curvature kernel `K = a·I + b·(J−I)`
  (circulant); the character split `a₀` (trivial) and `z` (nontrivial), `z = (λ₁+ω̄λ₂+ωλ₃)/√3`.
  Authority: `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`, `charged-lepton-koide-cone-2026-04-17.md`.
- **Retained CP-evenness** — the framework Dirac operator is real, `θ=0`; the effective action is
  CP-even (invariant under `z → z̄`, i.e. `δ → −δ`).

## Minimal Example

The three hw=1 species on one Z³ unit cell carry a single complex C₃-nontrivial amplitude
`z = r e^{iδ}` (the order parameter). The clock `C₃[111]` acts as `z → ω z` (`ω = e^{2πi/3}`); CP
acts as `z → z̄`. Everything below is the most general local functional of this one complex field.

## Derivation

### Step 1: A1 ⇒ a complex C₃ order parameter `z = r e^{iδ}`
The retained character decomposition gives the nontrivial-character amplitude `z` as a single
complex number; A1's per-site complex structure (the Cl(3) pseudoscalar) is what makes `arg(z)=δ`
a genuine U(1) phase rather than a sign. The clock symmetry acts by `z → ω z`.

### Step 2: C₃-clock invariance ⇒ allowed operators are powers of `z³`
Any C₃-invariant local term must be invariant under `z → ω z`. The invariant monomials in `z` are
`|z|²` and `z^{3m}` (and conjugates), since `ω^{3m}=1`. Hence the most general C₃-invariant local
potential is
```
V = f₀(|z|²) + [ c₃ z³ + c₆ z⁶ + … + c.c. ]   (with |z|²-dependent coefficients).
```

### Step 3: CP-evenness ⇒ cosines only (no sines)
CP sends `z → z̄`, i.e. `δ → −δ`, and (retained `θ=0`) the action is CP-even, so the couplings
`c_{3m}` are real. Writing `z = r e^{iδ}`:
```
z^{3m} + z̄^{3m} = 2 r^{3m} cos(3m·δ).
```
Therefore, **at fixed radius `r` (on the Koide cone)**, the angular potential is forced to be
```
V(δ) = A cos(3δ) + B cos(6δ) + (higher harmonics),   A = 2 c₃ r³,  B = 2 c₆ r⁶,   A,B ∈ ℝ.
```
This is **exactly the flavon spontaneous-CP potential** — now *derived* as the unique C₃-clock +
CP-even local form, not postulated. The `3δ` harmonic is forced by the generation/clock number 3.

### Step 4: Relevance ordering (lattice RG)
By A2 (locality/analyticity), operators are ordered by their power of the order parameter: the
cubic `z³` (→ A) is more relevant than the sextic `z⁶` (→ B), which is more relevant than `z⁹`, …
So the leading two harmonics `A cos3δ + B cos6δ` dominate the IR angular potential; higher harmonics
are increasingly irrelevant. Truncating at `B` is RG-justified, not ad hoc.

### Step 5: The cone fixes the radius; the phase is the residual
The retained cone result fixes the **radial** ratio `|z|/a₀ = 1/√2` (⟺ `Q=2/3`). In Bernoulli
language this radial structure is the **mean/variance** data: `M(3)=Q=2/3`, `V(3)=2/9`, `V=M/3`.
The **phase** `δ = arg(z)` is the orthogonal, residual degree of freedom — the azimuthal position on
the cone — left open at Step 7 of the retained derivation. **This is the entire admitted quantity.**

### Step 6: The decisive lane target — phase = variance
The spontaneous-CP minimum of Step 3's potential is `cos(3δ) = −A/(4B)`. The framework's bet
`δ = 2/9` is `cos(3δ) = cos(2/3)`, i.e. `3δ = Q`, i.e. `δ = Q/3 = V(3)`. Stated cleanly and without
the radian-bridge dressing: **the azimuthal phase equals the radial variance**,
```
arg(z) = δ  ?=?  V(3) = (N_gen − 1)/N_gen² = 2/9.
```
The radial structure (cone) already *contains* `V(3)=2/9` as a combinatorial fact (retained). The
open, genuinely *dynamical* statement is that the **phase locks to that variance**. That is the one
theorem the dynamics lane must prove.

### What follows from A1+A2 vs what is an added dynamical assumption
- **From A1+A2 + retained structure (derived here):** the order parameter `z=re^{iδ}`; the potential
  *form* `A cos3δ + B cos6δ + …` (C₃-clock invariance); cosines-only (CP-evenness); the relevance
  ordering A≫B≫… ; the cone fixing `r` and hence `M(3),V(3)`.
- **Added dynamical assumptions (the lane's new inputs, NOT from A1+A2):**
  1. `z` is a **dynamical** field with a kinetic term and an RG flow (a flavon), not a frozen
     background — needed because static/geometric phases are `q·π`, never a bare rational (the
     retained radian-bridge obstruction).
  2. The couplings `A,B` (hence `δ`) are fixed by an **IR fixed point** of the generation-sector
     flow — the asymptotic-safety mechanism, run through the framework's forced gravity/emergent
     time (the sector that "sees" the gauge singlet).
  3. The fixed point **locks `arg(z) → V(3)`** (phase = variance), equivalently `A/B → −4cos(2/3)`.

## Novel Prediction

If the phase-locks-to-variance mechanism is correct, then because `V(N)=M(N)/N` holds for *every*
`N`, the **same** dynamics applied to the **quark** sector (where the relevant count is `N_quark=6`,
not `N_gen=3`) must lock the corresponding azimuthal phase to `V(6) = (6−1)/6² = 5/36`. The retained
CKM CP structure already carries `η² = 5/36 = V(6)` as the analogous *radial* variance; the
prediction is that the quark azimuthal CP phase (the part beyond the radial `cos²δ_CKM = 1/n`) is
`5/36 rad` at the same fixed point — a single locking mechanism producing `2/9` (leptons, N=3) and
`5/36` (quarks, N=6) from the **one** rule `phase = V(N)`. This is testable against the PDG CP phase
and is *not* an input to the derivation.

## Weakest Link

Added assumption #3 (the fixed point actually **locks** `arg(z) → V(N)`). Steps 1–5 are forced by
symmetry; assumptions #1–#2 are the standard dynamical-field/RG setup; but #3 — that the IR fixed
point lands exactly at the variance value rather than some other point in `0<|A/B|<4` — is unproven.
The test: compute the generation-sector β-function (functional RG / Wetterich) for `A/B` with the
C₃-clock + gravity couplings and check whether `−4cos(2/3)` (lepton) and the `N=6` analogue are
attractors. This is the lane's milestone-3 computation.

## Status
PROPOSED (Steps 1–5 rigorously forced by symmetry; Step 6 target stated precisely; the locking
itself is the open dynamical computation).
