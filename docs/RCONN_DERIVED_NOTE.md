# R_conn Matching-Rule No-Go With Exact Fierz Support

**Date:** 2026-04-14; matching-rule no-go repair 2026-05-26
**Runner:** `scripts/rconn_matching_rule_nogo_certificate.py`
**Claim type:** no_go
**Status:** exact Fierz/channel-count support plus a bounded no-go for
deriving the physical connected-trace selector from the current packet.

## Scope

Earlier versions of this note used the symbol `R_conn` for the physical
lattice connected-trace readout and then identified it with the exact
SU(3) adjoint channel fraction `8/9`. Audit correctly found that the
identification is not derived by the packet. The exact algebra is real:
for SU(`N_c`),

```text
F_adj = dim(adj) / dim(N_c x N_c-bar) = (N_c^2 - 1) / N_c^2.
```

At `N_c = 3`, `F_adj = 8/9`. What does not follow from that algebra is the
physical readout rule that discards or absorbs the singlet/disconnected
channel in the EW-current observable.

This repair retires the unconditional physical-readout claim. It preserves
the exact Fierz support and states the current no-go boundary:

```text
R_phys(kappa_EW) = F_adj + kappa_EW (1 - F_adj)
K_EW(kappa_EW) = 1 / R_phys(kappa_EW)
```

The connected-trace specialization is `kappa_EW = 0`, giving
`K_EW(0) = 9/8`. The full-trace specialization is `kappa_EW = 1`, giving
`K_EW(1) = 1`. Both completions satisfy the exact Fierz arithmetic and the
same color-blind CMT scaling. Therefore the current packet does not derive
the selector `kappa_EW = 0`.

No new axiom, fitted selector, or audit verdict is introduced.

## Binding Claim

On the current retained/support surface available to this row:

1. The SU(`N_c`) Fierz completeness identity is exact.
2. The Hilbert-space adjoint fraction is exactly
   `(N_c^2 - 1) / N_c^2`; at `N_c = 3` this is `8/9`.
3. The physical EW-current readout has a free disconnected-channel
   coefficient `kappa_EW`.
4. CMT mean-field scaling multiplies connected and singlet channels by the
   same factor, so it cannot select `kappa_EW`.
5. OZI-style bounded suppression supplies a size class for the singlet
   channel, not an exact coefficient.
6. The two completions `kappa_EW = 0` and `kappa_EW = 1` agree on the
   Fierz algebra and CMT scaling but disagree on `K_EW`. The selector is
   therefore underdetermined by the current packet.

This is a no-go for unconditional `R_conn = 8/9` as a physical readout
claim. The exact `8/9` support remains available as `F_adj`, not as a
derived connected-trace observable.

## What The Old MC Check Means

The legacy MC runner `scripts/frontier_color_projection_mc.py` compared a
Monte Carlo connected-trace estimate with the analytic `8/9` target. That is
a consistency check after choosing the connected-trace target; it is not a
derivation of the target or of `kappa_EW = 0`.

This repaired row uses the dedicated runner above as the binding artifact.
The old MC check is retained only as diagnostic context.

## What This Note Does Not Claim

- It does not claim that the physical connected-trace readout is derived.
- It does not claim an unconditional package coefficient `K_EW = 9/8`.
- It does not use numerical agreement to fit or ratify `kappa_EW = 0`.
- It does not add a new axiom or select a new convention.
- It does not apply an audit verdict.

## Runner Certificate

The runner verifies:

- normalized SU(`N`) generators and the Fierz completeness identity for
  `N = 2, 3, 4, 5`;
- the exact adjoint fractions, including `F_adj = 8/9` at `N_c = 3`;
- `K_EW(0) = 9/8`, `K_EW(1) = 1`, and the fact that the two completions
  share the same Fierz/CMT premises;
- CMT scaling invariance for several nonzero scale factors and multiple
  `kappa_EW` values;
- bounded OZI-size behavior without coefficient selection; and
- source-note hygiene for this no-go boundary.

Expected local certificate:

```text
RUNNER STATUS: PASS (PASS=30 FAIL=0)
```

## Reopen Conditions

Reopen the physical `R_conn = 8/9` readout only with a retained-grade
lattice-current selector theorem or an exact disconnected-current
coefficient computation that fixes `kappa_EW = 0` from accepted primitives.
Until then, downstream uses of `9/8` must be written as the conditional
connected-trace specialization `K_EW(0)`.
