# Assumptions And Imports

## Framework Inputs

- The note studies the existing L_s=3 PBC cube link-adjacency graph with
  81 link-tensor nodes and 324 shared-cyclic-index edges.
- The runner continues to test the same two implemented heuristics:
  min-degree and min-fill.
- Memory is computed as complex entries times 16 bytes.
- The runner's memory display divides by `1024^3`, so the correct unit label
  is `GiB`.

## Imports Retired Or Exposed

- No new math or physics import is introduced.
- The stale decimal/binary unit mixture is retired.
- The truncation-threshold calculation is made native to the runner's binary
  4 GiB budget:

```text
truncation_dim^30 * 16 bytes <= 4 * 1024^3 bytes
truncation_dim <= (4 * 1024^3 / 16)^(1/30) ~= 1.91
```

## Open Dependencies

- The runner does not certify a global treewidth lower bound.
- The runner does not search all contraction paths or path optimizers.
- The result does not compute or constrain `<P>(beta=6)`.
