# Distinct check: common-mode traveling and synthesis interface

Verdict: conditional support; no necessary correction found. The physical-moment replacement, ordered outgoing comparison, wrong-window terms and same-offset nominal synthesis are valid within the cited background and inverse premises. The source does not establish a time, halfline concentration or complete-performance point.

Target: `three_site_common_mode_traveling/PROPOSAL.md`, SHA-256 `0abafe7b46fe6c93df110df8bc1e7a9dbc3a4eca30d38dbdea619337ca75940d`. The complete target and the complete perturbed outgoing source were read/refreshed. All target pins and the additional local/core review pin below were verified.

## Physical reference measure and row transfer

The scalar first application about the original physical carrier has seed diagonal Delta+r0 and first bond -a1. Its exact second moment is therefore (Delta+r0)^2+a1^2. Equivalently the mean and second moment in y are r0 and r0^2+a1^2, and translating delta=y+Delta adds both 2Delta r0 and Delta^2. Equation (1) retains these terms. Using merely the recentered variance here would be invalid because the processor error envelope depends on physical delta.

The isolated scalar measure is normalized by the checked common-mode result. Common transmission with its exact Jacobian is contractive, so the retained transmitted second moment is at most this full physical second moment and 0<pe<=1. The retained band remains |delta|<=d. No loaded actual density is substituted for that scalar comparison measure.

Source compression leaves the background and preconnector row exactly unchanged. The row -kappa a1a2 Ltilde Q^-1 follows from the actual last-source column and retains the order. From Q^-1=(I-Kload)^-1 Qref^-1, the selected reference factor acts first as P/q_e,Delta. Expanding the left Neumann factor gives the relative error eN+j||Ltilde||Theta/(1-Theta). Since j<.003 and ||Ltilde||<461, the ceiling 1.384 is valid and independent of the source ratios. The selected ideal coefficient has the same numerator sign, reference plane and physical propagation phase; only its exact scalar determinant and source numerator change. Its load remains m_j(delta), not m_j(delta-Delta).

Minkowski and Fourier isometry then give the displayed Esel: the floor and Neumann terms cost sqrt(pe), and the physical linear-energy term costs sqrt(m2_phys). The estimate may be coarse when Delta dominates lambda, but it is valid. No old emitter-coupling cap or nominal Theta is silently reused.

## Wrong windows and conjugate incoming wave

For wrong-window input Qref^-1 C is bounded by 170 before the left Neumann correction mixes its output. Combining ||Ltilde C||<2e-23 with the full row bound 461 gives the displayed Bwrong. It includes the selected output generated from complementary input, rather than discarding it. The unchanged physical derivative ceiling .006 and retained q-width produce Ewrong=.006 Bwrong sqrt(2h) with the existing two-window Fourier aggregation. The old-input combination sqrt(2)Esel+Ewrong is the same full-input convention as the checked outgoing premise, while parity and record-X sectors combine orthogonally. The actual physical energy label on each wrong window is retained.

Real source detunings preserve the qualified real sector structure. Stone conjugation acts on fixed coefficients; it gives the incoming scalar conjugate and W*, retaining the SAME exp(-itE) factor. It does not conjugate an arbitrary old/reference state or require the ordered lower Q to equal the upper Q's adjoint. Fourier restriction to the physical ray is contractive, so each traveling coefficient discrepancy costs Eraw. The two waves share physical coordinates and their errors must be added; the proposal correctly pays 2Eraw.

## Same-Delta nominal replacement and complete accounting

At fixed supplied Delta, zeroing residuals defines a single nominal complex coefficient. Both physical windows have the same shifted scalar function after extracting their actual old-energy carriers, since the source offset and residuals multiply the full internal identity. The scalar relative bound survives the unchanged transmission, phase and Jacobian. It gives raw error L sqrt(p_Delta,0) for each wave. The common ideal scalar replacement introduces no extra old-energy multiplier, and both waves together cost 2L sqrt(p_Delta,0).

There is no normalization by pe and no fit to the perturbed waveform. The target is the nominal packet at this Delta, not the zero-offset packet. Reexpressing a physical spectral integral in y introduces exp[-it(2j+Delta)] exactly once; adding it again to an already physically evolved packet would be wrong. The proposal explicitly forbids that double count. c_att, literal W and exp(-itK) remain in the final target.

When the nominal outgoing physical-halfline norm r_Delta,0 is positive, normalizing that raw packet costs exactly 1-r_Delta,0 because r_Delta,0<=sqrt(p_Delta,0)<=1. Discarding its incoming partner costs its raw norm. Combining these with represented source/background and the traveling bounds proves (5), for the times on which the cited S and B apply (in particular t>=0 for the displayed local/core envelopes). There is one actual omitted-state charge, and the distinct scalar reference truncation is already in S. No source escape estimate is used to infer incoming smallness or target normalization.

The frozen source's local/core dependency was labeled provisional at authorship. Its exact e817e63d argument now has review `644e29302a077f72e940c7396c562bf1ba87a5741f60a66c86dc7f6899972d77`, supporting the stated interfaces without correction. This supplies the recorded selective check; it is not an additional independent check by this same reviewer. The complete synthesis remains conditional on those physical and inverse hypotheses and on any separately needed scalar halfline bounds.

A compatible output-only finite-cut theorem may be added because source offsets lie in the zero-weight region, but this does not choose M or time. The optional seven-block global scalar is algebraically distinct from the source-only Delta and must multiply both actual evolution and target if adopted. Neither optional observation supplies performance here.

## Exposure and limits

Root authored this extension and its perturbed outgoing predecessor. I authored attachment and traveling/reference ancestors and checked the common-mode scalar, actual and local/core interfaces. This is a distinct examination of the new composition with shared ancestry disclosed, not blind independent recertification of those ancestors. The changed physical moment, full row factorization, wrong-window handling and raw-versus-normalized accounting were reconstructed directly.

No useful-time, finite-receiver complete bound, zero-offset-target robustness, arbitrary-noise tolerance, native supply or permanent halt follows. No numerical dynamics, integration, sweep, scientific runner, Git/publication/checkpoint action, prompt/model change or delegation was performed. Only this review was written, with deterministic hash verification.

## Exact source identities

- `three_site_common_mode_source/PROPOSAL.md`: `5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb`.
- `three_site_common_mode_source_check/REVIEW.md`: `af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb`.
- `three_site_common_mode_actual_interface/PROPOSAL.md`: `9225b6ea6533dea56db4f8b7157deac5c6f52e5927b554052c59299622a13957`.
- `three_site_common_mode_actual_interface_check/REVIEW.md`: `e9b32196906e1d4b5010ac9b30d348e438d6e88fcdac82d51ae107f3f7ba1cea`.
- `three_site_common_mode_local_core/PROPOSAL.md`: `e817e63d7b6e7d1ba7d87db2322b8b5b7dd88b028fdbdd59962d4c3898713dcf`.
- `three_site_perturbed_outgoing/PROPOSAL.md`: `b5dedac09f31e7b78f12142abaf42ac4294d33190e23f4330e9bc5df8f9dbf2b`.
- `three_site_perturbed_outgoing_check/REVIEW.md`: `d3fc5b78ffd66efab9839a965072109bb843f213ac3111156576b8f9d002e38f`.
- `three_site_outgoing/PROPOSAL.md`: `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`.
- `three_site_outgoing_check/REVIEW.md`: `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- `three_site_traveling_interface/PROPOSAL.md`: `75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3`.
- `three_site_traveling_interface_check/REVIEW.md`: `9cb7655b688a61ce32b950f2d95024762023770380a6e5df8afaa1939744230a`.
- `three_site_common_mode_local_core_check/REVIEW.md`: `644e29302a077f72e940c7396c562bf1ba87a5741f60a66c86dc7f6899972d77`.
