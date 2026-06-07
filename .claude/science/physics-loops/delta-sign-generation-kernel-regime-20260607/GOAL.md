# Goal

Repair the conditional delta-sign row by replacing the sampled `delta=-0.3`
sign propagation with an exact second-order formula and by connecting the
generation pair to the stacked periodic density-kernel bridge.

The intended outcome is bounded support for:

```text
delta < 0
K_C3 = t^2 delta / (eps_gap (eps_gap + delta))
K_C3 < 0 when eps_gap > 0 and eps_gap + delta > 0
```

This block does not claim a physical magnitude, does not prove the realized
gap branch, and does not set an audit verdict.
