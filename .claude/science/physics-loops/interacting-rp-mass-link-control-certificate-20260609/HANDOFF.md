# Handoff

Branch: `physics-loop/interacting-rp-mass-link-control-certificate-20260609`

Target claim:
`interacting_rp_full_algebra_fixed_a_gauge_invariant_four_fermion_bounded_note_2026-06-05`

What changed:

- Added `scripts/frontier_interacting_rp_mass_link_reflection_controls_2026_06_09.py`.
- The companion source-hash-pins
  `scripts/frontier_interacting_rp_full_algebra_2026_06_05.py`.
- It verifies the SU(3) full-algebra mass scan through `m = 0.01`.
- It verifies the non-conjugating link-reflection convention breaks Hermiticity
  and PSD while the correct reflected Gram remains PSD.
- The source note now links the companion runner/cache.
- The companion cache reports `TOTAL: PASS=4 FAIL=0`.

Verification:

```text
python3 scripts/frontier_interacting_rp_mass_link_reflection_controls_2026_06_09.py
TOTAL: PASS=4 FAIL=0

python3 scripts/cached_runner_output.py scripts/frontier_interacting_rp_mass_link_reflection_controls_2026_06_09.py
status: ok
```

Remaining boundary:

The branch does not claim continuum/OS-reconstruction or compact-group
Wilson-boundary positivity. Those remain out of scope as in the original note.

Next action:

Review-loop landing supplies the reviewer extraction. The remaining action is
independent re-audit of the changed source note. Do not edit `docs/audit/**` by
hand.
