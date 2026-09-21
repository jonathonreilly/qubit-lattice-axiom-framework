---
claim_id: mobile_records_local_curl_quantum_interface_and_born_formation_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied fifteen-state immutable-record process, local curl readouts enforce exact divergence identities while native nearest-neighbor formation gives the stated conditional fourteen-color Euler equation. Ordered late-time canonical covariance is quadratic at small wave number. The original fourteen-label marked kernel has rank seven; fixed qubit preparations and an independent apparatus cannot implement it, while the displayed qutrit/four-dimensional constructions and projective cubic covariance minimum have their stated separate scopes. A changed Born-compatible kernel realizes one quantum event with the stated optimal parent fidelity and classical time-dependent wave sector. These results do not identify an operational qubit with the framework algebra, realize repeated permanent quantum histories, prove native stochastic fluctuations, select a quantum vacuum or derive electromagnetism."
upstream_dependencies:
  - minimal_axioms
  - mobile_records_immutable_transverse_curl_limits_bounded_theorem_note_2026-09-21
runner: scripts/mobile_records_local_curl_quantum_interface_and_born_formation_2026_09_21.py
---

# Local curl fields, quantum interfaces and continued record formation

**Date:** 2026-09-21  
**Type:** bounded_theorem  
**Status:** proposed_retained  
**Author support:** conditional-support; no independent audit verdict.

This packet tests one specified mobile-record model at three connected
interfaces: exact local field identities during birth, a physical quantum
implementation of its marked probabilities, and the effects of changing
those probabilities to fit a one-qubit event. Each calculation keeps the
permanent classical records distinct from the derived field readout and
from the additional operational quantum hypotheses.

The fifteen-state alphabet, transport, birth rates, clock and field map are
supplied choices, not a derivation from
[the minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
The conservative/fluctuation supplier is the exact proposed source in
[the transverse construction](MOBILE_RECORDS_IMMUTABLE_TRANSVERSE_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md),
draft PR8560 at c26b0171974c456f68dd92a4c8661ade1cc5ddbd.
The finite-alphabet native-entropy supplier is the separately proposed
[PR8561 source](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/4ae52ade2299b4dfaff388971f423aa8f6ddf64a/docs/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md),
head4ae52ade2299b4dfaff388971f423aa8f6ddf64a. Its complete note is included
byte unchanged in this packet's suppliers directory, SHA-256
b10c0ad5fb9e0802b9fb7a5c206d5d9e1970b2c2573a5d792ab29b2758aea0dc.
These are explicit provisional dependencies; no combined landing or audit
closure is asserted. The original source bodies below were independently
examined at the hashes in PUBLICATION_TRANSFORM.json.

The local-curl and ordered late-state results concern the classical process.
The single-event quantum construction does not make its whole history a
quantum process. Norm and late-wave scattering bounds in Part C apply to
the six vector components U,V, with beta>0, not the separately decaying
density mode. The original and changed kernels are separate models.

## Part A. Local curl readout with nearest-neighbor formation

2026-09-21. Primary conditional derivation and proposed extension of the
checked finite-alphabet Euler proof. Selective independent mathematical review is complete. This
construction changes the field readout, not the permanent record content.
It is separate from the thirteen-state collective-loop process.

### 1. Keep the fifteen-state record process, change the derived field

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

### 2. A genuine nearest-neighbor forming-label law

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

### 3. Conditional finite-alphabet Euler extension

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

### 4. Complete linear reaction at the homogeneous trajectory

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

### 5. Precisely what is inherited at j=0

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

### 6. The spectral requirement has moved into the underlying state

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

### 7. What this construction changes

The collective-loop locality counterexample has a constructive escape:
use a local curl of record features and a genuinely nearest-neighbor birth
law. Exact Gauss identities then impose no distant vacancy test on formation.
A controlled conditional Euler route and explicit propagating linear modes
remain available. The missing physics is now explicit: why this field
readout is selected, how the required correlated state is generated, what
removes or interprets the other readable fields, and where quantum dynamics
and matter sources enter. The identity div curl=0 is not evidence for any
of those answers. No claim of physical electromagnetism or TOE closure is made.

### 8. A late-state selection result within this supplied native process

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

## Part B. Exact quantum-interface resource requirements

2026-09-21. Primary conditional derivation, with completed selective independent review.
This tests the one-parent birth law in LOCAL_CURL_READOUT_AND_NATIVE_FORMATION.md.
It does not identify the axiom's possibility algebra with an operational
quantum carrier without an additional bridge assumption.

### 1. The classical probability matrix has rank seven

Use the six A labels with e=+/-e_i,b=0 and the eight B labels with e=0,
b in {+/-1}^3. Set the six-component vector t_a=(e_a,b_a/2), and

    T_ab=t_a dot t_b,
    P_ab=[1+j T_ab]/14,             0<|j|<1.              (1)

Here b indexes the single occupied parent and a the newborn label; the
other five neighboring sites are vacant. Every column sums to one because
sum_a t_a=0. If F is the matrix with row t_a, then

    F^T F=2 I_6,      T=F F^T,      T^2=2T,
    T 1=0.                                                (2)

Therefore P has eigenvalue1 on the constant vector, eigenvalue j/7 on
six feature directions, and eigenvalue0 on seven remaining directions.
It has rank7 whenever j!=0. The sign of j does not alter the rank.

Suppose each of the fourteen unknown parent labels is represented by
some density matrix rho_b on a single physical qubit. The choice of those
states is otherwise unrestricted. A fixed instrument has effects E_a,
and its classical output probabilities obey

    Q_ab=Tr(E_a rho_b).

The real space of Hermitian qubit operators has dimension4, so rank(Q)<=4.
Consequently no such instrument realizes (1) exactly, even if it may
disturb the parent, uses arbitrary input-independent ancillas, and chooses
the fourteen input density matrices freely. An input-correlated record of
the preparation label is a different resource and is excluded here.
More precisely, the input and apparatus have the product state rho_b tensor
tau, with fixed tau. Shared randomness that correlates the choice of
preparation encoding with the apparatus is also excluded; a mixture of
different coordinated encodings need not retain this rank bound. Private
apparatus randomness independent of the input is already included in E_a.

The same test applies to positive observed rate effects. Giving every input
a strictly positive content-dependent occurrence rate h_b would require
the rate matrix P diag(h). Its rank remains7, whereas a qubit rate-effect
matrix still has rank at most4. Thus a positive occurrence clock does not
repair this single-parent interface. An input at which formation never
occurs does not implement the stipulated positive-rate native law.

This is a finite operational-interface test of this matrix. It does not
rule out the record process as a classical process, spatially encoded
records, quantum-only output marginals, or a different quantum formation law.

### 2. A quantitative bound without choosing the qubit encoding

Let delta=max_b TV(P_.b,Q_.b), optimized over any choice of fourteen qubit
input states and any fourteen-effect POVM. The following bound is not
claimed sharp:

    delta >= sqrt(3/7) |j| / 14.                          (3)

Indeed rank(Q)<=4 makes its kernel have dimension at least10. Its
intersection with the seven-dimensional range of P has dimension at least3.
On that range the smallest singular value of P is |j|/7. Choose three
orthonormal vectors in the intersection. Their Q images vanish, giving

    ||P-Q||_F^2 >= 3 j^2/49.

Each column difference has zero sum. If its positive and negative masses
both equal delta_b, its squared Euclidean norm is at most2 delta_b^2.
Summing fourteen columns yields ||P-Q||_F^2<=28 delta^2, proving (3).
The argument bounds any single-qubit realization, without a covariance
restriction or an asserted optimal carrier encoding.

### 3. Exact approximation for the natural fourteen Bloch rays

Now specify rho_b=(I+v_b dot sigma)/2, with v_A=e and v_B=b/sqrt(3).
This is a different optimization: the input encoding is fixed.

Proper cubic rotations act on both sets of rays by qubit unitaries.
Group averaging cannot increase the convex worst-input total variation.
An optimal averaged POVM therefore has the form

    E_A=alpha I+u e_A dot sigma,
    E_B=eta I+w b_B dot sigma,
    6alpha+8eta=1,
    alpha>=|u|,        eta>=sqrt(3)|w|.                  (4)

The respective fourfold and threefold stabilizers force the displayed
vector directions. Only proper rotations are used in this argument.
For j>=0 put a=alpha-1/14, d=eta-1/14 and z=w/sqrt(3)-j/56. The two
distinct input-row losses, computed directly from the dot-product counts,
are

    TV_A=max(|a|,|u-j/14|)+2|a|+4max(|d|,|w|),
    TV_B=3max(|a|,|u|/sqrt(3))
              +max(|d|,3|z|)+3max(|d|,|z|).             (5)

Project u into [0,j/14] and w into [0,sqrt(3)j/56]. This decreases every
absolute slope discrepancy in (5). Replacing a,d by zero then decreases
the displayed losses again. The resulting effects obey positivity at
alpha=eta=1/14 for 0<=j<=1. Thus a,d can be set to zero in the unrestricted
optimization, not merely in a convenient ansatz. It remains to minimize

    max(j/14-u+4w, sqrt(3)u+3j/28-2sqrt(3)w)             (6)

over that rectangle. A positive weighted average of the two affine
functions cancels w and is minimized at u=0. Their intersection at u=0
lies within the rectangle. Equivalently, along the intersection the loss
increases with u. Hence

    delta_natural=|j|(3-sqrt(3))/14,                     (7)
    u=0,     w=j(2-sqrt(3))/56,
    alpha=eta=1/14.

Relabeling every output by t_a->-t_a handles negative j. Formula (7) is an
exact optimum over all POVMs for these fixed inputs. It is not the optimum
over all qubit encodings in Section2. For j=1/2 it is about0.045284 of total
variation; the unrestricted-encoding lower bound (3) is about0.023381.

### 4. Positive higher-dimensional realizations

The rank bound for a d-dimensional carrier is d^2>=7, hence d>=3. This is
only a dimension lower bound. The following constructions establish more.

For |j|<=1/3, a qutrit suffices. Let G_1,...,G_6 be six traceless Hermitian
Gell-Mann matrices normalized by Tr(G_r G_s)=2delta_rs. Write G(t)=sum t_rG_r.
Its operator norm is at most its Hilbert-Schmidt norm sqrt(2)|t|<=sqrt(2).
Set

    epsilon=1/(3sqrt(2)),      d_j=3sqrt(2)j/28,
    rho_b=I_3/3+epsilon G(t_b),
    E_a=I_3/14+d_j G(t_a).                              (8)

The states have trace1 and are positive. The effects sum to I_3 and their
minimum eigenvalue is at least(1-3|j|)/14. Direct trace multiplication
gives Tr(E_a rho_b)=(1+j t_a dot t_b)/14. Thus the minimum carrier Hilbert
dimension is exactly3 for 0<|j|<=1/3 when parent disturbance is allowed.
No minimal-dimension claim is made for 1/3<|j|<1.

A four-dimensional carrier works throughout |j|<=1. Use an orthogonal
two-valued orbit register and one qubit:

    rho_A=|A><A| tensor (I+e_A dot sigma)/2,
    rho_B=|B><B| tensor (I+b_B dot sigma/sqrt(3))/2.

Define block-diagonal effects, listing their A and B register blocks,

    E_A=diag((I+j e_A dot sigma)/14, I/14),
    E_B=diag(I/14, (I+j sqrt(3)b_B dot sigma/4)/14).       (9)

They sum to identity; their nonconstant Bloch radii are |j| and3|j|/4,
so they are positive. Their probabilities are exactly (1). These are
ordinary disturbed-parent instruments, for example by square-root effects.
The register is an additional physical resource. Encoding a qutrit or
four-level carrier across fundamental qubits would require an explicit
spatial carrier, motion and capacity construction; (8)-(9) do not supply it.

There is a stronger exact statement if the carrier must also realize the
proper cubic rotations by a single projective unitary representation U_g,
with rho_(gb)=U_g rho_b U_g^dagger and E_(ga)=U_g E_a U_g^dagger.
Under that extra covariance condition the minimum carrier dimension is4
for every 0<|j|<1. The construction (9) is covariant with
U_g=I_orbit tensor u_g, where u_g is the usual spinor implementing the
proper rotation on Bloch vectors. The following argument rules out d=3
without assuming the qutrit states in (8).

The proper cubic group is S_4. Both triples e and b transform in its
three-dimensional rotation representation R. Since P acts as j/7 on
their direct sum, the equivariant preparation map from label coefficients
to Hermitian carrier operators must be injective on R+R. The conjugation
representation Ad(U) must therefore contain at least two copies of R.
If d=3, its remaining dimension is3; one dimension is the identity
operator. Write its character as 1+2chi_R+chi_W, with W of dimension2.

For reference the complete ordinary S_4 character table is below, on
classes identity, transposition, double transposition, three-cycle,
four-cycle (sizes1,6,3,8,6):

    1:       (1,  1,  1,  1,  1)
    sign:    (1, -1,  1,  1, -1)
    E:       (2,  0,  2, -1,  0)
    R:       (3, -1, -1,  0,  1)
    R sign:  (3,  1, -1,  0, -1).

These follow from the sign representation, the four-letter permutation
representation minus its constant, and the permutation of the three
pairings minus its constant. Character inner products verify irreducibility
and the squared dimensions sum to24. Thus every dimension2 W is E or a
sum of two one-dimensional characters.

At a transposition, the proposed Ad(U) character equals -1+chi_W(g).
It must equal |Tr U_g|^2>=0, including for a projective U. The only
dimension2 choice with chi_W(g)>=1 is two trivial characters. Thus
Ad(U) would have exactly three trivial components. Equivalently, the
complex commutant of U would have dimension3. Complete reducibility for
unitary representations of a fixed finite projective multiplier says this
dimension is the sum of the squared irreducible multiplicities. Dimension3
therefore forces three inequivalent multiplicity-one blocks. In total
carrier dimension3 each block must be one-dimensional. Three inequivalent
one-dimensional projective representations with the same multiplier cannot
exist: the ratio of any two is an ordinary S_4 character, and S_4 has
only two such characters. This is a contradiction. The d=1,2 cases were
already excluded by rank. No classification of all projective S_4 irreps
is needed for this argument.

### 5. Exact pure-parent permanence is a stronger interface

Suppose the parent carrier instead has a pure state |psi_b> for each
label b, and the whole fixed channel must return that same pure parent
state exactly. Its dilation factors on each input as

    V|psi_b>=|psi_b> tensor |z_b>.

For any nonorthogonal pair, preservation of the inner product gives
<z_b|z_c>=1 (up to consistent state phases), so their complementary
classical outcome laws must agree. Every two columns of P differ for
j!=0: F has column rank6, so T_.b=T_.c would imply t_b=t_c, contrary
to the fourteen distinct features. Hence all fourteen parent states must
be mutually orthogonal if the nonconstant marked birth law is implemented
with exact pure-parent preservation. The carrier dimension is then at
least14, attained by a fourteen-state classical pointer register with
the controlled stochastic law (1).

Four physical qubits can hold that many orthogonal code states, but this
dimension statement is not a mobile four-site record construction. It does
not apply unchanged to mixed-state permanence, quantum-only newborn
outputs, inaccessible hidden labels or a model outside ordinary quantum
instruments. It is the explicit operational bridge, not mobility alone,
that carries this obligation.

The higher-dimensional constructions certify probability kernels. In
particular, the qutrit construction has not supplied a unitary representation
of the spatial cubic group that acts on its encoded states; the preceding
argument shows that it cannot meet that additional covariance requirement.
The covariant four-dimensional realization remains a disturbed-parent
instrument and does not satisfy exact pure-parent permanence.

The principal consequence is that the new local-curl construction proves
compatibility of specified classical dynamics with kinematic Gauss and
propagating modes, while its particular fourteen-label native law still
needs a nontrivial physical qubit/record bridge. Neither the selected
alphabet nor the rank7 kernel is derived from the four minimal axioms.

### Literature and verification scope

Prepare-and-measure dimension tests are established quantum-information
machinery; see Gallego, Brunner, Hadley and Acin,
[Device-independent tests of classical and quantum dimensions](https://arxiv.org/abs/1010.5064).
The representation in their Eq.(1) and their distinction between uncorrelated
devices and shared preparation/measurement randomness were inspected. This
note uses the former representation and a nonlinear rank argument; it does
not import a device-independent bound valid under all shared resources.
The exact kernel and approximation constants above are this campaign's
application of that machinery, with no novelty claim for the general method.

`fourteen_label_quantum_check.py` checks all196 probabilities of both positive
carrier constructions, the rank/eigenspaces, a natural-encoding minimax
primal witness and reduced dual identity. Nine unrestricted qubit POVM
programs use all fourteen independent effects and reproduce (7); they do not
force cubic covariance or solve the variable-input-encoding optimization.
The full results, feasibility residuals and source identity are retained in
FOURTEEN_LABEL_QUANTUM_RESULTS.json. Numerical optima supplement the proof;
they do not establish the physical bridge or an independent review.

## Part C. A one-qubit-compatible change of birth kernel

2026-09-21. Primary conditional construction, with completed selective independent review.
This changes the supplied birth kernel, retaining the previous immutable
classical exchange process. It is not the original rank7 law.

The quantum-interface obstruction suggests a constructive alternative.
Define a single Bloch feature s_a=e_a on A-axis labels and s_a=b_a/sqrt(3)
on B-cube labels, and choose

    W_ab=1+j s_a dot s_b,      0<|j|<1,
    birth rate(a at x)=(beta/N) product_(y nearest x)W_(a,eta_y),
    W_a0=1.                                                  (1)

Every W is positive and each single-parent column sums to14. For physical
parent preparations rho_b=(I+s_b dot sigma)/2, the POVM
E_a=(I+j s_a dot sigma)/14 reproduces W_ab/14 exactly. For k unknown
independent quantum parents, positive rate effects

    F_a=(beta/N) tensor_(r=1)^k(I+j s_a dot sigma_r)           (2)

reproduce all the product rates. A sufficiently short observed event
instrument can use sqrt(dt F_a), with no-event sqrt(I-dt sum_a F_a).
This is a positive one-event quantum interface; it disturbs parents and
does not establish the repeated classical waiting law or permanent unknown
physical parent states. Neither the formation clock nor j is selected.

The fourteen unit Bloch vectors obey sum_a s_a=0 and
sum_a s_a s_a^T=(14/3)I. Their equal input ensemble is a qubit projective
two-design at the order needed for average operation fidelity. The same
Kraus trace argument as the earlier six-axis interface therefore gives the
sharp parent-preservation fidelity, averaged over these fourteen inputs,

    F_max=(2+sqrt(1-j^2))/3.                               (2a)

The square-root effects attain it. Exact pure-parent preservation is
impossible for j!=0 in this specified ordinary quantum interface. This
single-operation optimum does not describe a repeated-event physical law.

Use the same raw moment fields X=sum p_a e_a,Y=sum p_a b_a,U=2X,V=Y.
The conditional product-replacement reaction law is now

    B_a=beta p0[1+j s_a dot (X+Y/sqrt(3))]^6.                (3)

At p_a=rho/14 the trajectory is still rho'=14beta(1-rho).
The exchange Maxwell coefficient remains c=2gamma rho/7. Put h=beta j(1-rho).
The complete vector reaction and exchange linearization is

    partial_t (U,V) = c(curl V,-curl U)
                   +4h [[3,2sqrt(3)],[2sqrt(3),4]] (U,V).   (4)

The density reaction eigenvalue is -14beta. The orbit difference, two A
quadrupoles, three B pair characters and B triple character retain zero
linear reaction. Thus all fourteen occupied species directions are still
accounted for; there is no removal of their readable degrees of freedom.

The reaction matrix in (4) has eigenvalues28h and0. Its driven combination
is P=(sqrt(3)U+2V)/sqrt(7); its undriven orthogonal combination can be
Q=(-2U+sqrt(3)V)/sqrt(7). This constant two-field rotation leaves the
antisymmetric curl coupling unchanged. Longitudinal raw components have
reaction eigenvalues28h and0. At a frozen background, each transverse
helicity has the two drift eigenvalues

    14h +/- sqrt((14h)^2-c^2|K|^2).                        (5)

Consequently complex oscillatory instantaneous modes remain when
c|K|>14|h|. At long wavelengths during active formation these frozen
eigenvalues are real. At saturation h=0 and the previous pure wave
frequencies return. With the actual time-dependent rho(t), matrices at
different times generally fail to commute, so (5) is not an integrated
phase formula or a global stability theorem. The finite-time matrix ODE
has to be solved with its time ordering retained.

There is nevertheless a controlled late-time statement about that matrix
ODE. The exchange block is anti-Hermitian in the U,V norm, while the
reaction block has eigenvalues28h and0. For any Fourier solution F(t),

    1 <= ||F(t)||/||F(s)|| <= exp[2j(rho(t)-rho(s))]       (6)

when j>0; for j<0 the same interval is reversed, with
exp[2j(rho(t)-rho(s))] <= the ratio <=1. The integral used here is
integral_s^t28h=2j(rho(t)-rho(s)). Thus transient amplification or damping
is finite even when frozen long-wavelength eigenvalues are real.

Let L_infinity be the pure exchange block at c_infinity=2gamma/7. The
coefficient remainder has the integrable norm bound

    ||L(t)-L_infinity||
      <=v0 exp(-14beta t)[28beta|j|+|c_infinity||K|].       (7)

The interaction-picture field Z(t)=exp(-L_infinity t)F(t) satisfies an ODE
with integrable coefficients and remains bounded by (6). Its integral
equation is Cauchy as t tends to infinity. The same argument for the inverse
fundamental matrix, or Liouville's determinant formula with finite integrated
trace, shows that its limiting linear map is invertible. Consequently every
fixed mode has a finite asymptotic free-wave amplitude Z_infinity, with

    F(t)=exp(L_infinity t)[Z_infinity+O(exp(-14beta t))].   (8)

The constant depends on the fixed mode and parameters. The longitudinal
zero-frequency parts are included; the transverse part oscillates at
|c_infinity||K|. This is a finite-dimensional linear scattering statement,
not a native stochastic fluctuation theorem or a spatial ultraviolet limit.

The curl readouts E=d cross V,B=-d cross U still have exact microscopic
Gauss identities for every event. Their linear reactions are obtained by
applying these curls to (4), with the corresponding fixed change of basis;
no claim that they obey the earlier equal scalar-gain formula is made.

There is a symmetry cost to this deformation under the previous full
polar/axial convention. A cross-orbit term e_A dot b_B/sqrt(3) changes sign
under an improper spatial rotation, since e is polar and b axial. It is
nonzero, for example for e_A=e_x and b_B=(1,1,1). Thus (1) is covariant
under all24 proper cubic rotations, but not under the48-element extension
used for the original law. The minimal axioms ask for the former; any
physical parity requirement is an additional obligation here. A handed
coupling, a different encoding, or a larger carrier changes that question.

This deformation demonstrates that the original rank7 mismatch belongs
to a specific supplied kernel. Positive one-qubit event rates and a
nontrivial classical propagating sector can coexist after changing that
kernel. Exact unknown-parent permanence, repeated quantum histories,
state selection, physical symmetry and field identification remain open.

Because (1) remains strictly positive and has the same equal-label
homogeneous trajectory, the conditional entropy extension and monotone
count argument of the local-curl note apply with these new weights as well.
From a fixed interior equal-label product start, in the same ordered
t->infinity at finite N followed by N->infinity limit, the selected full
occupancy law is again locally product. Its scaled-curl covariance is again
(4/7)(|K|^2I-KK^T). The changed quantum event interface therefore does not
by itself produce either of the desired correlated comparator states.

## Reproduction and remaining physical obligations

The runner and byte-bound evidence are described in
[the evidence README](../.claude/science/mobile-record-local-curl-quantum-20260921/README.md).
Exact algebra, numerical POVM optimization and finite time-ordered ODE
controls are labeled separately. Independent proofs/checks are sealed
before their respective author-code comparison; neither those seals nor
the author controls are formal audit verdicts.

The desired long-range state, microscopic operational carrier, repeated
unknown-parent permanence, native stochastic fluctuation limit, continuum
quantum dynamics, Lorentz symmetry and gravity are not established here.
They are open questions, not an asserted set of independent impossibility
theorems. No fraction of TOE completion follows from this packet.
