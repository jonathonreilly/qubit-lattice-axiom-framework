# Registered criteria, 892504e4c

Written before this session's first numerical run. The source's existing
simple/generic-flux numerical tables have been read. None is treated as a
new run or an independent check here.

Q1 (exact rational check). Derive Q(z) from two derivatives of |z|^-2,
omitting its common nonzero scalar. Check at (1,0,0,0), (1,2,3,4),
(2,-1,0,3) that Q equals the induced action of the reflection
I-2 zz^T/|z|^2 on two-forms. An inequality means the implementation or
normalization derivation needs repair. Equalities at finitely many points
are a check of the algebra, not the proof for all z.

Q2 (counterexample to the auxiliary scalar-kernel assertion). For
u=d=(e01+e23), check exact zero of <u,Q(z)d> at those three points, while
Q(z)^2=I and ||u||^2=||d||^2=2. Also check one opposite-duality pair gives
a nonzero value at z=e0. The general counterexample requires a handwritten
identity for all z; finite zero tests alone cannot establish it. This does
not refute RANK-U, because attainability as the two constrained maps is a
separate question.

U1 (finite-box evidence). Reuse, with explicit credit, the pinned
`witness_rank_moment.py` polynomial and constraint construction at L=5.
Use unit fluxes F=e01, F=(e01+e23)/sqrt(2), and
F=(e01-e23)/sqrt(2), in Fock gauge and that gauge plus
(-1)^(x0+x1+x2) x3, with coordinates centered for x3.
No optimization and no process pool. Check the polynomial residual <=1e-10,
the constrained basis residual <=1e-9 relative to matrix norms, and
||m(F)|| <=1e-8 max(1,||m||). Failure invalidates the affected evidence.
Report all six singular values, the dipole singular values, the actual
maximum gradient of t, and ranks at relative tolerance 1e-8.
If ||m|| <=1e-9, save the gauge and call it a *candidate* counterexample
requiring exact reconstruction. Otherwise this is evidence only for these
six gauges at one size. A positive value does not prove RANK-U or any
lower bound uniform over t. Check a few directions of Q against the full
images of m and dip; report their largest coupling, without treating a
finite sample as a uniform result.

Execution: the real `scripts/lab_ops.py numeric-lock` must report acquired.
Its omitted sparse dependency `automation_lock.py`, if needed, is copied
unchanged from HEAD into `tooling/` here and supplied via PYTHONPATH.
Run preflight with minimum free-memory fraction 50%, run with nice 10 and
all BLAS/OMP thread variables 1, and monitor RSS with a 2,000,000,000-byte
self-stop. Recheck free memory at script entry. Never use a process pool.

## Outcome

None of Q1, Q2 or U1 was executed. Preflight found the lock held by another
worker. While waiting, the exact construction in
`../../library/rank-u-staggered-limit.md` refuted the limit clause directly.
The item therefore ended without a numeric job, without an acquire, and
without a claimed numeric PASS or FAIL. These criteria are preserved as
unrun proposals, not evidence. The symbolic proofs do not rely on them.
