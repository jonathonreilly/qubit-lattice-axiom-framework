# No-Go Ledger

## Block94

Route:

```text
fixed Route-2 carrier
+ granted T-side endpoint values
+ basic source-vector conservation/equipartition selector equation
=> rho_E = 21/4
```

Verdict: no-go / negative route pruning.

Reason:

- No-lift, same-slope/collinearity, product conservation, L1 conservation,
  center absolute balance, and positive linear source conservation select
  non-target values or cannot select the target.
- A positive diagonal quadratic metric can select the target only by supplying
  `b/a=1449/704`.
- The source bridge `c_TE=-8/9` selects the target exactly, but that is the
  named missing primitive rather than a consequence of the fixed-carrier
  selector equations.

## Existing Main-Surface Boundaries Used

- E-channel naturality no-go: minimal Route-2 naturality leaves `rho_E` free.
- E-center blindness no-go: E-center-blind constraints cannot select the
  target.
- Source-domain bridge no-go: current typed bank has no `R_conn -> c_TE`
  bridge.
