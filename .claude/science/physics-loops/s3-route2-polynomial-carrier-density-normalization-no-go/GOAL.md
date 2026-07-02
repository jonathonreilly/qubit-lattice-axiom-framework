# Goal

Attack the source/readout-side channel-density normalization target for the
S3/Route-2 endpoint triple. Test whether the current class-A polynomial
carrier

```text
K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)
```

can derive the channel-weight division needed for

```text
(-1, -2, 21/4).
```

Actual result: scoped no-go. The current polynomial carrier contains no
channel-weight coordinate and cannot derive `D_X=A_X/w_X`.
