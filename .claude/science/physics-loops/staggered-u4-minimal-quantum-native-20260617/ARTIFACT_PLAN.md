# Artifact Plan

- Source note: split current minimal-Quantum carrier from abstract Cl(3) representation surface; add `minimal_axioms` as load-bearing dependency; remove stale live-framework non-closure wording.
- Runner: add source guards and current one-qubit carrier checks while retaining `k >= 2` abstract counterexamples.
- Cache: refresh runner output.
- Verification: runner, cache check, py_compile, dependency/stale-wording grep, and `git diff --check`.
