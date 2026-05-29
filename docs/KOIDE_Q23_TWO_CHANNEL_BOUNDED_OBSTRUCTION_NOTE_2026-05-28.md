# Koide Q=2/3 — two-channel bounded obstruction (campaign capstone)

> **PARTIAL CORRECTION (2026-05-28) — see
> `KOIDE_Q1_OVERREACH_SELF_CORRECTION_NOTE_2026-05-28.md`.** The
> "framework natively selects F3 (Q=1)" framing over-privileges the
> dimension/trace measure. Block-counting (the 2 central idempotents of
> `ℝ[Z₃]=ℝ⊕ℂ`) is equally canonical and gives F1 (Q=2/3). Correct: the
> trace/dimension-type channels (the ones analyzed here) give F3, but
> block-counting (→F1) is canonical and untouched. Status is UNDETERMINED
> between two canonical measures, not "framework → Q=1."

**Date:** 2026-05-28
**Claim type:** bounded_retained (two-channel; framework natively selects
F3); promotion route OPEN and named. Imports no axiom/comparator/
convention; promotes no row; sets no retained status (audit lane decides).
Local-branch working note.
**Scope:** close the charged-lepton Koide `Q=2/3` derivation question on
A1+A2+retained, consolidating the kinematic no-go and the dynamical probe
campaign into a single structural verdict.
**Runner:** `scripts/koide_two_channel_f3_inheritance_2026_05_28.py`;
cache `logs/runner-cache/koide_two_channel_f3_inheritance_2026_05_28.txt`.
**Upstream this campaign:** `KOIDE_Q23_BLOCK_WEIGHT_HARDENING`,
`KOIDE_F1_SELECTION_PANEL_FINDINGS`, `KOIDE_U1B_WALL_RADIAL_RELOCATION`,
`KOIDE_F1_KINEMATIC_NO_GO` (all 2026-05-28).

## The object
Charged-lepton √mass packet = Hermitian C₃-circulant `H = aI + bC + b̄C²`;
`Q = 1/3 + (2/3)(|b|²/a²)`. `Q=2/3 ⟺ r:=|b|²/a²=1/2` (F1, equate isotype
TOTAL norms `3a²=6|b|²`). `Q=1 ⟺ r=1` (F3, equate PER-REAL-DIMENSION
norms). The whole program reduces to: does A1+A2+retained force F1?

## Verdict: NO — settled two-channel bounded obstruction; framework → F3
Both channels converge on **F3 (r=1, Q=1)**; F1 is supplied by neither.

### Channel 1 — KINEMATIC (settled no-go)
Reality + `U(1)_b` phase/crossed-product + Tomita–Takesaki/KMS (finite
*and* Z³ type-III) + Connes cocycle + canonical Euclidean-Jordan trace all
fail to force `r=1/2`. The generation circulant is abelian ⇒ modular flow
trivial (`Δ=1`); the EJA is rank-3 split `ℝ⊕ℝ⊕ℝ`; reality keeps `{ω,ω̄}`
two equal modes. The doublet's 2 real dimensions are never canonically
collapsed to 1 complex unit. (`KOIDE_F1_KINEMATIC_NO_GO_NOTE`.)

### Channel 2 — DYNAMICAL (now closed, same obstruction)
A 5-corner hunt (0/5 reach F1) plus the prior probe campaign (5/21/25/28 +
Z³ potential):
- **Free/Gaussian (the theorem):** the canonical free energy
  `(½)log det K = (½)[1·log E₊ + 2·log E⊥]` **is** the dimension-counting
  measure → F3. (Verified.)
- **Interacting:** Probe 28 vertex `≈0.0072 ≪` the F3↔F1 gap (`ΔQ=1/3`).
- **Nonperturbative:** `H` *is* the C₃ θ-vacuum winding sum, so θ only
  rotates `arg(b)` (r invariant); instanton fugacity sweeps r continuously
  → **r→1** at strong coupling; zero-mode counting = real-dim 2 = F3.
- **Positivity/BPS saturation (import-free):** saturation lands on the cone
  *boundary* — r=0 (Q=1/3) or r=1 (Q=1, doublet `a−b` goes massless). **r=1/2
  is strictly interior**, so no positivity/unitarity saturation can reach it.
- **Index/topological:** quantizes the generation *count* (d=3, integer,
  constant in (a,b)), not the continuous amplitude ratio r.
- **Gap equation:** C₃-democratic kernel → r=1; r=1/2 only via the irrational
  tuned ratio `s/d = 4±3√2` (fitting).

### The unifying theorem
**Dynamics inherits the kinematic dimension-count.** Every measure A1+A2
canonically supplies — inner products, phase-space volumes, the Gaussian
functional determinant, positivity Grams, index counts, regular-rep
Frobenius norms — reads the C₃ doublet as **2 real dimensions** and so
extremizes/saturates at **F3**. The free/Gaussian action and the
dimension-counting measure are the *same object*: the two channels are not
two chances at F1, they are one chance counted twice. F1 requires the
unsupplied **(1,1) complex-multiplicity** primitive (`a²=2|z|²`, collapsing
the doublet to one complex unit).

## The single uncovered escape (why this is bounded_retained, not no_go)
The entire campaign **assumed the real measure** (`|v|² = a² + 2|z|²`)
throughout. But **A1 = M₂(ℂ) = Cl(3,0) is a complex algebra**, and the
`U(1)_b` the campaign treats as a "free direction to be killed" is exactly
the phase of a *complex structure* (the Cl(3,0) `J`). The one place the
verdict could flip:

> **Does A1's intrinsic complex structure `J` CANONICALLY FORCE the
> holomorphic/Kähler measure that counts the doublet as ONE complex unit
> (collapsing `U(1)_b` as a complex-structure gauge the qubit fixes)?**

If yes → F1 (Q=2/3); if no → the framework is F3-native (Q=1). This is the
same residual the sister weight-audit lane flagged as **ND4**
(real-Gaussian vs holomorphic/Kähler measure on the complex doublet `b`) —
two independent lanes converge on the identical open question. Positing the
holomorphic measure is currently an **import**; engineering a Z³ potential
to hit r=1/2 is **fitting** (the Z³-potential note shows the honest minimum
lands at the wrong point, `m_V≈−0.433` vs `m_*≈−1.161`).

## Status and bottom line
**bounded_retained:** the charged-lepton Koide carrier is **framework-native
F3 (Q=1)** on both kinematic and dynamical channels, with the
holomorphic-collapse promotion route **OPEN but currently un-derived**. The
program reduces to one decidable question: prove or refute that A1's
`Cl(3,0)=M₂(ℂ)` complex structure canonically supplies the holomorphic
measure. Until then, Q=2/3 is not derived from A1+A2+retained — and the
honest reading is that the framework, taken with its real/Euclidean
measure, selects Q=1, not the observed 2/3.
