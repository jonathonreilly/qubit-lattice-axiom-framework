# Native two-cycle histories with a physical nearest-neighbor projector relay

Working conditional derivation, written before its checker, 2026-09-13.
This binds one native two-event family to an actual local Record law.
It does not select the quantum carrier, Born probabilities, prepared state,
Hamiltonian, controls, clock or probability calibration from the axioms.

## 1. One connected native carrier

Coarse vertices are
0=(0,0,0),1=(1,0,0),2=(2,0,0),3=(0,1,0),4=(1,1,0),5=(2,1,0).
Edges are01,12,03,14,25,34,45. Physical vertices lie at twice these
coordinates; edge qubits lie at their physical midpoints. Protect the tree
03,34,14,45,25, and use both remaining edges01,12 as candidate Records.
Their actual sites arex1=(1,0,0),x2=(3,0,0), with free relay site
u=(2,0,0). All protected hopping amplitudes are the same t>0.

Use the main native edge/CAR definitions with increasing neighbor order:
B_i=product incident Z,
A_ij=epsilon_ij X_ij product earlier endpoint-neighbor Z,
T_ij=(i/2)A_ij(B_i-B_j).
The two square cycles areS1=cycle(0,1,4,3),S2=cycle(1,2,5,4), with
the main i^length phase. The initial code sets both cycles to+1.
It has dimension32 and represents global even CAR on6vertices. The input
below has particle number2, an allowed even sector.

Let H=t sum_protected T_ij. The candidates have zero hopping from the outset.
For each candidate use the protected B=B1 parity pulse
U_j=cI+sB Z_ej S_j, c=3/sqrt10,s=1/sqrt10.
Then kappa=2cs=3/5 and eta=c²-s²=4/5.
All protected observables commute with S_j,Z_ej and old Record Zs.
Since(S_j Z_ej)²=-I, the pulse is full-carrier unitary.
For the incoming code P_code and Q_jz=(I+zZ_ej)/2,

    Q_jz U_j P_code = J_jz F_z P_code,
    J_jz=sqrt2 Q_jz P_code,
    F_z=(cI+zsB)/sqrt2,
    F_z²=(I+z kappa B)/2.

The native nonbridge theorem makes J_jz an isometry onto the next code
and an intertwiner of the protected algebra. The unused cycle excludes
the first candidate and survives its event. Thus the second event uses
the same protected B and H after decoding. Both graph deletions leave
the protected tree connected.

The matter current is I14=i t(c1†c4-c4†c1), or
-t A14(I-B1 B4)/2 physically, with norm<=t. All H and F_z commute with
total matter number. This is a conditional finite quantum model, not extra
unrecorded quantum-state ontology supplied by the four framework axioms.

## 2. One preparation and two positive first branches

Prepare the even Slater state with occupied orbitals e0 and(e1+i e4)/sqrt2.
Use covariance C_ij=<c_j†c_i>. Initially m=<B1>=0, C14=-i/2 and<I14>=-t.
The first native outcomes both have probability1/2. The decoded branches
are pure Slater states with occupied orbitals

    e0, (r_z e1+i e4)/sqrt(1+r_z²),
    r_+=1/2, r_-=2.

Consequently m_z=z kappa and<I14>_z=-eta t. No postselection of only one
first branch is allowed. Dwell under the full connected H for duration
tau>=0; write s0=t tau. The second plus probabilities are

    p_z(s0) = [1+kappa m_z(s0)]/2.

Every p_z lies in[1/5,4/5], since B is an involution. All four complete
native histories therefore have positive weight.

These probabilities have explicit real scalar formulas. Let h be the6x6
unit-weight protected adjacency matrix, so the one-particle dwell is
exp(-i s0 h). The orbit of e1 is symmetric under0<->2,3<->5.
On this four-dimensional cyclic subspace h^4-4h²+I=0.
Set omega_±=sqrt(2±sqrt3) and w_±=(sqrt3∓1)/(2sqrt3). Define

    a = sum_± w_± cos(omega_± s0),
    b = sum_± w_± omega_± sin(omega_± s0),
    d = (1/2) sum_± w_± omega_±(omega_±²-3) sin(omega_± s0).

Then U11=a,U14=-i b,U10=-i d. To derive the last identity, note that
h e1=e4 and h³ e1=e0+e2+3e4, while U10=U12 by reflection symmetry.
The spectral weights follow from sum w=1 and<h²>_e1=1. Hence

    nu_z(s0)=d²+(r_z a+b)²/(1+r_z²),
    m_z(s0)=1-2nu_z(s0),
    p_+(s0)-p_-(s0)=(9/25)(a²-b²).

These are supplied prepared-controller values derived from this native
family, not probabilities fitted to a desired empirical answer.

## 3. A short-time separation with surviving branch current

Only T14 among the protected terms is incident to vertex1. Therefore
||[H,B1]||<=2t and

    m_+(tau)-m_-(tau) >= 2kappa-4t tau.

For0<=s0<=1/40 this is at least11/10, and the two second-event plus
probabilities differ by at least33/100. This analytic bound does not
depend on approximating the matrix exponential.

Also||H||<=5t and||I14||<=t, so
|<I14>_z(tau)-<I14>_z(0)|<=10t²tau.
For that same interval both currents remain<=-11t/20.
Because B anticommutes with I14, the second selective update obeys

    <I14>_(z,w)=eta <I14>_z(tau)/(1+w kappa m_z(tau)).

The denominator is positive and at most8/5, so every final branch has
<I14>_(z,w)<=-11t/40. The tree remains connected and no protected hopping
has been turned off. This is a finite-window branch-current result, not
late-time transport or an interacting phase.

There is an additional exact energy property of this chosen state family.
The protected graph is bipartite, with A={1,3,5},Bset={0,2,4}. Let S be
+1 on A and-1 on Bset. Then h is real and S h S=-h. The initial covariance
satisfies S conjugate(C) S=C. This property survives exp(-i s0 h) and
the real diagonal parity filters, including their real Gram normalization.
All opposite-sublattice entries of C are purely imaginary. Thus every
protected hopping has zero mean in every branch at every dwell time:
<H>=0 in one fixed vacuum energy convention. This is mean matter energy
only; it does not price the controls or imply an energy eigenstate.

## 4. The unrelayed physical condition fails on this family

Every native midpoint has exactly one odd coordinate. Its physical nearest
neighbors have zero or two odd coordinates, so native midpoint sites form
an independent set in Z3. A native Record alone cannot change another
native edge site's neighboring Record configuration.

In the preparation below, omit only the relay formation. The second site's
complete auxiliary neighbors stay fixed across the two positive first
histories. The first native event is distance2 away. Thus its local
condition is identical after the two branches although its native second
probabilities differ by at least33/100 for0<=s0<=1/40. Any ONE law on that
condition has worst-case total-variation error at least33/200 on the pair.
The conclusion rejects this unrelayed conditional protocol. It does not
exhaust auxiliary Records, other schedules, joint layers or state families.

## 5. Twelve prepared Records and one fixed local kernel

Let P be a supplied rank-one Hermitian projector for Z-plus data.
Write P_+=P,P_-=I-P. Encode the dimensionless dwell in

    v=s0/(1+s0), D=(20+v)I+P, T=10I.
    Cplus=(100+p_+(s0))I, Cminus=(200+p_-(s0))I.

D has intrinsic decoding lambda=(Tr D-1)/2, P=D-lambda I,
v=lambda-20 and s0=v/(1-v). For the global mathematical kernel permit
any real lambda in[20,21) with trace-one idempotent P; the quantum-data
family uses Hermitian P. Controller recognition uses scalar central
matrices in[100,101]I and[200,201]I, decoded by subtracting the tag.

For each x in{x1,x2}, prepare:
D atx-e3,x-2e3, and T atx+e3,x+2e3.
Prepare Cplus atx2+e2,x2+e2+e3.
Prepare Cminus atx2-e2,x2-e2-e3.
These12 sites are distinct and avoid all7native edge qubits and u.

For ANY complete finite multiset xi of recorded nearest-neighbor M2
contents, define ONE kernel F:
- If xi contains T and exactly one D-type neighbor, decode its P.
  If it also has exactly one Cplus, exactly one Cminus, and exactly one
  data-neighbor occurrence equal to P or I-P, let p be the corresponding
  decoded controller value. Otherwise set p=1/2.
  Emit p delta_P+(1-p)delta_(I-P), dropping zero-mass atoms.
- In every other nonempty condition use the empirical neighbor measure,
  with occurrences counted separately.
- For the empty condition use delta_0.

This is a normalized nonnegative Borel measure on all M2. All recognizers
use scalar center, real intervals, trace and algebraic idempotence/equality.
Translations and proper rotations preserve the multiset. Complex
similarities and conjugation preserve these algebraic recognizers and
transport the atoms, so the kernel has those algebraic covariances too.
The actual quantum realization is restricted to its chosen Hermitian
frame; no Born inner product is derived from this kernel.

## 6. Physical projector relay and complete local laws

The finite event-boundary protocol is:
(1) first native event atx1;
(2) the fixed protected dwell, then one relay Record atu;
(3) second native event atx2; then absorb as a Record process.

Before(1), x1 sees only D and T. Its F distribution is the native fair
P_+/P_- law. After first sign z, u sees only P_z atx1. Thus its F law is
delta_Pz, and it records a COPY of the actual projector outcome.

A supplied physical implementation of this relay uses one ready qubit
atu in P_+. Apply

    Ucopy=Q_e1,+ tensor I_u + Q_e1,- tensor X_u,

then measure its Z basis with Record contents P_+,P_-.
The two factors are physical nearest neighbors. After the first Record,
the copied outcome is deterministic. Ucopy commutes with all protected
observables and H because they commute with the old Z_e1; it preserves
the conditional matter/reference state and old Record. Its ready state,
Pauli flip, timing and energy/control resources remain supplied.

Before(3), x2's complete recorded neighbors are:
D atx2-e3, T atx2+e3, Cplus atx2+e2, Cminus atx2-e2,
and the relay P_z atu=x2-e1. Its sixth neighbor is unrecorded.
The actual F distribution is therefore p_z(s0) on P_+ and1-p_z(s0) on P_-,
exactly the native second-event distribution.

No auxiliary analog output label is identified with a qubit state.
The new relay Record is the actual copied native projector. The12 initial
metadata Records are supplied M2 contents; their physical preparation and
precision are not derived. The active quantum calculation uses7native
edge factors and1ready relay factor. Together with metadata,20 physical
sites are used. After completion15 are recorded and5protected native edge
sites remain unrecorded.

## 7. Permanence, reconstruction and exact cylinders

Each initial D,T,Cplus,Cminus Record has an equal neighboring buddy.
No prepared Record ever sees BOTH a trigger T and a D-type neighbor, so
its local law remains empirical and continues to support its content.
This last geometric assertion must be checked using all six neighbors;
an intended-role diagram alone is insufficient.

The first native Record retains its D,T neighbors and gains only the
relay P_z; it sees neither controller, so its law remains fair.
At u, after the second event the neighbors are P_z and P_w.
The empirical law retains P_z with positive mass even when z differs
from w. At x2 its five neighbors stay fixed and the realized outcome
always has positive mass. No site forms twice. H and later native pulses
commute with the old native/relay Z Records.

The two Cplus sites and two Cminus sites identify x2 and the frame.
Their unique closest unlike-tag pair isx2+e2,x2-e2, at distance2.
The Cplus buddy displacement is e3; then e1=e2 cross e3. This recovers
x1=x2-2e1,u=x2-e1, and the D content recovers P and s0.
The domain consists of these preparations and legal event prefixes,
their translations/proper rotations, and their supplied Hermitian frames.
The current Record configuration recovers the first sign, relay stage and
second sign, so its next event has a unique answer. No sampled current
outcome, quantum posterior or clock is an extra law-state variable.
The use of occupancy in this mathematical domain is not a derived physical
instrument for reading an empty site.

Quantum states describe the conditional event-boundary instrument. The
fixed dwell is part of transition(2); this does not assign changing quantum
density matrices as additional framework states during a Record-free interval
or derive a physical continuous-time clock.

All new Record cylinders are

    Pr(z, relay=z, w)= (1/2) p_z(s0) if w=+,
                      (1/2)(1-p_z(s0)) if w=-.

They normalize, agree with the native ordered Born instrument including
dwell and physical copy, and retain all four native branches.
This is a conditional finite native-to-Record interface, not a full TOE,
a Born selection theorem, arbitrary-input simulator, autonomous formation
law, general many-event construction or axiom-forcing contradiction.

## 8. Author evidence and exact limits

check_block01_native.py builds the7edge-qubit Pauli carrier separately from
the6mode CAR calculation:110 assertions pass. It checks the native pure
state, code ranks, zero-dwell instruments, current signs, number, parity/current
derivatives through order3 and the four-dimensional spectral moments. A
rational Taylor enclosure of the6mode evolution challenges the analytical
nonzero-dwell bounds at s0=1/40. It does not exponentiate the full native
carrier; equivalence at all times follows from the protected intertwiner.

check_block01_local_law.py checks literal geometry/support on all9legal
prefix states, their24proper rotations and one translation:121 named checks
pass, with5050 Record-support visits including rational endpoint fixtures.
The two native probabilities remain symbolic parameters in[1/5,4/5] in
this checker; their actual values are derived and enclosed separately.
The missing relay leaves identical complete neighbor conditions; empirical
copying retains support after unlike second outcomes, while the attempted
unique-neighbor-only copying alternative would fail. The recovery directory
preserves two checker defects and their actual reproductions: incomplete
symbolic interval handling and accidental floating inputs at a rational
fixture. Neither changes the mathematical construction.

The author has reread the complete proof and both checker implementations.
The native and CAR paths share the specified graph and physical conventions;
they are different calculations by the same author, not independent review.
Full nonzero-dwell native identities rely on the supplied code theorem.
Independent source review remains pending. This is a working campaign
checkpoint; no new PR, negative-packet PASS or retained status is claimed.

Source provenance: current main b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf,
the native code parent cited in the copied informative-edge input, and that
provisional input at0b00d351b4c6d4ef6fd737925f5ae403e086cc95. The local-program
prior art ataf8fc05509d69c46c0113c7eaa240caaff3439db supplies context, not a
hidden native implementation premise. SOURCE_PINS.json binds those inputs.
