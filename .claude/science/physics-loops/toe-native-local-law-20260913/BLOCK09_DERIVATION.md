# Local Grassmann interactions and the common metric

Author derivation in progress; no independent review. This extends a
supplied classical geometric construction to formal Grassmann-valued local
functionals. It is not an operator-ordered quantum constraint theorem or an
interacting quantum continuum proof.

## Deriving the interaction condition from a graded bracket

Use odd spinor fields q, qbar on a smooth slice, with an even canonical
Poisson bracket satisfying {q_a(x),qbar_b(y)}=-i delta_ab delta(x-y).
The bracket between two odd coordinates is symmetric. Right/left derivatives
give, for even F,G,

    {F,G}=-i sum_a [ (F <-d/dq_a)(d/dqbar_a ->G)
                       +(F <-d/dqbar_a)(d/dq_a ->G) ].

For bilinears this gives {qbar A q,qbar B q}=-i qbar[A,B]q. Thus the
bilinear matter and configuration-connection calculations of the free
classical construction carry to this graded setting with the same signs.
The metric variables are even. The Darboux momentum shift and its curvature
follow from the same bilinear identity, now in the formal Grassmann algebra.

Use ordinary spinors q=g^-1/4 psi when expressing a potential, and let U
be a real, even, derivative-free local polynomial in their components.
It has no explicit spacetime-coordinate dependence and is invariant under
the local spatial spin rotation. Define V[N]=int N sqrt(g) U(q,qbar).
The metric derivative of V is ultralocal in N. Hence its mixed bracket with
the gravitational kinetic term cancels after N,M antisymmetrization. Its
self bracket has no derivatives of delta and likewise cancels. The new
normal bracket comes from the kinetic spinor term and V.

At a background normal frame, the lapse-gradient part of the kinetic flow is

    {q,H_m[N]}=...- (partial_i N) alpha_i q/2,
    {qbar,H_m[N]}=...- (partial_i N) qbar alpha_i/2.

All remaining terms are proportional to N and cancel in the cross bracket.
Let B_i be the EVEN derivation defined by

    B_i q=alpha_i q/2, B_i qbar=qbar alpha_i/2.

It acts on a product with the ordinary Leibniz rule, since the transformation
itself is even even though its arguments anticommute. Then

    {H_m[N],V[M]}+{V[N],H_m[M]}
       =-int sqrt(g) (N partial_i M-M partial_i N) B_i U.

The alpha_i in an orthonormal frame are the two Weyl blocks. Consequently
within the stated local-potential ansatz the old normal bracket is preserved
exactly when B_i U=0 for each boost generator. Necessity can be checked
coefficientwise in the exterior algebra: vanishing against all N,M first
gives div B=0 with N=1, then arbitrary N gives B.grad N=0 and hence B=0.
Spatial covariance was separately assumed. Together, rotations and boosts
are precisely the infinitesimal proper Lorentz invariance condition on U.
This is a local polynomial criterion; it supplies no quantum renormalization
or existence theorem for the interacting model.

## Why the commuting-spinor shortcut is unsafe

In a single two-component Grassmann species R=(r0,r1), the quartic
Rbar0 Rbar1 r0 r1 spans its degree-four top exterior power. A determinant-one
Weyl boost or spin rotation preserves the two annihilator and two conjugate
volume factors. Thus its density square is Lorentz invariant after normal
ordering. Directly, n_R j_R^i=0 for each i in this Grassmann algebra.
For commuting components, n_R j_R^i is generally nonzero. Applying that
commuting counterexample to the physical two-component fermion would give
a false interaction obstruction. The finite CAR normal-ordering constant
must also be separated from the quartic symbol.

## Candidate invariant space for one Weyl pair

Use the cone spin basis R=q_+, L=sigma3 q_-. Their free symbols are
+sigma.p and -sigma.p, while spatial rotations act by the same SU(2)
matrix. Boosts act as +sigma_i/2 on R and -sigma_i/2 on L, and by the
Hermitian conjugates on their barred components. Define n_R=Rbar R,
j_R=Rbar sigma R and similarly for L (j_L is written with +sigma; its
physical left-Weyl current has the opposite sign).

A U(1)-charge-preserving quartic has two annihilators and two conjugates.
The annihilator-pair representation decomposes as

    wedge^2 (R plus L) = scalar plus vector plus scalar.

Pairing with the conjugate representation suggests five complex invariant
basis polynomials: rbar r, lbar l, rbar l, lbar r and

    U_cross=n_R n_L+j_R.j_L,
    r=r0 r1, l=l0 l1.

The bar on a pair reverses order under conjugation; explicit component
calculations below must preserve that sign. Four Hermitian scalar-pair
combinations and U_cross give five real Hermitian couplings. If separate
valley number is required, the two pair-transfer combinations are excluded,
leaving three. This representation argument and its exact component basis
are to be checked independently by the exterior-algebra generator kernel.

## Specific native on-site interaction and the node phases

For a concrete interaction use c_n0^dagger c_n1^dagger c_n1 c_n0 in the
specified two-orbital Wilson carrier. At lattice spacing a and fixed v,
normalized cone fields have the leading expansion

    c_n = a^(3/2)/sqrt(v)
                [ exp(i kappa n3) R(y)+exp(-i kappa n3) sigma3 L(y) ],
    y=D^-1 a n, kappa=acos zeta.

This normalization preserves sum_n c^dagger c -> int dy (Rbar R+Lbar L)
after suppressing nonresonant phases. In the range zeta in [1/2,1),
4 kappa is never a reciprocal-lattice multiple, so pair transfer oscillates.
The zero-phase quartic is a sum of same-valley pair terms and the cross
pair term associated with

    m=r1 l0+r0 l1.

Unlike a scalar pair, m is a specified spatial triplet component. Its
conjugate product is expected to have nonzero spin-rotation and boost
variations. The exact zero-phase expansion and those variations must be
computed, not assumed from a density label. This is a proposed explicit
finite-cutoff discriminator, not an axiom-wide obstruction.

## A finite native construction to test the invariant alternatives

Finite Laurent filters f_+(k)=(1+sin k3/v)/2 and
f_-(k)=(1-sin k3/v)/2 take values 1,0 at the respective nodes. Define
filtered native fields R_n=f_+ c_n and L_n=sigma3 f_- c_n. They are finite
range, but are not exact separate canonical species at general momentum.
Only even, normal-ordered quartic combinations are proposed as physical
operators. The three valley-number-preserving invariant polynomials above
can be formed from these finite combinations, with explicit Hermitian
symmetrization when their finite-cutoff contractions require it.

Their leading node quartics match the intended invariant polynomials;
wrong-node leakage is derivative-suppressed. This construction would show
that the specified on-site mismatch can be changed within finite native
couplings, without changing the carrier or adding an axiom. The exact CAR
normal-ordering and path support remain checks to do.

## Scaling is a separate obligation

If the physical Hamiltonian is (h_0+lambda W)/a and c_n scales as above,
a derivative-free quartic contributes lambda a^2/v times its continuum
polynomial. A fixed small dimensionless lambda therefore has a vanishing
engineering coefficient; a nonzero finite continuum g would require
lambda=v g/a^2. That leaves a fixed small-coupling hypothesis as a->0.
Engineering scaling by itself is not a proof that interactions cannot
renormalize relevant terms or that a particular strong-coupling limit exists.
The known native small-coupling theorem must be checked on its own stated
counterterm and observable domain before use.

Primary source read so far: Dreiner–Haber–Martin arXiv:0812.1594v6,
section 2 passages spanning equations 2.52–2.75 and in particular the
commuting/anticommuting distinction and Fierz equations 2.59–2.70. The
313-page review has NOT been read in full. The component and generator
calculations planned here will not import an invariant coefficient from it.

## Exact component result and a dimension proof

The exterior calculation passed 76 initial checks. It found a five-dimensional
invariant subspace inside the 36-dimensional complex charge-preserving quartic
space, versus ten dimensions for rotations alone and three when separate valley
number is imposed. The listed five polynomials are independent and invariant;
the calculation also agrees with direct finite-CAR phase averages.

The dimension has an analytical proof rather than depending on the matrix
rank output. Complexify the proper Lorentz Lie algebra into the two commuting
sl(2) factors. R and L are their two fundamental representations, with an
inverse/conjugate representation identified by the invariant epsilon tensor.
Their same-species antisymmetric pairs r and l are scalars. The four mixed
components R_a L_b carry the tensor-product vector representation. It is
irreducible: the two sl(2) actions generate M2 tensor I and I tensor M2,
and their products span M4. A commuting endomorphism of that space is
therefore scalar, while no invariant vector lies in it. The two scalar
copies have four independent pairings with the two conjugate scalar copies;
the vector sector has one. This proves 4+1 dimensions. The explicit five
polynomials exhibit all of them. Hermitian conjugation fixes a five-real-
parameter family; separate valley phase invariance removes rbar l and its
conjugate, leaving the three stated real polynomials.

With monomial order Rbar0,Rbar1,Lbar0,Lbar1,r0,r1,l0,l1, the cross invariant is

    U_cross=-2 [Rbar0 Lbar0 r0 l0+Rbar1 Lbar1 r1 l1
                       +Rbar0 Lbar1 r1 l0+Rbar1 Lbar0 r0 l1].

It also equals -2 (Rbar L)(Lbar R), with precisely this Grassmann order.
The same-species relations are n_R^2=2 rbar r and
j_R.j_R=-3 n_R^2. These identities explain why a commuting null-current
formula is not the correct quartic reduction for a Grassmann field.

For the native zero-phase polynomial U_site=rbar r+lbar l+mbar m, the
third boost gives the explicit nonzero polynomial

    B_3 U_site=-2 Rbar0 Lbar1 r0 l1
                          +2 Rbar1 Lbar0 r1 l0.

The first two boosts give zero, the first two rotations give nonzero
polynomials, and the third rotation gives zero. This anisotropy is tied to
the actual relative sigma3 basis between the two native cones. It would be
missed by replacing the two orbital densities with two independently rotated
continuum species before carrying out the node expansion.

## Finite filtered operators and their honest domain

At v=.8, the finite filters satisfy

    {R_n0,L_n0^dagger}=(1/4-1/(8v^2)) I,

which is nonzero. Thus the construction does not claim exact microscopic
separate CAR species. Evaluate each degree-four invariant as a normal-ordered
polynomial in the filtered fields, with every creation factor to the left
of every annihilation factor. The three valley-preserving invariant operators
are Hermitian and commute with total fermion parity on the actual six-mode
CAR space at the neighboring z cells. This is a direct 64-dimensional
operator check, distinct from the exterior-algebra calculation.

For each microscopic monomial the exact identity

    c_i^dagger c_j^dagger c_k c_l
      =delta_jk c_i^dagger c_l
                           -(c_i^dagger c_k)(c_j^dagger c_l)

expresses it through even bilinears. All endpoints lie in three adjacent
z cells and two orbitals, so their x/z protected paths have length at most
three. The native even-path dictionary therefore encodes the full quartic
on bounded support. Normal ordering is essential: replacing this polynomial
with an un-normal-ordered product can add finite-cutoff bilinear terms.
Those terms have not been silently folded into the invariant quartic.

At a specified node, the finite filters have exact desired values. Their
wrong-node factors are O(a) on fixed smooth wave packets. The leading
four-leg vertex of these normal-ordered operators is therefore the intended
continuum invariant, with derivative-suppressed corrections. A proof of
renormalized interacting fields or the quantum constraint algebra does not
follow from this tree-level statement.

## A simpler covariant interaction inside the density-potential class

The finite-filter construction is not the only escape. The general real
symmetric orbital-density interaction can be classified at its two relevant
momentum transfers. Write its Fourier kernel at zero and at Q=2 kappa e3 as

    V(0)=[[a0,b0],[b0,c0]], V(Q)=[[aQ,bQ],[bQ,cQ]],
    W=(1/2) sum_(n,m,r,s) V_rs(n-m) :n_nr n_ms:.

The node density components are
rho_r,0=Rbar_r R_r+Lbar_r L_r and
rho_r,+Q=s_r Rbar_r L_r, s=(1,-1), with the conjugate at -Q.
Phase averaging gives

    U_V=(1/2) sum_rs V_rs(0) rho_r,0 rho_s,0
                      +sum_rs V_rs(Q) rho_r,+Q rho_s,-Q.

Expanding in the fixed exterior monomial order, its coefficients are
(aQ-a0) on Rbar0 Lbar0 r0 l0, (cQ-c0) on Rbar1 Lbar1 r1 l1,
-bQ on each mixed exchange monomial, and -b0 on each same-valley pair
monomial and each opposite-spin diagonal mixed-pair monomial. Comparing
with the five invariant basis polynomials proves, without a numerical fit,

    b0=0, a0=aQ+bQ, c0=cQ+bQ,
    U_V=(bQ/2) U_cross.

The three-dimensional kernel in the six Fourier values has a one-dimensional
nonzero quartic image; its two other directions have zero local quartic
symbol. The exterior-generator calculation gives exactly those equations.
An orbital-blind kernel has a0=b0=c0 and aQ=bQ=cQ. Its invariant local
quartic occurs only at V(0)=V(Q)=0. This is a classification of that explicit
six-parameter leading vertex, not a claim that every orbital-blind
interacting lattice model lacks an acceptable infrared limit.

A useful concrete choice needs no valley filters. Let rho3_n=n_n0-n_n1 and
choose the real even finite-range potential

    u(+e3)=u(-e3)=t/2,
    u(+2e3)=u(-2e3)=-t/2,
    u(0)=0, all other values zero,
    uhat(q)=t(cos q3-cos 2q3).

Set V_rs=s_r s_s u. Then V(0)=0 and V(Q)=uhat(Q) [[1,-1],[-1,1]],
so the leading interaction is

    U_V=-uhat(Q) U_cross/2,
    uhat(Q)=2t sin(3 kappa) sin(kappa).

For zeta in (1/2,1), kappa in (0,pi/3), this coefficient is nonzero when
t is nonzero. The endpoint zeta=1/2 is excluded for this particular stencil;
it makes uhat(Q)=0. The source-selection freedom is explicit: t, the stencil
and the orbital-density-difference channel are chosen inputs.

The full microscopic interaction is simply

    W=(t/2) sum_n [rho3_n rho3_(n+e3)-rho3_n rho3_(n+2e3)].

It has bounded native support, is Hermitian, translation invariant and
invariant under all coordinate reflections and orbital exchange. Since it
couples distinct cells and u(0)=0, its vacuum normal ordering creates no
onsite CAR contraction. The subtractions by 1/2 in the two orbital densities
cancel in rho3 itself. Thus the full centered density interaction has the
same explicit quartic operator, not an unreported chemical-potential term.
The four-leg continuum coefficient is

    g_cross=-lambda a^2 uhat(Q)/(2v)

when the physical Hamiltonian is (H0+lambda W-nu N_staggered)/a.

This interaction lies in the density-potential form of Giuliani–Mastropietro–
Porta 1907.00682v3, equation 2.19: w_rs=s_r s_s u/2. Section 2.3 was reread
for this match. The potential is real, even, finite range, periodicizable,
independent of volume, and has the required reflection symmetries. Its
orbital-exchange symmetry is also explicit. The unchanged Wilson kinetic
symbol meets the previously reconstructed two-node hypotheses. For each
fixed such potential and fixed zeta, the theorem's EXISTENTIAL small-coupling
bound and analytic staggered counterterm therefore apply to its stated
Weyl two-point/current results. Their values are not computed here.

That import does not prove the gravitational constraint algebra for the
interacting quantum model or preserve the tree-level quartic ratios under
renormalization. It also does not apply to lambda proportional to a^-2 on
an indefinitely fine lattice. The construction supplies a nonzero Lorentz-
invariant leading interaction within the same rigorously studied weak-
coupling model class, while leaving the finite-interaction continuum and
native quantum geometry problems open.

## Smooth-source vertex limit and an even-parity two-particle check

Take smooth compactly supported envelopes (or compatible periodic ones),
and a fixed zeta away from node merger. Insert the two-node expansion into
the finite normal-ordered quartic. The zero-phase terms give the polynomial
above. For the others, discrete summation by parts uses
exp(i m kappa)-1, m=2 or 4, which is nonzero in the stated parameter range.
Repeated differences of a fixed smooth envelope give arbitrary powers of a;
these oscillatory terms therefore disappear. The finite stencil shifts the
remaining envelopes by a D^-1 ell. Taylor expansion and a Riemann-sum bound
then give the leading four-leg matrix element with an O(a) remainder when
lambda a^2 is bounded. The estimate is on fixed smooth few-particle test
states, not on the norm of the many-body interaction or its ground state.

On a curved supplied metric, multiply a bond interaction by the endpoint
average of f=N/sqrt(det g_cone). Since q=g^-1/4 psi, the continuum local
potential is N sqrt(g) U(q)=N U(psi)/sqrt(g). The same finite-stencil proof
matches this source. Its coefficient and classical geometry are supplied;
this does not establish a microscopic geometric transformation law.

For a direct even-parity check, choose kappa=pi/4, v=1/sqrt(2), and a
periodic cube with L=16,32,64, a=2pi/L. Two normalized one-particle waves
have native spinors u and sigma3 vspin and z momenta kappa+a and -kappa+2a.
Their momenta are different allowed grid points, so the two-particle Slater
state is normalized even when the internal spinors overlap. For a nonzero
separation ell, direct evaluation gives

    <rho3_n rho3_(n+ell e3)>
      =2/L^6 [(u^dagger sigma3 u)(vspin^dagger sigma3 vspin)
                     -|u^dagger vspin|^2 cos((2 kappa-a) ell)].

The first term cancels between ell=1 and ell=2 in W. Thus, at t=1,

    <W>=-|u^dagger vspin|^2
                [cos(2 kappa-a)-cos(4 kappa-2a)]/L^3.

Multiplying by lambda/a with the diagnostic scaling lambda=v/a^2 gives

    <lambda W/a> -> -v |u^dagger vspin|^2/(2pi)^3.

This equals the continuum matrix element of -U_cross/2 with the derived
field normalization. The primary evaluates the antisymmetrized position-
space amplitudes directly for three choices of spinors; it does not insert
this expected cosine expression into that calculation. It also checks
normalization and overlaps. The actual and analytical finite values agree
to roundoff, and the predeclared O(a) errors pass. The coarse errors are not
assumed to decrease monotonically. The displayed diagnostic scaling does
not enter the imported small-coupling theorem and does not establish a
strong-interaction continuum limit.

A more explicit version of the graded sign calculation uses one spatial
direction: H_N=-i/2 int N(qbar alpha q'-qbar' alpha q). Its left Euler
derivatives give {q,H_N}=-(N alpha q'+N' alpha q/2) and
{qbar,H_N}=-(N qbar' alpha+N' qbar alpha/2). Applying this even flow to U
then yields the normal-bracket difference stated at the beginning, including
its minus sign. No commuting-spinor chain rule is substituted for the odd
Euler derivatives; the product transformation is even and uses the ordinary
Leibniz rule only after those derivatives have been taken.

Current check source 0d179de7c0555f42afec447df58da0d3ee23f398fc58642fe8ed7703235dcda6
ran 115 author checks in .43117995792999864 seconds. These finite checks
challenge the written representation, bracket and scaling derivations.
Independent review, loop corrections to the four-leg vertex, gravitational
quantum constraints and native metric dynamics remain open.

## Cold-review distinctions retained for any public milestone

The two-particle matrix-element test uses the empty Fock vacuum to define
an even Slater state. This is a valid finite CAR-sector test state, not the
half-filled interacting ground state of the Weyl theorem. The canonical
quartic symbol is a bare interaction coefficient. The imported theorem
instead controls a dressed ground-state two-point function after tuning
nu(lambda), with renormalized velocities and Z. Those statements concern
different objects. In particular, the bare common metric used to identify
the quartic boost generators cannot be silently equated with the dressed
metric in a claim about renormalized four-point functions. No such
four-point or gravitational Ward theorem is imported.

Current-main source comparisons read in full at this checkpoint:
INTERACTING_RP_FULL_ALGEBRA_FIXED_A_GAUGE_INVARIANT_FOUR_FERMION_BOUNDED_NOTE_2026-06-05.md
concerns a different supplied finite staggered/gauge RP construction and
explicitly leaves the Lorentz continuum limit outside its scope.
QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md
separates the local M2 algebra from a physical boost identification. Here
the Weyl action and its boosts are supplied through the specified kinetic
symbol; this note does not derive that identification from the local algebra.
No effective audit status or universal no-go is inherited from either source.
