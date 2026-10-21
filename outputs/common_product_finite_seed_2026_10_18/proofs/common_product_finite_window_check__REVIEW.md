# Uniform observation interval: distinct bounded check

No required mathematical correction was found. The proposed endpoint allowances prove the uniform complete-output bound (8), and the ordered parameter choices yield an interval of fixed positive relative width at arbitrarily small certified error. The comparator remains a time-dependent packet and physical phase. This does not prove a stationary output or a time-independent readout operation.

## Pins, exposure and reused dependencies

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, read completely and SHA-256 verified: `common_product_finite_window/PROPOSAL.md`, `1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b`.
* Complete composition, previously fully read and checked in this same session, with its hash freshly verified: `common_product_finite_seed_router/PROPOSAL.md`, `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.
* My preceding composition report, hash freshly verified: `common_product_finite_seed_router_check/REVIEW.md`, `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9`.

The full component source identities and physical premises in that composition report are reused at their stated scopes. They are not independently re-certified by this interval extension. My prior launch, boundary and composition work is shared exposure, not prior verification of the new uniform theorem. ROOT suggested the interval question; I read the candidate formulas before checking them. This is a distinct source-exposed same-model check, not blind discovery, model-diverse replication, a formal audit or retained status. Existing workflow snapshots from the coherent checking task are reused without claiming remote-main freshness.

The source's description of the composition check as still pending reflects its authoring chronology. The present check can use the now-completed pinned composition report without treating that report as a check of the interval result.

## Monotonicity and mixed-endpoint normalization

For A>0, differentiation gives `F'(A)=-(2A^-3+A^-2)/(2sqrt(A^-2+A^-1))<0`. In the late tail, A=tvmin-ell grows and `d(t/A)/dt=-ell/A²<0`. Thus both nonnegative factors in T decrease. This proves d_late(t)<=d_L, with no unsupported general claim that T decreases with time.

For the outgoing tail, A=2ell+2-tvmax shrinks and `d(t/A)/dt=(2ell+2)/A²>0`. Both nonnegative factors increase, proving N_out(t)<=n_O. These conclusions use fixed g, G_0 and G_1 across the interval; the source explicitly fixes them.

The denominator 1-d_late(t) is positive and increasing, while N_out(t) is increasing. Their ratio need not be monotone. Nevertheless `N_out(t)<=n_O` and `1-d_late(t)>=1-d_L>0` give the proposed mixed-endpoint allowance d_O. This is the correct inequality direction and does not assume an extremum of the ratio at either endpoint.

The exact outgoing norm satisfies q_out(t)>=1-d_late(t)>=1-d_L. Let r(t) be the norm of the discarded part of the normalized outgoing vector. The composition gives r(t)<=d_out(t)<=d_O<1. Orthogonality of retained and discarded coordinates then gives

    ||P B_packet(t)|| = q_out(t) sqrt(1-r(t)^2)
       >= (1-d_L)sqrt(1-d_O²)>0.

This verifies (7), including its uniform lower bound rather than merely pointwise nonvanishing. The two normalization costs are still the composition's 2d_late and 2d_out. Bounding them by 2d_L and 2d_O changes no target or phase. Each of the finitely many retained Fourier amplitudes is continuous in t by dominated convergence, and the denominator stays away from zero, so beta_F(t) is continuous. No time-dependent choice of a phase convention is hidden here.

## Boundary and whole-time cell envelopes

The window assumptions ensure qi(t)>1 and qo(t)>2 for every t between t0 and tplus. In B_boundary(t), `1/qi(t0)-1/qi(t)` is nonnegative and increasing because qi increases. Likewise `1/qo(t)-1/qo(t0)` is nonnegative and increasing because qo decreases. Finally `d(t/qo(t))/dt=2ell/qo(t)^2>0`, making A_o(t) nonnegative and increasing. A product of these last two nonnegative increasing functions is increasing. Thus the boundary estimate is bounded by its value at tplus; there is no subtraction of quantities with uncontrolled signs.

This estimate uses the corrected hopping-only perturbation from the composition, with d_hop=sqrt((j-gamma)^2+j²). It preserves the equal-diagonal weak-emitter block and the nonzero exterior Dirichlet generator. Nothing in the window step changes that operator or reverts to Laplacian deletion.

The physical cell estimate `min{2,2kappa+t(8j kappa+epsilon1)}` is nondecreasing for t>=0. Its largest interval value is therefore e_C at tplus. It continues to charge the whole physical duration from the actual seed, not only the time after t0. The early error e0 is fixed by the single initial comparison at t0 and stays the same for every later application. In particular, the factorial estimate still has argument 4jt0.

Every observation time satisfies the composition's required inequalities: t>=t0, tvmin>ell, tvmax<2ell-2, d_late<1 and d_out<1. Its pointwise uniform input bound is therefore available throughout the interval. Replacing its nonnegative terms by the established common bounds gives (8). Taking both suprema does not add an error factor or require exchanging a limit with a supremum. The estimates already hold for every unit input, including arbitrary passive-reference extension. The trivial distance cap remains valid, and the channel estimate follows pointwise with the same uniform constant.

## Ordered existence and relative width

Since sigma'<pi/3, cmin=2cos(sigma')>1, whereas cmax=2. Hence the open interval `(1/cmin,2/cmax)` has positive width and contains two fixed numbers alphaMinus<alphaPlus. They can be selected once, independently of later accuracy and physical scale choices, while keeping the cutoff fixed.

Choose rho first to suppress the fixed spectral-tail allowance, then u0 to suppress the launch remainder, right tail and incoming boundary contribution. All derivative constants may depend on rho and the cutoff; no uniform rho limit is needed. At fixed u0, the early factorial series has fixed argument 4u0 and increasing starting degree ell+2, and the early comparison gap grows with ell. Both early geometric costs therefore vanish.

At the left endpoint, A_late=(alphaMinus cmin-1)ell has a positive fixed coefficient and jtminus/A_late is constant. Therefore T is O(ell^-1/2). At the right endpoint, A_out=(2-alphaPlus cmax)ell+2 likewise has a positive coefficient and jtplus/A_out is bounded. Thus n_O is O(ell^-1/2), and d_O tends to zero because 1-d_L tends to one. The strict normalization conditions eventually hold uniformly.

For the boundary term, qo(tplus)=(2-alphaPlus cmax)ell, so jtplus/qo(tplus) is constant and A_o(tplus) is bounded at the fixed spectral choices. Multiplication by d_hop cancels the 1/j scale in the velocity denominator; the outgoing contribution is O(1/ell). The incoming contribution is bounded by a fixed constant divided by u0 cmin-1 and was already made small. These are compatible simultaneous choices, not unrelated limits.

Once ell and both dimensionless endpoints are fixed, reducing eta=b/D0 and zeta=D0/D1 controls the cell error at splus=jtplus. Rescaling j and gamma together and setting the physical times by (9) leaves the ideal dimensionless estimates intact. The safe cap construction from the composition therefore applies unchanged. No additional sites, blocks or loads are introduced by specifying an observation interval.

The exact interval width is `(alphaPlus-alphaMinus)ell/j`, and its ratio to tminus is the positive constant `(alphaPlus-alphaMinus)/alphaMinus`. Neither increasing ell nor decreasing the common physical scale collapses this relative width. Each selected device has finite positive times; no efficient absolute runtime follows. A change in spectral support would change constants and could change the admissible alpha interval, so it is correctly excluded from the fixed-choice scaling argument.

## Scope and record

This is a uniform family of time-indexed complete-output comparisons for one fixed device and one fixed seed map. The common packet moves and disperses, and the physical scalar phase varies with time. The theorem preserves emitter and mediator vacancy in its comparator while charging their actual residuals in the norm. It does not infer a common stationary spatial vector, permanent halt, capture/reset, stable classical Record, or an unproved operational statement about discarding observation-time information. Supplied interactions, exact coefficients, legal input/program preparation and native physical identifications remain as in the composition.

Only this report was written. No scientific program, numerical simulation, symbolic solver, source modification, W/Git/PR/canonical/checkpoint/editable-prompt change, model change or delegation occurred. Hashing and directory creation were bookkeeping. No retained status or formal audit verdict is assigned.
