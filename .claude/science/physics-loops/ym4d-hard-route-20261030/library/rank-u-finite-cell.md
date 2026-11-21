# Finite-cell formulation and an axial-gauge case of (RANK-U)

Source pin: `892504e4c63f195fbd791a1db913f67b4b749459`.
Author: openai/gpt-6-astra/max, mac-mini-codex. All proofs below are elementary
derivations in the stated lattice model; no hard-core or literature lemma is
used. Subsequent result: `rank-u-staggered-limit.md` disproves the arbitrary-
gauge uniform inequalities in sections 1--2. The finite-dimensional
equivalences and the restricted axial-family theorem below remain valid.

## 1. Exact matrices, including limits of kernels

Let R={0,...,L-1}^4 with positive links whose two endpoints lie in R.
Let E be its real link space with counting inner product, B=d_0 the incidence
gradient, and Z=ker B^T. Extend currents by zero outside R. Let e_k be the
six axial linear potentials `e_(mu,nu)(x,r)=x_mu 1_(r=nu)`, mu<nu.
They have unit constant curl in their named planes. Centering the coordinates
only adds harmonic constants and does not change any dipole of a conserved
current. Set e_F=sum_k F_k e_k and A=e_F+Bt.

**Discharged (definitions and duality).** Define

    (R_A J)_x = (1/2) sum_(l incident to x) A_l J_l,
    (Delta J)_k = <J,e_k>.

The incidence in R_A is unsigned; the signs of J and A are those of the
fixed positive link orientations. In particular `R_A^T lambda = lambdabar A`.
Let U have columns spanning the evaluations on R of all polynomial link
fields of degree <=3 satisfying `H u=0` on the infinite lattice, H=d^T d.
The infinite-lattice operator is meant here, not an open-box boundary
condition. Choose particular degree <=3 polynomials P_k(F) with
`H P_k(F)=VV(delta_l,e_k,e_F)` as in the target, when these exist, and set

    C_0(F,t) = [B^T; R_A],          C(F,t) = [B^T; R_A; U^T],
    (T(F,t) J)_k = <J,P_k(F)-tbar e_k>.

Then N=ker C_0, NN=ker C, dip=Delta|N and m=T|NN, exactly. For instance
T|NN=0 if and only if, for every k, there are lambda_k, chi_k and a harmonic
polynomial u_k such that on every link of R

    P_k(F)-tbar e_k = B chi_k + lambdabar_k A + u_k.              (U1)

Proof: `(ker C)^perp=im C^T`. This equality follows directly by taking
orthogonal complements of `im C^T`: its orthogonal complement is ker C.
In finite dimensions taking the orthogonal complement twice returns the
original subspace. The block rows of C give (U1). []

**Implication (finite-dimensional reformulation).** Fix L,M and a choice of
the P_k(F) linear in F. This linear choice is available if all the requisite
polynomial equations are solvable: choose a solution for each basis pair
and extend linearly. It is not a proof of their solvability for a new action.
Normalize |F|=1 and t(x_*)=0. The parameter set

    K_(L,M) = { (F,t): |F|=1, t(x_*)=0, ||Bt||_infinity<=M }

is compact. Indeed every t(x) is bounded by M times the length of a path
from x_* to x, at most 4(L-1); all defining constraints are closed.
Let Gamma_(L,M) be the closure of

    { (F,t,Pi_NN(F,t),Pi_N(F,t)) : (F,t) in K_(L,M) }

in the product with two spaces of orthogonal projection matrices. Gamma is
compact: projections satisfy Pi=Pi^T=Pi^2 and ||Pi||<=1, a closed bounded
condition in finite dimensions. Write S,P for its two projections. At every
point of Gamma, `CS=0`, `C_0 P=0` and `PS=S`, by continuity.

For this fixed L,M, the *limit-subspace* nonvanishing clauses in (RANK-U)
are equivalent to the two strictly positive minima

    alpha_(L,M) = min_Gamma ||T(F,t) S||_op > 0,
    beta_(L,M)  = min_Gamma ||Delta P||_op > 0.                  (U2)

Proof: these norms are continuous on the compact Gamma. A positive
continuous function has positive minimum: otherwise a sequence tending to
zero has a convergent subsequence and a zero at its limit. Conversely a
positive minimum implies nonvanishing on every limit. []

For fixed F the same proof applies with the unit sphere replaced by {F}.
The source must choose whether its box size is uniform over F. Equations
(U2) do not assert existence of any L for arbitrary M.

**Discharged (why the word "limit" matters).** For 0<=s<=1 let
`C(s)=[s,0]` and `T(s)=[1,s]`. The restriction of T(s) to ker C(s) is nonzero
for every s, including s=0. Nevertheless ker C(s)=span(e2) for s>0 and
T(0)e2=0. Pointwise nonvanishing on the enlarged kernel at s=0 does not
establish (U2). The source's limit clause correctly asks for more.

## 2. The additional coupling inequality

Use Qhat and the ten directions D_10 proved in `rank-u-dipole-kernel.md`.
The local inequality needed for the proposed scalar-kernel argument is

    gamma_(L,M) := min_(F,t,S,P in Gamma)
       max_(n in D_10) || S T(F,t)^T Qhat(n) Delta P ||_op > 0.  (U3)

**Discharged counterexample elsewhere in this packet.** The first minimum
in (U2), and the minimum in (U3), are zero for F=e01, M=2, every L>=4;
see `rank-u-staggered-limit.md`. The second minimum in (U2) alone remains
open for arbitrary t. Equation (U3)
is the exact compatibility strengthening: it asks for unit J in im S and
unit K in im P with a nonzero dipole coupling in some direction, uniformly
over limits. Separate positive factors in (U2) do not imply it. The
annihilator calculation in the companion lemma proves this logical point.
That annihilator argument alone does not show failure for the constrained
images; the staggered construction supplies a different, actual failure
of their uniform moment bound.

**Discharged (normalizing moments at fixed size).** If w_q(J) is any fixed
norm consisting of ||J||_2 plus finitely many absolute polynomial moments
of degrees <=q, then

    ||J||_2 <= w_q(J) <= C(L,q) ||J||_2.

Each moment is a fixed linear functional on the finite link space, bounded
by Cauchy--Schwarz; summing proves the estimate. Thus at fixed L,M strict
positivity in (U2)/(U3) remains strict under this normalization. No estimate
in M follows from this observation.

## 3. An explicit class where the local test survives

**Discharged (axial family, including all its limits).** Let L>=4,

    F=e01,     e_F=x0 e1,     t(x)=C x1,     A=(x0+C)e1,          (U4)

with any real C. There are fixed currents J in NN(t) and K in N(t),
independent of C, for which

    m_J = 2 e12,       dip(K)=e02,
    <m_J,Qhat((e0+e1)/sqrt(2)) dip(K)> = -2.                   (U5)

In particular nonzero m, nonzero dip, and their compatibility all persist
along every bounded sequence of these gauges. This is a special case, not
a reduction of arbitrary t to (U4).

Proof. Let y be the positively oriented 02 plaquette current based at
(1,1,1,1). Set K=y and J=H y using the infinite-lattice H, with zero
extension. The support of H y is within one lattice step of that plaquette,
so it fits in R for L>=4. Both y and H y are conserved. On a conserved
current H equals the componentwise positive scalar lattice Laplacian:
expanding d^T d gives

    (H y)_a(x) = sum_b [2 y_a(x)-y_a(x+e_b)-y_a(x-e_b)]
                    - (B B^T y)_a(x),

and B^T y=0. Hence J and K have only components 0 and 2. Since A has only
component 1, R_A J=R_A K=0 identically for every C. For every harmonic
polynomial u, finite summation by parts gives
`<J,u>=<H y,u>=<y,H u>=0`. Thus J is in NN(t) and K is in N(t).

Here is the polynomial calculation defining m, including its normalization.
For a mu,nu plaquette use

    phi(a)=a_mu(x)+a_nu(x+e_mu)-a_mu(x+e_nu)-a_nu(x),
    m(a)=(a_mu(x)+a_mu(x+e_nu))/2,
    n(a)=(a_nu(x)+a_nu(x+e_mu))/2,
    VV(a,b,c)=sum_p (phi wedge m wedge n)(a,b,c).

With the axial e_k above and e_F=x0 e1 the link currents
`J2_k(l)=VV(delta_l,e_k,e_F)` are zero except

    J2_12=2 x0 e2,             J2_13=2 x0 e3.                  (U6)

To check (U6) directly, for k=12 only 12 plaquettes contribute to the
first variation. Their `m(e_k)n(e_F)-n(e_k)m(e_F)` equals
`-(x1+1/2)x0`. Its curl transpose contributes x0 to a 2-link; the variation
of n contributes another x0 because phi(e_k)=1 and m(e_F)=x0. All 1-link
contributions cancel as a difference in x2. The same calculation with 2
replaced by 3 proves the 13 case. For k=01 the two fields are equal. For
k=02 or 03 the mixed product has no dependence in the two directions of
its plaquette, and neither nonzero flux plane contains the other field's
component. For k=23 the only mixed product is on 13 plaquettes, proportional
to x0 x2, whose differences in directions 1 and 3 vanish; the flux terms
also vanish. These observations exhaust the six planes.

Thus valid particular solutions are
`P_12=-(x0^3/3)e2`, `P_13=-(x0^3/3)e3`, with the other P_k=0.
Indeed the centered second difference of x0^3 is 6x0, and these two fields
are divergence free. Pairing H y against these P_k and tbar e_k is exact
finite summation by parts. For k=12,

    H(P_12-tbar e_12) = H[-(x0^3/3)e2-C x1^2 e2]
                      =2(x0+C)e2,

whose circulation on y is 2. The 13 case has only component 3 and gives
zero on y. For k=02,03,23 the product tbar e_k is harmonic (a mixed
quadratic independent of its own link direction). For k=01 it has only
component 1, so its pairing with J is zero. Therefore m_J=2e12.
The dipole of the unit 02 plaquette is e02 directly from the definition
of Delta. The reflection with normal (e0+e1)/sqrt(2) sends e0 to -e1 and
fixes e2, so Qhat e02=-e12. This proves (U5). []

**Discharged (a crude quantitative bound for this class).** ||K||_2=2 and
||J||_2<=||J||_1<=16||y||_1=64, since the scalar four-dimensional lattice
Laplacian has absolute coefficient sum 16. The normalized row norm is
therefore at least 1/32 and the normalized coupling in (U5) at least 1/64,
uniformly in C. These constants are not bounds for arbitrary gauges.

**Discharged (a warning about dipole rank).** If C>0 in the uncentered box
coordinates, N(t) for (U4) has dipole image exactly
`span(e02,e03,e23)`, of dimension 3. At the boundary x1=0, R_A J=0 forces
the outgoing J1 to be zero because x0+C!=0. Inducting in x1 forces every
J1 to vanish. The remaining conservation equation permits independent
closed currents in each 0,2,3 slice. Their dipoles have no 1 index:
`d_a1=0`, and conservation gives `d_1a=-d_a1=0`. Plaquettes in each of
the three remaining planes attain the three basis dipoles. Thus a proposed
universal repair requiring rank(dip)>=4 would be false. This three-space
is not a duality space and (U5) shows that compatibility can still hold.
