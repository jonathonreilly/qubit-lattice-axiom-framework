# Physical many-particle trial states reach the relaxed threshold upper coefficient

Author proof candidate, September30. No independent check or formal review yet.
The contract and frozen input identities are adjacent. This is one upper
variational bridge for the ACTUAL supplied native M2 Hamiltonian, not a full
EOS, phase theorem, pair-boson substitution or axiom adoption. The current
landed density model and checked provisional N4 threshold/positivity sources
retain all their hypotheses. mu,tau>0 are fixed throughout.

## 1. Target and exact physical preparation

Write the landed model as H0=sum_x h_x, with

 H0=mu N-2mu sum PE-mu sum PT+V3+W,
 W=tau sum_(x,j,A) [Q_A(x+e_j)-Q_A(x)]* [Q_A(x+e_j)-Q_A(x)],
 V3=mu sum_x n_x binom(sum_(d in G)n_(x+d),2),
 G={+/-2e_i,+/-e_i+/-e_j:i<j}.

All b_x=|0><1| are the physical site operators. The five Q, their hard-core
products and their shared-center normalizations are those of the current
native density source, unchanged. Let
R=(QE1,QE2,QT12/sqrt2,QT13/sqrt2,QT23/sqrt2). For z inC5, ||z||=1, put

 C_z^dagger=sum_(x,A) z_A R_A(x)^dagger,
 A_z=C_z^dagger-C_z.

On every sufficiently large periodic torus, H0 Omega=0 and
H0 C_z^dagger Omega=0, with ||C_z^dagger Omega||^2=V. This uses the exact
q0 single-pair Gram, not canonical pair commutators. H0 and N conserve
particle number and H0 is nonnegative on the FULL carrier.

A finite four-site configuration S has no nonzero translation stabilizer on
Z3. Choose one representative S_sigma for each translation orbit. Let chi
have finite support in this physical N4 orbit basis. Define

 W_sigma^dagger=product_(x in S_sigma) b_x^dagger,
 X_chi=(1/sqrt2)sum_(sigma,t)
             [chi_sigma W_(S_sigma+t)^dagger-conj(chi_sigma) W_(S_sigma+t)],
 psi_L(u)=exp(u^2 X_chi) exp(u A_z) Omega,  u real.          (1)

This is an EXACT normalized state on all physical M2 sites. It is not a
truncated vector, a state of independent pairs, or a projection onto a
chosen matching. All four-site creation words obey original hard-core
exclusion; different pairings of the same occupation word still interfere.
For each fixed chi, X is a bounded finite-range interaction with four-site
terms, though its range can grow when improving the threshold approximation.
No preparation efficiency or physically selected source is claimed.

## 2. Uniform local commutator bounds

The landed grouping has ||h_x||<=h_*=182mu+240tau and support at most25sites.
This is a grouping bound, not a global norm made independent of volume.
For completeness, 153 triple terms contribute153mu; the onsite plus E/T
attractions give(1+16+12)mu; fifteen gradient squares give240tau. All their
sites lie among x, its six nearest neighbors and its18 length-two neighbors.

Expand A_z into literal two-site terms d_e B_e^dagger-conj(d_e)B_e, allowing
repeated physical pairs from distinct centers. Each such anti-Hermitian term
has norm|d_e|: it couples |00> to |11> and annihilates the other two states.
Let ell_z be the sum of absolute primitive coefficients at one center.
The coefficient sums of the five R fields are

 (sqrt2,4/sqrt6,sqrt2,sqrt2,sqrt2),
 ell_z<=sqrt(32/3),   alpha=4ell_z.

Each translated two-site term meets a specified site in at most two positions,
so the per-site sum of A-term norms is at most2ell_z. A commutator therefore
costs at most alpha times the size of the current support. This overcounts
shared-center words harmlessly. Similarly set

 m_chi=(1/sqrt2)sum_sigma |chi_sigma|,   beta=8m_chi.

A four-site X-term has norm|chi_sigma|/sqrt2 and has four possible translates
through each site. Its commutator costs at most beta times support size.
Each A step adds at most one site and each X step at most three; using three
for both gives a convenient common bound. Define

 F_m(s)=product_(j=0,...,m-1)(s+3j), F_0(s)=1.

For ANY prescribed sequence of r A and s X commutators acting on an operator
O with initial support q,

 ||ad_A^r ad_X^s O||<=alpha^r beta^s F_(r+s)(q)||O||.      (2)

The notation denotes that particular ordered nesting; the same bound works
for every interleaving. Proof: expand into local connected sequences, drop
every disjoint commutator, bound each one by2 times the local norm, and count
choices using the current support cardinality. Repeated terms are included.
It is not assumed that the sum of all sequences itself has small support.
Summing the h_x gives (2) timesVh_* with q25, and summing n_x gives V withq1.
The constants depend on chi and couplings, never onV. Any fixed-chi torus
large enough to embed its terms has these bounds; global occupation remains
unrestricted. Spatial range affects that embedding size, not the cardinality
bound. This is why no V*u^2<<1 hypothesis is needed.

## 3. An actual uniform sixth-order energy remainder

For anti-Hermitian A and realu, conjugation exp(-uA) O exp(uA) is norm preserving.
Integral Taylor remainder therefore bounds orderm by
|u|^m ||ad_A^m O||/m!, and likewise for X at parameteru^2.
The number phase exp(i pi N/2) fixes H0,N,Omega,X and sends A to-A.
Every vacuum expectation used below is even inu.

Expand the X conjugation to second order, then the A conjugations:

 e^(-u^2X) H0 e^(u^2X)
 =H0+u^2[H0,X]+(u^4/2)[[H0,X],X]+R_X,
 ||R_X||<=|u|^6 ||ad_X^3 H0||/6.

The H0-only expectation has no terms through degree3, because H0 kills both
Omega and A Omega; its degree5 also vanishes by parity. For [H0,X], the
vacuum expectation is zero, odd derivatives vanish, and retaining its
A-degree2 leaves an orderu4 remainder, multiplied byu2. For the double-X
term retain its vacuum expectation; its first A derivative is zero and its
remaining second-order error is multiplied byu4/2. Thus

 |<H0>_(psi_L(u))/V - e4_L u^4| <= D_chi |u|^6,           (3)
 D_chi=h_*[alpha^6 F6(25)/720
          +alpha^4 beta F5(25)/24
          +alpha^2 beta^2 F4(25)/4
          +beta^3 F3(25)/6].

This is an integral remainder for the full unitary state, valid at every
realu with its stated loose bound. It is not a finite-volume asymptotic with
an unspecified V-dependent error. All orderings are kept in the double
conjugation; no BCH commutativity is used.

The same calculation for N needs only the fourth-order remainder. Its pulse
part has second coefficient2V. The single-X commutator has zero vacuum and
first-A expectation because it changes particle number by4; the double-X
remainder is already orderu4. Therefore

 |<N>_(psi_L(u))/V-2u^2|<=B_chi u^4,                      (4)
 B_chi=alpha^4 F4(1)/24
          +alpha^2 beta F3(1)/2+beta^2 F2(1)/2.

These statements hold for complexz andchi. The number phase is enough for
parity; no reality assumption on the state is being imposed.

## 4. Identifying the coefficient without losing identical-pair factors

The vector expansion at fixed finite volume gives

 psi_L(u)=Omega+u C_z^dagger Omega
       +u^2[(C_z^dagger)^2 Omega/2 -V Omega/2 +X_chi Omega]+O_L(u^3).

Indeed C_z C_z^dagger Omega=V Omega. Because H0 kills the first two vectors,

 e4_L=V^-1 <(C_z^dagger)^2 Omega/2+X_chi Omega,
                  H0[(C_z^dagger)^2 Omega/2+X_chi Omega]>.  (5)

Only this coefficient calculation uses a fixed-volume vector expansion;
(3) supplies the uniform error for the actual state. The vacuum component
is harmless because H0 Omega=0.

In the infinite translation-orbit convention of the checked threshold source,
Phi_z is the physical matching profile(C_z^dagger)^2 Omega/sqrt2.
Let F_z=H4 Phi_z; it has FINITE relative support and finite row-square energy
E_bare(z). The bounded N4 operator obeys0<=H4<=16mu+144tau.
For finite-supportchi define

 E_z(chi)=E_bare(z)+2 Re<chi,F_z>+<chi,H4 chi>.             (6)

Every term in (6) is an actual physical configuration form. For a sufficiently
large torus, the finitely many compact orbits inchi,F and H4chi have no
translation identifications, and their normalized orbit vectors are
V^-1/2 sum_t |S+t>. The X definition gives
X_chi Omega=sqrt(V/2) chi_L, while(C_z^dagger)^2 Omega/2 corresponds to
sqrt(V/2) Phi_z,L. Hence(5) equals

                         e4_L=(1/2) E_z(chi).             (7)

The incoming profile is not square summable on the infinite relative space.
Equation(7) does NOT assert an isometry of the entire finite-torus N4 fiber.
Far-separated torus configurations may have translation stabilizers. They
are outside the compact collision/source supports and cannot change(6):
the original N2 zero equations cancel H Phi exactly for separated pairs.
Equivalently the bare pulse coefficient is a finite connected commutator
coefficient, so embeds locally without depending on those distant orbits.
The fixed finite cross term andchi term then embed directly. Choose L larger
than twice the diameter of all these finitely many connected supports and
any translated overlaps needed by the four commutators. Such a finite L_chi
exists; no all-size alias assertion or fixed cutoff independent ofchi is used.

The profile normalization in(7) is essential. In the E1 example the known
bare form is104mu+240tau and the unitary pulse coefficient is HALF of it,
52mu+120tau. This agrees with the independent physical quartic calculation;
no empirical coefficient is inserted.

## 5. Reaching the checked relaxed threshold infimum

The checked N4 theorem defines

 T(z)=inf_(chi in l2) E_z(chi)
     =E_bare(z)-<F_z,G_H(0)F_z>,  T(z)>0.                 (8)

The strict positivity is the separately checked extension at fixedmu,tau;
no uniform-coupling lower bound is imported from it. The zero-energy
minimizer need not belong tol2. This causes no gap here. Its resolvent
approximants chi_epsilon=-(H4+epsilon)^-1 F are inl2 and approach the infimum
in quadratic-form value, by the checked finite inverse form. Since H4 is
bounded and F is finite, finite-support approximations of any chi_epsilon
converge in(6). Thus for everyepsilon>0 there is a FINITE chi with

                 T(z)<=E_z(chi)<=T(z)+epsilon.            (9)

Neither an l2 limiting minimizer nor a numerical Green-matrix evaluation is
assumed. The state(1), with this fixedchi, equations(3)-(4),(7) and its explicit
finite constants provide the desired actual many-particle upper embedding.
The order is fixedaccuracy -> fixedchi -> arbitrarily largeL -> smallu.
The remainder constants may diverge asaccuracy tends tozero; they are never
used uniformly inthat further limit.

## 6. Grand-canonical upper asymptotic and a coherent-channel lower consequence

Let g_L(nu)=E0(H0-nu N)/V. For fixedchi, set t_chi=E_z(chi)>0. Equations(3)-(4)
give the exact variational upper estimate

 g_L(nu)<= (t_chi/2)u^4 -2nu u^2
                           +D_chi |u|^6+nu B_chi u^4.

Taking u^2=2nu/t_chi yields for L>=L_chi,

 g_L(nu)<= -2nu^2/t_chi
                  +(8D_chi/t_chi^3+4B_chi/t_chi^2)nu^3.   (10)

It follows, without assuming a thermodynamic ground-state limit, that

 limsup_(nu down0) limsup_(L toinfinity) g_L(nu)/nu^2
                                      <=-2/T(z).          (11)

For each fixedchi first take the two indicated limits, then improvechi using
(9). T(z) is continuous on the compact unit sphere, because the threshold
form is a finite Hermitian matrix on Sym2C5; it is strictly positive there.
Minimizing over coherent z therefore gives the same bound with
T_coh=min_(||z||=1)T(z)>0. Fragmented/entangled many-pair states may improve
it; equation(11) is an UPPER bound, not equality or a polarization selection.

There is an additional consistency consequence of the LANDED full-carrier
coercivity, c=min(tau,mu/12)/99090432:

 <H0>/V>=c[(<N>/V)^2-2<N>/V^2].

Apply this to(1) at fixedchi,u, take L toinfinity first to remove the last
term, then u down0 using(3)-(4). It gives E_z(chi)/2>=4c. Infimizing over
finitechi proves the explicit COHERENT-channel bound

                          T(z)>=8c.                      (12)

This is a statement for rank-one symmetric incoming vectorsz tensorz. It
is not a bound on the smallest eigenvalue of the full15channel matrix,
whose arbitrary entangled input need not have this form. It also does not
identify the exact many-body lower-energy coefficient. The loose lower
bound in the landed grand-canonical theorem and(11) are consequently
consistent: -1/(4c)<=-2/T_coh.

The variational trial itself has rho=2u^2+O_chi(u4), so its energy-to-mean-
density-squared ratio tends to E_z(chi)/8. No fixed-number projection or
canonical thermodynamic theorem is claimed from that ratio. Establishing
such a theorem, especially a matching many-body lower bound with the full
channel functional, remains an additional task.

## 7. Explicit one-word improvement on the bare E pulse

Take the exact physical configuration

 S={0,(3,-1,1),(3,1,1),(6,0,0)}.

Only its middle two sites are G neighbors, an axialy edge; the endpoints
are isolated. Direct actual operator action gives

 h_S=<S,H4 S>=8mu/3+4tau,
 [H4(C_E^dagger)^2 Omega](S)=tau/3.                        (13)

The diagonal follows from4mu number energy minus(4mu/3)E attraction and
4tau center-gradient energy; V3=0 and every plane annihilator vanishes.
The source amplitude is the actual original-word witness of the threshold
report and was freshly reconstructed here, not replaced by a generic matrix.
Choose the single compact correction

 chi_S=-tau/(3sqrt2 h_S),
 X_chi= -tau/(6h_S) sum_t [W_(S+t)^dagger-W_(S+t)].

Its true quartic energy coefficient is

 e4=52mu+120tau -tau^2/(36h_S)
   =52mu+120tau -tau^2/(96mu+144tau).                      (14)

This is a strict many-particle trial improvement for everymu,tau>0, with
all remainders bounded by(3)-(4). It does not approximate the entire T matrix
or assert this one correction is optimal. Atunitcouplings the generator
coefficient is-1/40 and e4=41279/240, compared with172 for the bare pulse.
The gain is small but exact; no fit or parameter search selected a match.

The new check_word.py implements literal N4 annihilation/creation from the
five supplied Q fields with exact Fraction arithmetic. It imports no prior
action routine. It reconstructs the full21entry H|S> column, checks all21
Hermitian reverse columns, contracts its exact matching amplitude, and
verifies(13)-(14) at three rational parameter controls. Actual wall0.0775s,
CPU0.07736s,RSS17,973,248bytes, under20CPU/150MB price. This is a local word
control; the all-volume unitary remainder and threshold variational passage
are proved above rather than inferred from finite matrices.

## 8. What this does and does not retire

This constructs a concrete upper variational map from every compact physical
N4 correction to an exact full-carrier many-particle state with a uniform
error. Improving compact corrections reaches the relaxed threshold upper
coefficient, with explicit identical-pair normalization. It replaces the
unjustified step of simply inserting the pulse quartic as a scattering
coupling. It also gives the independently interpretable one-word improvement.

The matching LOWER energy comparison is still missing. A small density of
defects does not by itself control their order-rho^2 energy, and an absolute
QH0Q gap is not a resolvent estimate at extensive background energy. Nothing
here fixes fragmentation, spontaneous U1 order, finite-density excitation
spectra, linear tensor polarizations, record readout or a common gravitational
source. The Hamiltonian, state preparation and quantum interpretation remain
supplied. Current axiom inconsistency is neither proved nor suggested by the
success of this optional model construction.

Focused independent checking is required before extensive reuse. Particularly
check the physical orbit normalization, finite-torus stabilizer exception,
uniform mixed-commutator remainders, and order of infimum/volume/density limits.
