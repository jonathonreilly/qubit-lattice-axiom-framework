---
claim_id: uniform_autonomous_resource_density_for_original_rotor_records_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: 'For the supplied original compensated rotor law from Omega, fixed finite horizon, regional binned original histories and quantum output, a positive time-independent enlarged-cell local apparatus has finite dimensions, coupling bounds and initial energy density independent of torus volume. The source-energy density, clock debit, residual interaction and passive-read mean energy exchanges have separate controlled errors. Supplied law, preparation, program, apparatus and readout; finite tolerance and finite observation grid.'
upstream_dependencies:
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - cubic_original_record_response_at_fixed_couplings_bounded_theorem_note_2026-09-26
runner: scripts/uniform_autonomous_original_record_resource_density_2026_09_30.py
---

# Uniform autonomous resource density for regional original rotor records

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
next_trace_action: investigate source selection and microscopic realization with the original readout preserved
conditional_surface_status: supplied rotor law, initial state, finite apparatus, program and readout
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: constructive finite-horizon local approximation with volume-independent apparatus resources under stated imports
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

For every fixed positive K, delta, kappa, finite T>0, finite source region X,
finite set F of monitored original birth centers, finite passive observation
grid, and positive process and mean-energy tolerances, there is one finite
choice of local apparatus dimensions, finite-range coupling bounds and initial
energy per cell, independent of the even torus side L>=24, for which a positive
time-independent Hamiltonian approximates the original binned F-history and X
quantum output from Omega, and its clock-energy debit supplies the original
source mean-energy density gain up to the prescribed source, interaction and
read-energy allowances.

This is the target proved below. The law, quantum probability interpretation,
couplings, initial state, clocks, programmed couplings and blank memories are
explicitly supplied. The implementation uses enlarged cells with an explicit
finite qubit encoding. The original source factors and original coherent or
resolved mark maps are kept. All later births remain in the target process.
There is no reset, rephasing or timed gate intervention in the closed run.
Reading at the stipulated grid remains a supplied external operation, with a
separate energy allowance. The theorem concerns unconditional output trace norm
and mean energies; it does not assert a bound after division by rare outcome
probabilities.

The proof is self-contained after the definition of the supplied source law.
Sections 2-3 prove its local cutoff and moment transfer. Section 4 proves a
dimension-independent finite-cell influence estimate. Sections 5-6 retain the
actual marked instrument in local collisions and dilation. Sections 7-9 give
the pulse, ideal-clock and positive finite-clock construction in a noncircular
resource order. Sections 10-11 prove the source/controller ledger and resource
encoding. Each of these is proved here; no absent open-branch theorem is used
as an unexplained premise. There is no missing lemma within this conditional
target. Native one-qubit-per-original-site selection, the microscopic limit of
the supplied law and physical apparatus selection are separate questions.

## 1. Source, observation topology and imports

The [common-field limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
defines the supplied effective law. Its [local pair form](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md)
and [original-record source](CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md)
fix the words and original readout used here. Only these definitions and the
local pair identity are imported; their later response or band conclusions
are not used. Bounds needed here are rederived below.

On an even cubic torus let A and B be the two parity classes and N=L^3/2.
The final source factor is C^2 at A, C^3 at B, and six integer rotors stored
at each B endpoint. On the intermediate hard-core site space |0>,|+>,|-> put
c_(x,q)=|0><q|, n_x=sum_q |q><q|, q_x=|+><+|-|-><-| and U_e|m>=|m+1>.
Links are oriented from A to B. Operators on distinct factors commute. P
projects onto every A occupied. Define

    F_a = sum_(d~a,q=+/-1) c_(d,q)* c_(a,q) U_ad^(-q),
    j_(a,b,sigma) = c_(a,sigma)* c_(b,-sigma)* U_ab^sigma,
    B_(a,b,sigma) = P j_(a,b,sigma) F_a P,
    S_ac = F_c F_a P,
    A_ac = -2 delta S_ac* S_ac,
    D = sum_(a->b) (1-n_b) E_ab(E_ab-q_a),
    h = K D + sum_(unordered a,c: dist(a,c)=2) A_ac.       (1.1)

The sum has 9N pairs. The div convention is sum_b E_ab at A and
-sum_a E_ab at B; the supplied physical subspace obeys div E=q-1_A.
Omega has all A charges +1, all B empty and all E=0. In a nonzero complete
birth word, F_a sends the old charge q to an empty d; j creates sigma at a
and -sigma at a distinct empty b. E_ad changes by -q and E_ab by sigma.
These changes preserve each Gauss equality. S_ac* S_ac also preserves Gauss.
Births increase N_B by two. Magnetic terms and loss terms preserve N_B;
their reverse paths are included in (1.1).

Fix either the resolved labels m=(a,b,sigma) and L_m=sqrt(kappa)B_m, or the
coherent labels m=(a,b) and

    L_(a,b)=sqrt(kappa)[B_(a,b,+)+B_(a,b,-)].             (1.2)

There is no normalization in this sum. The coherent apparatus copies b and
does not copy sigma. Put Gamma_a=sum_(m centered at a) L_m*L_m. The original
GKSL generator is -i[h,rho]+sum_m(L_m rho L_m* - {L_m*L_m,rho}/2).
The marked instrument is its quantum-jump instrument with the same L_m,
all losses and every unobserved gain. This probability/update interpretation
is supplied, as are time, units with hbar=1 and the meaning of these records.

We compare the cq state of the binned ordered F-history and quantum output
on X at a prescribed finite grid including 0,T. Passive reads copy or
dephase already completed flags and retain their values; they do not change
the source intentionally or introduce feedback. An untouched external
reference and passive classical memory can be carried throughout. Since the
source input is the specified pure Omega, this does not assert an arbitrary
entangled source-input theorem. Matrix-amplified intermediate estimates are
used to telescope the actual correlated states. Histories may retain all
finite words; multiple events in a bin are not discarded from the target.
Exact continuous timestamps are integrated into bins. The norm is the trace
norm of this unconditional joint output, with maximum two.

The resource choice may depend on K,delta,kappa,T,X,F,grid and tolerances,
but not on L. It works uniformly at every translate of a fixed local test,
even when the chosen proper coloring varies with the torus. This uniformity
also allows summing local source-energy errors and dividing by N. The result
is not a fixed global trace-error claim for all records as N grows.

### Elementary all-sector bounds

If o neighboring B sites of a are occupied, the outward incidence matrix
has at most 6-o nonzero entries per input and o+1 per output. Its entries
are unit rotor shifts between charge words. Cauchy-Schwarz on this bipartite
incidence gives ||F_a||^2<=(6-o)(o+1)<=12. For a fixed birth edge the analogous
degrees are 5-o and o+1, so ||B_res||^2<=(5-o)(o+1)<=9. The two sigma ranges
in (1.2) are orthogonal, hence ||B_coh||^2<=18. After F_a, exactly 5-o empty
neighbors remain for birth, with two charge choices. Thus, in that block,

    Gamma_a = 2 kappa(5-o) F_a*F_a,
    ||Gamma_a|| <= g0 := 80 kappa.                      (1.3)

The bounds for o=0,...,5 are respectively 60,80,72,48,20,0 times kappa;
o=6 is zero. They hold in both instruments. The sum of individual squared
jump norms at a is <=108 kappa. Also ||A_ac||<=288 delta. A center has
18 distance-two A neighbors. Define A_a=(1/2)sum_c A_ac and

    v0=2592 delta,   ||A_a||<=v0,   h_a=K D_a+A_a.      (1.4)

Here D_a is the sum of the six electric terms at a and sum_a h_a=h.
Integers m obey m(m-q)>=0 for q=+/-1, so D>=0. The bounds are independent
of the number of previous births and total volume.

## 2. Local rotor propagation and original histories

This section supplies the locality argument for unbounded integer rotors;
a bounded-spin locality theorem is not substituted for it.

Every electric summand is diagonal and finite-support, and all such summands
commute. In alpha_t(O)=exp(iKD t)O exp(-iKD t), all electric terms disjoint
from the support of a bounded local O cancel. Terms meeting that support add
only one nearest-neighbor halo. Terms at the new halo do not cause further
growth: they were disjoint from O and commute with the terms already kept.
The conjugates are strongly and strongly-adjoint continuous on each local
Hilbert space, with unchanged norm. Norm continuity on all B(H_local) is
not assumed.

On a fixed finite graph, conjugation is strongly continuous on trace class.
The electric interaction-picture bounded magnetic/dissipative perturbation
therefore has strong trace-class integrals and an absolutely convergent
Dyson series. A finite-time partition into constant Lindblad coefficients
converges on trace class by its integral equation, since each coefficient is
strongly continuous and uniformly bounded. Each approximate propagator is
CPTP; the limit is CPTP and normal in the adjoint picture. We use adjoint
strong or ultraweak integrals, not a norm-Bochner integral on B(H).

Group half the magnetic pairs and all dissipators at each center a. In the
electric picture a grouped coefficient has cb norm at most

    lambda=5184 delta+160 kappa                         (2.1)

and support inside the radius-four ball about a, with at most 129 cells.
It annihilates every observable supported disjointly. The factors 5184 and
160 are 2||A_a|| and 2||Gamma_a||. A cell belongs to at most 129 such balls.
For an observable initially on x cells, after j coefficients its support
has at most x+129j cells, so the number of possible next centers is at most
129(x+129j). With q=max(1,ceil(x/129)), the number of length-j contributing
strings is bounded by 16641^j(q)_j. Time-simplex integration gives, for
z=16641 lambda t<1, the tail after degree m,

    ||tail_m|| <= ||O|| R_(q,m)(z),
    R_(q,m)(z)=sum_(j>m) binom(j+q-1,j) z^j.            (2.2)

One initial electric halo has at most 7|X| cells. A contributing step moves
at most eight lattice edges. A canonical patch containing B_(8m+1)(X)
has identical coefficients through degree m to the full graph. The difference
is at most twice (2.2), uniformly over the local observable unit ball and
matrix amplifications. Counts overestimate also on small tori. If a buffer
wraps around, use the entire torus; its cardinality is no larger than the
same cubic-ball overcount.

For any finite T, subdivide into a finite number of intervals with
16641 lambda t<1/2. On the last interval approximate the local output by a
normal CP contraction on a finite patch; apply the same argument backwards
to the larger support on each preceding interval. Telescope by contraction.
At each step a finite m makes (2.2) as small as desired. This produces a
finite spatial patch and arbitrarily small error for the entire interval,
uniform in L and local matrix dimension. No exponential-in-T efficiency
claim is needed.

For monitored centers F, remove only their gains from the background
generator, retaining their losses and every unobserved gain. This gives a
normal completely positive trace-nonincreasing no-monitored-event map.
Insert the actual marked gains at specified ordered times. The background
coefficients still annihilate the identity outside the enlarged fixed anchor
containing every monitored gain support and the output electric halo; take
x<=7|X|+25|F|. The number of background strings and their time integrals obey
the same bound (2.2). Sum specified monitored labels using
sum_(m at a)||L_m||^2<=108 kappa. At any order the sum of absolute insertion
weights is bounded by exp(108 kappa |F|T). Hence it suffices to choose the
spatial error smaller by this finite factor. Equivalently one may first cap
the number of monitored insertions and then remove that cap: the probability
of at least j monitored events satisfies

    Pr(N_F(T)>=j) <= (g0 |F|T)^j/j!.                   (2.3)

To prove (2.3), integrate the j-th factorial moment density using the rate
effect sum_(a in F)Gamma_a<=g0|F| and contractive intervening propagation.
This counts j selected events in a trajectory and allows other events between
them. It does not assume the full torus has few events. The resulting
instrument comparison is in cq trace norm after integration over timestamps,
including every original mark and all later births. Binning and a finite
sequence of passive reads are CP contractions, so the same construction and
finite telescoping apply. All statements are on the ambient tensor algebra;
restriction to Gauss-preserving states is made afterwards.

## 3. Uniform prepared field box and energy transfer

Let P_R project onto |E_e|<=R for every edge, and compress each COMPLETE
magnetic term and jump:

    A_ac,R=P_R A_ac P_R,  L_m,R=P_R L_m P_R,
    Gamma_a,R=sum_(m at a) L_m,R* L_m,R,
    h_R=K D_R+sum A_ac,R,   h_+=h_R+v0 N I>=0.          (3.1)

The internal F steps in A_ac are not individually clipped. In particular
P_R S* S P_R differs in general from (P_R S P_R)* (P_R S P_R).
Compression decreases each bounded term norm and Gamma_a,R<=P_R Gamma_a P_R.
Electric terms remain commuting diagonal local operators and the halo is
unchanged. Thus section 2, including monitored instruments, applies with the
same constants for every R.

For a fixed local tolerance first choose a common finite canonical patch
using section 2 for BOTH rotor and boxed processes. On that fixed patch
Omega has zero fields. A complete magnetic or loss word changes the total
absolute field by at most four on each density leg, and each original gain
word by at most two per leg. All intermediate elementary steps have the
same finite bound with a fixed additional allowance. Consequently every
interaction-picture Dyson coefficient of order <=j agrees with the unboxed
one on Omega once R>=4j+8. Electric conjugation only supplies phases and
does not change field support. On the fixed patch the bounded perturbation
has finite trace-class norm C_patch, independently of R. Its tails are
bounded by sum_(j>r)(C_patch T)^j/j!, and weighted tails acquire only a
polynomial in 4j+8. This proves prepared trace-norm and weighted convergence
on that patch for every finite T. The same proof applies to a capped marked
instrument and passive field-independent copies; remove the cap using (2.3).
Localize back to both full graphs. This order proves the local rotor-to-box
limit uniformly in L; a volume-dependent global cutoff estimate has not been
declared uniform by exchanging limits.

Here is the separate uniform-integrability estimate needed for energy. For
a fixed finite edge set S put Q_S=1+sum_(e in S)|E_e|. A bounded finite-shift
operator W with bandwidth s relative to Q_S decomposes as
W=sum_(d=-s)^s W_d, where W_d=sum_n Pi_(n+d) W Pi_n and ||W_d||<=||W||.
The orthogonality of input and output bands gives this norm inequality.
For u>=0,

    ||Q_S^u W Q_S^(-u)|| <= b_u(s)||W||,
    b_u(s)=(2s+1)(1+s)^u.                              (3.2)

Magnetic terms meeting S have s<=4; jumps have s<=2; their exact loss
products have s<=4. Terms disjoint from S cancel in the adjoint generator,
and the electric term commutes with Q_S. For p>=0, Cauchy-Schwarz applied
to the two Hamiltonian forms and the gain/loss forms yields

    L* Q_S^p <= C_p(S) Q_S^p,
    C_p(S)=2b_(p/2)(4)V_S
             +[b_(p/2)(2)^2+b_(p/2)(4)]G_S,             (3.3)

where V_S=sum_(magnetic terms meeting S)||A_ac|| and
G_S=sum_(jumps meeting S)||L_m||^2. These constants depend only on the
finite set S, not L or R. Finite spectral truncations justify differentiating;
the fixed-patch weighted Dyson argument gives the domain limit. Localize the
bounded spectral cuts by section 2 and use monotone convergence, or apply
the same positive form inequality first to each finite torus. Gronwall gives

    Tr(Q_S^p rho_L(t)), Tr(Q_S^p rho_L,R(t))
      <= exp(C_p(S)t),       0<=t<=T,                   (3.4)

since the initial moment equals one. Only canonical source restrictions are
used for patch energy. No arbitrary bounded boundary operator is assigned
this weighted estimate without its own bandwidth control.

If a self-adjoint local O has ||O psi||<=C||Q_S^2 psi|| on finite-field
vectors, its cut O_r=1_(Q_S<=r)O1_(Q_S<=r) has

    |Tr rho(O-O_r)| <= 2 C Tr(rho Q_S^4)/r^2.           (3.5)

Indeed insert the spectral complement on either side, use Cauchy-Schwarz
with Q_S^2 on both factors and bound its tail probability by r^-4 times
the fourth moment. The same estimate holds after purification for mixed
rho. This proof does not commute O with Q_S. Each h_a obeys the required
relative quadratic bound. Choose r from (3.4)-(3.5), then the bounded local
trace tolerance for O_r, then R. This gives uniform per-center convergence
of original source-energy means, at every specified observation time.
Compression gives its actual h_a,R expectation on a boxed state. A safe
local norm bound is

    ||h_a,R|| <= e_R:=12K(1+R)^2+v0.                  (3.6)

The same moment proof with a sufficiently large finite set and p controls
the local form L* h_a. Finite-field differentiation followed by these
weighted limits gives Delta<E h_a>=integral_0^t <L*h_a> ds. Thus the energy
increment used below is the integrated ORIGINAL source current. It does
not identify an instantaneous clock current or a work distribution.

## 4. Finite-cell influence without a dimension factor

We next work on finite-dimensional ambient tensor cells, including any
finite flag or proof word-register factors. For a bounded observable define

    c_x(O)=sup_(unitary U_x)||[O,U_x]||.

Haar-twirl one cell at a time. The conditional expectation E_Z onto the
exterior algebra obeys ||O-E_Z O||<=sum_(z in Z)c_z(O), by telescoping the
twirls and contractivity. This is an ambient tensor calculation; the
Gauss-constrained subspace need not factor. We do not twirl that subspace.

Let C_Z be a local unital CP map and d_Z=||C_Z-I||_cb. It fixes the exterior
algebra, so (C_Z-I)E_Z=0. For x outside Z contraction and locality give
c_x(C_Z O)<=c_x(O). For x in Z,

    c_x(C_Z O)<=c_x(O)+2d_Z sum_(z in Z)c_z(O).          (4.1)

Thus its influence vector is bounded by the nonnegative matrix
I+2d_Z 1_Z1_Z^t. A disjoint color layer whose supports have size <=v and
diameter <=d has row and column sums bounded by 1+2v max d_Z; with weight
exp(mu distance), replace the increment by 2v exp(mu d) max d_Z.
Products are bounded by the exponential of the sums of these increments.
All are independent of cell dimension, total volume, and ancillary matrix
amplification. Initially c_x(O_X)<=2||O||1_X(x).

If a local difference map E fixes the exterior to zero, then

    ||E(O)||<=||E||_cb sum_(z in Z)c_z(O).              (4.2)

Telescope two circuits and use (4.2) against the propagated influence
matrix, retaining contraction on the other side. Local defects are summed
against a spatially summable kernel, not a total-volume norm. Omitting
terms outside a buffer costs an exponentially decreasing factor in its
radius, with a finite prefactor depending on the observed anchor and the
integrated local strengths. This follows directly by inserting
exp(mu distance) in the path matrix and bounding the omitted sites by
exp(-mu buffer radius). For interactions with several finite support types,
use a finite coloring of their bounded-degree overlap graph.

A local Hamiltonian step has cb deviation <=2dt||H_Z||. Finite-volume
Lie splitting and the integral equation therefore give the corresponding
continuous bound with exponent at most

    4v exp(mu d) sum_colors integral_0^T max_Z ||H_Z(t)||dt.  (4.3)

The precise coloring only changes this finite overcount. In Duhamel for two
Hamiltonian programs, the reference-evolved observable is inside the local
commutator; the perturbed propagator is outside and preserves norm. Therefore
only the reference's influence kernel is needed to sum arbitrary local
Hamiltonian differences. A perturbed program need not obey that kernel.

Unbounded onsite clock momentum will be removed exactly by a product
interaction picture. We first apply this proof at arbitrary finite clock
cutoff, where Haar twirling is legitimate. At fixed finite spatial volume,
section 9 proves prepared vector convergence to the ideal clock. Passing the
uniform spatial comparison through that limit proves only the prepared-state
ideal-clock locality required here. There is no infinite-dimensional normal
Haar average or whole-space norm convergence of clock propagators.

## 5. Colored original collisions and per-center word records

Fix R. For a time step tau with tau g0<=1/2 define at each A center

    K_a0=sqrt(I-tau Gamma_a,R),
    K_am=sqrt(tau)L_m,R.                               (5.1)

Their adjoint products sum to I. At a monitored center use its OWN classical
word space, with a chosen finite length cap and one overflow value. For each
word w and each original m, the gain Kraus is

    L_m,R tensor |append_m(w)><w|.                     (5.2)

Overflow appends to overflow, but never stops a physical source jump. The
sum of adjoint products of (5.2) is Gamma_a,R tensor I; the no-event factor
keeps w untouched. This local extension realizes the full original history
on classical words. It may dephase coherent word inputs on gains, which
does not change the classical target. Different centers have distinct local
word registers. A single nonlocal shared append factor is not used.

In the adjoint cb norm the collision C_a satisfies

    ||C_a-I||_cb<=3g0 tau,
    ||C_a-exp(tau D_a)||_cb<=7g0^2 tau^2.               (5.3)

For the first inequality write the gain norm as tau||Gamma_a,R|| and use
||sqrt(I-tau Gamma)-I||<=tau g0. For the second, expand the square root
with its scalar second-order remainder on [0,1/2], compare the gain plus
loss with tau D_a, and bound the exponential remainder using ||D_a||<=2g0.
The generous constant seven covers both remainders. The same proof applies
to (5.2), including overflow, because its rate effect is unchanged. The
continuous D_a semigroup contains every repeated original gain; no-event
and multiple-event terms are compared jointly.

Stars overlap exactly when their A centers have distance two; there are
18 such neighbors. Hence a greedy coloring uses chi=19 colors uniformly in
L. Stars of a color are disjoint. On each fine interval apply all center
collisions in color order and the free source evolution for that interval.
Refine each prescribed observation interval separately; its endpoints remain
exact. Choose refinements so min tau_k>=max tau_k/2. Let n be their total
number. Section 4 bounds the discrete influence by a constant depending on
T,g0,geometry but not the mesh, since d_Z=O(tau_k). The bounded boxed source
evolution has the analogous influence bound with strength determined by e_R.

Choose one finite spatial patch using these uniform bounds BEFORE taking
the mesh to zero. On that fixed patch all generators are bounded. The usual
telescoped product estimate follows directly by integrating commutators in
the two-factor Duhamel identity: its error is a fixed patch constant times
T max tau_k. Adding (5.3) has the same order. Return to the large graph by
the two patch comparisons. This proves volume-uniform local convergence of
the original marked collision process, including passive tests. Word caps
are chosen from (2.3); the physical apparatus only needs one finite flag
per fine interval. An overflow discrepancy is bounded by the same local
instrument comparison and the target tail.

When the requested binned history keeps relative order between different
observed centers within a fine bin, color order can differ from time order
only on bins with two or more monitored events. The factorial bound gives
total probability <=(g0|F|)^2 T max tau_k/2. This is added to the error
before coarsening to the prescribed bins. Unobserved multiple births
continue in the source evolution; no global one-event approximation is made.

## 6. Local Julia completion and the exact copied labels

For each a,k introduce a fresh physical flag F_ak and a copy E_ak, both
blank initially, with dimensions 13 for resolved marks or 7 for coherent
marks (including the blank). They have zero assigned free Hamiltonian.
Let R_a psi=sqrt(tau_k)(L_m,R psi)_m and put

    U_flag = [[sqrt(I-R_a*R_a), -R_a*],
              [R_a, sqrt(I-R_a R_a*)]].                (6.1)

Functional calculus gives sqrt(I-R*R)R*=R*sqrt(I-RR*), so block
multiplication proves unitarity. Its blank column is exactly (5.1).
On flag and copy use the modular copy C|m,e>=|m,e+m mod d_F>, and set

    U_ak=C(U_flag tensor I_E)C* = exp(-i G_ak),
    0<=G_ak<=2pi I.                                   (6.2)

Choose the spectral argument of U in [0,2pi), separately on its invariant
Gauss blocks and on the matched subspace span{|m,m>}; choose argument zero
on any unused identity subspace. The matched subspace is invariant because
C* takes it to span{|m,0>} before U_flag. This proves that every fractional
pulse exp(-iuG_ak), not just its final value, keeps flag and copy matched.
After tracing E the flag is exactly classical, including while entangled
with clocks and source. For coherent marks the two sigma contributions
remain in the same edge-labeled block. No sigma copy has been introduced.

Each G_ak is supported on the source star of a and this flag/copy pair,
commutes with Gauss and has norm <=2pi. Existing flags stay present. Physical
free evolution and other centers' gates do not touch a given completed pair.
Later tails of its own smooth pulse can touch it; their effect is included
in the process comparison, rather than assuming irreversible storage.

## 7. A finite local pulse program

Within each fine interval choose chi ordered color slots and triangular
pulses p_ak(t) of area one, half-width s, height 1/s. Choose
s<=min tau_k/(8chi+4), with guards around every observation boundary.
All centers of a color use the same pulse location. At a fixed center its
n triangles are disjoint, so sum_k p_ak<=1/s. The deterministic Hamiltonian
program is

    h_+ + sum_(a,k) p_ak(t)G_ak.                       (7.1)

For comparison only, turn off h_R during the pulse/guard windows and
increase its speed on the remainder of each interval to retain total free
time tau_k. A factor at most two suffices by the width choice. This realizes
the color collisions and free source evolution exactly at fine endpoints.
The difference between it and (7.1) has integrated local source strength
O(n chi s e_R). Use (4.3) for the reference program. For each color its
pulse strength integral is <=2pi n, independent of s; free source contributes
a finite multiple of e_R T. Thus the reference influence constant C_prog
is chosen before s. Duhamel and (4.2) make the local pulse/free error tend to
zero with s. Globally serializing all N centers is unnecessary.

Let L_c=4T, omega=2pi/L_c. Regard the pulses as functions on this circle,
with no wrap through the observation windows. Convolve p_ak with the
positive normalized Fejer kernel of degree M to obtain f_ak. Its coefficients
are explicitly

    fhat_ak(j)=(1-|j|/(M+1)) exp(-ij omega t_ak)
                 sinc^2(j omega s/2)/L_c, |j|<=M.      (7.2)

Here sinc(0)=1. Positivity, area one and the pointwise sum bound are
preserved by convolution. The triangle's variation is 2/s and Lipschitz
constant 1/s^2. Integrating the elementary Fejer first circular-distance
moment bound gives the conservative errors

    ||f_ak-p_ak||_1 <= rho1
       =L_c[1+log(M+1)]/[(M+1)s],
    ||f_ak-p_ak||_infty <= rhoinf
       =L_c[1+log(M+1)]/[2(M+1)s^2].                  (7.3)

For example, bound its density by the minimum of (M+1)/L_c and
L_c/[4(M+1)y^2], using |sin(pi y/L_c)|>=2|y|/L_c for
|y|<=L_c/2, and integrate |y|. A larger right side remains valid for small
M. Duhamel against the deterministic reference bounds smoothing by a fixed
local influence factor times 2pi n rho1 per center.

## 8. Ideal translating clocks, averaged locally

For analysis put one circle clock at every A center, momentum P_a=-i d/dx_a,
and initial normalized packet

    beta(x)=[L_c(2k0+1)]^(-1/2) sum_(m=-k0)^k0 exp(im omega x).

The product packet is independent of the source and flags. On the circle
the probability theta of |x|>sigma, 0<sigma<L_c/2, obeys

    theta <= L_c^2/[4(2k0+1)sigma^2].                 (8.1)

Indeed the Dirichlet numerator is bounded by one and the denominator by
|sin(pi x/L_c)|>=2sigma/L_c on that complement, then integrate over its
length. This deliberately loose tail bound suffices.

At fixed finite volume the analysis Hamiltonian

    H_infty=h_+ + sum_a P_a + sum_(a,k) f_ak(X_a)G_ak  (8.2)

is self-adjoint on the sum-momentum domain by bounded perturbation. The
characteristic solution is

    Psi_t(y+t1)=beta_product(y) U_y(t)psi,             (8.3)

where U_y is the source/flag propagator with scalar coefficients f_ak(t+y_a).
Different coordinates translate with the same velocity one. Equation (8.3)
follows by differentiating finite Fourier vectors and extends by unitary
continuity. After tracing clocks the complete source/flag process is the
mixture over initial offsets y. Passive clock-independent copies at finitely
many grid times preserve this representation with the same y throughout;
they do not reprepare clocks. The clock-coordinate marginal remains the
translated product distribution for the unconditioned process, despite
source/clock entanglement.

There is no global good-clock event with a probability loss N theta. For
one center, good offsets |y_a|<=sigma have integrated triangle-train mismatch
<=2n sigma/s by variation. For bad offsets the mismatch is <=2n by positivity
and full-circle area. Multiplication by ||G||<=2pi gives expected mismatch

    <=4pi n(sigma/s+theta).                            (8.4)

The smoothing term (7.3) adds 2pi n rho1. In Duhamel place the deterministic
reference-evolved observable inside each commutator. Its summable spatial
influence kernel is independent of y and was fixed before s. Average each
local mismatch against this kernel and use (8.4). Linearity of the sum and
expectation suffices; no independence between a bad clock and a propagated
state is assumed. The outer perturbed unitary is contractive, so no uniform
propagation estimate for arbitrary bad-offset programs is invoked. For a
finite passive test sequence telescope the same inequalities with its fixed
enlarged anchor. After s is fixed choose sigma/s small, then k0 large and
M large. The local averaged-clock process error tends to zero uniformly in L.

## 9. Positive finite clocks and the order of resources

Implement |m|<=K_c with ordinary projection Pi_Kc. Set

    H_Ca=omega sum_(m=-K_c)^K_c (m+K_c)|m><m| >=0,
    F_ak=Pi_Kc f_ak(X_a)Pi_Kc >=0,
    V_K=sum_(a,k) F_ak G_ak,
    H_AUT=h_+ + H_C + V_K >=0,  H_C=sum_a H_Ca.        (9.1)

These are finite matrices and H_AUT is time independent. F_ak is Toeplitz
compression, not a cyclic shift. Clock and payload factors commute, giving
positivity of each product. With V_a=sum_k F_ak G_ak,

    0<=V_a<=2pi sum_k F_ak tensor I<=2pi/s.             (9.2)

Once R,n,s,M,k0 are fixed, choose a spatial buffer using section 4 for this
static apparatus. Its interaction strengths are bounded by the fixed source
local norms and 2pi/s per A center. Remove H_C in a product interaction
picture; its large onsite norm never appears in propagation. The spatial
buffer is therefore independent of K_c. Use the same buffer for source and
record outputs and for local clock-only tests needed below. Section 4's
ideal-clock extension is justified by the following fixed-volume limit.

In a fixed patch containing N_patch A centers, let
v_patch=2pi N_patch/s. Treat h_++sum P_a as free. Each bounded interaction
insertion changes one clock momentum by at most M. Starting in |m|<=k0,
every vector coefficient and every internal prefix of order <=r is identical
in the ideal and compressed clocks if K_c>=k0+Mr; the scalar clock shifts
give only a common phase. All interactions have norm <=v_patch. The two
Dyson tails give vector difference <=2sum_(j>r)(v_patch T)^j/j!, hence trace
or instrument error

    eta_band <=4sum_(j>r)(v_patch T)^j/j!.              (9.3)

Passive clock-independent copies leave this prefix condition unchanged;
the total integration simplex still has volume T^j/j!. This proves the
fixed-volume prepared limit used in section 4, with all local dimensions
other than the clock fixed. Pass its uniform boundary bound to the ideal
process, then choose r for the fixed buffer and finally K_c. No later choice
changes the local interaction bound that selected the buffer.

For clarity a permissible nested choice is:

1. Choose local energy spectral cuts and a common spatial rotor patch, then
   R by section 3 for the desired local source/process error.
2. Choose count caps, a common collision patch and a sufficiently fine mesh n
   by section 5, preserving prescribed grid endpoints.
3. Choose s by section 7 using the already fixed program influence bound.
4. Choose sigma, M and k0 for (7.3), (8.1), (8.4) and endpoint bounds below.
5. Choose the static apparatus buffer independently of K_c; choose r for
   (9.3), then K_c>=k0+Mr.

All choices are finite and independent of L. Finite contraction telescoping
sums the errors. Boxed source mean energies are bounded local observables,
so their last-stage errors are <=e_R times the local trace error. The earlier
rotor energy truncation was separately priced in (3.5); trace norm alone
does not control the unbounded target energy. The clock-energy ledger below
does not multiply this trace error by a growing clock-energy norm.

## 10. Endpoint interaction envelope and the complete mean ledger

At a prescribed observation boundary every triangle is zero for all offsets
|y_a|<=sigma, with sigma<s chosen inside its guard. In the ideal process
the clock marginal is known exactly from (8.3). Therefore the positive
clock-only envelope, not merely the interaction's pre-read expectation,
satisfies

    <2pi sum_k f_ak(X_a)> <=2pi[n rhoinf+theta/s].       (10.1)

The bad-offset bound uses sum_k f_ak<=1/s. In the local finite-clock
comparison of section 9 include the bounded clock-only observable
2pi sum_k f_ak; its norm is <=2pi/s, independently of K_c. Its compressed
expectation differs by at most (2pi/s)eta_clock for a chosen local trace
tolerance eta_clock. Thus at every observed boundary,

    0<=<V_a><=nu,
    nu=2pi[n rhoinf+theta/s]+(2pi/s)eta_clock.           (10.2)

After s is fixed, later parameters make nu arbitrarily small uniformly in L.
The same clock-only envelope bounds the state immediately after any
unconditioned flag read, because that read leaves the clock marginal
unchanged. Source and H_C commute with the read. Only the V_a at touched
centers can change, and each pre- and post-read mean is bounded by nu.
Thus the absolute supplied reader energy exchange is at most 2nu|F_read|
for that read. This is an unconditional allowance, also when the source and
apparatus are correlated. It is not asserted for postselected histories.

The time-independent positive finite Hamiltonian conserves its total energy
exactly. On the closed run,

    -Delta<H_C>/N = Delta<h_R>/N+Delta<V_K>/N.          (10.3)

The scalar v0 N shift cancels. Uniform per-center source-energy transfer
and (10.2) give

    | -Delta<H_C>/N - Delta<h>_original/N |
       <= epsilon_source_mean + 2nu.                  (10.4)

Here epsilon_source_mean prices both source endpoints. If passive reads
inject a total mean energy W_read, then total conservation between reads
gives the exact same identity with W_read/N added to the clock debit on the
left. Its absolute allowance is the sum of the estimates just stated.
Equation (3.4) justifies the original source current integrated in time;
(10.4) is a density balance for that actual original energy, not a shifted
surrogate energy. Positive H_AUT by itself would not prove (10.4); the
endpoint interaction envelope and the source-energy transfer are essential.

## 11. Resources, qubit encoding and limits

The initial clock mean per A center is omega K_c, its maximum 2omega K_c,
and its variance omega^2 k0(k0+1)/3. These follow from the uniform
coefficients on -k0,...,k0. Every flag and copy begins in a supplied pure
blank state. Their assigned free spectra are zero, but their finite memory
capacity and pure preparation are explicit resources. Every coupling is
included in V_K. A safe initial positive total mean-energy density per A
center is

    e_R+omega K_c+2pi/s.                               (11.1)

At Omega the electric term is zero; the source positivity shift is included
in this bound. Local source couplings are bounded using (3.6), clock free
norm by 2omega K_c and total pulse coupling at one center by 2pi/s. These
finite quantities, dimensions and interaction supports are independent of L.
They may be very large as tolerance decreases or T increases. The theorem
does not give an efficiency or optimal-resource statement.

Let q_E=ceil(log2(2R+1)), q_C=ceil(log2(2K_c+1)), and q_F=4 for resolved
or 3 for coherent marks. Factorwise isometries give sufficient qubit counts

    b_A=1+q_C+2n q_F,       b_B=2+6q_E.                (11.2)

Put these qubits in disjoint cubic blocks of side
l=ceil(cuberoot(max(b_A,b_B))) assigned to original cells. Preserve each
original source factor and flag readout by its fixed code isometry. Compress
operators to this legal code and extend positive total terms by zero on
unused code states; the prepared code is invariant. This is an explicit
finite M2 encoding with enlarged cells, not identification of a whole source
cell with a single physical M2 factor.

A star has one A and six B cells, so a pulse acts on at most
13+36q_E+q_C+2q_F qubits. A magnetic pair of axial centers a,a+2e_i has
two A and eleven distinct B cells; the safe whole-pair bound is 24+66q_E.
Diagonal distance-two pairs share two B cells and use fewer. The support's
cell l1-diameter is at most four; allowing within-block offsets gives range
at most seven block widths and finite interaction arity. No nearest-neighbor
two-qubit decomposition with the same autonomous ledger is silently added.

The prescribed clock phase, positive Fourier functions, logarithms, spatial
coloring, memory bank, enlarged-cell map and exact coefficients are supplied
implementation choices. The target is finite-horizon, finite-tolerance,
regional binned histories with mean source/controller balance. Exact
unbinned timestamps, stationary or catalytic supply, infinite-time storage,
permanent apparatus flags, microscopic law convergence and physical
selection are not conclusions of this theorem. These scope exclusions
are not impossibility claims about other constructions.

## 12. Prior scope, verification and review record

The main note `FINITE_AUTONOMOUS_MARKED_DYNAMICS_UNDER_GRID_OBSERVATIONS_BOUNDED_THEOREM_NOTE_2026-09-24.md`
constructs a finite positive history clock for a global finite-dimensional
payload and explicitly leaves spatial locality and finite resource density
outside its result. Its one-time predecessor
`AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`
has the same global-payload limitation. They are prior scope comparisons,
not proof premises here. The provisional fixed-volume local supplier in
PR9397 (head 72e8656de1a34d236db62f2443b23cd15c2d5f25) and thermodynamic
source proposal PR9399 (head 5bec44a4a08d7e7727e8d23d94c884fc32332b05)
motivated this composition. Every load-bearing argument needed from them is
re-established above; neither absent source is in the declared input closure.

The new contribution is the regional process topology and noncircular
volume-uniform resource construction: uniform prepared rotor cutoffs,
near-identity local marked collisions, deterministic-reference influence
for averaged clock offsets, and static-buffer selection before clock-band
compression. The clock-only endpoint envelope also prices passive reads.
Prior focused analytic checks of the discovery proof are authoring context,
not a formal review or a theorem premise. This composed source needs its
own complete source review.

The primary runner uses finite exact word/geometry controls and small
floating matrix controls of the composition. It checks actual original
word signs, gain/loss and coherent-copy conventions, local overlap counts,
word-register behavior, finite clock prefixes, positive compression and the
controller/interaction ledger. These controls corroborate the displayed
analytic proof at their declared sizes. They do not numerically establish
the uniform quantifiers or calibrate a physical source. Its output and
source/input-bound cache are generated through `scripts/runner_cache.py`.
Scratch mutations and every execution failure are recorded in the owned
loop pack. No extra scientific helper or hidden runtime input is required.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  python3 scripts/uniform_autonomous_original_record_resource_density_2026_09_30.py
```

This is an author proposal of conditional mathematical support. The
framework's four axioms and approved primitives are unchanged. Source review,
graph acknowledgment, combined integration validation and any subsequent
independent audit are distinct requirements; no formal disposition is
pre-stated here.
