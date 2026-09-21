# A local curl encoding permits native formation and exact Gauss identities

2026-09-21. Primary conditional derivation and proposed extension of the
checked finite-alphabet Euler proof. Independent review pending. This
construction changes the field readout, not the permanent record content.
It is separate from the thirteen-state collective-loop process.

## 1. Keep the fifteen-state record process, change the derived field

Use vacancy, the six A-axis labels and eight B-cube labels of draft PR8560.
Their two record features are e and b, with e=+/-e_i on A, b in {+/-1}^3
on B, and the other feature zero. These are fourteen distinct selected
possibilities/readout labels, not a derivation of that menu from M_2(C).
Every exchange moves whole records unchanged. Write U(x)=2e(x), V(x)=b(x).
Values zero at a vacancy are mathematical bookkeeping, not an axiom that
an empty site has an observable readout.

For centered differences d_i f(x)=[f(x+e_i)-f(x-e_i)]/2, define

    C f = d cross f,
    E_lat = C V,       B_lat = -C U.                       (1)

These are local derived quantities assembled from neighboring records.
They are not new contents attached to a record. Since centered differences
commute, d dot C=0 identically. Thus both microscopic Gauss identities hold
in every configuration, through every whole-record exchange and every
single-site birth. No constraint on a birth's distant vacancy footprint
is required. If U is polar and V axial, then E_lat is polar and B_lat
axial under the already specified full cubic action.

This is a kinematic identity of the chosen readout. It is not an emergent
gauge redundancy or a proof that all raw longitudinal and scalar degrees
of freedom disappear. They remain independently record-readable. Periodic
curls also have zero global flux, and the centered operator has the usual
additional even-volume high-frequency zeros.

## 2. A genuine nearest-neighbor forming-label law

For j with 0<|j|<1 choose the covariant positive weights

    W_ab=1+j[e(a).e(b)+(1/4)b(a).b(b)],    W_a0=1.         (2)

Their bracket lies between -1 and 1: A/A dot products are in {-1,0,1},
B/B products divided by four in {+/-1/4,+/-3/4}, and cross-orbit terms
are zero. Hence 1-|j|<=W_ab<=1+|j|. All are strictly positive. The B/B
term is a scalar even with the axial convention, so reflection covariance
is retained as well as the proper cubic covariance required by the axioms.

At a vacant x create label a at microscopic rate

    (beta/N) product_(y nearest x) W_(a,eta_y),    beta>0. (3)

Conditional on a birth at x, its label law is precisely these fourteen
products divided by their sum. It depends only on the six nearest-neighbor
conditions, and for j!=0 it varies with them. It is a supplied example of
the distribution clause, not a selection of W by the axioms. Rate, clock,
menu, context-exchange tensor and the field readout remain supplied choices.
Record formation, permanence, capacity and the exact identities in (1)
coexist for this process. The earlier collective-birth locality counterexample
does not apply to (3), which is an actual single-site nearest-neighbor law.

## 3. Conditional finite-alphabet Euler extension

Use the positive-floor context exchange of PR8560 with potential
Psi=gamma X cross Y, X=sum_a p_a e(a), Y=sum_a p_a b(a).
For full-support smooth probability fields the exact product currents are

    J_a=gamma p_a[e(a) cross Y+X cross b(a)-2X cross Y].

The macroscopic candidate equation with (3) is

    partial_t p_a+div J_a(p)=B_a(p),
    B_a=beta p_0 m_a(p)^6,
    m_a=1+j[e(a).X+(1/4)b(a).Y],                         (4)

where p_0=1-sum_(a=1)^14 p_a and the vacancy equation has reaction
-sum_a B_a. All finite-volume birth rates are bounded, local functions.

Here is the complete change in the previously checked entropy argument
(PR8557 for exchange, PR8561 for native formation). On a finite torus use
the uniform fifteen-label reference pi. If f_t=d mu_t/d pi and D_N(f)
is the unweighted swap square-root-density form, the birth adjoint bound
is R_N^*1<=beta(1+|j|)^6 N^3. The exchange contribution retains its fixed
floor kappa>0 and pointwise product stationarity. Consequently

    integral_0^T D_N(f_t)dt
       <=N^3[log(15)+beta(1+|j|)^6 T]/(N kappa).          (5)

The same finite count-sector Poincare comparison and marginal Hellinger
bound give fixed-block replacement: each count sector of the fifteen-label
interchange process is connected, and the lower rate bound is unchanged.
The constants may depend on the fixed alphabet size and j, but not N.
The successive limits N->infinity, block size ell->infinity and the
macroscopic averaging scale->0 are the ones of the cited exchange/native
proofs; seven-site birth terms add a block-boundary O(1/ell) term.

For the inhomogeneous product nu_p, average the birth adjoint under a
block product with occupied probabilities q. Its local value is

    Vbar_B(q;p)=beta sum_a [q_a p_0/p_a-q_0] m_a(q)^6.    (6)

At q=p it is zero. Its differential in q_b is
beta[p_0 m_b(p)^6/p_b+sum_a m_a(p)^6], exactly the b component of
H(p)B(p), H=diag(1/p_a)+(1/p_0)11^T. Terms differentiating m_a(q)
vanish at q=p because their bracket is zero. Therefore the time derivative
of nu_p cancels the linear reaction term in the relative-entropy equation
when (4) holds, just as the exchange entropy potential cancels its flux.
The remainder is bounded by a uniform quadratic form on an interior
compact probability set. The bounded Hessian and entropy inequality give
the same entropy Gronwall estimate, with the new finite constants.

Thus, conditional on a C^2 solution p of (4) staying uniformly interior
on [0,T], and H(mu_N,0|nu_p(0))/N^3->0, the relative entropy per site
vanishes uniformly on that interval. This is an extension by the displayed
alphabet substitution and checked adjoint cancellation, not a new claim
of global smoothness or a stochastic fluctuation theorem. Tightness,
centering and fluctuation replacement for native formation remain separate.

## 4. Complete linear reaction at the homogeneous trajectory

At equal occupied probabilities p_a=rho/14, the features average to zero,

    rho'=14 beta(1-rho),
    rho(t)=1-v0 exp(-14 beta t),
    rho_A=3rho/7,   rho_B=4rho/7.                         (7)

The product law at (7) is a hydrodynamic background, not the exact finite
law when j!=0. Linearizing the full fourteen-species reaction and current
gives for U=2X and V=Y

    U_t=c(t) curl V+lambda(t)U,
    V_t=-c(t) curl U+lambda(t)V,
    c(t)=2gamma rho(t)/7,
    lambda(t)=12 beta j[1-rho(t)].                        (8)

The coefficient 1/4 in (2) makes the two reaction eigenvalues equal:
sum_A e_i e_j=2delta_ij, sum_B b_i b_j=8delta_ij. It is an explicit
design choice, not a value derived from symmetry. In the full moment basis,
the density has eigenvalue -14beta; the orbit difference 4rho_A-3rho_B,
two A quadrupoles, three B pair characters and B triple character have
zero linear reaction. All six vector components have eigenvalue lambda.
At a nonzero wave vector and gamma!=0 the four transverse vector modes
have drift lambda+/-ic|K|, while the two raw longitudinal components have
drift lambda. The additional seven zero-reaction fields are retained.

Applying continuum curl to (8) and using (1), with continuum
E=curl V and B=-curl U, yields

    E_t=c(t) curl B+lambda(t)E,
    B_t=-c(t) curl E+lambda(t)B,
    div E=div B=0.                                     (9)

Coefficients are homogeneous in space; an inhomogeneous background would
produce gradients of c and lambda and is not covered by (9). The temporal
generators in (8)-(9) commute. The amplitude multiplier is exactly

    exp(integral_s^t lambda)=
         exp[(6j/7)(rho(t)-rho(s))],                     (10)

and the wave phase is |K| integral_s^t c(tau)d tau. For j>0 the total
amplification is bounded by exp[(6j/7)(1-rho(s))]; j<0 damps it. This is
deterministic linear response about the conditional Euler background.

An exact finite-system covariance witness prevents importing the uniform-
birth product fluctuation theorem. Starting from the homogeneous product,
the macroscopic-time derivative of the covariance of matching U components
at nearest-neighbor sites is

    d/dt Cov(U_i(x),U_i(x+e_l))|_0
          =16 beta j rho(1-rho)/7,                       (11)

and identically for V. Both endpoints contribute; the other five neighbor
factors average to one. Exchanges give zero because that product is their
stationary law. This is nonzero for beta>0, j!=0 and interior rho. The
same formula for a microscopic-time generator has an extra factor 1/N.

## 5. Precisely what is inherited at j=0

At j=0, the existing growing-product Gaussian theorem applies unchanged.
For continuum mode K, let U_K^N,V_K^N be its N^-3/2 fluctuation fields.
The microscopic derived fields must be scaled as

    E_K^N=N i s(K/N) cross V_K^N,
    B_K^N=-N i s(K/N) cross U_K^N.                        (12)

This is N times (1), because an unscaled lattice difference vanishes at
a fixed continuum wavelength. For any fixed finite collection of modes,
the deterministic matrices in (12) converge to iK cross. The continuous
mapping of the established Gaussian process therefore gives (9) with
lambda=0, plus transverse Gaussian birth noise. Its equal-time covariance
in either sector is

    S_E(K,t)=S_B(K,t)=(4rho(t)/7)(|K|^2 I-KK^T),          (13)

and its instantaneous birth bracket is

    Q_E(K,t)=Q_B(K,t)=8beta[1-rho(t)](|K|^2 I-KK^T).      (14)

The E/B equal-time cross covariance is zero. Thus exact Gauss does not
mean noise-free formation. There is no longitudinal noise, but transverse
noise survives this normalization. Without the factor N in (12), the
fixed-mode covariance tends to zero. This result is restricted to fixed
finitely many modes; no ultraviolet tightness theorem has been added.

## 6. The spectral requirement has moved into the underlying state

More generally, let F(x)=sum_(r in a fixed finite set) M_r xi(x+r)
be a fixed-coefficient linear local encoding of arbitrary microscopic
features xi. If d dot F=0 is an identity for every xi, its analytic Fourier
matrix A(k) obeys s(k)^T A(k)=0. Put k=t v and let t tend to zero:
v^T A(0)=0 for every v, hence A(0)=0 and A(k)=O(|k|).
If the underlying covariance S_xi(k) is bounded near zero, then

    S_F(k)=A(k)S_xi(k)A(k)^*=O(|k|^2).                   (15)

This is a bounded-spectrum statement about linear finite-range encodings,
not all nonlinear record models or already constrained correlated fields.
The N-dependent normalization in (12) does not evade the spectral shape:
its continuum covariance still grows as |K|^2.

For the curl encoding, an underlying transverse spectrum proportional
to 1/|k|^2 instead produces a finite nonzero transverse projector. This
is the classical Coulomb-phase/thermal-field target. It requires a
long-range correlated underlying state; it is not a property of the
homogeneous product state used in the proved fluctuation theorem.

The quantum-vacuum target is different. For a supplied canonical free
oscillator H=(p^2+|k|^2 q^2)/2 with [q,p]=i, the ground state has
<p^2>=|k|/2 and <q^2>=1/(2|k|). Identifying electric amplitude with p
and magnetic amplitude with |k|q gives field variance |k|/2 per transverse
polarization. Under a curl encoding this would require a potential spectrum
proportional to 1/|k|. The canonical commutator and Hamiltonian are additional
assumptions in this comparison; none has been derived for the record model.

## 7. What this construction changes

The collective-loop locality counterexample has a constructive escape:
use a local curl of record features and a genuinely nearest-neighbor birth
law. Exact Gauss identities then impose no distant vacancy test on formation.
A controlled conditional Euler route and explicit propagating linear modes
remain available. The missing physics is now explicit: why this field
readout is selected, how the required correlated state is generated, what
removes or interprets the other readable fields, and where quantum dynamics
and matter sources enter. The identity div curl=0 is not evidence for any
of those answers. No claim of physical electromagnetism or TOE closure is made.

## 8. A late-state selection result within this supplied native process

There is a further conclusion that does not require a native fluctuation
theorem. Start at a fixed interior density 0<rho0<1 with independent equal
occupied-label probabilities rho0/14. Assume the conditional Euler result
of Section 3 for the homogeneous solution on each fixed finite interval.
At each finite N let the process run indefinitely, including its exchanges
after the last birth. Then:

1. Every site is eventually occupied, almost surely.
2. The final fraction of each of the fourteen labels tends in probability
   to 1/14 as N tends to infinity.
3. The limiting finite-N law is the mixture, over these final counts, of
   uniform permutations of the labels. Its local thermodynamic limit is
   the full-occupancy product with probability 1/14 for every label.

For the first statement, a configuration with m vacancies has total
macroscopic birth rate at least r_min m, where

    r_min=14 beta(1-|j|)^6>0.

Each birth reduces m by one and no event increases it. The expected
macroscopic absorption time is at most H_m/r_min, where H_m is the
harmonic sum. This gives almost-sure finite absorption at each finite N;
it is not a uniform-in-N fixed-time filling claim.

For the second statement let P_(N,a)(T) and V_N(T) be the occupied-label
and vacancy fractions at a fixed macroscopic T. The entropy-per-volume
Euler conclusion implies their laws of large numbers:

    P_(N,a)(T) -> rho(T)/14,    V_N(T) -> v(T).

No subsequent exchange changes any label count, and all subsequent births
number at most V V_N(T). Hence deterministically

    P_(N,a)(T) <= P_(N,a)(infinity)
                   <= P_(N,a)(T)+V_N(T).                 (16)

Take N large at fixed T, and then choose T large enough that
v(T)=v0 exp(-14beta T) is arbitrarily small. This squeezes every final
fraction to 1/14. No uniform hydrodynamic estimate up to an N-dependent
absorption time is needed. The argument uses monotone formation and exact
label-count conservation, not an assumed final independent law. Empty
initial density is not covered by this interior-entropy argument.

At full occupancy, the positive-floor nearest-neighbor whole-label
exchanges connect every configuration with given label counts. The uniform
law on that count sector is invariant by the same pointwise telescoping
identity as the product law. A finite irreducible continuous-time chain
converges to this unique conditional law. Since the finite process reaches
full occupancy almost surely, its long-time law is the stated mixture.
Sampling finitely many sites from a uniform count sector is sampling
without replacement. Its falling-factorial probabilities converge to
the product probabilities when all count fractions tend to 1/14. This
proves the third assertion. It does not bound the time required for mixing
after saturation or exchange the large-volume and late-time limits.

An exact second-moment identity strengthens the readout conclusion without
asserting a central limit theorem. In a uniform count sector with empirical
label law p, any one-site feature vector f has covariance C_f(p) at one
site and -C_f(p)/(V-1) at two distinct sites. For nonzero lattice Fourier
modes k,l and the V^-1/2 convention,

    Cov(fhat(k),fhat(l)^*)
        =[V/(V-1)] C_f(p) 1_(k=l modulo 2pi).            (17)

Its conditional nonzero-mode mean is exactly zero. Averaging (17) over the
selected final counts and using their convergence proves that the late-state
U and V covariance tends to (4/7)I; their cross covariance tends to zero.
Applying the scaled curls (12) yields

    S_E(K)=S_B(K)=(4/7)(|K|^2 I-KK^T)                   (18)

for each fixed nonzero continuum mode. Thus the quadratic spectrum in this
ordered late-state limit is selected by the specified formation-plus-mixing
process; it is not solely an artifact of initially preparing a product.
The result still differs from both comparator spectra of Section 6.
Neither a dynamical Gaussian limit for that count mixture nor a uniform
mixing-rate theorem is claimed here. All global zero modes retain their
separate count-history meaning, while the curl readout removes their flux.
