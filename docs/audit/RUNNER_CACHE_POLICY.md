# Runner Cache Policy

**Status:** binding for all PRs that modify cached runners under `scripts/` or
any repository input declared by those runners.

## What this is

Every primary runner referenced from a ledger row has a source-identity-pinned
cache file at:

```
logs/runner-cache/<runner-stem>.txt
```

The cache header pins the file to the runner's content SHA-256. A runner that
reads mutable repository files must declare them in `AUDIT_INPUT_PATHS`; its
header also pins a deterministic fingerprint of those files. The audit prompt's
Section 3 uses the cache only while every required identity matches.

The cache is **version-controlled**: cache files live in git on every
branch and are landed alongside the runner change that produced them.

## Why the cache exists

The audit lane's auditor uses the strongest configured full Codex GPT
model at maximum reasoning by default. It judges each claim from a
restricted packet that includes the runner's source code and the runner's
stdout. If the runner or one of its repository inputs changes but the cached
stdout doesn't, the auditor sees a stale picture and may issue a verdict that
doesn't match the current evidence. The cache must therefore stay synchronized
with both its runner and its declared inputs.

A naive "always run live" approach has two costs we explicitly do not
want to pay: long compute jobs (`frontier_alpha_s`, lattice plaquette
sweeps, etc.) would block every audit, and the same expensive run would
happen many times across audits that share a runner.

The same rule applies outside formal audits. Analysis agents should not run
primary runners directly just to inspect stdout. They should use the cache-first
analysis command:

```bash
python3 scripts/cached_runner_output.py scripts/<runner>.py
```

This command prints a fresh source-identity-pinned cache if one exists. If the
cache is missing or stale, it runs the runner once, writes the canonical cache,
and then prints that cached result. Use `--check-only` when analysis must refuse
live execution, and use `--refresh` only when intentionally replacing a fresh
cache.

## Cache file format

```
===== runner cache v1 =====
runner: scripts/<name>.py
runner_sha256: <hex>
input_fingerprint_sha256: <hex>  # present only with AUDIT_INPUT_PATHS
timeout_sec: 120
exit_code: 0
elapsed_sec: 12.34
status: ok          # ok | nonzero_exit | timeout | error
----- stdout -----
<stdout, capped at 200 KB tail>
----- stderr -----
<stderr, capped at 50 KB tail>
```

No timestamps anywhere. The file is purely a function of the captured runner
SHA, optional declared-input fingerprint, and execution result, so re-running
`precompute_audit_runners.py` on an already-fresh cache is a byte-level no-op
(gate-clean).

## Declared repository inputs

A cached runner that reads mutable repository files declares every such file
with a literal top-level tuple or list:

```python
AUDIT_INPUT_PATHS = (
    "docs/SOURCE_NOTE.md",
    "docs/audit/data/source_fixture.json",
)
```

The declaration must be non-empty, unique, normalized, repo-relative, and
contain no `..` segment. It is parsed with `ast.literal_eval`; the cache layer
never imports the runner to discover inputs. An invalid declaration or an
unreadable declared file blocks cache writing. Environment variables, network
responses, machine-local files, randomness, wall-clock state, and other
mutable inputs must be eliminated or explicitly fixtured before a cache can be
treated as canonical evidence.

## Freshness rule

A cache file is **fresh** iff its header `runner_sha256` equals the SHA-256 of
the runner file on disk and, when `AUDIT_INPUT_PATHS` is declared, its
`input_fingerprint_sha256` equals the deterministic fingerprint of the current
path/content sequence. Anything else is **stale**:

| Status         | Meaning                                                         |
| -------------- | --------------------------------------------------------------- |
| `fresh`        | Runner SHA and any required input fingerprint match             |
| `missing`      | No cache file exists for this runner                            |
| `corrupt`      | Cache file exists but the header is malformed                   |
| `sha_mismatch` | Header SHA differs from current runner SHA — runner was edited  |
| `input_mismatch` | Declared inputs are invalid, unreadable, missing from the header, or differ from the current fingerprint |

Every status other than `fresh` requires repair or refresh.

## Policy

Three surfaces keep runner caches fresh without making open PRs noisy:

1. **Pre-commit hook** (`docs/audit/scripts/pre_commit_audit_check.sh`)
   The hook always runs
   `precompute_audit_runners.py --staged-only --check-only`. The selector
   includes staged known runners and reverse-maps every staged path to known
   cached/ledger runners whose `AUDIT_INPUT_PATHS` contain it. The hook blocks
   if any selected cache is stale. The developer's fix is to run
   `precompute_audit_runners.py --staged-only` and stage the resulting
   `logs/runner-cache/` files.

2. **PR CI advisory** (`.github/workflows/audit.yml`)
   Every PR runs a diff-scoped
   `precompute_audit_runners.py --pr-diff <base> --check-only`. The same
   reverse map includes declared-input-only changes. It reports stale caches as
   warnings/job-summary advisories rather than a red check because `main` moves
   continuously and PRs may stay open while review catches up. Review-loop's
   landing gate remains responsible for regenerating caches from current
   `main` before landing.

3. **Audit-runner consumption** (`scripts/codex_audit_runner.py`)
   The audit runner reads cache files only when the runner SHA and any required
   declared-input fingerprint match. A stale cache is treated as if absent,
   and authority-bearing audit calls execute the runner live by default. Those
   live audit calls do not write the canonical cache; intentional refreshes use
   the precompute or cache-first command and the concurrency check below.

## Execution/concurrency binding

Before execution, the cache layer captures the runner SHA and declared-input
fingerprint. After execution it recomputes both. If either identity moved, it
deletes the in-progress log, refuses the canonical cache write, reports an
orchestrator error, and leaves the previous cache stale. When identities agree,
the header is written from the *pre-execution* capture. Therefore an edit in the
small interval after the post-check cannot bind old output to new bytes: the
pre-run header immediately mismatches the edited file.

## Per-runner timeouts

Runners that need more than the default 120s window declare so at the
top of their module:

```python
# scripts/my_heavy_runner.py
AUDIT_TIMEOUT_SEC = 1800   # 30 minutes — basin sweep over 12k seeds
```

The precompute orchestrator and the audit runner both honor this
declaration. Resolution priority:

1. `AUDIT_TIMEOUT_SEC = N` declared at module top of the runner
2. Legacy substring overrides in `runner_cache.TIMEOUT_LEGACY_OVERRIDES`
   (kept as a fallback while runners are progressively annotated)
3. Default 120 seconds

When a runner times out, the cache file records `status: timeout` and
`timeout_sec: <ceiling>` so an auditor reading it can see the timeout
was hit and either return `COMPUTE_REQUIRED` or accept that the runner
is genuinely slow and the recorded tail is partial. The remedy when
that's wrong is either:

- annotate the runner with a higher `AUDIT_TIMEOUT_SEC` and refresh, or
- speed up the runner (often the right answer for heavy exploration scripts).

## Live monitoring during a precompute pass

While `precompute_audit_runners.py` is executing, each in-flight runner
streams its merged stdout+stderr to a live log at:

```
logs/runner-cache/.in-progress/<runner-stem>.txt
```

You can `tail -F` any of those files to watch a runner make progress
mid-execution. The live log is replaced by the canonical cache file
when the runner completes, and the `.in-progress/` directory is
gitignored.

The orchestrator also prints heartbeats every 30 seconds for runners
that have been alive longer than 60 seconds:

```
[heartbeat] 3 runner(s) > 60s in flight:
   180s    14213b  frontier_alpha_s.py
   125s     2018b  ALT_CONNECTIVITY_FAMILY_BASIN.py
    65s        0b  some_stuck_runner.py     # 0 bytes after 65s = suspicious
```

A runner that emits 0 bytes for a long time is either doing pure CPU
work (sympy simplify, eigendecomposition, etc.) or stuck. Open the live
log to tell which.

## Refresh commands

```bash
# Refresh all stale caches in the audit queue (default — fastest path)
python3 scripts/precompute_audit_runners.py

# Cover the full ledger, not just queue
python3 scripts/precompute_audit_runners.py --all

# Refresh runners selected by staged runner or declared-input changes
python3 scripts/precompute_audit_runners.py --staged-only

# Specific runners by path
python3 scripts/precompute_audit_runners.py \
    --runners scripts/foo.py,scripts/bar.py

# Dry verification (CI gate behavior; exit 1 if any stale)
python3 scripts/precompute_audit_runners.py --all --check-only

# Re-run even fresh caches
python3 scripts/precompute_audit_runners.py --force

# Delete cache files for runners that no longer exist
python3 scripts/precompute_audit_runners.py --cleanup-orphans
```

## Implementation files

| File                                          | Role                                          |
| --------------------------------------------- | --------------------------------------------- |
| `scripts/runner_cache.py`                     | Shared module: identities, paths, format, execution binding |
| `scripts/precompute_audit_runners.py`         | Refresh tool and changed-input reverse selector |
| `scripts/cached_runner_output.py`             | Cache-first stdout command for analysis work  |
| `scripts/codex_audit_runner.py`               | Reads cache via `runner_cache.cache_excerpt_for_audit` |
| `docs/audit/scripts/pre_commit_audit_check.sh`| Pre-commit gate                               |
| `.github/workflows/audit.yml`                 | CI gate                                       |
| `docs/audit/templates/audit_workflow.yml`     | Template for the workflow file                |

## Bypass

`git commit --no-verify` skips the local hook. The PR check is advisory, so it
is not an enforcement substitute. Review-loop must still reject or refresh any
stale selected cache before landing; audit consumption independently refuses a
cache whose current identities do not match.
