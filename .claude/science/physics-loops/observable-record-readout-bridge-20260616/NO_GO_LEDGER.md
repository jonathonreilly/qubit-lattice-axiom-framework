# No-Go Ledger

## T1-d From Record Alone

Record additivity does not select a determinant-only readout. Exact witness:

```text
W_epsilon(S) = log det(S) + epsilon Tr(S)
```

For positive diagonal source blocks, this is continuous and direct-sum
additive. `diag(4,1)` and `diag(2,2)` have the same determinant and different
trace, so the readout is not a function of determinant alone.

## Source-Disjoint To Record-Disjoint

The source-to-record assignment can be non-injective unless a readout-context
bridge forbids it. Record additivity is conditional on already disjoint records;
it does not prove source-disjoint blocks register as disjoint records.
