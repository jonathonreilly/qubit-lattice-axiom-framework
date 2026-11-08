---
claim_id: su2_homogeneous_native_qubit_code_bounded_theorem_note_2026_11_08
claim_type: bounded_theorem
claim_scope: An explicit four-qubit code realizes the five-state SU(2) link and its orientation reversal by geometric site permutation. On every native cubic torus of side 5n, n >= 3, 125 orthogonal coarse-grid code sectors form a subspace invariant under all native translations and proper cubic rotations. Local phase projectors give an exact finite-range extension of a supplied cubic-invariant electric/plaquette Hamiltonian. This is a chosen tensor-product quantum code, not an axiom-selected state, nearest-neighbor admissibility rule, record process, or continuum theory.
upstream_dependencies: []
runner: scripts/gb1_cf_native_placement_exact_2026_11_08.py
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Can the glued five-state SU(2) model be placed homogeneously on native site qubits without changing the axioms?
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: Test whether a native nearest-neighbor admissibility and record law can realize this code and its observables, while comparing alternative frameworks.
conditional_surface_status: Ordinary qubit tensor composition, the supplied SU(2) link model, the code, and the coarse Hamiltonian are explicit conditions.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Explicit isometries, geometric symmetry, orthogonal sectors and finite-range operator extension with a complete finite-dimensional proof.
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A homogeneous native qubit code for the five-state SU(2) model

**Type:** bounded_theorem
**Status:** proposed_retained

This is an author proposal, not an audit verdict. It tests a mathematical
placement on the supplied lattice. Neither the framework nor the selected
gauge model is treated as physically established.

## 1. Exact target and conditions

Use one factor \(\mathbb C^2\) at every native site, ordinary tensor
composition, and the actual permutations of sites induced by translations
and proper cubic rotations. The one-site algebra is \(M_2(\mathbb C)\).
Ordinary generated tensor composition is a stated condition of this model;
it is not additional wording in the Qubit axiom.

On a coarse oriented link use
\(R=\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle,|3\rangle,|4\rangle\}\),
the retained Haar functions \(1,2x_1,2x_2,2x_3,2x_4\) for
\(g=x_4I+i\sum_a x_a\sigma_a\). Its endpoint representation is
\((0,0)\oplus(\tfrac12,\tfrac12)\). Orientation reversal is

\[
K=\operatorname{diag}(1,-1,-1,-1,1).
\]

The link operators are
\(P_\mu=(|\mu\rangle\langle0|+|0\rangle\langle\mu|)/2\),
\(U=P_4I+i\sum_aP_a\sigma_a\), and
\(E^2=\tfrac34\sum_{\mu=1}^4|\mu\rangle\langle\mu|\).
Thus \(KUK=U^\dagger\) and \(KE^2K=E^2\).
Spatial rotations do not rotate the internal gauge-color index.

**Result.** The following explicit code uses a coarse spacing of five native
edges. It retains all 125 grid origins as orthogonal sectors in the same
native qubits. Their direct sum, and a finite-range operator extension on it,
are invariant under the full native space group. A single fixed-origin
sector has only the coarse translation subgroup. The full code therefore
contains an encoding-origin degree of freedom; it is 125 copies of the
coarse link space, not an origin-free identification with one copy.

## 2. A geometric four-qubit link

Let \(e_1=|1000\rangle,e_2=|0100\rangle,e_3=|0010\rangle,
e_4=|0001\rangle\), with positions ordered along the link. Define

\[
\begin{aligned}
J|0\rangle&=(e_1+e_4)/\sqrt2,&
J|4\rangle&=(e_2+e_3)/\sqrt2,\\
J|1\rangle&=(e_1-e_4)/\sqrt2,&
J|2\rangle&=(e_2-e_3)/\sqrt2,\\
J|3\rangle&=(|1100\rangle-|0011\rangle)/\sqrt2.
\end{aligned}
\]

The columns are orthonormal: the two disjoint one-excitation pairs give four
orthonormal vectors, and the last vector has two excitations. Consequently
\(J^\dagger J=I_R\). Reversing the four native positions gives a permutation
unitary \(F\) with

\[
FJ=JK,\qquad Q=JJ^\dagger,\qquad FQF^\dagger=Q,
\qquad Q|0000\rangle=0.
\]

The last identity will distinguish grid origins. For every link operator
\(A\), encode it as \(JAJ^\dagger\). These operators obey the original
products and adjoints on the code. Their identity is \(Q\), not the full
16-dimensional identity: this is a corner embedding. No unused state is
silently declared to be a physical link state. Four qubits are sufficient
for this geometric construction; global optimality is not asserted.

## 3. Disjoint placement and separation of origins

Fix \(n\ge3\) and the native torus
\(\Lambda=(\mathbb Z/(5n)\mathbb Z)^3\). For each
\(p\in(\mathbb Z/5\mathbb Z)^3\), its coarse vertices are \(p+5z\),
with \(z\in(\mathbb Z/n\mathbb Z)^3\). The positive coarse edge
\(v\to v+5\hat e_i\) uses precisely

\[
v+\hat e_i,\quad v+2\hat e_i,\quad v+3\hat e_i,\quad v+4\hat e_i.
\]

Distinct coarse edge interiors are disjoint. Put the code \(J(R)\) on each
edge interior and fix every other native qubit to \(|0\rangle\). This
defines an isometry \(J_p\) from the full coarse link space to a native
subspace \(\mathcal C_p\). Each coarse cell uses 12 active qubits and 113
spectators among its 125 native sites. There are \(3n^3\) coarse links, so
\(\dim\mathcal C_p=5^{3n^3}\). This includes the boundary representations
before Gauss constraints are imposed.

**Separation lemma.** \(\mathcal C_p\perp\mathcal C_q\) for \(p\ne q\).

An active native site has exactly one coordinate differing from its phase
modulo five. Let \(D\) be the nonempty set of coordinates where \(p,q\)
differ. If \(|D|=1\), choose a direction \(i\notin D\): each of the four
interior sites on a \(q\)-edge in direction \(i\) differs from \(p\) in
that fixed coordinate and in coordinate \(i\). If \(|D|=2\), choose the
remaining direction, leaving two fixed differing coordinates. If \(|D|=3\),
any direction leaves two fixed differences. In every case this entire
\(q\)-edge lies in \(p\)-spectators. It is therefore \(|0000\rangle\) on
\(\mathcal C_p\), and orthogonal to that vector on \(\mathcal C_q\).
The conclusion holds for arbitrary entangled link states, because the
spectator factor is fixed on the whole first subspace.

It follows that the native subspace

\[
\mathcal C=\bigoplus_{p\in(\mathbb Z/5\mathbb Z)^3}\mathcal C_p,
\qquad \dim\mathcal C=125\,5^{3n^3},
\]

contains all origins without attaching any external phase register.

## 4. Full geometric covariance and local phase projectors

A native translation by \(a\) sends \(\mathcal C_p\) to
\(\mathcal C_{p+a}\), with phase residues taken modulo five. A proper
cubic rotation sends it to \(\mathcal C_{Rp}\). Such a rotation sends each
edge interior to another, either preserving its traversal order or reversing
all four positions. In the second case \(FJ=JK\) supplies exactly the
required link inversion. Spectators remain spectators. This proves the
intertwining using actual geometric permutations, without compensating gates.
The full direct sum is consequently invariant under every native translation
and every proper cubic rotation about any native site.

For an explicit invariant vector, take the coarse all-\(j=0\) product
vector in every phase and sum its 125 normalized images with equal amplitude.
Orthogonality normalizes the sum by \(1/\sqrt{125}\); geometric operations
permute its summands. This is a mathematical example, not a selected vacuum
or a claim about physically realized records.

At any native site \(x\), define \(D_x\) as the product of \(Q\) on the
six length-five edge interiors incident to \(x\). These supports are
disjoint, so \(D_x\) is an orthogonal projector on 24 qubits, within
Manhattan distance four of \(x\). Reversal invariance of \(Q\) makes this
definition geometric. The separation lemma, applied at \(x\), gives

\[
D_x|_{\mathcal C_p}=
\begin{cases}I,&x\equiv p\pmod5,\\0,&x\not\equiv p\pmod5.\end{cases}
\]

Thus origin selection for a local operator needs no nonlocal sector projector.
The different \(D_x\) need not commute on the entire native Hilbert space;
their stated action on \(\mathcal C\) suffices.

## 5. An exact finite-range extension of a supplied generator

Let \(H\) be the coarse sum of equal-coefficient electric terms and
equal-coefficient elementary magnetic plaquette terms. A magnetic term is the
real color trace of the oriented product of the four \(U\)'s. Reverse
edges use \(U^\dagger\). Rotations permute the plaquettes and change a
chosen traversal only by cyclic order or reversal. Different links commute
entrywise, so cyclic color trace and real-part reversal leave the sum
unchanged. Together with the electric identity in section 1, this proves
the coarse cubic invariance used below.

Choose a seed \(h_0\) containing the three outgoing electric terms and the
three positive coordinate-plane plaquette terms. Summing its coarse
translates counts each physical term once. Encode its supported links using
\(J\) to obtain \(\widetilde h_0\), and put
\(a_0=D_0\widetilde h_0D_0\). Each term maps the true-phase code to itself;
the right \(D_0\) annihilates every other phase. The left one ensures a
self-adjoint extension and acts identically on the true code.

For \(O\) the 24 proper cubic rotations and \(T_x,U_R\) their native
permutation unitaries, define

\[
H_{\rm native}=\frac1{24}\sum_{x\in\Lambda}\sum_{R\in O}
T_xU_Ra_0U_R^\dagger T_x^\dagger.
\]

Reindexing the finite sums proves full native translation and rotation
invariance. On \(\mathcal C_p\), only \(x\equiv p\pmod5\) contributes.
For each \(R\), that sum restricts to the rotated coarse Hamiltonian,
which is \(H\). Therefore

\[
H_{\rm native}J_p=J_pH\quad\text{for every }p.
\]

The same isometries preserve gauge constraints and polynomial identities
between compatible observables, including regional Gauss gluing on this fixed
coarse graph. This placement does not allocate artificial subdivision vertices
or additional cut-link registers. Transporting a subdivision map requires
separately supplied source and target encodings. The Hamiltonian does not mix phases.
It does not select the code, eliminate other native states, or supply a
physical origin-selection mechanism.

Each seed is supported within Manhattan radius nine: the farthest plaquette
interior has offset \(5+4\), while the phase detector reaches four. Thus
each interaction has diameter at most 18 native spacings. The finite
certificate gives diameter 13 for this particular seed. This is finite
range, not a nearest-neighbor rule or a finite-depth update schedule.
No spectral or ground-state claim is made for the off-code complement.

On \(\mathbb Z^3\), the same local supports, code constraints and symmetry
identities make sense without a chosen infinite tensor-product Hilbert
representation. The finite-volume theorem above supplies no thermodynamic
limit or physical infinite-volume state theorem.

## 6. A finite capacity test of the same-spacing identification

For any connected finite graph with \(V\) vertices and \(E\) edges, the
five-state link space has dimension \(5^E\). Every even occupied-edge
pattern contributes at least one Gauss singlet: occupied half-spin ends
can be paired at each vertex. Regrouping all endpoint factors by vertices
gives a nonzero invariant vector; different edge-occupation patterns are
orthogonal. The binary incidence matrix has rank \(V-1\): its rows sum
to zero, and a reduced spanning-tree minor is nonsingular by leaf removal.
Consequently

\[
\dim\mathcal H_{\rm Gauss}\ge2^{E-V+1}.
\]

On the open \(3\times3\times3\) cube, \(V=27,E=54\), giving at least
\(2^{28}\) physical states compared with \(2^{27}\) states of 27 ordinary
qubits. On the periodic three-cube the corresponding values are
\(V=27,E=81\), and the lower bound is \(2^{55}\). These are explicit
finite counterexamples to encoding the entire respective physical sector
isometrically in the same number of site qubits. They do not test a
restricted low-energy sector, extra boundary storage, other composition
rules, or the coarse construction above.

## 7. What this says about the framework

The construction supplies a space-group-invariant code on one qubit per
native site, with a local way to identify its encoding origin. It closes a
kinematic placement question under the specified tensor-product model.
It uses an origin sector structure, coarse spacing, code and spectator
preparation that are choices, not consequences of the axioms. Computational
basis symbols specify the encoding; they are not asserted to be privileged
physical possibilities or readable Record contents.

The [current axioms](MINIMAL_AXIOMS_2026-06-29.md) require a covariant
nearest-neighbor probability law and permanent records with content-only
readout. Neither follows from this finite-range Hamiltonian. The realized-
state primitive supplies no prepared code state or block origin. Enlarging
local site content, placing fundamental degrees on links, changing the gauge
model, or seeking only an emergent low-energy representation are legitimate
alternatives to compare if the native law fails. No axiom is edited here,
and the encoding is not evidence that this framework is physically correct.

## Evidence and prior work

The [exact runner](../scripts/gb1_cf_native_placement_exact_2026_11_08.py)
checks the link matrix units, inversion, all phase residues, all 24 rotations,
disjoint supports, local detector geometry and incidence ranks. The
[cache](../logs/runner-cache/gb1_cf_native_placement_exact_2026_11_08.txt)
records the actual execution. Three separately executed defects are rejected:
wrong inversion parity, allowing nonzero overlap with the all-zero vector,
and retaining a preferred grid origin. These checks supplement the general
proof; they do not test a physical formation law.

The [native research record](../.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/native_placement/HANDOFF.md)
binds the source, independent comparison, full outputs and verification limits.
Independent mathematical checking is separate from formal landing and audit.
The [scope stress test](SU2_HOMOGENEOUS_NATIVE_QUBIT_CODE_SCOPE_CHECK_2026-11-08.md)
records the finite capacity witnesses and the live alternatives.

Arrighi, Fargetton and Wang distinguish direct coding from grouped simulation
in [their QCA paper](https://arxiv.org/abs/0704.3961), definitions 7–14. That
distinction motivates keeping coarse coding separate from native dynamics;
their universality theorem is not used here. The repo's MDTN embedding
outline on [PR #10135](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10135)
explicitly leaves fine-translation covariance open in sections 3.6 and 9.5.
The present explicit origin sectors and local projectors address that
kinematic issue without using its gap claim or identifying its proposed
Gauss constraints with Admissibility. No literature-priority claim is made.
