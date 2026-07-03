# Global-Color Orientation Of The Matter State Is Predictively Vacuous

**Type:** bounded_theorem
**Scope:** predictive-equivalence / retire-mode refinement of the global color-neutrality admission.
**Primary runner:** [`scripts/frontier_color_orientation_predictive_equivalence_2026_06_09.py`](../scripts/frontier_color_orientation_predictive_equivalence_2026_06_09.py)
**Runner cache:** [`logs/runner-cache/frontier_color_orientation_predictive_equivalence_2026_06_09.txt`](../logs/runner-cache/frontier_color_orientation_predictive_equivalence_2026_06_09.txt)
**Date:** 2026-06-09

This note authors no `effective_status`, grade, or audit verdict for itself or any
cited note, and frames its result strictly as a source proposal; the independent
audit lane assigns status.

## Context — the admission this refines

The gauge-link / color-einselection campaign's
[`COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_DEPOLARIZATION_ADM2_GATING_ADMISSIONS_COLLAPSE_TO_TWO_NARROW_THEOREM_NOTE_2026-06-09.md)
converged onto two irreducible gauge-structure admissions, one of which is the
**global color-neutrality admission**:
a global color-singlet / Gauss-law physical-state condition on the matter color
density `rho_color` on the irreducible fundamental carrier `C^3`. That collapse
note recorded that *"the realized matter state is a global `SU(3)` singlet"* is **not
entailed** by *"observables are `SU(3)`-invariant"* — invariance of the observable
algebra constrains the commutant and leaves the sector free.

This note splits the global color-neutrality admission along its own internal
seam and retires one half. A color state `rho` carries, under the global
`SU(3)` action `rho -> U(g) rho U(g)^dag`, two separable kinds of data:

- its **orientation** — the position of `rho` within its `SU(3)` orbit;
- its **invariant content** — the spectrum / Casimirs of `rho` (the purity
  `Tr rho^2`, equivalently the block-04 order parameter `Tr rho^2 - 1/3`).

The claim: the **orientation** half is predictively vacuous and retires as a
source proposal; the **invariant** half (purity) is the genuine residual and is
the subject of the separate Part B reduction.

## Premise (named, conditional)

> **P.** The color observable algebra is the `SU(3)`-invariant subalgebra (the
> gauge principle: observables commute with the global `SU(3)` action).

`P` is the corpus-standard reading under which the global color-neutrality
admission is even posed. The color `SU(3)` itself is the **retained**
commutant structure of
[`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
(`graph_first_su3_integration_note` = `retained` on the live ledger): the joint
commutant on the graph-first surface is `gl(3) ⊕ gl(1)` with compact semisimple
part `su(3)`. The result below is stated **conditional on `P`**; it introduces no
new import and adds no axiom.

## Theorem (orientation retirement / predictive equivalence)

Conditional on `P`, for every state `rho`, every `g ∈ SU(3)`, and every
observable `O`:

```
    Tr( U(g) rho U(g)^dag · O )  =  Tr( rho · O ).
```

*Proof.* `O` is `SU(3)`-invariant (premise `P`), so `U(g)^dag O U(g) = O`. Then
`Tr(U(g) rho U(g)^dag O) = Tr(rho U(g)^dag O U(g)) = Tr(rho O)`. ∎

Hence **every record-level consequence** (a scalar readout of an observable) is
invariant under a global `SU(3)` rotation of the state. Two states related by a
global `SU(3)` rotation are predictively identical: no observable, at any time,
depends on the state's color **orientation**.

### What this retires, and what it does not

- **Retired (orientation).** Requiring a particular color orientation — a named
  color frame, a color direction, a specific point inside an `SU(3)` orbit — is
  predictively vacuous: it changes no observable expectation. The orientation
  component of the global color-neutrality admission is therefore a
  **retire-as-source-proposal** item, not a physical admission. (The
  predictive-equivalence check holds to the runner's
  exact-arithmetic tolerance.)
- **Not retired (purity).** The `SU(3)`-**invariant** content of `rho_color` — its
  spectrum, equivalently `Tr rho^2` — is preserved by the rotation and remains
  observable-distinguishable via two-copy invariants (the different-spectrum
  control is separated by purity). So the global color-neutrality admission
  splits as **orientation (retired here) ⊕ purity (the genuine residual)**; the
  purity half is the follow-on registrable surface and is **not** addressed here.

On the single irreducible carrier the invariant observable algebra is the scalars
(Schur; commutant dimension `1` in the runner): the only color invariants of
`rho` are functions of its spectrum, all orientation-blind. The orientation is
the orbit coordinate carrying zero invariant — which is precisely why it is
predictively inert.

## The r-dial teeth (the load-bearing guard)

The same argument must **not** force the Koide block-weight `r`. It cannot, and the
runner exhibits why:

- The global color `SU(3)` acts only on the **color** tensor factor. The
  generation / mass pattern — which carries `r` — is color-singlet and is left
  pointwise fixed (the `r`-readout is exactly invariant under a
  color-orientation rotation).
- Observables **do** depend on `r` (the `r`-readout distinguishes `r = 1/2`
  from `r = 1`), exactly as they depend on the masses. `r` is an
  `SU(3)`-**invariant** of the state, not an orientation coordinate.
- The asymmetry is structural: color **orientation** has an exact symmetry group
  (`SU(3)`) that makes it gauge, so the predictive-equivalence blade applies. `r`
  has **no** such symmetry — there is no transformation that moves `r` while
  fixing all observables — so the blade has nothing to act on. The argument
  retires a flat gauge direction and touches **no invariant**; `r` is an invariant,
  hence untouched.

This is the `COMMUTANT`-vs-`OBSERVABLE-COUPLED` distinction, not the demoted loose
register-not-read dichotomy: orientation is retired because an exact symmetry acts
along it (a precise statement), whereas `r` and the masses are coupled to
observables and stay physical.

## Precedents cited and distinguished

- **Same blade, different domain.**
  [`FLAVOR_PER_SECTOR_ORIENTATION_IS_GAUGE_CP_IS_INTER_SECTOR_NARROW_THEOREM_NOTE_2026-06-08`](FLAVOR_PER_SECTOR_ORIENTATION_IS_GAUGE_CP_IS_INTER_SECTOR_NARROW_THEOREM_NOTE_2026-06-08.md)
  retires *per-sector flavor* orientation as gauge under the **discrete**
  generation-relabeling `S_3` acting on the **mass matrix**. The present note is a
  **different gauge group** (continuous color `SU(3)`) acting on a **different
  object** (the matter **state's** color density inside the global
  color-neutrality admission). The shared
  pattern is "an orientation along which an exact symmetry acts is gauge"; the
  domains do not overlap.
- **Scope-correction precedent.** The loose register-not-read dichotomy was demoted
  (2026-06-06), and for color the genuine partition map is trivial on the
  irreducible triplet (panel `forced_finding`). The present argument does **not**
  use that dichotomy: it is the exact symmetry statement above, with teeth
  exhibited by the negative control: predictive equivalence **fails** for a
  non-invariant adjoint operator — the equivalence is specific to the invariant
  subalgebra, not vacuously true for all operators.

## No hat discharged

This retires the **orientation** data of the **state**. It delivers no pointer
frame, no partition, no twirl weight, and no depolarization — **purity is
untouched** (a polarized state stays polarized under rotation; the only
`SU(3)`-invariant projectors are `0, I`, so no nontrivial pointer set is
produced). It does **not** deliver a local connection, so it does not discharge
or short-circuit the static local color-frame redundancy: the statement is
global — one `g` for every site — and a global rotation commutes with a
site-shift, supplying no per-edge link data. The static local color-frame
redundancy, record-level reduction, residual color-state purity, and
blocking-isometry residuals are untouched.

## What this does NOT do (honest boundary)

- It does **not** show the matter state is a singlet, nor that `rho_color = I3/3`.
  The purity half of the global color-neutrality admission is left fully open.
- It does **not** derive the gauge principle `P`; `P` is named and the result is
  conditional on it. `P` is the same premise the global color-neutrality
  admission already lives under.
- It is **not** a no-go and is not closure language: it retires one half of one
  admission as predictively vacuous, leaving the purity half and the promotion
  routes of the campaign open.
- The carrier is the irreducible fundamental `C^3`; the conditionality of the
  supplied `C^3` color realization (`MR_color` residual) is inherited.

## What the runner verifies

Exact finite-dimensional linear algebra on `C^3`, `C^3 ⊗ C^3`, and `C^3 ⊗ C^3`
(gen ⊗ color); random `SU(3)` witnesses (fixed seed) for already-proven
identities, no Monte-Carlo fit in the logic path; memory-safe (`≤ 9×9`).
`TOTAL: PASS=19 FAIL=0`:

- **Color commutant checks:** 3 ⊗ 3̄ = 8 ⊕ 1: adjoint action preserves the traceless 8-block and fixes
  the singlet; an off-diagonal bilinear `E_12` (adjoint) is not invariant; the
  single-carrier color commutant is the scalars (dim 1, Schur).
- **Predictive-equivalence checks:** `<O>_rho = <O>_{g rho g†}` exact for an invariant
  `O` on `C^3 ⊗ C^3`.
- **Purity-residual checks:** orientation moves while the spectrum / purity is preserved exactly; purity
  distinguishes a different-spectrum state (the residual is real).
- **r-dial guard checks:** the `r`-readout is fixed by color rotation yet
  distinguishes `r`; a non-invariant color operator does move.
- **Negative control:** predictive equivalence fails for a non-invariant
  operator (teeth — specific to the invariant subalgebra).
- **Discipline guards:** no depolarization delivered (purity untouched), no
  frame delivered (only `0, I` invariant projectors), static local
  color-frame redundancy not short-circuited (global rotation commutes with
  the site-shift).
