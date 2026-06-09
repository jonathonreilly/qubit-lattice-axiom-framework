# R2: Stress Conservation Is Noether-Derived From Exact Z³ Translation — the O(k) Contact Is the Seagull, Not a Non-Conservation; the Residual Relocates to the Symmetric (Belinfante) Form

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** Noether derivation + residual relocation (R2, the crux of the graviton-diffeomorphism exercise chain)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/r2_stress_conservation_noether_seagull_2026_06_08.py`](../scripts/r2_stress_conservation_noether_seagull_2026_06_08.py) (PASS=4).

## The gate

The graviton-diffeomorphism exercise's strongest framework-native lever (R2): **Z³ translation invariance
→ Noether → conserved `T^{μν}` → [proven: `δ(½h_{μν}T^{μν}) = −ξ_ν∂_μT^{μν}` + total-deriv] gauge
invariance iff `∂_μT^{μν}=0` → (Barnich–Henneaux) diffeomorphisms → λ=1 → (reflection positivity) G>0.**
The crack: the prior cubic-Ward notes
([`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md),
[`UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE`](UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md))
found the lattice stress vertex leaves an **O(k) contact = half the amplitude**, so `∂_μT^{μν}=0` appears
to fail. R2 asks: is that a genuine non-conservation, or the (derivable) seagull?

## Result (R2 PASSES the conservation; the crack is the seagull)

**Exact Z³ (Z⁴ with emergent time) translation invariance is an axiom-level symmetry, and Noether's
theorem guarantees an exactly-conserved lattice stress tensor.** Demonstrated on the free lattice scalar
(inverse propagator `G⁻¹(p) = m² + Σ_μ(2sin(p_μ/2))²`):

- **(R2a) The conserved (point-split) Noether current satisfies the EXACT lattice Ward identity.** With
  `q̂_μ = 2sin(q_μ/2)` and the point-split vertex `V^μ(p,q) = 2sin(p_μ + q_μ/2)`,
  > `q̂_μ V^μ(p,q) = G⁻¹(p+q) − G⁻¹(p)` exactly (max error `7×10⁻¹⁵` over 20000 random momenta).

  The Ward identity **is** the lattice conservation law (contact terms included) — exact conservation from
  exact translation invariance.
- **(R2b) The O(k) "contact" IS the derivable seagull.** A naive local vertex `V^μ_naive = 2sin(p_μ)` fails
  the Ward identity, and its failure equals **minus** the point-split-minus-naive seagull *exactly*
  (`q̂_μV^μ_naive − rhs = −q̂_μ(V^μ−V^μ_naive)`, max `6×10⁻¹⁵`). So the prior notes' "O(k) contact" is the
  **seagull** = the difference between the naive and the conserved (point-split) Noether current —
  **required by the symmetry, hence derivable**, not a genuine non-conservation.
- **(R2c) Noether at all orders.** The point-splitting that closes the 2-point Ward identity is the
  n-point Noether construction; the exact translation symmetry guarantees the conserved stress tensor with
  **all** its seagulls. The prior cubic O(k) contact is that seagull at 3-point — the same phenomenon
  (argued here by Noether; the explicit cubic Noether seagull, matching the prior notes' *supplied* one, is
  the follow-on, not re-derived here).

**So the conservation leg `∂_μT^{μν}=0` is DERIVED from the exact Z³ translation axiom symmetry — it is
not an open admission, and the "O(k) contact" crack is resolved as the Noether seagull.**

## The residual relocates to the symmetric (Belinfante) form

The graviton couples to the **symmetric** stress tensor; gauge invariance under `h→h+∂ξ` needs the
**symmetric part** conserved, `∂_μT^{(μν)}=0`. **(R2d):**
- **Scalar matter:** the canonical `T^{μν} = ∂^μφ∂^νφ − η^{μν}L` is already symmetric (verified) — R2
  fully holds.
- **Spinning (Dirac/qubit) matter — the framework's matter:** the canonical `T` is **not** symmetric (it
  carries the spin current); the Belinfante symmetrization needs **rotation invariance**, which on the
  cubic lattice is only **O_h** and becomes **SO(3) only emergently** (continuum). So the symmetric
  conserved stress tensor (the graviton source) is **emergent**.

**Therefore R2 reduces the stress-conservation gate from "is `T` conserved at all?" (now answered: yes, by
Noether) to "does `T` acquire the symmetric (Belinfante) form, i.e. emergent SO(3) rotation invariance
(O_h → SO(3))?"** — the emergent-Lorentz frontier and the exercise's catch-22.

## What is and is not claimed

- **Is:** stress conservation `∂_μT^{μν}=0` is Noether-derived from the exact Z³ translation axiom symmetry
  (the conserved point-split current satisfies the exact lattice Ward identity, R2a); the prior "O(k)
  contact" is the derivable seagull (R2b), not a non-conservation; the remaining residual is the symmetric
  (Belinfante) form for the framework's spinning matter = emergent rotation invariance (R2d). So R2 PASSES
  the conservation and sharply relocates the residual.
- **Is not:** does **not** explicitly construct the cubic (3-point) Noether seagull (argued by Noether,
  R2c — the explicit construction matching the prior notes is the follow-on); does **not** establish the
  emergent O_h→SO(3) rotation invariance (that is the separate emergent-Lorentz frontier, on which the
  symmetric form depends); does **not** by itself close λ=1 / G>0 (that needs the symmetric conserved `T` →
  diffeo → λ=1, i.e. the continuum). Adds no axiom or fitted value; form/sign level.

## Boundaries (honest)

- **2-point demonstration + Noether argument for higher points.** R2a/R2b are exact at 2-point; R2c is the
  standard all-orders Noether statement (an exact symmetry has conserved currents at every order), not an
  explicit cubic re-derivation. The prior notes' *supplied* cubic seagull should match the Noether one —
  that match is the next concrete artifact.
- **The residual is real.** Emergent SO(3) rotation invariance of the stress tensor is required for the
  symmetric (graviton-coupling) form; it is the emergent-Lorentz/catch-22 frontier, not closed here.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Z³ lattice with exact translation
  symmetry (the Noether source).
- [`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md),
  [`UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_CUBIC_DIFFEO_WARD_OPERATOR_TELESCOPE_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  — the prior cubic-Ward O(k) contact, here identified as the Noether seagull.

## Forbidden-imports check

No PDG / fitted value. The lattice Ward identity `q̂_μV^μ = G⁻¹(p+q)−G⁻¹(p)`, the point-split vertex, and
the seagull = point-split-minus-naive are standard lattice-field-theory Noether constructions, reproduced
exactly in the runner. The Belinfante/rotation statement is standard; the framework content is that its
spinning matter needs emergent O_h→SO(3) for the symmetric form.
