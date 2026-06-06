# Beta=6 SU(3) Wilson Single-Plaquette Resummation-Ansatz Frontier Verdict

**Original date:** 2026-05-30
**Current-frontier repair:** 2026-06-06
**Claim type:** bounded_theorem (methodology / ansatz-verdict harness)
**Status authority:** independent audit lane only. This source note does not
set an audit verdict or effective status.
**Primary runner:** [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)
**Cached runner output:** [`logs/runner-cache/frontier_beta6_resummation_ansatz_test_2026_05_30.txt`](../logs/runner-cache/frontier_beta6_resummation_ansatz_test_2026_05_30.txt)

## Scope

This note repairs the old 2026-05-30 test harness after the beta=6 exact
coefficient frontier moved. The old note used a single-coefficient physical
series and said the ansatz tests were waiting on exact `d_6`. That state is
stale. The current source runner now consumes the exact coefficient frontier
exposed by the current beta=6 packets:

```text
d_5  = 1/472392
d_6  = 7/5668704
d_7  = 5/17006112
d_8  = 5/272097792
d_9  = -2035/264479053824
d_10 = -10483/5289581076480
d_11 = -13/3967185807360
```

This remains a bounded methodology/result note. It does not close beta=6,
derive `<P>(6)`, prove a physical value bound, repin `u_0` or `alpha_s`, or use
the Monte-Carlo comparator as a derivation input.

## Live Runner Result

The repaired runner recomputes the retained single-plaquette baseline
`P_1plaq(6) = 0.42253173965`, validates the d-log-Pade machinery on a controlled
complex-pair proxy, then performs live leave-one-out ansatz tests against
`d_5..d_11`. The current cached scorecard is:

```text
SCORECARD: PASS=28 FAIL=0
```

The strong-coupling partial sum through `d_11` is diagnostic only:

```text
Delta_{5..11}(6) = -0.0113206828227
P_1plaq(6) + Delta_{5..11}(6) = 0.411211056827
```

This is not a closure and is not a physical value estimate.

## Tadpole / Geometric Verdict

The tadpole / boosted-PT single-ratio pattern is no longer waiting; it is
falsified by the current exact coefficients. The consecutive ratios are:

```text
d_6/d_5   = 0.583333333333
d_7/d_6   = 0.238095238095
d_8/d_7   = 0.0625
d_9/d_8   = -0.418724279835
d_10/d_9  = 0.257567567568
d_11/d_10 = 0.00165347069859
```

The runner's leave-one-out tests miss every target `d_7..d_11` outside the 5%
support window. The decisive sign witness is `d_9`: the single-ratio prediction
from `d_7,d_8` is positive, while exact `d_9` is negative.

The bare single-plaquette tadpole fixed-point checks also remain non-closing:
`beta_eff = beta * <P>` collapses to the trivial `P=0` branch, the over-boost
convention lands at `P = 0.61152284`, and the `z=6` mean-field /
Drouffe-Itzykson branch reproduces the blocked `P_1plaq(31.5) = 0.87418441`.

## d-log-Pade Verdict

The d-log-Pade predictive test is active, but not support-stable:

```text
d_5..d_8  -> predict d_9:  FALSIFY, rel = 0.3692
d_5..d_9  -> predict d_10: SUPPORT, rel = 0.04514
d_5..d_10 -> predict d_11: FALSIFY, rel = 4.578
```

The `[2/2]` d-log-Pade singularity diagnostic from `d_5..d_10` gives
`|beta_c| = 5.38609`, `arg = -1.23374`, which remains useful complex-pair
radius evidence. It is not a proof of the true analytic continuation or a
beta=6 value theorem.

## Current Padé Continuation Spread

Using the seven exact coefficients in
`B(beta) = Delta(beta) / (d_5 beta^5)`, the runner recomputes:

```text
[2/3] -> <P>(6) = 0.589858288711
[3/2] -> <P>(6) = 0.519085410577
[3/3] -> <P>(6) = 0.537903702672
[2/4] -> <P>(6) = 0.514032402651
[4/2] -> <P>(6) = 0.528316216587
```

The full spread is `0.5140324 .. 0.58985829`; the highest-order
`[3/3],[2/4],[4/2]` cluster is `0.5140324 .. 0.5379037`. Therefore the
seven-coefficient continuation is ambiguous and not converged to `0.5934`.

## Boundaries

- `0.594` / `0.5934` is a Monte-Carlo comparator only, never a fit or proof
  input in this harness.
- The current exact coefficients are consumed as the current beta=6 frontier
  packet; their own independent audit status remains separate.
- The runner evaluates and falsifies/support-tests ansaetze against the current
  coefficient frontier; it does not derive a physical beta=6 plaquette value.
- No new axiom, carrier convention, or hidden external physics premise is
  introduced.

## Key Files

- [`scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py`](../scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)
- [`BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md)
- [`BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md)
- [`BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md)
- [`BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md)
