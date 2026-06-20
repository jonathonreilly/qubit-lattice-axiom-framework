# Gauge-Vacuum Plaquette Word-Count Rescaled Tail Support Note

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py`](../scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py)
**Cached output:** [`logs/runner-cache/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.txt`](../logs/runner-cache/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.txt)

This note adds source-side bounded support for the finite-packet word-count
all-k remainder lane. It does not close the all-k bridge, does not set an
audit status, and does not alter the finite-packet boundary:

```text
tensor NMAX = 4, tensor MODE_MAX = 80,
source NMAX = 7, source MODE_MAX = 200,
matrix-element same-label adjacent bond,
eta_inf boundary.
```

Its role is to remove one concrete obstruction in the parent row: the existing
double-precision path loses the post-leading correction around `k = 20` because
the residual is obtained as a small difference after the leading
`theta^(k-1)` slice is subtracted. The new runner recomputes the same finite
packet with the dominant channel scaled out and uses high-precision symmetric
eigenvectors for the tail rows.

## Inputs

- [`GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_POWER_BLOCK_BIRKHOFF_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md`](GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_POWER_BLOCK_BIRKHOFF_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the finite entrywise-power packet.
- [`GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md`](GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md)
  supplies the theta identity, paired source coefficient, and source
  asymptotic inputs.
- The all-k remainder certificate is the downstream target that consumes this
  support. It is not a load-bearing input to this note.

## What the support runner checks

Let

```text
x_k - chi_pair = theta^(k-1) sigma_slice + e_k.
```

The parent certificate currently uses a finite-window constant

```text
q_l1_alpha_constant =
  max_{2 <= k <= 18} ||e_k||_1 / alpha^k
  = 56.64730598492354,
```

with the maximum occurring at `k = 2`. The new support runner verifies:

1. The finite-packet scale ordering is unchanged:
   `theta * alpha > theta * gamma` and `theta * alpha > theta^2`.
2. The old finite-window constant is reproduced on the existing double path.
3. The high-precision rescaled path agrees with the existing double path on
   stable rows `k = 2, 10, 18`.
4. The double path loses the tail at `k = 20`; the high-precision path recovers
   the expected post-leading correction.
5. The sampled high-precision tail rows are monotone decreasing in
   `||e_k||_1 / alpha^k` and remain below `4.05`.

The high-precision tail sample is:

```text
k = 19: q_l1 = 3.91641238973101321e-6,  q_l1 / alpha^k = 4.03317129516350649
k = 20: q_l1 = 1.87939769580492291e-6,  q_l1 / alpha^k = 4.01086368815541409
k = 24: q_l1 = 1.00410457916496004e-7,  q_l1 / alpha^k = 3.95222810809581134
k = 30: q_l1 = 1.25566173623093168e-9,  q_l1 / alpha^k = 3.91472697818150262
k = 36: q_l1 = 1.57966298824259254e-11, q_l1 / alpha^k = 3.90084797305440686
k = 40: q_l1 = 8.52234005296532082e-13, q_l1 / alpha^k = 3.88147938506695016
```

These rows are far below the finite-window envelope from `k = 2`, and they
show that the apparent collapse of `e_k` in double precision is numerical
cancellation rather than a source-theorem fact.

## What remains open

The analytic monotone/Neumann tail proof remains open. To turn this support
artifact into a full all-k bridge, a later source note still has to prove, on
the same finite packet, that the rescaled tail ratio cannot rebound after the
sampled high-precision window. A suitable proof target would be an explicit
Neumann-series or block-resolvent bound for the reduced entrywise-power matrix
that controls `||e_k||_1 / alpha^k` for every later `k`.

This note therefore supplies bounded support for the all-k repair route:
the tail has the expected third-scale behavior in a high-precision window, and
the remaining blocker is now the analytic uniform-tail proof rather than a
double-precision artifact.

## Verification

Run:

```bash
python3 scripts/gauge_vacuum_plaquette_word_count_rescaled_tail_support_2026_06_18.py
```

Expected final line:

```text
TOTAL: PASS=14, FAIL=0
```
