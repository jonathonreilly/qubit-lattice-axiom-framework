# Flavor — a native Jahn-Teller route to the generation hierarchy

**Date:** 2026-05-29
**Claim type:** candidate mechanism / numerical experiment (NOT a derivation,
NOT a promotion). Imports nothing; sets no retained status (audit lane
decides). Continuation of `FLAVOR_FULL_OPERATOR_NONPERTURBATIVE_VALUE_NOTE_2026-05-29.md`.
**Runner:** `scripts/flavor_jahn_teller_cubic_breaking_2026_05_29.py`
(+ cache `logs/runner-cache/flavor_jahn_teller_cubic_breaking_2026_05_29.txt`).

## The question
The full free+Wilson operator gives the three generations (hw=1 BZ corners)
degenerate → Q=1/3. The observed hierarchy (Q=2/3) requires the cubic/S₃
axis-symmetry to break. Is the cubic-symmetric vacuum **stable** (→ Q=1/3
forever), or does the full theory **spontaneously break** it? This is the
lattice-scale analog of "does QCD spontaneously break chiral symmetry."

## The numerical experiment
Fermion vacuum energy of the Wilson-Dirac operator on Z³ as a function of a
**cubic-symmetry-breaking** distortion of the Wilson coefficients
`r_μ = r₀(1+d_μ)`, `Σd_μ = 0` (pure cubic-breaking). `E_vac = −Σ_k |eig D(k)|`.

1. **Native instability found.** `E_vac(ε) − E_vac(0) < 0` for `ε≠0`, both
   signs and both distortion patterns: the cubic-symmetric point is a **local
   maximum** of the fermion vacuum energy. The fermion sea *lowers* its energy
   by splitting the degenerate generation corners — a **Jahn-Teller / Peierls**
   instability. This is native: no operator is written down, no chiral grading
   is imported; it is driven by the fermion determinant.
2. **Analytic (ε², not log).** `dE/ε² ≈ −0.025` (constant) — so the instability
   **competes** with the gauge/elastic stiffness rather than running away:
   `E_total(ε) = dE_ferm(ε) + (K/2)ε²` breaks iff `K < K_c`. `g_bare=1` fixes
   the stiffness `K` → the outcome is determined by the full action.
3. **Q vs base mass.** At a heavy base mass the splitting is small relative to
   the mass → Q stays ≈1/3. Near-critical (light) generations give a large
   relative hierarchy → Q rises through `[1/3, 1]`. **But see the refinement
   below: 2/3 is *in* that range but is NOT naturally/robustly delivered with
   the observed 3-distinct spectrum** — an honest correction to a first,
   over-rosy "passes 2/3" reading.

## Refinement (corrected Q-structure — `scripts/flavor_jahn_teller_Q_structure_2026_05_29.py`)
The cubic-breaking is **traceless** (`Σd_μ=0`), so the three corner masses have
**fixed mean** `M0`, and `Q = 3M0/(Σ√M_μ)²` spans `[1/3, 1]`. Three facts
sharpen (and partly walk back) the optimistic reading:

- **(A) The energetically-preferred direction gives TWO DEGENERATE generations.**
  The `E_vac` angular scan minimizes at the "one-axis-out" directions →
  masses `(M0+2a, M0−a, M0−a)`. Sweeping toward criticality reproduces the
  **gross lepton structure "1 heavy + 2 light"** and passes `Q=2/3` (at
  `a/M0≈0.957`, masses `(2.91, 0.043, 0.043)`) — but at **leading order the two
  light generations are degenerate** (`e=μ`), which is not observed. The e–μ
  splitting needs a **secondary, subleading** breaking.
- **(B) The simplest 3-distinct pattern `(M0+d, M0, M0−d)` CAPS at `Q=0.5`** (as
  the lightest → 0), not 2/3. *(This corrects the prior "passes 2/3": that
  reading was `Q_max=0.515` for this pattern.)*
- **(C)** A genuinely 3-distinct, steep hierarchy (`~(2.85, 0.15, ~0)`) **can**
  give `Q=2/3`, but it is a **fine point** in the traceless plane, not the
  energetically-cheapest direction.

## Why this matters: it sidesteps the central chirality gate
The whole multi-lens Koide campaign hit one wall — `koide_z3_equivariant_
anticommuting_no_go` (retained_bounded): no native **operator** anticommutes
with `Γ_χ` on the generation R³. But that is a statement about
**eigenvectors**. Q depends only on **eigenvalues**. The Jahn-Teller
mechanism sets eigenvalues by spontaneous vacuum anisotropy **without writing
any chiral grading** — so the operator-level no-go is **orthogonal** to it.
This is the first **native** route to the *value* that the entire
operator-level campaign could not see, and it is exactly the audit's reframe
("the chirality wall is orthogonal to the value") made concrete.

## Honest status
A **native candidate mechanism** for the generation hierarchy: a fermion-sea
Jahn-Teller instability spontaneously breaks the cubic axis-symmetry, splitting
the near-critical (light) generation corners → hierarchical masses with Q in
`[1/3,1]`, **2/3 in range**, the value set by (criticality + stiffness@g_bare=1).

- **NOT a flat direction:** the value is set by a definite instability competing
  with a fixed (`g_bare=1`) stiffness — there is no free flavor knob.
- **NOT the blocked import:** spontaneous and eigenvalue-level, not a
  chiral-grading operator on R³.
- **NOT yet a derivation of 2/3,** and two concrete gaps remain:
  1. **Stiffness.** The fermion sea *alone* runs to **maximal anisotropy** (no
     interior minimum of `E_ferm(ε)` — it decreases monotonically to the
     boundary where one `r_μ→0`). So the breaking magnitude — hence Q — is set
     by a **stiffness** the fermion determinant does not supply. The *generic*
     gauge expectation is that the stiffness wins (symmetric vacuum, Q=1/3);
     whether the framework's specific (`g_bare=1`) stiffness lets the breaking
     win is a **full-action lattice computation** — and the stiffness is set by
     the same **action-derivation ("bridge gap")** that is itself an open
     frontier. The flavor value is downstream of the action derivation.
  2. **e–μ degeneracy.** The energetically-preferred pattern leaves the two
     light generations degenerate at leading order; the observed `e≠μ` needs a
     secondary breaking not yet identified.

This is the concrete, computable, **open** derivation target the
"nonperturbative value" relocation pointed to: a definite native mechanism
whose outcome is a lattice number, with a real structural hint (the cheapest
pattern matches the gross "1 heavy + 2 light" lepton structure) and two named
gaps (stiffness from the action; e–μ splitting). Not a wall, not a flat
direction, not yet a derivation.
