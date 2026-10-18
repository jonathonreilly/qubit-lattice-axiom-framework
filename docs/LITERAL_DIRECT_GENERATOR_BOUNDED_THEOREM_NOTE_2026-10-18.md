# A direct-generator benchmark for the literal old-system operation

Claim status: **bounded_theorem**, conditional on the explicitly supplied blocks and input. The exact source has a distinct analytical SUPPORT review, accepted by ROOT at this changed-apparatus scope. This is an author synthesis, not an additional independent check or retained audit.

The literal old target admits a small exact selected-time implementation if a direct target-generator block is supplied on its existing nearest-neighbor old pair. Keeping the original old/source internal Hamiltonian, one additional positive real two-body block implements the required old operation with its entire elapsed aging. An optional independent two-site head gives an exact output endpoint at that same calibrated time. The resulting benchmark has six qubits and nine positive blocks, with complete-vector error at most \(\epsilon/8\) on an explicit positive-width window.

This changes the actuator inventory. The direct generator and static synchronization ratio are supplied; the original clock/source contacts and scattering graph are removed. The [real endpoint transmission construction](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md) remains a distinct conditional result under its own premises. This benchmark neither validates nor invalidates that apparatus, and does not establish a physical speedup under equal suppliers. Its purpose is to expose which resource cost comes from restricting the available interactions. It does not derive native coefficients, capture, reset or permanent halt.

## 1. Literal old system and positive device

Use the actual physical old sites \(1=(0,0,0)\), \(2=(1,0,0)\), retaining the original block
\[
 K=2I+Z_1Z_2,\qquad X=X_1X_2,\qquad
 W=\frac{(9+12i)I+(-16+12i)X}{25}.                 \tag{1}
\]
Thus K has eigenvalues1 and3, each twice, and full-support norm3. It is not replaced by a scalar onsite \(\omega n_P\). Let \(\theta\in(0,\pi/2)\) satisfy
\[
 \cos\theta=3/5,\quad\sin\theta=4/5,\qquad
 W=e^{i\theta}e^{i\theta X}.                        \tag{2}
\]
In particular \(\pi/4<\theta<\pi/2\) and \([K,X]=0\).

Keep the shared source sites \(A=(0,1,0)\), \(B=(1,1,0)\). With \(n=(I-Z)/2\), \(a=|0\rangle\langle1|\), retain
\[
\begin{aligned}
 C_{\rm src}&=\Delta_A n_A+\Delta_B n_B
 +h(n_A+n_B-a_A^\dagger a_B-a_B^\dagger a_A)+u n_A n_B,\\
 G_{\rm src}&=g_A n_A(I+X_1)+g_B n_B(I+X_2),\\
 B_{\rm int}&=K+C_{\rm src}+G_{\rm src},\qquad
 \iota\xi=\xi\otimes|00\rangle_{AB}.
\end{aligned}                                                     \tag{3}
\]
The exact retained coefficients are

| Coefficient | Exact value |
|---|---:|
| \(g_A\) | 0.996878563816670 |
| \(g_B\) | 0.599319315560298 |
| \(h\) | 3.999349697888060 |
| \(u\) | 0.544607276405587 |
| \(\Delta_A\) | 2.192035527016003 |
| \(\Delta_B\) | 2.186826508897014 |

These terminating decimals define exact supplied numbers. The seven retained positive blocks are K, the two \(\Delta\) occupations, the h source Laplacian, \(u n_A n_B\), and the two source/old contacts. Their ready-space identity and full-space symmetry are
\[
 B_{\rm int}\iota=\iota K,\qquad [B_{\rm int},X]=0. \tag{4}
\]
The first follows because every source term annihilates \(|00\rangle_{AB}\). For the second, X commutes with \(Z_1Z_2\), each source-only term and \(X_1,X_2\) individually. No assertion \([B_{\rm int},K]=0\) on excited sources is needed.

For \(g>0\), add the new directly supplied old-pair block
\[
 h_g=g(I-X_1X_2),\qquad H_{\rm int}=B_{\rm int}+h_g. \tag{5}
\]
It is positive on full support, real, nearest-neighbor and two-body, with eigenvalues0 and2g, each twice. Its norm is2g. It does not annihilate the old vacuum, and no vacuum-support or head-number lemma is invoked for it. K remains installed and counted once.

The original clock contacts, filter, emitter and long graph are absent in this new device. Adding (5) to those still-active contacts would be a different model requiring another proof. Equation(4) is preserved here precisely because the retained source-ready subspace is invariant.

## 2. Exact old operation and its complete phase

From (4)–(5), on the entire arbitrary-old ready space,
\[
 e^{-itH_{\rm int}}\iota
   =\iota e^{-itK}e^{-igt}e^{igtX}.                 \tag{6}
\]
Every identity holds after tensoring any passive reference \(F\); the old input may be coherently superposed and entangled with F. The sources remain exactly \(|00\rangle\) for all t on this input. Their outputs are retained, not projected away.

Choose
\[
 \tau=\theta/g.
\]
Then the exact selected-time operation is
\[
 e^{-i\tau H_{\rm int}}\iota
      =e^{-2i\theta}\iota e^{-i\tau K}W.           \tag{7}
\]
No old-energy revival is required. The physical elapsed time in the aging factor is \(\tau\), including all time since delivery.

For neighboring t use the specified common phase
\(\phi_{\rm int}(t)=e^{-igt-i\theta}\). Directly from the two eigenvalues of X,
\[
\begin{aligned}
 \|e^{-itH_{\rm int}}\iota
       -\phi_{\rm int}(t)\iota e^{-itK}W\|
 &=\|e^{igtX}-e^{i\theta X}\|\\
 &=2|\sin(g(t-\tau)/2)|\le g|t-\tau|.
\end{aligned}                                                     \tag{8}
\]
The fixed \(e^{-i\theta}\) is a known common output phase; it is not fitted separately to old inputs or energy sectors. The old target is \(e^{-itK}W\), not \(e^{-i\tau K}W\). The four-qubit/eight-block version already has exact center operation and the source vacuum as its common apparatus output, but has no spatial output marker.

## 3. Optional endpoint marker and finite-window theorem

Add two head qubits \(u=(0,0,1)\), \(v=(1,0,1)\), with the disjoint positive block
\[
 H_{\rm head}=J(n_u+n_v-a_u^\dagger a_v-a_v^\dagger a_u),
 \qquad J=\frac{\pi g}{2\theta}.                   \tag{9}
\]
Its full-support norm is2J. No other head/old/source interaction is installed, including on unused geometrically adjacent pairs. The complete Hamiltonian and ready isometry are
\[
 H_{\rm tot}=H_{\rm head}\otimes I+I\otimes H_{\rm int},
 \qquad E_{\rm in}\xi=|10\rangle_{uv}\otimes\iota\xi. \tag{10}
\]
The apparatus ready state is a delivered basis product. No coherent energetic reference array, entangled ancilla or incoming packet is supplied. The old input remains arbitrary and is not counted as apparatus preparation.

In the one-head sector the exact head solution is
\[
 e^{-itH_{\rm head}}|10\rangle
 =e^{-iJt}\bigl[\cos(Jt)|10\rangle+i\sin(Jt)|01\rangle\bigr].
\tag{11}
\]
At \(\tau=\theta/g\), \(J\tau=\pi/2\). Define the normalized complete target
\[
 \mathcal V_t\xi=
 i e^{-i((J+g)t+\theta)}|01\rangle_{uv}
                    \otimes\iota e^{-itK}W\xi.     \tag{12}
\]
It includes all six physical qubits and every passive reference. The input head site u and both sources are vacant, v contains the output head, and the old pair remains at its literal physical sites. At t=\(\tau\), actual and target vectors agree exactly, including the one common phase.

The head difference from its target factor satisfies
\[
 \|e^{-itH_{\rm head}}|10\rangle
                  -i e^{-iJt}|01\rangle\|^2
 =2-2\sin(Jt)=4\sin^2(J(t-\tau)/2).
\tag{13}
\]
Combining (8) and (13) by the triangle inequality for normalized tensor factors gives
\[
 \|e^{-itH_{\rm tot}}E_{\rm in}-\mathcal V_t\|
                  \le(g+J)|t-\tau|.                \tag{14}
\]
This is a complete induced operator bound with arbitrary passive extensions, not a marginal or conditional-state estimate.

For \(0<\epsilon\le1\), choose
\[
 w=\frac{\epsilon}{8(g+J)},\qquad
 I_{\rm obs}=[\tau-w,\tau+w].                       \tag{15}
\]
Here \(w/\tau=\epsilon/[8(\theta+\pi/2)]<1\), so the interval is positive, and \(Jw<1/8\). Throughout this interval,
\[
 \|e^{-itH_{\rm tot}}E_{\rm in}-\mathcal V_t\|
 \le\epsilon/8,\qquad
 d_{\rm complete,unhalved}\le\epsilon/4.            \tag{16}
\]
The channel bound follows from the normalized-isometry inequality, including mixed logical/passive states by purification. The actual head-at-v probability is exactly \(\sin^2(Jt)\), hence
\[
 \Pr(n_v=1)\ge1-(Jw)^2\ge1-(\epsilon/8)^2.          \tag{17}
\]
No actual output is discarded to state (16).

The endpoint is not an all-time completion flag. It has nonzero population before the desired old rotation is complete, and at \(t=2\tau\) the head returns to u while the old generator continues acting. There is no record R, capture, reset or permanent halt in this apparatus. Exact synchronization means the static ratio \(J/g=\pi/(2\theta)\) is supplied; it is not a demonstrated head-triggered gate. The selected observation window is not an autonomous output-release mechanism.

## 4. Geometry, incident cap and concrete resource choice

There are seven blocks in (3), one direct old-pair block in (5), and one head block in (9): **six qubits and nine positive blocks**. Omitting the optional head gives four qubits and eight blocks. All installed non-onsite interactions lie on ordinary cubic nearest-neighbor pairs. The old, source and head pairs are parallel; source contacts connect A to1 and B to2. Unlisted adjacent pairs do not install couplings.

Full-support load sums are
\[
\begin{array}{c|c}
 1&3+2g_A+2g\\
 2&3+2g_B+2g\\
 A&\Delta_A+2h+u+2g_A\\
 B&\Delta_B+2h+u+2g_B\\
 u,v&2J.
\end{array}                                                       \tag{18}
\]
The source Laplacian has norm2h, the occupation product norm1, and each source/old matrix \(n_A(I+X_1)\) or \(n_B(I+X_2)\) norm2. These loads are not computed only on the ready subspace.

A concrete choice is
\[
 g=10^{-3},\qquad J=\frac{\pi}{2000\theta},\qquad
 \tau=1000\theta.                                  \tag{19}
\]
It preserves the prior added-old-site ceiling2:
\(g_A+g=.997878563816670<1\) and
\(g_B+g=.600319315560298<1\). K's existing norm3 is additional. Exact substitution yields
\[
 \operatorname{load}(A)=12.729099326831050,\qquad
 \operatorname{load}(B)=11.928771812199317.
\]
Since \(g<J<2g\), \(2J<.004\). Thus a uniform incident cap \(\Lambda=13\) suffices with strict margin. No cap2 on every site is asserted. Reducing g cannot remove the retained source loads. Uniformly rescaling K to fit another cap would change the literal old-system contract.

At (19), \(250\pi<\tau<500\pi\) in the supplied model units. The qubit/block count and center time are independent of \(\epsilon\); the certified absolute and relative window widths are proportional to \(\epsilon\). Exact center operation does not give an error-independent positive-width interval. This is a short constant-size conditional benchmark with supplied exact coefficients, not a measured timescale, an optimized lower bound or a manufacturing-precision theorem.

## 5. Scientific meaning of the changed supplier

The exact gate is available because this particular W is generated by \(X_1X_2\), which commutes with the literal K and with the full retained internal B. The new actuator (5) is that target generator shifted positively by an identity. It is not obtained from the original clock contacts, not derived from a framework primitive, and not a theorem for arbitrary targets or arbitrary old Hamiltonians.

| Aspect | Original endpoint transmission apparatus | Direct-generator benchmark |
|---|---|---|
| Literal old K and ordered old target | Retained | Retained |
| Gate mechanism | Supplied source contacts, filter and head scattering | Newly supplied \(g(I-X_1X_2)\) on old pair |
| Runtime controls after delivery | None under its stated premises | None |
| Apparatus output | Specified common outgoing profile with all source/head residues bounded | Exact source vacuum and independent finite endpoint marker near selected time |
| Time domain | Its separately established infinite/finite domains | Selected shrinking finite window (15) |
| Native interaction/state supply | Open | Open, including the newly supplied target generator |

This comparison does not hold the actuator inventory or observation contract fixed. It therefore does not prove a physical speedup over the old construction under equal suppliers. The old source route remains valid under its stated conditional premises; this separate alternative does not supersede or recertify its proof. If a task restricts admissible additions to that original displayed inventory or its two clock ports, the direct block is outside that narrower task.

The apparatus cannot be appended to another continuously acting device and treated as a timed gate without an attachment proof. There is no autonomous capture/release, no reusable source/clock reset and no native identification of the elapsed time, coefficients or observed endpoint. All positive matrix forms, selected zero couplings, basis-product delivery and static coefficient ratio remain declared suppliers. The bare old-target algebra is exact; the physical interpretation remains conditional.

## 6. Evidence closure and scoped disposition

Exact installed source identities and publication provenance are recorded in the [source manifest](../outputs/literal_direct_generator_2026_10_18/SOURCES.json).

The primary new source is [direct-generator proposal](../outputs/literal_direct_generator_2026_10_18/source_checks/literal_direct_generator/PROPOSAL.md), 15405 bytes, SHA256 `c0cc65e615bb6bdb7466c01c68ce53d6647c75e73a322bd88fff97580428f7d6`. The [distinct review](../outputs/literal_direct_generator_2026_10_18/source_checks/literal_direct_generator_check/REVIEW.md), 22934 bytes, SHA256 `e58d3fd82b27d94ae862a528707e3eb279ad5964dd5ca4641fb0e7e4fbfe3e38`, was read completely before this disposition update. It supports the literal target, phase, complete-output bounds, full-support positivity, geometry and loads with no required mathematical correction. ROOT accepted that scoped result. The review also checks the contract memo, but its separate negative and encoding diagnostics are not dependencies of the present positive theorem. Historical pending labels in the frozen author source remain historical.

The original K/W and exact source coefficients are reproduced explicitly above, so no spectral/packet theorem is imported as a proof premise. The original frozen route identity is `fa51af25903bd07f2ec7a3ab6f4afb78122011a4197b81d514f653d12ce288e9` at renewal_20261016_230727/real_transmission_autonomous_route/ROUTE.md. Its actual original source/ready-space identity was completely recovered before this proposal. The linked canonical endpoint note was read narrowly at lines1–190 for its current conditional-scope statement and literal internal-model table, SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`; its appended refinements are not new proof dependencies or claimed reread here. An initial oversized read was truncated, so only the bounded explicitly reread portion is claimed as complete coverage.

The campaign request `REQUEST.txt`, SHA256 `f436b1f1ddef230339a6c855f70924635e0a0fc050f0549b3cea75e61d242fe4`, does not explicitly ban all alternative positive old-pair blocks. That absence is not evidence of native availability; (5) is an explicit added supplier. The contract-recovery memo `6c3d06b432006d1e2a7cffab73f873751dd243712fad39808c560e515aa91f74` is provenance context only. Its separate parity encoding and diagnostic counterexample, and the unrelated preparation-use probe, are not theorem dependencies of this benchmark.

ROOT suggested this direct-generator alternative and its supplier tradeoff. This drafter authored the proposal and reconstructed its ready-space identity, phase, head transfer, finite-window norm and loads; synthesis is not another independent check. The distinct reviewer did not author the two checked source bodies, but did author or review substantial earlier campaign work. The reviewer reconstructed the finite-dimensional identities and bounds with shared campaign exposure and the same model; this is neither blind nor lineage-independent or model-diverse validation. Shared model and campaign exposure are explicit, and no retained audit or physical validation is claimed.

Only this research-directory manuscript and its byte-exact pending snapshot/disposition diff were written for the synthesis. The initial pending manuscript is preserved as `NOTE_initial_081766.md`, SHA256 `08176611a9716c5c89291ed82b1537d6ddeabbe871755acec4e3707e97948915`; the update changes disposition and provenance only, leaving the science unchanged. Work used source reading, analytical presentation and deterministic hashes. No scientific executable, simulation, external search, delegation, Git/canonical/checkpoint/axiom/editable-prompt/model change or publication occurred. The source remains frozen; ROOT owns integration and publication. No editable prompt changed.
