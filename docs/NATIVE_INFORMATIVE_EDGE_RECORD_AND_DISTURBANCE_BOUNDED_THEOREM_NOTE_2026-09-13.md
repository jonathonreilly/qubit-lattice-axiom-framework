---
claim_id: native_informative_edge_record_and_disturbance_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "On the supplied finite native edge/CAR carrier with a connected protected graph, any full-carrier protected binary effect has an explicit cycle-pulse realization as a single-site edge Record with the corresponding decoded Lueders instrument. Native parity pulses have bounded plaquette-star support, exact selective and averaged current/energy formulas, a sharp contrast/disturbance relation and even-Slater finite-history updates. Born weights, code, preparation, controls and scheduling remain supplied; a complete physical nearest-neighbor Record law is not derived."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_informative_edge_record_2026_09_13.py
---

# Native informative edge Records and their matter disturbance

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

An explicit pulse turns a native nonbridge edge Record into a binary
measurement of protected matter while the protected graph stays connected.
The parity specialization gives its exact information, disturbance, current
and matter-energy account. This is a conditional quantum-carrier theorem;
Born probabilities, preparation, pulse selection and occurrence remain inputs.
Actual current-surface status is conditional-support. Independent source
review and formal audit remain pending.

~~~yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Full-carrier operator identities and a general finite-history proof, with exact physical Pauli and separately constructed CAR/Slater checks."
trace_class: upstream_support
target_claim_id: native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
target_blocker_text: "Obtain matter information through a native edge Record without requiring that event to disconnect the protected matter graph."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply a complete neighboring-Record carrier for the event statistic and a physical law selecting preparation, controls and occurrence."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

| Input or obligation | Treatment |
|---|---|
| [Native edge/CAR source](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md), equations1–4 and Theorems1–3 | Conditional carrier, code, nonbridge isometry, number and hopping dictionary; the required hypotheses are restated below |
| Ordinary composition, finite graph, protected spanning graph, input quantum state and Pauli frame | Supplied physical/model conditions |
| Full-carrier positive effect, cycle pulse, Born/Lueders readout and event schedule | Supplied program and event conditions; the resulting native instrument is derived |
| Connected matter instrument, parity response, instantaneous current/energy and pure even-Slater update | Proved below on the declared domain |
| Physical local Record law, preparation, calibration, autonomous control and total apparatus energy | Separate open obligations |

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) does not by itself
select this quantum carrier or program. The approved scale, kinetic-isotropy
and realized-state primitives are not treated as missing premises. This
calculation does not add an axiom, primitive, fitted observation, editable
prompt or audit verdict.

## 1. Physical algebra and supplied inputs

Use the finite connected simple graph and actual edge qubits of the native
edge-Record note of2026-09-05. Vertices are at2v and the qubit for(v,v+e_a)
at2v+e_a. With fixed vertex labels and neighbor orders, define

\[
B_i=\prod_{e\ni i}Z_e,\quad
A_{ij}=\epsilon_{ij}X_{ij}
 \prod_{k<_i j}Z_{ik}\prod_{l<_j i}Z_{jl},\quad
T_{ij}=\frac i2 A_{ij}(B_i-B_j).
\tag{1}
\]

For an oriented cycle C of length l, S_C=i^l product_C A is a central
Hermitian involution; its X support is the cycle. The remaining code P
fixes every remaining cycle to+1 and every old Record Z to its recorded
sign. On a connected remaining graph it faithfully carries the global
even-CAR algebra, with

\[
B_v=1-2n_v,\quad A_{ij}=-i\gamma_{2i}\gamma_{2j},\quad
T_{ij}=c_i^\dagger c_j+c_j^\dagger c_i.
\tag{2}
\]

Odd global parity is absent on the unaugmented carrier. A fixed total-N
sector is allowed only when it is compatible with that even parity.

Protect a connected spanning subgraph \(\mathcal B\). Candidate edges
outside it never hop: the supplied matter Hamiltonian is
\(H_{\mathcal B}=\sum_{f\in\mathcal B}a_fT_f\), real|a_f|<=t.
Every unused candidate e has a cycle C_e made of e and a protected path.
Let S=S_Ce, Z=Z_e, Q_z=(I+zZ)/2. Then SP=P and{S,Z}=0.
The protected physical algebra \(\mathcal A_{\mathcal B}\), generated
by all B_v and protected A_f, commutes with S,Z and all old Record Z's.
The maps J_z=sqrt2 Q_zP are isometries from the incoming code onto the
new code after e records. They intertwine every protected observable.

Ordinary composition, this placement/code, the input state, Hamiltonian,
chosen pulse/effect and its Born/Lueders event/schedule are supplied.
They are not selected by the four current framework axioms. The result
does not identify a quantum density matrix as extra framework ontology.

## 2. Any protected binary Lueders effect at the native edge

Let E be a physical full-carrier operator in \(\mathcal A_{\mathcal B}\)
with0<=E<=I on that full carrier. Positivity merely on P is insufficient
for the following physical functional calculus. Define

\[
E_+=E,\quad E_-=I-E,\quad
a=\frac{\sqrt E+\sqrt{I-E}}{\sqrt2},\quad
b=\frac{\sqrt E-\sqrt{I-E}}{\sqrt2},\quad U_E=a+bZS.
\tag{3}
\]

These commuting Hermitian functions of E commute with Z,S, and a²+b²=I.
Since(ZS)†=-ZS and(ZS)²=-I, U_E†U_E=I on the full physical carrier.
Using SP=P and Q_z Z=zQ_z gives the exact code identity

\[
K_zP:=Q_zU_EP
=(a+zb)Q_zP=J_z\sqrt{E_z}P.
\tag{4}
\]

Thus, for every protected O and arbitrary code state, including an
entangled external reference,

\[
PK_z^\dagger K_zP=PE_zP,\qquad
PK_z^\dagger O K_zP=P\sqrt{E_z}O\sqrt{E_z}P.
\tag{5}
\]

This is the binary Lueders instrument after decoding through J_z. Its
single-site physical Record is the actual Z_e outcome. No new clean pointer
qubit was appended; the incoming cycle code is an essential supplied
resource. Generic E can have extensive support. Functional calculus stays
inside its tensor-factor support, so support(U_E) is contained in the union
of support(E) and support(ZS), without a general locality bound for E.

Every unused cycle of the form f plus a protected path excludes e and
commutes with U_E and Q_z. Old Records also commute. The next code is
therefore valid: these cycles together with the protected cycles generate
all remaining cycle relations, by choosing a spanning tree inside the
protected graph. The construction repeats, even for noncommuting
successive protected effects. Induction of(4) gives the ordinary ordered
Lueders history, with any supplied protected Hamiltonian dwell interleaved.
Generic effects need not conserve N. This is the standard binary dilation
algebra realized in this existing native cycle carrier, not a Born derivation.

## 3. Native parity pulse, selective update and bounded support

Choose a vertex v incident to e and put B=B_v. Let0<=theta<=pi/2,
c=cos(theta/2),s=sin(theta/2), kappa=sin(theta), eta=cos(theta).
The physical Hermitian involution Y=iZS commutes with B. Set

\[
U_v=\exp[-i\theta BY/2]=cI+sBZS,\qquad
F_z=(cI+zsB)/\sqrt2,\qquad E_z=\tfrac12(I+z\kappa B).
\tag{6}
\]

Both F_z are positive on this theta range, and K_zP=J_zF_zP.
For m=Tr(rho B),

\[
p_z=\tfrac12(1+z\kappa m),\quad
\rho_z=F_z\rho F_z/p_z,\quad
m_z=\frac{m+z\kappa}{1+z\kappa m}.
\tag{7}
\]

Only p_z>0 branches are normalized. The decoded nonselective channel is

\[
\Lambda_v(\rho)=c^2\rho+s^2B\rho B
=\tfrac{1+\eta}{2}\rho+\tfrac{1-\eta}{2}B\rho B.
\tag{8}
\]

Write O=O_++O_- with O_±=(O±BOB)/2. Direct expansion of F_z O F_z gives

\[
\langle O\rangle_z=
\frac{\langle O_+\rangle+z\kappa\langle BO_+\rangle
 +\eta\langle O_-\rangle}{1+z\kappa m},\qquad
\Lambda_v^*(O)=O_++\eta O_-.
\tag{9}
\]

All coefficients, including the selective denominator, are derived from
the same instrument. For a plaquette C_e, the generator BY lies within
the four vertex stars. Those stars have at most4*6-4=20 distinct edge
factors in the cubic graph, each at physical Manhattan distance at most4
from the candidate midpoint. B_v adds none outside these stars. This is
a bounded support pulse, not a nearest-neighbor gate synthesis or an
autonomously selected Hamiltonian.

At kappa=0 the pulse is the fair state-preserving event. At kappa=1 it
projectively measures vertex parity while the protected graph stays
connected. Later hopping can change that parity: the permanent edge Z
records its value at this event, not an eternally frozen occupation.
For all strengths, [B,N]=0, so every branch preserves a sharp N and the
nonselective channel preserves the full initial N distribution. A selective
branch can update the classical probabilities of different N sectors
when B is correlated with N; it does not generally preserve that distribution.

## 4. Current and a common matter-energy ledger

For oriented protected i<j define

\[
I_{ij}=ia_{ij}(c_i^\dagger c_j-c_j^\dagger c_i)
=-\tfrac{a_{ij}}2 A_{ij}(I-B_iB_j).
\tag{10}
\]

The second equality follows by expanding the Majoranas in(2) and projecting
onto opposite occupations. This observable anticommutes with B_v exactly
when v is one endpoint, and otherwise commutes. The instantaneous mean
incident current is multiplied by eta nonselectively and by
eta/(1+z kappa m) conditionally. A nonzero incident mean keeps its sign on
supported branches when theta<pi/2. A disjoint current is unchanged
nonselectively, but can update conditionally through its correlation with B.
These statements do not assert persistent transport for arbitrary later
interleaved histories; information acquisition changes the matter state.

The odd part of H_B under B_v is exactly

\[
H_-:=\tfrac12(H_{\mathcal B}-B_vH_{\mathcal B}B_v)
=\sum_{f\in\mathcal B:f\ni v}a_fT_f.
\tag{11}
\]

Consequently, using one fixed Hamiltonian and energy zero,

\[
\Delta\overline E_{\rm matter}
=-(1-\eta)\langle H_-\rangle,\qquad
|\Delta\overline E_{\rm matter}|
\le(1-\eta)\|H_-\|
\le6t(1-\eta).
\tag{12}
\]

The last bound uses degree at most6 and||T_f||<=1. No candidate hopping
is deleted at this event because it was zero from the outset. Equation(12)
accounts for the matter change under the complete pulse and readout; the
pulse usually does not commute with H_B. An energy-conserving controller,
battery and its preparation remain an additional physical obligation.

## 5. Sharp contrast versus disturbance: elementary proof

For any finite instrument with Kraus operators A_zr on a finite code, let
Lambda be its decoded nonselective channel. A fixed desired output unitary
may first be undone in this definition. Let epsilon=||Lambda-Id||_diamond
using the full trace norm convention, without a factor1/2. For two
orthonormal inputs|0>,|1>, let p_z,q_z be its outcome distributions and
D=(1/2)sum_z|p_z-q_z| their total variation distance. Then

\[
\epsilon\ \ge\ 1-\sqrt{1-D^2}.
\tag{13}
\]

To prove this, the preserved coherence coefficient is

\[
u=\langle0|\Lambda(|0\rangle\langle1|)|1\rangle
=\sum_{z,r}\langle0|A_{zr}|0\rangle
 \overline{\langle1|A_{zr}|1\rangle}.
\]

Cauchy-Schwarz within each outcome gives
|u|<=sum_z sqrt(p_z q_z)=b, because each diagonal Kraus amplitude is at
most the corresponding output-vector norm. The diamond norm bounds the
induced trace norm on the unit-trace-norm operator|0><1|, hence|u-1|<=epsilon.
Thus b>=1-epsilon if epsilon<=1. A second Cauchy-Schwarz inequality gives

\[
D^2=\tfrac14\left(\sum_z|\sqrt{p_z}-\sqrt{q_z}|
 (\sqrt{p_z}+\sqrt{q_z})\right)^2
\le1-b^2\le2\epsilon-\epsilon^2.
\]

Rearrange for(13); for epsilon>1 the bound is immediate since its right
side is at most1. No restriction to two-dimensional codes, pure output
states, minimal dilations or ancilla-free implementations was made.

If the native code contains both B eigenvalues, take its two eigenstates.
Equation(6) gives D=kappa. Equation(8) gives
epsilon=(1-eta)||Ad_B-Id||_diamond/2=1-eta: the upper bound is2 for the
channel difference, and the balanced superposition of opposite B states
has orthogonal images under B, attaining2. Thus(13) is saturated exactly.
If a further restriction makes B scalar, both contrast and disturbance
vanish and the saturation statement with D=kappa does not apply there.

This is an elementary information-disturbance optimization and its native
realization. Information-disturbance tradeoffs are established mathematics;
see Kretschmann, Schlingemann and Werner,
[quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009), for the general
channel context. The proof above does not import a theorem from that paper.
Preservation of one observable is much weaker than closeness of the full
channel: B itself is exactly preserved nonselectively while D can be positive.

## 6. Exact even-Slater history update

For theta<pi/2, each F_z is a positive multiple of an exponential of n_v:

\[
F_z=a_z r_z^{n_v},\quad
a_z=(c+zs)/\sqrt2,\quad r_z=(c-zs)/(c+zs)>0.
\tag{14}
\]

Consider a pure Slater determinant of even particle number on the connected
code. Define C_ij=<c_j†c_i>, its occupied-space orthogonal projector,
nu=C_vv, R=I+(r_z-1)|v><v| and d=r_z²-1. Its conditional one-particle
projector is

\[
C'=R\left[C-\frac{d\,C|v\rangle\langle v|C}{1+d\nu}\right]R,
\quad p_z=a_z^2(1+d\nu)
=\tfrac12[1+z\kappa(1-2\nu)].
\tag{15}
\]

Proof: write the orthonormal occupied orbitals as the columns of V.
The many-particle filter maps their wedge to the wedge of RV, with squared
norm det(V†R²V)=1+d nu. The normalized occupied projector is
RV(V†R²V)^(-1)V†R. The rank-one inverse formula yields(15).
The denominator is positive since r_z>0 and0<=nu<=1. Hence C'²=C',
Tr C'=Tr C, and the state remains a pure even Slater determinant.
Any number-conserving quadratic dwell applies its one-particle unitary to
the occupied subspace. Induction gives a closed exact finite history within
this supplied state class. Projective endpoint branches are obtained directly
from F_z, or their nonzero-branch limits; formula(14) is not used at a zero
denominator. In this convention <I_ij>=2a_ij Im C_ij.

No closure is claimed for an even-parity-conditioned mixed Gaussian:
conditioning on global parity generally destroys Gaussianity. The input
Slater state, orbital phases and preparation are still conditions, and the
full matrix C is not a demonstrated local Record statistic.

## 7. The precise remaining local-law question

Fix nonzero kappa and a finite or countable specified ready-history family.
The local matrix conditions have their usual Borel sigma algebra. Let eta_h denote
the COMPLETE physical nearest-neighbor Record condition at the forming edge
(distinct from the cosine eta in earlier sections). The candidate's native
binary probabilities are p_z(h)=[1+z kappa m_v(h)]/2. There exists one
binary content law on this family depending only on eta_h if and only if

\[
\eta_{h_1}=\eta_{h_2}\quad\Longrightarrow\quad
m_v(h_1)=m_v(h_2).
\tag{16}
\]

This follows by inversion of p_+(h); sufficiency defines the law on each
fiber. Its realized condition set is countable, so this map is Borel there
and extends measurably by a fixed binary law elsewhere. For an uncountable
ready family, fiber constancy is only the set-theoretic factorization
criterion; the induced mean on conditions must additionally be measurable
to define a stochastic kernel. No such measurability is inferred solely
from fiber constancy. At kappa=0 the fair kernel works automatically.
If two same-condition histories
have means m_1,m_2, their native outcome total variation is
|kappa||m_1-m_2|/2. Any one proposed law for that condition has maximal
error at least|kappa||m_1-m_2|/4 on the pair; the midpoint law attains it.
This is a two-distribution optimization, not an exhaustion of physical
carrier constructions or a general framework impossibility theorem.

The current proposal has not encoded m_v(h), or a sufficient alternative,
into complete neighboring permanent Records for every supported native
history. Merely supplying two distinct quantum preparations at the same
Record condition would test this chosen ready family; it would not prove
that they are two admissible full framework states. Equation(7) updates m
at the measurement, but Hamiltonian dwell also requires correlations.
Equation(15) closes a quantum calculator, not the physical local carrier.

This construction therefore supplies a matter-informative native event, its exact
disturbance and energy price, and an explicit remaining factorization test.
It neither derives physical Born probabilities from the axioms nor forces
an axiom update. Occurrence, control, preparation, covariance of role choice,
physical calibration and a complete nearest-neighbor Record law remain open.

## 8. Checks, prior work and authority

The [primary runner](../scripts/native_informative_edge_record_2026_09_13.py) performs188 exact grouped assertions.
It independently assembles physical ordered Pauli operators on a four-edge
square and two adjacent squares with seven edge qubits. The latter tests
two noncommuting effects, preservation of the first Record and the unused
cycle, and the full ordered history effect. Constant effects0/I test zero
branches without normalization. Five parity strengths include both endpoints.
A positive input has nonzero matter parity, bond current and bond energy.
The physical continuity commutator independently checks each current sign.

A separate occupation-bit four-mode CAR construction verifies the current
dictionary and the Gram update of a complex two-particle Slater state through
two informative events and an intervening quadratic dwell. An explicit
even-state mixture changes its conditional mean particle number from1 to2/5;
this supports the selective-sector-weight qualification in section3.
There is no numerical tolerance, Monte Carlo estimate or SDP in these checks.
Finite examples support the written general proof; they do not replace it.

Generic binary dilation and information-disturbance tradeoffs are established
mathematics. The contribution here is their explicit realization and resource
account on this supplied physical cycle carrier. Existing native bridge
parity measurements and fair nonbridge isometries are in the linked parent.
Programmed leaf filtering and bridge entangling are related prior proposals;
neither their unlanded conclusions nor their source bytes are proof inputs.

The [source manifest](../.claude/science/physics-loops/native-informative-record-20260913/SOURCE_MANIFEST.json) preserves discovery
provenance. The [cold review and recovery record](../.claude/science/physics-loops/native-informative-record-20260913/REVIEW_HISTORY.md)
records the measurable-factor qualification found by the author; the original
proof is retained in the packet. The [mutation results](../.claude/science/physics-loops/native-informative-record-20260913/mutations/RESULTS.json)
record actual altered sources and rejected predicates. The
[scope record](../.claude/science/physics-loops/native-informative-record-20260913/NO_GO_DISCIPLINE_CHECKLIST.md) distinguishes the
positive construction/optimization from a carrier-exhaustion claim.

All current mathematical inputs are on main or in this delta. Independent
source review is pending. The full mechanical pipeline, strict lint and
ledger-based changed-evidence validation on the exact combined current-main
candidate remain integration gates before landing. The author does not
land science, invoke formal audit or assign an audit verdict.
