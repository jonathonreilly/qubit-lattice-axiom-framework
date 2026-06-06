# Goal

Repair `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02` by preserving the
finite metric computation while removing the unsupported conclusion that A1
selects `det_R` as the physical default.

The repaired packet keeps:

```text
HS metric = diag(3,6,6)
det_R and det_C are conditional arithmetic readings
operator-symbol and continuous-U(1)_b routes are pruned
```

It leaves the physical doublet-count selector open.
