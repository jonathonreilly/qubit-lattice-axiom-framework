# Assumptions And Imports

Allowed support:

- Block147 selector-equivalence atlas.
- Block148 clause-independence hardwall.
- Exact `K_R -> P_R -> E/T` carrier/readout reduction as a candidate frame.
- Minimal `1 + adjoint` same-source extension as conditional support.
- Generic P-cal/source-measure and Fisher/Riesz support only as geometry once
  Route-2 objects are supplied.
- Endpoint orientation sign support, consumed downstream only.

Forbidden imports:

- Endpoint value or endpoint triple.
- `rho_E`, `q_E`, or observed quark values.
- Fit-derived source weights or target comparators.
- Treating formal source jets, generic Fisher geometry, or finite `P_R` slots
  as physical without a Route-2 source/readout realization theorem.

Open import:

```text
Route-2 physical same-source selector realization theorem:
construct Omega_R, P_0, P_h, and physical readout variables X,Y for P_R/E-T;
prove E[XY]=1, connected typing, E[X]E[Y]=1/9, mu=1, and downstream
orientation sign consumption.
```
