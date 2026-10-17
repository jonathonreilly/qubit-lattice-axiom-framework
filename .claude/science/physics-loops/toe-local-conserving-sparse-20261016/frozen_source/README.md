# Source-only sparse compiler publication proposal

Start with [THEOREM_NOTE.md](THEOREM_NOTE.md). It presents the accepted fixed-q conditional result together with the later qualified fixture evidence. The [seven-body recovery map](BODY_RECOVERY_MAP.md) links every complete immutable argument/review/qualification; [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) maps all originals and copied bytes.

- [PROVENANCE.json](PROVENANCE.json): strict primary status UNBOUND; no actual canonical parent, Git base, current wrapper review or publication.
- [EXPOSURE_AND_SCOPE.md](EXPOSURE_AND_SCOPE.md): review coverage, historical pending statements and evidence limits.
- [EVIDENCE_MAP.json](EVIDENCE_MAP.json): exact old execution sources, launchers, failure, streams, words and matrices.
- [PR_BODY.md](PR_BODY.md): proposed description only; no PR has been created.
- [CHECKPOINT.md](CHECKPOINT.md): final source-packet checkpoint, written by the sealer after metadata checks.
- [FREEZE.json](FREEZE.json): final exhaustive inventory; no writes follow this seal.

Seven selected immediate freezes are copied, including their embedded source captures. This bounded closure contains 131 files and 10,367,578 bytes. Three additional history records preserve the old publication review and old seal; the prior publication archive is not recursively copied. Broader historical citations are not claimed fully archived. Original source paths in historical receipts stay literal; the manifest gives their packet recovery paths.

The read-only validator defaults to exit 2 with UNBOUND. Explicit `--source-only` checks bytes and returns 0 when valid. It cannot accept a future binding, update source, run science, inspect Git or publish. From this directory:

    python3 -B verify_provenance.py --packet-root .
    python3 -B verify_provenance.py --packet-root . --source-only

The final validator checks exact top-level inventory, including nested source seals and all saved execution artifacts; only this packet's root FREEZE.json is excluded from its own member set. Source verification is not scientific certification. Actual packaging invocations and complete streams are in `runs/metadata_checks/`; no science is rerun.
