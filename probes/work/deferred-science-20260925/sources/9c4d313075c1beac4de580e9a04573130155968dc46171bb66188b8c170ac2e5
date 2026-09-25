# Released-source POST command and evidence record

1. Read both released root seal JSONs and verified their supplied SHA256 values.
2. Verified and snapshotted the 11 author-seal members, its seal, the range
   supplement member, and its seal: 14 files in `POST_sources/`. Saved exact
   original/snapshot paths, hashes, and byte counts in `POST_SOURCE_PINS.json`
   and matches in `POST_SOURCE_VALIDATION.log`.
3. Read the complete Fisher candidate and range supplement. Compared them with
   the immutable PRE. Read both complete author program versions, both complete
   result JSONs, stderr logs, and source records. An overlong display of the
   combined read was truncated; affected material was then read in smaller
   complete batches. No truncated display is counted as completed verification.
4. Parsed every byte of both stdout streams as four JSON objects. The first
   three objects match every cube row of the corresponding result JSON, and
   the fourth equals the complete result. `POST_AUTHOR_EVIDENCE_PARSE.json`
   records correspondence and complete stderr contents. Inspected both result
   JSONs in full. The first author run has dtype future warnings, not failed
   assertions; the final run has empty stderr.
5. Revisited the necessary sections of the unchanged, previously fully read
   model sources via text search. No unreleased root packet or additional
   literature was opened. No author or campaign builder was imported or run.
6. Wrote `post_coherence_checks.py` from finite matrix algebra without importing
   PRE, campaign, or author code. Before its first execution, removed an unused
   vacuous compatibility assertion; it is not counted as a check. Executed once
   using `/opt/homebrew/opt/python@3.13/bin/python3.13`, with cwd this directory.
   The process completed in about 0.23 seconds with exit 0. Full stdout/stderr,
   exact source hash and command, result JSON, and runtime version are retained.
   No independent numerical control failed or required a rerun.
7. Wrote POST.md with source provenance, complete proof comparison, newly
   reconstructed POST implications, precise limits, and numerical evidence
   boundaries. The old PRE files were never edited. Revalidated both released
   seals, source originals and snapshots, the 15 PRE members, and the own run's
   source/output correspondence before sealing the new POST packet.

Reproduction of the own check: `python3 post_coherence_checks.py` in this
directory, with Python and NumPy. Outputs from the sealed execution are already
present. Reproduction would overwrite its result JSON, so use a fresh copy to
preserve the immutable seal. No expensive cube computation was reproduced.
