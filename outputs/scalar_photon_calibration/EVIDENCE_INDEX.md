# Evidence and reproduction

The current computation is [the primary runner](../../scripts/scalar_photon_calibration.py), its four imported helpers and [the source note](../../docs/SCALAR_PHOTON_CALIBRATION_NOTE_2026-10-16.md). It needs no previous campaign checkout, ignored graph file, empirical array or provenance archive. The source/result identities and software versions are in [result.json](result.json); the envelope cache is in [scalar_photon_calibration.txt](../../logs/runner-cache/scalar_photon_calibration.txt).

The four overlapping control units report 48/0, 33/0, 12/0 and 19/0. They are constructed mathematical checks, not independent experiments. The [portable replay](portable_replay_v1.json) copies only the declared six-file closure to a fresh temporary directory and reproduces the complete result byte-for-byte with the same Python/CAS.

## Focused checks

- [Separate-gain comparison](reviews/split_gain_review.md): independent temporal derivation, then exposed characteristic comparison; observed quadratic-fixture derivative extraction 111/0 and general correspondence 20/0.
- [Common-gain robustness](reviews/common_gain_robustness.md): conditioning and the single-shell omission survivor.
- [Independent weak proof](reviews/weak_independent_review.md) and [bounded comparison](reviews/weak_comparison.md): 25 independent controls, unchanged author replay 19/0 and static correspondence 7/0. The loose L1 enclosure and finite-moment limitation remain visible.
- [Initial canonical integration](reviews/canonical_initial_review.md), [weak delta](reviews/canonical_weak_delta.md), and [editorial confirmation](reviews/canonical_editorial_confirmation.md): source-bound scopes, including independent implementations and unchanged-source reuse.
- [Cluster-value decision](reviews/cluster_value.md): one coherent milestone; the weak comparison confirms the appended lemma belongs to it.

These are focused checks, not formal audit or shared landing validation. Readable report copies have only trailing whitespace normalized; [copy provenance](reviews/copy_provenance.json) binds the exact originals.

## Immutable historical evidence

[Source evidence](historical/source_evidence.tar.gz) preserves 346 exact files from the direct derivation and five completed focused checks. Its [manifest](historical/source_evidence_manifest.json) gives every original relative path, byte count and digest. [Integration evidence](historical/integration_evidence.tar.gz) preserves 103 files from source mutations, canonical reviews and their snapshots; its [manifest](historical/integration_evidence_manifest.json) gives the matching identities. Extract each archive into its own directory; original relative relationships are retained. Historical absolute paths are provenance and may be obsolete. The current primary never reads these archives.

Failures remain included: the missing background coefficient, unsimplified reception identities, original timeouts, the reviewer's path-coordinate correction, source-movement guards, bytecode-induced cache identity failure and storage failure. The [first mutation results](mutation_RESULTS_attempt01.json) detected six of seven attempted changes; the incomplete background positive control is retained. Its [consistent correction](mutation_RESULTS_v2.json) restores integrated A as well as coefficients and is detected. The density mutation records physical failed checks before an eigenvector exception. The weak helper has three algebraic mutation controls and its independent check has five. No failure is relabelled as a clean execution.

The supplied action, registered geometry, angular/source contract, smooth positive reception gains and rank remain premises. No action, absolute scale, preferred state or empirical calibration is derived by these controls.

[Packaging evidence](historical/packaging_evidence.tar.gz) preserves the two historical cache versions and previous-base citation snapshot byte-for-byte; its [manifest](historical/packaging_evidence_manifest.json) binds all three. These were moved into the archive after a staged whitespace check flagged terminal blank lines in the historical cache copies. Current source, current cache and scientific results were unchanged.
