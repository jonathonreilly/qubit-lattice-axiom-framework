---
claim_id: actual_input_energy_and_original_mark_power_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Conditional actual input mean-energy increment and selected original-mark adjoint-dissipator power for a supplied charged preparation. Low-reference-band bounds and explicit counterexample; no photon absorption, finite laboratory error or empirical agreement."
upstream_dependencies:
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - weak_field_wave_packets_from_mobile_record_dynamics_bounded_theorem_note_2026-09-24
  - original_record_calibration_and_prepared_matter_probe_bounded_theorem_note_2026-09-24
  - prepared_original_record_probe_energy_vacuum_response_and_clock_scope_bounded_theorem_note_2026-09-24
  - photon_dispersion_observational_constraints_and_live_formation_response_bounded_theorem_note_2026-09-24
  - optical_reference_energy_limits_for_original_record_counts_bounded_theorem_note_2026-09-24
runner: scripts/actual_input_energy_and_original_mark_power_2026_09_25.py
---

**Type:** bounded_theorem
**Status:** conditional mathematics with independent PRE and released-source POST checks; no retained audit verdict.

# Actual input energy and original formation-mark power

A response to a reference oscillator excitation does not establish photon
absorption. For the same charged preparation and full supplied matter/field
law, this unit computes two previously distinct missing quantities: the
actual input mean-energy increment, and one original mark's contribution to
the ordinary mean-energy derivative, including its anticommutator term.

An unrestricted bright reference excitation can lower the full input mean.
A hard low-reference band instead gives a quantitative positive mean-energy
bridge. The selected mark has a positive limiting energy-power baseline on
the charged reference vacuum, with a separately bounded low-band excess.
These are initial-state results. The charged vacuum is not the full ground
state, and the generator has no derived energy-conserving reservoir ledger
here. No transition line, photon identity, preparation work, heat, absorption,
physical detector calibration or observed agreement follows.

The original formation instrument, actual output matter, occupied-B electric
gates and harmonic Haar average are retained. Fixed-graph limits and their
compact-packet domains are essential. Static band bounds do not certify a
simultaneous physical-volume or laboratory-time limit. The six-site example
cannot form a second pair and is not the construction used here.

The exact mathematical parents are
[local pair form and general graph magnetic dynamics](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[local compensation common field record limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[weak field wave packets from mobile record dynamics](WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[original record calibration and prepared matter probe](ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
The preceding [probe energy and clock scope](PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[conditional photon timing bridge](PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md) and
[optical reference restrictions](OPTICAL_REFERENCE_ENERGY_LIMITS_FOR_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md) retain
their own premise and observational distinctions. Equation numbering is local
to each part. The optional optical substitution in Part A is conditional
on those separate physical identifications.

## A. Actual input mean-energy increment

### 1. The missing identification tested here

The earlier optical-band analysis constrains REFERENCE oscillator energies.
A charged preparation is not an eigenstate or ground state of the full law.
We now compute the actual full-Hamiltonian mean increment between its supplied
one-reference-excitation and vacuum preparations. This does not measure an
implemented preparation's work or any postclick energy transfer.

Use the exact preparation of PR9143 (note SHA
14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b):
all A plus except d=(1,1,0),h=(2,2,0) minus, three B blockers at
(0,-1,0),(0,0,1),(0,0,-1) plus, and one further B plus at c=(1,0,0)
or e=(0,1,0). Its Gauss-consistent embedding is
J_-=(|m_c>V_com U_dc^-1-|m_e>V_com U_de^-1)/sqrt(2).
Use the same fixed common integer flow V_com in both arms and keep

    h_g=(g²/(2tau)) D+(1/(4tau g²)) H4,
    H4=-2 sum_{a<c, sharing a B neighbor} (F_c F_a P)* F_c F_a P.

The electric D, all original marks and actual postformation matter sectors
are retained. We evaluate input expectations, not a restricted evolution.
Let phi_0,g and phi_1,g be the normalized compact vacuum and one-particle
packets of the weak-field parent, with real eigenbasis f_r and

    Omega_r=sqrt(lambda_r),  sum |alpha_r|²=1,
    mu=sum |alpha_r|² Omega_r >0,
    d_zr=(z.f_r)/sqrt(2 Omega_r), chi_z=sum alpha_r d_zr.

The dimensionless reference energy is mu; in the chosen generator units
its frequency is mu/tau. An SI energy interpretation would add hbar.
Fix an even cubic torus L>=16. Take g->0 at each fixed L, tau and alpha.
All error constants below may depend on that graph and preparation.

### 2. Exact local magnetic compression

Let H4_empty be the all-A-plus, B-empty field block. The following is an
operator identity for angle multiplication on the initial field sector:

    J_-* H4 J_- - H4_empty = F(A),
    F(A)=4722 + sum_{z!=0} a_z exp(i z.A).                    (1)

There are 140 nonzero words, with a_z=a_-z>0. Every word is a contractible
integer circulation. The exact finite certificate has this distribution:

| a_z | number of oriented words | plaquette filling area l_z |
|---:|---:|---:|
| 1 | 22 | 1 |
| 1 | 6 | 2 |
| 2 | 110 | 1 |
| 85 | 2 | 1 |

The two coefficient85 words are the original probe plaquette p and -p.
Consequently sum a_z=418, F(0)=5140, and

    sum a_z l_z² = 436.                                    (2)

Every listed filling is an exact signed sum of elementary plaquette rows;
its area is its coefficient l1 norm, not a Euclidean area approximation.
The complete word and filling certificates are saved. Both sides8 and16
were evaluated; after unwrapping, their local polynomials agree exactly.
Only L>=16 is used in the stated uniform local construction.

Here is the exhaustive finite-algebra rule underlying the certificate.
For each unordered overlapping pair x,z, apply the two actual outward
hard-core hops F_x then F_z. A charge q leaving A along its stored A-to-B
edge contributes that edge's exponent -q. Carry each initial branch string
and its sign, group final matter words, and square their Laurent amplitudes.
The prepared contribution to H4 is minus that polynomial, because -2 is
multiplied by the preparation's normalization1/2. Subtracting the empty
block adds twice the corresponding empty-input norm polynomial. This is
exactly the pair form, and keeps interference only between identical final
matter words. No replacement of distinct outputs by coherent amplitudes
is made.

A pair contributes a difference only if an A center is one of the two
minus sites or its B neighborhood meets an occupied B site of either
branch. Otherwise it acts identically on both matter branches, its two
output matter families remain distinct, and its norm equals the empty
block. There are266 pairs in this active union. Their finite neighborhoods
can be unfolded inside [-5,6]^3; the vertices remain distinct for L>=16,
and all contributing paths use the same local adjacencies as the explicit
side16 certificate. Remote pairs cancel exactly, not approximately. This
establishes the same polynomial for all the stated sizes. The side8 control
is a separate finite check, not the proof of arbitrary-volume locality.

Divergence cancellation, conjugate coefficients, word lengths <=6, the
flat sum5140 and all filling equalities are checked with integer arithmetic.
Since6<L, these circulations have no harmonic winding. Initial zero electric
winding entails Haar harmonic-angle averaging; (1) survives that average.
We do not replace the full charged dynamics or its postbirth winding sectors
by zero angles. The prior flat coefficient5140 is a consistency control for
(1), not a derivation of its nonconstant coefficients.

### 3. Actual full-energy difference

Define the actual input mean difference

    Delta_g=<J_-phi_1,g,h_g J_-phi_1,g>
                 -<J_-phi_0,g,h_g J_-phi_0,g>.

The parent electric term is

    D=sum_{a in A,b~a} 1_{q_b=0} E_ab(E_ab-q_a).

Its EMPTY-B restriction can be reduced using Gauss, but that reduction is
not the full postformation D. In our two branches, let w_e be the probability
that edge e's B endpoint is occupied. It is1 on the18 edges touching the
three fixed blockers and1/2 on the12 edges touching c or e, and0 elsewhere.
Thus sum_e w_e=24. J_-* D J_- is the branch average of the corresponding
quadratic operators with their fixed integer-flow shifts s_c,s_e. Matter
orthogonality removes cross terms. The constants cancel between the two
preparations; all linear electric expectations vanish by oscillator parity,
up to exponentially small compact cutoff corrections, also for complex alpha.

Put xi_e=sum_r alpha_r f_re sqrt(Omega_r/2). The one-particle minus vacuum
rescaled electric variance on that edge is2|xi_e|². Therefore the actual
electric mean increment tends to

    (1/tau)[mu/2 - sum_e w_e |xi_e|²].

The occupancy factor is indispensable. A pre-seal draft mistakenly used
the all-B-empty electric form here. Its note, controls and outputs are
preserved under history/pre-electric-occupancy-correction and explicitly
superseded. The error was found by rereading the exact parent equation(5),
before independent disclosure or any publication.

For any contractible circulation z, Gaussian differentiation gives

    <exp(i g z.x)>_1-<exp(i g z.x)>_0
        =-g² exp(-g² v_z/2) |chi_z|²,
    v_z=sum_r d_zr².                                      (3)

The original initial block has H4_empty=constant-2sum_p(W_p+W_p*).
Because sum_p |chi_p|²=mu/2, its magnetic mean difference tends to
mu/(2tau). Inserting (1) and (3) yields the full result

    Delta_g = (1/tau)[mu - sum_e w_e |xi_e|²
                          - (1/4)sum_{z!=0} a_z |chi_z|²]
                     + O_{L,alpha,tau}(g²).                (4)

The compact normalization and cutoff-derivative corrections are exponential
up to fixed powers of g. Quadratic electric Sobolev moments of the compact
Hermite packets justify the unbounded expectation. Equation(4) does not
follow just from bounded characteristic-function convergence.

All w_e and a_z are nonnegative, so the limiting mean increment is <=mu/tau.
There is no general equality with reference excitation energy.

### 4. An exact failure of the unrestricted photon-energy reading

Take the bright reference packet alpha=d_p/sqrt(v_p), which maximizes the
original selected mark's leading contrast. Then |chi_p|²=v_p,
mu=||c_p||²/(2v_p)=2/v_p, and v_p>=1/sqrt(3). The two coefficient85 words
alone give

    lim tau Delta_g <= 2/v_p-(85/2)v_p
                      <= -73/(2sqrt(3)) <0.                (5)

Thus adding this particular reference one-excitation LOWERS the actual
full mean energy of the supplied charged preparation for sufficiently
small g at fixed graph. This is an analytic counterexample to identifying
every reference creation with a positive-energy full-system photon.
The result concerns the difference between two input means. Adding a scalar
to the Hamiltonian changes neither that difference nor its sign. It establishes
neither an instability of every state nor a violation of conservation in an
energy-conserving completion. The changed reference packet changes the charged
preparation's magnetic energy; no dynamical production protocol is asserted.
The original sealed author's imprecise total-energy wording and the accepted
independent correction are preserved in the evidence history.

The broad preparation mean and variance found in PR9147 remain present.
Their common leading terms do not determine the order-one difference (4).
The corrected Fourier control retains its actual electric-occupancy loss
as well as the magnetic loss; (5), not a floating numerical sign,
certifies the counterexample. This example cannot be advertised as an optical photon.

### 5. A positive low-reference-band mean-energy bridge

The same obstruction becomes small for a truly low-band packet. Suppose
alpha is supported on 0<Omega<=epsilon, 0<epsilon<=2. A nonempty band on the
cubic torus has L epsilon>=4. The integer-momentum cube estimate gives
N_epsilon/V <=27 epsilon³/64. For an elementary plaquette,

    sum_{Omega<=epsilon} d_pr²/Omega_r
      =(1/(2V))sum_{0<D<=epsilon²} D_xy/D
      <=27 epsilon³/128.                                 (6)

Here D=4sum sin²(k_mu/2), D_xy contains its x,y terms. This bound includes
both transverse polarizations with their exact Fourier norm; harmonic zero
modes are absent and the plaquette curl annihilates them.
Weighted Cauchy with mu=sum|alpha|²Omega and a filling of area l_z gives

    |chi_z|² <= mu l_z² (27/128) epsilon³.                 (7)

For clarity, apply weighted Cauchy to chi_z and then the triangle inequality
to the restricted vectors Omega^-1/2 d_p making up d_z. Every plaquette
has the same (6), including different orientations and positions.
For an individual link, weighted Cauchy and the transverse spectral projector
also give

    |xi_e|² <= (mu/2) sum_{band,r}|f_re|²
             <= mu N_epsilon/(2V) <=mu(27/128)epsilon³.

The projector's diagonal at each nonzero momentum is <=1, including the
two polarizations together, not2. Adding its24 occupied-edge weights and
the magnetic weight436/4=109, the actual added mean obeys

    (1-(3591/128)epsilon³) mu/tau
       <= lim_{g->0} Delta_g <= mu/tau.                   (8)

When its lower coefficient is positive, this is a quantitative positive
mean-energy increment near the reference energy. It is NOT a narrow
actual energy distribution, a transition line, invariant photon subspace,
absorption theorem, stable detector or positive-time count law. It compares
two supplied initial states and leaves their large apparatus energy spread.
A hard band is stronger than a mean-energy bound; rare ultraviolet tails
cannot simply be discarded to apply (8).

Only under the same separate physical photon/clock and archival cosmology
identifications as PR9124 would a hard optical ceiling E_lab imply
epsilon<6E_lab/E_QG,min. Equation(8) would then bound this LIMITING relative
mean discrepancy by (3591/128)(6E_lab/E_QG,min)^3. No finite-g error estimate
at the resulting tiny scale, no empirical confirmation and no stronger
statistical interpretation of that observational bound is supplied.

### 6. Scientific controls and scope stress test

The new author program evaluates the full local polynomial from pair norms,
with disclosed reuse of prior vertex/preparation and active-pair logic. It
does not import the earlier flat action certificate as a substitute for
link monomials. A separate program verifies all signed plaquette fillings
and evaluates finite Fourier overlap sums. Those sums are floating controls,
not interval enclosures. Band membership at an exact floating threshold is
diagnostic only; the analytic cube bound supplies the all-size inequality.
The finite-g rows evaluate uncut harmonic compression, not full compact
rotor propagation. All rows, including negative increments, are preserved.

N1: narrow-band photons, collective energy-selective matter, native bound
states, source preparation and other physical identifications remain open.
N2: mean-energy mismatch, broad variance and short-window count limits are
separate facts, not independent universal obstructions. N3: exact charged
preparation, hard reference band, fixed graph before g->0, Haar harmonic
fiber and supplied SI map are explicit. N4: we control full input mean
expectations with their domain, not a reservoir or transition ledger.
N5: (5) is a specific counterexample; it is not a framework no-go. N6: (8)
is the surviving positive low-band mean-energy bridge. N7: actual absorption
requires dynamics and physical source/detector identification beyond an
input expectation. N8: earlier reference count and energy results retain
their stated scopes; this resolves one previously uncomputed identification.
The independent PRE and released-source POST support this conditional result, with the stated energy-zero wording correction. Their optional optical physical identification is outside that independent mathematical check.


## B. Selected original-mark mean-energy power

### 1. Observable and premises

Use the same supplied common matter/field generator and the exact preparation
J_- of PR9143. On an even cubic torus L>=16, all A sites are plus except
d=(1,1,0),h=(2,2,0) minus. Three B plus blockers occupy (0,-1,0),(0,0,1),
(0,0,-1); a fourth is at c=(1,0,0) or e=(0,1,0). The two arms have the
common fixed integer flow V_com and respective U_dc^-1,U_de^-1 factors,
with amplitudes +1/sqrt(2),-1/sqrt(2). Let a=(0,0,0), b=(-1,0,0), and
select either original mark B=B_(a,b,sigma)=P j_(a,b,sigma) F_a P.

The full Hamiltonian in frequency units is

    h_g = K D + delta H4, K=g^2/(2 tau), delta=1/(4 tau g^2),
    D = sum_(x in A,y~x) 1_(q_y=0) E_xy(E_xy-q_x),
    H4 = -2 sum_(x<z, overlapping) S_xz* S_xz,
    S_xz = F_z F_x P.

All matter sectors and the EMPTY-B electric projector are retained. For a
normalized input with both psi and B psi in the domain of D, define this
single channel's power

    P_j(psi)=kappa [<B psi,h_g B psi>
                             - Re <B psi,B h_g psi>].             (1)

This is the adjoint dissipator expectation, including the anticommutator.
The Hamiltonian part contributes zero to the derivative of its own energy.
Other channels contribute their own terms; (1) is not the total flux. It is
not a conditional output mean minus an unconditional input mean, energy per
record, heat, work, or an implemented microscopic reservoir-energy balance.
The declared smooth compact packets and their finite Wilson shifts lie in
the domains of all powers of N_E=1+sum_e E_e^2. D is controlled by N_E there,
so both terms in (1) are defined at every fixed g>0. This does not claim that
finite shifts preserve the full domain of the degenerate occupied-B D for
arbitrary inputs. At fixed g, diagonal D commutes with N_E; bounded finite
shifts are bounded on each N_E graph norm. The interaction-picture expansion
therefore preserves the weighted trace domains. With the extra moments of
these compact packets, differentiating the energy mean at zero gives (1).
Ordinary trace-norm convergence alone would not justify this step.

Let phi_0,g and phi_1,g be the parent's normalized compact transverse vacuum
and one-excitation packets, with fixed finite graph and normalized coefficients
alpha. Write psi_n,g=J_- phi_n,g. Let x=A_transverse/g, Omega_r=sqrt(lambda_r),
and real orthonormal transverse modes f_r. For any contractible circulation z,

    d_zr=(z.f_r)/sqrt(2 Omega_r), chi_z=sum_r alpha_r d_zr,
    v_p=sum_r d_pr^2 >=1/sqrt(3).

Harmonic angles have their required Haar distribution. They are not set to
zero. Contractible circulation observables ignore them; fixed common flow
shifts contribute only bounded constants to electric derivatives.

### 2. Exact magnetic compression with the anticommutator

Suppress V_com, which commutes with every magnetic angle multiplication.
Use the unnormalized two-arm vector v, with integer Laurent amplitudes +1,-1.
Set M=B*B. The magnetic part of (1), divided by kappa delta, is multiplication
by the exact real Laurent polynomial

    C(A)=sum_(x<z) [-||S_xz B v||^2
                                 + Re <S_xz M v,S_xz v>].         (2)

The preparation's factor1/2 and H4's factor-2 cancel. In the second term use
<B v,B H4 v>=<M v,H4 v> before substituting the pair form. Distinct final
matter configurations are orthogonal; only their equal-output amplitudes
interfere. The finite control implements outward charge-q hops with exponent
-q, original creation with exponent sigma, its actual adjoint with -sigma,
then inward charge-q hops with +q. It includes the full B*B action on v.

If the support of S_xz is disjoint from the star of a, S_xz commutes with B
and B*. Its two contributions cancel exactly. The 264 potentially contributing
pairs have centers with unfolded coordinates in [-4,4]^3 and neighborhoods
in [-5,5]^3. These embed without collisions for every L>=16. Thus the side16
enumeration gives the same local polynomial on all stated tori; it does not
approximate a sum of remote terms. The common preparation's endpoints also
lie in this patch. Its common flow cancels from (2) regardless of its routing.

The two signs give the same polynomial. Its 303 terms have constant 2794,
coefficient sum 0 and absolute coefficient sum 6700. All nonzero words are
divergence-free, conjugate-paired, and have length at most 10 (the retained
certificate actually has maximum 8). Since10<L, none winds around the torus.
Every word is preserved by the harmonic Haar average.

Let c_p be the positively oriented xy plaquette row at the origin. The exact
Hessian H=-sum_z C_z z z^T has 520 nonzero entries and c_p^T H c_p=49600.
It factors over integers as

    H=c_p t^T+t c_p^T,
    C(A)=(c_p.A)(t.A)+O(|A|^4).                              (3)

The 67-edge circulation t is recorded in POWER_SPECTRAL_RESULTS.json. All
entries of the matrix identity are checked with Fraction arithmetic. The
factor is recovered without a numerical fit: H c_p/4 minus
c_p(c_p^T H c_p)/32 equals t since ||c_p||^2=4. Its divergence is exactly zero.
Conjugate pairing removes odd powers. C(0)=0 is also consistent with Bv=0
when the original plaquette phase vanishes; the factorization is verified
directly, not inferred from that consistency observation alone.

### 3. Electric contribution and the power limit

The exact selected output is a fixed charge/flow factor times
(W_p-1) phi_n,g/sqrt(2), up to an irrelevant sign and unitary Wilson factor.
Consequently ||B psi_n,g||=O(g), and every first electric derivative of that
vector is O(1): differentiating W_p-1 costs O(1), while differentiating the
packet costs O(g^-1) multiplied by an O(g) factor. Fixed flow derivatives
are bounded. The actual D is a finite sum of quadratic and linear derivatives
with matter-diagonal bounded coefficients, including its occupancy gates.
Thus

    |<B psi,D B psi>|=O(1), ||D psi||=O(g^-2),
    |<B psi,B D psi>| <= ||B psi|| ||B|| ||D psi||=O(g^-1).

Multiplication by K=g^2/(2 tau) makes their contribution to (1) tend to
zero. This argument needs no false replacement of D by sum E^2 after
formation. It establishes O(g) as a sufficient bound; it does not assert a
sharp correction order. Constants depend on the fixed graph and packet.

The finite Laurent expansion, compact Gaussian moment bounds and exponentially
small cutoff errors now give

    lim_(g->0) P_j(psi_0,g) = kappa/(4 tau) C_pt,
    lim_(g->0) [P_j(psi_1,g)-P_j(psi_0,g)]
                         = kappa/(2 tau) Re(conj(chi_p) chi_t),  (4)
    C_pt=sum_r d_pr d_tr.

Here C_pt is the vacuum covariance of c_p.x and t.x. The one-excitation
covariance increment is 2 Re(conj(chi_p) chi_t). This is an instantaneous
effective-generator limit of the supplied input states. It is not a result
for a finite laboratory interval or a microscopic initial derivative, and
it does not discard the full dynamics between subsequent marks.

### 4. A positive baseline proved without a floating sign

The retained exact plaquette certificate is

    t=1550 c_p + sum_q b_q c_q, sum_q |b_q|=646.             (5)

All 32 nonzero integer coefficients and their elementary plaquettes are
listed in POWER_POSITIVE_CERTIFICATE.json. A numerical linear program found
a candidate filling; rational recomposition verifies every one of 525 link
equalities exactly. No optimizer tolerance or optimality conclusion is used
as a proof premise. Translation and cubic symmetry give ||d_q||=sqrt(v_p)
for every elementary plaquette. Cauchy and the triangle inequality therefore
prove

    904 v_p <= C_pt <=2196 v_p.

In particular the selected channel already has strictly positive limiting
energy power on the REFERENCE vacuum charged preparation:

    lim P_j(psi_0,g) >= (226/sqrt(3)) kappa/tau >0            (6)

for kappa>0. This vacuum is not the full charged ground state. Equation(6)
does not measure creation of energy in an isolated closed system: the given
open generator has no derived energy-conserving reservoir completion here.
It shows why treating every selected original mark as absorption of an
incident positive-energy photon is not established by the count formula.

For the unrestricted bright packet alpha=d_p/sqrt(v_p), the excess in (4)
is twice this vacuum contribution and the full one-excitation power limit
is three times it. This is a property of the supplied state, not a detector
quantum efficiency or photon absorption rate. The input mean-energy result in Part A is not used to prove (4).

### 5. Low-band response and the observational limitation

If alpha is supported in 0<Omega<=epsilon<=2, the local Fourier estimate is
v_p,epsilon<=27 epsilon^4/128. It follows by enclosing the centered integer
momenta in a cube: nonempty band implies L epsilon>=4, at most
27 L^3 epsilon^3/64 momenta contribute, each with plaquette weight at most
epsilon/(2 L^3). The two transverse polarizations are already included.
Every elementary plaquette has the same restricted norm. Equations(4),(5)
then imply

    |lim(P_j(psi_1,g)-P_j(psi_0,g))|
          <= kappa/(4 tau) (2196*27/64) epsilon^4,
    |lim(P_j(psi_1,g)-P_j(psi_0,g))|/lim P_j(psi_0,g)
          <= (2196/904)(27 sqrt(3)/64) epsilon^4.             (7)

These are bounds on the limits at fixed graph. A hard band is a stronger
premise than a mean energy ceiling. Nothing here bounds arbitrary rare
high-energy tails by epsilon^4, makes the band invariant under the full
charged dynamics, or supplies a physical finite-g error at tiny optical
scales. The fractional power response and the count response are different
observables; neither is automatically the measured efficiency of an APD.

### 6. Evidence and surviving scope

The root personally wrote the new B/B* pair-form calculation, reviewed its
complete code, exact normalization, support cancellation and all covariance
arguments. Laurent/preparation geometry is explicitly reused from the prior
author controls, not presented as an independent implementation. The Hessian,
integer filling and all eighteen finite Fourier rows were inspected. The
retained side16/32/64 vacuum covariance values are approximately 1245.3524,
1245.3667,1245.3676; these are floating controls, while (6) supplies the sign.
All three programs completed successfully; their actual logs/receipts remain.
The earlier spectral output says the electric proof was pending at execution;
section3 supplies that argument later without rewriting the old output.

N1: native bound matter, collective energy-selective responses, other inputs
and reservoir completions remain open. N2: this single-channel instantaneous
power, input-energy increments, broad energy spread and short-window counts
are separate results. N3: supplied state/law, fixed graph before g->0, exact
occupancy gates and harmonic Haar fiber are explicit. N4: all terms in the
selected adjoint dissipator are kept; the full all-channel ledger is not
computed. N5: no framework no-go or empirical exclusion follows. N6: (7)
retains a quantitative low-band statement while exposing the positive
baseline. N7: actual photon absorption requires a physical source, matter
identification and calibrated count/energy dynamics. N8: earlier output
mean-minus-input estimates do not substitute for (1). The independently sealed
PRE reconstructs the power limit. The separate released-source POST verifies
the complete coefficient and the 525-link filling, and independently checks
the all-volume positivity and hard-band arguments. It confirms the sufficient
smooth-packet domain statement above. No audit verdict is applied.

## C. Evidence and comparison scope

The primary runner transparently reuses the five exact root source programs,
copied byte-for-byte into an isolated temporary execution directory. It runs
each stage freshly in dependency order, preserving the complete polynomial,
filling and finite Fourier outputs together with actual execution bindings.
These are algebraic and uncut harmonic controls, not compact rotor trajectories,
interval enclosures, laboratory predictions or an empirical fit.

Part A has a blind independent PRE and separate released-source POST. The
independent construction retains the occupied-B electric mask, matches the
entire magnetic polynomial and supplies a separate FFT evaluation. Its own
different negative-energy-increment witness and sharper band bound are
independent PRE additions, not retroactive root results. The root's initial
incorrect empty-B electric reduction and both generations of results remain
preserved. The accepted total-energy wording correction is applied above.

Part B has a blind independent PRE and separate released-source POST, with
exact Laurent and separately written matrix-jet reconstructions and a full
small-torus matrix control. Its
sign-indefinite excess-power result and side-six topology correction retain
their independent provenance. The root's all-volume plaquette certificate
was checked exactly after release against the independent PRE vector, using
a separately written plaquette-boundary construction. The positive baseline
and hard-band proofs were checked in that POST phase. The independent L16
Fourier control agrees; the L32/L64 author tables were inspected, without a
new independent evaluation of those sums. Neither checker executed an author
program. The domain precision repair is sufficient for the declared packets;
the POST also supplies a specific original-B domain argument, which is not
needed as an additional premise here.
No finite-spin initial derivative is inferred: bare microscopic P inputs have
j_S P=0, so convergence to a nonzero effective power cannot be transferred by
an unproved derivative/limit interchange.

The one-channel instantaneous power is not a total energy ledger. Counting
statistics, input energy, conditional output energy and the full adjoint
dissipator are kept distinct. The physical source, stable matter response,
scale calibration and finite laboratory errors remain open. The results do
not claim TOE completion, empirical confirmation, exclusion, or an audit verdict.
