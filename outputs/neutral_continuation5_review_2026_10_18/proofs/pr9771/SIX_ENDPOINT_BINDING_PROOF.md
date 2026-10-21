<!-- Original PR9771 source SHA256 9bca83bd9986010a752d3d8424c4fdba7bf91a0a50d37ff45c5546328f99331b. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Six-column binding in the native endpoint coefficient (root)

Use exactly the first-order height operator derived in ENDPOINT_BOUND_MODE_PROOF.md, now on the2x3 transverse rectangle with six same-orientation one-wall columns and uniform exterior. No extra interaction. Fix total common-translation momentum0 and the connected component containing the flat height state. The physical leading endpoint energy is12Jz+Jz lambda times this operator. Boundary sector and Hamiltonian remain supplied; this is a K1 theorem.

Each native move preserves the parity of the multiplicity at every height. Starting flat with six columns, all multiplicities are even. Sorted heights therefore have possible nonzero gaps only after ranks2 and4. Escape of the relative configuration requires a large gap separating2+4 columns, or a finer2+2+2 split. At such a gap all cross-cluster native terms vanish because active heights must differ by at most one.

# Uniform four-column input, including all internal components

For each of the15 induced four-column subsets, the FULL even-multiplicity relativeheight space consists of flat plus six rays of2+2 assignments. This includes components not reachable from their own flat states, which is necessary for breakup channels prepared through other columns. At momentumk the core is flat+the first site of each ray. Each ray has constant hopping t_a(k), |t_a|<=2, |t'_a|<=1, and essential spectrum within[-4,4]. Some rays can have zero hopping. No other contact remains beyondheightdifference1.

At energy-5, eliminate the independent tails. Positivity of H4+5 is equivalent to positivity of the7x7 Schur matrix
M(k)=H_core(k)+5I+diag(0,s_1,...,s_6),
s_a=(-5+sqrt(25-4|t_a|²))/2.
The negative sign of s is essential. Tail operators plus5 are positive, so this is an ordinary self-adjoint Schur equivalence.

Source-bound interval arithmetic at30decimaldigits verifies M(k_j)-(1/4)I positive by interval LDL* at257 grid points k_j=pi(j/128-1), j0..256, for all15 shapes. Every interval pivot has a strictlypositive lower endpoint. The displayed floating minimum pivots are only summaries; interval positivity comparisons are the certificate. Complex conjugation uses explicit real/imaginary components because the installed mpmath interval conjugate method failed operationally; no science inference followed from that software failure.

Only the six flat contacts depend on k in H_core, so ||H'_core||<=sqrt6. The diagonal derivative satisfies |s'_a|<=4/3 because the square-root denominator>=3. Thus ||M'||<4; the intentionally looser bound8 is used. Every k is withinpi/256 of a grid point;8pi/256<1/10. Therefore M(k)>=(1/4-1/10)I>0 uniformly. Hence H4(k)>=-5 on every full even-parity component, for all cluster momenta. No floating Ritz fit is used for this lower bound.

# Essential threshold and exact finite trial

Two-column clusters have lower bound-2 (or0 if nonadjacent). Combining the uniform four bound gives every2+4 channel lower bound-7;2+2+2 gives-6. A discrete IMS partition based on the two sorted gaps, refined by finite label partitions, has edge differencesO(1/R), bounded graph degree and hence form errorO(R^-2). Its exterior pieces are separated cluster channels; its interior support is finite. Weakly vanishing Weyl sequences therefore have energy lower limit>=-7. This proves inf essential spectrum>=-7, not equality.

The fixed cutoff maxh-minh<=6 generated from flat has1459states. An integer vector q on those states is stored in six_endpoint_integer_trial.json and extended by zero to the infinite component. Exact integer arithmetic gives
q^Tq=9999999925139683,
q^T H q=-71308060208219532,
10 q^T H q+71 q^Tq=-3080607397277827<0.
Its Rayleigh quotient is approximately-7.1308060742, but only the exact inequality< -7.1 is used. Zeroextension makes it a valid trial even if some other states within the same range require paths outside the cutoff. The variational principle and essential bound imply at least one discrete relative-height eigenvalue below-7.1. Thus binding below all asymptotic breakup channels is proved in this coefficient sector, not just inferred from finite-size convergence. The exact lowest eigenvalue and uniqueness are not claimed.

# Original readout remains a derived operator

For A=6, the physical-center fiber operator K6(k) is bounded analytic in k: pairmoves carry phases exp[+/-ik/3], swaps carry1. Choose a finite-rank spectral cluster P(0) enclosing one or more isolated eigenvalues below-7.1, separated from other spectrum; its continuationP(k) is normcontinuous near0.

The localized original Fourier readout excess is -4cos(p/2)exp(ip/2)exp(ipR)D_p, with D_p=sum_(c=1)^6 exp[ip(h_c-R)]. It is bounded by6 and strongly tends6I as p->0. Finite rank gives ||P(p)D_pP(0)-6P(0)||->0. Hence the bound-cluster vertex tends-24P(0) and is nonzero for sufficiently small finitep. No fitted source coefficient or added scalar coupling is present. Atp0 it is constant, not an internal inelastic excitation. This argument does not prove a nonflat six-column dispersion, a unique scalar species or vacuum creation.

Higher native orders, finitepairedends, physical preparation, fermion/gravity identification and observational constraints remain open. Interval certificates and finite grids are mathematical/model-development checks, not empirical data or a formal audit verdict.

The coefficient -24 refers to the unnormalized upper-interface excess only. A finite interval includes a second, lower-interface contribution; at zero momentum the total six-column excess is -48 when all intervals have length at least two. No volume normalization is implicit.
