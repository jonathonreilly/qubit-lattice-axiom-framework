# Conditional quantitative consequence of a full source-containment certificate

Root analytical continuation on the SAME fixed finite leading W1 rotor fibers, not a proof of the missing containment. Actual H(theta) is the finite Hermitian Laurent matrix, G is the original fixed positive diagonal loss, and Z(theta)=-i delta H(theta)-kappa G/2 with fixed delta,kappa>0. All original field-cycle variables are retained. Suppose, as an EXTRA UNPROVED HYPOTHESIS, that the full invariant dark space N(theta) is formally fresh-source orthogonal for almost every phase. This is exactly the containment identified in ROOT_REDUCTION, not a protected-submodule substitute. No scientific computation or new physical law.

The conclusion below is a polynomial phase-averaged unweighted no-event tail for a source whose fiber trace density is bounded. That regularity is an additional declared condition here; it is not silently assigned to the full microscopic source. It yields no integrable residence or energy UI.

## 1. Uniform finite-dimensional Gram comparison

Let d be the full finite fiber dimension and O_H=[G;GH;...;GH^(d-1)]. Use the fixed interval[0,1] and W(theta)=integral_0^1 S_theta(t)* G S_theta(t)dt. There is c>0 depending only on d,delta,kappa,G and a uniform bound for||H||, such that

    W(theta) >= c O_H(theta)*O_H(theta).                 (1)

Here is a direct justification with no phase-generic observability assertion. Put f(t)=sqrt(G) exp(tZ)v. Each scalar component satisfies the order-d constant-coefficient ODE supplied by Cayley-Hamilton for Z. Its monic ODE coefficients range over a compact box because ||Z|| is bounded uniformly. For every coefficient tuple in that box, the map from the d initial derivatives to the function on[0,1] has a strictly positive L2 Gram matrix: a solution zero throughout an interval has all initial derivatives zero. The companion system solution and its Gram depend continuously on those finitely many coefficients. Compactness therefore gives one positive minimum Gram eigenvalue for the ENTIRE box. Summing componentwise,

    integral_0^1 ||f(t)||²dt >= c0 sum_(j<d)||sqrt(G)Z^j v||².

This remains true for nonnormal Z and defective characteristic roots; no eigenvector diagonalization was used. Expand powers of Z=-i delta H-kappa G/2 and classify each non-pure-H word by its RIGHTMOST G. This gives

    G Z^j=(-i delta)^j G H^j+sum_(l<j) B_jl G H^l,

with bounded matrix coefficients B_jl, uniformly over the H norm ball. Triangular inversion (delta>0) bounds the O_H norm by the stack of G Z^j. Finally||G w||<=sqrt(||G||)||sqrt(G)w|| proves(1), adjusting constants. If G=0, formal-source orthogonality forces the source zero and the conclusion is trivial.

## 2. A genuine Laurent minor prices the decay

Let r be the generic rank of O_H, and choose any actual nonzero r-by-r Laurent minor q(theta). Its existence at generic rank is algebraic; no specific minor or full containment is constructed here. On q!=0 the rank is r. If r=0, the source is again zero under the stated containment. Otherwise let M bound||O_H||. Cauchy-Binet applied to its nonzero singular values gives

    lambda_min_positive(O_H*O_H) >= |q(theta)|²/M^(2(r-1)).  (2)

Indeed the product of all r positive eigenvalues is the sum of squared r-minors and at least|q|², while the other r-1 eigenvalues are at most M².

N=ker O_H reduces both H and G. The exact loss identity is

    ||S_theta(1)v||²=||v||²-kappa <v,W(theta)v>.

For v in N orthogonal complement, (1)-(2) give one-step contraction by1-c1|q|². Choose c1 small enough that this number is nonnegative; the loss identity itself bounds the admissible constant. Invariance of N orthogonal complement and iteration yield

    ||S_theta(t) P_(N perpendicular)||² <= C exp(-c1 t |q(theta)|²)  (3)

for all t>=0 and q!=0. Constants depend on the FULL fixed sector and supplied coefficients. No volume, spin or parameter uniformity is claimed.

## 3. Elementary phase sublevel bound

Multiply q by a Laurent unit so it is an ordinary polynomial in its unit-circle variables. Let s_i be its degree range in variable i and S=sum_i s_i. If S=0, q is a nonzero constant and(3) is uniformly exponential. If S>0, there is a finite q-dependent C_q such that normalized Haar measure obeys

    measure{|q|<=eta} <= C_q eta^(1/S),   0<eta<=1.       (4)

An elementary induction supplies this deliberately weak exponent. Treat q as a degree-m polynomial in one variable with leading coefficient a in the remaining variables. For |a|>eta^beta, factor this one-variable polynomial over C. Small product implies some root is within(eta/|a|)^(1/m) of the circle point. The union of m such disks has circle measure at most C_m(eta/|a|)^(1/m). The set |a|<=eta^beta is bounded by induction. If the leading coefficient has remaining degree-range sum S_a>0, choose beta=S_a/(S_a+m), obtaining exponent1/(S_a+m)>=1/S. If a is a nonzero constant, factorization directly gives exponent1/m>=1/S. Zero degree variables are omitted. Constants absorb coefficient magnitudes and the non-small eta range. This proves(4) for the actual correlated Laurent polynomial, not independently weighted paths.

Integrating(4) against2c1 t eta exp(-c1 t eta²)deta gives

    integral exp(-c1 t |q|²)dtheta <= C (1+t)^(-1/(2S)). (5)

The zero set q=0 is Haar null. No unproved literature regularity theorem is required for this elementary finite-polynomial estimate.

## 4. Source-density scope and unresolved consumer

For a positive trace-class source rho on the physical direct-integral Hilbert space, define its positive fiber trace density through any positive rank-one decomposition. This density is the sum of the fiber outer products of those vectors; rho is NOT identified with a diagonal multiplication operator and no dephasing is performed. Suppose its fiber density R(theta) has range in N(theta) orthogonal complement almost everywhere, and esssup_theta Tr R(theta)<=B<infinity. Then the actual decomposable semigroup trace is bounded by

    Tr(S(t)rho S(t)*) <= B integral ||S_theta(t)P_(N perpendicular)||²dtheta
                      <= C B (1+t)^(-1/(2S)).           (6)

The first range condition follows for formal fresh sources from the EXTRA full-containment hypothesis. It could instead be established for a particular actual source directly. The bounded-density condition is not proved here for every physical source or for the microscopic process. Arbitrary normalizable sources still have only the earlier dominated-convergence conclusion without this additional regularity.

For S>=1, the guaranteed exponent1/(2S) is at most1/2. This weak upper estimate therefore supplies NO finite integrated residence, weighted electric moment, quadratic UI, arbitrary-volume limit or continuously forced microscopic closure. A concrete full-containment row identity/nonzero rank certificate is still missing; a quantitative theorem for actual sources also requires its density control. This conditional implication makes the value and limitations of such a future certificate explicit. It does not replace its construction or count as a new milestone.
