# Exact finite-clock electric/magnetic representation on a contractible complex

Personal active derivation,2026-09-15. This is a finite-volume identity for
the actual supplied Villain law. It is not a fixed-order phase theorem.
The purpose is to match the next effective-field construction to the law
without discarding electric or magnetic defects or their phase coupling.

## 1. Tree gauge and primitive integer curls

Let the finite connected cell complex have E edges,V vertices,P plaquettes.
Assume its integer first and second cohomology vanish, as for a contractible
cubical box. Choose a spanning tree and set its link angles to zero by a
vertex gauge transformation. The remaining r=E-V+1 angles are theta in
(R/2pi Z)^r or in(2pi/N)Z_N^r. The normalized tree gauge quotient is exact
for gauge-invariant observables: every gauge orbit has the same finite
clock size, and the continuous change of variables is an integer torus
automorphism with Haar Jacobian one. The unfixed global vertex gauge
transformation contributes the same constant to every orbit.

Let D be the P by r plaquette-edge incidence matrix after tree columns are
removed. It has full real column rank. Integer H^1=0 implies its columns
are an integer basis of all integer exact plaquette cochains. Integer H^2=0
implies

 K=D Z^r=ker(d_2:Z^P ->Z^(3-cells)),

so K is primitive in Z^P. Put Q=D^T D>0,
P_e=D Q^-1 D^T and P_perp=I-P_e. Every coset[k] in Z^P/K may be represented
by an integer plaquette cochain k. The projected quotient P_perp Z^P is a
full lattice in the complementary real space; it is discrete because P_perp
has rational entries. Its kernel on Z^P is exactly K.

The magnetic charge is m=d_2 k. It is invariant on the coset, obeys d_3m=0,
and identifies the coset under the cohomology assumption. Its squared
Coulomb energy is

 ||P_perp k||^2=<m,(d_2 d_2^T)^+m>,

because P_perp is the real image of d_2^T. Boundary conditions are the
actual finite-cell ones in these matrices; there is no substitution by a
componentwise Dirichlet Green kernel.

## 2. The actual partition function and all integer characters

For integer j in Z^r let

 Z_N(j)=N^-r sum_{theta in(2pi/N)Z_N^r}
      exp[i<j,theta>] prod_p phi_beta((Dtheta)_p),
 phi_beta(u)=sum_{k in Z}exp[-beta(u-2pi k)^2/2].

The normalized observable is Z_N(j)/Z_N(0). Tree-gauge integer characters
correspond to conserved integer edge currents before gauge fixing. In
particular a plaquette Wilson loop has j=D^T e_p.

For any smooth periodic function F(theta), clock sampling equals the sum
of its Fourier coefficients at N Z^r. Applying it with the character gives

 Z_N(j)=sum_{a in Z^r} Z_U(1)(j+Na),

where Z_U(1)(l) is the Haar integral with integer character l. Its Fourier
series converges absolutely for the positive smooth Villain product.
For a fixed coset[k], unfold k+D n into real angles theta-2pi n.
The integer source changes by an integer multiple of2pi and is unchanged.
Completing the square with

 theta=v+2pi Q^-1 D^T k

then gives the exact identity

 Z_N(j)=C_beta sum_{a in Z^r}sum_{[k] in Z^P/K}
  exp[-(1/(2beta))<j+Na,Q^-1(j+Na)>]
  *exp[-2pi^2 beta||P_perp k||^2]
  *exp[2pi i<j+Na,Q^-1D^T k>],                        (1)

 C_beta=(2pi beta)^(-r/2)(det Q)^(-1/2).

The phase is independent of representative: k->k+D n changes its exponent
by2pi i<j+Na,n>, an integer multiple of2pi i. The electric a variables and
magnetic cosets are both retained. The double series is absolutely
convergent because its absolute value factors into two finite-rank Gaussian
lattice sums. This also justifies the final Fourier/unfolding rearrangement
by finite cutoffs and dominated convergence after Gaussian integration.

If an integer matrix R completes[D R] to a unimodular P by P matrix, write
k=R b with b in Z^(P-r). Then(1) is an ordinary pair of integer Gaussian
sums with matrices

 Q_e=Q^-1, Q_m=R^T P_perp R>0, M=Q^-1D^T R,
 phase=exp[2pi i(j+Na)^T M b].                         (2)

Such a completion exists because K is primitive. A particular coordinate
choice need not be spatially local. Gauge/tree choices and completions
must not be mistaken for changes to the physical measure.

## 3. Checks that prevent dropping a defect species or its phase

Setting a=0 gives the continuous U(1) numerator; it is not the finite-clock
law. Setting[k]=0 gives a pure exact-curl/zero-magnetic sector; at fixed
coupling it is not the full law either. The two omissions have different
origins and neither is authorized by the exact identity.

The summands in(1) are not generally nonnegative. On a single four-cube,
r=32-16+1=17,P=24. Symmetry gives(P_e)_pp=17/24 for every plaquette p.
Take j=0,a=D^T e_p and k=3e_p with N=3. The phase is

 exp[2pi i *9*(17/24)]=exp[2pi i*51/8],

whose real part is -1/sqrt(2). The associated energies are
<a,Q^-1a>=17/24 and||P_perp k||^2=9*(7/24).
The magnetic charge d_2(3e_p) is nonzero and satisfies d_3d_2(3e_p)=0.
Both configurations and the negative real weight are exact finite-matrix
facts. Pairing the charge-reversed conjugate term leaves a negative real
pair contribution. Thus a proof treating the two unintegrated gases as an
independent positive product has changed the representation.

This is not a sign obstruction to every positive representation. For each
fixed l=j+Na, the magnetic coset sum is a centered Gaussian lattice
characteristic function in the b coordinates of(2), hence strictly positive
by Poisson summation. Therefore summing the magnetic variables first yields
an exact positive electric marginal. Its effective interaction is the
logarithm of that magnetic characteristic function, evaluated at M^T l.
The matrix M contains the real Green operator and an integer choice of
representatives; its spatial locality is not supplied by positivity.

The block15 convex closed-charge lemma cannot simply be substituted here:
its closure/boundary kernel differs, and the source map in(2) must be
controlled. An all-source Hessian bound helps only after its metric is
shown to match the electric current metric or a controlled local carrier
norm. Dirac-string/representative invariance does not itself prove such a
norm estimate.

## 4. Finite test design

A single three-cube has r=5,P=6 and one magnetic coordinate. Tree-gauge
clock enumeration requires N^5 states. A primitive row minor of D gives a
unimodular completion by one coordinate plaquette. Compare the direct
clock partition function and plaquette characters with the two Gaussian
sums, including the phase and C_beta. Root-of-unity phase classes make
this finite comparison cheap without changing the identity.

For the single four-cube, calculate Q^-1,P_e,P_perp with exact rational
arithmetic, check all incidence identities, rank, primitivity and the
negative N=3 mixed-phase witness. A complete N^17 clock enumeration is
unnecessary for that exact witness and is not claimed.

Finite cutoffs in the Gaussian sums are finite challenges, not executions
of the infinite series. For the centered electric sum, a useful normalized
tail check follows from the centered lattice-Gaussian MGF bound:

 Pr(max_i|a_i|>A)<=2 sum_i exp[-N^2(A+1)^2/(2beta Q_ii)].

The one-dimensional centered magnetic coordinate of the three-cube has
Pr(|b|>B)<=2 exp[-2pi^2 beta Q_m(B+1)^2]. Absolute double-sum tails may be
bounded by the product of the two positive Gaussian partition sums times
the sum of these two tail probabilities. Nonzero source characters require
a shifted-tail argument or a separately reported cutoff comparison.

## 5. What remains

The identity identifies the actual coupled defect problem. A successful
fixed-order proof must control its positive marginalized interaction or
retain the mutual phase in a convergent construction. It must then prove
the physical-score covariance and higher connected correlation limit, or
an equivalent photon observable theorem. The two-species representation
and its negative individual terms do not refute a Coulomb phase and do not
force an axiom change. They make the next proof obligation concrete.
