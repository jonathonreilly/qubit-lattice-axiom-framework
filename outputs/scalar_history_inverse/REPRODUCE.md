# Reproduce the scalar-history milestone

Use Python 3.12.8 and SymPy 1.14.0 for byte-identical receipts. From the repository
root, the primary source-bound controls are:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/scalar_history_inverse.py
```

The repository's runner_cache envelope supplies the declared 120-second bound
when generating the canonical cache. The committed cache records that bounded
execution. The standalone command above does not itself enforce a wall timeout.

The portability wrapper below enforces 120 seconds on each subprocess and runs
the frozen programs only in temporary copies. It reproduces the independent
pre-exposure mathematics, independent additions, both historical author
versions and the current primary. Expected historical v1 failures remain failures.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B outputs/scalar_history_inverse/replay_bundle.py
```

Its five cases compare output bytes. It writes portable_replay.json beside
itself, leaving the closed independent bundle unchanged. This wrapper was
written by root and is a portability check, not an independent derivation.
The focused checker's separate source-root-explicit integration replay and
disposable-directory instructions are in
[REPRODUCTION_v1.md](independent/REPRODUCTION_v1.md).

To reproduce the ten mutation challenges in isolated temporary copies:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -B outputs/scalar_history_inverse/check_mutations.py
```

All data in these commands are exact constructed mathematical fixtures. No
observational record, calibration set, holdout or empirical validation enters.
