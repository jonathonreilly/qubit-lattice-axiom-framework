<!-- Owning original: PR9755; source SHA256 33832d1197c7795360a609cbb4052e5fca0cde0621331f0b6378011a3548c9be. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Fixed-order local normal-form check for commuting longitudinal bonds

Checked 2026-10-18 against the root's stated new construction. This is a finite-order statement for H/Jz=2N+lambda V, up to the omitted constant longitudinal vacuum energy, with N=sum_z (1-ZZ)/2. It is not an optimized-order/exponentially long prethermal theorem and does not prove a resonance or selected equilibrium state.

## Homological operator

Let alpha_theta(A)=exp(i theta N) A exp(-i theta N) and [N,A_m]=m A_m. Integer spectrum of N gives integer m, including in degenerate sectors. Then

    P A = (1/2pi) integral alpha_theta(A) dtheta,
    S(A)=sum_(m!=0) A_m/(2m)
        = i/(4pi) integral_0^(2pi) (theta-pi) alpha_theta(A) dtheta.

Indeed integral(theta-pi) exp(i m theta) dtheta=2pi/(i m). Therefore [S(A),2N]=-(A-P A). For Hermitian A, A_m dagger=A_-m, making S(A) anti-Hermitian. The sign is appropriate to exp(lambda S) H exp(-lambda S). The operator-norm bound is pi/4 times ||A||, since integral |theta-pi| dtheta=pi^2. No additional Q norm factor is needed in this sawtooth representation.

All bond terms in N commute. Bonds disjoint from A's ORIGINAL support commute with both A and the other bond rotations and cancel out. Thus alpha_theta(A), P A and S(A) are supported on X enlarged by its two longitudinal neighbor sets, not by iterative spread. For a0(A)=sup_i sum_(X contains i)||A_X||, assigning each transformed term to that enlarged support gives

    a0(S A) <= (3pi/4) a0(A),
    a0(P A) <= 3 a0(A).

The factor three comes from possible original support at i or either z neighbor. Repeated neighbors or short boundaries only decrease this upper bound. Individual homogeneous pieces can be assigned to the enlarged support; no global inverse or chosen state is used.

## Nested commutator estimate

For finite-range decompositions with maximum term cardinalities s_A,s_B, assigning commutator terms to unions and using disjoint-support commutation gives

    a0([A,B]) <= 2(s_A+s_B) a0(A) a0(B).

After j commutators the support cardinality is at most s_B+j s_A (a deliberately loose bound). Consequently

    a0(ad_A^n B) <= (2 a0(A))^n
       product_(j=0..n-1)[s_B+(j+1)s_A] a0(B).

The root's displayed product is therefore valid. Dividing by n!, the majorant has radius at least 1/(2 s_A a0(A)) in the conjugation parameter. Polynomial factors in n do not remove that positive radius. Extensive global operator norms must not replace a0 here.

## Exact finite product, rather than formal series only

A small extra step is needed when composing several conjugations: after the first exact exponential the interaction has unbounded support, so one cannot simply reapply the finite-s_B inequality to that exact transformed interaction. Instead majorize the joint nested expansion from the original finite-range H.

Fix order m and finite-range S_1,...,S_m from the formal recursion; put s=max_k s_(S_k). Every mixed word with n total commutators obeys the same support product with s, and its a0 factors are the product of a0(S_k). Summing the factorial denominators of the product exponentials by total n yields the multinomial bound

    a0(U(lambda) B U(lambda)^-1)
    <= a0(B) sum_(n>=0) [2 A(lambda)]^n/n!
          product_(j=0..n-1)[s_B+(j+1)s],

    A(lambda)=sum_(k=1..m) |lambda|^k a0(S_k).

This converges whenever 2s A(lambda)<1, uniformly in volume. It defines an actual locally analytic interaction-valued conjugation near lambda=0, agreeing with the finite-volume exact product. At real lambda all generators are anti-Hermitian and U is unitary. At complex lambda analyticity does not require unitarity.

At each recursion stage the order-k coefficient is a finite sum of local commutators, hence finite range and finite support size. Choosing S_k with the homological inverse removes its off-N part; its P part defines D_k. The formal coefficients through order m consequently agree with the convergent exact expansion and commute with N. A Cauchy/Taylor estimate on a smaller fixed lambda disk yields

    a0(R_m(lambda)) <= C_m |lambda|^(m+1),

with C_m independent of volume. Constants may grow rapidly with m; no useful uniform-in-m or optimal-order conclusion follows from this bound.

The same argument can retain exponential diameter weights: diam(X union Y)<=diam X+diam Y for overlapping supports. Replace a0 by a_mu and use the finite generator ranges, shrinking the lambda radius as needed. This supplies quasi-local interactions rather than only a bare a0 estimate if a later Lieb-Robinson comparison needs them. Alternatively fixed support-cardinality weights work similarly. The exact remainder is quasi-local, not strictly finite range.

## Qualifications

The construction uses only the integer commuting-bond structure and fixed-order local commutator estimates. It does not require an on-site decomposition or a nondegenerate vacuum, so invoking an on-site theorem without adaptation is unnecessary. Periodic or open finite boxes admit the same upper bounds; their local restrictions must be chosen consistently for an infinite-volume limit. Symmetries commuting with N and respected by V pass through P/S and the recursion. The lambda-sign checkerboard symmetry gives order-by-order parity covariance when that lattice symmetry actually exists.

An interaction-norm bound on R_m is not a small global Hilbert-space operator norm in infinite volume, nor by itself a bound on a pole of the microscopic resolvent. Local-time bounds need the subsequent locality argument and specified observables/state; growing wave packets need their support factors tracked. Long-time ground-state selection and microscopic source identification remain separate.

Conclusion: the proposed finite-order actual normal form and volume-uniform local remainder are supported by the stated estimates, provided the exact product is bounded via the joint mixed-word expansion above (or an equivalent analytic interaction-space argument).
