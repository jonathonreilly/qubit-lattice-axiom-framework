# Koide Q=2/3 Extremal-Bridge Panel — Findings (local exploration)

**Date:** 2026-05-28
**Status:** panel-exploration working note. NOT a theorem note, NOT an audit
verdict, NOT a PR candidate. Local-branch record only. Sets no retained
status. Adds no axiom/import/vocabulary.
**Scope:** attack the #2 audit-ledger open item — the source law that would
force the physical charged-lepton packet to extremize the block-total
Frobenius functional (F1) on `Herm_circ(3)`, selecting BAE `|b|²/a²=1/2`
hence Koide `Q=2/3`.

## The crux, stated sharply

On `Herm_circ(3)`, `H = aI + bC + b̄C²`, the `C_3`-isotype decomposition
gives a 1-real-dim trivial isotype (`E_+ = 3a²`) and a 2-real-dim doublet
isotype (`E_⊥ = 6|b|²`, the conjugate-pair `{ω, ω̄}`). The whole bridge is
the weight pair `(μ, ν)` in `S = μ·log E_+ + ν·log E_⊥`, whose constrained
extremum sits at `κ = a²/|b|² = 2μ/ν`:

- **F1** = `(1,1)` (one weight per real-irreducible isotype) → `κ=2` → BAE → **Koide Q=2/3**.
- **F3** = `(1,2)` (weight by real dimension) → `κ=1` → **no Koide**.

Everything reduces to selecting F1 over F3. The 30-probe BAE campaign found
the tested retained-dynamics packet selects **F3** (`κ=1`).

## Panel composition

Four physicist perspectives + a literature disambiguator attacked
independently, then were cross-examined:

1. Representation theory
2. Lattice QFT (path-integral measure)
3. Variational principles / statistical mechanics
4. Mathematical physics (gauge Casimir / Weyl-vector routes E & F)
5. Literature-search wrong-escape disambiguator

## The one escape candidate that reached F1 — and why it fails

The lattice-QFT perspective proposed the only route that *reaches* F1: the
doublet parameter `b = |b|e^{iθ}` carries amplitude `|b|` and phase
`θ = arg(b)` (the Brannen clock phase). If `θ` is a flat zero mode, a
Faddeev–Popov extraction of its orbit volume should collapse the doublet's
two real dof to one amplitude, converting the measure weight `2 → 1`
(F3 → F1), forcing `κ=2`.

**Cross-examination refuted this on three independent grounds, any one fatal:**

### (A) Measure-theory error — FP orbit extraction does not reduce the radial Jacobian
The doublet partition function is
`Z_⊥ = ∫ d²b e^{-S(|b|)} = ∫ |b| d|b| dθ · e^{-S(|b|)}`.
Because the `C_3`-invariant action depends only on `|b|`, the `∫dθ = 2π`
factors out as a constant. **But the remaining radial measure is still
`|b| d|b|`** — the `|b|^{k-1}` factor with `k=2`. A Gaussian block of `k`
real dof gives `Z ∝ E^{k/2}`, hence effective weight `ν ∝ k`. Extracting the
constant angular orbit does **not** change `k`: `∫|b|d|b|·e^{-c|b|²} ∝ c^{-1}`,
the `k=2` scaling. A genuine `k=1` mode has measure `d|b|` (no Jacobian),
which requires the block to be 1-real-dimensional from the start (`b∈ℝ`).
Even hard-pinning `θ=θ₀` via `δ(arg b − θ₀)` leaves `∫|b|d|b|` intact. So the
doublet retains its dimension-2 (`k=2`) weight; **F3 stands**. The "2→1
collapse" conflates *factoring out the angular orbit volume* (a constant)
with *reducing the radial Jacobian power* (the actual dof count). They are
not the same operation.

### (B) Orthogonality — Koide is a radial (amplitude) condition, independent of the phase
With eigenvalues `λ_k = a + 2|b|cos(arg b + 2πk/3)` ≡ Brannen
`√m_k = μ(1 + 2η cos(δ + 2πk/3))`, one has `μ=a`, `η=|b|/a`, `δ=arg(b)`.
Since `Σ√m = 3μ` regardless of `δ`, `Q = (1+2η²)/3`, so

> **Koide Q=2/3 ⟺ η² = 1/2 ⟺ |b|²/a² = 1/2 ⟺ BAE ⟺ κ=2 — and is COMPLETELY INDEPENDENT of the phase δ = arg(b).**

Koide is a constraint on the **radial** coordinate `|b|/a`. Anything done to
the **angular** coordinate `arg(b)` — quotienting, pinning, APS-η — cannot
control `|b|/a`. The framework's own Route-F runner confirms this:
`(a=1, b=1)` has `arg(b)=0` and satisfies every retained constraint, yet
`|b|²/a²=1 ≠ 1/2`. **This retires the entire phase-based escape family
(phase-quotient, APS-η pinning, SO(2)/U(1)_b quotient) as a category error:
they attack the wrong coordinate.**

### (C) Circularity — the pinned phase is itself downstream of Koide
The retained `KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20`
proves `δ = Q/d` with `Q=2/3` as the retained observational input (I1), and
states "closing I1 (Q=2/3) closes I2 (δ=2/9) automatically." So `δ=2/9` is a
*corollary* of Koide, not an independent input. Using the pinned phase to
select F1 = Koide re-imports the conclusion (`σ₁=1/2` = BAE) through the back
door. Confirmed against the literature: in Brannen's form, `η²=1/2` (Koide)
and `δ` are independent fitted parameters, and the measured masses are in
mild conflict with *simultaneous* exactness of `η²=1/2` and `δ=2/9`.

## What the canonical measures actually select (sharper negative)

Three independent perspectives converged that the **natural/canonical**
measure selects **F3, not F1**:

- **Wedderburn / block-determinant:** `ℝ[C_3] ≅ ℝ ⊕ ℂ`. The doublet is the
  `ℂ` factor, real-dimension 2; `det` of a scalar `β` on it is `β²`. So
  `log det(ℝ) + log det(ℂ) = log E_+ + 2 log E_⊥ = F3` (`κ=1`). This is the
  one-loop / analytic-torsion structure: each irreducible sector contributes
  its determinant **with its dimension as multiplicity**.
- **Plancherel / Peter–Weyl:** the canonical measure on the dual weights by
  dimension. The doublet's dim-2 weight is the genuine Weyl/Vandermonde
  Jacobian, nonzero off the measure-zero coincident-eigenvalue wall.
- **Every surveyed variational principle** (Theorem 5's six, plus Gaussian
  path-integral, Born-rule, von Neumann entropy) carries a microstate/dimension
  measure → F3 or a degenerate triplet. **None** used bare isotype-counting.

F1 = `(1,1)` is reachable only via "block democracy" (treat each isotype as a
single undifferentiated scalar, ignoring that the doublet is 2-dimensional) —
the SO(2)/U(1)_b quotient named in Probe 13. The literature endorses
dimension-weighting (F3) for integrating a continuous functional over a group
dual; isotype-counting (F1) is the wrong measure for that purpose.

## New finding — Route F is convention-CONTRADICTED, not convention-dependent

Route F's `T(T+1) − Y² = 1/2` requires the PDG `Y(L) = −1/2`. The retained
`CL3_SM_EMBEDDING_THEOREM` **derives** `Y = (+1/3)P_symm + (−1)P_antisymm`,
i.e. `Y(L) = −1` (verified eigenvalues `+1/3 ×6, −1 ×2`, `Tr Y = 0`), giving
`T(T+1) − Y² = 3/4 − 1 = −1/4 ≠ 1/2` (runner cache line 20). So the framework
does not merely stay silent on the normalization — its own retained theorem
points *away* from 1/2. Route F would have to **override a retained theorem**
to reach its target. The existing bounded-obstruction classification should
be sharpened from "convention-dependent" to "convention-contradicted by the
retained embedding theorem." (Route E analogously fails: `|ρ_{A_1}|²` is
normalization-soft `{1/4, 1/2, 1}`, the A₂ double-match needs an `sl(3)` the
framework retains 0/8 generators of, and no gauge→flavor bridge exists. Both
routes reproduce the *value* 1/2 only *conditional on F1 already chosen*;
neither addresses the F1-vs-F3 functional selection at all.)

## Verdict

**No escape.** The single functional-selection route that reaches F1
(phase-quotient) is refuted three ways: (A) a measure-theory error (orbit
extraction ≠ Jacobian reduction; doublet keeps its dim-2 weight), (B)
orthogonality (Koide is the radial condition `η²=1/2`, independent of the
phase the route manipulates), and (C) circularity (`δ=Q/d` makes the pinned
phase downstream of Koide). The canonical measures (Wedderburn determinant,
Plancherel, Weyl–Vandermonde) actively select **F3 (κ=1)**, a sharper
negative than "F1 unselected." Routes E/F reproduce the value 1/2 but never
touch the weighting question, and Route F is contradicted by retained content.

**The genuine residual atom (triangulated from rep-theory, variational, and
literature):** a *principled* selection of the **intensive (isotype-counting /
block-democracy) measure over the extensive (dimension / Plancherel) measure**
on the `C_3`-isotype lattice of `Herm_circ(3)` — equivalently a derivation
that the charged-lepton scalar lane factors through the SO(2)-orbit invariant
`|b|`, treating each isotype as one scalar order parameter. Standard harmonic
analysis says the *canonical* choice is the dimension measure (F3), so the
framework needs a positive, charged-lepton-specific reason to use the counting
measure — and no such reason exists in retained content. This matches the
campaign residue verbatim; the panel adds (i) the orthogonality observation
that retires the phase-based escape family as a category error, and (ii) the
Route-F convention-contradiction sharpening.

## Honest forward steps (negative results worth recording, pending user direction)

1. A narrow note ruling **out** two specific F1 routes by explicit
   computation: (a) the reduced-norm / regular-rep Wedderburn-Frobenius
   construction does **not** reproduce `E_+ = 3a²`, `E_⊥ = 6|b|²`; (b) the
   block-determinant principle is canonical but lands on **F3**.
2. Record the orthogonality fact (Koide ⟺ `η²=1/2`, independent of `δ`) as the
   reason the phase-based escape family (APS-η, SO(2)-quotient, phase-pinning)
   cannot close BAE: BAE is a radial constraint; those routes act on the angle.
3. Sharpen the Route-F bounded obstruction to "convention-contradicted."

These are negative/scoping results; none closes BAE. Any positive closure
still requires either a new charged-lepton-specific measure-selection primitive
(which would need explicit user approval as an admission) or a genuine
gauge→flavor bridge — neither present in retained content.

## Files consulted (all on `origin/main`)

- `docs/BAE_BLOCK_TOTAL_FROBENIUS_DERIVATION_NARROW_THEOREM_NOTE_2026-05-16.md`
- `docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`
- `docs/KOIDE_A1_DERIVATION_STATUS_NOTE.md`
- `docs/KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md`
- `docs/KOIDE_A1_PROBE_PLANCHEREL_PETER_WEYL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe12.md`
- `docs/KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md`
- `docs/KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`
- `docs/BAE_MAX_ENTROPY_RETAINED_BOUNDED_OBSTRUCTION_NOTE_2026-05-10_baemaxent.md`
- `docs/CL3_SM_EMBEDDING_THEOREM.md`
- `logs/runner-cache/cl3_koide_a1_route_f_casimir_difference_2026_05_08_routef.txt`
