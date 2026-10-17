# Larger-coupling source integration review

Finding: no mathematical source drift, missing load-bearing numerical hypothesis, or verification overclaim found in the inspected changes. The appended proof and top summary preserve the reviewed conditional result: kappa=10^-8, infinite complete operator error <.000320 for t>=4e21, and one fixed M=2e23 device with finite error <.001320 on [4e21,8e21]. No source correction requested.

## Scope and exposure

I read the complete note diff against 62e1e95bb012350410a1ff18764ebd97babcd697: the new leading summary and all 418 appended lines, including provenance and verification limits. I read the runner's complete new LC arithmetic section, added input paths and metadata, the complete manifest addition, frozen CHECK_MAP and root qualification. The earlier unchanged component arguments and final composition check are reused at their pinned revisions. An initially truncated runner diff was replaced by a complete direct read of the changed arithmetic. An oversized canonical-result display was not treated as full verification: only its separately extracted metadata was used below.

I authored the original weighted-profile proposal and several component reviews, including the final composition report. This is source-exposed integration review, not a new independent proof of those components. No science execution, syntax compile, inherited program, simulation, numerical integration or scientific rerun occurred. Read-only Git diff was specifically authorized. No W/Git/PR/checkpoint/prompt edit occurred; only this report was written. Model and effort remained unchanged, and previously read applicable guidance was reused.

## Mathematical integration

The proof retains the new physical positive compensation and its unchanged background/scalar, all eight emitter coordinates, local Stone normalization and synthesis, and a separate charge for all exterior spectral mass. The coarse p0>=.84 only establishes existence over the coupling range. The improved p0 bound at the selected coupling is proved before its use in amplitudes and the restricted moment. The full ratio includes the coupling-dependent complementary terms and retains d0 and the fixed closed-channel floors.

The background construction includes the two details required by the regularity review: closed A is a free full-line diagonal resolvent with its actual gap, and the outgoing row <130 uses Tg_PP=Aopen*r_g*z^2. The generic ||Tg||<208 is not misused to infer that row. The two-site norm factor, 24+20 propagation steps, phase derivatives 42 and 90, and all complementary derivative terms survive the integration.

The dependency chain remains acyclic. Real energy regularity supplies the mass lemma; actual complex disks separately supply operator Cauchy and exact Schur-self-energy oscillation. The proof does not infer complex continuation from the real derivative. It establishes complementary invertibility before defining the Schur continuation and pays the complex energy change separately. The complete source-specific strip uses background continuation and the supplied resonance margin, not the old fixed-kappa full inverse.

The density comparison retains the shift c, normalization of the actual global spectral measure, finite cutoff and regularity smallness hypotheses. Conservative L=10^6 is used only after proving L<36000. Reference and actual deficits are distinct. The restricted dk moment keeps its Fourier factor, shifted denominator and full interval width. Its resulting static cost is the previously reviewed .000318243241<.000319.

The same f,p0,a0 and actual generalized columns occur throughout. The fixed scalar profiles are conjugated; arbitrary old/reference inputs are not. Preparation and localized columns pay their within-parity overlap factors, while orthogonal open fibers do not acquire a spurious factor. The C subtraction is algebraic off-real, retaining complete core and closed tails with Hilbert-space analyticity. Bottom and both hard-cutoff sides survive. The scalar contours keep the corrected exp(-y) identity and outgoing phase113; positive target normalization remains quadratic.

The new scalar outgoing paragraph uses a loose .18/kappa coefficient where the checked component and runner use .176/kappa. This is harmless: the displayed .012 prefactor remains valid even with .18, since .18*2J/sqrt(pi)<.012 for J<.031. The stronger .176 coefficient itself follows from 17*.062/6<.176. No error budget depends on equating those two ceilings.

The real source trace uses .122 from the inherited real E'<.061 bound, explicitly present earlier in the same note; the new .062 complex envelope does not replace it. Likewise the side real-part loss .061h^2 is conservative relative to the inherited analytic energy formula. These are not newly missing hypotheses.

The final sum includes static, complete localized, incoming and positive normalization costs, with ample rounding margin below .000320. Radius18, distance M+23, finite interval [T,2T], M+116 qubits and comparison to the same embedded infinite target remain explicit. The leading summary correctly says the coupling and actual profile change and does not preserve the old sharper error pair. Operator and unhalved trace tolerances are distinguished.

## Runner and evidence language

The new LC block uses separate lc_ parameters and leaves historical kap/T checks intact. Exact Fraction substitutions corroborate the reviewed bounds. In particular it retains Neumann smallness checks, conservative real mass constant, complementary Schur correction, all-column trace factor eight, separate side/bottom source bounds, the two-side and overlap arithmetic identities, phase113, squared normalization, restricted width2sigma, outgoing factor2, finite transfer prefactor and trace factors. Input additions name the reviewed components and composition; their manifest pins agree with those in the composition report. No positional old input indices were introduced by this diff.

The runner and CHECK_MAP explicitly do not establish analytic identities, local synthesis, actual mass accounting or operator aggregation by execution. The map's draft/unexecuted language and old runner pin describe the frozen authoring artifact, while the note separately describes later canonical execution. They are not conflicting claims about the same event. The frozen root qualification similarly labels arithmetic execution as pending at its creation.

I inspected canonical receipt metadata (status ok, exit0, empty stderr and stated elapsed time), the complete 17-entry mutation summary and the four integrity-case/inert-import summary. These agree with the note's bounded descriptions. I did not independently inspect every mutation diff, full stdout, prelaunch receipt or runtime pin, and did not reproduce any run. Therefore the detailed 331-check/76-input/byte-count and intended-failure execution claims remain root-owned evidence, not newly verified execution results from this review. The source appropriately labels them scalar coverage probes rather than independent proofs or a full combined-main landing check. No stronger scientific claim is inferred from their count.

## Source pins

W is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree. N is its sibling renewal_20261017_110934. Refreshed SHA256 values:

| Source | SHA256 |
|---|---|
| W/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md | bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5 |
| W/scripts/real_endpoint_autonomous_output_2026_10_17.py | 93cc122aa253fc2a6fc26748826561bdf61343227e36a9f1df02f4f248e5b991 |
| W/outputs/real_endpoint_autonomous_output_2026_10_17_inputs/ARTIFACT_MANIFEST.json | 450b972b5fdc715b71e8213446b1cef7aab5814a898fc3c09c6ec5f3de2950f6 |
| W/outputs/real_endpoint_autonomous_output_2026_10_17_larger_coupling_validation/CHECK_MAP.md | 85a173e4683594126b649921dfbef56fc9a56313219717a83e5afa6df5ef936b |

Reused exact composition: N/LARGER_COUPLING_COMPOSITION.md, 3fd18e576fb394caea2b93272c4b430d782ec5c4663a9e961c8e3205d179952f. Its complete review: N/larger_coupling_composition_check/REVIEW.md, f2094c29156d63152bddb4792e27e822902274f4d18b1d1b1f577b85cb949646. That report supplies the exact component source/check hash table and exposure record, also reproduced in the new note and input manifest. The controlling pre-append note hash is d3a48c35bf77a7ee5a084b949ff30573610282b97b88f3ad31bed3f5991894e9.

This acceptance is limited to integration fidelity and the scoped source arithmetic. Inherited supplied-model/kernel/calibration conditions, implementation and physical-identification limits remain. No retained or audit status is assigned. No editable prompt files changed.
