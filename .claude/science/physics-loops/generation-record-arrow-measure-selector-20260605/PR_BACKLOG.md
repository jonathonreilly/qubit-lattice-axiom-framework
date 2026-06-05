# PR Status

Opened and verified:
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2705

## Title

[physics-loop] generation record arrow measure selector bounded-support

## Body summary

Adds a bounded theorem for the arrow/measure gate. On the two-letter
generation Record alphabet with dimensions `(1,2)`, a supplied prior
`pi_gamma proportional to dim^gamma` and relative-entropy ascent stabilize the
exact generation dial at `s=gamma`.

Endpoint results:

- `gamma=0` record-letter/block-count prior -> `s=0`, `r=1/2`, `Q=2/3`.
- `gamma=1` dimension/Born prior -> `s=1`, `r=1`, `Q=1`.

Runner:

- `python3 scripts/generation_record_arrow_measure_selector_2026_06_05.py`
  with PASS=21 FAIL=0.

This does not derive physical `gamma=0`. It isolates the remaining
charged-lepton value gate as the choice of record-letter prior over
dimension/Born prior.
