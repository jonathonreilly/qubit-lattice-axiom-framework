# Portable implementation handoff

Implementation complete in isolated checkout microscopic-transmon-review, branch physics-loop/microscopic-transmon-20260927, based on e37967e326c2bdb429bd3106d34158bd5420e9c0. No commits, pushes, authority edits, optimizer reruns, raw extraction reruns or full integration/audit pipeline were performed. Parent owns the note, review/closure pack and release decisions. No editable prompt files changed.

## Files and runtime contract

- scripts/microscopic_transmon_2026_09_27.py: primary spectral reconstruction and supplied-snapshot comparator, explicit600s timeout and complete literal input closure.
- scripts/microscopic_transmon_independent_2026_09_27.py: independent spatial/phase quadrature and full charge-photon helper, imported and executed by primary.
- data/microscopic_transmon_2026_09_27/: all8 source-version,12 raw-transfer and12 ablation snapshots; both model protocols; calibration ledger, exact archived input records and processed01 source row; processed03 exact timestamp/source fit errors and three raw03 center snapshots; single-junction cosine controls; independently checked pair regression anchors; provenance hashes/URLs.

All runtime reads are repository-relative and included in AUDIT_INPUT_PATHS. Package data hashes are verified before use. No outside/ignored science dependency is read. The raw source archive URLs are provenance references, not runtime network inputs: https://zenodo.org/records/10728469 and its Krause2024_Quasiparticle.zip file. provenance.json records the archive SHA and exact upstream local snapshot/source hashes and included-file hashes. The upstream calibration/extraction fits are supplied local reanalyses, not mislabelled as published author results. Data sizes are below40kB per file.

## What executes

The primary checks exact32 keyset, status/success, finite physical parameter bounds and fixed constants; calibration vectors against the included independent data ledger; reconstructed endpoint spectra against each supplied fit; calibration residual/cost reconstruction; all12 matched ablation differences; three cosine ablation identities and both source-version cosine scale maps to prior one-junction controls. Selected raw_period_0.3/.01 spatial and ablation parameters are reconstructed independently at22charge/12photon and28charge/16photon cutoffs, with direct spatial/phase quadrature. Historical independent anchors are explicitly regression evidence and are also reproduced, not substituted for the independent construction.

All32 full f03 center/full endpoint dispersion comparisons are emitted against the processed03 target; all32 center comparisons are also emitted against every raw03 center. Targets load only after calibration/spectrum checks. There is NO raw03 dispersion statistic. Empirical residual proximity never determines a PASS. Pass/fail concerns implementation, input identity and selected numerical consistency, not experimental acceptance, source-analysis validity or theory status.

## Actual commands and results

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/microscopic_transmon_2026_09_27.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/microscopic_transmon_2026_09_27.py --mutation FAMILY
```

Run from the checkout, FAMILY in data,split,normalization,field,coupling,independent. Canonical standalone execution exits0 with TOTAL: PASS=155 FAIL=0. Each mutation exits1 at a real affected check; none is converted to green. These external stdout logs are execution evidence, NOT canonical runner-cache envelopes. Parent should produce any required canonical cache with scripts/runner_cache.py after final note/input closure is frozen.

- `portable_runner.log`: exit0, 1.369s, SHA256 `a522969cc8da7dc1cf1ef70ddef650247eedf83a03f818a98dae99aaf6e25bbe`; final `TOTAL: PASS=155 FAIL=0`.
- `portable_mutation_data.log`: exit1, 0.232s, SHA256 `d51bbff179d21a0ed359d853a15fbadb223e92a1a3643c05cc544ca9405ff23a`; final `TOTAL: PASS=0 FAIL=1`.
- `portable_mutation_split.log`: exit1, 0.255s, SHA256 `b68b7578f0ddef8836b0391de4d071d71ce048b91a86ecb3bfe2e201cb76d896`; final `TOTAL: PASS=0 FAIL=1`.
- `portable_mutation_normalization.log`: exit1, 0.249s, SHA256 `b68b7578f0ddef8836b0391de4d071d71ce048b91a86ecb3bfe2e201cb76d896`; final `TOTAL: PASS=0 FAIL=1`.
- `portable_mutation_field.log`: exit1, 0.261s, SHA256 `47e0ba514ed5db28dd26e232e2986a17b4dd76bc673b64287f9de657169bf100`; final `TOTAL: PASS=0 FAIL=1`.
- `portable_mutation_coupling.log`: exit1, 0.246s, SHA256 `b68b7578f0ddef8836b0391de4d071d71ce048b91a86ecb3bfe2e201cb76d896`; final `TOTAL: PASS=0 FAIL=1`.
- `portable_mutation_independent.log`: exit1, 0.595s, SHA256 `abc1f2ea096581799654a6a8af9093a952248fe6cf2a3a5d5b20cccf789ebd90`; final `TOTAL: PASS=0 FAIL=1`.

Mutation behavior: data corrupts read bytes before hash verification; split divides full dispersion by two; normalization doubles the local potential; field drops m dependence; coupling changes G by10%; independent perturbs the independently reconstructed f03 by10kHz. Each is detected against an unaffected reference or source invariant. Numerical consistency thresholds are10Hz for spectra/independent checks; actual selected independent differences remain around10^-3Hz, not a physical precision claim.

Limits: supplied stationary-center/parity and geometric premises, cross-acquisition constants, source-version ambiguity, finite-dimensional approximations, retrospective model choice, fit termination/local basins and missing systematic uncertainty remain explicit. Snapshot optimization and source extraction are not certified by this runner. The helper is independent in construction, but authored packaging and its checks still need final independent source review. Parent note/source factual claims may need additional provenance records; no release/audit verdict is granted here.

## Exact final file hashes

- `scripts/microscopic_transmon_2026_09_27.py`: `f24a77c599da768b82a26240871ae58a1c798937ffc95201277c8b969f73bcb6`
- `scripts/microscopic_transmon_independent_2026_09_27.py`: `2fddf6f97495fdfcda12a6b51814a5a9f1cb24600e94e8fcd9cfb4ade9599066`
- `data/microscopic_transmon_2026_09_27/HARMONIC_ABLATION_PROTOCOL.md`: `25e6fd73b2debf7af248f525b95b91ae53bec138767b1e8668836b15a410c89a`
- `data/microscopic_transmon_2026_09_27/PROTOCOL.md`: `d5d6ffc5674ccd62e5468c29e9980a55dbcc74927120548d391ad3c82afce061`
- `data/microscopic_transmon_2026_09_27/calibration.json`: `2e80a3646f6a2527a62c208ce31ccbc3258eb796ac5452dbd009be698d5b5f1b`
- `data/microscopic_transmon_2026_09_27/cosine_control.json`: `19311d798ff3c017bc269d790b37217dc4cac00dc41761a84a16775da13e3f88`
- `data/microscopic_transmon_2026_09_27/fits.json`: `1db744ff5ff43d6165f1ae7dfec5a49911be64e413ecfd7addb7d09fc9615786`
- `data/microscopic_transmon_2026_09_27/harmonic_ablation_fits.json`: `fca3770298f91ed7cc158c811fba8fe44c567bd2b946111187f44a72fe60ee9d`
- `data/microscopic_transmon_2026_09_27/independent_anchors.json`: `3e9df2e7e2067c8800cb3267f3689fcb081d4474f1c32d6e19461094e8f007ea`
- `data/microscopic_transmon_2026_09_27/provenance.json`: `d341acbde8ea55b450d57a4e72e85df62ca73ddc88537500372eb871f61fbd96`
- `data/microscopic_transmon_2026_09_27/raw_transfer_fits.json`: `5b25bc09c09331c1683e6cb4b2aa62fdecd45f52bc9e7864a04dbedf8a672491`
- `data/microscopic_transmon_2026_09_27/targets.json`: `66401169f1b76bc4813019f0e3247227f6fc793033404146ea440c306d00e084`

## Narrow pre-freeze corrections

Read both complete portable scripts and made only the requested changes: sorted raw-case iteration, explicit600s helper timeout, explicit ValueError for duplicate independent labels (not disabled by python -O), and emitted scientific-versus-integrity read inventory. The helper has no data-provenance hash pin; its changed source is included directly in AUDIT_INPUT_PATHS. No data or numerical algorithm changed.

Final runner again exits0 with155 checks; all six mutations again exit1 at their affected checks. PYTHONHASHSEED=1 and913 executions both exit0 and have byte-identical stdout, SHA256 `a522969cc8da7dc1cf1ef70ddef650247eedf83a03f818a98dae99aaf6e25bbe`. Evidence: portable_hashseed_1.log, portable_hashseed_913.log, portable_determinism_results.json; all mutation logs and portable_execution_results.json refreshed. These remain external execution logs, not canonical cache envelopes.
