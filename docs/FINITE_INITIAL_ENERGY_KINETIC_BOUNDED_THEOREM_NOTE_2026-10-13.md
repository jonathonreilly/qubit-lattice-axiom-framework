---
title: "Single-time kinetic energy laws for fixed normal initial states"
claim_id: finite_initial_energy_kinetic_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
runner: scripts/initial_state_kinetic_identity_2026_10_13.py
upstream_dependencies:
  - modulated_kinetic_energy_bounded_theorem_note_2026-10-13
  - general_compact_control_kinetic_energy_bounded_theorem_note_2026-10-13
  - two_zero_kinetic_energy_bounded_theorem_note_2026-10-13
  - kinetic_correlation_limits_bounded_theorem_note_2026-10-13
assembly_status: publication_prepared_root_review_and_runtime_pending
scientific_execution: none_in_publication_preparation
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: "Supplied massive free CAR model, fixed normal input, fixed smooth real controls and carrier above threshold, bounded kinetic and BV resources; finite input energy separately for mean/W1; explicit actual-cell premises."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Unchanged conditional analytic cores, separately derived and source-exposed checked; source identity is not a mathematical certificate."
next_trace_action: "Root reviews and executes exact source integration; cumulative current-main validation and independent retained audit remain separate. Downstream consumer not yet selected."
audit_required_before_effective_retained: true
bare_retained_allowed: false
dependency_resolution: exact_published_parent_core_maps
---

# Single-time kinetic energy laws for fixed normal initial states

Claim type: bounded_theorem

Claim status: conditional-support. This note preserves two accepted analytic cores with their exact hypotheses. It adds publication metadata, an explicit notation dictionary and exact source/dependency maps. It supplies no retained-audit, formal Lean, model-diverse or empirical verdict.

## Target and quantifiers

For each fixed normal initial density matrix in the supplied massive free CAR/Fock model, the single-time free-energy law approaches its initial law convolved with the vacuum kinetic Poisson comparison; finite initial free energy separately yields additive mean convergence and W1 convergence.

Fix m,v>0, real compact smooth spatial slots, carrier omega>2m, and finite bounds on kinetic horizon, envelope supremum and total variation. The real BV envelope and terminal time may vary with h=|lambda|. With J_h=lambda^2 integral_0^T A(t)^2dt, the comparison law is the initial energy law convolved with omega times Poisson(nu_omega J_h). Weak convergence to a single limiting law is asserted along convergent J_h; the characteristic-function comparison and finite-energy W1 comparison retain the current J_h. Drive uniformity is for each fixed rho, which is independent of coupling, terminal time and envelope. No W1 rate or multi-time process follows.

The weak-law theorem needs normality but no energy moment. The mean/W1 theorem needs finite initial free energy, treats arbitrary nonquasifree states and keeps anomalous covariance. The separate zero-anomalous subclass has the stated uniform mean control. The explicit inverse-vacuum and two-particle families vary with the drive and delimit uniform extensions over energy-bounded input classes at positive production; they do not contradict any fixed-state theorem.

Zero envelope, zero pair-production rate and bounded kinetic windows including T=0 remain included. The positive-production hypothesis belongs to the uniformity counterexamples. The proof does not establish threshold, massless, high-variation, changing spatial-slot, physical state-selection or trajectory limits.

## Proof obligations, imports and notation

The obligation graph is explicit: modulated464 supplies the vacuum law/mean and weighted full-input remainder; general470 supplies signed Born/pair-density machinery; corrected859 supplies the CAR pictures, skew graph and energy-domain conventions; correlation335 supplies the older fixed-test topology machinery. The new cores prove the weighted full operator estimate, arbitrary-state covariance/energy identity, echo argument, compact-test extensions and conditional initial-state transfer. These are ordinary conditional analytic results, not cited retained authorities. All four directly used canonical parents and five exact core maps are in the [parent bindings](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/PARENT_BINDINGS.json). Mean301 is transitive support under the general-control owner. No chirp theorem is imported.

Part A is root407 lines9-383; Part B is independent224 lines20-216. Full originals and omitted historical status sections remain recoverable from the [source archive](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/SOURCE_RECOVERY.md). Full-source digests are different from extracted-core digests. The [publication map](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/PUBLICATION_EDITS.json) identifies both.

Part B's U is Part A's Y, and its H is H0. Its field F is b in Part A. The generalized densities obey Q=I-C, n_B=N_A and kappa_B=-kappa_A; this accounts for the opposite anomalous-term signs. The bare C in Part B's pair graph is the scalar-band conjugation from corrected859, distinct from C_rho. J_real=Gamma C is distinct from J_h.

Part A's exact trace-distance identity applies only to pure initial states. Part B adds an asymptotic result for each fixed normal mixed state, not an exact finite-coupling mixed-state identity or a state-uniform limit. Its full-picture compact statement uses the additional uniform freely rotated creator-word lemma, not an illicit moving compact test in Part A. Finite-mode statements are for finite-rank detectors with their stated rank dependence; a continuum spatial region or energy band is not automatically finite rank. A vacuum-based necessary detector-rank bound is retained only for initially empty modes.

## Explicit actual-cell hypotheses

The actual-cell application assumes an exact common free energy and embedding, all required M23 calibration bounds, and weighted trace convergence ||(H+I)^(1/2)(rho_a-rho)(H+I)^(1/2)||_1 -> 0 to one fixed finite-energy rho. M23 supplies bounds ||V_a-V||<=d0 epsilon_a, ||[H,V_a-V]||<=d1 epsilon_a and the stated uniform individual commutator bound; the parent also states its one-particle-generator comparison. With fixed resources, epsilon_a=o(h^2) is sufficient for the mean/law/W1 transfer. The weaker unweighted scale alone supplies no mean conclusion. An energy cap or convergence of initial energy distributions does not supply weighted trace convergence.

No missing theorem lemma is asserted within the supplied model and stated hypotheses. The strongest open physical-application obligation is to establish the actual common-energy/calibration and weighted preparation hypotheses for the desired realization; this package proves no preparation rate or model selection. They remain assumptions rather than new scientific parent claims.

## Review record and negative scope

The root derivation froze before its author opened the independent findings. The later focused comparison resolves the covariance dictionary, weighted domains, exact pure versus asymptotic mixed distance, and two-particle (one-pair) counterexample. It is source-exposed and same-family; the comparison author also wrote Part B. Root's separate proof and complete later checking are distinguished from that self-check. The unchanged original review's phrase "two-pair sector" is a transcription error corrected by its preserved precision note; no formula or acceptance scope changed.

The [N1-N8 checklist](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/NO_GO_DISCIPLINE_CHECKLIST.md) and [ledger](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/NO_GO_LEDGER.md) preserve exact uniformity witnesses and the procedural FAIL/partial-narrowing classification. Only the real families are counted; N1's five-family minimum is unmet. The bounded historical N8 search is recorded with its actual coverage. The proposed identity runner emits honest N5 nonexecution statements, not a mathematical certificate. No packet PASS, exhaustive impossibility or independent-wall count is claimed. Narrowed positive publication is allowed with these missed routes and limitations queued.

The actual regular parent is PR9517 at c5eaa6bf752a0893c83c0509c7c349dab53bff14. The former provisional wrapper remains archived. No prior source is rewritten. All new source integration, staging and publication remain root-owned; later combined validation and independent retained audit remain separate.

## Part A — unchanged root mathematical core

This complete selected core preserves I23's pure-state scope and section8's conditional application.

<!-- BEGIN EXACT CORE root407:9-383 -->
## 1. Model, inputs and statement

Use the supplied massive free CAR model and conventions of modulated464.
On K=L2(R;C2), D=-vp sigma_x-m sigma_y, E=(D^2)^(1/2)>=m>0,
P=(1+D/E)/2, P_-=I-P, and Gamma conjugates/reflections so
Gamma P Gamma=P_- and Gamma E Gamma=E. Put h_+=PK,
H0=dGamma(E|h_+) on fermionic Fock space F, with vacuum Omega.
Inner products are linear in the second slot. Annihilation is antilinear.
The fixed compact smooth real spatial slots f,g and centered even quadratic
control V are exactly those in modulated464. The state representation,
mass, velocity, control and fixed carrier omega>2m are supplied premises.

Let h=|lambda|>0, T<=tau_star/h^2, and c(t)=A(t)cos(omega t),
where A is real BV on [0,T], ||A||_infinity<=A_star and
Var(A)<=V_star. All displayed resources and spatial slots are fixed;
A and T may vary with h. Define

    J=h^2 integral_0^T A(t)^2dt,
    eta_h=sqrt(h log(2+h^-2)),
    nu=(pi/2)r(omega)>=0.                              (I1)

Here r is the exact pair density of general470/modulated464. Let W be the
full Fock propagator for H0+lambda c(t)V, Y=exp(itH0)W the interaction
representative, and Z its real unitary one-particle map, initially I.
The corrected convention is Y*gamma(k)Y=gamma(Z*k). Full and interaction
states have the same H0 spectral law, for every initial state.

The already checked modulated464 results supply, uniformly over this class,

    ||Z-I||<=C eta_h,
    ||E^(q/2)(Z-I-K1)||_HS<=C_q eta_h, q>=0 fixed,
    beta=PZP_-,  ||E^(1/2)beta||_HS<=C,
    M_vac:=Tr(E beta beta*)=omega nu J+O(eta_h),
    chi_vac(s)=exp(nu J(exp(is omega)-1))+O_s(eta_h).   (I2)

K1=-i lambda integral_0^T F_t c(t) M F_t*dt, with the exact F_t,M of464.
The q estimates are full-input estimates, not just off-diagonal estimates.
The scalar errors and constants refer to each fixed Fourier variable s.

For every fixed normal density matrix rho on F, write mu_rho for its H0
spectral law and mu_h,rho for that of W rho W*=exp(-iTH0)Y rho Y*exp(iTH0).
If J->J0, the claimed weak limit is

    mu_h,rho => mu_rho * Law(omega Pois(nu J0)).         (I3)

This weak statement requires no finite initial moment. If
M_rho=Tr(rho H0)<infinity, the additional claims are

    Tr(Y rho Y* H0)=M_rho+omega nu J+o_rho(1),
    sup_(A,T) W1(mu_h,rho,
                  mu_rho * Law(omega Pois(nu J))) ->0. (I4)

The mean error and W1 convergence are uniform over the fixed drive-resource
class for this fixed rho. No quantitative rate for them is asserted. These
are single-time final-energy laws. Convolution does not establish an
independent-increment process, joint energy measurements, or a two-time
work distribution. No uniformity over all energy-bounded initial states
is being asserted. A precise sufficient condition for varying actual-cell
initial states is given in section8.

## 2. A weighted full operator estimate

The proof needs a strengthening of the unweighted operator part of(I2):

    ||E^(q/2)(Z-I)||<=C_q eta_h, q>=0 fixed.             (I5)

This does not follow merely by multiplying ||Z-I|| by an unbounded energy.
We derive it from the same complete near/far decomposition as464.

Choose 0<a<(omega-2m)/2 and let Pi_n=1_(E<=m+a), Pi_f=I-Pi_n;
both commute with D,E,P. For S_q z=integral_0^T E^(q/2)F_t z(t)dt,
the checked threshold synthesis bound gives ||Pi_n S_q||<=C_q(1+T)^1/4.
Indeed E is bounded on Pi_n, and the unweighted threshold bound applies.
The far synthesis estimate is uniform:

    ||Pi_f S_q||_(L2([0,T];C2)->K)<=C_q.               (I6)

To see this directly, extend z by zero to the line and resolve D into its
two signed energy bands. Outside E<=m+a the Jacobian of p->E(p) is bounded
away from its threshold singularity. The matrix density made from
E^(q/2)Fhat(p) is bounded there: at infinity Fhat is Schwartz, and on
compact sets away from p=0 all factors are smooth. Temporal Plancherel
bounds the two band integrals by a fixed multiple of ||z||_2^2. A sharp
spectral cutoff is permitted here; no L1 decay of its time kernel is used.

In E^(q/2)Pi_i K1 Pi_j=-i lambda(Pi_i S_q)cM(Pi_j S_0)*,
any far factor therefore costs at most C_q h(1+T)^1/4, with a better
O(h) bound if both factors are far. The temporal multiplication has
norm at most A_star||M||, with no derivative of A.

For the near-near kernel, each signed energy lies in +-[m,m+a]. After
expanding the cosine, every frequency z has
|z|>=omega-2(m+a)>0. Stieltjes integration by parts, including the two
endpoint traces and every jump, gives

    |integral_0^T A(t)exp(izt)dt|
       <=(2A_star+V_star)/|z|.                         (I7)

The weighted momentum kernel has a square-integrable product majorant:
its output energy is bounded on Pi_n, and the fixed Fhat factors are L2.
Thus the near-near piece has HS, and hence operator, norm O_q(h).
Summing the four pieces shows
||E^(q/2)K1||<=C_q h(1+T)^1/4<=C_q sqrt(h) on the kinetic window
(enlarging the constant for h<=1). The full weighted remainder in(I2)
then proves(I5). Finite-time integrals are first taken in the graph norm;
closedness supplies the bounded extension of E^(q/2)(Z-I) to all of K.
In particular Z preserves Dom(E^(q/2)) for each such fixed q.

## 3. Energy echo and arbitrary normal states

Define the complex-linear self-dual field

    b(k)=a*(Pk)+a(P Gamma k),
    b(k)*=b(Gamma k), {b(f)*,b(g)}=<f,g>I.              (I8)

For real k, gamma(k)=sqrt(2)b(k). The real covariance identity extends
complex linearly to Y*b(k)Y=b(Z*k); ||b(k)||<=||k||. Consequently
||[Y,b(k)]||,||[Y*,b(k)]||<=d_h||k|| with d_h=C eta_h.

For each fixed s put U_s=exp(isH0) and the bounded echo

    R_s=Y*U_s Y U_s*.

Free conjugation rotates b(k) by exp(isD), preserving its slot norm.
The product commutator therefore obeys

    ||[R_s,b(k)]||<=2d_h||k||,
    <Omega,R_s Omega>=chi_vac(s).                     (I9)

The second identity uses U_s*Omega=Omega. It fixes the scalar echo
without choosing an implementer phase for Y.

For completeness, the Fock CAR commutant is scalar. A bounded operator Q
commuting with all b(k) commutes with all a(xi),a*(xi). Its QOmega is in
the common kernel of every a(xi), hence is a scalar vacuum: on each
positive-particle sector, contractions against a complete one-particle
basis can all vanish only for the zero vector. Commuting the creators
then determines Q as that scalar on the dense finite-particle subspace.

On separable Fock space every bounded operator sequence has a weak-operator
convergent subsequence (diagonalize matrix entries on a countable dense
set and use the uniform norm bound). Suppose h_n->0 and J_n->J0.
Every such limit of R_s commutes with all b(k) by(I9), so it is scalar;
its vacuum entry and(I2) force that scalar to be
g_J0(s)=exp(nu J0(exp(is omega)-1)). Thus the entire sequence has this
weak-operator limit. Pairing with a trace-class operator follows by its
finite-rank approximation and the uniform bound ||R_s||=1. Therefore

    Tr(rho Y*U_sY)=Tr(rho R_s U_s)
       ->g_J0(s) Tr(rho U_s).                         (I10)

The product is the characteristic function of the convolution in(I3),
continuous at zero. The characteristic-function criterion proves(I3).
It does not require rho to commute with H0, to be pure, to be even, to
have a finite first moment, or to satisfy Wick factorization.

For each fixed rho,s the characteristic comparison with g_J(s) is uniform
over the drive class: otherwise choose a bad sequence and a subsequence
whose J values converge in the compact interval[0,A_star^2 tau_star].
Equation(I10) contradicts a fixed positive discrepancy. This compactness
argument supplies no error rate or supremum over s or initial states.

## 4. Arbitrary-state covariance and the exact mean decomposition

Define the contraction C_rho on K by

    <f,C_rho g>=Tr(rho b(f)*b(g)).

Positivity and the CAR give 0<=C_rho<=I and
Gamma C_rho Gamma=I-C_rho. These statements hold for every normal state,
not just quasifree ones. On K=h_+ direct_sum P_-K write

    C_rho = [[I-N,kappa],[kappa*,Nbar]],
    Nbar=Gamma N Gamma.                               (I11)

Here <xi,N zeta>=Tr(rho a*(zeta)a(xi)) is the usual occupation operator.
The + block of C_rho-C_rho^2>=0 gives

    kappa kappa*<=N-N^2<=N.                           (I12)

For finite first energy, monotone positive spectral/finite-rank cutoffs in
the number-energy identity yield

    Tr(E N)=M_rho,
    n_rho:=Tr N<=M_rho/m,
    ||kappa||_HS^2<=n_rho,
    ||E^(1/2)kappa||_HS^2<=M_rho.                     (I13)

The last implication follows first with bounded spectral energy cutoffs
from(I12), then by monotone convergence of positive traces. It asserts
a weighted trace ideal, not a pointwise bound on individual matrix entries.

Put A0=PZP:h_+->h_+ and beta=PZP_-:P_-K->h_+. Field covariance gives
C_out=Z C_rho Z*. Taking P(I-C_out)P and using unitarity gives exactly

    N_out=beta beta* +A0 N A0* -beta Nbar beta*
                      -A0 kappa beta* -beta kappa* A0*. (I14)

The first term is the vacuum contribution; the negative occupation term
is the exclusion correction. The two anomalous terms retain their signs
and matrix order. No expansion of a many-body state into a Gaussian is used.

Let K_h=E^(1/2)(A0-I), B_h=E^(1/2)beta, and F_rho=E^(1/2)kappa.
Equations(I2),(I5),(I13) show

    ||K_h||,||B_h||<=delta_h=C eta_h,
    ||B_h||_HS<=C_B,
    E^(1/2)A0 kappa=F_rho+K_h kappa in HS,
    E^(1/2)A0 N^(1/2)=E^(1/2)N^(1/2)+K_h N^(1/2)
                                                       in HS. (I15)

All products in the following exact identity are consequently defined:

 M_out=M_vac+||E^(1/2)A0 N^(1/2)||_HS^2
              -||B_h Nbar^(1/2)||_HS^2
              -2 Re Tr[(F_rho+K_h kappa)B_h*].         (I16)

To justify it without assuming finiteness of the left side, first observe
that every unweighted term in(I14) is trace class: N,Nbar are trace class,
beta,kappa are HS, and A0 is bounded. Replace E by bounded increasing
spectral cutoffs in(I14). The positive normal
and vacuum terms are bounded by(I15), and both cross terms converge in
trace norm through their HS factors. This bounds the nonnegative cutoff
energies and lets monotone convergence identify M_out and(I16). Thus
finite energy is a conclusion of these domain/ideal estimates as well.

## 5. Vanishing coherence correction and mean convergence

For any fixed HS operator F:P_-K->h_+, bounded HS norms and small operator
norms of B_h imply

    Tr(F B_h*) ->0 uniformly over the drive class.     (I17)

Indeed choose a finite-rank F_d with ||F-F_d||_HS small. Then
|Tr(F B_h*)|<=C_B||F-F_d||_HS+delta_h||F_d||_1.
Choose d first, then h. This argument would not justify a moving arbitrary
HS test F_h with only a norm bound. Fixed rho is used precisely here.

Expanding the positive normal square and bounding the other terms in(I16)
gives the explicit estimate

 |M_out-M_vac-M_rho|
   <=2delta_h sqrt(M_rho n_rho)+2delta_h^2 n_rho
       +2C_B delta_h sqrt(n_rho)+2|Tr(F_rho B_h*)|.    (I18)

By(I13),(I17) this is o_rho(1), uniformly over permitted A,T. Combining
with the separately checked vacuum mean in(I2) proves the mean part of(I4).
The anomalous coherence term has been controlled, not set to zero by a
quasifree or gauge-invariant assumption. No universal quantitative rate
for an arbitrary fixed finite-energy rho follows from this approximation.

There is also a uniform relative energy bound for all finite-energy states,
although their limiting error is not asserted uniform:

    M_out<=C(1+M_rho).                                (I19)

Use ||F_rho||_HS<=sqrt(M_rho), n_rho<=M_rho/m and the bounded delta_h,C_B
in(I16), bounding 2sqrt(M_rho) by 1+M_rho. Applying this to normalized
pure states, then scaling, proves the form inequality

    Y* H0 Y <= C(H0+I).                               (I20)

This includes Y Dom(H0^(1/2)) subset Dom(H0^(1/2)). The bounded form
operator obtained by sandwiching with (H0+I)^(-1/2) has norm at most C.

## 6. First moments and Wasserstein-one

Along J->J0 the weak limit(I3) is nonnegative and has mean
M_rho+omega nu J0. Equation(I18) proves convergence to that mean
separately. For nonnegative random variables, weak convergence and these
finite means give uniform integrability: use convergence of min(X,R),
write E(X-R)_+=EX-E min(X,R), and bound
X 1_(X>2R)<=2(X-R)_+. This proves convergence in W1.

For uniform comparison at current J in(I4), a putative bad sequence has
a J-convergent subsequence. On it the exact law converges in W1 to the
corresponding fixed convolution target. The comparison targets also converge
in W1: couple their common initial random variable identically, and couple
the two Poisson variables through an independent Poisson increment. Their
distance is at most omega nu |J-J0|. The triangle inequality contradicts
the bad sequence. This reasoning covers nu=0 and J0=0 without division.

## 7. Correlations, compact tests and pure-state distance

The norm covariance bound directly gives, for any initial normal rho,

 |Tr(rho Y* product_(j=1)^r gamma(k_j)Y)
                  -Tr(rho product_j gamma(k_j))|
       <=r d_h product_j ||k_j||.                    (I21)

This comparison, unlike(I18), is uniform over initial states. It is a
norm estimate for each bounded-resource word. Density of CAR polynomials
extends it to each fixed element O of the norm-closed CAR algebra.
For the full propagator it compares the driven state to the freely evolved
initial state, not generally to the stationary initial state. Indeed the
free rotation replaces each k_j by exp(iTD)k_j without changing its norm;
the same polynomial approximation therefore remains uniform in T.
No uniform supremum over the entire CAR unit ball is established.

There is a different interaction-picture compact-test limit. The operators
Y themselves approximately commute with the CAR. Along any sequence with
J->J0, select a subsequence whose vacuum amplitude a_h=<Omega,Y Omega>
converges to a. Every weak-operator cluster of Y is then aI by the same
commutant argument. Hence Y psi converges weakly to a psi for every fixed
psi. For any compact Fock operator K, compactness makes K Y psi converge
in norm to a K psi. Polarization and trace-class approximation give

    Tr(Y rho Y* K) -> |a|^2 Tr(rho K).                 (I22)

The gap H0>=m off the vacuum makes |a_h|^2 the isolated zero-energy mass
of the vacuum-driven law. Its weak Poisson limit from(I2) yields
|a|^2=exp(-nu J0): use a bounded continuous test equal to1 at0 and0
on[m,infinity). Every possible phase subsequence gives the same squared
modulus. Thus(I22) holds on the full sequence with factor exp(-nu J0).
No phase convergence or strong-vector convergence of Y is claimed.

For a fixed pure state |psi><psi|, the same weak scalar limit gives
|<psi,Y psi>|^2->exp(-nu J0), and the exact pure-state identity yields

 ||Y|psi><psi|Y*-|psi><psi|||_1
            ->2sqrt(1-exp(-nu J0)).                   (I23)

These statements require normality but not finite energy. Compact tests,
fixed CAR tests and global trace norm remain different topologies. For
mixed rho no universal exact trace-distance formula is asserted. In the
full picture(I23) compares to the free evolution of psi by unitary invariance.
The fixed compact-test assertion(I22) is in the interaction picture; an
arbitrarily rotating compact test cannot be substituted without a new argument.

## 8. Conditional actual-cell and varying-initial-state application

Retain the exact actual/common free-energy identification and operator
hypotheses M23 of modulated464, with epsilon_a the fixed-resource weighted
calibration error. In particular

 ||V_a-V||<=d0 epsilon_a,
 ||[H0,V_a-V]||<=d1 epsilon_a,
 ||[H0,V_a]||,||[H0,V]||<=k1.                          (I24)

Suppose embedded actual band density matrices rho_a are normalized and obey

 delta_a=||(H0+I)^(1/2)(rho_a-rho)(H0+I)^(1/2)||_1->0 (I25)

for a fixed finite-energy rho. This weighted trace condition is an explicit
initial-state premise, not a consequence of the control-slot calibration.
Let B(T)=integral_0^T |lambda c(t)|dt<=A_star tau_star/h.
Bounded-perturbation Duhamel and the separate commutator work identity give,
for the same initial rho_a on both sides,

 ||Y_a rho_a Y_a*-Y rho_a Y*||_1<=2d0 epsilon_a B(T),
 |M_a(rho_a)-M(rho_a)|
      <=epsilon_a[d1 B(T)+k1 d0 B(T)^2].               (I26)

These are valid for normal mixed states: Duhamel is an operator estimate;
subtract the work identities with the same initial energy, use the bounded
commutators, and integrate 2 k1 d0 epsilon_a |lambda c(t)|B(t).
Its integral is k1 d0 epsilon_a B(T)^2. Energy cutoffs justify the work
identity at finite first energy; no unbounded energy is bounded by trace
distance. BV jumps do not produce a derivative of A in this free-energy work.

The change of initial state costs at most delta_a in trace distance and,
by the bounded sandwich operator from(I20), at most C delta_a in mean.
Explicitly apply trace duality to (H0+I)^(1/2)(rho_a-rho)(H0+I)^(1/2).
Thus epsilon_a=o(h^2) together with(I25) transfers(I3),(I4) to the actual
states, including uniformity over drive resources. The weaker epsilon_a=o(h)
controls only the unweighted comparison by these estimates.

Condition(I25) is attainable as a Hilbert-space approximation when the
actual band Fock projections Q_a commute with H0 and converge strongly to I:
take rho_a=Q_a rho Q_a/Tr(Q_a rho). Since (H0+I)^(1/2)rho(H0+I)^(1/2)
is trace class, strong projection convergence gives trace-norm convergence
of its Q_a compressions; normalization tends to1. This proves(I25) under
those stated projection hypotheses. Physical preparation of these band
states or any rate for their approximation is not supplied here. Exact
identification with an actual model must still satisfy the upstream premises.
<!-- END EXACT CORE root407:9-383 -->

## Part B — unchanged independent mathematical core and extensions

This companion core supplies alternative proofs and the additional topology/finite-mode results at their own stated scope. Its definition of fixed rho excludes dependence on coupling, terminal time or envelope. Its inverse-vacuum and normalized two-particle constructions deliberately vary with the drive; they do not contradict the fixed-state positive theorem. Its claims (1)-(2) denote weighted estimates and are distinct from Part A's I-numbered equations.

<!-- BEGIN EXACT CORE independent224:20-216 -->
Use the supplied Fock space over h=PK, H=dGamma(E), N=dGamma(I), vacuum Omega and H>=mN. Write U=Y(T), U0(T)=exp(-iTH), W=U0(T)U, and let Z be the interaction one-particle map. The model, fixed real compact smooth spatial slots, omega>2m, bounded kinetic horizon and fixed amplitude/total-variation resources are exactly those of464. Set

    h_lambda=|lambda|, eta_h=sqrt(h_lambda log(2+h_lambda^-2)),
    J_h=lambda^2 integral_0^T A(t)^2dt,
    nu=(pi/2)r(omega), Pi_J=Law(omega Poisson(nu J)).

A normal state here is a positive trace-class density matrix rho of trace one in this supplied Fock representation. It need not be quasifree, number diagonal or finitely supported in particle number. Fixed means independent of lambda, T and the envelope. Nonnormal thermodynamic states are outside the statement. Let mu_rho be its initial H law, and mu_out the H law in W rho W* (the interaction state has the same H law for every rho).

The proved conclusions are:

1. For every fixed normal rho and every sequence J_h->J, `mu_out -> mu_rho * Pi_J` weakly. Comparison with `mu_rho * Pi_(J_h)` is uniform over admitted envelopes/times in a metric for weak convergence.
2. If E_rho=Tr(rho H)<infinity, then `Tr(W rho W* H)=E_rho+omega nu J_h+o_rho(1)`, and `W1(mu_out,mu_rho * Pi_(J_h))->0` uniformly over that driving class. No universal rate for arbitrary fixed rho is claimed.
3. Interaction CAR observables return pointwise to their **initial** functional; full-picture observables approach their freely evolved reference. The compact and trace-distance statements in section 6 distinguish these topologies.
4. A common initial-energy bound does not make conclusions 1--2 uniform in rho. Section 7 gives explicit preparations in this exact model showing the failure and a separate uniform-mean class where the mean does survive.

These are single-time statements. The convolution admits abstract independent classical variables as a description of its marginal; it does not establish a joint measurement law, physical independent increments or a process.

## 2. Two weighted estimates needed beyond the vacuum statement

The source's Born near/far proof remains valid after E^(q/2) is placed on its output. Weighted near energies lie in a fixed bounded interval, so their synthesis norm is O_q((1+T)^1/4). The weighted far spectral density is bounded by threshold removal and the Schwartz tails, so temporal Plancherel gives O_q(1). Terms with a far factor therefore cost O_q(h_lambda(1+T)^1/4). The near-near frequency gap is unchanged; its extra output weight is bounded and its weighted HS norm is O_q(h_lambda). Adding M16 proves

    ||E^(q/2)(Z-I)|| <=C_q eta_h.                       (1)

This is an absolute bounded output-weight estimate. Closedness identifies the weighted operator; Z-I maps into the relevant energy domain. The identity `Z*-I=-(Z-I)Z*` gives the same bound for Z*.

Put beta=PZP_- and B1=PK1_A P_-. Its exact scalar Born kernel gives, for every fixed q>=0,

    ||E^(q/2)B1||_HS^2
      <=2lambda^2 integral e^q r(e)|I_A,T(e)|^2de
      <=C_q lambda^2 T.

The last step uses bounded e^q r and temporal Plancherel, not a new secular asymptotic. M16 then gives

    ||E^(q/2)beta||_HS<=C_q.                            (2)

We use q=1 and q=2. In particular E beta is HS uniformly, while its operator norm tends to zero by (1). These two distinct norms are essential to the fixed-state mean argument.

## 3. Bounded CAR argument for the energy law

Define the complex-linear field

    F(k)=a*(Pk)+a(P Gamma k).

It obeys F(Gamma k)=F(k)* and `{F(f),F(g)*}=<g,f>I`, hence ||F(k)||<=||k||. The corrected covariance extends complex-linearly to `U*F(k)U=F(Z*k)`. Thus commutators of U or U* with a(f),a*(f) are bounded by delta_h||f||, where delta_h=C eta_h. Product telescoping gives norm convergence on each fixed CAR polynomial; C*-norm approximation gives it on every fixed CAR observable.

The following elementary lemma also controls matrix elements. If bounded T_h have such commutators with bound epsilon_h||f||, epsilon_h->0, and t_h=<Omega,T_h Omega>, then

    <phi,(T_h-t_h I)psi> ->0                            (3)

for all fixed Fock vectors. For a nonempty creation word v, commute its adjacent annihilator across T_h; it kills Omega and leaves `|<v,T_h Omega>|<=epsilon_h product ||f_j||`. For matrix elements between two creation polynomials, commute T_h past the polynomial on its right, then normal-order the remaining finite CAR product. Its vacuum component gives t_h times the original inner product; every other component has the preceding error. Finite-creation vectors are dense, and uniform boundedness proves (3). All constants for fixed polynomials are uniform under free rotation of their slots.

A separate commutant check reaches the same conclusion: any bounded weak cluster point of T_h-t_h I commutes with all CAR generators. It maps Omega into the joint annihilator kernel, hence into its scalar span, and has that scalar action on the dense creation-polynomial space. Its zero vacuum matrix element forces it to vanish. This checks the representation and excludes an unproved norm-centrality inference.

For each real s define

    K_h(s)=U*exp(isH)U exp(-isH),
    c_h(s)=<Omega,K_h(s)Omega>.

The commutator bound for K_h(s) is 2delta_h||f||, since free conjugation rotates a(f),a*(f) by norm-preserving one-particle unitaries. Its vacuum expectation c_h is exactly the checked vacuum energy characteristic function. Applying (3), then trace-class approximation, gives the correctly ordered identity and limit

    chi_out(s)=Tr(rho U*exp(isH)U)
              =Tr(exp(isH)rho K_h(s)),
    chi_out(s)-c_h(s)Tr(rho exp(isH)) ->0.              (4)

No initial moment or quasifree assumption has entered. The finite-polynomial proof makes the remainder in (4) uniform even over s when c_h(s) is kept exact, because the extra free rotations preserve every approximation norm. The vacuum-to-Poisson approximation is used only at fixed s; no uniform-all-s Poisson claim follows.

Substituting M3 into (4) gives the characteristic function of `mu_rho * Pi_J` whenever J_h->J. It is continuous at zero, so the probability laws converge weakly. For uniform comparison at the current J_h, use its compact range `[0,A_star^2 tau_star]`: any bad sequence has a J_h-convergent subsequence, on which both laws have the same weak limit. This proves assertion 1 without replacing a normal state by a quasifree state or measuring its initial energy first.

## 4. Exact covariance and the unbounded first moment

Use the occupation-order generalized density defined by

    <g,Q_rho f>=Tr(rho F(f)F(g)*).

This convention has Q_vac=P_-, the complement of the vacuum-projection covariance sometimes used in the sources. CAR gives `0<=Q_rho<=I` and `Q_rho+Gamma Q_rho Gamma=I`. In positive/negative blocks,

    Q_rho=[[n,kappa],[kappa*,I-bar(n)]],
    bar(n)=Gamma n Gamma.

Here Tr(n)=Tr(rho N) and Tr(E n)=E_rho. The positive block of `Q-Q^2>=0` gives `kappa kappa*<=n-n^2<=n`, so finite particle expectation makes kappa HS. This is a positivity argument for arbitrary normal states, not Wick factorization.

The exact covariance order is `Q_out=Z Q_rho Z*`. Put A0=PZP. Its positive block is

    n_out=beta beta*+A0 n A0*-beta bar(n)beta*
                         +A0 kappa beta*+beta kappa* A0*.

Assume E_rho<infinity, hence Tr(n)<=E_rho/m. Define

    D_h=A0* E A0-E,
    L_h=(E beta)*A0 : h ->P_-K,

the bounded extension of beta* E A0.

Equation (1) shows that D_h extends boundedly through

    D_h=A0*E(A0-I)+(A0*-I)E,
    ||D_h||<=C eta_h,
    ||beta*E beta||<=C eta_h^2.

Equations (1)--(2) also give `||L_h||_HS<=C` and `||L_h||<=C eta_h`. Passing through bounded energy cutoffs gives the exact finite mean identity

    E_out=E_rho+E_vac+Tr(n D_h)-Tr(bar(n)beta*E beta)
                                   +2 Re Tr(kappa L_h). (5)

Every unbounded passage is controlled. `E^(1/2)A0 n^(1/2)` is HS because it is `E^(1/2)n^(1/2)` plus the bounded `E^(1/2)(A0-I)` times HS n^(1/2). The negative term is bounded-coefficient times trace-class bar(n). For the cross term, `beta*E_R A0 -> beta*E A0` in HS since E beta is HS; pairing with kappa is legitimate. Monotone convergence on the positive n_out identifies the finite exact energy. No energy trace is passed using unweighted norm convergence.

For a finite-rank F approximating the fixed kappa in HS,

    |Tr(kappa L_h)|
       <=C eta_h ||F||_1+C||kappa-F||_HS.              (6)

The normal terms in (5) are O(eta_h Tr(n)); first let h_lambda vanish in (6), then improve F. This proves the asserted additive mean, uniformly over the driving class for that fixed rho. If kappa is trace class, the total error is `O(eta_h[1+Tr(n)+||kappa||_1])`. If kappa=0, it is uniform over all states with a common energy bound. Gauge-invariant states have kappa=0. The distinction between small operator norm and bounded HS norm in L_h explains why arbitrary bounded-energy families do not share this mean conclusion.

This covariance calculation is a separate check of the mean predicted by the cocycle law. Initial anomalous coherence is retained explicitly and shown to vanish only with the stated fixed-state approximation.

## 5. W1 and the scope of uniformity

For fixed finite-energy rho, the limiting convolution has mean E_rho+omega nu J. Weak convergence from (4) and independent mean convergence from (5) imply uniform integrability for the nonnegative laws: use `E[(X-R)_+]=E[X]-E[min(X,R)]` and `X1_(X>2R)<=2(X-R)_+`. Truncation of Lipschitz tests then proves W1 convergence.

Uniform comparison over A,T for this one rho follows by the compact-J subsequence argument. The comparison convolutions themselves are continuous in W1: couple the initial variable identically and couple the Poisson counts by an independent increment, at cost at most `omega nu |J1-J2|`. This proves assertion 2. For a fixed normal state of infinite energy, (4) still supplies the weak law, but no W1 or finite mean is asserted.

Uniformity over driving parameters for a fixed state is different from uniformity over initial-state families. The trace-class approximation in (4) and the fixed HS tail in (6) are not supplied uniformly by an energy bound. The counterexamples below show that this is a real obstruction, not merely an incomplete estimate.

## 6. Correlations, finite modes and global state distance

For each fixed CAR observable B,

    ||U* B U-B|| ->0,

so interaction expectations tend to their initial values, uniformly in the initial density matrix for that fixed B. For the full picture the comparison is with `U0(T)rho U0(T)*`; the same norm estimate follows through free rotation. This does not say that arbitrary nonvacuum initial data return to vacuum in the interaction picture.

For a rank-d one-particle projection Q, expand its matrix algebra in 4^d Majorana monomials. A norm-one operator has coefficient l1 norm at most 2^d, and each monomial has degree at most 2d. Telescoping gives the sufficient uniform bound

    ||(U rho U*)_Q-rho_Q||_1
       <=min(2,2d 2^d delta_h).                         (7)

It proves convergence for fixed rank, even for varying Q and rho; its rank dependence is not claimed optimal. The full-state version compares with the free initial reduction. If b_Q=Tr(Q n), positivity of Q_rho gives the sharper occupation estimate

    Tr(Q n_out)=||Q_rho^(1/2)Z*Q||_HS^2
                         <=(sqrt(b_Q)+sqrt(d)delta_h)^2. (8)

Thus the vacuum detector bound d delta_h^2 survives for initially empty modes. A positive initial occupation cannot be counted as newly induced excitation, so the vacuum rank lower bound does not apply to total detections in arbitrary initial states.

Let g_h=<Omega,U Omega> and p_h=|g_h|^2. Lemma (3), compactness and trace-class approximation prove, for each fixed normal rho and fixed compact K,

    Tr(U rho U* K)-p_h Tr(rho K) ->0.                  (9)

The free-rotation uniformity in that lemma likewise gives `W-g_h U0(T)->0` in fixed weak matrix elements, whence

    Tr(W rho W* K)-p_h Tr(U0(T)rho U0(T)* K) ->0.       (10)

The gap and the checked vacuum law give `p_h-exp(-nu J_h)->0` uniformly. Thus the interaction compact-test limit at J_h->J is the subnormalized operator exp(-nu J)rho, while its CAR limit is the normalized initial functional. No contradiction occurs between the different test algebras.

There is an exact limiting global-distance statement for every fixed normal rho, including mixed states:

    ||U rho U*-rho||_1
       -2sqrt(1-exp(-nu J_h)) ->0.                     (11)

To prove it first take rho supported on a fixed finite-rank R. Set C_h=RUR and S_h=(R-C_h*C_h)^(1/2). By (3), C_h-g_h R tends to zero in norm. Extending the polar isometry of (I-R)UR identifies the density difference on two copies of R with

    [[C_h rho C_h*-rho, C_h rho S_h],
     [S_h rho C_h*,     S_h rho S_h]].

Continuity of the square root makes this trace-norm close to rho tensored with `[[p_h-1,g_h sqrt(1-p_h)],[conjugate(g_h)sqrt(1-p_h),1-p_h]]`. The scalar matrix has eigenvalues +-sqrt(1-p_h), proving (11). Finite-rank approximation of any fixed rho changes the distance by at most twice its trace-norm error. Unitary invariance gives the same result between the full state and its free reference. This proves more than a pure-state fidelity calculation, without claiming uniformity over rho.

If also T->infinity, this continuum model has `U0(T)->P_Omega` weakly. Each nonvacuum finite-sector matrix element has an L1 sum-energy density after a momentum-to-energy change; Fourier decay and finite-sector approximation prove the assertion. Consequently (10) has limit `exp(-nu J)<Omega,rho Omega><Omega,K Omega>`. Fixed full-picture CAR observables tend to vacuum by the analogous finite-creation argument and vanishing one-particle contractions. Freely transported probes can retain the initial excitations. None of these statements implies spatial-algebra norm convergence, a current or an escape velocity.

## 7. Explicit limits to initial-state universality

The unshifted vacuum Poisson law already fails for a fixed finite-energy one-particle state. The quadratic drive is even and preserves its odd parity, so its final vacuum probability is zero. A finite-intensity vacuum Poisson law has positive mass at zero. The convolution theorem retains the initial energy distribution and is compatible with this exact obstruction.

For failure of uniform claims, choose the positive-rate fixed slots supplied in470, a constant amplitude a_c in (0,A_star] and T=tau/lambda^2 with 0<tau<=tau_star. This requires a nonzero amplitude budget and a positive horizon; its variation is zero. Write mu=nu a_c^2 tau>0 and p=exp(-mu). The inverse map has beta'=PZ*P_-=Gamma beta*Gamma, hence the same unweighted HS norm as beta. If D0=P_-ZP_-, unitarity gives

    beta+beta'=-(A0-I)beta'-beta(D0*-I).

Using (1)--(2) on the right proves `||E^(q/2)(beta'+beta)||_HS=O(eta_h)` without assuming a weighted bound on beta' in advance. The inverse-vacuum state therefore has finite energy tending to omega mu.

Take the varying initial density `rho_h=U*P_Omega U`. Its exact output under U, and under W, is vacuum. It has uniformly bounded initial free energy, and its initial vacuum weight is p_h->p. The putative uniform convolution prediction has vacuum weight p_h p->p^2, whereas the output has weight 1; a continuous test supported below the gap detects the discrepancy. Its predicted additive mean tends to 2omega mu, while the exact output mean is zero. This disproves uniform weak-law, mean and W1 statements over bounded-energy initial families. Any positive energy budget admits the construction by taking a sufficiently small positive tau within a positive horizon.

There is a separate fixed-number obstruction to uniform weak-law/W1 convergence, even though its mean obeys the uniform kappa=0 estimate. Let L'_h be the exact pair graph of U*Omega:

    L'_h=beta' Gamma (A0*)^-1 C.

The inverse identity above and the checked graph normalization give, with J_real=Gamma C,

    L'_h=-B1 J_real+O_HS(eta_h),
    ||E^(1/2)(L'_h+B1 J_real)||_HS=O(eta_h),
    (1/2)||L'_h||_HS^2 ->mu,
    ||E^(1/2)L'_h||_HS^2 ->omega mu.

The factor 1/2 is the exact exterior-pair norm. Therefore

    b_h=||P_2 U*Omega||^2=(p_h/2)||L'_h||_HS^2 ->p mu>0.

The normalized two-particle vector `phi_h=P_2 U*Omega/sqrt(b_h)` has zero anomalous covariance and initial energy tending to omega. In fact its initial energy law converges in W1 to the point mass at omega: the pair-vector HS approximation reduces its characteristic function to `integral r(e)exp(ise)|I_A,T(e)|^2de / integral r(e)|I_A,T(e)|^2de`, which tends to exp(is omega) by M18; the weighted ratio above supplies the mean. Its exact output vacuum probability is b_h, since `<Omega,U phi_h>=sqrt(b_h)`. The comparison convolution has no mass below 2m. A continuous gap test therefore separates the laws by a nonzero limit; a Lipschitz gap test also gives a positive W1 lower bound. Its pair kernel has vanishing operator norm but nonzero HS norm, so it is not a single decomposable Slater pair for small h. A small fixed mixture with vacuum fits any positive energy budget and retains the discrepancy.

These preparations depend on the drive and lambda. They do not contradict a theorem for one fixed rho. They also show why a uniform mean theorem for kappa=0 does not establish a uniform law.
<!-- END EXACT CORE independent224:20-216 -->

## Source verification and direct imports

The [review history](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/REVIEW_HISTORY.md), [handoff](../.claude/science/physics-loops/toe-initial-state-kinetic-energy-20261013/HANDOFF.md) and source map distinguish prior complete analytic reading from current identity checks. The two selected mathematical slices are unchanged. Full original sources, precision, direct frozen evidence and acceptance remain archived. Nested historical receipts are preserved as provenance, not recursively audited.

The primary identity runner checks archive bytes, exact core reconstruction and canonical parent maps only. It executes zero mathematical predicates, no numerical science and no Lean build. No canonical runner/cache/graph/pipeline ran during publication preparation. Its cached output, if later created by root through the canonical envelope, is source-integrity evidence only.

Direct scientific imports:

- [modulated_kinetic_energy_bounded_theorem_note_2026-10-13](MODULATED_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [general_compact_control_kinetic_energy_bounded_theorem_note_2026-10-13](GENERAL_COMPACT_CONTROL_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [two_zero_kinetic_energy_bounded_theorem_note_2026-10-13](TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md)
- [kinetic_correlation_limits_bounded_theorem_note_2026-10-13](KINETIC_CORRELATION_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-13.md)
