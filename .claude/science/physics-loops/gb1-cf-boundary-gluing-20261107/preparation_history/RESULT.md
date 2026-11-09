# Preparation and ordered records determine a finite gauge history

**Claim type:** bounded_theorem. **Actual status:** conditional-support.
Research continuation of GB1-CF; no formal landing review or independent audit.

The finite state-sufficiency question has a positive construction. A prepared
header and an intrinsically ordered permanent log determine every future
probability in the supplied finite experiment, including magnetic updates.
The density matrix can be reconstructed from those records. The theorem does
not select the physical probability law or manufacture its preparation.

## 1. Inputs and exact domain

Use the enlarged code E_p, Gauss actions, electric sector projectors P_(e,b),
and supplied H_native of [the vertex-output result](../native_records/RESULT.md).
That result has a separate research check but no audit. Its declared finite
regulator is Lambda=(Z/(5n)Z)^3; it is not a completed infinite-lattice limit.
The free coarse vertices V_p, active link interiors A_p and frozen F_p remain
unchanged. On E_p, H_native intertwines H tensor I_outputs.

Fix d>=1, N>=1, M=d+N and n>=2M+8. Supply a finite dictionary mapping each
d-bit preparation label alpha to a normalized positive Gauss density rho_alpha.
Supply a finite control alphabet of exact magnetic/electric evolution maps,
such as U=exp(-i tau H), and a fixed controller that selects the next recipe
from alpha and the previously recorded bits. The dictionary is fixed across
the entire domain, and its geometry is interpreted in the recovered frame.
Neither a label-to-state calibration nor these law choices follows from the
four axioms. A passive external system is allowed when its reduced gauge
state is rho_alpha and it does not interact later.

All conditioning prefixes have positive probability. Apparatus markers,
header contents, blank pointers and their initial admissibility are supplied
boundary preparation. The finite model supplies next-site scheduling; the
Admissibility clause alone does not. There is no independent external step
counter or freely variable elapsed-time argument in its state.

## 2. Reconstruction theorem for completely positive histories

Let Phi_(h,b) be the known completely positive branch map for outcome b of the
next recipe. Require sum_b Phi_(h,b) to preserve trace. Define

    sigma_empty = rho_alpha,
    sigma_(h b) = Phi_(h,b)(sigma_h),
    p(b|alpha,h) = Tr sigma_(h b) / Tr sigma_h,
    rho_(alpha,h) = sigma_h / Tr sigma_h.                 (1)

Each sigma is positive. The child traces sum to the parent trace, so p is a
probability distribution at every supported prefix. A zero-trace positive
child is the zero operator and is not a subsequent conditioning domain.
Multiplying the conditional probabilities telescopes to Tr sigma_h, proving
normalized, prefix-consistent cylinders through all N stages. The normalized
branch update in (1) is exactly rho_(alpha,hb), so the reconstructed family is
closed under every allowed update. This is an induction, not a finite-check
extrapolation. Adaptive recipes are permitted because h determines the map.

For a magnetic interval followed by the native reader at fresh true-phase x,

    Phi_(h,b)(X) = (1/6) sum_(e incident to x)
                    P_(e,b) U_h X U_h^dagger P_(e,b).     (2)

The six unobserved edge choices are added as CP maps. No separate edge record
is needed for this specified mixture. An unknown or freely varying edge-choice
law would be a different input. Gauge invariance and trace preservation follow
from P_(e,0)+P_(e,1)=I, P_(e,b)^2=P_(e,b), and gauge-invariant U_h.

A separate recorded magnetic tick is also possible:

    Phi_(h,1)(X)=U_h X U_h^dagger,   Phi_(h,0)(X)=0.       (3)

Its next fresh pointer records 1; the known recipe identifies the slot's role.
On the compatible code, apply U_h and flip that blank pointer. Neither action
changes an older pointer. The calibrated permanent Record append, including
its outcome-1 support and registration, is supplied as part of this tick recipe;
a unitary pointer flip alone is not a Record-formation derivation. Equation (3)
consumes a record, so a later query can
recover which ticks occurred. A fixed U_h can instead be part of (2)'s single
composite event. Neither convention derives a physical time unit or describes
arbitrary continuous evolution between record events.

## 3. A carrier on the existing native output qubits

At coarse vertex a prepare seven bit-1 marker records at

    a, a+5e1, a+5e2, a+10e2, a+5e3, a+10e3, a+15e3.    (4)

Prepare the d header bits and reserve the N successive output slots at

    v_j=a+10j e1+20e2,   j=1,...,M.                     (5)

At stage k, precisely v_1,...,v_(d+k) carry word records. The first d contents
are alpha; the remainder are the ordered h. A recorded zero is present and
distinct from an absent site. Presence is part of the record configuration;
no readable value is assigned to an absent qubit.

To decode without a host frame, connect present records separated by five
native units in a coordinate direction. The marker is the sole nontrivial
component. Its unique degree-three center is a; its three arms have lengths
1,2,3, identifying the ordered positive axes. Every word site is isolated:
successive word sites differ by ten, and all are separated from the marker.
The bound n>=2M+8 prevents extra connections across the periodic boundary.
The identified frame is right-handed. Thus both a and its proper frame are
unique, independent of site-map insertion order. The record positions give
p=a mod 5, and (5) gives alpha, k, h and the next target v_(d+k+1).

There are exactly 7+d+k records. All are in V_p. No active link interior or
frozen F_p site is written or released. At most 7+M output qubits are used,
within n^3 available vertices. The remaining pointers retain their prepared
blank state. A prepared apparatus chooses an origin/frame; the law does not
choose a preferred one. The coherent superposition of origins allowed by the
earlier empty-record model is not this prepared domain.

Take the union of all translated and properly rotated prepared domains, and
transport the preparation dictionary, recipes and H with the recovered frame.
The unique decoder prevents two transported descriptions of the same records
from assigning different answers. Under the native unitary W_g representing
such a spatial symmetry, the decoded conditional state transforms as
rho_(gR)=W_g rho_R W_g^dagger. Covariance of (2)--(3) and trace invariance give

    p_(gx)(b|gR)=p_x(b|R).                              (6)

This is one fixed law on the whole declared orbit, including all 125 origin
residues. It is not a claim that an apparatus has no oriented preparation.

## 4. Record-only finite-neighborhood kernel and preservation

For k<N select the unique next site x=v_(d+k+1), and set

    K(R, R union {x:b}) = p(b|alpha(R),h(R)).             (7)

At k=N use absorbing continuation. Equation (1) proves that (7) is a normalized
Markov kernel whose complete variable is the record configuration R. It assigns
content probabilities at one common site fixed before the outcome. Unlike the
older outcome-dependent first-relay construction, the probability is not moved
into the choice of two different outcome sites.

Every record needed for decoding lies within native graph radius

    r_M = 10M+35                                        (8)

of the next site. Indeed word-to-word distance is at most 10(M-1), and the
farthest marker distance is bounded by 10M+20+15. Periodic distance can only
decrease these upper bounds. Thus (7)'s next-content distribution factors
through the finite ball's record condition. Equal such conditions at eligible
targets give equal probabilities. This is an exact finite-neighborhood
functional on the prepared domain, not a propagation-speed or gate-runtime
theorem. Its radius grows with the chosen history budget; a uniform bounded
range construction for arbitrarily long histories has not been supplied.

The kernel is genuinely capable of varying with its conditions. Choose the
first recipe to have U=I and let two header labels specify empty flux and a
singlet loop through the first target's adjacent plaquette. For the same target,
(2) gives b=1 weights 0 and 1/3. The distinguishing preparation label now occurs
inside the neighborhood (8), so these are different complete conditions.

For every selected target the original D_x detector is identity on E_p and
the pointer is fresh. All prior records are at vertices, disjoint from active
detector supports, so the record guard permits the readout. The prior
H_native intertwiner and (2)--(3) preserve every stored marker, header and
outcome. Induction shows the compatible joint quantum experiment has exactly
the kernel (7) when its preparation matches the decoded dictionary. No
off-code Hamiltonian record-protection claim is added.

This gives a finite prepared record-only kernel. It does not define a universal
admissibility completion for every possible matrix-content configuration or
derive the genesis/support of the initial apparatus records. The finite torus,
supplied control and calibration conditions remain visible.

## 5. A preparation certificate stronger than a label

There is a direct algebraic way to make one preparation record certify its
postcondition. Let psi be a normalized gauge singlet and P=|psi><psi|. Supply
the calibrated binary verification instrument {P,I-P}, with success written
at a fresh output. For every positive X,

    P X P = Tr(PX) P.                                  (9)

On any nonzero-probability success the normalized gauge state is exactly P,
independent of the earlier X. With a passive reference,

    (P tensor I) X (P tensor I) = P tensor <psi|X|psi>,   (10)

so the system also decouples from that reference on success. These equations
follow by inserting P=|psi><psi| on both sides. The complete empty-flux state
on the finite gauge graph is an example; it is not asserted to be the physical
vacuum. A prescribed closed singlet loop gives another covariantly transported
example. Their projectors commute with all Gauss actions.

Reserve the first output slot for this herald; condition on its recorded
success and initialize the recursion there at sigma_start=P_alpha, the pure
state certified by the decoded preparation program. This variant's initial
domain begins after that logged success: one slot is already used, and only
the remaining N-1 recipes are replayed. At N=1 it is already absorbing.
No unrelated mixed dictionary entry is used as the post-herald state, and no
pre-herald probability is assigned by choosing an arbitrary reference seed.
This removes an independent unknown initial density from post-preparation
predictions. It does not
determine success odds for arbitrary unrecorded pre-inputs, guarantee success,
construct the verifier's adjacent-gate circuit, or derive its calibration.
The full-graph rank-one verifier can have large finite support. A degenerate
electric-sector outcome alone does not certify the same postcondition.

## 6. Exact meaning of sufficient records

A unique rho_R is sufficient, but stronger than necessary. For any allowed
future instrument word w let E_w=Phi_w^*(I). Its cylinder probability at rho
is Tr(rho E_w). Two candidate states with the same records give every allowed
future probability identically if and only if

    Tr((rho-rho') E_w)=0 for every allowed word w.        (11)

Equivalently their difference annihilates the linear span of these effects.
This proves the criterion directly from CP duality. For closed-loop use, the
available recipes and successor-record updates must also be the same functions
of the records. Equal probabilities for all continuation words then imply
equal conditional continuation probabilities after any positive-probability
child, by dividing the joint probability by its first-event probability.
Equal one-step odds alone do not establish (11).

The fine Kraus path is not automatically an extra physical record. Known
unobserved branches are already marginalized in (2). Known null loops may also
be marginalized into a next-success instrument when that instrument is
well-defined and eventual success is certain. No claim that every null must
be logged is needed. A physically uncertain intervention or elapsed-time
law must be specified or reconstructed before applying this argument.

Two finite controls show what information must be handled. On the pair
sector span(empty,L), B_L=2X. At cos(tau)=3/5, the magnetic pulse changes the
next corner b=1 probability from 0 to 192/625 if that pulse is omitted from
the record/program description. This is a declared local pair control, not
the uniform full cubic Hamiltonian. Also, from |0>, the positive histories Z0,Y0
and Y0,Z0 have the same named outcomes but future Z1 probabilities 1/2 and 0;
their history masses are 1/2 and 1/4. Here Y0 projects onto (|0>+i|1>)/sqrt(2).
These are explicit omission controls, not a no-go for alternative encodings.
The projective order example does not construct a native Y0 reader.

## 7. Evidence, relation to prior work and next obligation

The existing August projective-history note supplies a conditional global
finite-history calculator; the September local-copy note reconstructs full
finite histories but assigns first outcomes through a nonlocal occurrence
kernel. Their trace-history machinery is prior art, not a newly discovered
probability principle. This result applies the general CP recursion to the
gauge code, gives the binary marker/log geometry, permits recorded magnetic
ticks, and proves the finite common-target neighborhood bound (8).

PRIMARY.md and PREPARATION_ADDENDUM.md preserve the supervisor's candidates.
Independent proof and exact-check evidence are indexed in HANDOFF.md. Research
checks do not constitute formal landing review or independent audit.

The remaining physical obligation is to realize the calibrated preparation,
controller and neighborhood kernel, with a scalable influence/resource law.
Equation (9) supplies a post-preparation state certificate; it does not derive
the preparation's own occurrence law. This finite positive result provides no
reason by itself to amend the state axiom. An independently variable quantum
state at fixed complete records would instead require either a better record
carrier or an explicitly reconsidered physical state description.
