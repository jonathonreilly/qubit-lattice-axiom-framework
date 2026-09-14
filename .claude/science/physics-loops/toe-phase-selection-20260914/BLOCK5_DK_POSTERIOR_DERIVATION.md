# A supplied DK likelihood program, with finite acceptance costs

Personal derivation, 2026-09-14. This is a downstream classical stochastic
protocol for the source action, not selection of an action, probability law,
formation schedule, initial program, physical phase or quantum observable.
Independent formal review is pending. Its logical arithmetic circuit is checked. The subsequent
BLOCK5_CAUSAL_EMBEDDING_DERIVATION.md gives a separately checked generic
causal geometry proof; the full DK coordinate roster is not instantiated.

## Exact conditioning and the proper-prior perturbation

The current released source has complex variables psi=(phi,zeta) and action

    S0(psi)=c^-1 ||q phi-B zeta||^2+||zeta||^2,
    B B*=S-c I,       S=(q+q*)/2 > 0.

Its q, B, c and the four arm values are supplied, not axiom consequences.
Define d=n+k, n=dim(phi), k=dim(zeta),

    L=[[q,-B],[0,I]],       N=diag(c I_n,I_k),
    Q0=L* N^-1 L.

q is invertible and N is strictly positive. Supply independent proper complex
Gaussian roots psi~CN(0,alpha^-1 I_d), alpha>0, then independent observations

    Y=L psi+eta,            eta~CN(0,N).

Here CN(0,C) has density exp(-z*C^-1 z)/(pi^d det C) with respect to
ordinary real 2d-dimensional Lebesgue measure. Completing the square gives

    psi | Y=0 ~ CN(0,C_alpha),     C_alpha=(Q0+alpha I)^-1.

The point conditional is the continuous Gaussian version. The unconditional
root law stays the supplied independent prior. No exact equality to C0 is
claimed at finite alpha. The alpha-to-zero limit is a limit of proper priors,
not permission to treat an improper uniform prior as a probability law.

The prior/likelihood Gaussian integral, or Sylvester's determinant identity
applied to Cov(Y)=N+alpha^-1 L L*, gives

    p_alpha(Y=0)=alpha^d/[pi^d det N det(Q0+alpha I)].

For the source itself,

    det Q0=|det q|^2/c^n,
    Q0^-1=[[q^-1 S q^-*, q^-1 B],
           [B* q^-*,            I]],
    q^-1 S q^-*=(q^-1+q^-*)/2.

Thus the supplied source raw mass c^n/|det q|^2 is det(Q0)^-1. Within
each four-arm menu d and c are constant, so equal prior arm weights and
conditioning at Y=0 approach its normalized raw-mass weights as alpha->0.
Across different choices of c, det N changes: the likelihood normalization
cannot be silently discarded to claim the same cross-model weights.

For the disclosed width-four, T_cover=12, xgraded, m=1 source, n=24,
k=40 and d=64. The runner binds the released helper SHA256 and its current
Block105 supplier certificate. It checks all four arm values at c=1/2 and
c=1/3. It does not reinterpret this finite 1+1-dimensional fixture as a
three-dimensional infinite-volume physical field.

## Explicit finite-alpha bounds

If Q0>=m0 I, diagonalization gives

    1 <= det(Q0+alpha I)/det Q0 <= (1+alpha/m0)^d,
    ||C_alpha-C0|| <= alpha/m0^2.

For t>=0,

    1/(1+t)-1+log(1+t) <= t^2/2,

because the derivative of the left side is t/(1+t)^2<=t. Hence the proper
complex Gaussian KL and Pinsker bounds are

    D(CN(0,C_alpha)||CN(0,C0)) <= d alpha^2/(2m0^2),
    TV <= alpha sqrt(d)/(2m0).

One exact finite lower bound is m0=1/Tr(C0), since the largest positive
eigenvalue is at most the trace. Here Tr(C0)=k+Tr Re(q^-1), so no spectral
fit or radical full-matrix inversion is needed. Use the minimum of these
armwise lower bounds for a common menu bound.

Write w_j for the normalized target arm weights and t_j in
[(1+alpha/m0)^-d,1] for their determinant tilts. The perturbed weights are
w_j t_j/E_w(t). A rejection coupling, accepting j with probability t_j,
gives

    TV(w_alpha,w) <= 1-(1+alpha/m0)^-d <= d alpha/m0.

This can be a loose finite bound; it is a bound, not a precision estimate.
The runner also computes the exact rational arm weights at alpha=1/10
and 1/100. It independently conditions the full joint covariance numerically
and compares full precision log determinants to the smaller exact Schur
formula

    P_phi(alpha)=alpha I+(1+alpha) q*(S+alpha c I)^-1 q,
    det Q_alpha=(1+alpha)^(k-n) det(S+alpha c I) det P_phi(alpha)/c^n.

## Positive observation windows: accuracy and rarity

Let W_epsilon={y: |y_i|<=epsilon for all i}, a product of complex disks,
and nmin=min(c,1). Cov(Y)>=N implies Cov(Y)^-1<=N^-1. Thus, throughout
the window,

    exp(-d epsilon^2/nmin) p_alpha(0) <= p_alpha(y) <= p_alpha(0).

Its real volume is (pi epsilon^2)^d, so the acceptance probability obeys

    exp(-d epsilon^2/nmin) alpha^d epsilon^(2d)
       /[det N det Q_alpha]
    <= P(W_epsilon) <=
    alpha^d epsilon^(2d)/[det N det Q_alpha].

Both quantities are positive for finite positive alpha,epsilon. Their decay
as alpha or epsilon shrinks, and their dimension dependence, are explicit.
There is no claimed nonvanishing thermodynamic acceptance probability.

For nonzero y the posterior is CN(C_alpha L* N^-1 y,C_alpha). The identity

    N^-1/2 L C_alpha L* N^-1/2 <= I

follows from C_alpha^-1=alpha I+L*N^-1 L. The KL of this shifted Gaussian
from CN(0,C_alpha) is at most y*N^-1 y, hence at most d epsilon^2/nmin.
Convexity of KL and Pinsker give

    TV(P(psi | W_epsilon), CN(0,C_alpha))
        <= epsilon sqrt(d/(2 nmin)).

Arm weights conditioned on W_epsilon differ from those conditioned by the
zero-density prescription by at most 1-exp(-d epsilon^2/nmin), using the
same rejection coupling. Adding these explicitly controlled errors and the
finite-alpha errors bounds the joint arm/field approximation to the supplied
target. These limits construct a conditional comparison, not typical native
phase selection or a Born rule. A rare selected ensemble is a physical cost.

## Logical local-degree circuit and the remaining spatial obligation

For each source root, a binary fanout tree provides one copy for each matrix
entry that uses it. A unary scale gate applies that coefficient; binary sum
trees compute each row of L. Its final observation gate adds the independent
Gaussian noise of that row. Roots, copies, scales, sums and observations have
total graph degree at most three. Every edge goes from an earlier node to a
later node, so the scalar circuit is a DAG. The runner checks each resulting
linear form exactly against the actual source L. Copying refers to readable
classical record data, not cloning an unknown quantum state.

A finite role/frame and one complex payload have an elementary closed-support
matrix codec, independent of the previous four-payload chart:

    M=z I+(8r+1)(R v).sigma,    v=(1,2,3), r a finite nonnegative integer.

The trace gives z. The traceless Hermitian vector's norm gives r, and its
free proper-cubic orbit gives R. For each r,R the support is an affine copy
of C, closed in M2(C); different labels give disjoint parallel planes.
Ordinary Pauli conjugation co-rotates R while leaving z unchanged. Neither a
physical spinor identification nor selection of the supplied frame follows.

The physical task is to embed the DAG with one payload at each
permanently written cubic site, nearest-neighbor parent reads, and no shared
wire site that introduces a cycle between otherwise unrelated causal stages.
Static precision routing alone does not settle this requirement. The separate causal-embedding derivation now proves a scaled detour
construction for this abstract graph class and tests smaller periodic DAGs.
The full DK coordinate roster remains uninstantiated in that finite checker.

The exact nonzero off-diagonal counts in q*q show that the simple independent
root / diagonal-child-block mechanism of the signed four-cycle does not
directly apply to the phi block of these supplied sources. This tests one
specific factorization, not all scalar orders or all Clifford cancellations.
