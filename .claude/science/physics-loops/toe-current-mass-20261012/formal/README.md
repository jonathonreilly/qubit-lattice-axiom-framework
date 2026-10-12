# Scoped Lean certificate: finite total-mass threshold

`MassThreshold.lean` compiled successfully with Lean 4.35.0-rc4 and the
previously installed mathlib revision
`939d5d5d9e6f07d1d8c80a16fa3fa39a7518b716`. For an arbitrary finite family,
nonnegative energies and individual inequalities `e_i²-u_i² >= m²` imply
`(sum e_i)²-(sum u_i)² >= (cardinality*m)²`. Taking `u_i=v*p_i` matches the
finite-sector algebraic step in M6–M7 of the pinned current-mass note.

The proof derives the pair bound from those hypotheses and sums every cross
term. It does not assume the pair bound as a replacement premise. Five
declarations, including the polynomial identity and two exact counterexamples,
print only `propext`, `Classical.choice`, and `Quot.sound`; the successful
certificate contains no `sorryAx` or added physical axiom.

The first compilation failed on token spacing and a missing finite-sum import.
Its exact source and complete diagnostics remain under `logs/attempt01`.
The corrected attempt is `logs/attempt02`, with a separate full outer receipt.
The two first false-implication controls timed out concurrently at their actual
120-second limits, yielding no logical conclusion. The preserved sequential
refinement uses both unchanged false propositions together, an explicit real
import, and a 240-second compiler limit. It exited 1 with an unsolved `False`
goal for each proposition. That rejection complements the successful exact
counterexample declarations; a timeout was never counted as a rejection.

This is root-authored formalization and scoped kernel checking, not an
independent reconstruction of the surrounding physics. It does not formalize
the dispersion, infinite Fock sums, maximal domains, null thresholds, filter
limits, almost locality, or the all-n boost differential identity M13. The
separate analytic source review covers those arguments. It confers no retained
audit status. First-attempt outer process capture was not separately stored;
the complete inner source/streams/receipt and tool transcript were preserved.

`SEAL.json` binds the exact sources, emitted object, all five compiler attempts,
their complete available inner/outer streams and runtime records. Generated
caches and temporary files are excluded. No compiler/library update occurred.


## Publication reproduction and archival paths

This README and the four human-readable Lean sources are copied from the sealed root formalization. The complete original directory is preserved by the packet evidence map, including the 266112-byte successful MassThreshold.olean (SHA-256 `76a5a6e63b2d696c6cce53ab8c390eff2efe80a6092e75bc99a7bbd9b4d9c7e5`), all available inner/outer execution records, failed source snapshots and complete diagnostic streams, including empty streams. The archive is not a Lean installation.

The successful recorded compiler argv was:

```text
/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011/lean_audit/lean-4.35.0-rc4-darwin_aarch64/bin/lake env lean -R /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011/current_mass_filter_lean /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011/current_mass_filter_lean/MassThreshold.lean -o /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011/current_mass_filter_lean/MassThreshold.olean
```

Its cwd, six environment overrides, runtime binary/toolchain/manifest hashes and exact version are in the unchanged SEAL and execution receipt. Reproduction requires that pinned Lean and mathlib installation and the preserved original sources; merely opening this packet does not reproduce compilation. Restore into a separate directory and adapt only source/output paths after review; never overwrite the sealed logs. The publication verifier checks source/object/diagnostic identities without invoking Lean, Lake, installation or network access.
