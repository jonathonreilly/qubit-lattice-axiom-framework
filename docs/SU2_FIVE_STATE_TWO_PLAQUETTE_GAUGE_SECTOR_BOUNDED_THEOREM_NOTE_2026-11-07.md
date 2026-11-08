---
claim_id: su2_five_state_two_plaquette_gauge_sector_bounded_theorem_note_2026_11_07
claim_type: bounded_theorem
claim_scope: On the specified seven-link, two-square graph with a five-state SU(2) quantum link on each edge and zero external charge at all six vertices, the gauge-invariant Hilbert space has dimension four. Its magnetic and electric matrices, an explicit nonzero shared-link commutator, and a finite-angle gauge-invariant square-exchange-symmetric joint update are derived exactly. Finite qubit encodings are given. No homogeneous cubic update, physical-law selection, record dynamics, continuum identification or mass gap is established.
upstream_dependencies: []
runner: scripts/gb1_cf_two_plaquette_s1_2026_11_07.py
actual_current_surface_status: candidate-retained-grade
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: Extend the finite-register gauge construction to compatible overlapping plaquettes within the current lattice axioms (GB1-CF).
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: Construct and check a spatially covariant overlap rule and homogeneous qubit allocation; then test the unchanged Admissibility and Record clauses.
conditional_surface_status: The theorem assumes the explicit finite link representation, graph, all-vertex zero-charge sector, and operators specified below.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Exact finite-dimensional conditional theorem with a complete sector count, explicit operators, and an all-angle invariant joint update.
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Two overlapping plaquettes with five-state SU(2) links

**Type:** bounded_theorem
**Status:** proposed_retained

This is an author proposal for a conditional finite-model result, pending
independent landing review and audit. The physical axioms are unchanged.

## Target and supplied model

**Claim.** The specified two-square SU(2) model has the four-dimensional
physical sector and operators displayed below, and its joint magnetic update,
also when composed with its electric layer, preserves gauge invariance and
exchange of the two squares at every real step angle.

The graph has vertices

\[
A=(0,0),\quad B=(1,0),\quad C=(2,0),\quad
D=(0,1),\quad E=(1,1),\quad F=(2,1),
\]

and oriented links \(AB,BC,DE,EF,AD,BE,CF\). The two squares share \(BE\).
There are no external links or matter charges, and the Gauss singlet condition
is imposed at all six vertices. This boundary sector is supplied data.

Each link has orthonormal basis \(|0\rangle,|1\rangle,\ldots,|4\rangle\), with

\[
P_\mu=\frac{|\mu\rangle\langle0|+|0\rangle\langle\mu|}{2},\qquad
U=P_4 I_2+i\sum_{j=1}^3P_j\sigma_j,\qquad
E_\ell^2=\frac34\sum_{\mu=1}^4|\mu\rangle\langle\mu|.
\]

These are explicit model definitions. The link matrix \(U\) is not assumed
unitary. The chosen representation is the five-state member of the quantum-link
family, not a claim about the minimum possible SU(2) register.

Equivalently, on normalized SU(2) Haar space let
\(g=x_4I+i\sum_jx_j\sigma_j\), \(\sum_\mu x_\mu^2=1\), and take
\(R=\operatorname{span}\{1,2x_1,2x_2,2x_3,2x_4\}\).
Haar invariance gives \(\int x_\mu=0\) and
\(\int x_\mu x_\nu=\delta_{\mu\nu}/4\). Thus the stated functions are
orthonormal, and compressed multiplication by \(x_\mu\) is exactly \(P_\mu\).
This is a finite mathematical construction, not an axiom-level choice of law.

## Gauge covariance and loop convention

For a link from \(x\) to \(y\), use the pullback
\(T(h_y,h_x)f(g)=f(h_y^{-1}gh_x)\). It preserves \(R\), so its projector
commutes with the pullback. Compressed multiplication therefore obeys

\[
T^\dagger U T=h_y U h_x^{-1}.
\]

For a traversal \(F_1,\ldots,F_n\), holonomy means \(F_n\cdots F_1\);
reversed traversal uses \(U^\dagger\). In this convention

\[
X_L=U_{AD}^\dagger U_{DE}^\dagger U_{BE}U_{AB},\qquad
X_R=U_{BE}^\dagger U_{EF}^\dagger U_{CF}U_{BC},
\]

and \(B_L=\operatorname{tr}X_L+(\operatorname{tr}X_L)^\dagger\), with the
same definition for \(B_R\). Adjacent gauge factors cancel in the reverse
traversal product, leaving conjugation at the starting vertex; its trace is
invariant. Each magnetic operator is Hermitian and gauge invariant on the
entire link Hilbert space. \(E_\ell^2\) also commutes with both endpoint
actions, since it is scalar on each endpoint representation sector.

## Complete physical sector

The link representation is \((0,0)\oplus(\tfrac12,\tfrac12)\). Call a link
occupied when it is in the four-dimensional second summand. At a vertex with
at most three incident edges, a singlet requires an even number of occupied
ends: the central element \(-I\) acts by \((-1)^n\). Zero occupied ends
give one singlet. Two occupied ends also give exactly one. After identifying
each dual doublet with the defining doublet using the SU(2) invariant epsilon
tensor, this is the antisymmetric tensor in
\(\mathbb C^2\otimes\mathbb C^2\). In the natural oriented labeling a mixed
incoming/outgoing pair instead uses the delta contraction in \(V\otimes V^*\).

Consequently the admissible occupied-edge patterns are the even subgraphs.
On this graph they are the empty pattern, left square, right square and outer
rectangle. Equivalently, the connected graph's binary cycle space has dimension
\(7-6+1=2\); listing its four elements gives precisely those patterns.
Each pattern has a unique singlet contraction. The physical dimension is four.

Use the basis \((|\varnothing\rangle,|L\rangle,|R\rangle,|O\rangle)\).
The first vector is the constant Haar function, called the **empty-flux
reference**, not the physical vacuum. The other three are fundamental Wilson
traces around the indicated cycles. Every edge occurs at most once, so those
functions lie in \(R^{\otimes7}\). Their norms are one: integrating along a
cycle reduces the norm to \(\int_{SU(2)}\chi_{1/2}(g)^2\,dg=1\).
Different occupied-edge patterns are orthogonal.

## Exact magnetic and electric matrices

In that basis the operators are

\[
B_L=\begin{pmatrix}
0&2&0&0\\2&0&0&0\\0&0&0&1\\0&0&1&0
\end{pmatrix},\qquad
B_R=\begin{pmatrix}
0&0&2&0\\0&0&0&1\\2&0&0&0\\0&1&0&0
\end{pmatrix},\qquad
E=\sum_\ell E_\ell^2=\operatorname{diag}(0,3,3,9/2).
\]

Here is a direct derivation of the magnetic coefficients. The square trace is
real for SU(2), so on Haar space the magnetic operator is twice multiplication
by that trace, compressed to the finite link space. Its empty-to-square
matrix element is twice the norm squared of the square trace, hence 2.

For the other matrix element, put \(h=g_{BE}\),
\(a=g_{AB}g_{AD}^{-1}g_{DE}^{-1}\), and
\(b=g_{EF}^{-1}g_{CF}g_{BC}\). Cyclicity of the scalar matrix trace gives
\(\chi_L=\operatorname{tr}(ha)\),
\(\chi_R=\operatorname{tr}(h^{-1}b)\), and
\(\chi_O=\operatorname{tr}(ab)\). Fundamental Haar orthogonality yields

\[
\int dh\,\operatorname{tr}(ha)\operatorname{tr}(h^{-1}b)
=\tfrac12\operatorname{tr}(ab).
\]

Thus \(\langle O|B_L|R\rangle=2\cdot\tfrac12\int\chi_O^2=1\).
The right-square calculation is exchanged. Each \(P_\mu\) changes a link
between its empty and occupied summands, so there are no other matrix entries.
The electric values count four, four and six occupied links, each costing
\(3/4\) in the declared normalization.

The shared-link commutator has the exact positive witness

\[
[B_L,B_R]=3\bigl(|L\rangle\langle R|-|R\rangle\langle L|\bigr),
\qquad [B_L,B_R]|L\rangle=-3|R\rangle.
\]

This witness lies within the Gauss-constrained sector.

## Finite-step updates and square exchange

Let \(S\) exchange \(|L\rangle\) and \(|R\rangle\), fixing the other two
basis vectors. This is induced by exchange of the two geometric squares, with
the corresponding link inversions. It is one patch symmetry, not the full
cubic-lattice covariance requirement. It satisfies
\(SB_LS=B_R\) and \(SES=E\).

For \(T(\theta)=e^{-i\theta B_L}e^{-i\theta B_R}\), exact Taylor expansion gives

\[
T-STS=-\theta^2[B_L,B_R]+O(\theta^3).
\]

For the palindromic product
\(T_L^{\mathrm{sym}}=e^{-i\theta B_L/2}e^{-i\theta B_R}e^{-i\theta B_L/2}\),
the exchange difference instead starts as

\[
T_L^{\mathrm{sym}}-ST_L^{\mathrm{sym}}S
=-\frac{i\theta^3}{8}[B_L+B_R,[B_L,B_R]]+O(\theta^4).
\]

On \(|\varnothing\rangle\) the displayed cubic coefficient is
\(3i(|L\rangle-|R\rangle)/4\). These are explicit nonzero coefficients for
the specified products. They assert neither failure at every angle nor a
general impossibility for other schedules.

A positive construction is the joint gate. Set \(H=B_L+B_R\). Direct matrix
multiplication gives \(H^3=10H\), hence for all real \(\theta\)

\[
J(\theta)=e^{-i\theta H}
=I+\frac{\cos(\sqrt{10}\theta)-1}{10}H^2
-i\frac{\sin(\sqrt{10}\theta)}{\sqrt{10}}H.
\]

It is unitary and satisfies \(SJS=J\). On the full finite link space the
same construction \(e^{-i\theta(B_L+B_R)}\) is gauge invariant because its
Hermitian generator is. The closed formula above is its restriction to the
four-state sector. For all real \(\tau,\theta\),

\[
V(\tau,\theta)=e^{-i\theta(B_L+B_R)}e^{-i\tau E}
\]

preserves gauge invariance and square exchange. This defines a finite-step
model; it does not select a physical Hamiltonian logarithm or a physical clock.

## Qubit encodings and their scope

The full link model embeds into three qubits per link by assigning the five
basis states to five distinct computational words. Extend the link matrices
by zero on the remaining three words and extend the group action trivially.
The code projector commutes with the extended Hermitian generators, so their
exponentials preserve the code. Equivalence to the link model holds on this
initialized code subspace. The unused words add extra singlets, so gauge
invariance alone does not enforce that initialization. Seven links use 21
qubits in this direct encoding; that is a sufficient count, not a minimum.

The constrained patch also has a two-logical-qubit encoding:
\(|\varnothing\rangle\mapsto|00\rangle\), \(|L\rangle\mapsto|10\rangle\),
\(|R\rangle\mapsto|01\rangle\), \(|O\rangle\mapsto|11\rangle\).
With \(n_j=(I-Z_j)/2\), its operators become

\[
B_L=X_1(2-n_2),\qquad B_R=(2-n_1)X_2,\qquad
E=3(n_1+n_2)-\tfrac32 n_1n_2.
\]

This is an exact finite-dimensional encoding. Neither encoding identifies the
original link and vertex geometry with a homogeneous allocation of the physical
site qubits. In particular, a two-logical-qubit compression of the closed patch
does not specify how overlapping patches glue while preserving local observables.

## Relation to the current lattice axioms

No change to the one-site \(M_2(\mathbb C)\) algebra is needed to represent the
finite matrices on qubit blocks. However, an encoding is only one part of the
native implementation question. The following are still open in this probe:

- one homogeneous three-dimensional code/observable assignment, with the
  required translation and proper-cubic-rotation covariance;
- a fixed finite-depth nearest-neighbor implementation of compatible
  overlapping joint gates on that assignment;
- one physical admissibility law and record evolution satisfying the unchanged
  Admissibility and permanent Record clauses;
- the selected state, Euclidean representation and continuum comparison.

The model's group, boundary sector and interaction were specified, not selected
by the axioms. This result supplies a coupled finite-patch example for GB1-CF;
the full target remains open. It establishes no gauge boson, continuum
Yang-Mills theory, vacuum identification, confinement or mass gap.

## Proof dependencies and edge cases

The proof uses the explicit link matrices, elementary SU(2) covariance and
Haar orthogonality, local two-spin singlets, and the displayed finite graph.
The sector count, operator coefficients and update claims are derived above.
No unmerged branch theorem is required to reproduce them.

The imported mathematical machinery is ordinary finite-dimensional SU(2)
representation theory and normalized Haar integration; its needed special
cases are derived here. The group, five-state representation, seven-link graph,
zero-external-charge boundary sector, interaction normalization and step angles
are supplied model choices, not measured data or consequences of the lattice
axioms. Their native-lattice implementation is an open bridge owned by GB1-CF.

All real step angles are covered by the joint construction, including zero.
The ordered-product statements are the stated Taylor coefficients, not a
classification of exceptional angles. External charges, dangling boundary
links, different finite representations, matter and more plaquettes require
their own sector and operator calculations.

The strongest missing next construction is a compatible, spatially covariant
extension on overlapping patches at fixed register size. This is materially
stronger than the finite-patch result and is not represented as a routine step.

## Evidence and review record

The primary runner constructs the five-state link matrices and loop states by
exact sparse action. A separate restricted-context checker independently derives
the physical sector and coefficients with Haar polynomial integration. The two
workers share a model family and the raw model specification; their arithmetic
routes and contexts are separate. This is a targeted mathematical check, not
an independent landing review or audit.

The [primary runner](../scripts/gb1_cf_two_plaquette_s1_2026_11_07.py) imports the
[Haar checker](../scripts/gb1_cf_two_plaquette_haar_check_2026_11_07.py) only for
an exact comparison added after both original derivations were frozen. The
checker never imports the primary. This static import brings the checker into
the primary's dependency packet, and its source is also an explicit cache
input. Neither runner reads an unmerged draft or mutable workflow document.

The [research handoff](../.claude/science/physics-loops/gb1-cf-pair-20261107/HANDOFF.md)
records the source identities, content-bound execution caches, mutation results,
and supervisor integration review. Frozen derivations, original execution logs,
and the [focused note check](../.claude/science/physics-loops/gb1-cf-pair-20261107/CHECKER_NOTE_REVIEW.md)
are preserved in the same pack. The focused check found no mathematical error
and requested explicit dual-doublet conventions, removal of an undefined
representation label, and an initialized-code qualification; all three are
incorporated here. No acceptance is inferred from a count of passing assertions.

The finite noncommutation and ordering examples are existence witnesses for
the displayed operators. They exclude no other update constructions. The
positive joint-gate construction is the result proposed for review; the open
global implementation questions are not impossibility claims. Independent
landing review and an audit remain required before effective retained status.

## Provenance and prior context

The finite quantum-link approach and SO(5) embedding are credited to
Chandrasekharan and Wiese,
[Quantum Link Models: A Discrete Approach to Gauge Theories](https://arxiv.org/abs/hep-lat/9609042).
Here the five-dimensional vector representation and the normalization of
\(P_\mu\) are specified explicitly. The two-square calculation is a
self-contained research probe, without a claim of literature priority.

The motivating open item is GB1-CF in PR #10139, assembly revision
fb9508e8390bf66da8f29ddb44611d2a531768cb, particularly `GB1QL.md` sections
1.1-1.3 and `GB1ISO_REFEREE.md` section 2.3. Those files are context and do not
enter the runner's scientific input closure. The current physical-premise
registry and `docs/MINIMAL_AXIOMS_2026-06-29.md` are unchanged.
