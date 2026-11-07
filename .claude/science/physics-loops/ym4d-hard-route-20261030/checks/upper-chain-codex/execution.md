# Execution record

Pinned source: 0cad38f3644a6749b0e4a5782335744bc1f45732.
The part file is the current checkpoint; this file records execution only.

`criteria.md` was written before the numerical run. The missing
`scripts/automation_lock.py` was retrieved byte-for-byte with
`git show HEAD:scripts/automation_lock.py` into this directory and made
available through PYTHONPATH; no file in scripts/ was changed. Bytecode
writing was disabled. The workflow was read from the same pinned Git
revision because it is absent from the sparse worktree. This was a bounded
task under the user's explicit no-commit, no-PR, no-audit and no-subagent
instructions, not a campaign or a backlog drain.

Preflight returned `go`; its complete output is `preflight.txt`. The
numeric lock returned `acquired` for holder `upper-chain-codex-0cad38f36`
before launching any check, and `released` afterwards. Both receipts are
saved here. Preflight reported 32% memory free on this MacBook; the 50%
threshold specified for the Mac mini does not apply to this machine.

The first launch exited before any mathematical check because the OS
rejected RLIMIT_AS with `ValueError: current limit exceeds maximum limit`.
The complete traceback is preserved in `history-stderr.txt`. The script
was then changed to report unavailable address-space enforcement and to
enforce the 2 GiB RSS limit itself, through a periodic signal and
per-trajectory checks. Thus the registered OS address-space cap was not
available; the RSS limit was enforced by the script. The completed run
reported peak RSS 16,351,232 bytes. It ran with `nice -n 10`, no process
pool, and OPENBLAS_NUM_THREADS, OMP_NUM_THREADS, MKL_NUM_THREADS,
VECLIB_MAXIMUM_THREADS and NUMEXPR_NUM_THREADS all set to 1.

The completed command was:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
nice -n 10 python3 \
.claude/science/physics-loops/ym4d-hard-route-20261030/checks/upper-chain-codex/check_history.py
```

`history-results.json` is its complete stdout. The finite positive history
expansion and domination were exact; 42 individual Jensen inequalities
held by rational arithmetic. The bounded-copy fourth-moment ratio was
65536 at each of three steps, hence norm ratio 16. At depth 1000 the
radius diagnostic gave log R = 460.1026131863838 and lambda/5 = 22.0.
The two logarithmic diagnostics use floating point; the symbolic slope
calculation in the library is the proof of that parameter issue.

These tests do not prove (H20.5), Wilson rarity or the cumulant bound.
The source-bound and centering derivations in the library were checked
algebraically, not by a Wilson simulation. No existing physics runner,
old numerical result or PASS line was rerun or adopted as new evidence.

The gate's findings 1–6 and needed upper-chain definitions and consumers
were read in bounded ranges. Searches of parts/ and library/ identified
the direct consumers. Only statement snippets from the mapped attempt
were encountered; neither hard-core proof was read, and no proof text
was transferred between attempts. The additional interface gate files,
mapped Requests entry, and Theorem DM consumer section were not absorbed:
the ordered task stopped in step 1. No I(k;D) file or marked Lemma 22.2
was created. Text corrections to the probability-mixture convention,
factor two and finite union were necessary prerequisites, not completion
of step 3.

`scope-check.json` records source identities, the allowed-path check and
hash equality for Lemmas 20.3, 22.1, 22.2 and Proposition 20.4. Those
statements were not modified. `git diff --check` passed. No commit, push,
PR, posting, audit, axiom edit, ledger edit, prompt edit or subagent ran.
