# Corner Dirac follow-up: historical recovery and correction record

PR #9689, frozen head `06b8f42d9bbf956763f5a3ea90d0992d0e67b145`.
This is historical source recovery, not a new canonical scientific claim or an audit verdict.
The current canonical corner-model Weyl/Dirac note and runner remain unchanged.
The submitted exploratory scripts, logs, serialized inputs and report are retained exactly;
the report's claims and PASS labels are not adopted by storing them here.

## Material corrections to the historical report

- A vanishing first-order node projection does not establish finite-strength node persistence or exclude higher-order shifts. Translation-breaking operators also require a different formulation from Bloch nodes.
- Sampled ranks remain lower bounds unless completeness is separately proved. Projected first-order mass linearity is not exact finite-strength linearity of globally sorted levels; the recorded larger-strength selection tests reorder bands.
- The four rounded indirect-gap ratios in `independent_check/touch2.log`, divided by the reported `2m_D`, are approximately 0.216, 0.229, 0.231 and 0.110. The submitted 0.22–0.46 range is incorrect. Positive sampled or locally optimized gaps are upper estimates of the true global indirect gap, not certified positive global gaps. Failed finite searches do not prove a vacuum obstruction.
- The A2 averaging check in `independent_check/realspace.py` first averages its seed into the trivial character, then projects onto a nontrivial character. The resulting zero is predetermined and cannot test general A2 perturbations.
- Untwisted momentum-Q invariant pairing operators exist in the recorded operator enumeration. Restrictions on their projected node blocks must not be stated as nonexistence of the operators.
- `touch.log` lists 22 candidates and `touch2.log` lists 18 flux-tested candidates; a complete count of 24 is not certified by those records.
- The globally sorted “upper doublet” in `realspace.log` has dimension six. It cannot certify an isolated massive doublet; the separately selected nearby subspaces require their own scope.
- Three listed route families do not constitute a passing complete negative-claim packet. No exhaustive exclusion is adopted.
- `ideal3.py` loads the untracked `Xbasis.npy` through `diraclib.py`. The tracked producer `dirac1.py` writes only six basis seeds. The claimed nine-dimensional optimization has no supplied reproducible array closure. `dump_runner.py` also contains a stale machine-local path; serialized inputs are historical data, not current validated inputs.

## Deferred scientific work

The packet contains candidates for signed-orbit operator dimensions, an inversion-parity decomposition, a cube-centred spinorial lift, and projected pairing-block witnesses. Their live promotion requires portable, explicitly pinned input closure, independent decisive controls, and claims restricted to the demonstrated operators and subspaces. These obligations remain open; archiving does not complete them. Preserve the original PR branch as a recovery handle for the deferred work.

## Recovery

`archive-manifest.json` maps the complete frozen `c19_dirac` directory, including inherited helpers, to exact gzip objects by raw SHA-256 and original Git mode. `original-pr-extra-paths.json` additionally preserves the submitted canonical-note proposal and campaign state. Decompress an object's `stored_path` and check its raw hash before restoring its `original_path` into a separate recovery directory. Do not execute pickle deserialization merely to inspect this history. The absent original `Xbasis.npy` cannot be recovered from this tree.

All original scientific source is recoverable; no historical report supplies authority over the corrected canonical source. No existing main path is replaced by this addition.
