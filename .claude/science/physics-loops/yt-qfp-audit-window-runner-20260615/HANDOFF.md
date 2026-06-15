# Handoff

This PR repairs the compute side of the YT QFP audit lane.

What changed:

- The default runner is now an audit-window certificate that completes quickly.
- The historical dense ODE sweep is still available with `--full-sweep`.
- The note's numerical-verification section records that distinction.

What did not change:

- No audit verdicts or generated audit-status surfaces were edited.
- The claim remains bounded support.
- The remaining science gap is the independent lattice taste-staircase RG
  envelope theorem, if the project wants to pursue promotion later.

Verification:

```sh
python3 scripts/frontier_yt_qfp_insensitivity.py
```

Expected result: `Tests: 14 PASS, 0 FAIL`.
