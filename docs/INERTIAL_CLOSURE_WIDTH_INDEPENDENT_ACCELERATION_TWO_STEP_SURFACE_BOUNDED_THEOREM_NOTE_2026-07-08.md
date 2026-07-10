# Uniform-Force Acceleration on an Unwrapped Two-Step Quasimomentum Lift — Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** Conditional on the supplied free two-step band and on a
single-band uniform-force probe, this note states the exact transport law on
an unwrapped quasimomentum lift and an analytic local-curvature bound before
the packet reaches a Brillouin-zone seam. No assertion is made for the
principal-value mean momentum after wrapping.

**Primary runner:**
[`scripts/inertial_closure_two_step_surface_2026_07_08.py`](../scripts/inertial_closure_two_step_surface_2026_07_08.py)

**Runner cache:**
[`logs/runner-cache/inertial_closure_two_step_surface_2026_07_08.txt`](../logs/runner-cache/inertial_closure_two_step_surface_2026_07_08.txt)

## Imported Surface and Open Dependencies

The band
\[
E(p)=\operatorname{arsinh}\!\sqrt{m^2+\sum_{j=1}^3\sin^2p_j}
\]
and \(M_I=m\sqrt{1+m^2}\) are inherited from the paired rest-gap note.
That paired note and its d-dimensional dispersion dependency require
independent audit. The additional imported probe is the standard single-band
uniform-force law with coefficient \(g\); it is not a gravitational coupling.

## Unwrapped-Lift Statement

Choose one open Brillouin branch and lift its quasimomentum coordinate to the
covering space. Let the initial density \(\rho_0(p)\) have compact support
strictly inside that branch. On the lift,
\[
\widetilde p(t)=p-gt e_3,
\qquad
\langle\widetilde p(t)\rangle
 =\langle\widetilde p(0)\rangle-gt e_3.
\]
This identity is exact for the supplied probe.

For the associated band velocity,
\[
\frac{d\langle X_3\rangle}{dt}
 =\int\rho_0(p)E_3(p-gt e_3)\,d^3p,
\]
and
\[
\frac{d^2\langle X_3\rangle}{dt^2}
 =-g\int\rho_0(p)E_{33}(p-gt e_3)\,d^3p.
\]
These formulas use the unwrapped lift. They also describe principal
quasimomentum only on the explicit pre-wrap interval for which the shifted
support remains inside the chosen branch. A principal-value mean after a seam
crossing is not part of the claim.

## Local Curvature Bound

Assume the packet is centered at zero and, throughout the interval considered,
\[
\operatorname{supp}\rho_0-gt e_3
 \subset\{q:\lVert q\rVert_\infty\le p_*(m)\},
\qquad p_*(m)<\frac{\pi}{2}.
\]
With \(\sigma_p^2=\int\rho_0(p)|p|^2\,d^3p\), define
\[
r(t)=M_I\int\rho_0(p)E_{33}(p-gt e_3)\,d^3p-1.
\]
Evenness gives \(\nabla E_{33}(0)=0\), so Taylor's theorem yields
\[
\frac{d^2\langle X_3\rangle}{dt^2}
 =-\frac{g}{M_I}[1+r(t)],
\qquad
|r(t)|\le C_4(m)(\sigma_p^2+g^2t^2),
\]
where
\[
C_4(m)=\frac12M_I
\sup_{\lVert q\rVert_\infty\le p_*(m)}
\lVert\operatorname{Hess}E_{33}(q)\rVert_2.
\]
The rest-point axial coefficient is
\[
\frac12M_I|E_{3333}(0)|
 =\frac{3+10m^2+4m^4}{2m^2(1+m^2)}.
\]
The runner evaluates the local formula on one compact seven-point
distribution. Its sampled Hessian maximum is diagnostic only: it is not a
certified supremum and does not establish the displayed analytic bound.

## Boundaries

- All momentum and acceleration formulas are on the unwrapped lift, or on the
  explicit pre-wrap interval above.
- The principal-value momentum after Brillouin-zone wrapping is excluded.
- The probe is supplied, species-blind, and nongravitational.
- No source coefficient, WEP identity, persistence, or interacting theorem is
  claimed.
- The paired source note and the source-band dependency remain unaudited.

## Dependencies

- [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md)
  supplies the conditional band algebra and \(M_I\).
- [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the still-unaudited band used by the transport formulas.

## Reproduction

```bash
python3 scripts/inertial_closure_two_step_surface_2026_07_08.py
```

The cache is regenerated only after the runner passes with its pre-wrap gate.
