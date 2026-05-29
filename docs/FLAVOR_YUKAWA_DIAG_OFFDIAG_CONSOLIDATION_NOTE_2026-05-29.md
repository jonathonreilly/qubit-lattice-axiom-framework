# Flavor — the e–μ gap dissolves; the value consolidates to r=½ (off-diag/diag)

**Date:** 2026-05-29
**Claim type:** consolidation / synthesis (NOT a derivation, NOT a promotion).
Imports nothing; sets no retained status. Reconnects the Jahn-Teller route
(`FLAVOR_JAHN_TELLER_CUBIC_BREAKING_NOTE_2026-05-29.md`) to the retained
Brannen biconditional.
**Runner:** `scripts/flavor_yukawa_diag_offdiag_consolidation_2026_05_29.py`
(+ cache).

## The thread I pulled
The Jahn-Teller refinement left two named gaps: (i) a **stiffness** (sets the
breaking magnitude), and (ii) the **e–μ degeneracy** (the energetically-cheapest
pattern leaves the two light generations equal at leading order). Chasing (ii)
consolidates the picture instead of opening a new front.

## The full generation Yukawa decomposes into diagonal + off-diagonal
On the three hw=1 corners the Yukawa `Y` splits as:
- **Diagonal `a`** — the corner masses (Wilson + diagonal condensate). The
  **Jahn-Teller instability acts here** (anisotropy = a *C₃-breaking diagonal*).
- **Off-diagonal `b`** — the C₃-symmetric corner↔corner coupling:
  `Y = a·I + b·C + b̄·C²` (`C` = 3-cycle).

With Brannen's `√m_k = a + 2|b|cos(θ + 2πk/3)`:
```
Q = Σm / (Σ√m)² = 1/3 + (2/3) r ,   r = |b|²/a²   — EXACT, θ-INDEPENDENT.
```
(Verified numerically across `r∈{0,¼,½,1}` and all θ.)

## Two consequences
1. **The e–μ gap dissolves.** The *splitting* of the three √masses (which corner
   is e, μ, τ) is set entirely by the phase `θ = arg(b)` — and θ is **exactly
   Q-orthogonal** (the retained Brannen δ). At `r=½`, θ sweeps the spectrum
   across the full 3-distinct range while **Q stays 2/3**. So the e–μ
   degeneracy is filled *trivially* by the off-diagonal phase and contributes
   **nothing** to the value question.
2. **The value consolidates to `r=½`.** `Q=2/3 ⟺ r = |b|²/a² = ½` — exactly the
   retained biconditional `koide_circulant_character_bridge`. Now `r` has a
   concrete full-operator meaning: **(off-diagonal corner-coupling)² /
   (diagonal corner-mass)²**.

## Why this is progress (a unification of the two gaps)
The Jahn-Teller (diagonal, C₃-breaking) and Brannen (off-diagonal, C₃-symmetric)
pictures are the **diagonal and off-diagonal of the same Yukawa**. The value
2/3 is **neither's alone**: it is the *ratio* of off-diagonal `b` to diagonal
`a`. Both `a` (set by the diagonal condensate / the "stiffness" scale) and `b`
(the off-diagonal corner-coupling) are **vacuum/condensate quantities**. So the
two gaps named earlier are **one** nonperturbative target:

> **Q = 2/3 ⟺ the off-diagonal corner-coupling is exactly `1/√2 ×` the diagonal
> corner-mass (r = |b|²/a² = ½) in the vacuum.**

That is a single, sharp, computable statement about the vacuum condensate
structure — the same `r=½` the whole campaign reduced to, but now anchored in
the full operator (not the isolated toy) and stripped of the spurious e–μ
distraction.

## Status
Consolidation, no false closure. The e–μ "gap" was a phantom (Q-orthogonal θ).
The genuine, irreducible target is unchanged and now sharper: a single vacuum
condensate ratio `|b|²/a² = ½`. This is exactly the retained biconditional,
re-derived inside the full generation operator, with both `a` and `b` identified
as the vacuum quantities a lattice computation would produce.
