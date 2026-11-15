# SPURION numerical criteria

Registered before creation or execution of the numerical runner. These are
finite regression criteria, not tests of all-history RG closure. Written
proofs do not depend on the checks. No exploratory numerical probe preceded
this registration.

1. Simultaneously transforming two SU(2) parallel transporters preserves
   their relative trace and relative-log conjugacy to error below 1e-11.
   Transforming only one transporter must change the trace by more than 1e-4
   in a declared deterministic control.
2. SU(2) probability-Haar radial integration at parameters t=2 and s=3
   reproduces Z(0)=1 and the positive relative quadratic coefficient
   ts Z'(t+s)/((t+s) Z(t+s)). Quadrature refinement changes Z and Z'/Z by
   less than 1e-10. A centered second difference of the exact integrated
   two-link expression agrees with the coefficient to relative error below
   1e-5. The coefficient exceeds 0.1. The unnormalized reader integral
   Z(t+s)/(Z(t)Z(s)) differs from one by more than 1e-2.
3. A rational Gaussian blocking Schur complement has exactly zero on the
   declared gauge vector while its fixed-input output block is positive.
   Adding a positive physical mass to the fine Hessian must give a nonzero
   output gauge quadratic form. All equalities use rational arithmetic.
4. In a finite three-edge graph with one tree, gauge fixing and reconstruction
   preserve the independent loop holonomy to error below 1e-11. The degree-four
   Taylor projector in the independent loop coordinate is exactly idempotent
   on rational polynomial probes; a fifth-degree probe remains in the remainder.
5. Complete-reader normalization has an exact finite control: an unread
   normalized kernel integrates to one; a nonconstant future reader changes
   the integral, and summing a complete two-outcome partition restores the
   unselected integral. Each equality is exact in rational arithmetic.

Resource acceptance, checked before and between groups: one process, no pools;
nice at least 10; OPENBLAS_NUM_THREADS, MKL_NUM_THREADS, OMP_NUM_THREADS,
VECLIB_MAXIMUM_THREADS, NUMEXPR_NUM_THREADS and BLIS_NUM_THREADS all equal one;
all sampled load averages below 8; macOS memory_pressure -Q reports at least
30 percent memory free; peak RSS below 1,000,000,000 bytes. Use an exclusive
lane numeric lock. Do not use RLIMIT_AS. A guard refusal or a refused nice
launch means NOT RUN for unexecuted checks, not PASS. Report every failed
criterion as FAIL; identify any subsequent probe as post-hoc.
