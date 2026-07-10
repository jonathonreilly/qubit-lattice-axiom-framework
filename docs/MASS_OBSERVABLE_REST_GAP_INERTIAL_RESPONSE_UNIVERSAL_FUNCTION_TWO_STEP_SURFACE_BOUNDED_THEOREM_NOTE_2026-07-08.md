# Free Two-Step Rest-Gap and Curvature Algebra — Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** Conditional on the supplied free staggered two-step band
\[
E(p)=\operatorname{arsinh}\!\sqrt{m^2+\sum_{j=1}^3\sin^2p_j},
\qquad m>0,
\]
this note proves the rest-gap, rest-point curvature, and the exact algebraic
relation between those two quantities. It does not identify this band with a
physical species, prove packet dynamics, or derive the coefficient \(m\).

**Primary runner:**
[`scripts/mass_observable_two_step_surface_2026_07_08.py`](../scripts/mass_observable_two_step_surface_2026_07_08.py)

**Runner cache:**
[`logs/runner-cache/mass_observable_two_step_surface_2026_07_08.txt`](../logs/runner-cache/mass_observable_two_step_surface_2026_07_08.txt)

## Imported Surface and Open Dependencies

The displayed band is an imported free-model surface. Its d-dimensional
dispersion authority is still unaudited at the time of this source repair.
Consequently this note proposes only a bounded conditional algebra result; it
does not promote that dependency or predict an audit outcome.

No realized-state premise is needed for these identities. The
`realized_state_primitive`, kinetic-branch selection, Record-stiffness
residuals, and shared-coupling templates are therefore not load-bearing
dependencies of this narrowed note.

## Exact Identities

### Rest gap

Since \(\sum_j\sin^2p_j\geq0\) and \(\operatorname{arsinh}\) is increasing,
\[
m_{\rm gap}:=min_p E(p)=\operatorname{arsinh}(m).
\]
The minimum is attained wherever every \(\sin p_j\) vanishes.

### Rest-point curvature

Along \(p=(0,0,q)\),
\[
E(q)=\operatorname{arsinh}\sqrt{m^2+\sin^2q}
     =\operatorname{arsinh}(m)
      +\frac{q^2}{2m\sqrt{1+m^2}}+O(q^4).
\]
Therefore
\[
\left.\frac{d^2E}{dq^2}\right|_{q=0}
 =\frac{1}{m\sqrt{1+m^2}}.
\]
Define the reciprocal curvature coefficient
\[
M_I:=m\sqrt{1+m^2}.
\]
This is a band-curvature definition only; the acceleration interpretation is
separate.

### Relation between the two algebraic readouts

Using \(m=\sinh m_{\rm gap}\),
\[
M_I
 =\sinh(m_{\rm gap})\cosh(m_{\rm gap})
 =\frac12\sinh(2m_{\rm gap}),
\]
and
\[
\frac{M_I}{m_{\rm gap}}
 =1+\frac23m^2+O(m^4).
\]
Thus the rest gap and reciprocal curvature agree only at leading small-\(m\)
order; the exact finite-spacing relation is the hyperbolic identity above.

## Boundaries

- Free \(U=1\), \(d=3\) supplied band only.
- The source band and its species interpretation are not derived here.
- No taste-projection, localization, persistence, packet-acceleration,
  interaction, gravity, source, or WEP claim is made.
- No audit verdict or expected audit disposition is stated.

## Dependencies

- [`FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the displayed \(d=3\) band and remains an unaudited load-bearing
  dependency at the time of this repair.

## Reproduction

```bash
python3 scripts/mass_observable_two_step_surface_2026_07_08.py
```

The cache is regenerated only from a green run of that script.
