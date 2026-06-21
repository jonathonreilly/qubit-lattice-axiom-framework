# Route Portfolio

## Route A: Channel-Scalar Source Preparation

Status: executed in this block.

Candidate:

```text
S(a_E,a_T)=diag(a_E,a_T,a_E,a_T)
```

Result: no-go. This candidate leaves `q_E` and `q_T` invariant.

## Route B: Center-Excess Nonuniform Source Preparation

Status: next positive source-map route.

Candidate:

```text
S=diag(a_E,a_T,b_E,b_T)
```

Target condition:

```text
rho_E * (b_E/a_E) = 21/4
```

This can move the E-center endpoint but needs a typed theorem for
`b_E/a_E`.

## Route C: Readout-Only Inverse-Square Coefficient

Status: open alternative.

Avoid a source map and instead prove that the readout row itself carries the
second inverse Schur factor. This must be a coefficient theorem, not a target
fit.
