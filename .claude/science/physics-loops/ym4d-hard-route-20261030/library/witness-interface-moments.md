# What the interface supplies to the witness moments

Author: openai/gpt-6-astra/max mac-mini-codex, 2026-11-01.
Source: `5f5f1693a60cfcb7aff5ccd1534f626294a37188`.
Status: implications and discharged finite-dimensional identities; source
delivery remains gap. No numerical run, paper lemma or independent review.

## 1. Finite-window pullback moments [implication]

Use the same map, actual mu hierarchy, Theta and admissible tori as **The
interface**. Assume FF_j and FF_(j+1), LOC and the reflection-grid hypotheses
of Lemma 10.6, FLOW's x_j/x_(j+1)<=5/4, LE_j, and GS_j(c) for every finite
n and s. These are named *conditional* producer inputs, not delivered
Wilson estimates. Use the deterministic pullback pi_R of Lemma 14.14 with
R<T_tor/4, where its construction is specified; G means regularity on its
read cube. This restriction suffices at each fixed physical scale as the
torus grows. No unconstructed small-torus completion is being invoked.

FF and the chessboard implication of Lemma 10.6 give, for every q>=1,

    sup_p ||x_(j+1) s_p(W)||_(Lq(mu)) <= M_q(Theta).          (M-1)

The pullback sends each plaquette to a fixed plaquette (possibly reversed),
or to a degenerate loop with zero energy. Consequently, for
Ebar(c';W)=sum_(h>=0) exp(-c_E h) sum_(p in Q_h(c')) s_p(W),
Minkowski and the plaquette count N_h<=C(h+1)^4 give

    ||1_G x_j Ebar(c';W^pi)||_q
      <=(5/4) M_q sum_h exp(-c_E h) N_h <= C_(q,Theta).    (M-2)

Repeated images cause no difficulty: count each original term in this
sum. The bound is independent of R, cutoff and volume. LE supplies
t_n^2<=C_(n,Theta) x_j Ebar. With GS(c), for each fixed n,s>=2,

    E_mu[1_G E_(W^pi) tau_n(V)^s] <= C_(n,s,Theta).          (M-3)

Indeed integrate C_(n,s)(1+t_n^s) and use (M-2) with q=s/2.
Smaller positive s follow by Holder. At fixed normalization the SU(2)
principal flux satisfies |psi_p|<=C sqrt(s_p): writing
s_p=1-cos(theta/2)=2 sin^2(theta/4), 0<=theta<=2pi, use
sin u>=2u/pi on [0,pi/2]. Thus M-3 gives all normalized flux moments
under the replacement law after averaging W, on G. Parallel transport
preserves |psi|, so the same holds for the transported fluxes used here.
Finite products follow by Holder, with higher moment orders specified
before use. This is the missing replacement-law half of H-MOM on fixed
windows, now reduced to FF+LE+GS(c), not to covariance traces.

This argument reads GS(c) for **all n and s**. Its restricted small-cube
version is insufficient. It does not repair that clause for either
producer, and it proves no common-frame regularity of a chart polynomial.

## 2. TV-P at zeroth order [implication]

Let P_W,Q_W be two probability kernels, let their base law be mu, and let
delta=E_mu[1_G TV(P_W,Q_W)], with TV=sup_A|P_W(A)-Q_W(A)|.
If for a real test f and some p>1,

    E_mu[1_G(P_W |f|^p+Q_W |f|^p)]<=M,

then clipping f at magnitude R gives

    E_mu[1_G |P_W f-Q_W f|] <=2R delta+M R^(1-p).           (TV-1)

The bounded part costs 2R times TV. For the tails use
|f|1_(|f|>R)<=R^(1-p)|f|^p and integrate. Choosing
R=delta^(-1/p) for 0<delta<=1 proves a bound
(2+M)delta^(1-1/p); delta=0 follows by increasing R. This uses the
average TV directly, not a supremum over W.

Apply this to OS(c'), f=P(psi/gamma_j) on any fixed template, and the
moments in section 1 plus the actual-law FF moments. It proves the
**finite-window, degree<=8, zeroth-order TV-P** with error o(1), conditional
on those named clauses. In fact any fixed finite degree is allowed if
the corresponding higher moments are supplied. It is not a uniform
operator bound on the entire completed norm class: OS(c') has
window-dependent constants, which must be controlled separately there.

For the fixed triple T, |T|/gamma_j^3 has every fixed finite moment under
these same two laws. To see this without an asymptotic expansion, reduce
each fixed loop to a finite product of transported plaquettes; telescoping
the product gives |v_Gamma|<=C_Gamma sum_p |psi_p|. Then use Holder on
2|v_1||v_2||v_3|/gamma_j^3. Thus TV-1 gives only

    E_mu[1_G |(E_W-E_(W^pi))T|]
       <=C_p gamma_j^3 omega(gamma_j)^(1-1/p).              (TV-2)

The NT2 version needs omega(g)^(1-1/p)=o(g), or a separate cancellation
estimate, to make this o(g^4). Rate-free OS(c') does not provide it.
The bad-set and chart errors also retain their own required rates.

## 3. The exact covariance requirement and its sixth moment [implication]

Fix a finite collection of transported flux components in one common
frame and a polynomial P of degree<=8, with coefficient l1 norm ||P||.
Let phi(W) be the normalized lift, Gamma(W) the fibre covariance, and
Gamma_0 its flat value. Let

    Delta(W)=max_(u,v)|Gamma_uv(W)-Gamma_0,uv|,
    V(W)=max_u max(Gamma_uu(W),Gamma_0,uu).

For consumption of OS(d), D_W below means its curl followed by the
orthogonal transports evaluated at V^*. Such transports preserve each
block's Hilbert--Schmidt norm and each diagonal trace. Variation of the
transports in the actual flux observable is part of JET8 below; OS(d)
is not silently asserted for a different, full observable Jacobian.

For positive semidefinite covariances, Gaussian interpolation gives

    |E_Gamma(W) P(phi+b)-E_Gamma_0 P(phi+b)|
      <=C_D ||P|| Delta(W)[1+|phi|^6+V(W)^3].               (C-1)

Here D is the fixed finite template, not the volume. Proof: interpolate
Gamma_t=Gamma_0+t(Gamma-Gamma_0). For positive definite Gamma_t,
d/dt E P(phi+b_t)=(1/2)sum_uv (Gamma-Gamma_0)_uv
E partial_u partial_v P(phi+b_t). This follows by differentiating the
Gaussian density and integrating by parts twice. Each derivative has
degree<=6 and coefficient norm bounded by C_D||P||. A centred Gaussian
with coordinate variance<=V has sixth absolute moments bounded by C V^3:
one-dimensional integration by parts gives E Z^6=15(E Z^2)^3;
Holder handles products. Expansion and (a+b)^6<=32(a^6+b^6) give C-1.
Add epsilon I and let epsilon decrease to zero to cover singular
covariances; polynomial moments are polynomials in covariance entries.

An exact sufficient input for finite-window COV8 is therefore

    E_mu[1_G Delta(W)(1+|phi(W)|^6+V(W)^3)] -> 0.           (C-2)

This is a covariance *difference*, not a difference of covariance norms.
It displays where the sixth moment enters. In particular, if Delta is
uniformly bounded on G and tends to zero in probability, V is uniformly
bounded, and phi has a uniformly bounded (6+eta)-th moment for some
eta>0, then C-2 follows by truncating |phi| and using uniform
integrability. A sixth-moment upper bound alone is not uniform
integrability of |phi|^6; the higher moment or an explicit tail bound is
needed for that inference.

**Source of these moments.** OS(a), interpreted with its stated
exponentially summable local envelope, and (M-1) give every fixed moment
of phi, by Minkowski and FLOW. OS(d) bounds diagonal traces near their
flat values on G; a uniform bound on the *flat* diagonal covariances
then bounds V. That flat bound is the quadratic portion of H-TREE (or
must be proved directly in the free blocked theory). Gaussian sixth
moments follow as above; actual-law and replacement-law sixth absolute
moments follow from FF and section 1. None of these upper bounds fixes
the value of an invariant sixth moment. The Sigma_+/Sigma_- example in
`witness-moment-gap.md` remains an exact obstruction to that inference.

## 4. A possible C2 route: one additional trace is enough [implication]

It would be too strong to say that the entire enlarged interface has no
possible covariance route. C2_j tests invariant chart polynomials and
could supply the missing off-diagonal information. Here is the exact
reduction, including its unmet qualifications.

For a real 3 by 3 block B=Gamma_pq(W) and its flat value c I_3,

    ||B-cI_3||_HS^2=||B||_HS^2+3c^2-2c Tr B.              (C-3)

No symmetry of this off-diagonal block is needed. If |c| and ||B|| are
uniformly bounded, both
| ||B||_HS-sqrt(3)|c| |->0 and |Tr B-3c|->0 force
||B-cI_3||_HS->0. When c=0 the norm estimate alone suffices.
OS(d) supplies the first estimate, and the diagonal trace, but not the
off-diagonal trace Tr Gamma_pq. Thus a sufficient smaller new request is

    E_mu[1_G |Tr Gamma_pq(W^pi)-Tr Gamma_pq(1)|] -> 0
              for every pair in the fixed template.       (CT2)

Together with OS(d), uniform flat variances and the moments just stated,
CT2 implies finite-window COV8: C-3 gives Delta->0 in probability;
positivity and bounded diagonal variances bound Delta; then use C-2.

To obtain CT2 from C2_j, the specific test is

    T_pq(W,xi)=sum_a (D_W xi)_p^a (D_W xi)_q^a,            (ADM2)

with the transports included in D_W. One must verify that it belongs to
the stated common-chart, joint-colour-invariant C2 class with
||T_pq||<=C_(D,Theta) uniformly in j and gamma, and that its good law is
the chart law approximated by OS(c), or prove the following transfer:

    E_mu[1_G |E_(W^pi)^good T_pq(W^pi,.)
                          -Tr Gamma_pq(W^pi)|]=o(1),
    |E_1^good T_pq(1,.)-Tr Gamma_pq(1)|=o(1).               (GOOD2)

If these hold, C2(a) and (M-2) bound the remaining comparison by
C_(D,Theta) E[1_G Ebar(W^pi)]=O(gamma_(j+1)^2), proving CT2.
GOOD2 could follow from OS(c) plus a common good-event identification
and polynomial uniform integrability. Its two displayed errors cannot
be erased merely because both laws are called a chart law.

**Gap.** The interface does not identify those good laws or state uniform
common-frame C4 norm bounds for ADM2's actual D_W and transports. C2 is
not an estimate for arbitrary colour-labelled tensor entries, and its
norm includes all field dependence. We have not proved ADM2/GOOD2 from
either producer. Hence COV8 still needs CT2 (or C-2) as an additional
supplier obligation, or this explicit C2 realization. This is a precise
missing bridge, not a claimed logical countermodel to all named clauses.

## 5. G0 and the stop [gap; dependencies now narrower]

Even finite-window COV8 and the zeroth-order TV-P do not finish G0. OS(b)
expands s_p, not every transported flux polynomial. One also needs the
actual framed flux chart and normalized lift linearization, for example

    E_chart[1_G |P(psi_j/gamma_j)
              -P(phi+D_W xi)|]=o(1)||P||,
    E_(mu,b)[1_G |P(phi+b)-P((gamma_(j+1)/gamma_j)A_j Z_(j+1)+b)|]
                                                   =o(1)||P||,          (JET8)

Here E_chart integrates mu(dW) and the replacement fibre's actual chart
law in xi, with psi_j the flux of that chart field; its failed-chart
contribution must also be bounded. In the second line b has the flat
Gaussian covariance independently of W, and Z_(j+1) is the coarse flux
of W. These are joint-law estimates, not expectations over W alone.
The coefficients must have the uniform integrability needed by OS(c).
For a fixed polynomial, JET8 + OS(c) + COV8 + zeroth-order TV-P give G0
by adding and subtracting the three surrogate expectations. For the
iteration in repaired 4.3 these estimates must hold on the **completed
weighted norm class**, and the transfer contraction (2)-(3) of
`witness-moment-gap.md` is still separately needed. Neither OS(a)'s
curvature sup bound nor a finite-template argument proves that closure.

Thus no invariant sixth moment value, full COV8, completed-class G0 or
NT2 first-order matching has been derived for Wilson. A finite-window
piece of TV-P and its required moment source have been resolved as
implications of named interface clauses; the remaining tensor/chart/law
and norm obligations are explicit. This is the first dependent stop.
