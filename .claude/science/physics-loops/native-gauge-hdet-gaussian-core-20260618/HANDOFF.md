# Handoff

This PR adds upstream source-side support for the native gauge determinant
blocker:
`native_gauge_transfer_weyl_determinant_assembly_rung_ten_bounded_note_2026-06-12`.

Changed source packet:

- Adds `NATIVE_GAUGE_TRANSFER_HDET_GAUSSIAN_CORE_SUPPORT_NOTE_2026-06-18.md`.
- Adds `scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py`
  and its runner cache.
- Wires the existing Weyl-determinant assembly note to cite `H_det_core`.
- Leaves full `H_det(A)`, exact-Bessel `K_W(A)`, determinant tails, and
  `H_spec` open.

Verification:

```text
python3 scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py
TOTAL: PASS=13, FAIL=0

python3 scripts/cached_runner_output.py --check-only scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py
fresh logs/runner-cache/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.txt

python3 -m py_compile scripts/native_gauge_transfer_hdet_gaussian_core_support_2026_06_18.py
git diff --check
```

Reviewer focus:

- Confirm the new support note does not derive or fit `K_W(A)`.
- Confirm the downstream assembly note is wired only to `H_det_core`.
- Confirm `H_det_remainder(A)` and `H_spec` remain explicit blockers.
- Confirm no generated ledgers, publication matrices, lane registry, active
  review queue, or front-door status surfaces are included.
