# Reproduction

Use Python 3.12.8 and SymPy 1.14.0 for the recorded byte-identical results.
All programs are portable within a copied evidence directory. Source-root
reads resolve against the explicitly supplied --source-pack. No scientific
program imports author code into the independent calculations.

Work in a disposable copy of this directory and choose fresh attempt labels;
the frozen evidence must not be overwritten.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B run_independent_bounded_v1.py \
  --attempt independent_reproduction01

PYTHONDONTWRITEBYTECODE=1 python3 -B run_author_comparison_v1.py \
  --source-pack "/absolute/path/to/campaign/pack" \
  --attempt comparison_reproduction01

PYTHONDONTWRITEBYTECODE=1 python3 -B replay_witness_bounded_v1.py \
  --source-pack "/absolute/path/to/campaign/pack" \
  --attempt witness_reproduction01
```

The author-source paths must match the literal lists and exact pins in
AUTHOR_SOURCE_SNAPSHOT_v1.json and AUTHOR_REVISION_SNAPSHOT_v2.json.
Those containers include complete source and receipt UTF-8 bytes, so the
original source hierarchy can be materialized in a disposable directory
without changing any frozen code. The witness hierarchy includes
independent_matter_clock/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md.

The comparison launcher runs the post-exposure formula correspondence program
and the unchanged primary in separate subprocesses. The witness launcher
copies its three required inputs before execution. Both compare complete
stdout bytes with the recorded author receipts. Each subprocess uses -B,
PYTHONDONTWRITEBYTECODE=1 and a 120-second timeout, preserving stdout/stderr,
timings, return codes and before/after source bindings.

The primary receipt binds note v1; the supplementary witness receipt binds
note v2. The independent pre-exposure record is kept distinct from both.
MANIFEST_v1.json binds all evidence files except itself; its own digest is
provided in the completion message.
