# Reproduction and portability

Use Python 3.12.8 and SymPy 1.14.0 to reproduce the byte-identical receipts.
A different version can change receipt metadata even if all identities
still pass. Each scientific subprocess was bounded at 120 seconds and used
both -B and PYTHONDONTWRITEBYTECODE=1.

Work in a disposable byte-for-byte copy of this evidence folder. Do not
rerun writing wrappers inside the closed original bundle. Existing attempt
names are protected against overwrite.

The final integration checker accepts a repository root explicitly:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B check_canonical_integration_v2.py \
  --source-root "/absolute/path/to/standalone/repository" \
  --attempt canonical_reproduction01
```

That root must contain the exact final note, primary, helper, result receipt
and citation-extractor bytes in CANONICAL_SOURCE_SNAPSHOT_v3.json. The checker
copies author sources into its own attempt repository, replays them there,
observes repository reads, performs isolated extraction and compares the
result to the pinned receipt. It never runs the primary in the supplied
source repository. Earlier snapshot/replay versions remain historical.

The original independent and original-author wrappers resolve the original
hierarchy:

```text
<repository>/.claude/science/physics-loops/
  observations-backward-derivation-24h-20261015/
    independent_non_equilibrium_scalar/
```

Their source bytes were not edited for portability. The exact original
author artifacts required in the parent pack are preserved as UTF-8 content
in AUTHOR_ORIGINAL_EXPOSURE_v1.json. A fresh materialized hierarchy can run
run_independent_bounded_v1.py and replay_original_unit_bounded_v1.py; omit
prior generated attempt files in that disposable run directory. The root
author plans a generic materializing wrapper outside this bundle. That
wrapper is not supplied or independently checked here.

The post-exposure independent_additions_v1.py does not read repository
files. run_additions_bounded_v1.py resolves only its sibling program and
captures a bounded execution in a fresh copied directory without an existing
additions_attempt01 record. Neither independent implementation imports the
author mathematics helper.

The metadata_snapshot_attempt*.py files are preserved one-shot packaging
history, not replay entrypoints. Their absolute canonical source path is
intentional evidence of the original operation. Do not rerun them to modify
or repin a closed bundle.

Every scientific execution's full argv, working directory, environment
flags, duration, return code, stdout/stderr hashes and source bindings are
saved in its *.run.json. MANIFEST_v1.json binds all files except itself;
its own digest is provided in the completion message.
