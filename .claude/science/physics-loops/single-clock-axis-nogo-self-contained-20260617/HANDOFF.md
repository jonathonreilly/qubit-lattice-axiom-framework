# Handoff

Branch: `physics-loop/single-clock-axis-nogo-self-contained-20260617`

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4204

This PR makes the single-clock axis-selection no-go packet self-contained for
auditability. It removes load-bearing direct source consumption of the
conditional parent single-clock source, the external finite-speed cone note,
the downstream anomaly row, and setup-convention example rows.

Science preserved:

- `W = P_{tau<->1} diag((-1)^{x_tau x_1})` exchange certificate is recomputed.
- OS/GNS reconstruction data transports exactly.
- Record durability is operator-order monotonicity and is unitary-transport
  invariant.
- Finite-speed registration-cone slice package transports exactly.
- Chirality is W-invariant; count-only routes cannot select an axis label.
- Per-axis BC asymmetry is sufficient and minimal on this tested surface, but
  is not derived here.

Verification run:

```bash
python3 scripts/single_clock_axis_selection_check_2026_06_11.py
python3 scripts/cached_runner_output.py --check-only scripts/single_clock_axis_selection_check_2026_06_11.py
python3 -m py_compile scripts/single_clock_axis_selection_check_2026_06_11.py
git diff --check
```

Additional local check: a source-edge grep for the removed direct-file tokens
returns no matches in the note, runner, and loop pack.

Reviewer-owned next step: review-loop/reviewer extraction, then independent
audit lane may decide whether this source packet is auditable and accepted.
