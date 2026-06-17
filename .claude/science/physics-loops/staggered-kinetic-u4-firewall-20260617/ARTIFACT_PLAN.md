# Artifact Plan

- Source note: remove U4 as a load-bearing markdown authority and from the YAML `upstream_dependencies`; keep U4 as plain-text provenance.
- Runner: add a source dependency guard that fails if the U4 markdown dependency or YAML upstream dependency reappears.
- Cache: refresh `logs/runner-cache/staggered_dirac_kinetic_class_forcing_check_2026_06_10.txt`.
- Verification: run the claim runner, cache check, py_compile, dependency-edge grep, and diff whitespace check.
