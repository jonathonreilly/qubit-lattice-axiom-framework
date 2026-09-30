# Polynomial field-weighted absorption for the actual low-global-excitation fast sector

Root analytic extension; candidate pending a focused independent check. Supplied rotor model, W=1, global N_B<=9, even cubic L>=6, fixed delta,kappa>0. Import only the exact operator bounds and unweighted decay from the frozen FAST_ONE_HOLE_ABSORPTION.md3950bd73aea13b20fac74585c639fb5903bde25cac1a7d2f9308ab771ce6371c, now fully root checked in independent-fast-small-sector-check/REPORT.mda8b68b5dcb912522927a7e30f9d5f34c413aee9979d2a3b6fc0e2423acd22b8f. No full microscopic convergence, thermodynamic density substitution or formal status is inferred.

## Target

Let Q=1+sum_links|E| on the fixed finite torus, A=−i delta H−kappa G/2, S(t)=exp(tA). The imported bound is ||S(t)||<=C0 exp(−gamma t), with C0>=1 and gamma>0 independent of volume and fields in the stated sector. H has Q bandwidth2 and norm<=M=1092; G commutes with Q. The stack J of original labelled jump maps has J†J=G<=12 and input/output Q bandwidth1.

For every nonnegative integer p and every psi in D(Q^p), prove

 ||Q^p S(t)psi||<=C0 exp(−gamma t) R_p(t)||Q^p psi||,           (P1)

where R_p is an explicit degree-p polynomial. Also prove a finite integrated Q_out^(2p) moment of the ACTUAL original absorbing output with only the initial Q^(2p) moment, thereby removing the exponential-input hypothesis of the author's A10. This does not remove the small global-N_B or leading-rotor-fast restrictions.

## Bounded commutators and domains

Let H_r be the Fourier band at integer Q difference r, −2<=r<=2; each has norm<=M. Consequently for integer j>=1,

 K_j=ad_Q^j(A)=−i delta sum_(r=−2)^2 r^j H_r,
 ||K_j||<=h_j:=5delta M 2^j.                              (P2)

The dissipative part contributes zero. On the finite-field core, exact multiplication gives

 Q^p A psi=A Q^p psi+sum_(j=1)^p binom(p,j)K_j Q^(p−j)psi. (P3)

Since Q>=1, (P3) bounds A on the graph space D(Q^p) equipped with norm||Q^p psi||. A has finite bandwidth, so it maps the finite-field core into itself; approximate graph-domain vectors by spectral finite-field projections and use closedness of Q^p to extend (P3) and the graph-space bound. The convergent exponential of this bounded graph-space operator agrees with the Hilbert-space exponential by uniqueness of its power series. Thus S(t) preserves D(Q^p). No transition or generator is changed at a field cutoff.

Repeated commutation of that same power series, or induction from Duhamel, gives bounded operators C_p(t)=ad_Q^p S(t), C_0(t)=S(t), with

 C_p(t)=sum_(j=1)^p binom(p,j)
          integral_0^t S(t-s) K_j C_(p−j)(s) ds.           (P4)

This identity first holds on the common core; the induction below supplies bounded extensions on the full Hilbert space. It is not a claim that Q itself is bounded.

## The polynomial recurrence

Set P_0(t)=1, P_p(0)=0 for p>=1, and

 P_p'(t)=C0 sum_(j=1)^p binom(p,j)h_j P_(p−j)(t).         (P5)

These are positive-coefficient polynomials of degree p. Using(P4), the imported semigroup estimate twice and induction yields

 ||C_p(t)||<=C0 exp(−gamma t)P_p(t).                     (P6)

Indeed the product of semigroup factors contributes C0² exp(−gamma t), and the remaining integral is exactly P_p(t)/C0. Equivalently the exponential generating function is

 sum_(p>=0) P_p(t) z^p/p!
   =exp[5 C0 delta M t (exp(2z)−1)].                    (P7)

Thus P_p(t)=2^p T_p(5 C0 delta M t), where T_p is the Touchard polynomial, T_0=1 and T_p(x)=sum_(j=1)^p {p brace j}x^j for p>=1. This is a polynomial identity, not use of a stochastic replacement process.

The exact graph-domain identity

 Q^p S(t)psi=sum_(r=0)^p binom(p,r) C_r(t)Q^(p−r)psi

and Q>=1 give(P1) with

 R_p(t)=sum_(r=0)^p binom(p,r)P_r(t).                   (P8)

For p=0 this reproduces the imported unweighted bound. For example R_1=1+2bt and R_2=1+8bt+4b²t², b=5C0delta M. No assumption of a finite exponential field norm has entered.

## Original absorbing output

For the three Q-band components J_r of the labelled map J, norm<=sqrt(12) and Q_out=q+r on an input Q eigenvalue q>=1. Therefore, on nonzero matrix entries, Q_out/Q_in<=2. Summing the bands gives the bounded map

 ||Q_out^p J Q_in^(−p)||<=3 sqrt(12) 2^p.               (P9)

This acts into the original direct sum of labelled physical output Hilbert spaces. It does not combine edges or turn a coherent sign into a separate record. Using(P1) and(P9),

 integral_0^infinity kappa sum_m ||Q_out^p j_m S(t)psi||²dt
   <=108 kappa 4^p C0² I_p ||Q_in^p psi||²,
 I_p=integral_0^infinity exp(−2gamma t)R_p(t)²dt <infinity. (P10)

If R_p(t)²=sum_j d_j t^j, then I_p=sum_j d_j j!/(2gamma)^(j+1), a finite explicit positive expression. Any additional nonnegative integer waiting-time moment follows by replacing j! by(j+r)! and the denominator power accordingly. Unweighted total absorption is exactly||psi||² by norm-loss identity and the exponential survival limit; the p=0 constant in(P10) is only a conservative upper bound.

Finally diagonalizing a positive input density and summing the nonnegative expressions extends(P1)'s squared estimate and(P10) to every input density with Tr(Q^(2p)rho)<infinity. Monotone bounded field-observable cutoffs and positive spectral finite-rank sums justify these passages without a preferred decomposition; no Loewner monotonicity of P_R rho P_R is assumed. The field observable is always the actual link field in the physical output.

## Scope and unresolved work

The improvement is limited and precise: the input need only have the relevant polynomial field moment. It supplies no decomposition of the full microscopic evolution into independent one-hole excursions, no uniform finite-spin replacement of H, no multi-hole absorption theorem, and no control over an extensive background from a local low-density assumption. Those remain the source-specific missing bridge.
