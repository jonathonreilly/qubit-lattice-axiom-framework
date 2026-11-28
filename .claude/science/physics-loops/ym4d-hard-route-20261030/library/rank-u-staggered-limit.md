# A bounded staggered sequence kills the limit clause of (RANK-U)

Source pin: `892504e4c63f195fbd791a1db913f67b4b749459`.
Author: openai/gpt-6-astra/max, mac-mini-codex. This is an exact author proof
in the finite lattice model, not a numerical observation or an audit.
The definitions and the polynomial computation (U6) are rebuilt in
`rank-u-finite-cell.md`. No hard-core or literature input is used.

## 1. Statement

**Discharged (counterexample to the stated limit clause).** For every integer
L>=4 let R={0,...,L-1}^4, ell=L-1, and use positive internal links and the
counting inner product. Take the unit constant flux F=e01, axial base
potential e_F=x0 e1, and

    sigma(x)=(-1)^x1,       f(x0)=x0^3,
    s(x)=sigma(x) f(x0),
    t_epsilon(x)=x1+epsilon s(x),
    0<epsilon<=1/(4 ell^3).                                    (S1)

Then `||d_0 t_epsilon||_infinity<=3/2`, so M=2 suffices for every L.
Nevertheless there is a constant C_L, specified explicitly below, such that

    ||m_epsilon(J)||_2 <= C_L epsilon ||J||_2
          for every J in NN(t_epsilon),                        (S2)

and consequently every convergent sequence of these kernel projections as
epsilon tends to zero carries the *zero* limiting moment map. The limiting
spaces have positive dimension. Thus the limit-subspace assertion in
(RANK-U), not merely a proposed proof of it, fails on every such box.

This statement does not assert that m_epsilon is identically zero at a
fixed positive epsilon. Pointwise nonvanishing without the limit clause
is a different question and is not settled by this example.

## 2. Gauge bound and two extra exact constraints

**Discharged.** Write A_epsilon=e_F+d_0 t_epsilon=A_0+epsilon d_0 s with
`A_0=(x0+1)e1`. The only nonzero components of d_0 s are

    (d_0 s)_0 = sigma [(x0+1)^3-x0^3],
    (d_0 s)_1 = -2 sigma x0^3.                                 (S3)

The second has magnitude at most 2 ell^3; the first at most 3 ell^2.
For ell>=3 this gives `||d_0 s||_infinity<=2 ell^3`, and (S1) implies the
claimed bound on d_0 t_epsilon (in fact at most 3/2).

Let J be any conserved current with rho(J,A_epsilon)=0. For a=2,3 set
`lambda_a(x)=sigma(x) x_a`. The endpoint average of lambda_a vanishes
on every 1-link, whereas A_0 vanishes on all other links. Hence

    lambdabar_a A_0 = 0

as an exact link field. Multiplying the density equation by lambda_a and
summing over sites gives, for epsilon!=0,

    0=<J,lambdabar_a d_0 s>.

By (S3) the field on the right is `x_a [(x0+1)^3-x0^3] e0`.
The elementary finite-difference product identity is

    d_0(f(x0)x_a) = x_a [(x0+1)^3-x0^3] e0 + f(x0)e_a.

Pairing with the conserved current J therefore proves

    <J,x0^3 e2>=0,             <J,x0^3 e3>=0.                  (S4)

These constraints hold for *every* nonzero epsilon, before the harmonic
moment constraints are imposed. They disappear from the density equation
at epsilon=0. No division by a small number is used in any estimate below;
division by epsilon here establishes an exact zero for epsilon!=0.

## 3. The component in direction 1 is small

**Discharged.** Let `r=rho(J,d_0 s)`. Since rho is linear in its field,

    rho(J,A_0)=-epsilon r.

Fix x0,x2,x3 and write j_n for J_1 on the link from x1=n to n+1,
with j_{-1}=0 at the boundary. At sites n=0,...,L-2 this reads

    (x0+1)(j_n+j_(n-1))/2 = -epsilon r_n.

Induction gives `|j_n|<=(2 epsilon/(x0+1)) sum_(k=0)^n |r_k|`.
Summing first over n and then over the transverse chains, and using x0+1>=1,
gives

    ||J_1||_1 <= 2 epsilon ell ||r||_1
              <= 2 epsilon ell ||d_0 s||_infinity ||J||_1
              <= 4 epsilon ell^4 ||J||_1.                     (S5)

The middle inequality follows because each link contributes half its
absolute weighted value at each of its two endpoints. The unused last
boundary-site equation can impose more constraints but cannot spoil (S5).

## 4. All six components of m tend to zero

**Discharged.** Use e_(mu,nu)=x_mu e_nu and the following particular
polynomials for the Wilson cubic form at F=e01:

    P_12=-(x0^3/3)e2,          P_13=-(x0^3/3)e3,
    P_01=P_02=P_03=P_23=0.                                   (S6)

The plaquette calculation proving `H P_k=VV(delta_l,e_k,e_F)` for these
polynomials is (U6) in `rank-u-finite-cell.md`; it uses precisely the
normalization VV=sum(phi wedge m wedge n) of witness Text 3.13.
Any other degree <=3 particular solution differs by PP_h and gives the same
functional on NN. By (S4), every J under consideration annihilates all P_k.

Let J now belong to NN(t_epsilon), so it additionally annihilates PP_h.
Split `t_epsilon=x1+epsilon s` in
`m_k(J)=<J,P_k-tbar_epsilon e_k>`. The epsilon part obeys

    |epsilon <J,sbar e_k>| <= epsilon ell^4 ||J||_1.            (S7)

For k=02,03,23 the remaining field x1bar e_k is respectively
`x1 x0 e2`, `x1 x0 e3`, `x1 x2 e3`. Each is a mixed quadratic with zero
scalar Laplacian and zero divergence, hence H=0. Their pairings vanish by
the harmonic constraints.

For k=01 the remaining field is `x0(x1+1/2)e1`, whose pairing has magnitude
at most ell^2 ||J_1||_1. For k=1a with a=2,3 it is x1^2 e_a. Conservation
and the exact site-polynomial identity

    d_0(x1^2 x_a) = (2x1+1)x_a e1 + x1^2 e_a

show that its pairing has magnitude at most 2 ell^2 ||J_1||_1. Combining
these bounds, (S5), and (S7) yields, for every k,

    |m_k(J)| <= epsilon (8 ell^6+ell^4) ||J||_1.

There are E=4(L-1)L^3 links. Thus (S2) holds with the explicit constant

    C_L = sqrt(6 E) (8 ell^6+ell^4).                           (S8)

No optimization, asymptotic fit, or numerical singular value enters this
bound. Its growth with L is irrelevant: L is fixed before epsilon tends
to zero, and the counterexample works for each L.

## 5. A nonzero limiting space with zero moment map

**Discharged.** Take `epsilon_n=1/(4 ell^3 n)`. The two constraints defining
NN have at most V-1 divergence rows, V density rows, and 140 polynomial
rows, since there are 4*binomial(7,3)=140 component monomials of degree
<=3. With V=L^4,

    dim NN(t_epsilon) >= E-2V+1-140
                        = (2L-4)L^3-139 > 0       (L>=4).     (S9)

The polynomial harmonic space can have fewer columns, which only improves
this bound. Orthogonal projections onto NN have a convergent subsequence
in finite dimensions: they lie in the compact set of symmetric idempotent
matrices of norm at most 1. Call its limit S. It is a projection, and its
trace is the limit of the traces, so its rank is at least the positive
lower bound in (S9). The constraint matrices converge to those at t_0=x1,
so im S is a subspace of NN(t_0).

The moment matrices T_epsilon converge to T_0 entrywise, because P is
fixed and tbar is affine in epsilon. Estimate (S2) gives
`||T_epsilon Pi_NN(t_epsilon)||_op<=C_L epsilon`. Taking the convergent
subsequence proves

    T_0 S = 0,                  rank S > 0.                    (S10)

This is exactly a limiting NN-space carrying zero m in the bounded set
specified by (RANK-U). If the simultaneous limit of N is desired, take a
further subsequence of its projections; (S10) is unchanged.

**Discharged (direct check of the limit, without the rate estimate).** For
any convergent sequence J_n in NN(t_epsilon_n), its limit J belongs to
NN(t_0) by continuity of the constraint matrices. The density equation at
t_0, starting at x1=0, forces J_1=0 on each chain. Equations (S4) pass to
the limit and kill (S6). The 02,03,23 terms are harmonic. The 01 term has
only component 1. The 12 and 13 terms reduce by the displayed gradient
identity to component 1. All six limiting moments are therefore zero.
For a vector J in the limiting projection space, choose
J_n=Pi_NN(t_epsilon_n)J, which converges to J. This proves (S10) directly
and checks the same conclusion separately from the constants in (S8).
This is a second calculation by the same author, not an independent review.

At t_0 itself m need not vanish on its larger kernel: the explicit
`J=H(02-plaquette)` of the finite-cell lemma has m_J=2e12 there. The rank
jump is the mechanism, not an empty kernel or an unbounded gauge.

## Consequences and limits

- **Discharged:** the source's limit version of (RANK-U) is false at M=2
  for every L>=4 in the axial reference convention used above, with exact
  unit flux and arbitrarily small perturbations of a bounded gauge. The
  reference-gauge conversion and its changed bound are specified below.
- **Discharged:** using any normalization w(J)>=||J||_2, including the
  source's higher-moment normalization with this term included, still gives
  `||m_epsilon(J)||/w(J)<=C_L epsilon`. Thus that normalization cannot
  restore a positive uniform lower bound in this sequence.
- **Gap:** pointwise nonvanishing at each fixed t, a method that does not
  impose the exact density kernel, and the source's suggested two-far-source
  replacement are not resolved here.
- **Gap:** this counterexample is to a local input in one proof route. It
  does not construct a covariance matching all Wilson/level-j tree tests
  and does not disprove the conclusion of Theorem 3.19 or NT2.

## 6. Reference-gauge convention and the exact quantifier covered

**Discharged.** If e_F is required to be the uncentered Fock potential
`e_F^f=(-x1 e0+x0 e1)/2`, replace (S1) by

    t_epsilon^f=x1+(x0 x1)/2+epsilon sigma x0^3.

The actual A_epsilon is unchanged and
`||d_0 t_epsilon^f||_infinity <= ell/2+3/2`. For a Fock potential centered
in the box a further linear gauge suffices, and the safe bound M_L=L+2
covers it. This is finite for every fixed box. The constrained spaces and
the moment map are unchanged, as verified next.

Put chi=x0 x1/2, so e_F^ax=e_F^f+d_0 chi. The plaquette Ward identity is

    VV(a,b,d_0 chi)=-<H a,chibar b>+<H b,chibar a>.              (S11)

Here is a derivation rather than an imported identity. On an oriented
plaquette path the antisymmetric area of b and d_0 chi telescopes to
`2 chi(base) phi(b)-2<J_p,chibar b>`. Also
`2 VV_p(a,b,d_0 chi)` equals phi(a) times that area for b minus phi(b)
times the area for a, by expanding the determinant phi wedge m wedge n.
The two basepoint terms cancel. Summing and using
`sum_p phi_p(a) J_p=H a` proves (S11) for finitely supported a; all uses
here have a a single link, so no boundary or decay limit is needed.

Since H e_k=0, (S11) shows that valid Fock-reference particular polynomials
are `P_k^f=P_k^ax+chibar e_k`. They still have degree <=3, and

    P_k^f - tbar_epsilon^f e_k
         = P_k^ax - tbar_epsilon^ax e_k.

Thus the moment matrices in the counterexample are exactly identical.
If the test potentials e_k are also changed by quadratic-polynomial
gradients d_0 eta_k, their particular solutions change by etabar_k e_F.
The resulting change in the moment field is
`etabar_k e_F - tbar d_0 eta_k = etabar_k A - d_0(t eta_k)`,
whose pairing is zero on N. This proves invariance of the asserted moments
under that probe convention as well.

**Scope of the negative result.** For each fixed L>=4 there is a finite
gauge bound for which the proposed limit clause fails, in either reference
convention. Consequently the intended assertion on one fixed box for
every finite M cannot hold. In axial coordinates M=2 already works at
every size. If the statement is instead changed to "for each fixed M in
Fock coordinates, choose L(M) so large that L(M) greatly exceeds M", this
particular construction does not rule out that new quantifier. The source
does not state or prove such a restriction, and its application allows
M to grow with the far distance. This distinction must not be suppressed.

The limit here is the ordinary limit of orthogonal projections and the
displayed continuous linear map m. A projectively rescaled first variation
of m would be a new object requiring its own error estimates; no claim
against such a replacement is made.
