# Artifact Plan

## Block16

- Add a source note recording the theta-to-slice `rho_E` dependency firewall.
- Add a runner deriving exact source factors and checking the semigroup
  propagation envelope.
- Cache the runner output.
- Add loop pack checkpoint files.
- Run focused checks only; do not audit, apply verdicts, push to `main`, or
  check PR conflict state.
- Open one review PR for the science block.
