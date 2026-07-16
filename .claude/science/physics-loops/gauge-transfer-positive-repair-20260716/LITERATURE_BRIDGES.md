# Literature Bridges

No literature is load-bearing in blocks 01 or 02.

For block 02, the old source named a Wilson reflection-positivity comparator
because it lacked the `SU(N)` coefficient signs. The repair no longer needs
that bridge:

```text
exp[alpha Re chi_R]
  = sum_n (alpha/2)^n/n! chi_((R plus Rbar)^tensor n),
```

and the irrep coefficients are nonnegative tensor multiplicities. Uniform
absolute convergence follows from the dimension majorant
`exp(alpha dim R)`. The real-Gram/Schur-power proof supplies a second
self-contained positive-type route.
