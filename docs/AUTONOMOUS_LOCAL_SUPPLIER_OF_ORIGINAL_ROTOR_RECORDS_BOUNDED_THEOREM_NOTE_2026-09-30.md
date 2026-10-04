---
claim_id: autonomous_local_supplier_of_original_rotor_records_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: 'On a fixed even cubic torus and finite horizon, the supplied original rotor process from Omega has a finite positive time-independent enlarged-cell local supplier approximating its binned original marks and source energy/current moments, with explicit controller, interaction and optional read-energy allowances. Accuracy-dependent finite qubit encoding; supplied law, apparatus and preparation.'
upstream_dependencies:
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - cubic_original_record_response_at_fixed_couplings_bounded_theorem_note_2026-09-26
runner: scripts/autonomous_local_original_rotor_supplier_2026_09_30.py
---

# Autonomous local supply of the original rotor records on a finite horizon

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: test selection and original-readout-preserving microscopic implementation separately
conditional_surface_status: supplied rotor law, apparatus and preparation
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: finite quantitative construction under explicitly supplied model and resource assumptions
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

For every fixed even torus L>=24, supplied positive K_s,delta,kappa, finite
horizon T>0 and positive process/moment/mean-ledger tolerances, there is an
explicit finite, positive, time-independent Hamiltonian on an enlarged local
tensor graph whose output approximates the ORIGINAL compensated rotor
process from Omega at any chosen finite grid of passive record observations.
The label convention is fixed as either resolved edge/sign marks or coherent
edge marks. Original quantum maps and their later births are retained. Source
mean energy and the first two quadratic source energy/current moments have
explicit transfer errors. Clock energy loss supplies the source mean gain
up to a controlled residual interaction term. Actual reads have a separate
energy-exchange allowance.

The construction gives one clock per A center, a bank of original-label
records and copies, and star-supported static couplings. Its explicit finite
M2 block encoding has accuracy-dependent geometric range and interaction
order. These are supplied apparatus resources, not a change to the framework
axioms or a claim of native carrier selection. No clock resets, rephasing or
externally timed collisions occur during the implemented closed run.

The proof has five load-bearing parts, all proved below: the weighted
original-history product cutoff (Appendix A); local original-label collisions
and matched record code (section 2); translation-clock pulse comparison
(section 3); positive finite Fourier compression with exact Dyson-prefix
agreement (section 4); and the endpoint controller/interaction ledger and
finite qubit encoding (sections 5-7). The landed source links define the
supplied law. No unlanded campaign theorem is needed as a premise.
The result is upstream support for a local source/action supplier of this
specified law. Framework selection and its physical-observable interpretation
remain outside the theorem's target.

## 1. Original source and finite target

The supplied common law and local magnetic decomposition are those of the
[common-field record limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
and [local pair form](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).
The original labels, preparation, tensor placement and sharper incidence
bounds are specified in the [fixed-coupling original-record source](CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md).
The dynamics below is taken as supplied; none of its later response or band
claims is used. The construction re-establishes its cutoff and apparatus
lemmas here, rather than citing campaign reports as theorem premises.

On an even cubic torus
of side L>=24, let N=L^3/2. There are N A sites and N B sites. The supplied law
and its original jump operators are

    h = K_s D + A,          A = delta H4 = sum_p A_p,
    A_(a,c) = -2 delta S_ac* S_ac,       S_ac = F_c F_a P,
    D = sum_(a->b) (1-n_b) E_ab(E_ab-q_a),
    B_(a,b,sigma) = P j_(a,b,sigma) F_a P.

Here p ranges over unordered distinct A centers at lattice distance two.

Use fixed source units with hbar_planck=1 and the actual nonnegative source
couplings. Clock position below has units of time, not lattice distance.

The hard-core record algebra, integer links, all A charges +/-1, B charges
0,+/-1, Gauss constraint div E=q-1_A, charge N, compensator, K_s,delta,kappa,
Omega, and readout are supplied imports.
For clarity, on the intermediate hard-core site space |0>,|+>,|->, write
c_(x,q)=|0><q|, n_x=sum_q |q><q| and U_e|E>=|E+1>. Different sites and
links commute. With all links oriented A to B,

    F_a=sum_(d neighbor a, q=+/-1) c_(d,q)* c_(a,q) U_ad^(-q),
    j_(a,b,sigma)=c_(a,sigma)* c_(b,-sigma)* U_ab^sigma.

P fixes every A occupied. The Hamiltonian and jumps begin and end in P;
the intermediate vacancies in F_c F_a and their adjoints are kept.
Omega has every A charge +1, every B empty and every field zero. At A,
div E=sum_b E_ab; at B it is -sum_a E_ab. Thus these elementary formulas
preserve div E=q-1_A on each complete word. A link is stored at its B endpoint.
An original B is supported on the radius-one star of its A center. It moves
the old A charge q to an empty B_d and creates charges sigma,-sigma at A,B_b,
where d differs from b; E_ab increases by sigma and E_ad decreases by q.
The resolved instrument has 12N labels. The coherent instrument has 6N labels
and jump B_(a,b,+)+B_(a,b,-), with no normalization and no sign resolution in
an environment. Fix ONE of these choices throughout.

Actual source bounds, valid in every later birth sector, are

    ||A_p|| <= 288 delta,        v := ||A||_upper = 2592 delta N,
    ||B_res||^2 <= 9,            ||B_coh||^2 <= 18,
    ||Gamma_a|| <= 80 kappa,     Gamma_a=kappa sum_(m at a) B_m* B_m.

Here is an incidence proof of the constants, including later sectors. At
neighbor B occupancy o, F_a has at most 6-o outgoing paths and o+1 inverse
predecessors, including the unit rotor shifts. The Schur bound gives
||F_a||^2<=(6-o)(o+1)<=12. At a fixed birth edge there are 5-o destinations,
so the resolved bound is (5-o)(o+1)<=9. The two sign outputs have orthogonal
A-charge ranges, giving the coherent bound 18 while retaining their sum
within the mark. For either label convention the center loss in that block
is 2kappa(5-o)F_a*F_a. Its bounds for o=0,...,5 are respectively
60,80,72,48,20,0 times kappa; the remaining block vanishes. Hence

    g:=80kappa N >=sum_a ||Gamma_a||.

There are eighteen distance-two A neighbors, hence 9N unordered magnetic
pairs. ||S_ac||<=12 gives ||A_p||<=288delta and the quoted v. For weighted
word bounds it is convenient to use the separately safe estimate

    g_w:=300kappa N >=sum_m ||sqrt(kappa)B_m||^2.

It follows already from the sharper bounds above (which sum to 108kappa N).
Thus g and g_w have explicit different uses; neither assumes a constant
trajectory rate. Compression gives Gamma_(a,R)<=P_R Gamma_a P_R. Integer
E(E-q_a)>=0 proves selfadjointness of K_s D+A on Dom D and h+vI>=0.

Take a product cutoff |E_e|<=R. Compress each original A_p and B_m onto this
box and use Gamma_(a,R)=kappa sum B_(m,R)* B_(m,R). In particular,

    A_(p,R) = P_R A_p P_R,

NOT a product built from individually truncated F's. Intermediate excursions
in the original pair word must remain. These compressed maps have the same
local supports and preserve Gauss constraints. Write h_R=K_s D_R+A_R and
shift h_+=h_R+v I>=0. A scalar shift does not change records or transfers.
Useful bounds are

    Qmax = 1+6NR,
    hbar = 2 K_s Qmax^2 + 2v >= ||h_+||, ||h_R||,
    Pbar = g_w (316 K_s Qmax^2+2v) >= ||P_R^current||,
    P_R^current = kappa sum_m [B_m* h_R B_m - {B_m*B_m,h_R}/2].

The following explicit cutoff estimates include every subsequent birth.
Appendix A proves them for this product box, including the energy/current
quadratic domains; they are not unexplained finite-dimensional imports.
Let M_birth=N/2, b=1+2M_birth, x=(v+g_w/2)T, y=g_w T, and choose ell>=0.
Put

    bM = sqrt(sum_(j=0)^M_birth y^j/j!),
    X_p = bM sum_(l>=0) (b+4l)^p x^l/l!,
    Y_p = bM sum_(l>=ell+1) (b+4l)^p x^l/l!,
    R = 2M_birth+4ell+8,
    S_h=2K_s X_2+v,              S_P=g_w(316K_s X_2+2v),
    E_h=4K_s Y_2+3vY_0,          E_P=4g_w(316K_s Y_2+2vY_0).

The full original history/final-state trace error and source moment errors,
uniformly for t<=T, obey

    eta_rot<=min(2,4Y_0),                E_rot=4S_h Y_0,
    error energy second moment <=2S_h E_h,
    error source current mean <=2S_P Y_0+E_P,
    error source current second moment <=2S_P E_P.          (1.1)

They also bound the corresponding signed measures against any real history
function of supremum norm at most one. The current is the original source
form kappa sum[B_m* h B_m-{B_m*B_m,h}/2], on Dom Q^2 with
Q=1+sum|E_e|; its second moment means its squared vector norm. No particular
selfadjoint extension of this unbounded symmetric form is selected.
The estimates tend to zero as ell grows at fixed source volume, couplings
and T. Arbitrary source interventions injecting unbounded field energy are
outside this prepared-input theorem.

## 2. Original collision maps and actual records

Choose n bins, tau=T/n, with 80 kappa tau<=1/2. At center a let

    K_(a,0)=sqrt(I-tau Gamma_(a,R)),
    K_(a,m)=sqrt(tau kappa) B_(m,R).

Introduce a blank flag F_(a,k) with d_F=13 levels in the resolved case or
d_F=7 in the coherent case. A second zero-free-energy register E_(a,k) has
the same dimension. A finite local unitary U_(a,k) has ready column

    psi |0>_F |0>_E -> sum_(m including 0) K_(a,m) psi |m>_F |m>_E.    (2.1)

This is an isometry since sum K* K=I. First complete the single-flag column
sum_m K_m psi |m>_F to U_flag separately in its finite local Gauss blocks,
leaving spectator link coordinates fixed. An explicit completion is: with
R_a psi=(sqrt(tau kappa) B_(m,R)psi)_m on the nonblank flag block, use

    U_flag = [ sqrt(I-R_a*R_a)       -R_a*          ]
             [ R_a                  sqrt(I-R_aR_a*) ].       (2.1b)

The identity sqrt(I-R_a*R_a)R_a*=R_a*sqrt(I-R_aR_a*) follows from polynomial
approximation to the continuous square root. Block multiplication then gives
both U_flag*U_flag=I and U_flag U_flag*=I. It preserves the required Gauss
blocks and spectator coordinates because R_a intertwines them. Thus no global
unitary-completion or energy-projector locality assumption is hidden here.
Let C_copy be the local modular
copy permutation |f,e> -> |f,e+f mod d_F>. Choose the FULL unitary

    U_(a,k)=C_copy (U_flag tensor I_E) C_copy*,
    C_record=span{|m>_F |m>_E : m=0,...,d_F-1}.              (2.1a)

It has ready column (2.1) and preserves C_record. Completion and the copy
permutation are supplied local controls. Tracing E gives precisely the
original classical mark instrument; in the coherent case E copies only the
original edge label, never sigma. There is no hidden measurement resolving
the coherent sum.
Different (a,k) use fresh initially blank registers; all registers are retained
physically. A positive spectral logarithm on this local finite space gives

    exp(-i G_(a,k))=U_(a,k),               0<=G_(a,k)<=2pi I.        (2.2)

Its spectral calculation is local to one star and its records, not global
source-energy diagonalization. G need not commute with h_R; its failure to
commute is exactly what the clock supplies energy for.
Choose its logarithm by the same copy conjugation of a positive logarithm
of U_flag. Then G preserves C_record exactly. All terms of the implemented
Hamiltonian preserve the product of these matched-record subspaces.
Consequently tracing all E makes the F bank EXACTLY diagonal in the original
label basis at every time, including partial pulses and finite-clock errors.
This exact classical output statement does not assert exact record permanence.
For an effective logarithm with a separated branch cut, one may first choose
a computable common phase of U whose finite spectrum avoids 1, and then use
the logarithm with values in (0,2pi). This changes (2.1) only by one common
phase and leaves its instrument exactly unchanged. Such a phase is found by
testing a dense list for a certified positive spectral distance from 1.

Order centers a=1,...,N within each bin. The ideal discrete process applies
these U's in that order and then exp(-i tau h_R). Interpret nonzero F flags
as the actual label sequence in that bin, in that order, dropping zeros.
This is an explicit classical interpretation of actual labels; no data
decoding or replacement observable is inferred. Histories with two or more
continuous-time events in one small bin are accounted for in the error.
On the history-append space the collision and splitting bounds give

    delta_sweep <= T tau c,     c=7g^2+4 hbar g,   g=80kappa N.    (2.3)

For a derivation, on the original-word append space the center generator
has completely bounded trace norm <=2g_a, g_a=||Gamma_(a,R)||. Its no-event
collision component has expansion rho-tau{Gamma_a,rho}/2 with remainder
<=tau^2 g_a^2: for 0<=X<=I/2 the scalar functional-calculus identities give
||sqrt(I-X)-I+X/2||<=||X||^2/4 and
||sqrt(I-X)-I||<=||X||/sqrt2. Expanding its two factors gives that bound.
Its marked gain is exactly the generator gain.
The exponential remainder is <=(tau*2g_a)^2 exp(2tau g_a)/2
<=2e tau^2 g_a^2, so the sum is <7tau^2 g_a^2. The histories with two or
more events are present in this exponential and in the same norm estimate.
Duhamel's double-integral product identity for contraction semigroups bounds
the ordered-center split by 4tau^2 sum_(a<b)g_a g_b. Since the Hamiltonian
commutator norm is <=2hbar, its split with the sum of center generators
costs <=4tau^2 hbar g. The center and cross terms fit under 7tau^2 g^2.
CPTP telescoping over n bins proves (2.3), including references and the
complete retained word in each bin. No scalar Poisson replacement is used.

## 3. A static local program and its ideal translation-clock proof

Assume T>0; T=0 requires no apparatus. Set circle length L_c=4T and
omega=2pi/L_c. Put one clock at each A center. The analysis clock is
L2(circle) with P=-i d/dx, Fourier modes exp(i m omega x), m in Z.
It is NOT the implemented apparatus: its unbounded-below spectrum will be
removed in section 4. The initial clock wavefunction is the product of

    beta(x) = [L_c(2k0+1)]^(-1/2) sum_(m=-k0)^k0 exp(i m omega x).

For 0<sigma<=L_c/2 its position probability outside |x|_circle<=sigma obeys

    theta <= 1/[(2k0+1) sin^2(pi sigma/L_c)]
          <= L_c^2/[4(2k0+1)sigma^2].                         (3.1)

This follows directly from the finite geometric sum. All clock phases are
prepared around zero once. The state is a product across centers and with
the source/blank records; no intercenter entanglement or stored trajectory
correlations are assumed. The phase reference/preparation is nevertheless
a supplied, consumed resource.

Let m_g=Nn. Choose s<=tau/(8N+4). In bin k=0,...,n-1 put the center-a pulse
at t_(a,k)=k tau+2as. Its nonnegative periodic triangle g_(a,k) has support
[t_(a,k)-s,t_(a,k)+s], height 1/s, area 1, Lipschitz constant 1/s^2 and total
variation 2/s. The pulses are ordered and disjoint except at zero endpoints.
At each grid boundary j tau every triangle vanishes throughout the circle
neighborhood of radius s. At each center the sum over its n triangles is
bounded by 1/s.

Replace the triangles by the positive Fejer convolution of degree M:

    f_(a,k)=F_M*g_(a,k),
    F_M(x)=[L_c(M+1)]^(-1)
            [sin((M+1)pi x/L_c)/sin(pi x/L_c)]^2.

Each f is nonnegative, of Fourier degree M, integral one and supremum <=1/s.
Also sum_k f_(a,k)<=1/s and TV(f)<=2/s. Its first circular moment obeys

    mu_M := integral |x|_circle F_M(x) dx
          <= L_c[1+ln(M+1)]/[2(M+1)].

For an elementary proof use F_M<=min((M+1)/L_c,
L_c/[4(M+1)x^2]) and split at L_c/[2(M+1)]. Consequently

    rho_1 := ||f-g||_1 <= L_c[1+ln(M+1)]/[(M+1)s],
    rho_inf := ||f-g||_infty <= L_c[1+ln(M+1)]/[2(M+1)s^2].   (3.2)

Using 1+ln u<=2sqrt(u), u>=1, gives the simpler upper bounds
2L_c/[s sqrt(M+1)] and L_c/[s^2 sqrt(M+1)], respectively.
The actual stored Fourier coefficients, rather than a black-box pulse, are

    fhat_j=(1-|j|/(M+1)) exp(-i j omega t_(a,k))
              sinc^2(j omega s/2)/L_c,       |j|<=M,

and zero otherwise, with sinc(0)=1. The compressed matrix entry indexed by
clock modes u,v is fhat_(u-v).

The analysis Hamiltonian is

    H_infty = h_+ + sum_a P_a + V,
    V = sum_(a,k) f_(a,k)(X_a) G_(a,k),
    0<=V,           ||V||<=v_c:=2pi N/s.                    (3.3)

It is selfadjoint on D(sum P_a), by bounded perturbation. Its exact
characteristic solution, for initial coordinate vector y, is

    Psi_t(y+t 1) = [product_a beta(y_a)] U_y(t) psi,
    i dU_y/dt = [h_+ + sum_(a,k) f_(a,k)(y_a+t)G_(a,k)] U_y.

This is a time-ordered solution: no commutation of h and G is presumed.
The unconditional joint clock-position density translates exactly even
after source/clock correlations form. This follows from unitarity on each
characteristic, or pointwise trace cancellation. A postselected trajectory
need not have that marginal.

On the event that every |y_a|<=sigma, translation in L1 and TV(f)<=2/s give
||U_y(t)-U_0(t)|| <=4pi m_g sigma/s, uniformly for 0<=t<=T. The bad-position
probability is at most Ntheta. Comparing purifications and then tracing clocks
gives the trace-norm bound

    delta_jitter <=8pi m_g sigma/s +4sqrt(Ntheta).             (3.4)

Comparison of f and g gives delta_smooth<=4pi m_g rho_1. Under the triangles,
neglect h only on the interval from the first pulse's start to the last
pulse's end within a bin (length 2Ns). The remaining initial guard has length
s. Moving this guard to the end and restoring the omitted free time costs
at most (4Ns+2s)hbar in vector norm per bin. Thus the conservative bound

    delta_pulse <=16 m_g s hbar                              (3.5)

controls the difference from the ordered collision sweep with total free
evolution tau. All pulse timing above describes fixed coefficients of (3.3),
not a sequence of external actions during operation.

## 4. Implemented finite clocks: positive compression and exact Dyson support

Choose K_c>k0 and let Pi_K project one clock onto -K_c<=m<=K_c. Implement

    H_(C,a)=omega sum_(m=-K_c)^K_c (m+K_c)|m><m| >=0,
    F_(a,k)^K=Pi_K f_(a,k)(X_a) Pi_K >=0,
    V_K=sum_(a,k) F_(a,k)^K G_(a,k) >=0,
    H_AUT=h_+ +sum_a H_(C,a)+V_K >=0.                         (4.1)

This is a finite, time-independent Hamiltonian. F is the ordinary positive
Toeplitz compression. It is NOT a cyclic replacement of the Fourier shifts.
Its norm obeys ||V_K||<=v_c. The original h_R remains present throughout.
Clock ground energy is zero; adding K_c omega is only a scalar in the
comparison with H_infty, but is included in the physical preparation budget.

In the interaction picture of h_++sum P, each insertion of V changes one
clock momentum by at most M. Source and reference dynamics change no clock
momentum. Starting in the product band |m_a|<=k0, every Dyson word and every
prefix with at most r insertions lies inside the finite clock space whenever

    K_c>=k0+Mr.

For these orders the finite and infinite coefficients agree EXACTLY.
With T_j(z)=sum_(l>=j) z^l/l!, the two remaining norm-convergent Dyson series
therefore give, uniformly for 0<=t<=T,

    vector error <=2T_(r+1)(v_c T),
    delta_cut <=4T_(r+1)(v_c T).                             (4.2)

This also establishes the required clock-domain comparison: the ideal
generator is selfadjoint by bounded perturbation, its interaction-picture
Dyson series converges in operator norm, and equality of the low-order words
is on the explicitly specified initial band. No differentiation of an
incorrect wrapped position/momentum pair or unproved rotor LR hypothesis is
used. The finite model needs no unbounded operator domain at all.

Clock-independent contractions/isometries at fixed grid times leave the
momentum-word argument intact. Expanding the intervals gives total ordered
simplex volume T^l/l!, so the same bound holds when comparing corresponding
passive grid tests. This mathematical process comparison does not add those
tests to the autonomous closed-system energy ledger for free.

Combining the preceding bounds, the entire reduced history/source output
under corresponding passive original-record tests at fixed grid times is within

    eta_total <= eta_rot + delta_app,
    delta_app := T tau c +16m_g s hbar +4pi m_g rho_1
                 +8pi m_g sigma/s+4sqrt(Ntheta)+delta_cut.    (4.3)

Use the proved errors (1.1) plus hbar delta_app for source mean
energy, hbar^2 delta_app for its second moment, and Pbar delta_app and
Pbar^2 delta_app for source current mean and quadratic second moment.
These are bounded-observable additions after the rotor truncation, not a
claim that trace distance alone controls an unbounded observable. Arbitrary
energy-injecting source interventions are not covered by the rotor bridge.
Here current moments mean those of the original source-current expression
evaluated on the approximating source state at grid times. They are not
moments of the generally pulsed derivative i[H_AUT,h_R], and no new
selfadjoint extension or measurement law for an unbounded current is asserted.

## 5. Full energy ledger, including controller and residual interactions

The apparatus free energy is H_C=sum_a H_(C,a). Its initial mean is
N K_c omega, its maximum is 2N K_c omega, and its initial variance is
N omega^2 k0(k0+1)/3. Flags and their copy registers have zero free spectra.
All coupling energy is in V_K, not silently assigned to zero-cost switching.
The initial total mean is <h_R>_Omega+v+N K_c omega+<V_K>_0,
bounded above by hbar+N K_c omega+b0 below; it includes controller interaction
energy as well as the clock reserve and supplied source preparation.
The total positive Hamiltonian is conserved exactly, and

    -Delta <H_C> = Delta <h_R> + Delta <V_K>.                 (5.1)

Total conservation alone would be insufficient. Here the last term is small
at the actual observation boundaries. For sigma<s, at any jtau in [0,T],
the analysis translating density and the endpoint zeros of every triangle
give

    0<=<V>_(jtau) <= b0:=2pi m_g rho_inf +v_c Ntheta.

Using the joint finite-clock trace bound for the bounded V gives

    0<=<V_K>_(jtau) <= b0+v_c delta_cut,
    |Delta <V_K>| <=2b0+v_c delta_cut                       (5.2)

between time zero and any grid endpoint. Initially the finite state is
exactly in the projected band, so only the final endpoint needs the cutoff
term. The bounds are deliberately conservative despite V_K>=0.

Combining with the original rotor energy bridge proves the source-supplier
ledger

    |-Delta <H_C> - Delta <h>_original|
       <= E_rot +hbar delta_app +2b0+v_c delta_cut.          (5.3)

The original source mean increment also equals its integrated original
current on this finite horizon by the weighted-domain argument in Appendix A.
This does not prove convergence of an instantaneous clock-current operator
or equality of work distributions, and it does not identify a positive source
gain on every branch. Clocks can gain energy on branches; they are finite
energy/coherence resources, not catalysts or stationary reservoirs.

The closed run retains F and E quantum registers. Discarding E yields an
exactly classical F register by (2.1a), with original-process error (4.3).
There is no extra dephasing operation needed to obtain that output channel.
There is also no need to perform active intermediate projection in the run.
If an observer actually dephases or reads F at a grid boundary, free h_R and
H_C commute with that operation, but V_K need not. Its additional energy
change must be charged to that measurement apparatus. Positivity and the
same pointwise pulse bound limit each unconditioned mean change by
2(b0+v_c delta_cut); it is NOT declared zero. Grid-test trace accuracy and
the no-intervention closed ledger (5.3) are distinct claims.
If W_read is the sum of those mean energy inputs to the modeled system from
actual reads, conservation between reads gives the exact identity
-Delta<H_C>+W_read=Delta<h_R>+Delta<V_K>. The reader must supply or receive
W_read; its absolute value is bounded by the number of reads times the stated
per-read allowance. Postselected outcomes do not inherit that mean bound.

The finite apparatus need not have exactly monotone N_B or exactly permanent
old flags: small Fejer tails can recouple completed gates, and their unitary
completions include reverse actions off the ready subspace. The complete
history bound controls these effects over [0,T]. The monotone birth grading
used for rotor truncation belongs to the original target process, not to a
new exact irreversible law for this closed finite apparatus.

## 6. Explicit finite resource choices

For requested apparatus trace accuracy alpha>0 and endpoint interaction
allowance epsilon_E>0, taking smaller alpha if necessary so alpha<=1, choose

    n >= max(1, 2Tg, 5T^2 c/alpha),    tau=T/n,  m_g=Nn,
    s <= min(tau/(8N+4), alpha/[80m_g(hbar+1)]),
    sigma <= min(s/2, alpha s/(80pi m_g)),
    vbar=8N/s >= v_c,
    theta_* <= min(alpha^2/(1600N), epsilon_E/(8vbar N)),
    k0 = ceil(L_c^2/[8sigma^2 theta_*]),
    D0 = ceil(max(160m_g L_c/(alpha s),
                  64m_g L_c/(epsilon_E s^2))),
    M=D0^2-1,
    dcut=min(alpha/5, epsilon_E/(4vbar)),
    k >= max(ceil(6vbar T), ceil(log_2(8/dcut)), 1),
    r=k-1,                  K_c=k0+Mr.                     (6.1)

For entirely rational arithmetic take sigma= min(s/2,alpha s/(320m_g));
this uses pi<4. Since k>=6vbar T and e<3,
T_k(v_cT)<=2(e v_cT/k)^k<=2^(1-k). Thus delta_cut<=2^(3-k)<=dcut.
The five process contributions in (4.3), grouping both jitter terms, are
each <=alpha/5. Equations (3.1)-(3.2) give
2b0+v_c delta_cut<=3epsilon_E/4. All parameters are explicit and finite.
For computable input reals, implement these choices with certified rational
upper bounds before integer rounding and positive rational lower choices
for required tolerances and small widths. This avoids assuming that exact
equality of a general computable real to an integer is decidable. The
inequalities permit those conservative choices; the example below is rational.

The actual-source example takes L=24, N=6912, K_s=delta=kappa=T=1 and the
explicit rotor cutoff R=1346132804 certified in Appendix A, whose five
rotor errors are <2^-100. Choose

    alpha=1/[1000(1+hbar^2+Pbar^2)],  epsilon_E=1/1000.

The primary runner recomputes both the rotor tail certificate and these
resource inequalities with exact integer/rational arithmetic.
It uses the sharper g=552960 for sweeps and the earlier g_w=2073600 for
weighted/moment bounds. It yields n with 111 decimal digits, m_g with 115,
M with 1118, and K_c with 1344. One clock uses 4463 qubits under binary
encoding; the dominant cost is the 111-digit bank of fresh records per site,
not the clock's binary register. Each added source moment error is <1/1000,
the endpoint interaction allowance is <=3/4000, and the combined mean ledger
error is <2^-100+1/1000+3/4000. These are existence bounds with enormous
costs, not an efficiency claim. Clock energy and coupling bounds are

    <H_C>_0=N K_c omega,
    ||H_AUT||<=hbar+2N K_c omega+vbar.

The static program contains m_g positive logarithms (the same center map can
be repeated on different records) and at most m_g(2M+1) real Fourier
coefficients. All original matrix entries, square roots, logarithms and
Fejer coefficients are finite computable data for computable source inputs.
A loose star dimension is d_star=2[3(2R+1)^6]^6. Dense storage of all local
G matrices would need at most 2m_g(d_star d_F^2)^2 real entries, in addition
to those Fourier data; formula sharing can reduce this bound. These matrix
constructions are specified finite resource imports, not computations that
were performed by the small verification jobs.
No claim of economical compilation/preparation is made. A generic finite
state-preparation circuit for each clock is an explicit possible import;
the packet has only 2k0+1 equal Fourier amplitudes, needs no intercenter
entanglement, and its mean/variance are given above. Preparation and static
Hamiltonian fabrication are paid resources, not autonomous derivations.

Finite coefficient precision is allowed, with an explicit propagated-state
price. For identical preparation and a static perturbation W treated as
interaction, ||W||<=zeta gives trace error <=2Tzeta and adds at most
2Tzeta(hbar+v_c)+2zeta to the mean ledger bound (5.3). The first term prices
the altered final source and interaction expectations; the second prices
Delta<W>. It is not enough to charge only the perturbation energy.
For initial trace error epsilon_p under the same implemented Hamiltonian,
trace error adds epsilon_p and the TWO-endpoint source-plus-interaction
mean difference adds at most 2(hbar+v_c+zeta)epsilon_p. Alternatively a safe
bound is 2E_star epsilon_p with E_star=hbar+2N K_c omega+vbar+zeta, the
nonnegative total-norm upper bound. Apply the perturbation and preparation
allowances by telescoping if both occur. Positivity can be retained by
positive matrix-factor approximations or a further scalar shift. To retain
exact classicality, approximate within the prescribed conjugated matched-code
blocks; an arbitrary small W supplies only the stated trace approximation.
The initial clock mean budget changes by at most 2N K_c omega epsilon_p;
the initial total mean changes by at most E_star epsilon_p under the same
perturbed Hamiltonian. These preparation costs are separate from the
two-endpoint ledger allowance. No accuracy-independent fabrication or
preparation cost is asserted.

## 7. Geometry, explicit M2 encoding, and its limitation

On the supplied logical tensor graph each D term touches an original edge;
each A_p touches the union of two A stars whose centers have distance two;
and each clock pulse term touches one star, that center's clock, and its
one flag/copy pair. None uses the whole torus or a clock shared globally.
Its coupling norm is <=2pi/s per center after summing the local pulses.

For a literal tensor product of M2 sites, use the fixed computational-basis
encoding of each finite factor: A uses one qubit, B uses two (one unused
code), each of the six integer links at B uses
q_E=ceil(log2(2R+1)) qubits, one clock uses
q_C=ceil(log2(2K_c+1)), and each record uses q_F=4 resolved or 3 coherent.
At each coarse A cell allocate

    b_A=1+q_C+2n q_F,             b_B=2+6q_E

qubits. Place them lexicographically in a disjoint cubic block of side
a_block=ceil_cuberoot(max(b_A,b_B)). The fine torus has side L a_block.
Original physical source observables are the explicit factorwise encoded
operators; each mark is the basis value of its own record register. The
map back to original charge/link/record factors is this stated local basis
isometry, not a global or dynamical decoding lemma.

Extend each local encoded matrix by zero outside its local legal codes;
extend free clock energies nonnegatively and preserve all legal-code
subspaces. The resulting original-product code is invariant. Magnetic
terms remain bounded below by -v in total, so the same scalar shift makes
the full extension positive. Positivity of compressed clock potentials
and G is preserved. Thus (4.1) is an exact engineered finite-qubit
Hamiltonian realization of the enlarged tensor model on its prepared code.
On the fine graph its interaction diameter is at most 7a_block: a magnetic
pair has coarse diameter four, with at most three additional block widths
for internal coordinates. A pulse uses at most five block widths. The
number of qubits touched by a pulse is at most
13+36q_E+q_C+2q_F; a magnetic pair touches at most 24+66q_E.

This encoding explicitly changes the microscopic geometry and uses many-body
terms. In the certified example a_block and the range have 38 decimal
digits. It does not establish unchanged microscopic range, bounded arity,
uniform local dimension/coupling, or the native M2 carrier selection.
If those are additional target requirements, a further locality compiler
with identity-on-source preparation/readout and its own energy/controller
ledger remains a substantive missing theorem. This construction does not invoke
universal simulation as a replacement for that theorem.
Assuming such a compiler without proving its original-factor channel,
preparation and full-energy bounds would be a target-strength import for
that stronger microscopic version, not a consequence of this construction.

## 8. Imports, prior constructions and conclusion at the declared scope

The quantum carrier, hard-core charges, integer fields, Gauss constraint,
compensated Hamiltonian, source units/couplings, Omega, original instrument
and its quantum-to-classical readout are supplied model inputs. The clock
species, blank flags and copies, initial phase packets, local unitary
completions, logarithm choices, pulse schedule encoded in static coefficients,
and finite precision are supplied apparatus choices, with their dimensions,
energies, norms and errors priced above. Finite-dimensional spectral calculus,
Fourier series, bounded-perturbation selfadjointness, Dyson convergence and
trace-norm contraction are mathematical tools whose needed hypotheses were
checked. No observational target or fitted physical constant is used.

The closest landed apparatus predecessors are
`FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
`AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`
and
`FINITE_AUTONOMOUS_MARKED_DYNAMICS_UNDER_GRID_OBSERVATIONS_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
Their actual positive finite battery lift, interaction-picture program and
correlation-preserving grid-process comparison were inspected. In particular,
the grid note already preserves resolved/coherent marks and permits a larger
class of finite-dimensional interventions. Its history-clock hopping blocks
act on a global system/battery payload. This source supplies a different
construction with clocks and gates on original stars, a weighted transfer
from the full unbounded rotor process, and an endpoint energy ledger for the
local controller itself. It does not claim that autonomous clocks or finite
instrument dilations are new. The older
`LOCAL_BACKGROUND_AND_UNRESTRICTED_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md`
already gives strong box convergence and bounded total births; Appendix A
adds explicit original-history and weighted moment estimates. These prior
references are contextual here; the needed proofs are supplied in this note.

The proof supplies simultaneous finite-volume, finite-horizon process,
source-moment and mean-energy approximation. If a finite set of desired
observation times is not on a common exact grid, choose sufficiently nearby
grid points; quantitative timing error for that additional comparison must
be included. The theorem as stated uses a prescribed finite grid and may
refine its common denominator. T=0 uses no apparatus. The displayed resource
formulas use positive couplings; zero coupling limits can instead omit the
corresponding operators before choosing parameters. A tolerance >=1 may be
replaced by a smaller positive tolerance. Coherent marks keep their original
unnormalized sign sums throughout.

The source does not claim exact continuous timestamps, exact stationary
Markov dynamics for all times, permanent irreversible flags, a stationary or
catalytic clock, a volume-uniform apparatus, fixed microscopic range/arity/
strength, native source selection, or branchwise work statistics. These are
quantifier and interpretation limits, not impossibility theorems. An extension
to the unchanged one-M2-per-site microscopic geometry would require a proved
local compiler preserving original-factor preparation and record maps together
with its own controller-energy estimates; that stronger task is unproved here,
not a premise used to finish the present enlarged-cell construction.

No new negative theorem or independent-wall count is proposed. The numerical
wrong-model controls below exhibit particular changed-map discrepancies.
They do not quantify over alternative implementations. The selected negative
claim triggers were checked on that basis; no N-gate PASS or formal audit
verdict is inferred. The new source remains conditional-support pending its
own independent source review and later audit.

## Appendix A. Full original process and weighted product-box transfer

This appendix proves (1.1) directly for the law in section 1. Let
N_B=sum_(b in B)n_b and Q=1+sum_e |E_e| on the physical P carrier. Every F_a
raises N_B by one; its adjoint lowers it by one. Every j raises N_B by one.
Thus [N_B,B_m]=2B_m, while D, S_ac* S_ac and Gamma preserve N_B exactly.
Reverse paths in the magnetic word can relocate B occupations but do not
change their number. From Omega, a j-event history lies in N_B=2j, hence
j<=M_birth=N/2, including every later birth. No adjoint B is a recorded event.
This grading is a property of the original target and its box compression;
it is not imposed on the off-ready autonomous unitary completion.

A jump shifts the full radial field sum by at most two, and magnetic/loss
words by at most four. The weight includes links at occupied B sites even
where their contribution to D is masked out. It obeys D<=2Q^2. The product
box contains every radial state with sum|E|<=R and commutes with Q, D and
the charge/Gauss constraints. It is finite dimensional, with the loose bound

    d_R <= 6^N (2R+1)^(6N),       Q<=Qmax=1+6NR.

Use L_m=sqrt(kappa)B_m. A full history with j ordered times has Kraus density

    exp[(-ih-Gamma/2)(t-t_j)] L_(m_j) ...
                L_(m_1) exp[(-ih-Gamma/2)t_1].             (A.1)

Stack (A.1) over labels and the ordered j-time simplex for 0<=j<=M_birth.
The result V_t is an isometry into the direct sum of the corresponding
history L2 spaces tensored with the final source. Measuring that history
space gives the original classical label/time measure and conditional final
state. The cutoff uses the same label/time space and embedded final source.
Its loss is Gamma_R=sum L_(m,R)* L_(m,R), not P_R Gamma P_R; this preserves
trace exactly. Distances below are unconditional integrated cq trace norms,
not a normalized rare-history estimate.

In the interaction picture of K_s D the bounded no-event perturbation is

    G(t)=exp(iK_s Dt)(-iA-Gamma/2)exp(-iK_s Dt),
    ||G(t)||<=a:=v+g_w/2.

Strong continuity and boundedness suffice for its strong Dyson integrals;
rotor-wide norm continuity is unnecessary. The cutoff has the same bound.
A term with l such insertions and j jump insertions has all field prefixes
inside radius 4l+2j. This includes both internal jump factors of a loss word,
and the internal four hops of each original A_p. Electric factors do not
move any field. Summing allocations of l insertions among the dwell
intervals gives t^l/l!, and the ordered jump-time simplex has volume t^j/j!.
Summing squared label norms uses sum_m ||L_m||^2<=g_w. Thus, uniformly t<=T,

    ||Q^p V_t^(l) Omega|| <= bM (b+4l)^p x^l/l!,            (A.2)

with the quantities defined in section 1, and the same bound for the box.
For l<=ell, all original and cutoff coefficients agree including internal
projection insertions. Indeed 4ell+2M_birth=R-8. Two tail estimates give

    ||Q^p(V_t-V_(t,R))Omega||<=2Y_p,
    ||Q^p V_t Omega||, ||Q^p V_(t,R)Omega||<=X_p.            (A.3)

The series converge for every finite integer p. Pure-state trace distance
and contraction under history measurement yield eta_rot<=4Y_0. The argument
is valid with passive copies of history at fixed times: these insert
clock/source-independent history isometries, and the total simplex and word
bounds are unchanged. Binning is classical coarsening. The conditional final
source remains part of the output throughout.

For the moment estimates, a field-range-s bounded operator O decomposes by
integer radial change into 2s+1 bands, each with norm at most ||O||. This
follows by Fourier averaging against exp(i theta sum|E|). On a band,
Q_out<=Q_in+s<=(1+s)Q_in, whence

    ||Q^p O psi|| <=(2s+1)(1+s)^p ||O|| ||Q^p psi||.         (A.4)

At p=2 this factor is45 for each jump and225 for Gamma. Therefore on Dom Q^2

    ||h psi||<=2K_s||Q^2 psi||+v||psi||,
    ||Pcurrent psi||<=g_w[316K_s||Q^2 psi||+2v||psi||].      (A.5)

For the electric part of Pcurrent the three costs are respectively90,1,225:
L*D L uses 2*45, Gamma D/2 uses1, and D Gamma/2 uses225. The bounded A part
costs2v. This derives316, rather than assuming a moment follows from trace
convergence. The compressed current obeys the same estimate. The weighted
Dyson series propagates Dom Q^p for this initial vector; cutoff/domain
approximation of the energy derivative is consequently dominated on every
finite interval. It gives

    <h>_t-<h>_0 = integral_0^t <Pcurrent>_s ds.              (A.6)

This is the original source's mean-energy identity for this preparation.
It asserts neither positivity after later births nor equality to an
instantaneous apparatus current operator.

On an embedded box vector, h-h_R=(I-P_R)A P_R. This vanishes on the radial
interior of width four. Its contribution is bounded by vY_0 because only
high-order history words reach that strip. Together with (A.3) and (A.5),

    ||h V_t Omega-h_R V_(t,R)Omega||<=4K_sY_2+3vY_0=E_h.

The full and cutoff current words have field range at most eight and agree
on the radial interior sum|E|<=R-8. Their boundary difference costs at most
2g_w(316K_sY_2+2vY_0), and their weighted vector difference costs the same.
Hence their vector difference is bounded by E_P as defined in section 1.
The vector norms themselves are bounded by S_h and S_P. Cauchy-Schwarz and
difference of squared norms prove (1.1). For the mean energy use also the
exact identity P_R h P_R=h_R, yielding the sharper4S_hY_0. Inserting a
bounded real history function commutes with all final-source operators,
so the same bounds hold in total variation for moment-weighted histories.
Quadratic energy/current moments mean ||h psi||^2 and ||Pcurrent psi||^2;
(A.3) supplies their domains, including the needed fourth field moment.

For a directly evaluable tail, let X=ceil x,Y=ceil y,k=ell+1>=max(1,6X),
and p2=(b+4X)^2+16X. Elementary exponential moments give

    X_2=bM exp(x)[(b+4x)^2+16x] <=2^(Y+2X) p2,
    Y_0<=2^(1+Y-k),
    Y_2<=(b+4k)^2 2^(1+Y-k).                               (A.7)

Here bM<=exp(y/2)<=2^Y, exp(x)<=2^(2X), and k!>=(k/e)^k with e<3.
The weighted-tail successive ratio is at most one half beyond k:
it is x/(l+1) times [(b+4l+4)/(b+4l)]^2, maximized at the first term;
for x>0, X>=1 and k>=6X make it less than1/2. The x=0 case is immediate.
Thus all requested errors can be certified by integer exponents and bit
lengths without evaluating powers with millions of digits.

For L=24 and unit K_s,delta,kappa,T, choose
k=16(X+Y+N+1)=336531472. It gives M_birth=3456,
v=17915904,g_w=2073600,x=18952704 and R=1346132804.
The primary runner recomputes these numbers and proves all five bounds in
(1.1) below2^-100 by rational/integer inequalities. The apparatus resource
row of section6 then uses this same R with the larger product-box Qmax.
This is a sufficient existence certificate, not a practical cost estimate.

## Appendix B. Reproduction and review boundary

The primary reproduction command is

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python3 scripts/autonomous_local_original_rotor_supplier_2026_09_30.py
```

Its source-bound input list contains this note and the three actual-law notes
linked in section1. One runner carries the actual cubic-star birth words,
later-birth and magnetic-return grading, boundary-loss fixture, finite clock
prefix words, matched-record code, explicit geometry, clock-module energy
ledger and both resource certificates. The finite numerical clock module is
labeled as a fixture, not substituted for the original torus law. The
analytic proof supplies the infinite-history/domain and arbitrary-resource
quantifiers; the finite checks are discriminators for its formulas.

The original-star check has 9720 legal local words, independently counted as
2*6*2*5*3^4. Successive single-star birth layers have1,45,150,35,0 distinct
charge/field words. The full axial two-star word on Omega gives
<Omega|S_ac* S_ac|Omega>=6*6-1=35, hence the pair term has diagonal-70delta.
At the product zero-field box this diagonal survives compression of the
whole word; individually zero-box-truncated hops instead give zero. The
coherent edge mark's ten distinct sign/destination outputs give cross-sign
gain matrix element1; copying the sign separately instead gives0.

The finite clock fixture uses h=diag(0,2), G=I-X, f=(1-cos x)/2, k0=2 and
t=0.6. Its largest comparison matrix has dimension130. At K_c=10 its
source, clock and interaction energy changes are approximately
+0.03277574467294, -0.06870793908688 and +0.03593219441394, with their sum
within2e-15 of zero. This tests the complete energy identity while exhibiting
a particular nonzero controller interaction contribution; it is not an
original-source simulation. Exact integer matrix checks separately test
the matched code and the nonwrapping clock commutator. The apparatus example
is certified by integer/rational inequalities, without constructing its
enormous Hilbert space.

The exact marked-word, weighted-cutoff, local collision and clock arguments
received focused independent checks during discovery, including the corrected
whole magnetic support24+66q_E and propagated finite-precision ledger cost.
That earlier context is provenance only. This coherent source and its changed
primary implementation require their own full source/input review; no formal
review or audit verdict is carried over by naming those checks.

Machine-written evidence is `outputs/autonomous_local_original_rotor_supplier_2026_09_30.json`
and the envelope cache at
`logs/runner-cache/autonomous_local_original_rotor_supplier_2026_09_30.txt`.
Actual scratch mutation commands/results and source identities are recorded
in the accompanying loop pack. Graph acknowledgment and combined integration validation are separate handoff
requirements, not implications of these checks.

Historical author preparation, actual failed controls, mutation results and source-review provenance remain recoverable through [PR #9397](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9397) at frozen head `72e8656de1a34d236db62f2443b23cd15c2d5f25`. They are provenance, not current proof premises or audit authority. The canonical argument and its linked current supporting proofs own the theorem; finite runner controls do not supply its analytic quantifiers.
