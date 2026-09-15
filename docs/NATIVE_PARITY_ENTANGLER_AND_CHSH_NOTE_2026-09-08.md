---
claim_id: native_parity_entangler_and_chsh_note_2026-09-08
claim_type: bounded_theorem
claim_scope: "On the supplied native three-edge tree, product basis preparation and signed hopping pulses followed by a middle Z Record implement the stated four-input heralded parity map. Essential output dual-rail regrouping leaves a Bell resource with success probability one half and native local hopping/Z settings attaining CHSH two square root two. Both Record outcomes are retained. A native nonbridge Record is instead a fair isometric dictionary change. All preparation, placement, controls, Born readout and setting schedules remain supplied."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/native_parity_entangler_2026_09_08.py
---

# Native parity heralding and a readable Bell resource

**Date:** 2026-09-08

**Type:** bounded_theorem

This conditional construction produces a readable entangled resource using the supplied native instrument and hopping controls. Its success map uses different input and output rail pairings; that regrouping is essential. The result does not derive a formation law or a general interacting compiler.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Explicit physical Kraus construction and surviving local correlation experiment, independently checked with exact complex matrices."
trace_class: frontier_discovery
artifact_role: theorem
next_trace_action: "Supply physical preparation, hopping control and occurrence/readout selection."
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Carrier and supplied resources

The [native matter-instrument theorem](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md), equations 1–4 and Theorem 1, supplies the edge/CAR code and Record deletion dictionary. Here the graph is the path \(0-1-2-3\), with three physical edge qubits at the supplied midpoint roles. The full tree carrier represents the even four-mode CAR algebra. Its native operators are

\[
B_v=\prod_{e\ni v}Z_e,\qquad
n_v=\frac{I-B_v}{2},\qquad
T_{ij}=\frac{i}{2}A_{ij}(B_i-B_j).
\]

There are no cycle constraints on this tree. No extra reservoir, controlled hopping or independent occupation-phase generator is introduced. The initial occupation vector \(1100\) is a single physical computational basis vector, hence a product preparation of the three edge qubits. That preparation is supplied, not selected by the axioms.

Ordinary tensor composition, physical edge placement, signed hopping pulse control, pulse ordering, and the Born/Lueders Record schedule remain separate supplied conditions. In particular, graph incidence at edge midpoints is not a proof of nearest-neighbor interaction on the fine physical lattice. No Gibbs-preparation note is a scientific dependency.

## Input and output encodings

Input logical qubit \(A\) uses rails \((0,2)\), and input qubit \(B\) uses rails \((1,3)\), with one fermion in each pair. Define \(V_{\rm in}|ab\rangle\) to be the actual physical occupation vector with rail \(a\) of \(A\) and rail \(b\) of \(B\) occupied. The physical computational basis fixes its phase.

The output qubits instead use rails \((0,1)\) and \((2,3)\). Let \(V_{\rm out}\) denote their one-particle-per-pair encoding, with the same occupation-vector phase convention. The construction is therefore a heralded map between declared encodings, not a deterministic gate on unchanged logical wires.

## Preparation with native hopping pulses

For a path edge \(j\), write

\[
U_j(c,s)=I+(c-1)T_j^2-isT_j,
\qquad c=\cos\theta,\quad s=\sin\theta.
\]

The complete transfer \(S=U_{12}(0,1)\) has angle \(\pi/2\). With \(c=s=1/\sqrt2\), define the two preparation rotations

\[
G_{02}=S\,U_{01}(c,c)\,S^\dagger,
\qquad
G_{13}=S^\dagger\,U_{23}(c,c)\,S.
\]

Each expression is a finite sequence of adjacent native hopping pulses before any cut. Inverse transfers use the supplied signed pulse control. These conjugations implement rotations on disjoint mode pairs; the resulting rotations commute and preserve each input rail-pair number. In the actual physical phase convention,

\[
G_{13}G_{02}|1100\rangle
=V_{\rm in}\frac{(1,1,1,1)^{\mathsf T}}{2}
=V_{\rm in}|+\rangle_A|+\rangle_B.
\]

Thus no independent nonlocal Hamiltonian generator or phase-preparation primitive is assumed.

## Complete internal Record instrument

The physical middle edge measures the parity of one side:

\[
Z_{12}=B_0B_1=(-1)^{n_0+n_1},
\qquad Q_- =\frac{I-Z_{12}}2,
\qquad Q_+ =\frac{I+Z_{12}}2.
\]

Supply the usual binary \(Z_{12}\) Record event. Both outcomes are permanent Records, and both remove the middle hopping edge. On the total-two-particle input domain, the odd branch has exactly one particle in each surviving component. Its full physical columns satisfy

\[
Q_-V_{\rm in}=V_{\rm out}K_-,
\qquad
K_-=\begin{pmatrix}
0&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&0
\end{pmatrix}.
\]

The failure output is explicit. In occupation-vector notation, set

\[
V_{\rm fail}=\bigl(|1100\rangle,|0011\rangle\bigr),
\qquad
K_+=\begin{pmatrix}1&0&0&0\\0&0&0&1\end{pmatrix}.
\]

Then

\[
Q_+V_{\rm in}=V_{\rm fail}K_+,
\qquad K_-^\dagger K_-+K_+^\dagger K_+=I_4.
\]

The even branch carries input labels \(00\) and \(11\), with two particles on one side and none on the other. It is retained as failure, not identified with two output qubits or recycled without further resources. These full-column identities hold for arbitrary input density matrices and passive references.

For the prepared input \(|++\rangle\), the success probability is \(1/2\), and the normalized output is

\[
|\Psi^+\rangle
=\frac{|01\rangle+|10\rangle}{\sqrt2}.
\]

The map does not select when the Record occurs, and a failure is not an unrecorded outcome.

## Readout after the permanent cut

The surviving operators \(T_{01}\) and \(T_{23}\) commute with the old middle Record. Each connected component has odd parity and a readable single-particle dual rail. The original crossed input rails would require hopping across the deleted edge; the output regrouping avoids that forbidden operation.

For the successful state, the surviving product correlation is

\[
\langle T_{01}T_{23}\rangle=-1,
\]

whereas occupation dephasing gives zero. This coherence can be tested with the same native controls and terminal \(Z\) Records. Let

\[
R=U_{23}(1/\sqrt2,1/\sqrt2)\,
  U_{01}(1/\sqrt2,1/\sqrt2).
\]

In the output encoding,

\[
V_{\rm out}^\dagger Z_{01}Z_{23}V_{\rm out}=-Z_AZ_B,
\qquad
V_{\rm out}^\dagger R^\dagger Z_{01}Z_{23}RV_{\rm out}=X_AX_B.
\]

Consequently the sum of the bare and rotated product expectations is

\[
W=\langle-Z_AZ_B+X_AX_B\rangle.
\]

Every separable output state has \(W\le1\), by the two-component Bloch-vector Cauchy–Schwarz bound and convexity. The heralded state gives \(W=2\). For an arbitrary density matrix on the declared output encoding, define
$\widehat W=-Z_AZ_B+X_AX_B$ and $F=\langle\Psi^+|\rho|\Psi^+\rangle$.
The commuting Pauli products have Bell-basis eigenvalues $2,0,0,-2$ for
$\widehat W$, with the eigenvalue $2$ on $|\Psi^+\rangle$. Thus
$\widehat W\leq2|\Psi^+\rangle\langle\Psi^+|$ and $F\geq W/2$.
This is the fidelity consequence of the same trusted measurement model.

This is a trusted-measurement entanglement witness. Each terminal readout consumes its outer edge, so different settings require fresh preparations.

## Native CHSH settings

Write \(U_{ij}(\theta)=\exp(-i\theta T_{ij})\) and define

\[
A(\theta)=U_{01}(\theta)^\dagger Z_{01}U_{01}(\theta),
\qquad
B(\phi)=U_{23}(\phi)^\dagger Z_{23}U_{23}(\phi).
\]

Choose the supplied settings

\[
\theta_0=0,\quad\theta_1=\frac\pi4,
\qquad
\phi_0=\frac\pi8,\quad\phi_1=-\frac\pi8.
\]

The actual physical correlation matrix and specified CHSH combination are

\[
(E_{ab})=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad E_{00}+E_{01}+E_{10}-E_{11}=2\sqrt2.
\]

Local means vanish. Cross-component setting operators commute and preserve the middle Record. The successful herald precedes the independently supplied setting choices, so no filtering conditional on settings is needed. Setting independence, spatial arrangement, Born probabilities and scheduling remain hypotheses; this is not a loophole-free experimental claim. It establishes usable correlations after the cut, not a restored physical connection, a universal gate or a state-transfer protocol.

## Why a nonbridge Record is different

Consider the supplied native constrained code after arbitrary fixed old Records. Let \(e\) be an unrecorded nonbridge edge and \(P\) its input code projector. A remaining cycle through \(e\) has a stabilizer \(S\) with \(SP=P\) and \(SZ_eS=-Z_e\). Therefore

\[
PZ_eP=0,\qquad
PQ_zP=\frac P2,
\qquad Q_z=\frac{I+zZ_e}{2}.
\]

For \(K_z=Q_zP\), each outcome has \(K_z^\dagger K_z=P/2\). Its image lies in the output code with the new fixed \(Z_e=z\) and the remaining cycle checks. Deleting a nonbridge edge leaves the connected-component partition unchanged, so the parent dimension formula gives equal input and output dimensions. Thus

\[
J_z=\sqrt2\,Q_zP
\]

is an isometry onto the output code. Every surviving \(A_f\), \(f\ne e\), contains at most a \(Z_e\) factor, and every \(B_v\) commutes with \(Q_z\). Hence \(J_z\) intertwines the surviving represented CAR algebra, retaining the known Record signs and reference coherence. It is not an identity under an arbitrary physical tensor-factor identification.

Adding a bypass to the middle bridge changes its single-\(Z\) measurement into a fair, information-free flag on this native code. One cannot retain the original parity entangler merely by adding that path. This boundary concerns the specified measurement and encoding, not every gate or multi-event protocol.

## Evidence and review

The [live primary runner](../scripts/native_parity_entangler_2026_09_08.py) executes the [numeric physical helper](../scripts/native_parity_entangler_numeric_2026_09_08.py) and the [independent exact helper](../scripts/native_parity_entangler_exact_2026_09_08.py). Both retain full complex success and failure columns. The exact helper independently derives

\[
T_{01}=Y_0\frac{I-Z_1}{2},\qquad
T_{12}=Y_1\frac{I-Z_0Z_2}{2},\qquad
T_{23}=Y_2\frac{I-Z_1}{2},
\]

and constructs occupation vectors by prefix parity. This checks the phases that concurrence or real-part output alone would not establish. The nonbridge result is analytic, using the parent code theorem; it is not inferred from the tree fixture.

Paired outputs are [numeric](../outputs/native_parity_entangler_numeric_2026_09_08.json), [exact](../outputs/native_parity_entangler_exact_2026_09_08.json) and [primary](../outputs/native_parity_entangler_2026_09_08.json). The [execution cache](../logs/runner-cache/native_parity_entangler_2026_09_08.txt) records actual execution. Original review and port provenance are summarized in the
[historical review record](work_history/repo/review_feedback/NATIVE_PARITY_ENTANGLER_HISTORY_2026-09-08.md).
The three outputs record the current live execution; the historical source's
review label does not certify the present integration. Formal audit status
remains pending and is not granted by these checks.

## No-Go Discipline Gate

This section checks the narrow nonbridge/bypass boundary; it asserts no universal
no-go and no formal audit verdict.

- **N1 — Routes and scope.** Keeping the bridge gives the explicit parity
  entangler above. Adding a bypass while keeping this single physical Z event
  yields the proved information-free isometry. Keeping crossed output rails
  would require the deleted middle hopping. Regrouping into surviving components
  gives the affirmative readout construction. Changing the measurement or using
  multiple events is untested and outside this boundary. These distinctions
  delimit the claim; their count is not proof of exhaustive protocol coverage.
- **N2 — Independent conditions.** The cycle stabilizer and anticommutation
  establish the fair outcome; unchanged component partition and the parent
  dimension formula establish surjectivity. These are explicit hypotheses,
  not independent universal obstructions to every control protocol.
- **N3 — Supplied inputs.** Preparation, signed hopping, the native constrained
  code, Born events and settings remain supplied. No registered primitive is
  declared absent or converted into a wall.
- **N4 — Residual.** The residual is exactly $K_z^\dagger K_z=P/2$ and the
  surviving-algebra intertwiner. No missing physical number is fitted.
- **N5 — Resolution.** The live finite helpers execute full complex success
  and failure columns, the prepared Bell vector, and all four CHSH correlations
  on three physical qubits. The nonbridge statement is analytic; spatial
  scaling, arbitrary multi-event protocols and occurrence dynamics are not
  numerically executed or certified by that fixture.
- **N6 — Partial closure.** The bridge and regrouped-output construction is
  an affirmative route already established here. Different measurement or
  control protocols remain open; no new axiom is claimed necessary.
- **N7 — Counter-route.** The strongest apparent counter-route adds a bypass
  to retain connectivity. It changes the stabilizer action on this same Z
  measurement and hence its information content; the displayed algebra resolves
  only that route. It does not exclude a redesigned instrument.
- **N8 — Historical scope.** The original packet's scoped-boundary ledger at
  head `9ae85474d22ed4a987508293b60bed48f9108a43` said no formal no-go was
  submitted. This canonical account retains that limit; prior review labels
  are historical evidence, not repeated or current certification.

## Prior art and remaining physical obligations

Parity-assisted fermionic processing is established prior art: Beenakker, DiVincenzo, Emary and Kindermann, [Charge detection enables free-electron quantum computation](https://arxiv.org/abs/quant-ph/0401066), Physical Review Letters 93, 020501 (2004), [DOI](https://doi.org/10.1103/PhysRevLett.93.020501). The abstract was checked for attribution. No hardware-detail theorem or deterministic CNOT from that paper is a proof input here. The narrow result is the explicit native permanent-cut instrument, essential regrouping and surviving native hopping/\(Z\) correlation experiment.

The physical preparation, signed partial hopping pulses, Record occurrence, readout and setting schedule remain supplied. The construction has no claim to universal interactions, a gauge/matter identification, an autonomous clock or an axiom-selected coupling. It is affirmative conditional frontier discovery, not closure of an existing parent blocker.
