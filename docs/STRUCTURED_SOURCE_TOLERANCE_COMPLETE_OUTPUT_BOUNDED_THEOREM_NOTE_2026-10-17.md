# Structured source tolerance for complete autonomous output

This note combines a selectively checked source-only tolerance certificate with an exact positive-block re-expression. Under the supplied physical identification, calibration, preparation and remaining-device premises below, the finite device has complete operator-norm output error **less than 0.000660 throughout [2×10¹⁴,4×10¹⁴]**. The six-block compensated family uses one fixed nominal target. A seven-block implementation removes the hopping-dependent occupation adjustments and has the same bound with the explicit actual-tuple global phase retained.

The component and tolerance-composition checks are complete. This publication synthesis is prepared for a separate integration review; it is not a retained-status audit or experimental validation. Canonical location: `docs/STRUCTURED_SOURCE_TOLERANCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`. Proof links below use the portable packet `outputs/source_tolerance_2026_10_17/proofs/`.

## Conditional construction and theorem

Keep the calibrated original hopping j, with .0027<j<.003, and set

\[
 \lambda=10^{-13},\quad g=5\cdot10^{-8},\quad h=4\cdot10^{-6},
 \quad T=2\cdot10^{14},\quad M=50,000,000.
\]

The receiver has M retained slow-lead sites and the exact compression cap. The unchanged device is that of the [three-site temporal parent](THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), using the source installation of the [spectral parent](CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md). These dependencies retain the original real endpoint calibration, physical graph, converters, record gate, shared internal operator, positive local interactions and preparation premises; their labels are not substitutes for those hypotheses.

The source sites are s₀=(40,66,1), s₁=(40,65,1), s₂=(40,64,1), followed by the old port p=(40,63,1). For every real tuple in the box

\[
 a_1^2={\lambda^2\over3}(1+e_1),\quad
 a_2^2={8\lambda^2\over3}(1+e_2),\quad
 \kappa^2=3j\lambda(1+e_3),\qquad
 |e_i|\le10^{-6},\quad |d_i|\le10^{-19},
\]

choose positive amplitudes and negative exchange hoppings. The dᵢ are scalar identity detunings on the entire internal fiber. They are not old-energy-, parity- or record-dependent. All non-source coefficients, graph contacts and source-vacuum preparation remain exactly as supplied. Prepare the head at s₀, every other head blank, the original internal source vacuum and computational record 0. The input consists of an arbitrary old state, optionally entangled with an arbitrary passive reference. Let V denote this seed isometry.

Shared B is included once and obeys Bι=ιK on the prepared vacuum embedding, where

\[
 K=2I+Z_1Z_2,\qquad
 W={(9+12i)I+(-16+12i)X_1X_2\over25}.
\]

No commutation of the full Hamiltonian with K is assumed. Old aging remains e⁻ⁱᵗᴷ, and W is literal, including its phase.

Define the target from the exact **nominal** three-site transmitted hard-band coefficient at these λ,j,g,h. It retains the complex cubic finite-band denominator, flux/Jacobian, the phase 61.5q+.5k+172k_old(q), and the single calibrated phase ζ. Let β₀(t) be its raw physical output packet on m≥0, with physical time factor exp[−it(2j−2g cos k)], and r₀(t)=‖β₀(t)‖. The checked bounds below ensure r₀(t)>0 on [T,2T]. With the original vacancy scalar c_att and output embedding J_out, define

\[
 \mathcal T_0(t)=e^{-itc_{\rm att}}
 J_{\rm out}\!\left[{\beta_0(t)\over r_0(t)}
                  \otimes e^{-itK}W\right].                 \tag{1}
\]

This is an isometry into the complete comparison space: record 1, source vacuum, blank non-output heads and the physical output packet. It is not the normalized actual successful branch. Finite actual states are embedded into the same infinite comparison space, without projecting or renormalizing the target tail.

For the compensated six-block Hamiltonian H_old,M defined below, every allowed tuple satisfies

\[
 \sup_{T\le t\le2T}
 \|\operatorname{embed}e^{-itH_{\rm old,M}}V-\mathcal T_0(t)\|
 <0.000660.                                                \tag{2}
\]

The same nominal target is used across this entire family. For the seven-block implementation H_new,M, set C_src=κ+a₁+a₂ using the **actual** tuple. Then

\[
 \sup_{T\le t\le2T}
 \|\operatorname{embed}e^{-itH_{\rm new,M}}V
                   -e^{-itC_{\rm src}}\mathcal T_0(t)\|
 <0.000660.                                                \tag{3}
\]

These are complete vector-map/operator-norm bounds with arbitrary passive references. They cover all output coordinates, including undesired records and residual source/core states. They are not merely bounds conditioned on a herald.

The [full tolerance derivation](../outputs/source_tolerance_2026_10_17/proofs/three_site_source_tolerance_complete__PROPOSAL.md) and its [distinct check](../outputs/source_tolerance_2026_10_17/proofs/three_site_source_tolerance_complete_check__REVIEW.md) establish (2). The [positive-block identity](../outputs/source_tolerance_2026_10_17/proofs/three_site_positive_hopping_reexpression__PROPOSAL.md) and its [distinct check](../outputs/source_tolerance_2026_10_17/proofs/three_site_positive_hopping_reexpression_check__REVIEW.md) transfer it to (3). Their complete arguments and pinned dependencies, rather than summary verdicts alone, are imported.

## Two positive implementations and the retained phase

Write nᵢ for head occupation and X_uv=|10⟩⟨01|+|01⟩⟨10|. The old six source blocks are

\[
\begin{split}
 &j(n_2+n_p)-\kappa X_{2p},\\
 &a_2(n_1+n_2-X_{12}),\quad a_1(n_0+n_1-X_{01}),\\
 &(j+d_2-a_2)n_2,\quad(2j+d_1-a_1-a_2)n_1,
       \quad(2j+d_0-a_1)n_0.
\end{split}                                               \tag{4}
\]

All are positive on the stated box. Their full-space sum is

\[
 H_{\rm src,old}=j n_p+\sum_{i=0}^2(2j+d_i)n_i
                 -\kappa X_{2p}-a_2X_{12}-a_1X_{01}.       \tag{5}
\]

The occupations in (4) must track the changed amplitudes. Source compression retains jn_p, so the background is unchanged. These occupation terms vanish on blank source heads and introduce no new vacancy scalar.

For a>0, instead use P_a(u,v)=a(I_uv−X_uv). Its pair spectrum is {0,2a,a,a}: it is positive, has norm 2a, preserves head number and has vacuum energy a. The pair identity extends to the global identity. The seven source blocks are

\[
 P_\kappa(s_2,p),\ P_{a_2}(s_1,s_2),\ P_{a_1}(s_0,s_1),
 \quad jn_p,\ (2j+d_2)n_2,\ (2j+d_1)n_1,\ (2j+d_0)n_0.
                                                               \tag{6}
\]

On the FULL Hilbert space, including zero and multiple heads,

\[
 H_{\rm new}=H_{\rm old}+C_{\rm src}I,
 \qquad e^{-itH_{\rm new}}=e^{-itC_{\rm src}}e^{-itH_{\rm old}}.
                                                               \tag{7}
\]

The unchanged background is added once on both sides. Equation (7) requires no internal commutation and proves (3) directly. In (6), hopping amplitudes can vary without subtractive changes to the occupation coefficients. After centering by the actual C_src, each tuple is exactly the old compensated comparison family. Compression leaves jn_p+C_src I; moments and physical spectral windows shift by that same scalar. Finite and infinite receivers receive the same scalar, so their difference norms and the cut bound are unchanged.

This removes a specific hopping/occupation correlation requirement. It does not remove the occupation precision |dᵢ|≤10⁻¹⁹, the source relative squared-bond box, fixed downstream calibration or the supplied realization of P_a. For uncertain coefficients, (3) is an actual-scalar target family. One cannot omit exp(−itC_src(actual)) and claim the same phase-sensitive bound to a single nominal global-phase target. Global phase cancels in channel predictions, but remains part of the stated vector metric. A common potential applied only to the three source sites is a different modification; no common-mode detuning result is imported here.

## Complete error accounting

The proof keeps both Stone boundary values, both physical old-energy windows and all eight internal forcing directions. The real conjugation of the incoming coefficient produces W* with the physical exp(−itE) time factor; it does not conjugate arbitrary input/reference states. The two traveling errors are added, not assumed orthogonal.

The full ordered inverse margin for this perturbation box is Θ<7×10⁻⁶ and c>.9999729. The scalar complex packet ratio allowance is L<.000021501, including normalization and the absence of uncharged scalar bound mass in the reference model. This scalar fact is not promoted to a claim that the loaded apparatus has no outside spectrum.

For the actual device, the installed sixth central moment is bounded by μ₆<8.000026×10⁻⁶⁸, with d=2j sin h>2.15×10⁻⁸. Hence one common-union outside amplitude, including all spectral types, is at most √(2μ₆)/d³<4.1×10⁻¹¹. It is charged once globally. The represented source comparison separately pays the scalar reference truncation. Neither step assumes [H,K]=0.

The checked complete budget on [T,2T] is:

| Contribution | Strict ceiling |
|---|---:|
| One actual outside state | 4.1×10⁻¹¹ |
| All three represented source heads | .000082 |
| Every other finite coordinate and closed tail | .000505 |
| Actual outgoing and incoming coefficient discrepancies, 2E_raw | .0000285 |
| Both perturbed ideal packets replaced by the fixed nominal packets, 2L√p₀ | .00004301 |
| Nominal physical incoming packet | 3.1×10⁻⁷ |
| Single physical-halfline target normalization, 1−r₀(t) | 3×10⁻¹² |

The sum is .000658820044<.000659. Full background recovery L₀=14000 is applicable because (5) preserves the background compression; its absolute integral includes all closed tails. The joint source comparison includes both selected and wrong-window columns. The common scalar ideal-packet replacement does not incur an extra old-energy multiplicity or normalize the actual output.

The exact nominal weighted reference uses proof cutoff D=g/4, its finite-band moments and the retained physical phase. It gives E_w<3.1×10⁻⁷, cubic excluded-tail bound H(20)<8×10⁻⁷ and outgoing excluded norm <1.2×10⁻⁶. Together with 1−p₀<1.34×10⁻¹² these justify the incoming and single normalization rows. This step uses a truncated sixth moment for dispersion, not a divergent untruncated moment. No fitted packet, cutoff-smallness assumption or temporal simulation is used.

Finally the exact cap retains the compression diagonal at the last slow site. Weight zero on the entire finite core and the first output site, and weight n on output site n, makes only slow bonds contribute to the weighted imaginary part. The single-cut Duhamel bound, uniform for 0≤t≤2T, is

\[
 \|U_\infty(t)V-\operatorname{embed}U_M(t)V\|
 <1.2e^{-M+4gT\sinh1}
 <1.2e^{-2,960,000}<10^{-10}.                             \tag{8}
\]

Here 4gT=40,000,000 and sinh1<1.176. The bound includes returns and reflections. All source variations lie in the zero-weight region; (7) multiplies both unitaries by the same phase. Equations (2)–(3) follow with the advertised .000660 ceiling.

## Resources and remaining physical obligations

The source replacement changes neither geometry, preparation, head edges nor receiver length. Counts refer to explicit unmerged positive decompositions, not minima.

| Inventory | Six-block family | Seven-block implementation |
|---|---:|---:|
| Head sites | M+238 | M+238 |
| Physical qubits | M+243 = 50,000,243 | M+243 = 50,000,243 |
| Head edges | M+239 | M+239 |
| Positive blocks | 2M+281 = 100,000,281 | 2M+282 = 100,000,282 |

For (6), the source contributions to incident block-norm sums are 2j+d₀+2a₁ at s₀; 2j+d₁+2a₁+2a₂ at s₁; 2j+d₂+2a₂+2κ at s₂; and j+2κ at p. Unchanged background incidence at p must still be added. Old source load numbers cannot simply be reused for this decomposition, and the global identity contribution is not dropped from declared local block norms.

The result tolerates the stated real source coefficients, not arbitrary downstream or preparation errors, added edges, complex hopping phases or nonidentity detunings. Bond errors refer to squares; amplitude tolerances follow by square roots. The absolute diagonal tolerance and the original calibration remain supplied precision. Neither positive decomposition derives native interaction blocks, coefficient suppliers or a new physical axiom.

The interval and metric are those explicitly stated. There is no early-read guarantee, guarantee after 2T, permanent halt, irreversible capture, repeated monitoring/reset result or physical-seconds interpretation. The milestone establishes a structured tolerance envelope at an existing receiver, not a new speed/size optimum or measured hardware performance.

## Source identity and review exposure

The four direct sources are pinned as follows; the tolerance proof and review also enumerate their 28 exact component dependencies. Those full arguments remain part of the proof closure.

| Packet file | SHA-256 |
|---|---|
| `three_site_source_tolerance_complete__PROPOSAL.md` | `a11bd665e2db4f7bc2fb68b743a3d3ca6a9cb54cd6c0df8fed75f58d98d2bb26` |
| `three_site_source_tolerance_complete_check__REVIEW.md` | `8f6776b53df533185061592587addda6d528303e72cace15b533b20f76014fb6` |
| `three_site_positive_hopping_reexpression__PROPOSAL.md` | `9fa50cd2da480d59765aa5fbd7c556728a08ac4c385234dc055c26220b93a5d4` |
| `three_site_positive_hopping_reexpression_check__REVIEW.md` | `1e9630995e29cea591048983768658b0421b6b5658d3ac7bbbe0fa6dd034b956` |

This drafter authored the tolerance composition, scalar robustness and local/core extension and several nominal ancestors. Root authored the positive hopping identity. The distinct checker of these two direct results had authored the perturbed attachment and several traveling/reference ancestors; those ancestors have their own recorded selective checks. Thus the evidence is source-exposed analytical checking with explicit ancestry, not blind, model-diverse or independent recertification of every ancestral statement. The complete new positive identity and review and the tolerance review were read for this synthesis. This note introduces no new numerical certificate or common-mode result.

The component evidence is analytical. No new dynamics simulation, parameter sweep, numerical solver, formal proof or retained-status audit is claimed. Publication integration review is recorded separately in the accompanying packet. No editable prompt files or physical axioms were changed.
