# Pre-comparison finite-wavelength reconstruction

This independent reconstruction uses the complete supplied note at SHA-256
`c125636d6e2808e0f9ea452187bd3533159d4953205faf4bb68bc148c6c14aeb`,
the unchanged routed theorem and the previously checked microscopic generator.
No original analyzer, production outcome, author projection checker/results or
by-axis comparison was opened. The following controls and formulas are sealed
before those comparisons. No provisional mathematical correction is identified.

## Exact linear projection

At the uniform fourteen-color law, every row and column mean of the symmetric
pair tensor S_delta is zero. The actual rate is

    c = k0/2 + [S(l,a)+S(a,r)-S(l,b)-S(b,r)]/4.

For the probability-vector current c(xi_a-xi_b), conditioning on l=s leaves
`(1/2) diag(p) S_delta xi_s`, because the two terms correlating S(s,a) and
S(s,b) with their respective indicators add. This equals A_delta xi_s/4,
where A_delta=2diag(p)S_delta, and the mean subtraction vanishes. Conditioning
on r gives the same result. Conditioning on a=s or b=s kills all context
contributions by the zero row/column means and gives respectively
`(k0/2)(xi_s-p)` and `-(k0/2)(xi_s-p)`. Thus the four displayed coefficients
are exact; the physical outer rate half is essential.

At the winding matching the channel shift is a_delta=delta-e1. Write
z=k.a_delta. Reindexing the four site terms in a Fourier sum with phase
exp(-ik.u) gives exp(-iz), 1, exp(iz), exp(2iz). The exchange contributes
exp(-iz)-1. The symmetric factor is

    (k0/2)(exp(-iz)-1)(1-exp(iz)) = -2k0 sin^2(z/2),

and the context factor is

    (A_delta/4)(exp(-iz)-1)(exp(-iz)+exp(2iz))
       = -(i/2)[sin(2z)-sin(z)] A_delta.

The sum therefore gives exactly B(k)=-d(k)I-iA_6(q_eff), with the source's d
and q_eff. The six normalized features are (sqrt(7)e, sqrt(7)b/2), whose
one-site covariance is I6. The tensor has rank only in these vector moments;
the seven other tangent moments have no first-order cross coupling to them.
In this basis A_6(q)=(2gamma/7)[[0,-C_q],[C_q,0]], C_q v=q cross v.

The linear term of q_eff is k since (1/2)sum_delta delta delta^T=I and
sum_delta delta=0. The q_eff error is O(|k|^3). At k=theta e1 only delta=-e1
survives in the vector sum, yielding [sin(4theta)-sin(2theta)]e1/2. The four
other nonfixed channels contribute to the scalar damping even though their
vector terms cancel. For k along e2 or e3 the two opposite axis channels
give [sin(2theta)-sin(theta)]e_i. This reproduces both axis formulas, the
leading damping factors 4k0 and k0, and the Euler-time damping O(1/N).

## Covariance curvature and closure boundary

Let F be the normalized six-field column, C(t)=E[F_t F_0^dagger], and P the
orthogonal projection onto the full linear single-site Fourier space. The
restricted linear block is B and the other seven linear moments do not mix
into these six. The constant-swap symmetric part S preserves this linear
space. The remaining generator part is antisymmetric in the uniform product
L2 law. Hence, for R=(I-P)LF,

    LF=BF+R,       L^*F=B^dagger F-R.

Adjointness and orthogonality imply

    C'(0)=B,
    C''(0)=E[LF(L^*F)^dagger]=B^2-E[RR^dagger].

The correction is negative semidefinite in the Hermitian sense. This is an
exact initial-derivative identity, not a finite-time covariance closure. At
gamma=0, R=0 and the linear space is invariant, so the exponential covariance
is exact. At gamma!=0 a nonzero residual explicitly disproves exact closure
in the corresponding finite example.

Our independently assembled four-position routing cycle has four distinct
context positions, all fourteen colors, k0=5/4, delta=e1 and Fourier phase
pi/2. It is not an N=4 physical cubic torus. All 14^4=38,416 states and the
four oriented swaps were assembled directly. Gaussian-integer sums followed
by exact rational arithmetic verify both derivatives and give, at gamma=1,

    E[RR^dagger] = diag(2/49, 11/98, 11/98,
                       15/196, 15/196, 15/196),
    trace = 97/196.

The residual is zero at gamma=0. The calculation does not fit a relaxation
parameter and does not assert that this auxiliary cycle is the production
torus. Exact conditional means on all 38,416 four-label inputs also verify
the four local projection matrices, including their full tangent centering.

## Four statistics and Fourier signs

For one nonzero axis mode let n=Q/|Q|, P_L=diag(nn^T,nn^T), P_T=I-P_L and

    D = [[0,iC_n],[-iC_n,0]].

D^dagger=-D and D^2=-P_T. With omega=(2gamma/7)|Q|,
`U=P_L+cos(omega t)P_T+sin(omega t)D=exp(-iA_6(Q)t)`.
The sign convention makes the ideal signed cross equal +sin(omega t),
not its negative. For a stationary law with endpoint covariance I6 and
two-time covariance C, the normalized mean squared propagation error is

    E||F_t-UF_0||^2/6 = 2-Re tr(U^dagger C)/3.

The other three normalized means are respectively
`Re tr(P_T C)/4`, `Re tr(D^dagger C)/4`, and `Re tr(P_L C)/2`.
These denominators are the transverse and longitudinal dimensions. Their
ideal values are cos(omega t), sin(omega t), and 1.

For the axis projected benchmark put r=exp(-Ntd), and let
theta_eff=(2gamma/7)N q_eff,axis t. The four expressions reduce to

    error = 2-r[2+4cos(theta_eff-omega t)]/3,
    transverse_auto = r cos(theta_eff),
    signed_cross = r sin(theta_eff),
    longitudinal_auto = r.

This calculation retains unit endpoint variances. Replacing the stochastic
endpoint by a dissipatively propagated initial field would give a different
error. For example C=(1/2)I and U=I give the correct error 1, whereas the
deterministic damped-path error is 1/4. This is an explicit normalization
countercontrol.

Independent numeric controls assemble the unsimplified four-coefficient
symbol and compare it to the simplified symbol for two oblique wavevectors,
both signs of gamma, zero gamma and zero wavevector. Axis matrix exponentials
are compared to the scalar formulas for N=16,32,64,128 and our chosen test
times 0,1/4,1/2,3/4,1. These are theoretical predictions without production
input. Their time list is a test choice until the original analysis schedule
is inspected after this seal. No N256 observable is accessed.

## Independent controls and remaining comparison

`independent_projection.py` imports no author checker. Its first execution
completed with exit code zero and empty stderr. `PRE_COMPARISON_RESULTS.json`
contains the exact local/curvature matrices, nine oblique/zero symbol controls
and 60 axis/time predictions. The complete output was inspected, with the
60 prediction rows displayed compactly. Exact integer and rational statements
are distinguished from floating matrix-exponential/trigonometric evaluations.
No failed attempt occurred and no within-hypothesis counterexample was found.

The aggregate-analysis part of the assigned review remains to be performed:
read the original analyzer/sign controls, reconstruct history-level statistics
and whole-history means/SEs from all original N<=128 histories, check the
bootstrap convention selectively, then compare the parameter-free benchmark
and its by-axis analysis. The projected exponential remains a post-outcome,
unfitted mechanistic benchmark, not a theorem about exact finite-time damping,
a new fitted assessment or a claim about irregular geometry.
