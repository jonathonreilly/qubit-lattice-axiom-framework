# Composite Free Additivity and Finite Contact Comparator on the Two-Step Surface — Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** On the supplied one-dimensional two-step band, this note
proves the fixed-total-momentum reduction and free two-particle additivity.
It also records a finite measured contact-interaction comparator. The finite
comparator is not an interaction theorem or a universal source statement.

**Primary runner:**
[`scripts/composite_mass_additivity_binding_defect_2026_07_08.py`](../scripts/composite_mass_additivity_binding_defect_2026_07_08.py)

**Runner cache:**
[`logs/runner-cache/composite_mass_additivity_binding_defect_2026_07_08.txt`](../logs/runner-cache/composite_mass_additivity_binding_defect_2026_07_08.txt)

## Imported Surface and Open Dependencies

For species \(s\in\{a,b\}\), take the supplied band
\[
E_s(p)=\operatorname{arsinh}\sqrt{m_s^2+\sin^2p}.
\]
The paired rest-gap note and its d-dimensional dispersion authority remain
unaudited. Two distinguishable particles on a finite ring are part of the
model definition. The attractive contact term \(-U\delta_{x_a,x_b}\) is an
imported finite comparator only.

## Fixed-Total-Momentum Reduction — Exact

For ring size \(L\), total-momentum index \(K\), and \(P_K=2\pi K/L\), the
relative-coordinate block is
\[
H_K(r,r')=
\frac1L\sum_q e^{iq(r-r')}
 [E_a(q)+E_b(P_K-q)]-U\delta_{r0}\delta_{r'0}.
\]
Translation invariance decomposes the full two-particle Hamiltonian into these
\(L\) blocks. Therefore the union of the block spectra equals the full
two-particle spectrum. The runner checks this identity at \(L=12\).

## Free Additivity — Exact

At \(U=0\),
\[
E_{ab}(p_a,p_b)=E_a(p_a)+E_b(p_b),
\]
so the free rest energy is
\[
E_{ab}(0,0)=\operatorname{arsinh}(m_a)+\operatorname{arsinh}(m_b).
\]
For equal masses and an even momentum index, the discrete grid contains
\(q=P/2\), and near rest the band minimum is
\[
E_2(P)=2E(P/2).
\]
Consequently
\[
E_2''(0)=\frac{1}{2M_I},
\qquad M_{I,\mathrm{free pair}}=2M_I.
\]
For a product state and the free Hamiltonian
\(H_0=h_a\otimes1+1\otimes h_b\), expectation values add exactly. Spatial
overlap of distinguishable wave packets does not alter this tensor-product
identity.

## Finite Contact Comparator — Measured, Not a Theorem

The runner diagonalizes the finite \(L=64\) contact blocks for
\[
m\in\{0.5,1.0\},\qquad U\in\{0.2,0.8\}.
\]
It reports whether the lowest \(K=0\) level lies below the finite-ring free
continuum edge and prints the measured separation. This is only a finite
comparator for the supplied contact model. It does not establish binding for
all couplings, interaction shapes, volumes, or framework realizations.

## Boundaries

- One-dimensional supplied band and distinguishable species only.
- The exact claim consists only of the momentum-block reduction and free
  additivity formulas.
- The contact result is explicitly finite and measured.
- No universal source functional, WEP statement, static-comparator no-go,
  persistence claim, or derived interaction is included.
- No audit result is predicted.

## Dependencies

- [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  supplies the conditional one-particle band algebra and remains unaudited.
- [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
  is the still-unaudited source of the supplied band.

## Reproduction

```bash
python3 scripts/composite_mass_additivity_binding_defect_2026_07_08.py
```

The cache is regenerated only from a green run.
