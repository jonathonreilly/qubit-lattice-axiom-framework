# Assumptions And Imports

No new imports or premises are introduced.

The branch keeps the existing finite live-capture harness and changes only the
safe readout convention for the roundoff-level two-body residual:

```text
two-body max < 1e-12
```

This is exactly the threshold used by the runner assertion.
