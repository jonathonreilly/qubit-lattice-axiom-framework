# The actual two-pair periodic Schur operator converges to the full threshold form

Author discovery, September30,2026. **Conditional-support**, not formal
review, audit or retained status. The old packets remain frozen. This new
proof requires a focused independent check before substantial reuse.

For fixed supplied mu,tau>0, fixed guard radius R>=14, and odd torus side
lengths L tending to infinity, let S_(2,L) be the actual physical N=4
periodic-cell Schur operator constructed in the checked compatible-cell
packet. It acts on all Sym^2 C^5, with its declared polar-frame convention.
Let V=L^3 and let T0 be the already checked full15-channel compact-response
threshold form of the same infinite-lattice Hamiltonian. The result is

             || V S_(2,L)-T0 || ->0.                         (1)

This establishes a fixed two-pair finite-volume normalization and limit.
It does not establish the many-pair expansion uniformly through n<=K, or
replace the physical boundaries of a large system by periodic cell seams.
No leading EOS, finite-density phase or positive-energy scattering matrix
is obtained. No convergence rate is claimed in(1).

A consequence for the ACTUAL N=4 torus spectrum is

 V lambda_j(H_(4,L))->lambda_j(T0), j=1,...,15,
 V lambda_16(H_(4,L))->infinity,                           (2)

with eigenvalues in increasing order and multiplicity. The lowest fifteen
levels lie in total momentum zero for sufficiently large odd L. The proof
also identifies the local limit of their constrained Schur minimizers as
the finite-energy threshold minimizers with the prescribed incoming tensor.
Those limiting profiles are not square-summable physical four-particle states.

## 1. Sources, supplied law and what is reused

CONTRACT.md was frozen before the new computation at SHA256
 d91c5835919f4e5abde5b66193e331d054652bc6b3370660e8524cf1366128a6.
PRE_DERIVATION.md preserves the complete proposed compactness mechanism
before the exact finite controls. Main and ai/execution were refreshed;
main remains30a9461ee19a49b99fa6628fe942f08e504e8903, procedures remain the
selected7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The complete actual main
native law, complete original threshold proof, and complete new independent
compatible-cell check were read. SOURCE_BINDINGS.json records exact bytes.

The latter check, SHA256
25b3f255f611108b125936d40bde7d437348fee56be02e683ae2cbbf682d8170,
confirms the prior compatible REPORT04e13444 and periodic bridgeb99af6fa
at their declared scopes. Their finite cell gap is reused, not presented
as new science here. The unconfirmed numerical/certified threshold packet
was neither read nor used. No threshold entries, fit, or comparison value
is an input to this limit.

A current-main native threshold search and current open heads9399,9398,9397,
9008 were inspected. The open supplied record/gravity/ice units supply no
premise. The closest actual input here is the checked N4 compact-response
construction, which explicitly left finite-torus zero-mode treatment open.
No exhaustive or historical priority claim is made, and no generic dilute-gas
theorem is imported. The uniform Sobolev and energy-density arguments needed
below are proved directly.

The carrier is one physical qubit per site, with b_x=|0><1|, n_x=b_x^dagger b_x
and commuting operators at different sites. The supplied graph has eighteen
differences G={+/-2e_i,+/-e_i+/-e_j}. Set m_x=sum_(d in G)n_(x+d). With

 d_i(x)=b_(x+e_i)b_(x-e_i), v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
 Q_E1=(d1-d2)/sqrt2, Q_E2=(d1+d2-2d3)/sqrt6,
 Q_Tij=(1/2)sum_(s,t)v_ij^(s,t),

use exactly the unchanged law

 H0=mu N-2mu sum PE-mu sum PT+V3+W,
 V3=mu sum_x n_x binom(m_x,2),
 W=tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2.

The checked full-carrier positive identity and gradient bound are

 H0=S+mu D+W,
 S=(2mu/3)sum|d1+d2+d3|^2
                +(mu/4)sum_planes sum_(r<s)|v_r-v_s|^2,
 D=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0,
 H0>=a Egrad9, a=min(tau,mu/12).                         (3)

Egrad9 uses the nine unique forward graph bonds B_d(x)=b_x b_(x+d),
d=2e_i or e_i+/-e_j. In each plane order(+,-), the normalized constant
soft matrix U has axial rows(1/sqrt2,1/sqrt6),(-1/sqrt2,1/sqrt6),
(0,-2/sqrt6), and that plane's own T column(-1,+1)/sqrt2. Thus U^dagger U=I5.
The single-bond S symbol at zero is2mu P_high, P_high=I9-UU^dagger.

In the N=4 sector, let Q_nm select configurations without a perfect matching
of graph edges. The actual graph classification gives D>=Q_nm, hence

 H4>=mu Q_nm, 0<=H4<=16mu+144tau.                        (4)

These statements hold on sufficiently large tori as well as in the infinite
zero-momentum orbit fiber. The connected perfect-matching core is finite
modulo translations. Outside it, a perfect-matching configuration consists
of two disconnected graph edges with a unique pairing. There it is exactly
isometric to the exchange-symmetric two-bond exterior. In that exterior the
Hamiltonian is the compression of the finite-range positive form
h2(q) tensor I+I tensor h2(-q). No isometry is used inside the core.

## 2. Incoming profiles, odd-volume orbits and every volume factor

Write A for a complex symmetric5x5 matrix with Frobenius norm. If
C_alpha^dagger is the uniform sum of the five normalized pair creators
(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2)^dagger, the physical incoming
matching amplitude is obtained from

 Phi_A^phys=(1/sqrt2)sum_(alpha,beta) A_(alpha,beta)
                         C_alpha^dagger C_beta^dagger Omega.

On two far graph edges of forward types d,e, its occupation coefficient is
sqrt2 (U A U^T)_(d,e). The sum over actual perfect matchings defines its
coefficients in the collision core; nonmatching configurations have zero
coefficient. Denote this infinite relative-orbit profile by Phi_A.

For odd L every four-site torus configuration has a free translation orbit.
Indeed the order of any stabilizing translation divides its orbit partition
of four sites and also has odd order, so must be one. The normalized orbit
basis is therefore V^(-1/2)sum_t|S+t>. A raw fiber profile with coefficient
Phi_A(S) corresponds to Phi_A^phys/sqrt(V) in the physical torus Hilbert
space. It has norm squared V||A||^2+O(1). Dividing that profile by sqrt(V)
gives the asymptotically normalized two-pair state Phi_A^phys/V.

Fix R>=14. Let chi_R,L A be the raw incoming orbit profile, retained only
where the two edges are mutually R-isolated. Such configurations have a
unique pairing. This deletes a fixed finite relative region for fixed R.
Consequently, for large odd L,

 G_L=chi_R,L^dagger chi_R,L/V=I-K_R/V, K_R>=0,             (5)

where K_R is a fixed finite15x15 matrix. In particular G_L->I and is invertible.
The actual polar frame is

 V_(2,L)=chi_R,L G_L^(-1/2)/sqrt(V).                     (6)

This is precisely the physical frame of the checked periodic-cell theorem.
It is a rank15 isometry into the full N=4 carrier, not an assumed canonical
pair algebra. Let P_fr be its range and Q_fr=I-P_fr.

The checked theorem gives

 H_(4,L)>=Delta_L Q_fr,
 Delta_L=a/[C_B R^3+C_R L^2],
 C_B=28000322, C_R=4+15 C_B(R+4)^3,
 V_(2,L)^dagger H_(4,L)V_(2,L)<=theta_L I,
 theta_L=120 max(mu,2tau)s_R/[V(1-delta_L)],
 s_R=(2R+9)^3-(2R-7)^3, delta_L=(2R+9)^3/V.             (7)

These are valid for L>=10(R+4), delta_L<1. Hence theta_L=O(V^-1),
Delta_L is of order L^-2, and theta_L/Delta_L=O(L^-1).

Define the finite Schur operator by the actual physical inverse on Q_fr:

 S_(2,L)=V_(2,L)^dagger H V_(2,L)
  -V_(2,L)^dagger H Q_fr(Q_fr H Q_fr)^(-1)Q_fr H V_(2,L). (8)

Equivalently, for fixed A its quadratic value is the minimum of <Psi,H Psi>
under V_(2,L)^dagger Psi=A. The minimizing complement is unique by(7).
Translation covariance and invariance of the frame force the minimizer into
momentum zero. After rescaling its raw fiber coordinates by sqrt(V), write
it as psi_L. Then its raw energy is

 E_L=V<A,S_(2,L)A>,
 chi_R,L^dagger psi_L/V=G_L^(1/2) A.                    (9)

The trial estimate(7) bounds E_L uniformly for fixed A,R,mu,tau. Q_fr is the
frame complement; it is different from the nonmatching projection Q_nm.

The checked infinite threshold form has the actual variational definition

 <A,T0 A>=inf_(chi compact) E_infty(Phi_A+chi)
        =inf_(chi in ell2) E_infty(Phi_A+chi).           (10)

Its energy is the sum of the actual positive rows and D term in(3).
All nonzero rows of Phi_A lie in a fixed collision neighborhood. Compact
responses and their energy limits in(10) keep the physical collision core.
No bounded infinite zero-energy inverse is assumed in the present proof.

## 3. Actual pair-removal fields retain the normalization and the pin

For an arbitrary zero-momentum raw four-particle profile psi on an odd torus,
define the81 component field

 F_(d,e)(r)=psi({0,e,r,r+d})/sqrt2
             if the four sites are distinct, and0 otherwise.   (11)

The coefficient on the right is the physical orbit amplitude of that
occupation, independent of the chosen representative. This is a redundant
removal map inside the collision core, where several matchings can yield
the same physical coefficient. No independent minimization of these entries
will be made. It obeys exactly

 F_(d,e)(r)=F_(e,d)(-r),   F_(d,e)(0)=0.                 (12)

The common pin is the literal hard-core overlap of the two forward anchors.
Outside the finite collision hole, exchange-orbit normalization makes this
map an isometry: the ordered pair coordinates count each physical exterior
orbit twice, and each value is divided by sqrt2.

Apply the actual pair annihilation rows and retain only graph-edge residual
outputs. For a fixed residual {0,e}, the physical annihilation amplitude is
sqrt2 F_(.,e). Summing all its translated outputs cancels exactly the V from
the normalized translation-orbit basis. Restricting positive rows therefore
gives, for raw physical energy E,

 E>=2a sum_(r,d,e,j)|F_(d,e)(r+e_j)-F_(d,e)(r)|^2,
 E>=2 sum_e S_onepair(F_(.,e)),
 E>=mu ||Q_nm psi||^2.                                 (13)

The first two factors two arise from(11). They do not count a bosonic pair
commutator. Residuals which are not graph edges contribute additional
nonnegative terms and were omitted only in these inequalities.

Let M=V^(-1)sum_r F(r). Fourier projection onto the constant spatial mode in
the second positive form gives

 E>=4mu V ||P_high M||_HS^2.                            (14)

Exchange makes M symmetric. Consequently the components of M outside
Sym^2 U are O(E^(1/2)V^(-1/2)). This high-channel control is separate from
the gradient bound; dropping it would leave the incoming internal tensor
unidentified.

## 4. A uniform torus Sobolev bound, proved here

For a scalar or fixed finite-dimensional vector field f on the cubic torus,
with mean m, there is a dimension-dependent constant independent of L such
that

 (sum_x |f(x)-m|^6)^(1/6)
           <=C (sum_(x,j)|f(x+e_j)-f(x)|^2)^(1/2).       (15)

A short proof makes its uniformity explicit. Triangulate every unit cube by
the same translation-invariant tetrahedral pattern and interpolate f affinely.
The interpolant I f is continuous and periodic. Finite-dimensional norm
comparison on one reference cube gives

 ||I f||_(L6)>=c ||f||_(ell6),
 ||gradient I f||_(L2)<=C ||gradient_lattice f||_(ell2).

The first comparison follows because an affine nodal interpolant with zero
L6 norm has every vertex value zero; compactness of the unit sphere in this
fixed nodal space gives a strictly positive constant. The second follows by
writing the affine derivatives as a fixed combination of vertex differences
and joining each such difference by at most three unit edges. Summing cubes
has bounded overlap. Translation invariance gives integral I f=sum_x f(x),
so the interpolant of f-m has mean zero.

For completeness, Euclidean Sobolev on R3 follows from elementary Fubini and
Cauchy. For compactly supported w, put
A_i(x_other)=integral |partial_i w| dx_i. Then
|w|^(3/2)<=(A_1 A_2 A_3)^(1/2). Two successive Cauchy inequalities give
integral |w|^(3/2)<=product_i ||partial_i w||_1^(1/2).
Apply this to w=|v|^4 and use
||partial_i |v|^4||_1<=4||v||_6^3||partial_i v||_2.
It yields ||v||_6<=C||gradient v||_2. Approximation gives the same inequality
for the compactly supported continuous piecewise-affine functions used here.

Extend the mean-zero periodic interpolant through a fixed number of adjacent
periods, and multiply by a smooth cutoff which equals one on one period,
has support in three periods per coordinate, and derivative O(L^-1).
Euclidean Sobolev gives

 ||I(f-m)||_6<=C[||gradient I(f-m)||_2+L^-1||I(f-m)||_2].

The continuum periodic Fourier Poincare inequality bounds the second term
by the first: its first nonzero frequency is2pi/L. Combining the estimates
proves(15), with no L-dependent constant. Complex components are treated by
their real and imaginary parts, or by the norm inequality; the fixed81
components introduce no volume dependence.

Apply(15) to F_L and use(13). Since F_L(0)=0, the mean itself is bounded:

 ||F_L-M_L||_(ell6)<=C sqrt(E_L/a),
 ||M_L||<=C sqrt(E_L/a),
 sup_r ||F_L(r)||<=2C sqrt(E_L/a).                      (16)

The pin is essential for the second line. A gradient bound alone leaves the
constant unrestricted.

## 5. The constraint fixes the incoming constant in the limit

Let q_R(r,d,e) indicate mutual R-isolation of the two graph edges. Outside
its fixed finite complement, the raw guarded incoming profile has physical
amplitude sqrt2(U A U^T)_(d,e). The exact ordered/physical overlap identity is

 chi_R,L^dagger psi_L/V
    =U^dagger [V^-1 sum_r q_R(r) componentwise F_L(r)] conjugate(U).
                                                               (17)

U is real in the chosen forward convention; the right side is U^T[... ]U.
The exchange-symmetric Frobenius inner product on A is used. The ordered
sum counts two representatives, canceled by the sqrt2 factors from the
incoming and removal profiles. Equation(17) includes every channel and
uses no diagonal-polarization restriction.

The omitted guard set contains only a fixed number of coordinates for fixed
R, and(16) bounds each one uniformly. Thus (9),(17) imply

 U^T M_L U -> A.

Together with(14), symmetry of M_L and U^dagger U=I this proves

                    M_L -> U A U^T.                    (18)

The conclusion concerns the full mean field, not just a sequence of local
averages guessed to approach the supplied tensor.

## 6. Physical compactness and lower semicontinuity

Take a subsequence realizing the liminf of E_L. Every fixed infinite
four-site orbit has a canonical image on all sufficiently large odd tori.
If it admits a matching, its amplitude is sqrt2 times an entry of F_L and
is uniformly bounded by(16). If it does not, (13) bounds the entire Q_nm
part in ell2 and hence each coefficient. A diagonal subsequence therefore
converges pointwise on every fixed physical orbit to a profile psi_infty.

Fatou applied to (13),(16),(18) gives

 Q_nm psi_infty in ell2,
 F_infty-U A U^T in ell6,
 sum |gradient F_infty|^2<infinity.                     (19)

Each actual positive row in(3) has finite support in orbit coordinates.
Any finite collection of them and of the nonnegative D terms agrees exactly
with the infinite-lattice collection once L is sufficiently large. Passing
to the local coefficient limit, then increasing the collection, yields

 E_infty(psi_infty)<=liminf E_L.                        (20)

This is lower semicontinuity of the physical form, including the matching
core and all nonmatching configurations. It is not a statement about a
free two-bond replacement at collisions.

## 7. Compact responses are dense in this limiting energy class

The crucial domain step is to prove that psi_infty is an admissible relaxed
threshold competitor, despite its non-square-summable incoming part.
Write w=psi_infty-Phi_A. In the finite connected matching core this is a
finite vector. In Q_nm it lies in ell2, by(19), because Phi_A vanishes there.
In the separated two-pair exterior it corresponds exactly to the symmetric
ordered field

                 u(r)=F_infty(r)-U A U^T,

up to changes on the finite collision hole. Thus u is ell6. Both psi_infty
and Phi_A have finite positive-row energy, so their difference does too,
by the squared triangle inequality. In the far exterior this is precisely
the free two-bond row energy from the actual h2 tensor sum. Its factors are
finite-range rows obtained from the original S and W; no scalar replacement
or continuum dispersion is used.

Choose an even cutoff eta_m(r), equal to one for |r|<=m, zero for |r|>=2m,
and with one-step differences at most C/m. For any finite-range row L_nu,

 L_nu[(1-eta_m)u]
  =(1-eta_m at a reference point)L_nu u+[commutator term].

The summed squared first term tends to zero by the finite tail row energy.
For the commutator term, bounded range and finite coefficients give

 C m^-2 sum_(m-O(1)<=|r|<=2m+O(1)) |u(r)|^2
   <=C [sum_(same annulus)|u(r)|^6]^(1/3) ->0.           (21)

The annulus has O(m^3) sites; Holder supplies its two-thirds power, which
cancels m^-2. All internal matrix rows are retained. The cutoff is even so
exchange symmetry is preserved. For large m its varying part is far from
the collision core, where the physical/exterior identification is exact.

Independently truncate the Q_nm part in its ell2 norm. The actual N4
operator is bounded by16mu+144tau, so this truncation converges in its energy
seminorm. Keep the finite core unchanged. These operations construct compact
physical orbit vectors w_m with

 E_infty(w_m-w)->0,
 E_infty(Phi_A+w_m)->E_infty(psi_infty).                 (22)

The second follows by Cauchy-Schwarz for the positive row form. Couplings
near the core are unchanged eventually, or converge by the ell2 estimate;
they have not been discarded. Equation(10) now gives the necessary lower
variational bound

 <A,T0 A><=E_infty(psi_infty)<=liminf V<A,S_(2,L)A>.      (23)

Merely knowing pointwise decay of a correction would not have justified
(22). The ell6 estimate and the actual finite-row energy supply its domain.

## 8. Compact trial responses give the reverse inequality

For every epsilon>0 choose one linear compact-response map chi_epsilon on
all fifteen incoming columns whose infinite physical energy matrix obeys

 E_infty(Phi_.+chi_epsilon .)<=T0+epsilon I.             (24)

This follows from the checked common regularized threshold-response maps,
followed by compact approximation in finitely many columns. Alternatively,
quadratic projection in the positive energy completion gives the same
simultaneous finite-dimensional approximation. Boundedness of H4 and the
finite source ensure that compact approximation preserves the cross terms.
No minimizing correction in ell2 is asserted to exist.

Embed X_epsilon,L A=Phi_A+chi_epsilon A on a sufficiently large odd torus in
raw orbit normalization. Its nonzero positive rows have fixed finite relative
support: far separated pairs solve the actual constant N2 zero equations,
and the compact response adds only a fixed neighborhood. Hence

 E_L(X_epsilon,L A)=E_infty(Phi_A+chi_epsilon A)           (25)

exactly for all large enough L, with that threshold depending on the fixed
compact response. No uniform support cutoff in epsilon is assumed.

The frame-coordinate matrix for these trials is

 B_L=G_L^(-1/2) chi_R,L^dagger X_epsilon,L /V=I+O(V^-1).

Indeed chi_R,L agrees with the constant incoming map except in a fixed
region, and the added response is compact. Therefore B_L is invertible for
large L. The raw trial X_epsilon,L B_L^(-1) A satisfies exactly the rescaled
constraint(9). Applying the finite constrained minimum and(24),(25), then
letting L tend to infinity, gives

 limsup V<A,S_(2,L)A><=<A,(T0+epsilon I)A>.

Finally let epsilon decrease to zero. Together with(23) this proves
convergence of every quadratic form. Complex polarization in the fixed
fifteen-dimensional space gives the operator-norm convergence(1).

## 9. Actual low spectrum and limiting profiles

The checked periodic-cell Schur comparison gives, when theta_L<Delta_L,
exactly fifteen low levels and

 lambda_j(H_(4,L))<=lambda_j(S_(2,L))
  <=[1+theta_L/(Delta_L-theta_L)]lambda_j(H_(4,L)).        (26)

Since ||S_(2,L)||=O(V^-1), multiplying the difference by V makes it O(L^-1).
Equation(1) proves the first part of(2). The remaining physical levels are
at least Delta_L, so V Delta_L tends to infinity. The frame is translation
invariant, its low spectral projections commute with translations, and any
other momentum lies orthogonal to the frame and has energy at least Delta_L.
Thus all fifteen low levels are in momentum zero. This is a conclusion about
the full finite N4 operator, not only a preselected fiber.

Every limit profile obtained in Section6 attains T0 by(23) and the now proved
energy convergence. It minimizes the physical energy among profiles whose
exterior correction is ell6 with finite row energy and whose Q_nm correction
is ell2. Compact variations give H4 psi_infty=0 pointwise.

There is at most one such minimizer for a fixed A. For two minimizers their
midpoint is admissible by Section7, so the parallelogram identity forces the
difference w to have zero positive-row energy. W then makes Q_alpha(x)w
constant in x for every fixed residual pair. Sending x to infinity makes
that constant zero: for a graph residual use the exterior ell6 decay; for
a non-graph residual use the Q_nm ell2 decay. The original Hamiltonian,
with all Q amplitudes zero, gives pointwise

                    (4mu+V3(S))w(S)=0.

Thus w=0. The local compactness argument consequently gives convergence of
the whole sequence of constrained minimizers, not just extracted subsequences,
in every fixed physical orbit coefficient. This is not convergence in the
full ell2 norm of the nonnormalizable incoming profiles, and no tail rate
is asserted.

## 10. A zero-mode shortcut which would give the wrong problem

It is not legitimate simply to replace a finite-torus zero-energy Dirichlet
inverse by the infinite transient one. The scalar nearest-neighbor Laplacian
already shows the problem. Write G_L^+ for its mean-zero torus inverse and
remove the origin. Its exact Dirichlet inverse on the remaining sites is

 D_L^(-1)(x,y)=G_L^+(x-y)-G_L^+(x)-G_L^+(y)+G_L^+(0).     (27)

Applying the Laplacian gives delta_(x,y) away from zero, and the expression
vanishes at zero; uniqueness on the finite pinned torus proves(27). If
G_infty is the transient three-dimensional kernel and g=G_infty(0), its
infinite pinned inverse instead is

 G_infty(x-y)-G_infty(x)G_infty(y)/g.

The pointwise limit of(27) differs by the nonzero harmonic rank-one term

              g[1-G_infty(x)/g][1-G_infty(y)/g].         (28)

This uses the standard torus mean-zero kernel limit, obtainable directly
by cutting out its integrable q=0 singularity as in the checked Neumann
packet. The fixed incoming mean constraint is therefore load-bearing in
the present proof. The scalar example refutes this particular shortcut;
it does not refute the full-channel limit just proved.

## 11. Exact controls and actual cost

The new standard-library control imports no earlier author runner. It uses
an odd L=9 torus, nineteen Gaussian-integer orbit profiles spanning the
fifteen incoming tensor directions and including matching-core and nonmatching
configurations. Their literal translation sums contain13851 occupation words.
Direct physical annihilation rows and the59049 relative field entries agree:

 physical graph-residual gradient /V =1262,
 relative gradient of f=sqrt2 F =1262,
 physical graph-residual S /V =491/2,
 relative S of f =491/2.

All81 common pins, all59049 exchange relations, the exact constant-high
bound941/2187<=491/2, and all fifteen complex guarded incoming overlaps
were checked. These controls exercise the factor sqrt2, orbit normalization,
redundant core map and omitted nonnegative residual rows. They do not establish
the uniform Sobolev theorem or the infinite-volume convergence by sampling.

Separately, exact rational inversion on the27-site scalar torus checks all
676 entries of(27). Its pinned diagonal is26/81; applying the inappropriate
transient-style finite formula gives637/3564 instead. This supplies a concrete
finite check of the zero-mode distinction, not a numerical infinite Green
value or a T0 matrix entry.

The single job was frozen and priced at30 CPU seconds/150 MB, threads one.
It passed without a failed assertion or script repair, using5.764103 CPU
seconds,5.772395 wall seconds and55,492,608 bytes peak RSS. Runtime deadline
and STOP checks were active. CONTROL_FREEZE.json, controls.json and the
execution capture bind the actual script and output. No full N4 torus
spectrum, Schur entry, T0 entry, large Fock basis or numerical limiting value
was computed. The old packets were not edited.

## 12. The still-open many-pair and boundary problems

Equation(1) closes the fixed two-pair finite-volume identification left open
by the prior periodic bridge. It does not prove

 V S_(n,L) approximately sum_(i<j) T0^(ij)

uniformly for growing n<=K, or even claim the corresponding fixed n>2 limit.
At N=4 the matching core is finite and its complement is a three-dimensional
relative exterior plus the gapped nonmatching sector. For more pairs,
collision sets have unbounded spectator coordinates; the nonmatching versus
exterior split used in(19)-(22) no longer describes the whole geometry.
The pin/Sobolev compactness argument above cannot be reused as if those
spectator variables were a fixed finite multiplicity.

A compatible many-pair lower proof still needs controlled allocation of
actual positive rows to two-pair collision regions, while preserving shared
physical amplitudes and pricing simultaneous clusters and spectator boundary
errors. An arbitrary normalized four-particle lift already has the checked
wrong one-body/three-body balance and is not repaired by(1). Small global
norm leakage out of a periodic soft band also does not control amplitudes
on a rare collision set without an additional local estimate.

The separate lower comparison between a large physical torus and small
periodic cells remains open. Their seams are a changed boundary condition;
this proof does not assert that imposing them lowers H0. A lower Neumann
or positive-row boundary construction must still be supplied.

The result is consequently a genuine fixed-particle threshold bridge with
complete channel and physical normalization, not the desired dilute EOS.
It adds no axiom or primitive, makes no original-record substitution, and
selects no physical state, polarization, condensate or gravitational law.
