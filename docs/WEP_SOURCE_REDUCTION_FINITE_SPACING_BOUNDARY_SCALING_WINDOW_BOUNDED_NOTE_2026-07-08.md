# Free Source-Function Formulas and a Finite Composite Comparator — Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** Conditional on the supplied free band, this note records exact
single-particle and free-composite formulas. It also records one finite
contact-model comparison. It makes no universal WEP, source-law, or no-go
claim.

**Primary runner:**
[`scripts/wep_source_reduction_scaling_window_2026_07_08.py`](../scripts/wep_source_reduction_scaling_window_2026_07_08.py)

**Runner cache:**
[`logs/runner-cache/wep_source_reduction_scaling_window_2026_07_08.txt`](../logs/runner-cache/wep_source_reduction_scaling_window_2026_07_08.txt)

## Imported Surface and Open Dependencies

Let
\[
x=m_{\rm gap}=\operatorname{arsinh}(m),\qquad
M_I=m\sqrt{1+m^2},\qquad
F(x)=\frac12\sinh(2x).
\]
These are inherited from the paired rest-gap note, whose band dependency
remains unaudited. The finite comparison below uses the imported contact model
from the composite-additivity note. Neither source is promoted here.

## Conditional Single-Particle Formula — Exact

Suppose, as an additional model assumption, that a source coefficient is a
species-blind function \(G(x)\) of the rest gap alone and that the ratio
\(G(x)/M_I(x)\) is one constant \(c\) for every supplied single-particle mass.
Then
\[
G(x)=cM_I(x)=cF(x).
\]
This is an algebraic conditional, not a derivation of a physical source law.

## Equal-Mass Free-Composite Formula — Exact

Free additivity gives rest energy \(2x\) and reciprocal-curvature coefficient
\(2F(x)\). Applying the same mathematical function to the summed rest energy
gives
\[
\frac{F(2x)}{2F(x)}=\cosh(2x).
\]
The runner verifies this identity symbolically and records
\[
\cosh(2x)-1=2x^2+O(x^4).
\]
This comparison says only that these two explicitly defined prescriptions
differ at finite \(x\). It does not rule out other source variables,
interactions, or physical realizations.

## Small-Parameter Formulas — Exact

The free expressions have the expansions
\[
1-\frac{1}{\sqrt{1+m^2}}=\frac12m^2+O(m^4),
\]
\[
\frac{F(x)}{x}-1=\frac23x^2+O(x^4),
\]
and
\[
\frac{F(2x)}{2F(x)}-1=2x^2+O(x^4).
\]

## Same-Rest-Energy Contact Comparison — Finite Measurement

On an \(L=64\) ring, the runner tunes two points of the supplied contact
family to the same measured \(K=0\) energy and extracts their curvature masses
from nearby momentum blocks. It prints the tuned couplings, energy mismatch,
fit residuals, and measured mass separation. Its PASS gate requires both
fitted curvature masses to be finite and positive and the maximum fit residual
from an overdetermined five-point-in-`p^2` window to be at most `1e-6`. This
finite observation is not promoted to a statement
about all static interactions or all composites.

## Boundaries

- Exact content is limited to the displayed free formulas.
- The contact result is a finite measured comparator.
- No gravitational coupling, WEP closure, universal negative claim,
  mediator requirement, or framework-source reduction is asserted.
- Because no negative claim remains, the no-go-discipline gate is not
  applicable to this narrowed source note.
- No audit result is predicted.

## Dependencies

- [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  supplies \(x\), \(M_I\), and \(F\), and remains unaudited.
- [`COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md`](COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md)
  supplies the free-additivity identity and the finite contact comparator,
  and remains unaudited.

## Reproduction

```bash
python3 scripts/wep_source_reduction_scaling_window_2026_07_08.py
```

The cache is regenerated only from a green run.
