# 't Hooft 1981 Dual-Superconductor / Center-Vortex Confinement — External Narrow Theorem

**Date:** 2026-05-16
**Claim type:** positive_theorem
**Scope:** external 4D SU(N) Yang-Mills confinement mechanism: abelian
projection with residual U(1)^(N-1), magnetic monopole condensate (dual
superconductor) giving Wilson-loop area law, equivalent center-vortex
picture with Z_N center symmetry breaking, and the standard symbolic
vortex / monopole free-energy form. Cited only as published gauge-theory
context ('t Hooft 1978, 1981; Mandelstam 1976; Greensite 2011;
Del Debbio-Faber-Greensite-Olejnik 1996). No framework substrate
identification, hierarchy closure, scale ratio derivation, or
`α_LM^16` substitution is claimed.
**Status authority:** independent audit lane only; pipeline-derived
status set by `compute_effective_status.py`.
**Runner:** [`scripts/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py`](../scripts/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.txt`](../logs/runner-cache/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.txt)

## Claim

Let `A_μ(x)` be a smooth Euclidean SU(N) gauge connection on `R^4` (or
on a 4-torus compactification), with field strength

```text
F_μν = ∂_μ A_ν - ∂_ν A_μ + i [A_μ, A_ν].
```

The Euclidean Yang-Mills action is

```text
S[A] = (1 / (4 g²)) ∫ d^4x  Tr( F_μν F^μν ).
```

**Statement (external theorem; 't Hooft 1981; Mandelstam 1976):**

1. *Abelian projection.* For SU(N) gauge theory, fix a gauge by
   diagonalizing a chosen adjoint composite field `X(x)` ('t Hooft 1981).
   In a generic configuration `X(x)` is non-degenerate almost everywhere,
   and the residual gauge symmetry after diagonalization is the maximal
   abelian subgroup `U(1)^(N-1) ⊂ SU(N)`. Defects where two eigenvalues
   of `X(x)` coincide form codimension-3 loci in 4D Euclidean spacetime;
   these are the worldlines of **magnetic monopoles** carrying U(1)^(N-1)
   magnetic charge dual to the electric Wilson-line charge.

2. *Dual-superconductor / monopole condensate.* (Mandelstam 1976;
   't Hooft 1981.) If the magnetic monopoles **condense** — i.e., a
   gauge-invariant monopole creation operator `φ_mono(x)` acquires a
   non-zero vacuum expectation value `⟨φ_mono⟩ ≠ 0` — then by the
   electric-magnetic dual to the Meissner effect, **electric flux is
   confined into thin flux tubes** between colored charges, producing a
   **Wilson-loop area law**:

   ```text
   ⟨ W(C) ⟩  ~  exp(- σ × Area(C) ),     for large loops C,
   ```

   where `σ > 0` is the string tension. The vacuum free-energy density
   contributed by a dilute monopole gas carries a structural factor

   ```text
   f_mono ~ - exp( - S_mono ) × ( zero-mode determinant ),
   ```

   with `S_mono` the classical monopole action; the corresponding
   monopole-condensation phase is the dual superconductor.

3. *Equivalent center-vortex picture.* (Mandelstam 1976; 't Hooft 1978;
   Greensite 2011 review arXiv:0810.4392; lattice realization
   Del Debbio-Faber-Greensite-Olejnik arXiv:hep-lat/9609025.) In the
   center-vortex picture, magnetic disorder is carried by closed
   codimension-2 worldsheets (`Z_N` vortices) on which Wilson loops in
   the fundamental representation pick up a center phase
   `z = exp(2π i k / N)`, `k ∈ {1, ..., N-1}`. The condensate of `Z_N`
   center vortices breaks the global `Z_N` **center symmetry** of pure
   SU(N) Yang-Mills and produces the same area-law confinement: a
   Wilson loop linking `n` vortices on average picks up a center phase,
   and a random distribution of vortices over the minimal surface
   spanning the loop yields

   ```text
   ⟨ W(C) ⟩  ~  exp(- σ_vortex × Area(C) ),
   ```

   with `σ_vortex` set by the planar vortex density.

4. *Symbolic vortex action and condensate condition.* The vortex
   classical action per unit transverse area scales as

   ```text
   S_vortex ~ (1 / g²) × (string-tension factor σ a²),
   ```

   in lattice units `a`, where `σ a²` is the standard lattice
   string-tension factor. The **condensate condition** is that the
   exponential vortex weight is `O(1)` per unit transverse area:

   ```text
   exp( - S_vortex )  ~  O(1)   at confinement,
   ```

   reflecting the dual statement that vortex / monopole fugacity is
   large enough that the disorder field acquires a VEV. The monopole
   classical action carries an order-of-magnitude structural form

   ```text
   S_mono  ~  (8 π / g) × ( O(1) profile factor ),
   ```

   characteristic of a 't Hooft-Polyakov monopole in the U(1)^(N-1)
   subgroup ('t Hooft 1974; Polyakov 1974, cited for completeness as
   published context; the precise prefactor and profile depend on the
   Higgs sector chosen in the abelian projection).

5. *Center symmetry breaking signature.* On a 4-torus with one compact
   thermal-like direction or in pure Yang-Mills with `Z_N` global
   symmetry, the order parameter is the spatial Wilson loop / vortex
   creation operator. In the confining phase, vortex condensation
   manifests as `⟨ V ⟩ ≠ 0` for the disorder field `V`, dual to the
   Wilson-loop area law for the order field `W`. Center symmetry is
   broken by the vortex VEV in the disorder sector, equivalent to the
   Wilson-loop area law in the order sector (Kramers-Wannier duality
   between center order and vortex disorder).

6. *Area law as physical observable.* The defining physical observable
   of confinement is the area-law decay

   ```text
   - lim_{R, T → ∞}  (1 / (R T)) log ⟨ W(R × T) ⟩  =  σ  >  0,
   ```

   for the rectangular `R × T` Wilson loop in the fundamental
   representation, with `σ` the string tension. Both the monopole-
   condensate / dual-superconductor picture and the center-vortex picture
   predict this area-law decay; they are widely understood as
   complementary descriptions of the same confining vacuum (Greensite
   2011 review).

## Boundary

This note records an external 4D Yang-Mills confinement theorem and its
standard published lattice-gauge context. It does **not** claim:

- that the framework's substrate is identified with the dual-
  superconductor / monopole-condensate / center-vortex mechanism (no
  identification of any framework substrate, lattice cell, taste,
  blocking, plaquette family, or project-specific structure with the
  't Hooft 1981 abelian-projection vacuum);
- that the 4D SU(N) Wilson lattice is identified with any
  framework-specific lattice;
- closure of any framework substitution, hierarchy formula, scale
  ratio, or physical observable;
- closure of the `α_LM^16` substitution or any framework `α^N`
  hierarchy at integer `N`;
- closure of `v/M_Pl` or any other dimensional scale ratio (the
  electroweak hierarchy is **not** claimed; the note records only the
  confinement mechanism as a standalone external theorem);
- derivation of the string tension `σ` from framework primitives — the
  external string-tension factor `σ a²` is named symbolically, and
  numerical values of `σ` from lattice or experiment together with any
  derivation of `σ` from framework primitives are not asserted here;
- any numerical prediction or comparison with observation beyond the
  published gauge-theory context;
- any new framework axiom or repo-wide premise.

Any later framework use must separately identify the framework
substrate with the 4D SU(N) gauge background, identify a framework
observable with the Wilson loop or vortex condensate, and verify the
substrate-specific bridge.

## External References

- G. 't Hooft, "Topology of the gauge condition and new confinement
  phases in non-abelian gauge theories", Nucl. Phys. B **190** [FS3]
  (1981) 455 (abelian projection; magnetic monopole condensate).
- G. 't Hooft, "On the phase transition towards permanent quark
  confinement", Nucl. Phys. B **138** (1978) 1 (center symmetry
  breaking; disorder operator).
- S. Mandelstam, "Vortices and quark confinement in non-abelian gauge
  theories", Phys. Rep. **23** (1976) 245 (original dual
  superconductor mechanism).
- J. Greensite, "An introduction to the confinement problem", Lect.
  Notes Phys. **821** (2011); review arXiv:0810.4392 (modern
  center-vortex review).
- L. Del Debbio, M. Faber, J. Greensite, Š. Olejnik, "Center dominance
  and Z₂ vortices in SU(2) lattice gauge theory", arXiv:hep-lat/9609025
  (lattice center-vortex observable; center dominance).
- G. 't Hooft, "Magnetic monopoles in unified gauge theories",
  Nucl. Phys. B **79** (1974) 276 (monopole action structure).
- A. M. Polyakov, "Particle spectrum in quantum field theory",
  JETP Lett. **20** (1974) 194 (independent monopole solution; cited
  for completeness).

## Verification

The paired runner checks (in exact Fraction arithmetic with SymPy `pi`
symbolic where appropriate):

1. **T1**: abelian-projection structure — residual gauge group after
   diagonalization of the adjoint composite is `U(1)^(N-1) ⊂ SU(N)`;
   stated symbolically for general `N` and verified for `N = 2, 3`.
2. **T2**: vortex action symbolic form
   `S_vortex = (1 / g²) × (σ a²)` reproduced from the published center-
   vortex parameterization.
3. **T3**: at SU(3) with `g² = 1` and lattice `σ a² = 1`, the
   symbolic vortex action `S_vortex = 1` (named symbolically; no
   numerical confinement claim).
4. **T4**: monopole action order-of-magnitude form
   `S_mono ~ (8 π / g) × O(1)` recorded as published symbolic shape
   (no precise prefactor asserted; runner verifies the structural form
   only).
5. **T5**: condensate condition `exp(-S_vortex) ~ O(1)` at confinement
   recorded as a symbolic / qualitative threshold.
6. **T6**: Z_N center-symmetry-breaking signature — note states that
   vortex condensation breaks center symmetry and is dual to the area
   law (Kramers-Wannier duality between order and disorder fields).
7. **T7**: area-law observable
   `- lim (1 / (R T)) log ⟨ W(R × T) ⟩ = σ > 0`
   stated as the canonical Wilson-loop confinement diagnostic; runner
   verifies the formula is present in the note.
8. **T8**: source-note boundary — note declares `claim_type:
   positive_theorem`.
9. **T9**: boundary disclaimer — note does **not** claim framework
   substrate identification.
10. **T10**: boundary disclaimer — note does **not** claim
    `α_LM^16` closure, hierarchy closure, or scale ratio derivation.

Expected runner result: `PASS=N`, `FAIL=0`.
