# Flavor — the native staggered hw=1 projection induces a diagonal but exactly-zero generation hopping (democratic r=0); the on-site:hopping ratio is not geometry-fixed at the charged-lepton point

**Date:** 2026-06-02
**Claim type:** a derived geometric fact about the framework's matter sector + a negative on the value axis. Not closure.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade.
**Runner:** `scripts/flavor_hw1_staggered_projection_democratic_r0_2026_06_02.py` (SCORECARD 5/5).

## Question
Door A asked whether the framework's actual mass-operator *construction* (rather than a prior on
couplings) geometrically fixes the charged-lepton ratio `r = |b|²/a²` at `r=1/2` (`Q=2/3`). The most
promising geometric sub-route: is the on-site term `a` not a free Yukawa but **induced** by the
lattice geometry when the full multi-corner-qubit operator is projected onto the 3-dimensional hw=1
generation sector?

## Result — native projection forces the *democratic* endpoint r=0, not r=1/2
With one `M₂(ℂ)` qubit per corner and the native staggered single-bit-flip generators on 3 corner
qubits (`ℂ⁸`),
```
G₁ = σx ⊗ I ⊗ I ,   G₂ = σz ⊗ σx ⊗ I ,   G₃ = σz ⊗ σz ⊗ σx ,
```
the hw=1 single-excitation sector is `span{|100⟩,|010⟩,|001⟩}` (basis index set `{1,2,4}`). Computing
the induced generation hopping:

- The **direct** hw=1 block of the native kinetic term `K = Σ Gᵢ` has **exactly zero** off-diagonal
  hopping (verified `max|off-diag| = 0`).
- The **Schur-complement induced** hopping `b`, swept over 401 reference energies `z ∈ [−3,3]`, is
  **exactly zero** (`max induced |b| ≈ 1e-14`). The second-order path through the vacuum `|000⟩`
  (staggered sign `+1`) is cancelled exactly by the path through the doubly-excited state (staggered
  sign `−1`).

The induced **diagonal** `a` is nonzero. So the projection geometry alone gives `b ≡ 0`, hence

> **r = |b|²/a² = 0  ⇒  Q = 1/3** (the S₃-democratic endpoint),

which is the *opposite* of the charged-lepton point `r=1/2`. To obtain any nonzero generation
hopping one must separately add a native bivector term, whose coefficient relative to the by-hand
mass is unconstrained by the projection.

## Consequence
This is a clean, derived geometric statement: **the native single-bit-flip staggered projection onto
hw=1 induces a diagonal but exactly-zero generation hopping (democratic r=0) by staggered-sign path
cancellation.** On the value axis it is a *negative*: projection geometry does **not** pin the
on-site:hopping ratio at `r=1/2`; the charged-lepton value is not delivered by the projection. It
narrows where any derivation of `r=1/2` must come from — not from the projection geometry of the
native staggered operator.

## The next paths this opens (not closing)
- The nonzero generation hopping must be sourced by a native bivector / a specific action term; the
  ratio of that term to the diagonal is the live question (companion: the equal-block-HS unification
  note, and the open native-action-form question).
- The `r=0` democratic endpoint may itself be the correct reading for an *unbroken* (e.g.
  neutrino-like) sector on the same line `Q = 1/3 + (2/3)r`; that sibling-sector reading is a
  separate question this fact supports.

## Provenance (verified 2026-06-02)
- Direct and Schur-induced hopping zero, induced diagonal nonzero, `r=0` ⇒ `Q=1/3`: verified
  directly (runner 5/5). Construction from the four-lane Door-A analysis (workflow `wf_c8faf07e`).
- This note sets no audit status; it records a derived computational fact and a value-axis negative.
