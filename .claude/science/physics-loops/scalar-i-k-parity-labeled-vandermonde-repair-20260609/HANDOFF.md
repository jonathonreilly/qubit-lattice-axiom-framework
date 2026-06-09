# Handoff

Branch: `physics-loop/scalar-i-k-parity-labeled-vandermonde-repair-20260609`

Target claim:
`scalar_i_and_real_generation_structure_k_parity_separation_bounded_note_2026-06-08`

What changed:

- Replaced the sorted-eigenvalue Vandermonde check with the labeled generation
  Vandermonde from the cited orientation note.
- The runner now shows `Delta(+delta)=+0.04674385` and
  `Delta(-delta)=-0.04674385`, so the labeled orientation is K-odd.
- The sorted-spectrum discriminant remains as a K-even multiset control only.
- The source note is narrowed to scalar-`i` phase data versus real `J_cs`
  complex-structure data.
- Runner cache was refreshed to `TOTAL: PASS=9 FAIL=0`.

Verification:

```text
python3 scripts/frontier_scalar_i_real_generation_k_parity_separation.py
TOTAL: PASS=9 FAIL=0

python3 scripts/cached_runner_output.py scripts/frontier_scalar_i_real_generation_k_parity_separation.py
status: ok
```

Remaining boundary:

This branch does not derive realized handedness, a selector, probability rule,
or any empirical value. It only corrects the finite K-parity separation surface.

Next action:

Open a PR for reviewer extraction and independent re-audit. Do not edit
`docs/audit/**`.
