# Literature Bridges

No external physics value is used.  The mathematical background is the
standard finite exponential-family/Radon-Nikodym identity:

```text
R_h = exp(h O) / E exp(h O)
score = O - E[O]
Fisher norm = Var(O)
```

and the standard Gibbs/log-density relation

```text
P_h proportional exp(-S_h),  S_h = S_0 - h O + c(h).
```

These are used as finite algebraic identities, with the physical selection of
the source-measure surface supplied by the repo's Tier-A P1/P-cal policy.
