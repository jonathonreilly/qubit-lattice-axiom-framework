# Actual number response: a slow-field energy limit and a spectral alternative

Author discovery candidate; conditional on the explicitly supplied native M2
Hamiltonian and the source-bound checked homogeneous energy theorem. This is
not formal review, an audit, a phase claim, or part of the frozen native
thermodynamics delivery. A new focused check is required before reuse.

There is a nontrivial consequence of the actual energy law: an arbitrarily
long-wavelength density field has a controlled nonlinear canonical response.
At a field of size O(rho), that response must be carried either by genuine
jumps in ground-state density modulation or by positive-energy density
spectral weight on an O(|k|sqrt(rho)) scale at some nearby field. Ordinary
ground degeneracy alone is not the first alternative. The conclusion does
NOT move that spectral weight to the homogeneous lambda=0 ground state.

The distinction is essential. Uniform convergence of ground energies, even
to a smooth quadratic response function, need not give the zero-field linear
susceptibility. Section8 gives an exact finite-pencil discriminator. No
bosonic carrier, condensate, harmonic replacement or continuum dynamics is
used in the positive statements below.

## 1. Actual inputs, conventions and limit order

The complete main source7180c065 was refreshed at
fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7. On the full cubic site-qubit tensor
product let b_x=|0><1|, n_x=b_x* b_x, N=sum n_x. The actual pair displacements
are +/-2e_i and +/-e_i+/-e_j, eighteen distinct neighbors for L>=5. Use

 d_i(x)=b_(x-e_i)b_(x+e_i),
 v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j),
 QE1=(d1-d2)/sqrt2, QE2=(d1+d2-2d3)/sqrt6,
 QTij=(1/2)sum_(s,t) v_ij^(s,t).

With fixed supplied mu,tau>0, the unchanged law is

 H0=mu N-2mu sum PE-mu sum PT+V3+W,
 V3=mu sum_x n_x binom(m_x,2),
 W=tau sum_(x,j,A)[Q_A(x+e_j)-Q_A(x)]*[Q_A(x+e_j)-Q_A(x)],
 H0=S+mu D+W,
 S=(2mu/3)sum_x |d1+d2+d3|^2
     +(mu/4)sum_(x,i<j,r<s)|v_r-v_s|^2,
 D=(1/2)sum_x n_x(m_x-1)(m_x-2).                           (1)

The literal local grouping H0=sum h_x has radius two and
||h_x||<=h=182mu+240tau. Number is conserved. H0>=0 and the all-density
coercivity are landed supplied-model results, not choices of a realized
state or consequences of M2 alone.

The checked homogeneous mean/grand and canonical compositions supply

 g(nu)=lim_L min spec(H0-nu N)/L^3,
 e(rho)=lim_(L,N_L/L^3->rho) E_L(N_L)/L^3,
 g(nu)=-(2/t)nu^2+o(nu^2),
 e(rho)=c rho^2+o(rho^2),  c=t/8>0.                       (2)

The grand limit is uniform on compact chemical-potential intervals; the
mean energy limit is uniform on[0,1/2]. The canonical limit in(2) is for
fixed0<rho<1/2, every integer sequence, and equals that mean energy. Here
t is the coherent minimum of the actual full15 threshold form T0, not its
least eigenvalue or a numerically fitted scattering coefficient. This author
previously authored parts of the lower/mean composition and independently
checked the canonical transfer/composition; those roles are not relabeled
independent checking of the present argument. Exact inputs/receipts are
bound in SOURCE_BINDINGS.json.

Fix even M>=6 and L a multiple of M. Set

 k=2pi/M, s=2sin(pi/M), phi_M(x)=cos(k x_1),
 A_M=sum_x phi_M(x)n_x, H_lambda=H0-lambda A_M,
 F_(L,N,M)(lambda)=V^-1 min spec(H_lambda restricted to N). (3)

All finite states/excitations below remain in the SAME exact actual N
sector. A_M commutes with N. The external density field is a mathematical
probe; it is not a derived physical law or a clock. Translation by M/2 in
axis1 changes A_M to -A_M and preserves H0 and N. Thus F is even, whether
or not an individual ground vector is translation invariant.

The principal limits are L->infinity at fixed M,rho and N_L/V->rho, then
M->infinity through even values, then rho->0. Field amplitudes lambda=alpha
rho have alpha fixed before the last limit. No unrestricted joint limit or
fixed-rho field-removal limit is asserted.

## 2. Literal continuity and a density f-sum on the full carrier

Let E be the unique physical pair-graph edges, B_e=b_x b_y for e={x,y}.
Expanding only the S and W squares in(1) defines a real symmetric matrix K:

 H0=mu D+sum_(e,f in E) K_ef B_e* B_f.                     (4)

This is an operator identity in every particle sector, not an independent
pair representation. On N=2, K is the actual graph-edge Hamiltonian; on
higher sectors the overlapping B_e obey their literal hard-core algebra.
Each row of a square contains edges with endpoints in one star or two
nearest-neighbor stars. Two endpoints in that row can be joined with at
most three coordinate steps. Thus for real phi with nearest-neighbor
Lipschitz constant L_phi, w_e=sum_(x in e)phi_x obeys

 |w_e-w_f|<=6 L_phi whenever K_ef can be nonzero.           (5)

The statement uses chosen local paths even across a torus seam, and is
valid for the periodic cosine with L_phi<=s. It does not use the unbounded
affine coordinate as a periodic test function.

For any such real phi put A(phi)=sum phi_x n_x. The exact site algebra gives

 [A(phi),B_e*B_f]=(w_e-w_f)B_e*B_f,
 [H0,A(phi)]=-sum K_ef(w_e-w_f)B_e*B_f,
 [A(phi),[H0,A(phi)]]=-sum K_ef(w_e-w_f)^2 B_e*B_f.        (6)

D, V3 and all diagonal terms commute with A(phi). The additional probe
-lambda A_M and any scalar chemical potential commute with A_M as well.
For an ordered pair of distinct graph edges define the Hermitian local
transfer current J_ef=i K_ef(B_e*B_f-B_f*B_e), J_fe=-J_ef. Then the actual
Heisenberg equation (hbar=1 in the supplied Hamiltonian time) is

 d n_x/dt=-(1/2)sum_(e,f)[1_(x in e)-1_(x in f)]J_ef.     (7)

The sum is local and sum_x of its right side is zero. This is number
continuity for actual two-site rearrangements, with no chosen dimer matching
or fluid velocity. A pair transfer can share an endpoint with another pair;
(6)-(7) remain valid in that case.

A useful uniform absolute row bound is

                    sum_f |K_ef|<=b, b=3mu+24tau.         (8)

Here is the full counting rather than a band-norm substitution. An axial
edge appears in the single S singlet row at its unique center, giving
(2mu/3)*3=2mu. A plane edge occurs at TWO centers; at each it appears in
three two-word difference rows, giving 2*(3mu/4)*2=3mu. For W an axial edge
occurs in six gradients per collective E row. Their bounds are
12tau sum_A |u_Ai| sum_j |u_Aj|, equal to20tau,20tau,16tau for the three
axial orientations. A plane edge occurs in six gradients at each of its two
centers, each with |coefficient|=1/2 and row coefficient sum4, giving24tau.
Triangle inequality before any cancellation proves(8). No plane center is
removed and no momentum-dependent Gram normalization is substituted.

For any state, write p_e=<B_e*B_e>=<n_x n_y>. Cauchy-Schwarz gives
|<B_e*B_f>|<=sqrt(p_e p_f). Symmetry of |K| and2sqrt(p_e p_f)<=p_e+p_f
combine (5)-(8) into

 |(1/2V)<[A_M,[H0,A_M]]>| <=18 b s^2 <P_edges>/V
                               <=C rho s^2,
 C=162b, rho=<N>/V, P_edges=sum_e n_x n_y<=9N.             (9)

The last inequality uses the actual eighteen-neighbor graph. It holds on
each occupation word and hence as an operator. This deliberately coarse
constant needs neither low-energy dimer factorization nor an EOS derivative.

If Omega is any exact-sector ground vector of H_lambda and P0 is its FULL
ground projection in that sector, define the positive inelastic measure

 dmu(omega)=V^-1 <A_M Omega, Q d1_(H_lambda-E0)(omega) Q A_M Omega>,
 Q=1-P0, omega>0, m_j=integral omega^j dmu(omega).          (10)

Its first moment is exactly half the double commutator in(9), by inserting
H_lambda Omega=E0 Omega on both sides. Therefore

                         0<=m1<=C rho s^2.               (11)

All elastic transitions inside a degenerate ground space are excluded.
Neither ordinary variance nor zero-energy ground mixing is counted as a
positive-energy density excitation.

## 3. Canonical thermodynamics in the actual periodic density field

For fixed M define G_(M,L)(nu,lambda)=V^-1 min spec(H0-nu N-lambda A_M).
Tile L by cubes of side ell that is a multiple of M. The field pattern then
aligns in every cube. Replacing the actual law by independent periodic
ell-cube copies changes only centers within two steps of a face or in the
leftover set. The same explicit bound as in the checked block proof is
24h B_L ell^2+h R_L for H0. Onsite source terms are identical on the full
cubes; their leftover cost is at most(|nu|+|lambda|)R_L. Thus G_(M,L)
converges uniformly on compact(nu,lambda) sets to G_M as L->infinity through
multiples of M. This uses a bounded-norm comparison, not monotone deletion
of positive physical neighbors.

Let e_(M,L)(r,lambda) be the minimum energy density of H_lambda over density
matrices of mean number rV. The finite convex hull obeys

 -|lambda|r<=e_(M,L)(r,lambda)<=(h+|lambda|)r.

After adding |lambda|r it is nonnegative convex, zero at r=0 and bounded
above by(h+2|lambda|)r. On0<=r<=1/2 its supporting slopes for the unshifted
function lie in[-|lambda|,2h+3|lambda|]. Consequently finite convex duality,
followed by uniform grand convergence, gives uniformly in r on[0,1/2]

 e_M(r,lambda)=lim_L e_(M,L)(r,lambda)
              =sup_nu {G_M(nu,lambda)+nu r}.              (12)

The supremum may be restricted to that fixed compact slope interval, or a
larger interval common to a bounded lambda family.

This mean limit also is the actual exact-N limit. For completeness, choose
any periodic ell-block mean-r state with ell a multiple of M. Dephase into
its m+1 number sectors, m=ell^3. Round block frequencies on B' regular
cubes with sum absolute errors<=2m and number error<=2m^2. Reserve

 r_L=ceil((|N_L-rV|+2m^2+2)/(min(r,1-r)m))+1

whole cubes, plus leftover sites. Their fraction tends to zero at fixed
ell,r. The residual integer number lies between zero and the number of
reserved actual sites, so fill it exactly with a site occupation state.
Both parities are allowed. Number-sector mixtures within a fixed sector
are legitimate variational states; no typical-sector projection is used.
The regular-block energy error is<=2(h+|lambda|)m^2; reserved-block norms
and true versus artificial periodic seams are bounded by the same radius-two
comparison with h replaced by h+|lambda|. Dividing by V gives

 limsup_L F_(L,N_L,M)(lambda)
       <=e_(M,ell)(r,lambda)+24(h+|lambda|)/ell.

The canonical lower is e_(M,L)(N_L/V,lambda). Uniform mean convergence and
continuity handle the moving density. Sending ell->infinity after L proves

 lim_(L multiple M,N_L/V->rho) F_(L,N_L,M)(lambda)
                                      =e_M(rho,lambda).   (13)

Both sides are Lipschitz in lambda with constant at most1 (indeed rho_L
and rho), so pointwise convergence promotes to uniform convergence on
compact lambda intervals by a finite net. These steps do not select any
state and may use phase-separated block competitors.

## 4. Actual slow-field energy, before taking any derivative

For the next comparison ell need NOT be a multiple of M. In each ell cube,
freeze the onsite chemical field nu+lambda cos(k x1) at one representative.
The actual field norm error per volume is at most |lambda| k ell. After
removing the same true seams, the independent cube energies are homogeneous
g_ell at these representative fields. Replace each representative by the
site values in its cube using the1-Lipschitz property of g_ell, costing at
most another |lambda| k ell. The leftover fraction vanishes when L->infinity.
The homogeneous boundary proof gives |g_ell-g|<=24h/ell uniformly on any
fixed compact chemical interval. Finally the discrete cosine-phase average
approaches its integral with error at most2pi |lambda|/M. Hence, for ell>=5,

 |G_M(nu,lambda)-G_ad(nu,lambda)|
     <=48h/ell+4pi |lambda|ell/M+2pi |lambda|/M,
 G_ad(nu,lambda)=(1/2pi)integral_0^(2pi) g(nu+lambda cos theta)dtheta. (14)

This is uniform for bounded nu,lambda. Taking ell approximately sqrt(M)
proves convergence without exchanging a finite-band symbol or a low-energy
projection with the actual interaction. In particular no continuum
hydrodynamic Hamiltonian has been supplied or inferred.

Uniform convergence in the compact supremum(12) yields

 E_ad(rho,lambda):=lim_(M even->infinity)e_M(rho,lambda)
       =sup_nu [nu rho+(1/2pi)integral g(nu+lambda cos theta)dtheta]. (15)

Only energy variational functions appear in(14)-(15). Calling this a slow
spatial field formula does not assert convergence of local densities or of
actual ground vectors. The elementary bound on the field gives

 |E_ad(r,lambda)-e(r)|<=|lambda|r,  0<=r<=1/2.             (16)

## 5. Dilute nonlinear response and its response measure

Fix0<alpha0<=c/4 and put lambda=alpha rho, |alpha|<=alpha0. Every maximizing
nu in(15) is a supporting slope of the convex function E_ad(.,lambda) at
rho. Its secants from0 and to2rho, together with(16), imply

 e(rho)/rho-|lambda| <=nu
       <=[e(2rho)-e(rho)]/rho+3|lambda|.                  (17)

For all sufficiently small rho these confine the relevant nu to
[c rho/2,5c rho], and every nu+lambda cos theta is between c rho/4 and
6c rho. Thus the actual asymptotic g(s)=-s^2/(4c)+o(s^2) is uniform across
all relevant arguments. Maximizing its quadratic part at nu=2c rho gives

 E_ad(rho,alpha rho)
       =rho^2[c-alpha^2/(8c)]+o(rho^2)
       =c rho^2-(alpha rho)^2/t+o(rho^2),                 (18)

uniformly on the stated alpha interval. The lower bound may use nu=2c rho
directly; the upper uses(17). No second derivative of e or g was taken.

All functions F,e_M,E_ad are concave in lambda. Their negative distributional
second derivatives are positive measures. Uniform convergence on compact
intervals implies weak convergence of these measures against compactly
supported smooth tests, directly by twice integrating the test derivative.
After lambda=rho alpha, (18) gives the ordered limit

 -d_alpha^2 [F_(L,N_L,M)(rho alpha)/rho^2]
             --> (2/t) d alpha,                          (19)

first L, then M, then rho. Atomic crossing response is included in this
measure. In lambda variables the rescaled measure is rho^-1 times the
pushforward of the lambda-curvature measure. Equation(19) is an averaged
response statement, not convergence of its density at alpha=0.

A particularly transparent finite consequence uses only three field values.
For any fixed0<alpha<=c/4 put a=alpha rho. For all sufficiently small rho,
then all sufficiently large even M, and then all sufficiently large allowed
L along every N_L/V->rho sequence, (13),(15),(18) give

 D_F:=F(0)-[F(a)+F(-a)]/2 >=a^2/(2t).                    (20)

The thresholds may depend on alpha,rho,M and the integer sequence. No
uniform joint scale is claimed. Evenness makes D_F=F(0)-F(a), but the
symmetric form fixes the factors without invoking ground-vector symmetry.

## 6. What the finite response measure actually contains

On a finite exact-N carrier the pencil H0-lambda A_M has finitely many
real eigenvalue branches. Except at finitely many branch coincidences its
distinct eigenvalues and spectral projections are analytic, and bottom
multiplicity is constant. One direct justification is to take the squarefree
part of its characteristic polynomial over the rational function field in
lambda; outside the finite zeros of its discriminant and denominators,
its distinct real roots are analytic by the implicit function theorem.
Identical branches cause constant multiplicities, not a response atom.
Eigenvalues are globally Lipschitz by the variational principle. The
concave lowest root therefore has curvature measure

              -F''=chi(lambda)d lambda+sum_j J_j delta_(lambda_j), (21)

where chi>=0 on the regular intervals and J_j=F'_-(lambda_j)-F'_+(lambda_j)
>=0. The exceptional set is finite, so there is no other singular component.
Limits of the integrable regular curvature account for all non-atomic mass.

At a regular point differentiate (H-E)Omega=0 on the ground complement.
One may choose the derivative orthogonal to the whole ground subspace;
(H-E)Q Omega'=Q A_M Omega. Constant bottom multiplicity also implies
P0 A_M P0=-E' P0. Differentiating the energy a second time gives, for EVERY
normalized ground vector at that regular point,

 chi(lambda)=-F''(lambda)
       =(2/V)<A_M Omega,Q(H-E)^-1 Q A_M Omega>=2m_(-1).    (22)

This argument applies to permanent degeneracy; no zero denominator is used.
A ground vector can be extended differentiably in the analytic subspace
with vanishing in-subspace derivative at that point. Differentiating its
Rayleigh expectation then proves(22), independent of that choice.

At an exceptional point the variational one-sided derivative formulas give

 J_j=[max_(ground Omega)<A_M>/V]-[min_(ground Omega)<A_M>/V]. (23)

Thus a positive atom means distinct modulation responses among actual
coexisting ground states. Merely having two symmetry-related vectors with
the SAME modulation expectation contributes no atom. Since A_M preserves
N, this is not a crossing of different total-number sectors.

The exact tent-kernel identity for concave F is

 D_F=(1/2)integral_(-a,a)(a-|lambda|)chi(lambda)d lambda
       +(1/2)sum_(|lambda_j|<a)(a-|lambda_j|)J_j.           (24)

Endpoint atoms have zero weight. It follows either by integrating F'' on
the two half intervals or by checking a linear function and each elementary
concave kink. The continuous tent has total weight a^2/2 after the factor1/2.

## 7. An actual nearby-field crossing/soft-spectrum alternative

Combine (20) and(24). At least one of the following occurs on the finite
actual exact-N Hamiltonian under the scale conditions of(20):

 (A) sum_(|lambda_j|<a)(a-|lambda_j|)J_j >=a^2/(2t).

 (B) At some regular lambda_* in(-a,a),
                           chi(lambda_*)>=1/(2t).        (25)

Indeed either the atomic contribution to D_F is at least a^2/(4t), or its
regular part is. The latter, divided by the tent area a^2/2, gives(B).
Continuity on regular intervals supplies an actual point, not just a
formal distributional derivative. In(A) the total jump sum is at least
a/(2t); no lower bound on one individual jump or on a specified field is
claimed. Cases(A),(B) can both occur.

In case(B), let rho_L=N_L/V. Equations(11),(22) give m_(-1)>=1/(4t).
For the lowest POSITIVE energy in the support of the density spectral
measure, positivity of that measure proves

 Delta_density^2 <=m1/m_(-1)<=4 C t rho_L s^2,
              Delta_density<=2sqrt(C t rho_L)s.           (26)

This is an upper bound on a density-coupled spectral threshold, not a lower
sound velocity or an isolated pole. More explicitly, with
Omega_cut=sqrt(8 C t rho_L)s,

 integral_(0,Omega_cut] omega^-1 dmu(omega)>=1/(8t).       (27)

For the omitted high part, omega^-1<=omega/Omega_cut^2 and(11) give at
most1/(8t); subtract from m_(-1)>=1/(4t). Equation(27) controls an INVERSE
energy weighted response. Arbitrarily small ordinary spectral mass at
very low energy is not excluded, so it is not an extensive unweighted
structure-factor or ODLRO claim.

This conclusion applies to the actual supplied density observable and
full-carrier exact-sector ground states at their stated lambda_*. Ground
space degeneracy is removed in(10), so it cannot be mislabeled positive
spectral weight. Fields have size at most alpha rho. At fixed positive rho
we do not send their size to zero, and lambda_* need not equal zero. The
long-wavelength perturbation also breaks one-site translation covariance;
its probe wave number is not an asserted sharp momentum of an eigenstate.

## 8. Why this does not already supply a homogeneous sound mode

Here is an exact logical discriminator, not a competing native model. Fix
beta>0 and a bounded field interval. On a finite diagonal carrier with labels
r=j delta covering the interval's minimizers, take

 H_delta|r>=r^2/(4beta)|r>, A_delta|r>=r|r>,
 f_delta(lambda)=min_r[r^2/(4beta)-lambda r].               (28)

Choose the label range slightly larger than2beta times the largest field.
Completing the square and taking the nearest grid point gives uniformly

 -beta lambda^2 <=f_delta(lambda)
        <=-beta lambda^2+delta^2/(16beta).                 (29)

Yet for |lambda|<delta/(4beta) the unique ground label is r=0, the energy
is exactly flat, its linear susceptibility is zero, and A_delta has no
inelastic spectral weight. All commutators with A_delta, hence its f-sum,
are zero. At lambda=(2j+1)delta/(4beta) the ground slope jumps by delta.
These atoms tend weakly to2beta d lambda as delta->0. Thus smooth limiting
pressure, positive limiting curvature and even an arbitrarily small f-sum
upper bound do NOT force unperturbed positive-energy density response.
It would be false to apply the regular spectral formula to the entire
limiting curvature while ignoring its crossing provenance.

The example is not a construction of the actual native H0 ground states
and does not disprove their compressibility, pairing phase or sound. It
identifies precisely an invalid inference from the available scalar data.
A narrower same-state sufficient input for homogeneous soft response is

 chi_(L,M)(0)=2m_(-1)(A_M; actual homogeneous ground)>=chi_*>0, (30)

with the full ground projection removed and the required volume/wavelength
uniformity specified. Then(11) immediately gives a positive density spectral
threshold <=s sqrt(2C rho_L/chi_*). A lower bound of this type is a genuine
static response obligation, weaker than a pole/dispersion theorem. Neither
(2),(18),(19) nor finite-distance pair coherence proves(30). Uniform
quadratic-response remainder control before exchanging field removal and
volume/wavelength limits would be one possible route; at fixed rho even
existence of the relevant thermodynamic second derivative remains open.
No finite-density phase, selected internal polarization, tensor mode,
physical clock/source or permanent record is established here.

## 9. Prior work, actual controls and remaining scope

The complete campaign phase and dilute-structure routes already prove
finite-distance pair coherence, a weak finite-mode commutator estimate and
several precise failures of phase arguments. Those are not counted again.
The older all-N capacity route was read, including its global-projection
counterfamilies. Its scalar coefficients are not a dynamical premise here.
Main's native charge-motion note concerns an edge-charge D=2 model; the
star spectral/response notes use a supplied Gaussian CAR reference. Their
carriers and their positive spectral measures cannot be imported into(1).
Main's exact Ward and ring-response notes already give the general spectral
moment method and ground-projection warning. The present mathematical delta
is the actual pair-H0 number row bound, actual slow-field canonical limit,
and the crossing-versus-inelastic-response alternative. No historical
novelty or new universal sum-rule principle is claimed.

The new standard-library Fraction control builds actual physical edge rows
from S/W and separately compares them with the original onsite/attraction
N2 expression. All nine orientations agree exactly. The uncancelled row
bounds are exactly those in(8); actual cancellations make the axial W rows
16tau, but that improvement is not needed. Four literal occupation-matrix
fixtures verify both commutators in(6), including shared endpoints and
nearest-center gradients. The initial affine probe commuted with axial S,
as its opposite-pair coordinate sums are identical. Its clean evidence is
preserved under historical/affine-probe-control. The final quadratic-plus-
affine probe makes all four double-commutator fixtures nonzero; this is a
coverage refinement, not a repaired mathematical failure.

The final process exited0:0.543957 child CPU seconds,0.653157 wall seconds,
31,801,344 bytes peak RSS, below its30CPU/40wall/150MiB price. BLAS limits1
and the original deadline/STOP guard were active. It enumerated584 literal
basis columns over supports of at most eight sites, not a finite-density
torus eigensystem. Neither run imported another author's assembly. No
thermodynamic convergence, susceptibility, mode or phase was numerically
fitted. The analytic arguments above carry every large-volume assertion.

All original campaign packets and the frozen delivery tree are untouched.
This source awaits focused independent checking; source hashes and clean
finite controls do not grant a formal review grade or retained status.
