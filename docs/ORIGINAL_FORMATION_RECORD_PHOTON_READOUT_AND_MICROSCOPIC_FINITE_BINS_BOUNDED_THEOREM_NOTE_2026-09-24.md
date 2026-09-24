---
claim_id: original_formation_record_photon_readout_and_microscopic_finite_bins_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional original-instrument distinction between supplied vacuum and one-particle preparations, sufficient shrinking finite bins, and an ordered microscopic event-probability limit; no physical detector, parameter selection or empirical confirmation."
upstream_dependencies:
  - minimal_axioms
  - weak_field_wave_packets_from_mobile_record_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
  - photon_dispersion_observational_constraints_and_live_formation_response_bounded_theorem_note_2026-09-24
runner: scripts/original_formation_record_photon_readout_and_microscopic_bins_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; no retained audit verdict.

# From supplied wave packets to the original formation records

The original instrument can distinguish a prepared one-particle wave packet
from its prepared vacuum through a deficit in a selected two-record coincidence.
The two-mark operator has finite spatial support and retains the coherent
matter output of the first birth. The statistic requires these to be the
first two events of the entire finite system.
For a fixed finite cubic graph, a fixed first-event interval and a lag
b=o((a/c)g²), the full compensated matter-field process has a nonzero leading
finite-probability contrast whenever the selected plaquette amplitude is nonzero.
At each fixed positive window, the original microscopic marked probability
converges to that common target. A subsequently chosen spin sequence can resolve
the shrinking contrast. No quantitative or economical spin schedule is claimed.

These are supplied quantum models, compensation, preparations, couplings,
coordinate labels and monitoring instruments. The result does not establish
observed photon detection or select a,c,g,kappa. The accompanying
[conditional timing constraints](PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md) require further physical
identifications, propagation control and cosmological assumptions. They are
not evidence that these records are astronomical photon measurements.

The source arguments are retained below with the narrow disclosed corrections
and current dependencies made explicit. Equations are numbered locally within
each labeled section. Root derivations, independent reconstructions, numerical
controls and physical interpretation have separate scopes. The review packet
preserves original sealed versions, including the earlier conservative
b=o((a/c)g⁴) bound and the corrected coherent-mark sentence.

The mathematical parents are the
[prepared weak-field theorem](WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[common compensated matter-field limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md),
[local pair-form Hamiltonian](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md), and
[bounded microscopic target with finite registers](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md).
Their supplied premises and ordered limits remain dependencies. In particular,
the older slow-formation scaling is not used to infer this live-kappa process.

## A. The original two-mark readout

### 1. A local pair of marks with a nonconstant field effect

Take a simple cubic torus with all periods even and at least six, all A plus
and all B empty, and unit rotor shifts. Use the full compensated target of
LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT and the local pair-form source.
All stored links below point from A to B. Choose

    a=(0,0,0), d=(1,1,0),
    c=(1,0,0), e=(0,1,0),
    b=(-1,0,0), f=(2,1,0),

with periodic coordinates. a,d are A; c,e,b,f are B. The first resolved mark
is j=(a,b,sigma), the second l=(d,f,tau), with either sign fixed in advance.
The marks refer to births; the outward-hop destinations are not measured.
Let C=B_l B_j P0. The claim is the exact initial-sector effect

    C^* C = 23 I + W_p + W_p^*,
    B_j^*B_j P0=5P0,                                  (1)

where W_p is the loop around a,c,d,e. Equation (1) is on the entire physical
initial field space, with arbitrary normalizable states and coherences.

Proof by paths: the first plus record can hop from a to any of its five
neighbors other than b. The second can hop from d to any of its five neighbors
other than f. Neither b is adjacent to d nor f to a. The two outward
destinations must differ. The common choices are exactly c,e, so there are
5*5-2=23 legal assignments. Every assignment has amplitude one. Equal final
matter words arise for the two assignments (a->c,d->e) and (a->e,d->c).
Their field-shift difference is precisely the plaquette cycle. The resulting
cross terms are W_p and W_p^*. All other final matter words are orthogonal.
The fixed birth shifts at (a,b),(d,f) cancel from C^*C. The argument does
not depend on the two selected signs.

If either edge uses a coherent sum of its two signs, its multiplicity is two;
the four eventual sign pairs have orthogonal A charge words. Thus the initial
pair effect is m_j m_l times (1), and the first effect is 5m_j I, with
m=1 resolved or m=2 coherent. This particular effect equality does not make
the complete instruments equivalent. We state subsequent formulas for the
resolved case. The zero-separation pair effect and BOUNDARY density acquire
m_j m_l for coherent choices. At positive separation use the actual chosen
B_j,B_l and first-mark CP output in (2); no first coherent-mark multiplicity
shortcut through the postbirth propagator is asserted.

If the matter charge configuration is dephased after the first mark, the two
first outward destinations c,e become distinguishable and the cross terms
in (1) disappear. The effect becomes 23I. That extra operation is NOT part
of the original instrument. Tracing the first matter state and propagating
only a reduced field would miss precisely the phase-sensitive readout.

### 2. The exact two-event density uses the full postbirth generator

For this finite graph, lambda=2kappa sum_A z(z-1)=30kappa V. Before the first
mark, the state is rho_s=exp(-is h0)rho_0 exp(is h0), with survival exp(-lambda s).
Here h0 is the actual initial-sector field Hamiltonian

    h0=K sum E^2-2delta sum_p(W_p+W_p^*)+constant.

Let A_+=-i h_+-kappa Lambda_+/2 be the FULL no-event generator after the first
birth, including its matter and q-dependent electric energy. The Janossy
density that j is the first event at s and l is the next at s+u is

    f_jl(s,u)=kappa^2 exp(-lambda s)
       Tr[B_l exp(u A_+)B_j rho_s B_j^* exp(u A_+^*)B_l^*]. (2)

No postbirth field Hamiltonian has been substituted. Strong continuity and
bounded B's give the exact boundary value

    f_jl(s,0)=kappa^2 exp(-lambda s)
                          [23+2 Re Tr(W_p rho_s)].       (3)

It is a density as u decreases to zero through positive separations, not a
positive probability of exactly simultaneous events. Given the first mark
at s, the selected immediate second-mark intensity is
kappa[23+2 Re Tr(W_p rho_s)]/5. Every individual first-mark density is
5kappa exp(-lambda s), independent of rho_0. This first-pair statistic is
therefore the first field-sensitive readout established by this construction.
No statement excludes other observables or differently prepared detectors.

### 3. A free packet gives a moving coincidence deficit

Use the prepared weak-field packet construction of the pinned source
WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS. Set

    K=c g^2/(2a_lattice), J=2delta=c/(2a_lattice g^2).

Here a_lattice is spacing; the earlier vertex a is only a label. Work on
the source's finite transverse real space with harmonic windings removed.
Let f_r be a real orthonormal eigenbasis of D_curl with lambda_r>0, and
omega_r=(c/a_lattice)sqrt(lambda_r). A plaquette row is c_p, so W_p on its
flat chart is exp(i g c_p dot x). Define

    d_pr=(c_p dot f_r)/sqrt(2 sqrt(lambda_r)),
    v_p=sum_r d_pr^2,
    |alpha>=sum_r alpha_r a_r^*|0>,  sum |alpha_r|^2=1,
    chi_p(s)=sum_r alpha_r exp(-i omega_r s)d_pr.       (4)

Finite combinations are sufficient. The two preparations are the normalized
compact rotor packets I_g|0> and I_g|alpha>. These are supplied initial field
states of the current common target, not a claim that formation prepares them.

The exact Gaussian/Fock characteristic functions of the harmonic reference
are

    <0|W_p|0>=exp(-g^2 v_p/2),
    <alpha_s|W_p|alpha_s>
                =exp(-g^2 v_p/2)[1-g^2 |chi_p(s)|^2].  (5)

For example, normal order exp(i g sum_r d_pr(a_r+a_r^*)) and evaluate its
matrix elements on the one-particle subspace. The vacuum scalar is the first
factor, and the one-particle matrix is delta_rt-g^2 d_pr d_pt. Formula (5)
also follows by a unitary change of one-particle basis making |alpha> a single
occupied mode. Spatial and temporal dependence is retained in chi_p(s).

The actual compact-rotor error is small enough to resolve this O(g^2) signal.
The parent gives, after an irrelevant scalar phase is aligned, a vector error

    ||e_g(s)|| <= C_T g^2+C_T exp(-b/g^2),              (6)

uniformly on a fixed finite [0,T], for either normalized packet. Its constants
depend on this fixed volume, c,a_lattice,T and packet. Set O_p=W_p+W_p^*-2I.
It has norm at most 4, while on the reference chart packet

    ||O_p I_g exp(-is H_quad)psi||
                 <= C_psi,T g^2 + C exp(-b/g^2).       (7)

Indeed |2(cos y-1)|<=y^2, and the finite-excitation harmonic trajectory has
uniformly finite fourth moments of c_p dot x. Gaussian cutoff normalization
has an exponentially small error. Expanding the expectation in reference
plus e, rather than bounding it by ||O_p|| ||e||, yields

    |<O_p>_actual-<O_p>_reference|
                <=2||e|| ||O_p reference||+4||e||^2
                =O_T(g^4)+O(exp(-b'/g^2)).             (8)

This uses only the parent's vector estimate and reference moments. No weighted
bound on the actual evolved state's error is silently assumed. The identity
term cancels because both compared states are normalized. Equation (8) is
the reason the first nonzero record contrast can be resolved.

Combining (3)-(8), the actual two-event boundary-density difference between
the one-photon and vacuum preparations is

    Delta f_jl(s,0)
       =-2 kappa^2 exp(-lambda s) g^2 exp(-g^2 v_p/2)
                                  |chi_p(s)|^2
          +kappa^2 exp(-lambda s) O_T(g^4).            (9)

The exponentially small terms can be absorbed for sufficiently small g.
Equivalently, after division by kappa^2 exp(-lambda s)g^2 the limit is
-2|chi_p(s)|^2, uniformly on [0,T]. The sign is a deficit relative to the
vacuum coincidence background. It is not a positive photon click rate.
The first-event rates have no contrast. The condition of no previous event
and its survival probability are part of this actual event statistic.

A finite narrow-band estimate makes the propagation statement precise.
In a traveling normal-mode basis write d_p(q,r)=exp(i q dot X_p)d_0(q,r),
with r a polarization. Suppose the occupied modes lie in a ball of physical
wavevectors of radius sigma about q0, within the Brillouin zone and away
from q=0. Put A=sum |alpha_(q,r) d_0(q,r)| and
M=sup_ball ||Hess_q omega||. Linearizing only the frequency gives a packet
chi_lin whose envelope is translated by v0 s, v0=grad_q omega(q0), and

    |chi_p(s)-chi_lin,p(s)| <= A M |s| sigma^2/2,
    ||chi_p(s)|^2-|chi_lin,p(s)|^2|
                         <= A^2 M |s| sigma^2.         (10)

Both amplitudes are at most A, so the second inequality follows directly
from the first. For the source dispersion an explicit Hessian is
c a_lattice [diag(cos k)/sqrt(D)-sin k sin(k)^T/D^(3/2)].
Its norm is at most 2c a_lattice/sqrt(D). If the whole ball is inside the
principal Brillouin zone, D>=4|a_lattice q|^2/pi^2 gives the sufficient
M<=pi c/(|q0|-sigma). Thus (10) is a finite-sum controlled group-translation
statement; curl/oscillator weights remain in the envelope. It is not a
universal statement about the peak of an arbitrary broad or multi-pulse
packet, nor a claim of a uniform astronomical propagation error.

### 4. Limits and the remaining measurement bridge

Equations (1)-(3) are exact for the stated full common rotor target. Equation
(9) is its prepared weak-field, fixed-volume, fixed-time asymptotic and its
next-event separation u->0 boundary. It does not assume no second birth or
discard any of the first output. The detector effect loses its contrast if
that output is prematurely dephased, which makes full matter-field coherence
load-bearing in this connection to records.

The microscopic spin model's bare jump annihilates its initial P state at
exactly zero microscopic time. A common-target convergence theorem on fixed
intervals does not permit exchanging that microscopic initial derivative
with its limit. This note makes no such claim. A microscopic finite-bin
comparison must preserve the ordered limit and its event-register estimates.

Sections B and C below address positive finite bins and their ordered
microscopic comparison. The supported window still shrinks with g;
it is not a fixed-duration detector claim.

The construction is conditional on the selected compensated law, coupling
family, rotor/packet preparation, time and spatial labels, coherent unresolved
hop paths and recorded jump marks. It neither prepares an astronomical
source nor calibrates a, c, g or kappa. It gives no efficient stable detector,
long-duration full-state photon theorem, fixed-coupling deconfined phase,
cosmological identification or new fit to photon timing data. Those remain
necessary before the conditional timing constraints can become a prediction
of what we observe. The result here is a concrete mathematical connection
between these supplied waves and the original formation-record statistics.

## B. A sufficient finite window from the full magnetic interaction picture

The prebirth graph estimate is explicitly attributed to the finite-bin PRE.
The new interaction-picture argument and smooth-observable contrast are
the root derivation; the complete comparison is retained in the review packet.

### 1. Fixed setting and claim

Fix the finite even cubic torus of sides at least six, the original resolved
marks j,l in the readout geometry, a,c,kappa>0, the prepared vacuum and a fixed
normalized one-particle packet, and I=[t,t+h] in a fixed bounded interval.
Write tau_*=a/c and use

    K=g^2/(2 tau_*), delta=1/(4 tau_* g^2), 0<g<=g0<=1.

Let phi_n,g(s), n=0,1, be the normalized exact initial-sector unitary orbits
after removing the scalar energy; the separate first-event survival is
exp(-lambda s), lambda=30 kappa V. The full postbirth generator is

    A_g=-i(K D_+ + delta H4_+) - kappa Lambda_+/2,
    eta_n(s)=B_j phi_n,g(s), M=B_l^*B_l,
    Lambda_+=sum over ALL original marks m of B_m^* B_m.

No postbirth field-only Hamiltonian or dephasing is substituted.
The event is the first original event j in I followed by the next event l
within lag b, with no intervening event and unrestricted later history:

    P_n(g;I,b)=kappa^2 int_I exp(-lambda s)
                    int_0^b <exp(u A_g)eta_n,M exp(u A_g)eta_n> du ds.

Put S_I=int_I exp(-lambda s)ds and
H_I=int_I exp(-lambda s)|chi_p(s)|^2 ds, with the readout packet amplitude.
At fixed graph and other fixed inputs, the claim is

    P_1-P_0 = -2 kappa^2 b g^2 exp(-g^2 v_p/2) H_I
              + kappa^2 b O(g^4 + b/tau_*),                    (1)

uniformly for 0<b<=r0 tau_* g^2, where r0>0 is fixed. In particular

    b/(tau_* g^2) -> 0                                        (2)

is sufficient to preserve the normalized coefficient -2H_I, which is
nonzero when H_I>0.
This improves the earlier sufficient b=o(tau_* g^4) estimate. Neither
condition is an optimality claim. A fixed physical b as g->0 is not covered.
All constants can depend on graph, tau_*, kappa tau_*, packet, cutoff and T.
No volume, spacing, or growing-time uniformity is asserted.

### 2. The actual prebirth graph estimate

On the parent's transverse quotient Q, remove the initial scalar and write

    H_g=K Q_E+V_g, Q_E=-Delta_Q,
    V_g=(tau_* g^2)^(-1) sum_p (1-cos(c_p.A)) >=0.

The explicit cutoff finite-Hermite preparation obeys ||H_g phi_n,g(0)||<=C/tau_*.
The parent's residual and Gaussian cutoff estimates prove this on D(Q_E).
Self-adjoint evolution preserves that domain and graph norm, at every s.

For smooth phi, integration by parts gives

    ||H_g phi||^2 =
       K^2||Q_E phi||^2 + ||V_g phi||^2
       +2K int V_g |grad phi|^2 -K int (Delta V_g)|phi|^2.

Here K||Delta V_g||_infinity<=C/tau_*^2 independently of g. Positivity and
approximation on the Q_E graph core therefore imply

    ||Q_E phi_n,g(s)|| <= C g^(-2),
    ||grad phi_n,g(s)|| <= C g^(-1).                           (3)

The second inequality follows from <phi,Q_E phi> and normalization.
This is the stronger estimate in finite-bin-photon-independent/PRE.md,
section 3, used with explicit attribution. It is a graph estimate on the
ACTUAL orbit, not an unbounded operator applied to the vector-norm error.

### 3. Magnetic evolution is a smooth matrix multiplier

Work temporarily on all link angles with the finite matter space in the
postbirth record-number sector. Electric translations are multipliers
exp(i d.A); every entry of H4_+, B_j and M is a finite trigonometric polynomial
with finite matter matrices. They are bounded smooth multipliers, independent
of g. This representation restricts to the physical Gauss space. It does not
assert that every postbirth state remains in the initial zero-winding sector.

Let

    V_g(u)=exp(-i delta u H4_+), r=u/(tau_* g^2).

For 0<=r<=r0, V_g(u)=exp(-i r H4_+/4) and its link-angle derivatives through
any fixed finite order are bounded uniformly in r and g. This follows by
differentiating the finite-matrix exponential using its Duhamel integral;
compactness and the fixed graph bound all coefficients.

In each matter word D_+ is a constant-coefficient diagonal polynomial in E
of degree at most two, with bounded word-dependent coefficients. It may
have unconfined directions. Applying the product rule to V_g(u) B_j phi,
and using (3), gives

    ||D_+ V_g(u) B_j phi_n,g(s)|| <= C g^(-2)                  (4)

uniformly in s and 0<=r<=r0. The bound follows from the sum of ||Q_E phi||,
||grad phi|| and ||phi||; every multiplier derivative is bounded. Smooth
physical electric words form a core; approximation proves that all these
vectors lie in D(D_+), and that u->V_g(u)eta is continuous in that graph norm.
The full torus derivatives of the initial quotient function are bounded by
the same derivatives on its orthogonal transverse subspace.

The contraction U_g(u)=exp(u A_g) and variation of constants now yield

    U_g(u)eta - V_g(u)eta =
      int_0^u U_g(u-v)[-i K D_+ -kappa Lambda_+/2]V_g(v)eta dv.

Equation (4), bounded loss and ||eta||=sqrt(5) imply

    ||U_g(u)eta_n - V_g(u)eta_n|| <= C u/tau_* .               (5)

Thus the magnetic-only and full squared-effect expectations differ by at
most C u/tau_*, separately for each input. The magnetic-only propagator is
an estimation device, not a replacement physical dynamics.

### 4. A smooth-observable contrast lemma

Write psi_n(s) for the harmonic reference vacuum or one-particle packet
and widehat I_g for the normalized cutoff map. Both reference probability
densities on the transverse coordinates x are even under x->-x. This holds
for any complex superposition within the one-particle subspace. The cutoff
need not be even: its departures from one occur in exponentially small
Gaussian tails. The parent gives

    ||phi_n,g(s)-widehat I_g psi_n(s)|| <= C g^2 +C'exp(-d/g^2)

uniformly on the fixed interval.

For any smooth scalar F on Q, subtract F(0). Taylor expansion, the vanishing
linear reference moment and fixed Gaussian polynomial moments give

    |<reference_1,F reference_1>-<reference_0,F reference_0>|
        <= C g^2 ||F||_(C^2).

Also ||(F-F(0))reference_n||<=C g ||F||_(C^1) plus an exponential tail.
Using exact normalization to cancel F(0), the cross terms with the vector
error are O(g^3)||F||_(C^1), and the error-square term is
O(g^4)||F-F(0)||_infinity. Consequently

    |<phi_1,F phi_1>-<phi_0,F phi_0>|
        <= C g^2 ||F||_(C^2).                                (6)

The norm can use a fixed finite chart atlas of the compact quotient.
Subtracting a constant from F does not change the left side. This estimate
requires the particular two preparations and their fixed-time approximation;
it is not a statement about arbitrary low-energy states.

To apply it to the magnetic expectation, compress

    F_r(A)=<q_initial|B_j^* exp(i r H4_+/4)
                         M exp(-i r H4_+/4) B_j|q_initial>.

This is a scalar smooth multiplier. It is gauge invariant because the
operator returns to the initial fixed matter word. It need not be invariant
under constant link-angle translations. The initial wavefunctions are.
Haar-average F_r over that harmonic translation subgroup; equivalently
compress to the initial zero electric-winding sector. The average descends
to Q, preserves the expectation, and does not increase derivative bounds.
This is a projection only of the TESTED initial-sector multiplier; it does
not delete postbirth winding states or paths.

The averaged F_r-F_0 has C^2 norm <=C r for r<=r0, by the differentiated
finite-matrix exponential and the original finite trigonometric coefficients.
Applying (6) to this difference yields

    |Delta_magnetic(r)-Delta_magnetic(0)| <= C g^2 r
                                          = C u/tau_* .       (7)

No field-only postbirth limit, parity of the actual evolved state, or
normalization conditional on a second event was used.

### 5. Integrated contrast and statistical scope

Combining (5) for both inputs and (7) gives, for the exact full lag effects,

    |Delta_full(u)-Delta_full(0)| <= C u/tau_* .                (8)

Section A gives
Delta_full(0)=-2g^2 exp(-g^2 v_p/2)|chi_p(s)|^2+O(g^4).
Multiplication by kappa^2 exp(-lambda s) and integration proves (1).
For (2), H_I>0 gives a strictly negative finite-bin coefficient.

The independent magnetic-lag PRE also spells out the following consequence
of (1). If H_I>0, there exist beta_*>0 and g_*>0 such that
0<b<=beta_* tau_* g^2 and 0<g<g_* imply

    -3 kappa^2 b g^2 H_I <= P_1-P_0 <= -kappa^2 b g^2 H_I.

Choose beta_* small enough to bound the O(b/(tau_*g^2)) normalized
remainder, and then choose g_* for the O(g^2) remainder. This proves
a deficit for a small fixed multiple of the magnetic time scale; it does
not give the exact boundary coefficient at that fixed multiple. No useful
numerical value of beta_* for the original graph is supplied.

The vacuum probability has, for r<=r0, the separate conservative estimate

    P_0=kappa^2 b [25 S_I +O(g^2 + b/(tau_* g^2))].

Indeed |F_r-F_0|<=C r, plus (5), and the boundary vacuum value is
25-g^2 v_p+O(g^4). Under (2), P_0~25 kappa^2 b S_I. This estimate does not
claim that the subleading vacuum term is uniformly resolved.

With a supplied known vacuum baseline and N independent resets/trials,
the old count diagnostic still has
SNR^2~4N kappa^2 b g^4 H_I^2/(25 S_I).
For b=tau_* g^(2+zeta), zeta>0, the sufficient fixed-SNR repetition scaling
becomes N of order g^(-6-zeta). Sampling both arms adds the second variance.
For a sufficiently small fixed b=beta tau_* g^2, the preceding two-sided
contrast and positive baseline bounds give the sufficient order g^(-6),
without the exact coefficient above. This fixed-beta consequence is
attributed to the independent magnetic-lag PRE.
These are protocol-specific sufficient scalings, not an optimal detector
bound or a claim that resets and preparations are physically implemented.

Section C proves the microscopic finite-bin comparison at each fixed
positive (g,b). A subsequent diagonal spin choice can preserve
this smaller signal by making each probability error o(kappa^2 b g^2).
No microscopic rate, economical spin size or simultaneous limit is supplied
by this note.

The allowed lag scale is tau_* g^2, with tau_*=a/c fixed, and shrinks with g. The result supplies no
fixed-duration laboratory detector, source preparation, calibration of a,c,g
or kappa, stable long-time photon phase, astronomical propagation theorem or
empirical agreement. It removes one overly restrictive sufficient estimate
inside the supplied model.

## C. The microscopic original-record probability

### 1. Precisely which parent statement is used

At fixed finite graph and fixed positive K,delta,kappa, the pinned
BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET note proves a uniform-in-spin
O(epsilon) approximation of the full microscopic density from P initialization
to its P target. It explicitly allows finite classical event/count registers
when compensation acts trivially on the register and preserves record number.
The LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT note proves strong trace-class
convergence of that spin target to the full rotor target, uniformly on fixed
time intervals, with epsilon^2 S(S+1)=delta/K. The spin target retains the
same KD and bounded strongly converging magnetic/jump terms. Both are
provisional supplied-model dependencies. Their bounds are not uniform as
K,delta, the graph or the observation horizon vary.

The following argument spells out the required registers and time partitions.
It does not infer a trajectory law from unconditioned density convergence
alone. No arbitrary continuously conditioned microscopic-history theorem is
assumed from those parents.

Initially N0=|A| and each formation increases record number N by two.
Hamiltonian and no-event evolution preserve N. Thus both microscopic and
common processes have at most M=floor(|B|/2) events on this finite graph.
The graph and M stay fixed. The alphabet J consists of the original recorded
marks: resolved edge/sign marks or coherent edge marks, as actually chosen.
The two signs of a coherent mark are not separately recorded or dephased.

### 2. Finite deterministic time bins preserve the original instrument

Choose a finite partition 0=t0<t1<...<tm=T*. Use a classical register basis
consisting of all words w of length at most M in pairs (bin index, original
mark). On interval r, replace each channel j_S in the bookkeeping dilation
by j_S tensor V_(r,j), where V_(r,j)|w>=|w,(r,j)> when |w|<M and is zero
at length M. Distinct prefixes have distinct images for a fixed channel,
so each V is a partial isometry of norm at most one. Its norm is one
when M>=1; M=0 has no two-event readout and is trivial. The register begins empty.
Hamiltonian, compensation, W and T act trivially on it.

The actually reachable subspace satisfies N=N0+2|w|. At |w|=M the physical
formation channel already vanishes because fewer than two empty sites remain.
On this subspace the original loss is unchanged. The register density stays
classical, and tracing it out gives exactly the original unmonitored system
density and its original mark instrument. The word merely stores observed
marks and time bins; it is not an added physical reservoir, reset or law.
No part of the system's postbirth matter coherence is measured by this label.

On each interval the lifted data satisfy the parent's assumptions:

 [W tensor I,j_S tensor V]=-j_S tensor V,
 (j_S tensor V)(P tensor I)=0,
 [C_S tensor I,W tensor I]=0,
 ||j_S tensor V||<=||j_S||.

The canonical cluster rotation remains U_S tensor I. The effective channel
is exactly B_(j,S) tensor V_(r,j), and the effective Hamiltonian is h_S
tensor I. The number of generator channels at a time is the original |J|;
the register is finite for every fixed partition. Thus the parent's density
argument applies separately on every interval. At a switch, target P states
remain in P. Contractivity and a finite triangle inequality propagate the
error through all m intervals, including physical-spin initial approximants.
No estimate uniform as m tends to infinity is asserted.

The common-rotor proof also lifts to this finite register: KD is unchanged,
all remaining factors are uniformly bounded and strongly convergent, and the
same interaction-picture Dyson/finite-rank argument applies. Finite products
of these semigroups therefore converge on each fixed input. Hence at fixed
partition, all recorded word probabilities converge:

  P_micro,S(word belongs to A_partition)
                  -> P_rotor(word belongs to A_partition),       (1)

for every subset of the finite word alphabet. The subset can include any
later marks; reading the first two entries does not forbid later events.
Equation (1) is a bounded register effect evaluated on the converging full
joint density. It does not require bounded microscopic jump intensity.

### 3. Pass from rectangular bins to a positive relative-time window

Let I=[t,t+h], h>0, and b>0 be fixed, with T*>t+h+b. Define A to mean:
the first mark is j at s in I, the next mark is l at s+u with 0<u<=b.
There is no intervening event; all events after the second are unrestricted.
If fewer than two events occur, A is false.

In the common rotor model the full jumps are bounded. Put

 R = kappa ||sum_j B_j* B_j|| <= kappa sum_j ||B_j||^2 < infinity.

Every conditional no-event state has instantaneous total hazard at most R.
Equivalently its next-waiting-time density is bounded by R, directly from
contractivity of the full no-event semigroup and the bounded loss. This also
bounds the first-event time density. No unbounded Hamiltonian derivative or
smoothness of the initial field state is needed.

For a partition of mesh at most eta, let A_eta^- contain the word bins every
realization of which satisfies A, and A_eta^+ contain those with at least one
realization satisfying A. Use the stored word order even when the first two
events have the same bin. Then, for both microscopic and target trajectories,

 A_eta^- subset A subset A_eta^+.

A target trajectory in A_eta^+ minus A_eta^- has first time within eta of
one of the two endpoints of I, or second-minus-first time within 2 eta of b.
Possible exact endpoint coincidences have target probability zero. Once eta
is sufficiently small compared with the positive margins, the density bounds
and conditioning on the first event give the sufficient estimate

 P_rotor(A_eta^+ minus A_eta^-) <= 8 R eta.             (2)

The first endpoints contribute at most 4R eta; the waiting-time interval at
b contributes at most 4R eta. The first-event distribution integrates to at
most one. Mark restrictions only reduce these upper bounds. One can use a
larger harmless constant at partition endpoints without changing the proof.

Apply (1) at each fixed partition before sending eta to zero. The sandwich
and (2) prove

               P_micro,S(A) -> P_rotor(A)             (3)

at fixed graph,K,delta,kappa,I,b. There is no need for a uniform microscopic
hazard bound, which would be false at the supplied epsilon^-2 jump scaling.
The same sandwich argument applies to these events for arbitrary normalizable
initial rotor fields with trace-norm convergent physical-spin approximants.
It does not imply convergence of time-density derivatives, total variation
of all continuous record laws, or uniform convergence for shrinking b.

### 4. An ordered microscopic realization of the packet contrast

Now use the two-mark and finite-bin arguments in Sections A and B.
Use one fixed cubic graph, fixed c,a,kappa,I, and the supplied family
K_g=cg^2/(2a), delta_g=c/(4ag^2). For each fixed g, prepare the normalized
projection of the compact vacuum or one-particle rotor packet into the physical
spin box, in the bare P matter sector. Projection converges in norm as S grows;
the parent theorem does not require replacing this by a dressed initial state.

For each fixed g and b>0, (3) applies with

 epsilon(g,S)^2 S(S+1)=delta_g/K_g=1/(2g^4).

Let g_n tend to zero and b_n>0 obey the sufficient small-bin condition in the
finite-bin theorem in Section B. Its probabilities satisfy

 [P_rotor,1(g_n;I,b_n)-P_rotor,0(g_n;I,b_n)]
                    /(kappa^2 b_n g_n^2) -> -2 H_I,    (4)

where H_I is its survival-weighted packet-intensity integral. At each n first
hold g_n,b_n fixed, then choose a sufficiently large integer S_n so that for
both preparations the error in (3) is at most

 eta_n kappa^2 b_n g_n^2,          eta_n -> 0.

This is possible by (3); choose S_n still larger if necessary to make
S_n increase and epsilon(g_n,S_n)->0. Therefore the same normalized contrast
limit (4) holds for the actual microscopic recorded event probabilities.
For H_I>0 it is the same negative coincidence contrast, not a positive click.
All physical matter sectors and the unchanged original instrument remain.

This is an existence/ordered-diagonal statement. It provides neither a rate
for S_n nor a finite apparatus or resolution cost. The spin-to-rotor strong
convergence and parent constants are not uniform in g, shrinking bins or
volume. A prescribed simultaneous schedule cannot be substituted. In
particular the vanishing bare microscopic jump at time zero has never been
equated to the target instantaneous rate. A quantitative, feasible model of
source preparation, clocks and detection, and independently selected physical
parameters are still needed before this becomes a prediction for observations.

### 5. A separate finite model tests why the order matters

A five-state supplied penalty model has states P0,Q0,P1,Q1,P2, record numbers
0,0,2,2,4 and penalties 0,1,0,1,0. Take T=-(|Q0><P0|+|Q1><P1|+adjoint),
C=|P0><P0|+|P1><P1|, and j=|P1><Q0|+|P2><Q1|. It satisfies the abstract
parent selection rules, but is explicitly not the physical cube or cubic
rotor model. H2^C=H4^C=0 and its effective original mark is
B=|P1><P0|+|P2><P1|. Thus the target has two successive exponential waits
with rate kappa and then stops.

In either active microscopic block the no-event matrix is

 A_e = -i delta epsilon^-4 [[epsilon^2,-epsilon],[-epsilon,1]]
                         -kappa/(2epsilon^2) diag(0,1).

After each actual event the next block begins in bare P. If lambda_s,lambda_f
are distinct eigenvalues, the Q amplitude is

 c_e [exp(lambda_s u)-exp(lambda_f u)],
 c_e=i delta epsilon^-3/(lambda_s-lambda_f).

At a double root the expression is interpreted by its continuous limit;
the displayed control parameters and the small-epsilon limit avoid that
coalescence. The waiting density is kappa epsilon^-2 times its squared modulus. Integrating
its three exponential terms gives the exact CDF F_e(u). In particular the
finite-bin event probability is

 [F_e(t+h)-F_e(t)] F_e(b)
         -> [exp(-kappa t)-exp(-kappa(t+h))][1-exp(-kappa b)]

for fixed b>0. However, when b=epsilon^6, the microscopic short-time expansion
gives F_e(b)/(kappa b)~delta^2 epsilon^4/3 ->0, whereas the target ratio tends
to one. The expansion is controlled since b||A_e||=O(epsilon^2). This is a
concrete order-of-limits counterexample in the stated separate model; it is
not a claim that this is the cube's sharp resolution boundary or a universal
obstruction to its controlled diagonal sequence.

The accompanying small control checks these exact selection rules, fixed-bin
and shrinking-bin CDFs, and finite time-grid sandwiches for the two-wait target.
It does not simulate the cubic photon, prove the conditional parent theorem,
or supply a quantitative spin schedule for (4).

## D. Which packets can the family of probes distinguish?

This extension is attributed to the independently sealed readout PRE, rather
than to the author's earlier sealed derivation. Let D=C^TC on the finite
transverse quotient, let xi_s be the normalized one-particle mode vector,
and let Omega=sqrt(D). Section A's local amplitude is the component of
C D^(-1/4) xi_s /sqrt(2) at plaquette p. Therefore

    sum_p |chi_p(s)|²
      = (1/2)<xi_s,D^(-1/4) C^T C D^(-1/4)xi_s>
      = (1/2)<xi,Omega xi> >0.

Since D is strictly positive on that quotient, some plaquette satisfies
|chi_p(s)|² >= sqrt(lambda_min(D))/(2 N_p), where N_p=3V.
Every plaquette admits the legal rotated/reflected/translated mark geometry
when the periods are at least six. Thus every nonzero transverse packet has
some nonzero leading probe response at each fixed first time. A particular
plaquette can be dark. The finite sum of mode exponentials is analytic, so
a nonidentically-zero amplitude has positive weighted squared integral on
every nondegenerate first-event interval.

This is an energy-weighted family of responses, not a photon-number
calibration, a universal single-site response or a single-shot label.
The survival factor exp(-30 kappa V s) remains part of every statistic.

## E. Evidence and unresolved observation bridge

Independent readout PRE and released POST agree on the exact resolved effect,
boundary contrast and fixed-band translation. The first coherent-mark shortcut
is restricted to the boundary, as POST requires. The finite-bin PRE separately
supplied the stronger actual prebirth electric graph estimate used in Section B.
The magnetic-lag blind PRE independently reconstructs the larger window;
its released POST supports the analytic argument and normalization repair,
with the dark-packet qualifier applied here. Its fixed-beta corollary is
explicitly attributed in Section B. The numerical quadrature remains a
finite probe without an integration-error enclosure.
The microscopic PRE independently constructs a classical prefix/archive
register, retaining all later physical jumps, and proves the same fixed-window
implication and selectable diagonal. Its released POST supports the root
comparison, with the register norm and double-eigenvalue qualifications
applied in Section C. Its separately specified six-state example
and the author's five-state example both illustrate why an arbitrary shrinking
schedule is not justified; neither is a cubic-model failure result.

The canonical runner discloses its author-control provenance. It evaluates
primitive paths on the side-six cubic torus and two auxiliary graphs; separate
one-circle, finite-Fock and finite-band controls; a separate five-state
microscopic waiting model and target time-bin brackets; and a separate
two-component rotor Galerkin probe with the full noncommuting electric,
magnetic and loss terms. These auxiliary systems are not full cubic
postbirth propagation, interval enclosures or observational data.

The Galerkin probe's initial cutoff check failed because a small numerical
unitary normalization error was amplified by the common coincidence
background. The full failed and diagnostic attempts are preserved. Restoring
the theoretically exact normalization resolved the discrepancy without
relaxing the cutoff threshold. A fresh publication execution is recorded
separately from the historical and independent controls.

The result retains the original formation instrument and all physical
postbirth matter sectors. It neither prepares the assumed sources nor
implements clocks, resets, an efficient detector or a stable photon phase.
The window shrinks in microscopic units a/c. Fixed physical time resolution,
large volume, long propagation, finite-coupling errors, source emission,
parameter selection and empirical agreement remain open.

The qualified comparison is between probabilities of specified original
records under supplied preparations. A null timing constraint with an
adjustable lattice spacing is not confirmation over Maxwell theory. No
new axiom, universal obstruction, audit verdict or TOE completion is asserted.
