# Flavor — the chiral import is not derivable; the single pin is the value r=1/2

**Date:** 2026-05-30
**Claim type:** derivation attempt verdict + correction. Imports nothing.
**Runner:** `scripts/flavor_chiral_import_verdict_2026_05_30.py` (+ cache).
**Source:** chiral-import derivation press (`wf_95d69898`, 0/7 native derivations) +
the two unrun routes executed/reasoned here.

## The question
Can the generation chiral grading (the import that gives charged-lepton `Q=2/3`)
be **derived/forced** from A1+A2+retained? **Verdict: no identified native route
forces it; the single irreducible pin is the *value* `r=|b|²/a²=1/2` — a
continuous modulus.**

## Every native source fails (press, 7 angles)
- **Cl(3) volume** `ω=e₁e₂e₃=iI` is **central** — a sector label, no chiral action
  on states.
- **Anomaly / 't Hooft** is flavor-symmetric → reaches only **discrete** data
  (count, charges); cannot select a generation operator.
- **Native spacetime chirality** `ε=(−1)^{x+y+z}` (retained `cpt_exact`) is
  **generation-blind**.
- **Native antiunitary T** acts as `b→b̄` → **suppresses** the orientation
  (forces `Im b=0` → degenerate) — wrong sign.
- The three retained no-gos are airtight for their routes; the only unforbidden
  gap is a native C₃-**non-equivariant** operator (joint-commutant
  characterization not yet done).

## The two unrun routes — executed/reasoned, both fail to force the value
- **Escape (II), qubit-factor grading [run here]:** on `C²(qubit)⊗R³(gen)`, the
  grading `σ₃⊗I₃` (signature (3,3), balanced) makes `D=[[0,A],[A†,0]]`
  anticommute *natively* (the qubit is from A1) and gives 3 distinct masses =
  **singular values** of `A`. But that forces the singular-value (Yukawa)
  readout, which is generic for generic `A` and θ-dependent **≤2/3** for
  circulant `A` (verified: `r=½, θ=0 → Q=0.43`, not 2/3). The (1,2) generation
  grading that yields `Q=2/3` (signed-eigenvalue/Brannen) is **not** supplied by
  the (3,3) qubit grading. So escape (II) **relocates** the import to "`A` has
  Koide singular values" and forces the **wrong readout** — does not force 2/3.
- **Discrete Z₃ anomaly:** anomalies are topological/**discrete**; `r=½` is a
  **continuous** modulus → category mismatch (same as the time-emergence panel)
  → cannot force `r=½`.

## Correction to my earlier framing (phase-dof / move-1)
The antisymmetric generator `i(C−C²)` is part of the **circulant** (`= Im b`), is
**C₃-equivariant**, and **commutes** with `Γ_χ` — it is **not** the chiral
import. A circulant with complex `b` already gives **3 distinct** masses while
commuting with `Γ_χ` (verified). So the import is **not** "the antisymmetric dof
for 3-distinctness"; 3-distinctness needs only the orientation `θ≠0`, which may be
**native** (`positivity_orientation_selects_c3`, retained_bounded — positivity
selects the C₃ orientation). The single irreducible pin is specifically the
**value** `r=½` (`b/a=1/√2`), i.e. the eigenvector-cone condition `⟨v|Γ_χ|v⟩=0`.

## Honest verdict — the charged-lepton flavor structure decomposes
| piece | status |
|---|---|
| `n_gen=3` (the count) | **derived** (retained `three_generation_hw1`) |
| 3 distinct masses (orientation θ≠0) | **possibly native** (positivity selects C₃) |
| `Q=2/3` (the value `r=½`) | **the single irreducible pin** — a continuous modulus |

No native route forces `r=½`: measure → Q=1, dynamics → Q=1/3, criticality → ∞,
Cl(3) volume central, anomaly discrete (can't reach a continuous modulus),
time-arrow → orientation-not-value, reflection → suppresses, qubit-factor escape →
wrong readout. Given the pin, `Q=2/3` is **derived** (retained
`koide_anticommuting_operator`); the pin itself is **reproduced, not derived** —
the same single pin shared across Koide / quark / generation-ID / strong-CP /
signed-gravity, = the observed chirality/Koide content of the SM.

## Status (current-state, not terminal)
Two threads the no-gos do **not** close, for a future attempt: (1) the
exhaustive joint-commutant characterization of (Cl(3) site-action, Z³
translations, hw=1 projector) — is there a native C₃-non-equivariant operator at
all? (2) whether a derivation of the *value* `r=½` exists outside the
operator-grading framing entirely (every operator/measure/dynamics route is now
mapped and lands elsewhere). The honest current classification: the framework
**derives the count and (plausibly) the 3-distinctness, and reproduces the one
continuous value-pin `r=½`** that it does not derive.
