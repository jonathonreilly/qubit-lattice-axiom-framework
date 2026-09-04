# Composite Curvature Sum Rule and Band Controls — Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** For a supplied one-dimensional two-particle band Hamiltonian
with a total-momentum-independent relative potential, this note proves the
fixed-split Feynman–Hellmann curvature sum rule and records quadratic and
cosine-band controls. It does not assert split independence on a finite
periodic domain or a universal static-comparator no-go.

**Primary runner:**
[`scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py`](../scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py)

**Runner cache:**
[`logs/runner-cache/composite_mass_energy_equivalence_static_comparator_2026_07_08.txt`](../logs/runner-cache/composite_mass_energy_equivalence_static_comparator_2026_07_08.txt)

## Imported Surface and Open Dependencies

Take
\[
H_P=K_P+V,\qquad
K_P(q)=E(\alpha P+q)+E((1-\alpha)P-q),
\]
where \(V\) is a supplied relative-coordinate potential independent of total
momentum \(P\). The band and finite comparator construction are inherited from
the composite-additivity note, which remains unaudited. No interaction is
derived from the framework.

## Curvature Sum Rule — Exact

Let \(|0\rangle\) be a nondegenerate even bound state of \(H_0\), with excited
states \(|n\rangle\). Feynman–Hellmann and second-order perturbation theory give
\[
\frac1{M_{\rm comp}}
 =\langle0|A_\alpha|0\rangle
 -2\sum_{n\ne0}
 \frac{|\langle n|B_\alpha|0\rangle|^2}{E_n-E_0},
\]
where
\[
A_\alpha=\alpha^2E''(q)+(1-\alpha)^2E''(-q),
\qquad
B_\alpha=\alpha E'(q)+(1-\alpha)E'(-q).
\]
This identity holds for each fixed \(\alpha\) on the stated domain. Changing
\(\alpha\) is not generally a coordinate relabeling on a finite periodic grid:
it changes the relative-coordinate twist unless the boundary domain is
transformed with it. No finite-volume split-independence theorem is claimed.

For an even band at the symmetric split \(\alpha=1/2\),
\(B_{1/2}=0\), so
\[
\frac1{M_{\rm comp}}=\frac12\langle0|E''(q)|0\rangle.
\]
The potential affects the value through the bound-state wavefunction. This
identity alone makes no statement about what values all possible potentials
can or cannot realize.

## Quadratic-Band Control

For the analytic unbounded quadratic band
\[
E(q)=m+\frac{q^2}{2m},
\]
\(E''=1/m\) is constant and the symmetric formula gives
\[
M_{\rm comp}=2m
\]
independently of the supplied relative potential. The finite-ring runner
implements a signed-zone quadratic control; it gates the exact first-order
term and prints the small zone-edge artifact separately.

## Cosine-Band Control

For
\[
E(q)=m+\frac{1-\cos q}{m},
\]
the same sum rule gives
\[
\frac1{M_{\rm comp}}=\frac{\langle\cos q\rangle}{2m}.
\]
The runner checks this curvature against direct finite-band fits for contact
and finite-range wells. These are control examples, not a claim about the
entire class of static interactions.

## Boundaries

- One-dimensional supplied band and nondegenerate even bound state.
- The relative potential is imported and \(P\)-independent.
- The proposed bounded scope is limited to the fixed-split sum rule and the two
  stated controls.
- No finite-periodic split-independence claim is made; the small-ring runner
  explicitly resolves the split dependence at fixed boundary conditions.
- No universal mass-energy-equivalence negative, mediator necessity,
  WEP statement, or claim that Record supplies or forces interaction
  dynamics remains.
- No audit result is predicted.

## Dependencies

- [`COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md`](COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md)
  supplies the still-unaudited finite-ring band/comparator construction.

## Reproduction

```bash
python3 scripts/composite_mass_energy_equivalence_static_comparator_2026_07_08.py
```

The cache is regenerated only from a green run.
