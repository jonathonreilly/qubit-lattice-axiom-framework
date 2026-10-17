# Common source offsets with complete autonomous output

Under the supplied physical identification, original calibration, preparation and unchanged-background premises, the three-site product-source device admits a **complete finite-device operator-norm error below .000986 throughout [2×10¹⁴,4×10¹⁴]**, uniformly for the structured family below. A supplied common source offset may satisfy |Delta|≤10⁻¹², while the residual identity detunings remain bounded by 10⁻¹⁹. The comparison target is the exact nominal packet at the **same supplied Delta**. This is not closeness to one zero-offset target when Delta is unknown.

The component arguments and operating-point composition have completed selective checks. This publication synthesis is prepared for separate integration review; it is not a retained-status audit or experimental validation. Its parent is [Structured source tolerance for complete autonomous output](STRUCTURED_SOURCE_TOLERANCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md). The portable proof packet is `outputs/common_source_offset_2026_10_17/proofs/`; exact source identities are collected below.

## Conditional device family and target

Retain the original calibrated .0027<j<.003 and set

    lambda=10^-13, g=5×10^-8, h=4×10^-6,
    T=2×10^14, M=50,000,000.

Keep the parent's physical graph, endpoint and converter calibration, record gate, shared internal operator B, source vacuum, real negative exchange signs and exact slow receiver. For each supplied real Delta and residual tuple require

    |Delta|≤10^-12,
    a1²=(lambda²/3)(1+e1), a2²=(8lambda²/3)(1+e2),
    kappa²=3jlambda(1+e3), |e_i|≤10^-6,
    |r_i|≤10^-19.

All amplitudes are positive. Delta+r_i multiply the entire internal identity, not an old-energy-, parity- or record-dependent operator. All remaining device coefficients and the preparation are exact supplied premises.

The source coordinates remain s₀=(40,66,1), s₁=(40,65,1), s₂=(40,64,1), with old port p=(40,63,1). With nᵢ the head occupation and X_uv=|10⟩⟨01|+|01⟩⟨10|, use six positive blocks:

    j(n₂+n_p)−kappa X₂p,
    a2(n₁+n₂−X₁₂), a1(n₀+n₁−X₀₁),
    (j+Delta+r2−a2)n₂,
    (2j+Delta+r1−a1−a2)n₁,
    (2j+Delta+r0−a1)n₀.

Their source diagonals are 2j+Delta+r_i. Compression away from all three source heads retains exactly j n_p, so the emitter-free background is unchanged. These positive occupations must track the changed coefficients. They vanish on blank heads and add no vacancy scalar. Shared B occurs once, with Bι=ιK on the prepared vacuum, where

\[
 K=2I+Z_1Z_2,\qquad
 W={(9+12i)I+(-16+12i)X_1X_2\over25}.
\]

Prepare the head at s₀, all other heads blank, the original internal source vacuum and computational record0. Let V be this seed isometry, allowing arbitrary old inputs entangled with arbitrary passive references. No commutation of full H with K is assumed.

The physical processor windows remain

\[
 I_e=c_{\rm att}+2j+e+[-d,d],\quad e=1,3,\qquad d=2j\sin h.
\]

They do not move with Delta. Define the exact nominal scalar packet by setting e_i=r_i=0 at the same Delta. Its scalar determinant uses y=delta−Delta but the **physical** load m_j(delta):

\[
 q_\Delta(\delta)=(y^2-\lambda^2/3)
       [y-3j\lambda m_j(\delta+i0)]-(8\lambda^2/3)y.
\]

Its transmitted hard-band coefficient retains the physical phase 61.5q+.5k+172k_old(q), the calibrated ζ, exact flux/Jacobian, and delta=−2g cos k. Let β_Δ,0(t) be its raw outgoing packet on the physical slow halfline m≥0, evolved with exp[−it(2j+delta)], and r_Δ,0(t)=‖β_Δ,0(t)‖. The bounds below ensure r_Δ,0(t)>0 on [T,2T]. Define

\[
 \mathcal T_{\Delta,0}(t)=e^{-itc_{\rm att}}
 J_{\rm out}\!\left[{\beta_{\Delta,0}(t)\over r_{\Delta,0}(t)}
                    \otimes e^{-itK}W\right].             \tag{1}
\]

This normalized complete target has record1, source vacuum and blank nonoutput heads. It is fixed across residual tuples at that Delta; it is not a fitted or postselected actual waveform. The theorem is

\[
 \sup_{T\le t\le2T}
 \|\operatorname{embed}e^{-itH_{\Delta,r,M}}V
                   -\mathcal T_{\Delta,0}(t)\|<.000986.    \tag{2}
\]

Finite actual states are embedded into the same infinite comparison space, without projecting or renormalizing the target tail. Equation (2) includes all output coordinates, records, residual source/core states and passive references.

## What the common-offset extension proves

A source-only potential Delta P_source is not a full-apparatus scalar. The [scalar common-mode argument](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_source__PROPOSAL.md) retains m_j(Delta+y), proves real-band cubic margins and separately excludes hidden exterior scalar mass. It compares complex scalar packets at the same Delta. Even when Delta/j is small, shifted cubic packets can differ strongly from the zero-offset packet: their absolute overlap is [1+(Delta/(2lambda))²]⁻⁵ᐟ². This explains the target-family qualification; it is not a universal limitation on other architectures.

The [actual inverse and moment interface](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_actual_interface__PROPOSAL.md) keeps the original physical windows and full eight-dimensional forcing. In matrix notation Y=D−Delta I shifts only the source factors; the reference load remains m_j(D). The ordered Neumann factor retains all complementary channels and wrong-window inputs. Its error envelope includes a₀+b₀|Delta| after expressing physical delta in terms of y. Recentring does not remove that term.

The actual sixth central moment about the shifted source center is obtained directly from the installed prefix. The third Hamiltonian application first reaches the port, so its shifted port diagonal has not acted yet. Concentration in the original windows consequently pays the distance d−|Delta|. This covers actual outside atoms and other spectral types; scalar absence of atoms is not transferred to the apparatus.

The [local/core interface](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_local_core__PROPOSAL.md) controls all three source heads, the remaining finite core and closed tails. The [traveling interface](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_traveling__PROPOSAL.md) uses the physical scalar second moment (Delta+r₀)²+a₁², not its recentered variance. It preserves both physical windows and the full outgoing row. Real Stone conjugation gives incoming W* with the same physical exp(−itE); it does not conjugate arbitrary input/reference states.

The new [shifted reference-time argument](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_reference_time__PROPOSAL.md) is needed because bandcenter time estimates do not automatically transfer. It expands around k_Δ=acos(−Delta/(2g)), with velocity v_Δ=2g sin k_Δ and x=v_Δ(k−k_Δ). The exact dispersion is

\[
 \delta-\Delta=v_\Delta\sin(x/v_\Delta)
                 +\Delta[\cos(x/v_\Delta)-1].
\]

The quadratic curvature term is paid using a finite fourth moment; the cubic remainder uses a truncated sixth moment. The proof retains physical phase and Jacobian, both hard-cutoff tails, periodized lattice aliases, m=0 and exp[−it(2j+Delta)] exactly once. It provides scalar halfline bounds, not an unproved actual-source analytic continuation.

## Complete budget and finite receiver

The [complete family derivation](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_complete__PROPOSAL.md) and its [distinct composition check](../outputs/common_source_offset_2026_10_17/proofs/three_site_common_mode_complete_check__REVIEW.md) substitute this one family into those interfaces. The full inverse has Θ<.000077 and c>.9999029; the shifted installed moment is μ₆<8.000026×10⁻⁶⁸. The original-window outside amplitude is <4.1×10⁻¹¹.

The complete infinite-device budget on [T,2T] is:

| Contribution | Strict ceiling |
|---|---:|
| One global actual outside state | 4.1×10⁻¹¹ |
| All three represented source heads | .000117 |
| Remaining finite coordinates and closed tails | .000505 |
| Both actual traveling discrepancies, 2E_raw | .000319 |
| Both residual packets replaced by same-Delta nominal packets | .00004301 |
| Nominal raw incoming halfline packet | 3.1×10⁻⁷ |
| One physical-halfline normalization, 1−r_Δ,0(t) | 4.04×10⁻¹⁰ |

The sum is .000984320445<.000985. Both Stone lips and every wrong-window prepared column are included. Scalar reference truncation is contained in the source comparison and is distinct from the single actual omitted vector. The two traveling errors share physical coordinates and are added, not assumed orthogonal. Neither the actual output nor the perturbed scalar mass is normalized to hide error.

For the nominal same-Delta halfline estimates, proof cutoff D=g/8 stays inside the original physical band throughout the family. The checked substitutions give scalar comparison E<3.1×10⁻⁷, outgoing excluded norm <1.2×10⁻⁶ and transmitted mass deficit <4.02×10⁻¹⁰. These establish the last two budget rows and positivity of r_Δ,0. They are fresh shifted-carrier estimates, not zero-offset timing imported as a premise.

The exact compression cap and output-only weighted single-cut comparison give, uniformly for 0≤t≤2T,

\[
 \|U_\infty(t)V-\operatorname{embed}U_M(t)V\|
 <1.2e^{-M+4gT\sinh1}
 <1.2e^{-2,960,000}<10^{-10}.                           \tag{3}
\]

All source changes lie in the zero-weight region; only unchanged slow bonds g contribute. The estimate includes returns and reflections. Combining (3) with the complete budget proves (2).

The six-block family's counts remain M+238 head sites, M+243=50,000,243 physical qubits, M+239 head edges and 2M+281=100,000,281 unmerged positive blocks. These are counts for the specified construction, not minima. The parent's optional seven-block re-expression has H_new=H_old+C_src(actual)I with C_src=κ+a₁+a₂. If used, the target must also be multiplied by exp[−itC_src(actual)] and the block count increases by one. That exact identity is distinct from the source-only Delta modification and is not needed for (2).

## Precision, scope and evidence

The common offset range is ten linewidths and 10⁷ times the residual diagonal bound. This separates a supplied common offset from residual source disorder; it does not relax every diagonal error to 10⁻¹². The positive occupations track the source coefficients, and all downstream calibration, shared-source identification and preparation remain supplied premises. An unknown offset does not define a single target in (1). Native interaction realization, coefficient supply and a physical-seconds interpretation are not derived.

There is no early-read guarantee, guarantee after 2T, repeated monitoring/reset theorem, irreversible capture or permanent halt. No native-cell or derivative result is imported. The result is a conditional complete-map certificate at an existing finite receiver, not experimental performance or an optimum.

This drafter authored the shifted reference-time argument and complete family composition, and has attachment/traveling/reference ancestry. The shifted-reference checker authored scalar and actual-interface ancestors; those have their own recorded distinct checks. Root authored local/core and traveling extensions, separately checked by this drafter, and performed the distinct operating-point review. The exposure is explicit: these are selective same-model analytical checks with shared ancestry, not blind or model-diverse recertification of all premises. The full composition review was read before drafting this note.

Publication integration and portable source-copy/link verification are recorded separately. No new numerical dynamics, spectrum, sweep, solver, scientific runner, retained audit or editable prompt change is claimed by this synthesis.

## Primary exact source identities

| Source | SHA-256 |
|---|---|
| `three_site_common_mode_source/PROPOSAL.md` | `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb` |
| `three_site_common_mode_source_check/REVIEW.md` | `af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb` |
| `three_site_common_mode_actual_interface/PROPOSAL.md` | `9225b6ea6533dea56db4f8b7157deac5c6f52e5927b554052c59299622a13957` |
| `three_site_common_mode_actual_interface_check/REVIEW.md` | `e9b32196906e1d4b5010ac9b30d348e438d6e88fcdac82d51ae107f3f7ba1cea` |
| `three_site_common_mode_local_core/PROPOSAL.md` | `e817e63d7b6e7d1ba7d87db2322b8b5b7dd88b028fdbdd59962d4c3898713dcf` |
| `three_site_common_mode_local_core_check/REVIEW.md` | `644e29302a077f72e940c7396c562bf1ba87a5741f60a66c86dc7f6899972d77` |
| `three_site_common_mode_traveling/PROPOSAL.md` | `0abafe7b46fe6c93df110df8bc1e7a9dbc3a4eca30d38dbdea619337ca75940d` |
| `three_site_common_mode_traveling_check/REVIEW.md` | `4ac2571d63c5c6b4e7d7ea4e490a224b1e3d9d0a34b7ca4d82bce7fcc5038bdd` |
| `three_site_common_mode_reference_time/PROPOSAL.md` | `646f26bdb76fbb0b5c8144d492f094c6ffd191fd7312a6c77373fdc069b9d4de` |
| `three_site_common_mode_reference_time_check/REVIEW.md` | `0a49ed087c65465fb6df43783135afdbfe64b0c18d4d280a68bbb0d9a420a39d` |
| `three_site_common_mode_complete/PROPOSAL.md` | `fd5bdb8e9c40a7b8ad9904b3e0bc5519354ca1c1f9451aeacfc49e82b9161425` |
| `three_site_common_mode_complete_check/REVIEW.md` | `5fd025e507dc79f7106b397b334d34134558066c1e0553ae35a73ec919135a63` |

These source arguments enumerate the inherited identities and scope restrictions; their checks do not replace those premises.
