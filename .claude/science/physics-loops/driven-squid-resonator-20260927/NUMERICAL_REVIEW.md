# Selective independent numerical publication review

No consequential numerical or source-mapping defect was found in the inspected candidate. The primary runner reproduces the stated comparisons, its supplied snapshots and measured arrays match their pinned sources, and independent direct-basis checks support the newly packaged alignment path. This is a selective code/claim review, not an audit verdict, optimizer validation, empirical exclusion or merge authorization.

Reviewed branch: physics-loop/driven-squid-resonator-20260927; checkout HEAD during review e37967e326c2bdb429bd3106d34158bd5420e9c0. The new source was reviewed as working-tree content; hashes below define the exact revision.

## Complete source and data checks

I read the complete primary script and note, all input/provenance JSON fields, and parsed and compared every measured signal/axis value in measurements.json. All20×55 signal entries,20 flux coordinates and55 frequency offsets are identical to the corresponding reserved columns of the archived resonator_maps.npz. Both packaged-input hashes validate. All13 historical-source hashes in provenance.json match the accessible historical originals.

The two driven snapshots exactly match both completed driven_calibration.json rows. All six alignment snapshots match all six source rows, including their flux_offset and start_delta fields, without selection by evaluation residual. The drive_reference matches the historical older ng0 calibration snapshot. It is deliberately distinct from the driven snapshots; the note's reported6.181683MHz result is attached to that reference, so there is no unnoticed mixing of calibrations.

The nominal calibration indices and reserved indices are disjoint; reserved indices are exactly10,30,...,390, zero-based. The packaged extraction reproduces the prior per-column Lorentzian/Gaussian objectives, units and bounds. Physics predictions do not enter either extraction fit. The MHz-offset array is divided by1000 to form GHz, then residual GHz differences are multiplied by1e6 for kHz. The historical source-review packet separately verifies the published MHz axis and7.6918GHz reference; that reference remains distinct from a verified bare-resonator measurement.

The current runner supplies snapshots and re-extracts evaluation centers; it neither reconstructs raw calibration nor validates optimizer termination, stationarity, finite-difference stability or uncertainty. The note explicitly says so. The older undriven objective behind the alignment snapshots, retrospective addition of the alignment coordinate, and absence of confidence interpretation are also correctly disclosed. The prior independent optimizer-related review remains limited and must not be upgraded by this successful propagation run.

## Matrix, quadrature and displacement checks

The assembled first-neighbor charge coefficient is−(J_left+J_right exp(−i2πf))/2; the second-neighbor coefficient is(J_left²+J_right²exp(−i4πf))/(8EL), consistent with the stated real potential and its cosine1/2 factor. The ng-dependent charging diagonal is retained. The n cavity operator, positive P=i(a†−a), and drive X=a+a† preserve the previously checked orthogonal quadratures. Largest bare-overlap labels use flattened indices0,1,K for ground,cavity,device excitation; the added collision check is appropriate.

The pulse-area expression is unchanged and dimensionally consistent in cyclic GHz/ns. Displaced sideband diagonals use E+mw; the upper sine harmonic is+iFQ/2 and the lower−iFQ/2. The positive F=2GDw/(Omega²−w²), scalar mean and periodic-displacement derivation match the previously independently checked construction. The note preserves the infinite-oscillator versus finite-cutoff distinction and does not equate absolute quasienergies after scalar removal.

Sorting the two selected eigenvalue indices is sufficient because eigh returns ascending eigenvalues. The local projector-based pair selection remains a diagnostic, not globally tracked branches or a general guarantee of a unique minimum. In the scoped reference case its agreement with the historical continuous-time result remains valid. No new general branch-continuation claim appears in the note.

## Execution and selective independent changed-path test

Ran the complete publication runner with OPENBLAS_NUM_THREADS=1; it exited successfully with empty stderr. Full output is preserved in independent_publication_runner.json. It gives:

- Nominal RMS:36.452834893 and37.235061957kHz.
- Maximum shape-center change:2.641536834kHz.
- Drive amplitude:.835539183460559GHz; Rabi matrix:.004626167490906795.
-40/4 avoided-gap shift:6.181685612011378MHz.
-70/6 avoided-gap shift:6.181682974173874MHz.
- Alignment column50 range:113.265075..113.615047kHz; column250 range:17.177671..28.978532kHz.

These agree with the note's rounded statements. The nominal four large-residual values agree with the preserved independent direct charge–photon calculations; that evidence and its source identities were reused rather than recomputed unnecessarily. Likewise the drive result agrees with the independent historical one-period ODE anchor6.181682972797198MHz. Both historical checks used shared physical inputs and knew the author outputs, as the note honestly states.

For the new alignment propagation, independent_packaging_check.py constructs the real potential by phase quadrature and diagonalizes a direct charge⊗photon matrix (N24,K7), retaining all charge states rather than a24-device-eigenstate projection. It independently labels ground and cavity states. At column250, all six snapshots use the supplied flux+flux_offset convention; their shifts agree with the publication routine within .000069Hz. The lowest selected overlap is .998991. Full mapping checks and all six numerical comparisons are preserved in independent_packaging_results.json. This verifies this changed path at one consequential column; it is not a repeat of all160 cavity points or a proof of alignment calibration quality.

## Anchor honesty and limits

The hard-coded residual and monodromy values are explicitly labeled numerical regression references. They are not used to generate the predictions, fit parameters, select snapshots or extract centers. They do reject numerical departures beyond their stated tolerances. A1Hz residual tolerance and20Hz drive-anchor tolerance are implementation checks, not empirical uncertainty or error certificates. Their known values cannot independently prove the model: the primary calculations and the distinct prior/direct constructions provide the relevant numerical evidence. No new mutation runs were needed for this review; no mutation coverage is claimed here.

No change of physical scope is introduced by packaging. The note retains ground-state preparation, drive transfer and avoided-gap-to-line-center assumptions, the relative-axis control's retrospective status, source imports, and the missing dissipative observable bridge. The six alternate snapshots do not establish a measured flux offset or select a physical mechanism. The physical source supplement, historical direct scripts and optimizer are not runtime dependencies, as asserted; they are provenance, not automatically revalidated by running this packet.

One optional clarity improvement: emitted alignment rows omit start_delta even though all six starts are supplied. The rows are recoverable by input order and their distinct offsets, so this is not a numerical defect; retaining start_delta would make each output's lineage easier to inspect.

Only this review and independent checking evidence were written. No author source/data, calibration parameters, audit status, commits or other checkouts were modified.

## SHA-256 identities

- `scripts/driven_squid_resonator_2026_09_27.py`: `27da3ab028375f10aa3c78549e5a6607917a70eabb894ff6620ca64153ad9c28`

- `docs/DRIVEN_SQUID_RESONATOR_COMPARISON_OPEN_GATE_NOTE_2026-09-27.md`: `444a419264f234435ff95ffb6668c58a0f51013fb2469c24b757993a0b6febff`

- `data/driven_squid_resonator_2026_09_27/inputs.json`: `baf26b54105765b5c3833f668a74273247df1cb13c06d016f1d9b0c4a4022bbc`

- `data/driven_squid_resonator_2026_09_27/measurements.json`: `678a41d986c92b925b9f0661575c9ed0ec5c282558a6ed3db48102df80189e99`

- `data/driven_squid_resonator_2026_09_27/provenance.json`: `92734babc2ae0840ecc74ca21991fd25b4e2943c28a7d281a4a3ca29f2bde712`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/HISTORICAL_DISPLACED_FLOQUET_REVIEW.md`: `10a5f745d3f1042b2f197910ed402c0e5b6686c2d6cad556736759f287e96879`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/HISTORICAL_UNUSED_RESONATOR_REVIEW.md`: `0e6c1a726e11fc3ac0c6541891803d2c536ed767d80385ba28b5fb857857f88e`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/HISTORICAL_UNUSED_RESONATOR_SOURCE_REVIEW.md`: `ca172d8422babc54a34eac30fa1286c4ab07e23f0c81d59c2315a6bcd2f49fd0`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/independent_packaging_check.py`: `3132936d2e30076a0cf8101f6f29fb81a196ab8d00fff6454a1ad8a697063b5a`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/independent_packaging_results.json`: `65cc71c8c4a03eb851025eb167cd04dd0bb1048a22459072da748d1125e6df0f`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/independent_packaging_check.log`: `65cc71c8c4a03eb851025eb167cd04dd0bb1048a22459072da748d1125e6df0f`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/independent_publication_runner.json`: `784f166e79dc447de840be6b9cbf7aef0525d08ca16257af984125102a66ba16`

- `.claude/science/physics-loops/driven-squid-resonator-20260927/independent_publication_runner.stderr`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`


## Narrow follow-up: self-contained independent helper

Reviewed only the requested packaging deltas: the clarified “no circuit-parameter refit” docstring, start_delta output lineage, new driven_squid_independent_2026_09_27.py, its primary import and AUDIT_INPUT_PATHS declaration, six column250 comparisons, independent mutation, and corresponding execution paragraph. The helper preserves the independently constructed real-potential phase quadrature, direct finite charge⊗photon Hamiltonian, orthogonal photon momentum coupling and bare ground/cavity overlap labels from independent_packaging_check.py. It imports no primary builder or empirical extraction. The added collision assertion is appropriate. The original local lineage-check script remains historical evidence, not a runtime dependency.

Re-ran the final primary successfully; all six independent differences match the prior checks, with maximum absolute difference .00006838973831691Hz. All alignment rows now retain start_delta. Ran --mutation independent separately: it exited1 at the intended “Direct-basis independent comparison failed” exception, after an injected .000001GHz (1000Hz) discrepancy. This verifies the new1Hz comparison gate discriminates that fault; it is not a general mutation campaign or proof of the physical model. No new consequential finding. Earlier scope and physical/optimizer limitations remain unchanged.

The following hashes supersede the earlier primary/note identities for this follow-up; data identities are re-recorded to make the final closure explicit. Only review/evidence files were written.

- `scripts/driven_squid_resonator_2026_09_27.py`: `e133dd6a6099fadfdd870bb8405a5295b72269a07977ad7cd686a3041f3854d3`

- `scripts/driven_squid_independent_2026_09_27.py`: `ad751dac5a8b91829d9f88ba65d37a886d307ff3714bcaff4b2eb6fced76a93a`

- `docs/DRIVEN_SQUID_RESONATOR_COMPARISON_OPEN_GATE_NOTE_2026-09-27.md`: `8ab9e05364bbe3d3c53c3ad52933c61257bb11917af047cfb53a6a956af52a1c`

- `data/driven_squid_resonator_2026_09_27/inputs.json`: `baf26b54105765b5c3833f668a74273247df1cb13c06d016f1d9b0c4a4022bbc`

- `data/driven_squid_resonator_2026_09_27/measurements.json`: `678a41d986c92b925b9f0661575c9ed0ec5c282558a6ed3db48102df80189e99`

- `data/driven_squid_resonator_2026_09_27/provenance.json`: `92734babc2ae0840ecc74ca21991fd25b4e2943c28a7d281a4a3ca29f2bde712`

- `independent_final_runner.json`: `ff0fe3e75c46081172a063a91a3189b34cc275395f5ef1e20c9a8c118079080e`

- `independent_final_runner.stderr`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

- `independent_mutation.stdout`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

- `independent_mutation.stderr`: `56f85271183193021e28cf136095d252e90626441b0ded2f9609649ff5fa1b45`
