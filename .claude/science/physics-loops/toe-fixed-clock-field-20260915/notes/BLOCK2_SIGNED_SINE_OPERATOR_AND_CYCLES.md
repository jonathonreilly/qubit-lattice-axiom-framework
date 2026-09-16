# A bounded signed sine operator and the restricted-cycle issue

Personal derivation, 2026-09-15. This is a new operator estimate for the
component representation. It is not the complete cluster expansion.

## 1. Component-space operator, including the nonlinear sine

Use the infinite-lattice marked component measures nu_e,nu_m and fillings
S,n of the two-root note. Put H_e=L2(nu_e), H_m=L2(nu_m). Assume their
anchored moments M_e(r),M_m(r) are finite through order 6. Define the
operator T:H_e->H_m by kernel

    T(n,S)=sin(c<n,PS>), c=2pi N.

The statement includes the full sine, not just its linear approximation:

    ||T|| <= c sqrt(M_e(2) M_m(2))
                +(c^3/6) sqrt(M_e(6) M_m(6)).           (1.1)

To define its first term, let F_e f=integral S f(S) nu_e(dS), and likewise
F_m. Their adjoints are (F_e* u)(S)=<S,u>. The frame inequality gives
||F_e||<=sqrt(M_e(2)), ||F_m||<=sqrt(M_m(2)). The linear phase operator is

    T0=c F_m* P F_e,

so it has the first bound in (1.1). This is a signed bounded operator;
no entrywise l1 bound on P is required.

For the remainder R=T-T0, set l_e(S)=||S||_1^3 and l_m(n)=||n||_1^3.
Nonzero components have nonzero fills, so these are positive Schur weights.
Using |sin t-t|<=|t|^3/6 and |<n,PS>|<=||n||_1||S||_1 gives

    integral |R(n,S)| l_m(n) nu_m(dn)
      <= (c^3/6) ||S||_1
             integral ||n||_1^4 |<n,PS>|^2 nu_m(dn)
      <= (c^3/6) M_m(6) ||S||_1^3.                    (1.2)

The weighted frame integral in the middle has Schur norm at most M_m(6),
since its absolute row sum is bounded by
integral |n(i)| ||n||_1^5 nu_m(dn). Also ||PS||_2<=||S||_1.
Interchanging n and S in the symmetric bilinear form gives the other
weighted Schur inequality with M_e(6). The weighted Schur test proves
||R||<=c^3 sqrt(M_e(6)M_m(6))/6. The absolutely integrable remainder plus
the frame-defined linear term specifies T on the full component spaces.
All these bounds hold for arbitrary finite restrictions of the measures.

This definition agrees with finite-cutoff kernel sums in L2: truncate the
domain and range component spaces by increasing projections. The frame
operators converge strongly on their natural L2 vectors, and the bounded
remainder obeys the same truncation prescription. Arbitrary scalar orders
of conditionally convergent multiple sums are not asserted equivalent.

## 2. An explicit small norm with an energy reserve

Use the half-self-weight measures of the two-root note. With x_e=g^2,
x_m=b^2, its anchored count gives, for r=2 or 6,

    M^(1/2)(r) <= 2 C_A 4^r exp(-x/64)
                      /[1-393*2^(2r+4) exp(-x/64)]    (2.1)

when the denominator is positive; C_A=1,562,500. This follows from
m^(2r+4)<=2^((2r+4)(m-1)), applied to the complete component count.
The r=2 denominator is 1-100608 exp(-x/64), and the r=6 denominator is
1-25755648 exp(-x/64).

For x_e,x_m>=4096, the right side of (1.1), evaluated with these half
measures, is less than 3e-8. To see uniformity in both x values, the first
term factors into sqrt[x_e M_e(2)] sqrt[x_m M_m(2)] and the second into
(1/6)sqrt[x_e^3 M_e(6)] sqrt[x_m^3 M_m(6)]. Each upper factor decreases
for x>=4096 and its endpoint can be evaluated directly. Including the
factor 2 from the actual unoriented-component orientation sum in both
measures at most doubles the operator norm, giving a bound 6e-8.

This is only a sufficient fixed-parameter range for an operator estimate.
It does not establish a physical phase there. For example beta=256,N=2048
satisfies both inequalities with fixed finite parameters.

## 3. Every unrestricted alternating closed walk is controlled

First take finite component families and let rho=||T||<1. A length-2r
alternating closed-walk sum, permitting repeated component labels, is

    W_(2r)=Tr[(T* T)^r].                               (3.1)

All kernels here are real, so T* is the transpose with its measure weights.
Consequently W_(2r)>=0 and

    W_(2r)<=rho^(2r-2) Tr(T*T).                        (3.2)

For r>=2, the formal alternating signed cycle functional satisfies

    sum_(r>=2) (-1)^r W_(2r)/r
       =Tr[T*T-log(I+T*T)],
    sum_(r>=2) W_(2r)/r
       <=Tr(T*T) rho^2/[2(1-rho^2)].                  (3.3)

These are exact matrix identities and an absolutely convergent sum over
lengths. They do not identify the graph combinatorial factor of the
physical pressure; a closed walk can revisit vertices and edges.

The trace is bounded without a volume-dependent operator norm:

    Tr(T*T) <= c^2 ||K_m|| integral E_e(S) nu_e(dS).    (3.4)

For a finite set of electric component anchors, the last integral is at
most a constant times the number of anchors. This follows from the same
exponential component count and E_e<=||S||_1^2<=16m^4.
Thus (3.3) has a controlled extensive bound under these finite cutoffs.
No thermodynamic pressure identity is assumed.

## 4. Distinct labels and physical support compatibility

Orientation graphs in the physical gas use distinct compatible components.
One cannot infer positivity of their cycle sums from (3.1). The finite
chain example in block2_phase_energy_check has two compatible components
of each species and a product of four sine entries

    -0.09386628063417557.

The corresponding four ordered distinct-label closed walks sum to four
times this negative value (before positive activity weights), whereas
Tr[(T*T)^2] for the full 2-by-2 matrix is nonnegative. Repeated labels in
the latter are essential to its positivity. This is a witness about the
summation operation, not a claim that the physical pressure is negative.

There is nonetheless a useful exact fourth-order correction. For an
arbitrary finite real matrix T, let D4 sum the walks in (3.1) with its two
electric labels distinct and its two magnetic labels distinct. Put A=T*T,
B=TT*. Inclusion-exclusion gives

    D4=Tr(A^2)-sum_i A_ii^2-sum_j B_jj^2+sum_ij T_ji^4,
    |D4|<=Tr(A^2).                                    (4.1)

Indeed each diagonal-square sum is at most Tr(A^2), while the fourth-power
sum is at most either diagonal-square sum. These inequalities put D4
between -Tr(A^2) and Tr(A^2). This is a bound for distinct labels only.
Additional nontrivial support-compatibility factors need another argument;
the two-component example already has those factors equal to one.

Higher distinct-label cycles require control of collision partitions and
their combinatorics. Merely applying inclusion-exclusion at every length
may introduce factorial growth, so (3.3) is not a proof of their convergence.
Even a successful cycle estimate would still leave networks with branching
vertices, same-species real interactions, hard-core constraints and physical
sources. Those are explicit open obligations. The advance here is the full
signed sine operator bound with an energy reserve, usable without replacing
the sine by its linear term.
