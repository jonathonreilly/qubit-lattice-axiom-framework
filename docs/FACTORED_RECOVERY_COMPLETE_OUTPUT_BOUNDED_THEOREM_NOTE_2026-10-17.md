---
claim_id: factored_recovery_complete_output_bounded_theorem_note_2026-10-17
claim_type: bounded_theorem
claim_scope: "Conditional supplied nominal three-source apparatus: factored input/gate recovery derivative and complete operator error below .00076 on [1e13,2e13] with 2500243 physical qubits. Full analytical proof packet controls; finite runner corroborates ordered cap/gate identities, slow-root derivative restoration and ceiling arithmetic, not the full apparatus, continuum proof or physical realization."
upstream_dependencies:
  - faster_three_site_complete_output_bounded_theorem_note_2026-10-17
runner: scripts/factored_recovery_complete_output_2026_10_17.py
---

# Factored physical recovery: an earlier complete three-site output window

Claim type: bounded_theorem. Status: conditional publication draft prepared for review. The full recovery derivative and gate-load action have completed distinct checks. The new complete operating point has also completed its distinct check; final publication integration remains required. No retained audit status is conferred.

Under the unchanged original physical/calibration and preparation premises, the proposed complete certificate is **operator error <.00076 at every chosen read time in [10^13,2×10^13]**, with **2,500,243 physical qubits**. The new point uses

    lambda=2×10^-12, g=5×10^-8, h=4×10^-6,
    T=10^13, M=2,500,000,
    a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda.

The calibrated j remains fixed, with .0027<j<.003. The [PR9685 scientific and technical parent](FASTER_THREE_SITE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md) certifies lambda=10^-12, T=2×10^13, M=5,000,000 and complete ceiling .00086. The proposed point halves its interval scale and receiver sites, with a smaller sufficient ceiling, using a newly checked structural recovery bound. Each certificate uses different source coefficients and its own common waveform for all old/reference inputs. The comparison is between sufficient certificates, not measured error, an optimal time, or inability of the previous device to work earlier. Total-qubit ratios include the fixed offsets.

The mathematical improvement is a derivative bound for the actual full recovered background, including every finite head and all closed slow tails. It replaces the former large arbitrary-forcing estimate with physical cap and converter response identities, then uses the gate load acting on the actual forced state. The new point recomputes the remaining source, spectral and traveling costs; it does not assume they stay invariant when lambda*T stays20.

## Physical apparatus and literal common target

Keep the original contact/filter source, shared B, converters, capped input, eighteen-edge cable and24-head record gate. The source port is p=(40,63,1), with s2=(40,64,1), s1=(40,65,1), s0=(40,66,1). The initial head is at s0 with the supplied source vacuum, computational record0 and other prescribed blank registers. The nominal six positive source blocks are

    j(n_s2+n_p)-kappa X_s2,p,
    Q_a2(s1,s2), Q_a1(s0,s1),
    (j-a2)n_s2, (2j-a1-a2)n_s1, (2j-a1)n_s0,
    Q_a(u,v)=a(n_u+n_v-X_uv).

Here kappa<1.342×10^-7<j; the first block's eigenvalues are0,j-kappa,j+kappa,2j, and all remaining occupation coefficients are positive. Source diagonals stay2j. Compression off the three source heads leaves exactly j n_p, not a second copy of that cap. Shared B appears once, with B iota=iota K on the prepared vacuum. No new vacuum scalar is introduced and no full [H,K]=0 identity is assumed.

The slow receiver starts at r_m=(100,3+m,2), m>=0, beyond the distinct gate port o=(100,2,2). Its connector is sqrt(jg), internal hopping is g, and compensation occupations preserve diagonal2j. Keeping M sites and adding g n_r(M-1) realizes exact principal compression. It is not an absorbing boundary. The nominal source and exact graph/positive-block conventions are inherited from the [three-site temporal parent](THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md) and [spectral parent](CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md).

Retain literally

    K=2I+Z1Z2,
    W=[(9+12i)I+(-16+12i)X1X2]/25,
    c_att=2nu+2beta+4gamma_J+4gamma_c+4(sqrt(2)-1)j.

For d=2j sin h, physical windows are c_att+b+2j+[-d,d], b=1,3. Let delta=-2j cos q=-2g cos k and k_old(q)=2asin(sqrt(j/J)sin(q/2)), using the original calibrated J. The scalar reference coefficient is

    q3(delta)=(delta²-lambda²/3)(delta-kappa²m_j(delta+i0))
                                                -(8lambda²/3)delta,
    F3(q)=kappa a1a2(2j sin q) zeta exp[i61q+i172k_old(q)]
                                            /[sqrt(2pi)j q3(delta)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)).

It vanishes off the hard band. All physical reference planes, the slow Jacobian, fixed zeta and full denominator phase remain. In particular the phase61.5q+.5k+172k_old is not replaced by a fitted constant or interpreted as a number of slow-site translations. Define

    beta_t(m)=1/sqrt(2pi) int F_s(k)exp[ikm-it(2j-2g cos k)]dk,
    r(t)=||beta_t||_(m>=0),
    Tnorm(t)=exp(-it c_att)Jout[(beta_t/r(t)) tensor exp(-itK)W].

Jout supplies record1, source vacuum and the other prescribed registers. The bound below establishes r(t)>0. This is one common apparatus vector for every old input and passive reference. The finite actual evolution is embedded into the same infinite comparison space; no target tail is silently removed or renormalized again. The complete inequality is not obtained by postselecting actual output.

## The checked physical derivative chain

The exact uncapped new-port convention is S=T A^-1, A=[j(Q-Q^-1)]^-1. The input-cap factorization (`outputs/factored_recovery_2026_10_17/proofs/input_cap_factored_forcing__PROPOSAL.md`) proves, for the retained input sites0,...,20,

    alpha=-Q^21(I+Q^21 S_aa Q^21)^-1/j,
    Q^-n alpha=-Q^(21-n)(I+Q^21 S_aa Q^21)^-1/j.

Its distinct check (`outputs/factored_recovery_2026_10_17/proofs/input_cap_factored_forcing_check__REVIEW.md`) verifies the full noncommuting order, negative sign and21-step phase. Growing closed powers cancel before norms or derivatives are taken.

The direct old-core derivative (`outputs/factored_recovery_2026_10_17/proofs/prepared_core_direct_derivative__PROPOSAL.md`) and converter derivative (`outputs/factored_recovery_2026_10_17/proofs/prepared_converter_direct_derivative__PROPOSAL.md`) differentiate the physical matching equations and retain both40-step planes, first-new-site phase and velocity conversion. Large complementary old derivatives use an actual finite analytic-domain bound; a small real reflection or value norm is never treated as derivative evidence. Their separately scoped core check (`outputs/factored_recovery_2026_10_17/proofs/prepared_core_direct_derivative_check__REVIEW.md`) and converter check (`outputs/factored_recovery_2026_10_17/proofs/prepared_converter_direct_derivative_check__REVIEW.md`) preserve this scope.

The cap scattering derivative (`outputs/factored_recovery_2026_10_17/proofs/input_cap_scattering_derivative__PROPOSAL.md`) and complementary new-port recovery (`outputs/factored_recovery_2026_10_17/proofs/complementary_converter_recovery_derivative__PROPOSAL.md`) then cover arbitrary endpoint forcing. Direct complementary incidence at the outer old plane is not exponentially suppressed; only its source-reflected return is. Paying that direct term and the tiny actual cap coefficient gives an OLD172-head forced derivative <1.9×10^14. The combined bridge review (`outputs/factored_recovery_2026_10_17/proofs/input_cap_derivative_bridge_check__REVIEW.md`) checks both new arguments together, rather than counting them as independent evidence for each other.

The full factored recovery (`outputs/factored_recovery_2026_10_17/proofs/prepared_full_recovery_factored_derivative__PROPOSAL.md`) includes the21 input sites,18 cable heads and24 gate heads as well. Its distinct review (`outputs/factored_recovery_2026_10_17/proofs/prepared_full_recovery_factored_derivative_check__REVIEW.md`) verifies the following structure. Keeping B_o=Q_old^40 S_o Q_old^40 before differentiation suppresses the genuinely large closed source derivatives and yields a full new-port scattering derivative <60000. Exact cap products give all finite-input derivatives. The complete last-cable Green column has value <8000 and derivative <2.22×10^14. These are full-fiber bounds, not scalar selected-column estimates.

For the gate update, the load-action proof (`outputs/factored_recovery_2026_10_17/proofs/prepared_gate_load_action__PROPOSAL.md`), with its distinct root check (`outputs/factored_recovery_2026_10_17/proofs/prepared_gate_load_action_check__REVIEW.md`), gives an additional reduction. Gate head terms act trivially on the old/source fiber; terminal record terms are j n_T(I+X_R). Thus the local gate and slow surface commute with B, even though the preceding processor need not. With actual outgoing cable coefficient b, at a=v17 set

    b_a=Q^17 b, rho=Q² r_gate,
    y=(I+rho)b_a,
    D_g=-jQ-j²G_g, rho=-A D_g(I+A D_g)^-1.

The exact action is D_g y=-A^-1 rho b_a. The selected contribution is <.006*.129*460=.35604. Closed roots retain their actual propagated inverse-root factors and contribute <10^-29. Hence **||D_g y||<.357** on the full endpoint-forcing domain. This is not a claim that ||D_g|| is uniformly small: the coarse uniform .102 bound remains. Only its action on this actual response is improved, and that action bound is not differentiated.

In the ordered derivative of F_U=F_D-C_a D_g y, this replaces only the C_a' D_g y estimate. Hold the slow boundary root fixed for a local algebraic partial derivative dot, keeping all other energy dependence. The resulting complete finite bound is ||dot F||<2.9×10^14. The assembled equation restores the physical derivative exactly:

    M(E)=E I-H_finite+j V_o Q_slow(E)V_o^T, R=M^-1,
    F'=dot F-j R V_o Q_slow' V_o^T F.

Thus the slow derivative is paid once, not discarded. The checked output-column bound250000, actual output value3270 and ||Q_slow'||<1/(1.93g) give the full result

    ||L'||<1.00068[2.9×10^14+1.28×10^6/g]+30.

L includes all235 finite heads and every closed slow tail. The factors .00068 and .009 arise from the complete geometric lift and derivative series. Within each window the closed-channel projections are fixed and all vectors lie in the same physical output Hilbert space. Both lips, full forcing and passive references are retained; the propagating stationary ray is handled separately. The old source53f571b6 is contextual unchecked work, not a numerical premise of this chain.

## New complete point: every changed allowance

The new point derivation (`outputs/factored_recovery_2026_10_17/proofs/factored_recovery_complete_point__PROPOSAL.md`) recomputes all source-dependent quantities. Its completed distinct root review (`outputs/factored_recovery_2026_10_17/proofs/factored_recovery_complete_point_check__REVIEW.md`), SHA256 `c9de3941b6a3eb580e021e385550112221547033767ab0c39ebb64724d36b94d`, supports the changed arithmetic and full composition with no required correction. The review retains the supplied premises and its shared ancestral exposure; it is not a blanket recertification of those ancestors.

With a0=8×10^-18, b0=46000/.0053+290/g<5.81×10^9 and s=sqrt(1-3lambda/j), the full ordered three-site inverse has

    Theta=(j a0+kappa²b0)/s+6kappa²(a0+b0d)<1.048×10^-4,
    c3=(1-Theta)s>.9998951.

The installed sixth moment is mu6=3lambda^6+(8/3)jlambda^5<2.56000001×10^-61, including the port-reaching term. Its full-input common-union bound is sqrt(2mu6)/d³<7.3×10^-8. This is the one actual omitted vector, including every outside spectral type. It is not replaced by scalar reference mass or charged once per spatial region. In-window regularity still comes from the complete matching/root premises.

The all-three-source local comparison gives E_vec<8×10^-9, selected integral D_sel<3.149×10^-5 and wrong-window integral D_wrong<1.1×10^-33. Since lambda*t ranges from20 to40, the joint reference source amplitude is <7.3×10^-7. Including its distinct scalar truncation gives represented source norm <.000046.

At the new point the checked full Lprime is <3.159×10^14. The independently checked nominal cubic cancellation keeps |q0'|<3.00002(delta²+lambda²), while all noncommuting loading and complementary terms remain in the prepared derivative integral. Recalculation gives D3<2.24×10^12. The background IBP interface (`outputs/faster_three_site_2026_10_17/proofs/prepared_background_ibp__PROPOSAL.md`) therefore yields

    B_IBP(t)<=2kappa/(pi|t|) *
      [2c_a lambda² L0/(c3(d²+lambda²)^(3/2))
                                  +2c_a M_g/c3+L0 D3]
                <.000274*T/t, t>=T,
    c_a=2sqrt(2)/3, L0=14000.

Both hard endpoints, both lips and both physical windows are paid in this formula. The bracket terms are <10700, <5.965×10^14 and <3.136×10^16; the inverse-derivative term now dominates. The absolute alternative <.00227 remains valid but is not used in the final sum. No actual outside state is appended inside either background bound.

The exact outgoing row and scalar second moment lambda²/3 give selected raw error <1.523×10^-4, complementary error <10^-33 and total outgoing-plus-incoming coefficient allowance <.000432. Reality supplies the incoming coefficient by fixed conjugation of the rectangular Stone column, with physical exp(-itE) unchanged and ideal old multiplier W*, while outgoing uses W. Both errors can occupy the same physical ray and are added by triangle. Wrong-window inputs remain included.

The weighted scalar time theorem (`outputs/three_site_temporal_2026_10_17/proofs/three_site_weighted_reference_time__PROPOSAL.md`) is evaluated at the proof cutoff D=g/4, preserving literal F_s. It pays central phase/denominator error <5.86×10^-6, truncated-sixth-moment dispersion <2.78×10^-7 through2T, both hard tails <2×10^-10 each and lattice aliases <1.7×10^-13. The scalar mass deficit is <5.335×10^-10. These imply raw incoming norm <6.2×10^-6, outgoing excluded-halfline norm <7×10^-6 and one physical target normalization cost1-r<3×10^-10. No divergent full sixth moment or actual loaded scalar density is substituted.

| Complete contribution | Strict ceiling on [T,2T] |
|---|---:|
| One actual outside state | .000000073 |
| All three represented source heads | .000046 |
| Remaining finite background and closed tails | .000274 |
| Both raw traveling coefficient errors | .000432 |
| Raw scalar incoming packet | .0000062 |
| One physical target normalization | .0000000003 |
| Complete finite/infinite transfer | .0000000001 |
| Sum | .0007582734 |
| Proposed certificate | .00076 |

For the finite cut, the output-only weight is zero through r0 and increases by one along each slow bond. Exact cap compression and single-cut Duhamel give transfer <1.2exp[-M+4gT sinh(1)] on[0,2T]. Here4gT=2,000,000 and sinh(1)<1.176, giving exponent<-148,000 and transfer<10^-10. This includes all channels and returns; no absorbing-boundary premise is introduced.

The distinctly checked conditional complete result is

    ||J_M exp(-itH_M)V_M-Tnorm(t)||<.00076,
                         every t in [10^13,2×10^13].

The range is every apparatus output, and the domain includes arbitrary old inputs and passive references. Record1 failure effect is then <5.776×10^-7 I, success >.9999994224, normalized successful-vector distance <.000761, and complete-channel and successful SUBNORMALIZED CP-map diamond errors <.00152. Normalized conditioning is nonlinear and is not assigned a linear-channel diamond bound.

## Inventory, scope and evidence

The nominal inventory remains M+238 heads, M+243 physical qubits, M+239 head edges and2M+281 unmerged positive blocks: respectively2,500,238;2,500,243;2,500,239;5,000,281. Shared old/source/record qubits are counted once and passive references are excluded. Original incident loads are retained; the whole device's interactions are not bounded by the slow g alone.

The larger lambda increases actual moment, selected loading and traveling errors. The improved background bound offsets those costs in this sufficient certificate; there is no universal scaling claim. The derivative envelope is uniform only on its explicit positive-g real-window domain, and the temporal bound only on this selected finite interval. It is not an all-late-time guarantee for a capped device, permanent halt, irreversible memory, repeated monitoring or reset. No mediator construction, source-offset/tolerance family, arbitrary hardware noise, native coefficient supplier or physical-seconds conversion is imported.

All original exact calibration, correlated coefficients, positive selective interactions, product/source-vacuum/record preparation and native Hamiltonian/Record identification remain supplied conditional premises. The proof packet assembles whole arguments at their stated scopes, not conclusions inferred from filenames or check labels.

I authored the new point and several derivative/source/time ancestors. The cap bridge and full recovery have separate source-exposed checks; root independently checked the gate action. This note is same-model synthesis with shared ancestry, not a blind or independent recertification of its author's proofs. The new point review has been read in full and is complete. Final publication integration remains an open gate. Root owns the manifest, exact copies and graph evidence. Planned portable proof links use `outputs/factored_recovery_2026_10_17/proofs/<folder>__<filename>`; identity checks are not mathematical validation.

No scientific runner, numerical inverse, quadrature, dynamics, sweep, optimization, new parameter point, W/Git/PR/checkpoint/prompt/model change or delegation occurred while drafting this note. Only this research note was created.

Exact primary revisions:

- `input_cap_factored_forcing/PROPOSAL.md`: `95755c3a08b6434a7ec7f86897a80f975c7575be747d1a9f09cdf34c9cce4376`.
- `input_cap_factored_forcing_check/REVIEW.md`: `85ad12b8df4b15a4abeeded5b28e84d1413f9ab848122ca0e45e0e09eece66d3`.
- `prepared_core_direct_derivative/PROPOSAL.md`: `cfca9422163b4f4694a2efddbbff6779bd3c354bbd505e90af4d16189d1e40be`.
- `prepared_core_direct_derivative_check/REVIEW.md`: `75563597ec6edd1b688bfd81b51b4dc5b1adab7033d9f78a860f759cf5e70729`.
- `prepared_converter_direct_derivative/PROPOSAL.md`: `a444e105c88fcfad8fcae59b7f72d9dd9247e2b83ada73edeb7b97a849b33653`.
- `prepared_converter_direct_derivative_check/REVIEW.md`: `283494e3a50b12b77bf9d4be184452b49b582627fac20c802087e00e4d69e11d`.
- `input_cap_scattering_derivative/PROPOSAL.md`: `909fef0047e8380d00e1807cf9d88b74b0ff6704600414c0192ab296cb96069b`.
- `complementary_converter_recovery_derivative/PROPOSAL.md`: `ba7616be0df86880d68192641376422752d4a8bbcfc9f120fa62d196824361ec`.
- `input_cap_derivative_bridge_check/REVIEW.md`: `a9d60f8dd222af929c1d94cd860e4f51d2cd53b54a036a2e3480e0aa5a90a3d8`.
- `prepared_full_recovery_factored_derivative/PROPOSAL.md`: `09606913b6bd71637b089ded04180b3afa6934ae39fa85926cb05d4e1f69423a`.
- `prepared_full_recovery_factored_derivative_check/REVIEW.md`: `1a00c38e88361c0ca0e825ee4e339f5c419c1d9a16ec4d6495e34802d0835244`.
- `prepared_gate_load_action/PROPOSAL.md`: `89f04354d21d2ff9cb996dade6f1f92afb0f3f584ead81037978bc53055f5252`.
- `prepared_gate_load_action_check/REVIEW.md`: `fb5967fae2d36ba44dd8de92321b77ad5b78286e22a66a6ff5582b7d7b673275`.
- `factored_recovery_complete_point/PROPOSAL.md`: `7299cbf0dcfe9e3af93f64c1b17c8f906fac43ef9186200c489b760be49aecb1`.
- `factored_recovery_complete_point_check/REVIEW.md`: `c9de3941b6a3eb580e021e385550112221547033767ab0c39ebb64724d36b94d`.

## Reproducible finite corroboration

Run `python3 scripts/factored_recovery_complete_output_2026_10_17.py` (declared cap120seconds). Imports are inert. The primary checks finite noncommuting cap/gate identities, the canceled input products and two-step gate plane, three physical slow-root derivative samples, and arithmetic of the supplied ceilings. Wrong-order/phase and omitted-derivative controls prevent trivial identity-only success. It does not execute the235-head model, continuum estimates, dynamics, or calibration. The181 original source pins and eight inherited mapping manifests resolve to regular files (204 declared inputs total); the manifests are provenance metadata, not additional proof; historical canonical snapshots and11 current parent sources are separately bound in `outputs/factored_recovery_2026_10_17/landing/PROOF_INPUT_BINDING.json`. The historical53f571b6 proposal remains contextual and is not a numerical premise. Original author review/status statements above record provenance, not independent landing approval or an audit verdict. Exact original-note recovery is in the same landing folder.
