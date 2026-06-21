# No-Go Ledger

## Block06: Endpoint-Blind Renormalization Rescue

Pruned route:

```text
finite-box size-stable renormalization -> rescue q_E=15/8 without new readout primitive
```

Reason:

Any separable endpoint-blind renormalization

```text
gamma_X(endpoint;N) -> c_X(N) r_endpoint(N) gamma_X(endpoint;N)
```

preserves `lambda=q_E/q_T`. The endpoint target requires `lambda=9/4`, but the box-scan cache has bulk `lambda` far from `9/4`. Therefore this class cannot rescue the endpoint triple.

Scope:

This does not rule out a future nonlinear tensor observable or explicitly derived nonseparable covariance primitive. It only rules out hiding the missing E-center datum inside endpoint-blind normalization.
